"""Genera la visualización accesible de errores por día de M06-I.

Origen: libro propio F-PSMT-01, hoja BD_DIAS, diferencias de 90 nmol/mol
nominales, seis días x ocho réplicas. Ejecutar desde la raíz:
curso/.venv/bin/python curso/S2_modelos_calibracion/calc/M06_practica_I_grafico.py
"""
from html import escape
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
BOOK = ROOT / "docs" / "F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm"
OUTPUT = ROOT / "curso" / "S2_modelos_calibracion" / "M06_practica_I_residuos.html"
DAY_COLS = [6, 12, 18, 24, 30, 36]
DAY_NAMES = ["Día 1", "Día 2", "Día 3", "Día 4", "Día 5", "Día 6"]


def read_groups():
    book = openpyxl.load_workbook(BOOK, data_only=True, read_only=True)
    sheet = book["BD_DIAS"]
    groups = [[-float(sheet.cell(row, col).value) for row in range(31, 39)]
              for col in DAY_COLS]
    book.close()
    if any(len(group) != 8 for group in groups):
        raise ValueError("Se esperaban ocho errores por día")
    return groups


def chart_svg(groups):
    width, height = 960, 510
    panel_w, panel_h = 300, 225
    start_x, start_y = 42, 32
    plot_x, plot_y, plot_w, plot_h = 38, 32, 240, 145
    residuals = [[value - sum(values) / len(values) for value in values] for values in groups]
    ymin, ymax = -0.7, 0.7
    parts = [
        f'<svg viewBox="0 0 {width} {height}" role="img" aria-labelledby="chart-title chart-desc" xmlns="http://www.w3.org/2000/svg">',
        '<title id="chart-title">Residuos por día en el nivel nominal de 90 nmol/mol</title>',
        '<desc id="chart-desc">Seis paneles, uno por día, con ocho residuos respecto a la media de ese día, en orden de réplica. Los puntos se consultan con puntero o teclado; la tabla accesible contiene todos los valores.</desc>',
    ]
    for day, values in enumerate(groups):
        col, row = day % 3, day // 3
        ox, oy = start_x + col * panel_w, start_y + row * panel_h
        parts.append(f'<g aria-label="{DAY_NAMES[day]}"><text class="panel-title" x="{ox}" y="{oy}">{DAY_NAMES[day]}</text>')
        for tick in (-0.5, 0.0, 0.5):
            yy = oy + plot_y + plot_h * (ymax - tick) / (ymax - ymin)
            parts.append(f'<line class="grid" x1="{ox+plot_x}" y1="{yy:.1f}" x2="{ox+plot_x+plot_w}" y2="{yy:.1f}"/>')
            if col == 0:
                parts.append(f'<text class="tick" x="{ox+plot_x-8}" y="{yy+4:.1f}" text-anchor="end">{format(tick, ".1f").replace(".", ",")}</text>')
        parts.append(f'<line class="axis" x1="{ox+plot_x}" y1="{oy+plot_y}" x2="{ox+plot_x}" y2="{oy+plot_y+plot_h}"/>')
        parts.append(f'<line class="axis" x1="{ox+plot_x}" y1="{oy+plot_y+plot_h}" x2="{ox+plot_x+plot_w}" y2="{oy+plot_y+plot_h}"/>')
        for idx, value in enumerate(residuals[day], start=1):
            xx = ox + plot_x + (idx - 1) * plot_w / 7
            yy = oy + plot_y + plot_h * (ymax - value) / (ymax - ymin)
            aria = escape(f"{DAY_NAMES[day]}, réplica {idx}, residuo {value:.6f}".replace(".", ",") + " nmol/mol", quote=True)
            parts.append(f'<circle class="hit" cx="{xx:.1f}" cy="{yy:.1f}" r="12" tabindex="0" role="img" aria-label="{aria}" data-label="{aria}"/>')
            parts.append(f'<circle class="point" cx="{xx:.1f}" cy="{yy:.1f}" r="5" aria-hidden="true"/>')
        for idx in (1, 4, 8):
            xx = ox + plot_x + (idx - 1) * plot_w / 7
            parts.append(f'<text class="tick" x="{xx:.1f}" y="{oy+plot_y+plot_h+18}" text-anchor="middle">{idx}</text>')
        parts.append('</g>')
    parts.extend([
        f'<text class="axis-label" x="{width/2}" y="{height-7}" text-anchor="middle">Orden de réplica dentro del día</text>',
        f'<text class="axis-label" transform="translate(14 {height/2}) rotate(-90)" text-anchor="middle">Residuo (nmol/mol)</text>',
        '</svg>',
    ])
    return "".join(parts)


