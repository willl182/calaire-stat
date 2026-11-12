"""Cálculos reproducibles de las prácticas M11 B, I y A."""

from pathlib import Path
import runpy

import numpy as np
from scipy import stats


def practica_b():
    # Serie docente determinista simulada en nmol/mol; límites fijados antes del seguimiento.
    x = np.array([0.0, 0.4, -0.2, 0.1, 0.5, 1.8, 0.2, -0.1])
    mr = np.abs(np.diff(x))
    center = x[:5].mean()
    mr_bar = mr[:4].mean()
    limits = (center - 2.66 * mr_bar, center + 2.66 * mr_bar)
    mr_ucl = 3.267 * mr_bar
    signals = np.flatnonzero((x < limits[0]) | (x > limits[1])) + 1
    mr_signals = np.flatnonzero(mr > mr_ucl) + 2
    np.testing.assert_allclose(mr, [0.4, 0.6, 0.3, 0.4, 1.3, 1.6, 0.3])
    np.testing.assert_allclose([center, mr_bar, *limits, mr_ucl],
                               [0.16, 0.425, -0.9705, 1.2905, 1.388475])
    assert signals.tolist() == [6] and mr_signals.tolist() == [7]
    print("B: MR=", mr.tolist(), "centro=", center, "MRmedio=", mr_bar)
    print("B: LIC/LSC=", limits, "LSC_MR=", mr_ucl,
          "señales I=", signals.tolist(), "señales MR=", mr_signals.tolist())
    write_chart(x, mr, center, limits, mr_ucl, signals - 1, mr_signals - 2)


def practica_i():
    days = np.arange(0, 181, 30, dtype=float)
    y = np.array([0.10, 0.18, 0.25, 0.37, 0.44, 0.56, 0.63])
    fit = stats.linregress(days, y)
    residuals = y - (fit.intercept + fit.slope * days)
    s = np.sqrt(np.sum(residuals**2) / (len(y) - 2))
    tcrit = stats.t.ppf(0.975, 5)
    ci_slope = (fit.slope - tcrit * fit.stderr, fit.slope + tcrit * fit.stderr)
    design = np.column_stack((np.ones(len(days)), days))
    cov = s**2 * np.linalg.inv(design.T @ design)
    t210 = np.array([1.0, 210.0])
    prediction = float(t210 @ [fit.intercept, fit.slope])
    se_mean = float(np.sqrt(t210 @ cov @ t210))
    ci_mean = (prediction - tcrit * se_mean, prediction + tcrit * se_mean)
    se_future = float(np.sqrt(s**2 + se_mean**2))
    pi_future = (prediction - tcrit * se_future, prediction + tcrit * se_future)
    keep = days != 90
    sensitivity = stats.linregress(days[keep], y[keep])
    sensitivity_prediction = sensitivity.intercept + sensitivity.slope * 210
    np.testing.assert_allclose([fit.intercept, fit.slope, fit.stderr, prediction, s],
                               [0.0892857142857, 0.00302380952381,
                                0.0000922139, 0.724285714286, 0.014639], atol=1e-6)
    assert ci_slope[0] < fit.slope < ci_slope[1]
    print("I: a=%.9f; b=%.9f nmol/mol/d; SE_b=%.9f" %
          (fit.intercept, fit.slope, fit.stderr))
    print("I: IC95 b=", ci_slope, "predicción media 210d=", prediction,
          "IC95=", ci_mean, "SE media=", se_mean)
    print("I: s_res=", s, "SE observación futura=", se_future,
          "IP95=", pi_future)
    print("I: sin día 90 (sensibilidad, no exclusión autorizada): b=%.9f; pred210=%.9f" %
          (sensitivity.slope, sensitivity_prediction))


