"""Cálculos y gráfico reproducibles para las prácticas de aplicación de M02.

Todos los datos se generan mediante listas declaradas y reglas aritméticas
fijas; son simulados y no proceden de CALAIRE.
"""

from html import escape
from pathlib import Path

import numpy as np

# B: referencia e indicación emparejadas en tres días, nmol/mol.
days = np.repeat([1, 2, 3], 4)
x_b = np.repeat([99.8, 100.0, 100.2], 4)
e_b = np.array([
    -0.2, -0.1, 0.0, 0.1,
    -0.1, 0.0, 0.1, 0.2,
    0.0, 0.1, 0.2, 0.3,
])
y_b = x_b + e_b
assert np.allclose(y_b - x_b, e_b)
print("B data: day, x, y, e (simulated; nmol/mol)")
for row in zip(days, x_b, y_b, e_b):
    print(*row)
for label, values in (("x", x_b), ("y", y_b), ("e", e_b)):
    print("B", label, "mean", np.mean(values), "median", np.median(values),
          "sample variance", np.var(values, ddof=1), "sample SD",
          np.std(values, ddof=1), "range", np.ptp(values),
          "Q1/Q3", np.quantile(values, [0.25, 0.75], method="linear"))
print("B y sample SD vs e sample SD", np.std(y_b, ddof=1), np.std(e_b, ddof=1))
print("B y CV (%)", 100 * np.std(y_b, ddof=1) / np.mean(y_b))
for day in (1, 2, 3):
    subset = e_b[days == day]
    print("B day", day, "e mean", np.mean(subset), "e sample SD",
          np.std(subset, ddof=1))
zero = np.array([-0.2, -0.1, 0.0, 0.1, 0.2])
print("B zero mean, mean after truncation", np.mean(zero),
      np.mean(np.maximum(zero, 0)))

# I: three days of paired readings at each level; exact additive pattern
# creates visible within-day spread and a level-dependent error trend.
levels = np.array([80., 160., 240., 320., 400.])
within = np.array([-0.06, -0.02, 0.02, 0.06])
rows_i = []
for day, shift in enumerate([-0.08, 0.0, 0.08], start=1):
    for x in levels:
        for offset in within:
            e = 0.10 + 0.002 * x + shift + offset
            rows_i.append((day, x, x + e, e))
arr_i = np.asarray(rows_i)
print("I rows (day, x, y, e); simulated and deterministic")
for row in arr_i:
    print(*row)
for day in (1, 2, 3):
    vals = arr_i[arr_i[:, 0] == day, 3]
    print("I day", day, "mean e", np.mean(vals), "median e", np.median(vals),
          "MAD e", np.median(np.abs(vals - np.median(vals))),
          "pooled-across-levels sample SD", np.std(vals, ddof=1))
    for x in levels:
        cell = arr_i[(arr_i[:, 0] == day) & (arr_i[:, 1] == x), 3]
        cell_sd = np.std(cell, ddof=1)
        print("I cell day", day, "level", x, "n", len(cell),
              "mean e", np.mean(cell), "sample SD within cell", cell_sd)
        assert np.isclose(cell_sd, 0.051639777949432225)
mean_by_level = []
for x in levels:
    vals = arr_i[arr_i[:, 1] == x, 3]
    mean_by_level.append(np.mean(vals))
    print("I level", x, "mean e", np.mean(vals), "median e", np.median(vals),
          "MAD e", np.median(np.abs(vals - np.median(vals))))
coef = np.polyfit(arr_i[:, 1], arr_i[:, 3], 1)
pred = np.polyval(coef, levels)
print("I fitted e intercept/slope", coef[1], coef[0])
print("I predicted error by level", pred)
print("I residuals min/max", np.min(arr_i[:, 3] - np.polyval(coef, arr_i[:, 1])),
      np.max(arr_i[:, 3] - np.polyval(coef, arr_i[:, 1])))