def accessible_table(groups):
    rows = ["<table><caption>Residuos por día y número de réplica (nmol/mol)</caption><thead><tr><th scope=\"col\">Día</th>"]
    rows.extend(f'<th scope="col">Réplica {i}</th>' for i in range(1, 9))
    rows.append("</tr></thead><tbody>")
    residuals = [[value - sum(values) / len(values) for value in values] for values in groups]
    for name, values in zip(DAY_NAMES, residuals):
        rows.append(f'<tr><th scope="row">{name}</th>')
        rows.extend(f'<td>{format(value, ".6f").replace(".", ",")}</td>' for value in values)
        rows.append("</tr>")
    rows.append("</tbody></table>")
    return "".join(rows)


def main():
    groups = read_groups()
    document = f'''<!doctype html>
<html lang="es" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>M06-I · residuos por día</title>
<style>
:root {{ color-scheme: light; --surface:#fcfcfb; --page:#f9f9f7; --ink:#0b0b0b; --secondary:#52514e; --muted:#898781; --grid:#e1e0d9; --axis:#c3c2b7; --series:#2a78d6; }}
:root[data-theme="dark"] {{ color-scheme:dark; --surface:#1a1a19; --page:#0d0d0d; --ink:#f0efec; --secondary:#c3c2b7; --muted:#898781; --grid:#2c2c2a; --axis:#383835; --series:#3987e5; }}
* {{ box-sizing:border-box; }} body {{ margin:0; padding:1.25rem; background:var(--page); color:var(--ink); font:1rem/1.5 system-ui,-apple-system,"Segoe UI",sans-serif; }} main {{ max-width:1000px; margin:auto; }} .viz {{ padding:1rem; background:var(--surface); border:1px solid var(--axis); border-radius:8px; overflow-x:auto; }} svg {{ display:block; width:100%; min-width:720px; height:auto; }} .panel-title {{ fill:var(--ink); font-size:14px; font-weight:650; }} .tick {{ fill:var(--secondary); font-size:11px; }} .axis-label {{ fill:var(--secondary); font-size:12px; }} .grid {{ stroke:var(--grid); stroke-width:1; }} .axis {{ stroke:var(--axis); stroke-width:1; }} .hit {{ fill:transparent; cursor:crosshair; outline:none; }} .point {{ fill:var(--series); stroke:var(--surface); stroke-width:2; pointer-events:none; }} .hit:focus + .point {{ stroke:var(--ink); stroke-width:3; }} #tooltip {{ min-height:1.5em; color:var(--secondary); }} button {{ margin-bottom:.75rem; padding:.45rem .7rem; color:var(--ink); background:var(--surface); border:1px solid var(--axis); border-radius:4px; }} table {{ border-collapse:collapse; width:100%; margin-top:1rem; font-variant-numeric:tabular-nums; }} caption {{ text-align:left; font-weight:650; padding:.5rem 0; }} th,td {{ padding:.35rem .55rem; border-bottom:1px solid var(--grid); text-align:right; }} th:first-child {{ text-align:left; }} .sr-only {{ position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0,0,0,0); white-space:nowrap; }}
</style></head><body><main><h1>Residuos por día en un nivel del Level 2</h1>
<p>Valores propios del certificado F-PSMT-01, Level 2 frente al SRP 55; nivel nominal de 90 nmol/mol. Cada panel muestra ocho residuos respecto a la media de ese día, en orden de réplica.</p>
<button id="theme" type="button" aria-pressed="false">Cambiar a modo oscuro</button>
<section class="viz" aria-label="Gráfico de errores por día">{chart_svg(groups)}<p id="tooltip" role="status" aria-live="polite"></p></section>
{accessible_table(groups)}
<p>Fuente: <code>docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm</code>, hoja <code>BD_DIAS</code>, filas 31–38; el signo se invierte respecto a la columna de origen para graficar <var>e</var> = Level 2 − SRP 55.</p>
</main><script>
const root=document.documentElement, button=document.getElementById('theme'), tip=document.getElementById('tooltip');
button.addEventListener('click',()=>{{const dark=root.dataset.theme!=='dark';root.dataset.theme=dark?'dark':'light';button.setAttribute('aria-pressed',String(dark));button.textContent=dark?'Cambiar a modo claro':'Cambiar a modo oscuro';}});
document.querySelectorAll('.hit').forEach(mark=>{{const show=()=>{{tip.textContent=mark.dataset.label;}};mark.addEventListener('pointerenter',show);mark.addEventListener('focus',show);mark.addEventListener('pointerleave',()=>{{tip.textContent='';}});mark.addEventListener('blur',()=>{{tip.textContent='';}});}});
</script></body></html>'''
    OUTPUT.write_text(document, encoding="utf-8")
    print(f"HTML accesible generado: {OUTPUT.relative_to(ROOT)} ({len(groups)} días x 8 lecturas)")


if __name__ == "__main__":
    main()
