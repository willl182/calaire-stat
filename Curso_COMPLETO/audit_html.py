#!/usr/bin/env python3
"""Convierte los audit_*.md en páginas HTML autocontenidas con diseño propio.

Uso: python3 audit_html.py audit_a.md audit_b.md audit_c.md
Cada salida se escribe junto al .md con extensión .html.
"""
import html
import re
import sys
import unicodedata
from pathlib import Path

FIND_RE = re.compile(r"^(H\d+)\s*·\s*(.+?)\s+—\s+(P\d)(?:,\s*(.+))?$")
LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
TABLE_SEP_RE = re.compile(r"^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?$")
FIELD_RE = re.compile(r"^\*\*([^*]{2,60}?):\*\*\s*(.*)$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)")
BOLD_RE = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*(?!\*)")
ITAL_RE = re.compile(r"(?<![\w*])\*(?=\S)([^*]+?)(?<=\S)\*(?![\w*])")
CODE_RE = re.compile(r"`([^`]+)`")
PLACEHOLDER_RE = re.compile("\x00(\\d+)\x00")

# Etiquetas que marcan una acción concreta y se muestran como bloque destacado.
FIX_LABELS = {"Cambio", "Cambio propuesto", "Corrección", "Corrección requerida", "Práctica aplicada"}

SEV_LABEL = {"P1": "Corregir antes de impartir", "P2": "Completar antes de publicar", "P3": "Mejora"}


# ---------------------------------------------------------------- inline

def esc(text):
    return html.escape(text, quote=False)


def fmt(text):
    text = BOLD_RE.sub(r"<strong>\1</strong>", text)
    return ITAL_RE.sub(r"<em>\1</em>", text)


def inline(text):
    # Enlaces y código se guardan aparte para que el énfasis pueda cruzarlos.
    store = []

    def keep(html_fragment):
        store.append(html_fragment)
        return f"\x00{len(store) - 1}\x00"

    text = LINK_RE.sub(
        lambda m: keep(f'<a href="{html.escape(m.group(2), quote=True)}">{inline(m.group(1))}</a>'),
        text,
    )
    text = CODE_RE.sub(lambda m: keep(f"<code>{esc(m.group(1))}</code>"), text)
    out = fmt(esc(text))
    return PLACEHOLDER_RE.sub(lambda m: store[int(m.group(1))], out)


def plain(text):
    text = LINK_RE.sub(r"\1", text)
    return re.sub(r"[*`]", "", text).strip()


def slugify(text, used):
    norm = unicodedata.normalize("NFKD", plain(text)).encode("ascii", "ignore").decode()
    base = re.sub(r"[^a-z0-9]+", "-", norm.lower()).strip("-") or "seccion"
    slug, n = base, 2
    while slug in used:
        slug = f"{base}-{n}"
        n += 1
    used.add(slug)
    return slug


# ---------------------------------------------------------------- parse

def split_row(line):
    # Un "|" dentro de `código` no separa celdas.
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    cells, cur, in_code = [], [], False
    for ch in line:
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    cells.append("".join(cur).strip())
    return cells


class Node:
    def __init__(self, text="", ordered=False):
        self.text = text
        self.ordered = ordered
        self.children = []


def parse_list(lines, i, blocks):
    items = []  # [indent, ordered, text]
    n = len(lines)
    while i < n:
        line = lines[i]
        m = LIST_RE.match(line)
        if m:
            items.append([len(m.group(1).expandtabs(4)), m.group(2)[0].isdigit(), m.group(3).strip()])
            i += 1
            continue
        if not line.strip():
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            if items and j < n and (LIST_RE.match(lines[j]) or lines[j].startswith(" ")):
                i = j
                continue
            break
        if line.startswith(" ") and items:
            items[-1][2] += " " + line.strip()
            i += 1
            continue
        break

    root = Node()
    stack = [(-1, root)]
    for indent, ordered, text in items:
        while stack[-1][0] >= indent:
            stack.pop()
        node = Node(text, ordered)
        stack[-1][1].children.append(node)
        stack.append((indent, node))
    blocks.append(("list", root.children))
    return i