def practica_a():
    # Importa sin depender del directorio actual; los mismos datos y semilla se contrastan.
    path = Path(__file__).with_name("M11_ejemplos.py")
    namespace = runpy.run_path(str(path))
    result = namespace["ewma_cusum_risk"]()
    (seed, horizon, paths, p_ewma, p_cusum, p_ewma_shift, p_cusum_shift,
     p_ewma_all, p_cusum_all, delay_ewma, delay_cusum) = result
    assert (seed, horizon, paths) == (11026, 50, 100_000)
    assert round(p_ewma * paths) == 19909 and round(p_cusum * paths) == 9177
    assert round(p_ewma_shift * 89347) == 88270
    assert round(p_cusum_shift * 96059) == 94441
    beta, u_beta, cap = 0.00302381, 0.00009221, 0.20
    risks = {t: stats.norm.sf((cap / t - beta) / u_beta) for t in (30, 60, 90)}
    assert risks[60] < 0.05 < risks[90]
    print("A: riesgos exceder +0,20 nmol/mol:", risks)
    print("A: recurrencia serie +1, lambda=0,2, L=2,7, k=0,5, h=5")
    z = cp = cm = 0.0
    first_ewma = first_cusum = None
    for t in range(1, 13):
        z = 0.2 + 0.8 * z
        cp = max(0.0, cp + 1.0 - 0.5)
        cm = max(0.0, cm - 1.0 - 0.5)
        bound = 2.7 * np.sqrt(0.2 / 1.8 * (1 - 0.8 ** (2 * t)))
        assert np.isclose(z, 1 - 0.8**t)
        assert np.isclose(cp, 0.5 * t) and cm == 0.0
        if first_ewma is None and abs(z) > bound:
            first_ewma = t
        if first_cusum is None and max(cp, cm) > 5:
            first_cusum = t
        if t <= 2:
            print(f"  ocasión {t}: Z={z:.6f}, LSC_EWMA={bound:.6f}, C+={cp:.6f}, C-={cm:.6f}")
    assert (first_ewma, first_cusum) == (11, 11)
    print(f"  primera señal EWMA={first_ewma}; CUSUM={first_cusum}")
    html = (Path(__file__).parents[1] / "M11_practica_B_grafico.html").read_text(encoding="utf-8")
    assert html.count('<rect tabindex="0"') == 2
    assert '0,4000' in html and '0.4000' not in html
    assert 'aria-labelledby="title desc"' in html and '<caption>Datos accesibles' in html
    print("Gráfico: marcadores señal=2; coma decimal; tabla accesible: OK")
    print("A: detección condicional EWMA/CUSUM=", p_ewma_shift, p_cusum_shift,
          "demoras=", delay_ewma, delay_cusum)


def fmt(value, digits):
    return f"{value:.{digits}f}".replace(".", ",")


