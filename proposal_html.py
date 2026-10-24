#!/usr/bin/env python3
"""Build designed, standalone HTML reading editions of the course proposals."""
from pathlib import Path
import html
import audit_html as md

FILES = [Path('prop_a.md'), Path('prop_b.md'), Path('prop_d,md')]
CSS = '''
:root{color-scheme:light;--ink:#17252b;--muted:#586b70;--line:#d8e2df;--paper:#fff;--bg:#f2f6f4;--teal:#087e80;--soft:#e2f1ee;--gold:#a35d11;font-family:Inter,"Segoe UI",Arial,sans-serif}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);line-height:1.68}.shell{max-width:1320px;margin:auto;padding:36px 28px}.mast{padding:22px 0 30px;border-bottom:1px solid var(--line)}.eyebrow,.toc h2,.num{font-size:.76rem;letter-spacing:.1em;text-transform:uppercase;font-weight:700;color:var(--teal)}h1,h2,h3{line-height:1.22;letter-spacing:-.025em}h1{font-size:clamp(2rem,5vw,3.5rem);max-width:24ch;margin:.4rem 0 1rem}h2{font-size:1.75rem;margin:0 0 1.1rem}h3{font-size:1.18rem;margin:1.8rem 0 .65rem}p,li{max-width:78ch}p{margin:.7rem 0}a{color:#006d70;text-underline-offset:3px}.meta{color:var(--muted);font-size:.95rem}.layout{display:grid;grid-template-columns:250px minmax(0,790px);gap:54px;justify-content:center;padding-top:34px}.toc{position:sticky;top:20px;align-self:start;max-height:calc(100vh - 40px);overflow:auto;padding:18px;background:var(--paper);border:1px solid var(--line);border-radius:12px}.toc h2{margin:0 0 12px}.toc ol{padding-left:1.25rem;margin:0}.toc li{margin:.45rem 0;font-size:.91rem}.toc a{text-decoration:none;color:var(--ink)}.toc a:hover{color:var(--teal)}main{min-width:0}.section{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:clamp(22px,4vw,42px);margin:0 0 22px;scroll-margin-top:20px}.section h2{padding-bottom:15px;border-bottom:1px solid var(--line)}.section h3{color:#176c6d}.section ul,.section ol{padding-left:1.4rem}.section li{padding-left:.2rem;margin:.3rem 0}.section code{font-family:ui-monospace,monospace;background:var(--soft);padding:.08em .32em;border-radius:4px;font-size:.9em}.section blockquote{border-left:3px solid var(--teal);padding-left:1rem;color:var(--muted)}.section hr{border:0;border-top:1px solid var(--line);margin:1.5rem 0}.toplink{display:block;text-align:right;font-size:.85rem;margin-top:1.4rem}.footer{color:var(--muted);font-size:.85rem;text-align:center;padding:24px}@media(max-width:850px){.shell{padding:20px 14px}.layout{grid-template-columns:1fr;gap:18px}.toc{position:static;max-height:none}.toc ol{columns:2}}@media(max-width:520px){.toc ol{columns:1}.section{padding:20px}.shell{padding-inline:10px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
'''

for src in FILES:
    blocks = md.parse(src.read_text(encoding='utf-8'))
    used = set(); sections=[]; toc=[]; current=[]; title=src.stem
    for block in blocks:
        if block[0]=='h' and block[1]==1:
            title=md.plain(block[2]); continue
        if block[0]=='h' and block[1]==2:
            if current: sections.append(current)
            sid=md.slugify(block[2],used)
            toc.append((sid,md.plain(block[2])))
            current=[f'<section class="section" id="{sid}"><span class="num">{len(toc):02d} / Sección</span><h2>{md.inline(block[2])}</h2>']
        elif current:
            if block[0]=='h': current.append(f'<h{block[1]}>{md.inline(block[2])}</h{block[1]}>')
            elif block[0]=='p': current.append(f'<p>{md.inline(block[1])}</p>')
            elif block[0]=='list': current.append(md.render_list(block[1]))
            elif block[0]=='table': current.append(md.render_table(block[1],block[2]))
            elif block[0]=='hr': current.append('<hr>')
    if current: sections.append(current)
    nav=''.join(f'<li><a href="#{sid}">{html.escape(label)}</a></li>' for sid,label in toc)
    content=''.join(''.join(s)+f'<a class="toplink" href="#inicio">Volver arriba ↑</a></section>' for s in sections)
    date='23 de octubre de 2026'
    page=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Propuesta curricular del curso de estadística aplicada a la fotometría de ozono con SRP."><title>{html.escape(title)} — CALAIRE</title><style>{CSS}</style></head><body><div class="shell" id="inicio"><header class="mast"><div class="eyebrow">CALAIRE · Estadística aplicada · SRP</div><h1>{md.inline(title)}</h1><p class="meta">Edición de lectura en HTML · {date}</p></header><div class="layout"><nav class="toc" aria-label="Índice"><h2>En esta propuesta</h2><ol>{nav}</ol></nav><main>{content}</main></div><footer class="footer">Documento de trabajo curricular · CALAIRE</footer></div></body></html>'''
    dest=Path('prop_d.html') if src.name == 'prop_d,md' else src.with_suffix('.html')
    dest.write_text(page,encoding='utf-8')
    print(f'{dest}: {len(page):,} bytes')