def parse(md):
    lines = md.splitlines()
    blocks, para = [], []
    n, i = len(lines), 0

    def flush():
        if para:
            blocks.append(("p", " ".join(s.strip() for s in para)))
            para.clear()

    while i < n:
        line = lines[i]
        s = line.strip()
        if not s:
            flush()
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            flush()
            blocks.append(("h", len(m.group(1)), m.group(2).strip()))
            i += 1
            continue
        if re.fullmatch(r"-{3,}|\*{3,}", s):
            flush()
            blocks.append(("hr",))
            i += 1
            continue
        if s.startswith("|") and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1].strip()):
            flush()
            header = split_row(s)
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            blocks.append(("table", header, rows))
            continue
        if LIST_RE.match(line):
            flush()
            i = parse_list(lines, i, blocks)
            continue
        if para and FIELD_RE.match(s):
            # Una etiqueta «**Objeto:**» al inicio de línea abre párrafo nuevo.
            flush()
        para.append(line)
        i += 1
    flush()
    return blocks


# ---------------------------------------------------------------- render

def render_list(children):
    tag = "ol" if children[0].ordered else "ul"
    items = []
    for node in children:
        sub = render_list(node.children) if node.children else ""
        items.append(f"<li>{inline(node.text)}{sub}</li>")
    return f"<{tag}>" + "".join(items) + f"</{tag}>"


def render_table(header, rows):
    cols = len(header)
    head = "".join(f"<th>{inline(c)}</th>" for c in header)
    body = []
    for r in rows:
        r = (r + [""] * cols)[:cols]
        body.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    return (
        f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead>'
        f"<tbody>{''.join(body)}</tbody></table></div>"
    )


def render_field(label, rest):
    cls = "field fix" if label in FIX_LABELS else "field"
    return f'<p class="{cls}"><span class="k">{esc(label)}</span> {inline(rest)}</p>'