assert np.allclose(coef, [0.002, 0.10])

# A: balanced opposite-bias groups and a prespecified sensitivity point.
g1 = np.array([0.3, 0.4, 0.5, 0.4])
g2 = np.array([-0.3, -0.4, -0.5, -0.4])
all_a = np.r_[g1, g2]
with_point = np.r_[all_a, 1.6]
unequal_g2 = np.array([-0.3, -0.4])
unequal = np.r_[g1, unequal_g2]
for label, values in (("A group 1", g1), ("A group 2", g2),
                      ("A pooled", all_a), ("A pooled plus point", with_point),
                      ("A unequal-size pooled", unequal)):
    med = np.median(values)
    print(label, "n", len(values), "mean e", np.mean(values),
          "mean |e|", np.mean(np.abs(values)), "|mean e|", abs(np.mean(values)),
          "sample SD", np.std(values, ddof=1), "median", med,
          "MAD", np.median(np.abs(values - med)))
print("A group means unweighted with unequal sizes",
      (np.mean(g1) + np.mean(unequal_g2)) / 2,
      "pooled observation mean", np.mean(unequal))
assert np.isclose(np.mean(all_a), 0.0)
assert np.isclose(np.mean(np.abs(all_a)), 0.4)
assert np.isclose(np.mean(with_point), 1.6 / 9)

# Accessible, self-contained SVG/HTML charts for the B tasks.
# Day identity uses fixed color and marker encodings; no external packages.
colors = {1: "#2a78d6", 2: "#eb6834", 3: "#199e70"}
markers = {1: "circle", 2: "square", 3: "triangle"}
ink = "#0b0b0b"
secondary = "#52514e"
muted = "#898781"
surface = "#fcfcfb"
grid = "#e1e0d9"
axis = "#c3c2b7"
dark_ink = "#f0efec"
dark_secondary = "#c5c4be"
dark_muted = "#a4a39d"
dark_surface = "#1a1a19"
dark_grid = "#383835"
dark_axis = "#77766f"

def chart_role(role):
    return f'class="chart-{role}"'


def decimal(value, digits=1):
    return f"{value:.{digits}f}".replace(".", ",")
markers = {1: "circle", 2: "square", 3: "triangle"}
width, height = 840, 420
left, right, top, bottom = 80, 800, 45, 330
xmin, xmax = 1, len(e_b)
ymin, ymax = -0.25, 0.35

def sx(value):
    return left + (value - xmin) / (xmax - xmin) * (right - left)

def sy(value):
    return bottom - (value - ymin) / (ymax - ymin) * (bottom - top)

def mark(day, cx, cy, size=5):
    color = colors[day]
    if markers[day] == "circle":
        return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{size}" class="chart-mark-{day}" fill="{color}" stroke="{surface}" stroke-width="2"/>'
    if markers[day] == "square":
        return f'<rect x="{cx-size:.1f}" y="{cy-size:.1f}" width="{2*size}" height="{2*size}" class="chart-mark-{day}" fill="{color}" stroke="{surface}" stroke-width="2"/>'
    return f'<path d="M {cx:.1f} {cy-size-1:.1f} L {cx+size+1:.1f} {cy+size:.1f} L {cx-size-1:.1f} {cy+size:.1f} Z" class="chart-mark-{day}" fill="{color}" stroke="{surface}" stroke-width="2"/>'

def accessible_svg(svg_parts, title, description, prefix):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="{prefix}-title {prefix}-desc" viewBox="0 0 {width} {height}">',
            f'<title id="{prefix}-title">{escape(title)}</title>',
            f'<desc id="{prefix}-desc">{escape(description)}</desc>',
            f'<rect width="100%" height="100%" fill="{surface}"/>', *svg_parts, '</svg>']

