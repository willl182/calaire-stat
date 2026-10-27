"""Cálculos reproducibles de las tres prácticas de M03; todos los datos son simulados."""
from math import sqrt
from pathlib import Path
import numpy as np
from scipy.stats import norm, t as student_t

# B: especificaciones hipotéticas, explícitas y no atribuidas a un equipo.
h = 0.30
u_rect = h / sqrt(3)
delta = 0.10
u_res = delta / sqrt(12)
U, k = 0.60, 2.0
u_U = U / k
u_tri = h / sqrt(6)
t_crit_15 = student_t.ppf(0.975, 15)
t_half_width = t_crit_15 * 0.80 / sqrt(16)
# Comparación de incertidumbre de la media, lectura independiente frente
# a contribución común y serie determinista con deriva conocida por construcción.
sigma, n = 0.80, 16
u_media_iid = sigma / sqrt(n)
u_comun = 0.30
u_media_comun = sqrt(u_comun**2 + sigma**2 / n)
t = np.arange(16, dtype=float)
r = np.tile([-0.8, 0.8, 0.8, -0.8], 4)
y = 420.0 + 0.05 * t + r
media_global = y.mean()
medias_bloque = y.reshape(4, 4).mean(axis=1)
diferencia_mitades = y[8:].mean() - y[:8].mean()
assert np.allclose([u_rect, u_res, u_U, u_tri, u_media_iid], [0.1732050808, 0.02886751346, 0.3, 0.1224744871, 0.2])
assert np.isclose(t_crit_15, 2.1314495456) and np.isclose(t_half_width, 0.4262899091)
assert np.isclose(u_media_comun, sqrt(0.13))
assert np.allclose(medias_bloque, [420.075, 420.275, 420.475, 420.675])
assert np.isclose(media_global, 420.375) and np.isclose(diferencia_mitades, 0.4)

# I: diferencia de dos resultados; covarianza por patrón compartido declarada.
u1, u2, rho = 0.80, 0.60, 0.75
cov = rho * u1 * u2
u_delta_ind = sqrt(u1**2 + u2**2)
u_delta_dep = sqrt(u1**2 + u2**2 - 2 * cov)
assert np.isclose(cov, 0.36) and np.isclose(u_delta_dep, sqrt(0.28))
# I: datos fijados para el ejercicio; normalidad es supuesto de trabajo del gráfico.
residuos = np.array([-0.10, 0.00, 0.10, -0.10, 0.00, 0.10])
ss = float(np.sum(residuos**2))
s2 = ss / (len(residuos) - 1)
blom_p = (np.arange(1, 7) - 0.375) / (6 + 0.25)
blom_q = norm.ppf(blom_p)
prob_plot = np.column_stack((blom_q, np.sort(residuos)))
assert np.isclose(s2, 0.008)
assert np.allclose(blom_q, [-1.2815515655, -0.6433454054, -0.2018934791, 0.2018934791, 0.6433454054, 1.2815515655])
assert np.allclose(prob_plot[:, 1], [-0.1, -0.1, 0., 0., 0.1, 0.1])