def build(blocks, source):
    used = set()
    toc = []  # (level, id, label, sev)
    body = []
    summary_counts = {"P1": 0, "P2": 0, "P3": 0}
    total = 0
    title = source

    for b in blocks:
        if b[0] == "h" and b[1] == 3:
            m = FIND_RE.match(b[2])
            if m:
                total += 1
                summary_counts[m.group(3)] = summary_counts.get(m.group(3), 0) + 1

    section_open = article_open = seen_h2 = False
    header_html = ""

    def close_article():
        nonlocal article_open
        if article_open:
            body.append("</article>")
            article_open = False

    def close_section():
        nonlocal section_open
        close_article()
        if section_open:
            body.append("</section>")
            section_open = False

    for b in blocks:
        kind = b[0]
        if kind == "h":
            level, text = b[1], b[2]
            if level == 1:
                title = plain(text)
                header_html = f"<h1>{inline(text)}</h1>"
                continue
            if level == 2:
                close_section()
                seen_h2 = True
                sid = slugify(text, used)
                toc.append((2, sid, plain(text), None))
                body.append(f'<section id="{sid}"><h2>{inline(text)}</h2>')
                section_open = True
                continue
            m = FIND_RE.match(text) if level == 3 else None
            if m:
                close_article()
                fid, ftitle, sev, tag = m.group(1), m.group(2), m.group(3), m.group(4)
                fid_slug = fid.lower()
                used.add(fid_slug)
                toc.append((3, fid_slug, f"{fid} · {plain(ftitle)}", sev))
                tag_html = f'<span class="tag">{esc(tag)}</span>' if tag else ""
                body.append(
                    f'<article class="finding" id="{fid_slug}">'
                    f'<header class="finding-head"><div class="finding-meta">'
                    f'<span class="fid">{esc(fid)}</span>'
                    f'<span class="badge {sev.lower()}" title="{esc(SEV_LABEL.get(sev, sev))}">{sev}</span>'
                    f"{tag_html}</div><h3>{inline(ftitle)}</h3></header>"
                )
                article_open = True
                continue
            if level == 3:
                close_article()
                sid = slugify(text, used)
                toc.append((3, sid, plain(text), None))
                body.append(f'<h3 id="{sid}">{inline(text)}</h3>')
                continue
            body.append(f"<h{level}>{inline(text)}</h{level}>")
        elif kind == "p":
            text = b[1]
            fm = FIELD_RE.match(text)
            if fm and (article_open or section_open):
                body.append(render_field(fm.group(1).strip(), fm.group(2)))
            elif not seen_h2:
                body.append(f'<p class="lede">{inline(text)}</p>')
            else:
                body.append(f"<p>{inline(text)}</p>")
        elif kind == "list":
            body.append(render_list(b[1]))
        elif kind == "table":
            body.append(render_table(b[1], b[2]))
        elif kind == "hr":
            body.append("<hr>")

    close_section()

    summary = ""
    if total:
        chips = "".join(
            f'<span class="badge {k.lower()}" title="{esc(SEV_LABEL[k])}">{k} · {v}</span>'
            for k, v in summary_counts.items() if v
        )
        summary = (
            f'<div class="summary"><span class="summary-count">{total} hallazgos</span>'
            f"{chips}</div>"
        )

    toc_html = []
    open_sub = False
    for level, tid, label, sev in toc:
        if level == 2:
            if open_sub:
                toc_html.append("</ol></li>")
            toc_html.append(f'<li><a href="#{tid}">{esc(label)}</a>')
            open_sub = True
            toc_html.append('<ol class="sub">')
        else:
            dot = f'<span class="dot {sev.lower()}"></span>' if sev else ""
            toc_html.append(f'<li><a href="#{tid}">{dot}{esc(label)}</a></li>')
    if open_sub:
        toc_html.append("</ol></li>")
    toc_nav = (
        '<nav class="toc" aria-label="Contenido"><p class="toc-title">Contenido</p>'
        '<ol class="top">' + "".join(toc_html) + "</ol></nav>"
    )

    return {
        "title": title,
        "toc": toc_nav,
        "header": header_html + summary,
        "body": "".join(body),
        "source": source,
    }