def html_page(title, body, table):
    css = f'''<style>:root{{--surface:{surface};--ink:{ink};--secondary:{secondary};--muted:{muted};--grid:{grid};--axis:{axis};--series-1:{colors[1]};--series-2:{colors[2]};--series-3:{colors[3]};--fit:{ink}}}
body{{font:16px system-ui,sans-serif;color:var(--ink);background:var(--surface);margin:2rem}}svg{{max-width:100%;height:auto}}.chart-surface{{fill:var(--surface)}}.chart-grid{{stroke:var(--grid)}}.chart-axis{{stroke:var(--axis)}}.chart-zero{{stroke:var(--muted)}}.chart-ink{{fill:var(--ink);stroke:var(--ink)}}.chart-secondary{{fill:var(--secondary)}}.chart-mark-1{{fill:var(--series-1);stroke:var(--series-1)}}.chart-mark-2{{fill:var(--series-2);stroke:var(--series-2)}}.chart-mark-3{{fill:var(--series-3);stroke:var(--series-3)}}.chart-fit{{stroke:var(--fit);fill:var(--fit)}}table{{border-collapse:collapse;margin-top:1rem;color:var(--ink)}}th,td{{border-bottom:1px solid var(--axis);padding:.35rem .7rem;text-align:right;font-variant-numeric:tabular-nums}}th{{color:var(--secondary)}}caption{{color:var(--secondary);text-align:left}}
@media(prefers-color-scheme:dark){{:root{{--surface:{dark_surface};--ink:{dark_ink};--secondary:{dark_secondary};--muted:{dark_muted};--grid:{dark_grid};--axis:{dark_axis};--series-1:#68a9ff;--series-2:#ff9b70;--series-3:#63d6a6;--fit:{dark_ink}}}}}</style>'''
    return f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="color-scheme" content="light dark"><title>{escape(title)}</title>{css}<h1>{escape(title)}</h1>{body}{table}</html>'

svg = []
for tick in (-0.2, -0.1, 0.0, 0.1, 0.2, 0.3):
    yy = sy(tick)
    svg.append(f'<line x1="{left}" y1="{yy:.1f}" x2="{right}" y2="{yy:.1f}" class="chart-grid" stroke="{grid}" stroke-width="1"/>')
    svg.append(f'<text x="{left-12}" y="{yy+4:.1f}" text-anchor="end" class="chart-secondary" fill="{secondary}" font-size="12">{decimal(tick)}</text>')
svg.extend([f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" class="chart-axis" stroke="{axis}"/>',
            f'<line x1="{left}" y1="{sy(0):.1f}" x2="{right}" y2="{sy(0):.1f}" class="chart-zero" stroke="{muted}"/>'])
for idx in range(1, 13):
    xx = sx(idx)
    svg.append(f'<text x="{xx:.1f}" y="{bottom+22}" text-anchor="middle" class="chart-secondary" fill="{secondary}" font-size="11">{idx}</text>')
svg.extend([f'<text x="{(left+right)/2}" y="{height-20}" text-anchor="middle" class="chart-ink" fill="{ink}" font-size="14">Orden de lectura</text>',
            f'<text transform="translate(22 {(top+bottom)/2}) rotate(-90)" text-anchor="middle" class="chart-ink" fill="{ink}" font-size="14">Error e (nmol/mol)</text>',
            f'<text x="{left}" y="24" class="chart-ink" fill="{ink}" font-size="16">Datos simulados · tres días</text>'])