# Salida HTML interactiva accesible: un conjunto, marca y tabla equivalente.
def write_probability_html(path: Path) -> None:
    width, height = 760, 500
    left, top, plot_w, plot_h = 90, 70, 590, 310
    x_min, x_max, y_min, y_max = -1.5, 1.5, -0.15, 0.15
    sx = lambda value: left + (value - x_min) / (x_max - x_min) * plot_w
    sy = lambda value: top + (y_max - value) / (y_max - y_min) * plot_h
    visible = lambda value, digits: f"{value:.{digits}f}".replace(".", ",")
    points = "\n".join(
        f'<circle cx="{sx(x):.2f}" cy="{sy(y):.2f}" r="6" fill="#2a78d6" stroke="#fcfcfb" stroke-width="2"><title>Cuantil {visible(x, 2)}; error {visible(y, 2)} nmol/mol</title></circle>'
        for x, y in prob_plot
    )
    x_ticks = [-1, 0, 1]
    y_ticks = [-0.1, 0, 0.1]
    grid = "\n".join(
        f'<line x1="{left}" y1="{sy(y):.2f}" x2="{left+plot_w}" y2="{sy(y):.2f}" stroke="#e1e0d9"/> '
        f'<text x="{left-12}" y="{sy(y)+5:.2f}" text-anchor="end">{visible(y, 1)}</text>' for y in y_ticks
    ) + "\n" + "\n".join(
        f'<line x1="{sx(x):.2f}" y1="{top}" x2="{sx(x):.2f}" y2="{top+plot_h}" stroke="#e1e0d9"/> '
        f'<text x="{sx(x):.2f}" y="{top+plot_h+24}" text-anchor="middle">{x}</text>' for x in x_ticks
    )
    table_rows = "".join(
        f"<tr><td>{visible(x, 2)}</td><td>{visible(y, 2)}</td></tr>" for x, y in prob_plot
    )
    svg = f'''<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gráfico de probabilidad normal — práctica I de M03</title>
<style>
:root {{ color-scheme: light; --surface:#fcfcfb; --ink:#0b0b0b; --muted:#52514e; --series:#2a78d6; --grid:#e1e0d9; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ color-scheme:dark; --surface:#1a1a19; --ink:#f0efec; --muted:#c3c2b7; --series:#3987e5; --grid:#2c2c2a; }} }}
:root[data-theme="dark"] {{ color-scheme:dark; --surface:#1a1a19; --ink:#f0efec; --muted:#c3c2b7; --series:#3987e5; --grid:#2c2c2a; }}
body {{ margin:2rem auto; max-width:850px; padding:0 1rem; background:var(--surface); color:var(--ink); font:16px system-ui,sans-serif; }}
svg {{ width:100%; height:auto; overflow:visible; }} svg text {{ fill:var(--muted); font:14px system-ui,sans-serif; }}
.grid {{ stroke:var(--grid); stroke-width:1; }} .axis {{ stroke:var(--muted); stroke-width:1.2; }} .point {{ fill:var(--series); stroke:var(--surface); stroke-width:2; }}
table {{ border-collapse:collapse; margin-top:1rem; }} th,td {{ padding:.4rem .8rem; border-bottom:1px solid var(--grid); text-align:right; }}
</style><body><main><h1>Gráfico de probabilidad normal</h1><p>Práctica I de M03 · datos fijados para el ejercicio · errores (nmol/mol)</p>
<svg viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc"><title id="title">Gráfico de probabilidad normal de seis errores simulados</title><desc id="desc">Cuantiles normales teóricos de Blom frente a errores ordenados. Los seis puntos muestran empates en menos 0,10, cero y 0,10 nmol/mol; no certifican normalidad.</desc>
{grid}<line class="axis" x1="{left}" y1="{top+plot_h}" x2="{left+plot_w}" y2="{top+plot_h}"/><line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}"/>{points}
<text x="{left+plot_w/2}" y="{height-20}" text-anchor="middle">Cuantil normal teórico</text><text transform="translate(24 {top+plot_h/2}) rotate(-90)" text-anchor="middle">Error observado (nmol/mol)</text></svg>
<h2>Tabla accesible de los puntos</h2><table><caption>Posiciones de Blom, cuantiles y errores ordenados</caption><thead><tr><th>Cuantil normal teórico</th><th>Error observado (nmol/mol)</th></tr></thead><tbody>{table_rows}</tbody></table>
<p>Serie única: el título identifica la serie; las marcas azules tienen forma circular y contorno de superficie. Pase el puntero sobre cada punto para consultar sus valores. La figura no constituye una prueba de normalidad.</p></main></body></html>'''
    path.write_text(svg, encoding="utf-8")

write_probability_html(Path(__file__).with_name("M03_practica_I_probabilidad.html"))

# A: matriz de covarianza pequeña, variaciones de canal (V) y punto (nmol/mol).
# Dos canales del mismo punto: covarianza de lectura compartida.
Vcan = np.array([[0.04, 0.03], [0.03, 0.09]])
# Dos puntos: incertidumbre común multiplicativa relativa 1 %.
Vpt = np.array([[1.0, 4.0], [4.0, 16.0]])
for V in (Vcan, Vpt):
    assert np.allclose(V, V.T)
    assert np.linalg.eigvalsh(V).min() >= -1e-12