CSS = """
:root{
  --paper:#fbfaf6; --card:#ffffff; --ink:#1c1e22; --muted:#596070; --faint:#8b909a;
  --rule:#e3dfd5; --wash:#f3f1ea; --accent:#1d5c59; --accent-soft:#e5efed;
  --p1:#9b2226; --p1-bg:#f9e5e3; --p2:#7d4e00; --p2-bg:#fbefd2; --p3:#3f4d66; --p3-bg:#e8ecf3;
  --code-bg:#f0eee7; color-scheme:light;
}
@media (prefers-color-scheme: dark){
  :root{
    --paper:#15171b; --card:#1d2026; --ink:#e7e5df; --muted:#a3a8b3; --faint:#7a808b;
    --rule:#2d3139; --wash:#22252b; --accent:#7fc3bd; --accent-soft:#1d2e2d;
    --p1:#ffb4ab; --p1-bg:#4a1f1c; --p2:#f2c46d; --p2-bg:#41331a; --p3:#b9c6dc; --p3-bg:#262e3b;
    --code-bg:#2a2d34; color-scheme:dark;
  }
}
*{box-sizing:border-box}
html{background:var(--paper)}
body{margin:0;color:var(--ink);background:var(--paper);
  font:17px/1.68 "Charter","Iowan Old Style","Palatino Linotype",Georgia,serif;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
.shell{display:grid;grid-template-columns:276px minmax(0,1fr);max-width:1240px;margin:0 auto}
.sans,.toc,h1,h2,h3,h4,th,.badge,.summary,.field .k,.finding-meta,.fid,.tag{
  font-family:system-ui,-apple-system,"Segoe UI","Noto Sans",sans-serif}

/* índice */
.toc{position:sticky;top:0;height:100vh;overflow-y:auto;padding:36px 22px 40px 26px;
  border-right:1px solid var(--rule);font:14px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif}
.toc-title{margin:0 0 14px;font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--faint)}
.toc ol{list-style:none;margin:0;padding:0}
.toc li{margin:0}
.toc a{display:block;padding:5px 8px;margin:0 -8px;border-radius:6px;color:var(--muted);text-decoration:none}
.toc a:hover{color:var(--ink);background:var(--wash)}
.toc a.on{color:var(--accent);background:var(--accent-soft);font-weight:600}
.toc ol.top>li>a{color:var(--ink);font-weight:600;margin-top:10px}
.toc ol.sub{margin:2px 0 6px 10px;padding-left:8px;border-left:1px solid var(--rule)}
.toc ol.sub a{font-size:13px;line-height:1.35}
.dot{display:inline-block;width:7px;height:7px;border-radius:50%;margin:0 7px 1px 0;vertical-align:middle;background:var(--faint)}
.dot.p1{background:var(--p1)} .dot.p2{background:var(--p2)} .dot.p3{background:var(--p3)}

/* cuerpo */
main{padding:52px 64px 120px;max-width:860px;min-width:0}
h1{font-size:30px;line-height:1.18;letter-spacing:-.015em;font-weight:650;margin:0 0 18px}
h2{font-size:22px;line-height:1.3;font-weight:650;margin:0 0 14px;letter-spacing:-.005em}
h3{font-size:18px;line-height:1.35;font-weight:600;margin:30px 0 10px}
h4{font-size:15px;font-weight:600;margin:24px 0 8px;color:var(--muted)}
section{margin-top:56px;padding-top:28px;border-top:1px solid var(--rule)}
section:first-of-type{margin-top:36px}
p{margin:0 0 14px}
p.lede{font-size:18px;line-height:1.6;color:var(--muted);margin-bottom:10px}
a{color:var(--accent);text-underline-offset:3px;text-decoration-thickness:1px;word-break:break-word}
strong{font-weight:650}
hr{border:0;border-top:1px solid var(--rule);margin:36px 0}
ul,ol{padding-left:1.35em;margin:0 0 16px}
li{margin:5px 0}
li>ul,li>ol{margin:4px 0 4px}
code{font:0.84em/1.4 ui-monospace,"JetBrains Mono","Cascadia Code",Menlo,monospace;
  background:var(--code-bg);padding:.12em .36em;border-radius:4px;word-break:break-word}

/* resumen */
.doc-head{margin-bottom:8px}
.summary{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:18px 0 6px;
  padding:12px 14px;background:var(--card);border:1px solid var(--rule);border-radius:10px;font-size:14px}
.summary-count{font-weight:650;margin-right:6px;color:var(--ink)}

/* insignias */
.badge{display:inline-block;font-size:12px;font-weight:650;letter-spacing:.03em;padding:2px 9px;border-radius:999px;line-height:1.6;white-space:nowrap}
.badge.p1{color:var(--p1);background:var(--p1-bg)}
.badge.p2{color:var(--p2);background:var(--p2-bg)}
.badge.p3{color:var(--p3);background:var(--p3-bg)}

/* hallazgos */
article.finding{background:var(--card);border:1px solid var(--rule);border-radius:12px;
  padding:22px 26px 14px;margin:20px 0 26px;scroll-margin-top:24px;break-inside:avoid}
article.finding h3{margin:6px 0 14px;font-size:18.5px}
.finding-meta{display:flex;flex-wrap:wrap;align-items:center;gap:10px;font-size:13px}
.fid{font-family:ui-monospace,"JetBrains Mono",Menlo,monospace;font-weight:600;color:var(--muted);letter-spacing:.02em}
.tag{color:var(--muted);font-size:13px}
.tag::before{content:"· "}
.field{margin:0 0 12px}
.field .k{display:block;font-size:11.5px;font-weight:650;letter-spacing:.08em;text-transform:uppercase;color:var(--faint);margin-bottom:2px}
.field.fix{margin:16px 0 4px;padding:12px 16px;background:var(--accent-soft);border-left:3px solid var(--accent);border-radius:0 8px 8px 0}
.field.fix .k{color:var(--accent)}
.field.fix p,.field.fix{margin-bottom:0}
article.finding>p:last-child,article.finding>ul:last-child{margin-bottom:6px}

/* tablas */
.table-wrap{margin:18px 0 26px;border:1px solid var(--rule);border-radius:10px;overflow-x:auto;background:var(--card)}
table{width:100%;border-collapse:collapse;font:14px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}
th,td{padding:9px 12px;text-align:left;vertical-align:top;border-bottom:1px solid var(--rule)}
th{font-size:12px;font-weight:650;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);background:var(--wash);position:sticky;top:0}
tbody tr:last-child td{border-bottom:0}
td{min-width:120px}
td code,td a{font-size:.9em;overflow-wrap:anywhere;word-break:normal}
tbody tr:hover td{background:var(--wash)}
article.finding table{font-size:13.5px}

/* impresión */
@media print{
  :root{--paper:#fff;--card:#fff;--ink:#111;--muted:#444;--faint:#666;--rule:#ccc;--wash:#f3f3f3;--accent:#0b4f4c;--accent-soft:#eef5f4}
  .toc{display:none}
  .shell{display:block}
  main{padding:0;max-width:none}
  article.finding,.table-wrap{break-inside:avoid}
  h2,h3{break-after:avoid}
  a{color:inherit}
  th{position:static}
}
@media (max-width:960px){
  .shell{grid-template-columns:1fr}
  .toc{position:static;height:auto;max-height:340px;border-right:0;border-bottom:1px solid var(--rule);padding:22px 20px}
  main{padding:30px 20px 80px}
  h1{font-size:25px}
}
@media (max-width:600px){
  body{font-size:16px}
  article.finding{padding:18px 16px 10px}
}
"""