def write_chart(x, mr, center, i_limits, mr_ucl, i_signal_idx, mr_signal_idx):
    """Produce carta I-MR SVG y tabla accesible; estilos distinguen reglas."""
    labels = list(range(1, len(x) + 1))
    svg = ['<svg viewBox="0 0 760 490" role="img" aria-labelledby="title desc">',
           '<title id="title">Carta docente I-MR de ocho verificaciones</title>',
           '<desc id="desc">Serie simulada en nmol/mol con límites de control establecidos; las ocasiones 6 y 7 señalan.</desc>']
    for title, vals, y0, ymin, ymax, rules, signal_idx in (
            ("Individuales (nmol/mol)", x, 58, -1.2, 2.0,
             [(center, "Centro", "#6b6b68", ""), (i_limits[0], "LIC", "#eb6834", "6 4"),
              (i_limits[1], "LSC", "#eb6834", "6 4")], set(i_signal_idx)),
            ("Rango móvil (nmol/mol)", mr, 300, 0, 1.9,
             [(0.425, "Centro MR", "#6b6b68", ""), (mr_ucl, "LSC MR", "#eb6834", "6 4")], set(mr_signal_idx))):
        top, height, left, width = y0, 150, 78, 630
        def py(v): return top + height - (v - ymin) / (ymax - ymin) * height
        svg.append(f'<text x="{left}" y="{top-15}" fill="#0b0b0b">{title}</text>')
        for j in range(5):
            val = ymin + j * (ymax-ymin) / 4
            yy = py(val)
            svg.append(f'<line class="grid" x1="{left}" y1="{yy:.1f}" x2="{left+width}" y2="{yy:.1f}" stroke="#e1e0d9"/>')
            svg.append(f'<text x="8" y="{yy+4:.1f}" fill="#52514e">{fmt(val, 2)}</text>')
        for value, name, color, dash in rules:
            yy = py(value)
            line_class = "center-line" if "Centro" in name else "limit-line"
            svg.append(f'<line class="{line_class}" x1="{left}" y1="{yy:.1f}" x2="{left+width}" y2="{yy:.1f}" stroke="{color}" stroke-width="1.5" stroke-dasharray="{dash}"/>')
            svg.append(f'<text x="{left+width-58}" y="{yy-4:.1f}" fill="#52514e">{name}</text>')
        # Ambos paneles usan la rejilla de ocasiones 1..8; el MR de la ocasión k+1 cae en la columna k+1.
        offset = 0 if title.startswith("Individuales") else 1
        step = width / (len(labels) - 1)
        coords = [(left + (i + offset) * step, py(float(v))) for i, v in enumerate(vals)]
        svg.append('<polyline class="series-line" fill="none" stroke="#2a78d6" stroke-width="2" points="' +
                   ' '.join(f'{a:.1f},{b:.1f}' for a,b in coords) + '"/>')
        for i, (xx, yy) in enumerate(coords):
            shape = 'rect' if i in signal_idx else 'circle'
            occasion = labels[i] if title.startswith("Individuales") else labels[i+1]
            if shape == 'circle':
                svg.append(f'<circle tabindex="0" cx="{xx:.1f}" cy="{yy:.1f}" r="5" fill="#2a78d6" stroke="#fcfcfb" stroke-width="2"><title>Ocasión {occasion}: {fmt(vals[i], 4)} nmol/mol</title></circle>')
            else:
                svg.append(f'<rect tabindex="0" x="{xx-5:.1f}" y="{yy-5:.1f}" width="10" height="10" fill="#2a78d6" stroke="#fcfcfb" stroke-width="2"><title>Señal en ocasión {occasion}, valor {fmt(vals[i], 4)} nmol/mol</title></rect>')
        svg.append(f'<text x="{left}" y="{top+height+18}" fill="#52514e">Ocasión</text>')
        for i in range(len(vals)):
            xx = left + (i + offset) * step
            lab = labels[i + offset]
            svg.append(f'<text x="{xx:.1f}" y="{top+height+35}" text-anchor="middle" fill="#52514e">{lab}</text>')
    svg.append('</svg>')
    table_rows = ''.join(f'<tr><th scope="row">{i}</th><td>{fmt(v, 4)}</td><td>{"—" if i == 1 else fmt(mr[i-2], 4)}</td></tr>' for i,v in enumerate(x,1))
    legend = '<p><span class="key series"></span>Respuesta; <span class="key center"></span>Centro; <span class="key limit"></span>Límites (trazo discontinuo). Cuadrados: puntos señalados.</p>'
    html = f'''<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Práctica B — carta I-MR</title>
<style>:root{{color-scheme:light dark}}.viz-root{{--surface-1:#fcfcfb;--text-primary:#0b0b0b;--text-secondary:#52514e;--series-1:#2a78d6;--center:#6b6b68;--limit:#eb6834;--grid:#e1e0d9;color:var(--text-primary);background:var(--surface-1);font:16px system-ui,sans-serif;max-width:900px;margin:2rem auto;padding:0 1rem}}svg{{width:100%;height:auto}}.key{{display:inline-block;width:22px;border-top:2px solid;margin:0 5px}}.series{{border-color:var(--series-1)}}.center{{border-color:var(--center)}}.limit{{border-color:var(--limit);border-top-style:dashed}}table{{border-collapse:collapse;font-variant-numeric:tabular-nums}}th,td{{padding:.4rem .8rem;border-bottom:1px solid var(--grid);text-align:right}}caption{{text-align:left;font-weight:600}}@media(prefers-color-scheme:dark){{:root:not([data-theme="light"]) .viz-root{{color-scheme:dark;--surface-1:#1a1a19;--text-primary:#f0efec;--text-secondary:#c3c2b7;--series-1:#3987e5;--center:#898781;--limit:#d95926;--grid:#2c2c2a}}}}:root[data-theme="dark"] .viz-root{{color-scheme:dark;--surface-1:#1a1a19;--text-primary:#f0efec;--text-secondary:#c3c2b7;--series-1:#3987e5;--center:#898781;--limit:#d95926;--grid:#2c2c2a}}svg text{{fill:var(--text-secondary)!important}}svg .series-line{{stroke:var(--series-1)}}svg .grid{{stroke:var(--grid)}}svg .center-line{{stroke:var(--center)}}svg .limit-line{{stroke:var(--limit)}}</style>
<div class="viz-root"><h1>Práctica B: carta I-MR docente</h1><p>Datos simulados deterministas; no son resultados de CALAIRE. Unidades: nmol/mol.</p>{legend}{''.join(svg)}
<table><caption>Datos accesibles de la carta</caption><thead><tr><th>Ocasión</th><th>Individual (nmol/mol)</th><th>MR que termina aquí (nmol/mol)</th></tr></thead><tbody>{table_rows}</tbody></table></div></html>'''
    output = Path(__file__).parents[1] / "M11_practica_B_grafico.html"
    output.write_text(html, encoding="utf-8")
    print("Gráfico accesible:", output)


if __name__ == "__main__":
    practica_b()
    practica_i()
    practica_a()