u_ratio = sqrt((0.2/0.8)**2 + (1.0*0.3/0.8**2)**2 - 2*1.0*0.03/0.8**3)
u_point_difference = sqrt(np.array([-1., 1.]) @ Vpt @ np.array([-1., 1.]))
u_point_independent = sqrt(Vpt[0,0] + Vpt[1,1])
# Estimador muestral del ejemplo impreso: Pearson entre listas desplazadas.
serie_autocorr_A2 = np.array([1, 0.5, -0.5, -1, -0.5, 0.5, 1, 0.5, -0.5, -1, -0.5, 0.5, 1.0])
lag1 = np.corrcoef(serie_autocorr_A2[:-1], serie_autocorr_A2[1:])[0, 1]
assert len(serie_autocorr_A2) == 13 and np.isclose(lag1, 0.5)
assert len(y) == 16  # serie distinta, con deriva, usada para los bloques.
# Estrategia de promedio sobre una serie con deriva conocida y ruido centrado.
block_means = y.reshape(4,4).mean(axis=1)
corrected = y - 0.05*t
corrected_block_means = corrected.reshape(4,4).mean(axis=1)
u_ratio_sin_cov = sqrt((0.2/0.8)**2 + (0.3/0.8**2)**2)
u_ratio_var_sin_cov = (1.25**2)*0.04 + (1.5625**2)*0.09
assert np.isclose(u_ratio, 0.40625)
assert np.isclose(u_ratio_sin_cov, sqrt(0.2822265625))
assert np.isclose(u_ratio_var_sin_cov, 0.2822265625)
assert np.isclose(u_point_difference, 3.0) and np.isclose(u_point_independent, sqrt(17))
assert np.allclose(corrected_block_means, 420.0)
# Matriz inválida: simétrica pero no semidefinida positiva.
V_bad = np.array([[1., 1.2], [1.2, 1.]])
assert np.linalg.eigvalsh(V_bad).min() < 0

for name, value in [
    ('B_u_rectangular',u_rect),('B_u_resolucion',u_res),('B_u_U_sobre_k',u_U),('B_u_triangular',u_tri),('B_t_critico_df15',t_crit_15),('B_semiancho_t_95',t_half_width),
    ('B_u_media_iid',u_media_iid),('B_u_media_con_comun',u_media_comun),
    ('B_media_serie',media_global),('B_diferencia_mitades',diferencia_mitades),
    ('I_covarianza',cov),('I_u_diferencia_independiente',u_delta_ind),('I_u_diferencia_correlacionada',u_delta_dep),
    ('I_varianza_muestral_descriptiva',s2),('A2_corr_serie_autocorr_13_valores_lag1',lag1),
    ('A_u_razon_canales',u_ratio),('A_u_razon_sin_cov',u_ratio_sin_cov),('A_u_diferencia_puntos',u_point_difference),('A_u_diferencia_sin_cov',u_point_independent)]:

    print(f'{name}={value:.10g}')
print('B_medias_bloque='+str(medias_bloque.tolist()))
print('I_grafico_probabilidad_x_teorico_y_observado='+str(prob_plot.tolist()))
print('I_salida_grafica=M03_practica_I_probabilidad.html')
print('A_Vcan='+str(Vcan.tolist()))
print('A_Vpt='+str(Vpt.tolist()))
print('A_autovalores_Vcan='+str(np.linalg.eigvalsh(Vcan).tolist()))
print('A_autovalores_Vpt='+str(np.linalg.eigvalsh(Vpt).tolist()))
print('A_autovalores_V_invalida='+str(np.linalg.eigvalsh(V_bad).tolist()))
print('A_medias_bloque='+str(block_means.tolist()))
print('A_medias_corregidas_t0='+str(corrected_block_means.tolist()))
print('comprobaciones_M03_practicas=OK')