JS = """
(function(){
  var links=[].slice.call(document.querySelectorAll('nav.toc a[href^="#"]'));
  var byId={};
  links.forEach(function(a){byId[a.getAttribute('href').slice(1)]=a;});
  if(!('IntersectionObserver' in window)) return;
  var targets=Object.keys(byId).map(function(id){return document.getElementById(id);}).filter(Boolean);
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(!e.isIntersecting) return;
      links.forEach(function(l){l.classList.remove('on');});
      var a=byId[e.target.id];
      if(a){a.classList.add('on');
        var nav=document.querySelector('nav.toc');
        var r=a.getBoundingClientRect(), nr=nav.getBoundingClientRect();
        if(r.top<nr.top||r.bottom>nr.bottom){a.scrollIntoView({block:'nearest'});}
      }
    });
  },{rootMargin:'-18% 0px -72% 0px'});
  targets.forEach(function(t){io.observe(t);});
})();
"""


def page(doc):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(doc['title'])}</title>
<style>{CSS}</style>
</head>
<body>
<div class="shell">
{doc['toc']}
<main>
<div class="doc-head">{doc['header']}</div>
{doc['body']}
<footer style="margin-top:64px;font:13px system-ui,sans-serif;color:var(--faint)">Fuente: <code>{esc(doc['source'])}</code></footer>
</main>
</div>
<script>{JS}</script>
</body>
</html>
"""


def main(paths):
    for p in paths:
        src = Path(p)
        doc = build(parse(src.read_text(encoding="utf-8")), src.name)
        out = src.with_suffix(".html")
        out.write_text(page(doc), encoding="utf-8")
        print(f"{src.name} -> {out.name}")


if __name__ == "__main__":
    main(sys.argv[1:])