for day in (1, 2, 3):
    indexes = [i + 1 for i, d in enumerate(days) if d == day]
    vals = [e_b[i - 1] for i in indexes]
    points = " ".join(f"{sx(i):.1f},{sy(v):.1f}" for i, v in zip(indexes, vals))
    color = colors[day]
    svg.append(f'<polyline points="{points}" fill="none" class="chart-mark-{day}" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    for i, value in zip(indexes, vals):
        cx, cy = sx(i), sy(value)
        title = escape(f"Día {day}, lectura {i}, error {decimal(value)} nmol/mol")
        svg.append(f'<g><title>{title}</title>{mark(day, cx, cy)}</g>')
    legend_y = 52 + (day - 1) * 22
    svg.append(f'<line x1="650" y1="{legend_y}" x2="672" y2="{legend_y}" class="chart-mark-{day}" stroke="{color}" stroke-width="2"/><text x="680" y="{legend_y+4}" class="chart-secondary" fill="{secondary}" font-size="12">Día {day} ({markers[day]})</text>')
svg = accessible_svg(svg, "Error por orden de lectura y día", "Serie temporal simulada de doce errores en nmol/mol, cuatro lecturas en cada uno de tres días. Los centros diarios son −0,05; 0,05 y 0,15 nmol/mol.", "b-time")
rows = ''.join(f'<tr><td>{day}</td><td>{i}</td><td>{decimal(x)}</td><td>{decimal(y)}</td><td>{decimal(err)}</td></tr>' for i, (day, x, y, err) in enumerate(zip(days, x_b, y_b, e_b), start=1))
table = '<h2>Tabla accesible de datos</h2><table><caption>Referencia, indicación y error emparejados; unidades nmol/mol</caption><thead><tr><th>Día</th><th>Orden</th><th>x</th><th>y</th><th>e</th></tr></thead><tbody>' + rows + '</tbody></table>'

# Histogram with declared 0,1 nmol/mol bins from −0,25 to 0,35.
bin_edges = np.array([-0.25, -0.15, -0.05, 0.05, 0.15, 0.25, 0.35])
counts, _ = np.histogram(e_b, bins=bin_edges)
print("B histogram bins [left, right), final bin closed", list(zip(bin_edges[:-1], bin_edges[1:], counts)))
hw, hh = 840, 400
hl, hr, ht, hb = 85, 790, 55, 320
hist_svg = []
max_count = max(counts)
for count in range(max_count + 1):
    yy = hb - count / max_count * (hb - ht)
    hist_svg.append(f'<line x1="{hl}" y1="{yy:.1f}" x2="{hr}" y2="{yy:.1f}" class="chart-grid" stroke="{grid}"/>')
    hist_svg.append(f'<text x="{hl-12}" y="{yy+4:.1f}" text-anchor="end" class="chart-secondary" fill="{secondary}" font-size="12">{count}</text>')
bar_width = (hr - hl) / len(counts)
for j, (lo, hi, count) in enumerate(zip(bin_edges[:-1], bin_edges[1:], counts)):
    x0 = hl + j * bar_width
    bar_h = count / max_count * (hb - ht)
    hist_svg.append(f'<rect x="{x0+2:.1f}" y="{hb-bar_h:.1f}" width="{bar_width-4:.1f}" height="{bar_h:.1f}" rx="4" class="chart-mark-1" fill="{colors[1]}"/>')
    hist_svg.append(f'<text x="{x0+bar_width/2:.1f}" y="{hb+20}" text-anchor="middle" class="chart-secondary" fill="{secondary}" font-size="11">{decimal(lo,2)}</text>')
hist_svg.extend([f'<line x1="{hl}" y1="{hb}" x2="{hr}" y2="{hb}" class="chart-axis" stroke="{axis}"/>',
                 f'<text x="{(hl+hr)/2}" y="{hh-18}" text-anchor="middle" class="chart-ink" fill="{ink}" font-size="14">Error e (nmol/mol); bordes [izq., der.), salvo último cerrado</text>',
                 f'<text transform="translate(22 {(ht+hb)/2}) rotate(-90)" text-anchor="middle" class="chart-ink" fill="{ink}" font-size="14">Frecuencia (lecturas)</text>'])
hist_svg = accessible_svg(hist_svg, "Histograma de errores M02-B", "Doce errores simulados; seis intervalos de ancho 0,1 nmol/mol, bordes desde −0,25 hasta 0,35.", "b-hist")
hist_rows = ''.join('<tr><td>[{}; {}{}</td><td>{}</td></tr>'.format(decimal(lo,2), decimal(hi,2), ']' if j == len(counts)-1 else ')', count) for j, (lo, hi, count) in enumerate(zip(bin_edges[:-1], bin_edges[1:], counts)))
hist_table = '<h2>Tabla accesible de intervalos</h2><table><caption>Intervalos en nmol/mol y frecuencia</caption><thead><tr><th>Intervalo</th><th>Frecuencia</th></tr></thead><tbody>' + hist_rows + '</tbody></table>'

# Linear-interpolated box summaries by day, with whiskers to min/max.
def quantile_linear(values, q):
    return np.quantile(values, q, method="linear")

box_svg = []
box_y = {1: 110, 2: 200, 3: 290}
box_left, box_right = 150, 760
box_x = lambda value: box_left + (value - ymin) / (ymax - ymin) * (box_right - box_left)
for day in (1, 2, 3):
    vals = e_b[days == day]
    q1, med, q3 = quantile_linear(vals, [0.25, 0.5, 0.75])
    lo, hi = np.min(vals), np.max(vals)
    yy, color = box_y[day], colors[day]
    box_svg.extend([f'<line x1="{box_x(lo):.1f}" y1="{yy}" x2="{box_x(hi):.1f}" y2="{yy}" class="chart-mark-{day}" stroke="{color}" stroke-width="2"/>',
                    f'<line x1="{box_x(lo):.1f}" y1="{yy-10}" x2="{box_x(lo):.1f}" y2="{yy+10}" class="chart-mark-{day}" stroke="{color}"/>',
                    f'<line x1="{box_x(hi):.1f}" y1="{yy-10}" x2="{box_x(hi):.1f}" y2="{yy+10}" class="chart-mark-{day}" stroke="{color}"/>',
                    f'<rect x="{box_x(q1):.1f}" y="{yy-16}" width="{max(2, box_x(q3)-box_x(q1)):.1f}" height="32" class="chart-mark-{day}" fill="{color}" fill-opacity="0.18"/>',
                    f'<line x1="{box_x(med):.1f}" y1="{yy-16}" x2="{box_x(med):.1f}" y2="{yy+16}" class="chart-mark-{day}" stroke="{color}" stroke-width="2"/>',
                    f'<text x="105" y="{yy+5}" text-anchor="end" class="chart-secondary" fill="{secondary}" font-size="13">Día {day}</text>'])
    print("B box day", day, "min/Q1/median/Q3/max", lo, q1, med, q3, hi)
for tick in (-0.2, -0.1, 0, 0.1, 0.2, 0.3):
    xx = box_x(tick)
    box_svg.append(f'<line x1="{xx:.1f}" y1="80" x2="{xx:.1f}" y2="330" class="chart-grid" stroke="{grid}"/>')
    box_svg.append(f'<text x="{xx:.1f}" y="350" text-anchor="middle" class="chart-secondary" fill="{secondary}" font-size="11">{decimal(tick)}</text>')
box_svg.extend([f'<text x="{(box_left+box_right)/2}" y="385" text-anchor="middle" class="chart-ink" fill="{ink}" font-size="14">Error e (nmol/mol); caja Q1–Q3, línea mediana, bigotes mínimo–máximo</text>'])
box_svg = accessible_svg(box_svg, "Diagrama de caja del error por día", "Cuartiles lineales por día; los bigotes llegan al mínimo y máximo observados. No se excluyen puntos.", "b-box")
box_rows = []
for day in (1, 2, 3):
    vals = e_b[days == day]
    q1, med, q3 = quantile_linear(vals, [0.25, 0.5, 0.75])
    box_rows.append(f'<tr><td>Día {day}</td><td>{decimal(np.min(vals))}</td><td>{decimal(q1)}</td><td>{decimal(med)}</td><td>{decimal(q3)}</td><td>{decimal(np.max(vals))}</td></tr>')
box_table = '<h2>Tabla accesible de cuartiles</h2><table><caption>Resumen por día, nmol/mol</caption><thead><tr><th>Grupo</th><th>Mínimo</th><th>Q1</th><th>Mediana</th><th>Q3</th><th>Máximo</th></tr></thead><tbody>' + ''.join(box_rows) + '</tbody></table>'
output = Path(__file__).resolve().parents[1] / "M02_practica_B_grafico.html"
body = '<p>Datos simulados, nmol/mol; símbolos distintos identifican días y se conservan los errores negativos.</p>' + ''.join(svg) + ''.join(hist_svg) + ''.join(box_svg)
output.write_text(html_page("Práctica M02-B · errores por día", body, table + hist_table + box_table), encoding="utf-8")
print("B accessible charts", output)

# SVG/HTML helpers for I (three shared-scale panels plus temporal means)
# and A (signed errors by condition); all values also appear in tables.
def scatter_panel(title, x_values, y_values, groups, groups_for_plot, group_names,
                  xlim, ylim, fit=None, xlabel="Referencia x (nmol/mol)"):
    w, h, l, r, t, b = 840, 400, 85, 790, 55, 320
    px = lambda value: l + (value - xlim[0]) / (xlim[1] - xlim[0]) * (r - l)
    py = lambda value: b - (value - ylim[0]) / (ylim[1] - ylim[0]) * (b - t)
    parts = [f'<text x="{l}" y="28" class="chart-ink" fill="{ink}" font-size="16">{escape(title)}</text>']
    for tick in np.linspace(ylim[0], ylim[1], 5):
        yy = py(tick)
        parts.extend([f'<line x1="{l}" y1="{yy:.1f}" x2="{r}" y2="{yy:.1f}" class="chart-grid" stroke="{grid}"/>',
                      f'<text x="{l-10}" y="{yy+4:.1f}" text-anchor="end" class="chart-secondary" fill="{secondary}" font-size="11">{decimal(tick,2)}</text>'])
    if ylim[0] <= 0 <= ylim[1]:
        parts.append(f'<line x1="{l}" y1="{py(0):.1f}" x2="{r}" y2="{py(0):.1f}" class="chart-zero" stroke="{muted}"/>')
    if fit:
        xa, xb = xlim
        parts.append(f'<line x1="{px(xa):.1f}" y1="{py(fit[0]+fit[1]*xa):.1f}" x2="{px(xb):.1f}" y2="{py(fit[0]+fit[1]*xb):.1f}" class="chart-fit" stroke="{ink}" stroke-width="2"/>')
    for group in groups:
        color = colors[group]
        indexes = [i for i, g in enumerate(groups_for_plot) if g == group]
        label = group_names.get(group, f"Grupo {group}")
        for i in indexes:
            xx, yy = px(x_values[i]), py(y_values[i])
            parts.append(f'<g><title>{label}, x={decimal(x_values[i],1)}, e={decimal(y_values[i],2)} nmol/mol</title>{mark(group, xx, yy)}</g>')
        ly = 52 + groups.index(group) * 22
        parts.append(mark(group, 650, ly, 4) + f'<text x="662" y="{ly+4}" class="chart-secondary" fill="{secondary}" font-size="12">{label}</text>')
    if fit:
        for x, y in zip(levels, np.polyval([fit[1], fit[0]], levels)):
            parts.append(f'<path d="M {px(x):.1f} {py(y)-6:.1f} L {px(x)+6:.1f} {py(y):.1f} L {px(x):.1f} {py(y)+6:.1f} L {px(x)-6:.1f} {py(y):.1f} Z" class="chart-ink" fill="{ink}"><title>Predicción en x={decimal(x,0)}: {decimal(y,2)} nmol/mol</title></path>')
        parts.append(f'<line x1="650" y1="{52+len(groups)*22}" x2="672" y2="{52+len(groups)*22}" class="chart-fit" stroke="{ink}" stroke-width="2"/><text x="680" y="{56+len(groups)*22}" class="chart-secondary" fill="{secondary}" font-size="12">Ajuste descriptivo</text>')
    parts.extend([f'<text x="{(l+r)/2}" y="{h-18}" text-anchor="middle" class="chart-ink" fill="{ink}" font-size="14">{escape(xlabel)}</text>',
                  f'<text transform="translate(22 {(t+b)/2}) rotate(-90)" text-anchor="middle" class="chart-ink" fill="{ink}" font-size="14">Error e (nmol/mol)</text>'])
    return parts

# Groups are explicit inputs; each small multiple gets its own subset.
def save_i_chart():
    w, h = 840, 1600
    panel_markup = []
    group_names = {1: "Día 1", 2: "Día 2", 3: "Día 3"}
    for day in (1, 2, 3):
        subset = arr_i[arr_i[:, 0] == day]
        markup = scatter_panel(f"Día {day} · datos simulados", subset[:, 1], subset[:, 3], [day], [day] * len(subset), group_names, (60, 420), (-0.2, 1.2), fit=(coef[1], coef[0]))
        panel_markup.append(f'<g transform="translate(0 {(day-1)*400})">' + ''.join(markup) + '</g>')
    daily_means = [np.mean(arr_i[arr_i[:, 0] == day, 3]) for day in (1, 2, 3)]
    tx = lambda value: 125 + (value - 1) / 2 * 620
    ty = lambda value: 1450 - (value - 0.45) / 0.30 * 170
    temporal = [f'<text x="85" y="1370" class="chart-ink" fill="{ink}" font-size="16">Medias diarias frente al orden temporal</text>']
    for tick in (0.5, 0.6, 0.7):
        yy = ty(tick)
        temporal.extend([f'<line x1="100" y1="{yy:.1f}" x2="760" y2="{yy:.1f}" class="chart-grid" stroke="{grid}"/>',f'<text x="90" y="{yy+4:.1f}" text-anchor="end" class="chart-secondary" fill="{secondary}" font-size="11">{decimal(tick)}</text>'])
    temporal.extend([f'<text x="430" y="1560" text-anchor="middle" class="chart-ink" fill="{ink}" font-size="14">Día (orden temporal)</text>',f'<text transform="translate(30 1450) rotate(-90)" text-anchor="middle" class="chart-ink" fill="{ink}" font-size="14">Media del error (nmol/mol)</text>'])
    for day, value in enumerate(daily_means, start=1):
        temporal.append(f'<g><title>Día {day}, media {decimal(value,2)} nmol/mol</title>{mark(day, tx(day), ty(value))}</g>')
        temporal.append(f'<text x="{tx(day):.1f}" y="{ty(value)-12:.1f}" text-anchor="middle" class="chart-secondary" fill="{secondary}" font-size="12">{decimal(value,2)}</text>')
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="i-title i-desc" viewBox="0 0 840 1600">','<title id="i-title">Error frente a referencia y medias diarias</title>','<desc id="i-desc">Tres paneles diarios con escalas comunes, ajuste lineal descriptivo e indicadores de predicción, más un panel de medias diarias frente al orden temporal. Datos simulados.</desc>',f'<rect width="100%" height="100%" fill="{surface}"/>',''.join(panel_markup)+''.join(temporal),'</svg>']
    rows = ''.join(f'<tr><td>Día {int(day)}</td><td>{decimal(x,1)}</td><td>{decimal(y,2)}</td><td>{decimal(e,2)}</td></tr>' for day,x,y,e in arr_i)
    pred_rows = ''.join(f'<tr><td>{decimal(x,0)}</td><td>{decimal(y,2)}</td></tr>' for x,y in zip(levels,pred))
    mean_rows = ''.join(f'<tr><td>Día {day}</td><td>{decimal(value,2)}</td></tr>' for day,value in enumerate(daily_means,1))
    table = '<h2>Tabla accesible de observaciones</h2><table><caption>Datos simulados; referencia, indicación y error en nmol/mol</caption><thead><tr><th>Día</th><th>x</th><th>y</th><th>e</th></tr></thead><tbody>'+rows+'</tbody></table><h2>Predicciones de la recta</h2><table><caption>Ajuste descriptivo ê(x)=0,100+0,002x, nmol/mol</caption><thead><tr><th>x</th><th>ê</th></tr></thead><tbody>'+pred_rows+'</tbody></table><h2>Medias temporales</h2><table><caption>Error medio por día, nmol/mol</caption><thead><tr><th>Orden</th><th>Media</th></tr></thead><tbody>'+mean_rows+'</tbody></table>'
    dest=Path(__file__).resolve().parents[1]/"M02_practica_I_grafico.html"
    dest.write_text(html_page("Práctica M02-I · precisión y tendencia",'<p>Datos simulados; tres paneles con escala común. Línea negra: ajuste descriptivo; rombos negros: predicciones.</p>'+''.join(svg),table),encoding="utf-8")
    print("I accessible chart",dest)

# A panel stays within its two categorical conditions and signed error.
def save_a_chart():
    names={1:"Grupo 1",2:"Grupo 2"}
    w,h=840,440;l,r,t,b=100,780,55,350
    px=lambda value:l+(value-0.5)/4*(r-l)
    py=lambda value:b-(value+0.6)/1.2*(b-t)
    parts=[f'<line x1="100" y1="{py(0):.1f}" x2="780" y2="{py(0):.1f}" class="chart-zero" stroke="{muted}"/>']
    for group, values in ((1,g1),(2,g2)):
        for i,value in enumerate(values,1):
            xx,yy=px(i),py(value)
            parts.append(f'<g><title>{names[group]}, observación {i}, error {decimal(value,1)} nmol/mol</title>{mark(group,xx,yy)}</g>')
    for group in (1,2):
        ly=80+25*(group-1)
        shape=mark(group,650,ly,4)
        parts.append(f'{shape}<text x="662" y="{ly+4}" class="chart-secondary" fill="{secondary}" font-size="12">{names[group]}</text>')
    for tick in (-0.6,-0.4,-0.2,0,0.2,0.4,0.6):
        yy=py(tick)
        parts.extend([f'<line x1="100" y1="{yy:.1f}" x2="780" y2="{yy:.1f}" class="chart-grid" stroke="{grid}"/>',f'<text x="90" y="{yy+4:.1f}" text-anchor="end" class="chart-secondary" fill="{secondary}" font-size="11">{decimal(tick,1)}</text>'])
    parts.extend([f'<text x="440" y="390" text-anchor="middle" class="chart-ink" fill="{ink}" font-size="14">Observación dentro de cada grupo</text>',f'<text transform="translate(25 200) rotate(-90)" text-anchor="middle" class="chart-ink" fill="{ink}" font-size="14">Error e (nmol/mol)</text>'])
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Errores firmados por grupo" viewBox="0 0 {w} {h}">','<rect width="100%" height="100%" fill="{surface}"/>',''.join(parts),'</svg>']
    rows=''.join(f'<tr><td>{names[group]}</td><td>{i}</td><td>{decimal(value,1)}</td></tr>' for group,values in ((1,g1),(2,g2)) for i,value in enumerate(values,1))
    table='<h2>Tabla accesible</h2><table><caption>Errores firmados simulados, nmol/mol</caption><thead><tr><th>Grupo</th><th>Observación</th><th>Error</th></tr></thead><tbody>'+rows+'</tbody></table>'
    dest=Path(__file__).resolve().parents[1]/"M02_practica_A_grafico.html"
    dest.write_text(html_page("Práctica M02-A · errores firmados por grupo",'<p>Datos simulados; forma y color distinguen grupos, la línea horizontal marca cero.</p>'+''.join(svg),table),encoding="utf-8")
    print("A accessible chart",dest)

save_i_chart()
save_a_chart()
