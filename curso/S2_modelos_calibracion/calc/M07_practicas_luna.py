"""Cálculos y gráfico reproducibles de las prácticas M07; datos simulados salvo ISO publicado."""
from pathlib import Path
import numpy as np
from scipy import stats
import importlib.util

_ejemplos_path = Path(__file__).with_name("M07_ejemplos.py")
_spec = importlib.util.spec_from_file_location("M07_ejemplos", _ejemplos_path)
if _spec is None or _spec.loader is None:
    raise ImportError(f"No se pudo cargar el módulo {_ejemplos_path}")
_ejemplos = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ejemplos)
ols, ggmr = _ejemplos.ols, _ejemplos.ggmr

OUT = Path(__file__).resolve().parents[2] / "logs"

# B: conjunto didáctico simulado; mismos valores que el enunciado.
x = np.array([0, 100, 200, 300, 400, 500.], float)
y = np.array([0.2, 100.7, 200.1, 301.0, 400.4, 501.2])
beta, resid, s2, covb = ols(x, y)
a, b = beta
x_use = (250.50-a)/b
print("B OLS", f"a={a:.8f}", f"b={b:.10f}", f"s_res={np.sqrt(s2):.8f}", f"R2={1-(resid@resid)/sum((y-y.mean())**2):.8f}")
print("B residuos", np.round(resid, 8).tolist(), "máximo abs", f"{max(abs(resid)):.8f}")
print("B inversión", f"xhat={x_use:.8f}", f"corrección={x_use-250.50:.8f}")

# Gráfico B: SVG reproducible, con tabla HTML accesible como alternativa textual.
points = [(70 + v/500*680, 180 - r*105) for v,r in zip(x,resid)]
poly = " ".join(f"{px:.1f},{py:.1f}" for px,py in points)
def comma(value, digits=5):
    return f"{value:.{digits}f}".replace(".", ",")

circles = "".join(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="var(--series-1)" tabindex="0"><title>x={v:g}; residuo={comma(r)}</title></circle>' for (px,py),v,r in zip(points,x,resid))
rows = "".join(f"<tr><th scope='row'>{v:g}</th><td>{comma(r)}</td></tr>" for v,r in zip(x,resid))
xticks = "".join(f'<g><line class="grid" x1="{70+v/500*680:.1f}" y1="40" x2="{70+v/500*680:.1f}" y2="240"/><text class="muted" x="{70+v/500*680:.1f}" y="258" text-anchor="middle">{v}</text></g>' for v in range(0,501,100))
yticks = "".join(f'<g><line class="grid" x1="70" y1="{180-v*105:.1f}" x2="750" y2="{180-v*105:.1f}"/><text class="muted" x="58" y="{184-v*105:.1f}" text-anchor="end">{comma(v,1)}</text></g>' for v in [-.4,-.2,0,.2,.4])
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 300" role="img" aria-labelledby="title desc"><title id="title">Residuos OLS de datos simulados</title><desc id="desc">Residuo vertical en nmol/mol frente a referencia en nmol/mol. Ejes marcados cada 100 nmol/mol y cada 0,2 nmol/mol. La línea azul y círculos muestran residuos; la línea gris sólida indica cero. Los puntos permiten foco de teclado y muestran valores; la tabla accesible repite los datos.</desc><style>.surface{{fill:var(--surface)}}.ink{{fill:var(--ink)}}.muted{{fill:var(--muted)}}.axis,.grid{{stroke:var(--axis);stroke-width:1}}.grid{{opacity:.55}}.zero{{stroke:#898781;stroke-width:1}}.series{{stroke:var(--series-1)}}circle{{stroke:var(--surface);stroke-width:2}}:root{{--surface:#fcfcfb;--ink:#0b0b0b;--muted:#52514e;--axis:#c3c2b7;--series-1:#2a78d6}}:root[data-theme="dark"]{{--surface:#1a1a19;--ink:#f0efec;--muted:#c3c2b7;--axis:#383835;--series-1:#3987e5}}@media(prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--surface:#1a1a19;--ink:#f0efec;--muted:#c3c2b7;--axis:#383835;--series-1:#3987e5}}}}</style><rect class="surface" width="820" height="300"/><text class="ink" x="410" y="24" text-anchor="middle" font-family="system-ui" font-size="16">M07-B: residuos del ajuste OLS — simulados</text>{xticks}{yticks}<line class="zero" x1="70" y1="180" x2="750" y2="180"/><line class="axis" x1="70" y1="40" x2="70" y2="240"/><line class="axis" x1="70" y1="240" x2="750" y2="240"/><polyline class="series" points="{poly}" fill="none" stroke-width="2" stroke-linejoin="round"/>{circles}<text class="muted" x="410" y="282" text-anchor="middle" font-family="system-ui" font-size="13">Referencia x (nmol/mol)</text><text class="muted" x="18" y="140" transform="rotate(-90 18 140)" text-anchor="middle" font-family="system-ui" font-size="13">Residuo r (nmol/mol)</text><g font-family="system-ui" font-size="12"><line class="series" x1="535" y1="50" x2="560" y2="50" stroke-width="2"/><circle cx="548" cy="50" r="4" fill="var(--series-1)"/><text class="muted" x="566" y="54">Residuo OLS</text><line class="zero" x1="535" y1="68" x2="560" y2="68"/><text class="muted" x="566" y="72">Residuo cero</text></g></svg>'''
html = f'''<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>M07-B residuos OLS simulados</title><style>:root{{color-scheme:light;--surface:#fcfcfb;--ink:#0b0b0b;--line:#c3c2b7}}:root[data-theme="dark"]{{color-scheme:dark;--surface:#1a1a19;--ink:#f0efec;--line:#383835}}@media(prefers-color-scheme:dark){{:root:not([data-theme="light"]){{color-scheme:dark;--surface:#1a1a19;--ink:#f0efec;--line:#383835}}}}body{{font:16px system-ui;color:var(--ink);background:var(--surface);max-width:900px;margin:2rem auto}}table{{border-collapse:collapse}}th,td{{padding:.4rem .8rem;border-bottom:1px solid var(--line);text-align:right}}svg{{width:100%;height:auto}}</style><h1>Residuos OLS — datos simulados</h1><p><button type="button" onclick="document.documentElement.dataset.theme='light'">Tema claro</button> <button type="button" onclick="document.documentElement.dataset.theme='dark'">Tema oscuro</button></p>{svg}<table><caption>Datos del gráfico: referencia y residuo</caption><thead><tr><th scope="col">Referencia x (nmol/mol)</th><th scope="col">Residuo r (nmol/mol)</th></tr></thead><tbody>{rows}</tbody></table></html>'''
(OUT / "M07_B_residuos.html").write_text(html, encoding="utf-8")

# I: OLS/WLS comparados; uso inverso y prueba de falta de ajuste con réplicas verdaderas.
xw = np.array([0,100,200,300,400,500.], float)
yw = np.array([.4,100.5,200.8,300.2,401.4,500.5])
uw = np.array([.25,.30,.40,.60,.90,1.20])
X = np.column_stack((np.ones(len(xw)), xw)); W = np.diag(1/uw**2)
bo = np.linalg.lstsq(X, yw, rcond=None)[0]
bw = np.linalg.solve(X.T@W@X, X.T@W@yw)
print("I OLS", np.round(bo, 8).tolist(), "WLS", np.round(bw, 8).tolist())
Xb = np.column_stack((np.ones(len(x)), x))
x0 = 250.
tcrit = stats.t.ppf(.975, len(x)-2)
leverage = np.array([1., x0]) @ np.linalg.inv(Xb.T@Xb) @ np.array([1., x0])
ci_mean = tcrit*np.sqrt(s2*leverage)
pi_new = tcrit*np.sqrt(s2*(1+leverage))
print("I bandas en x=250", f"IC95 media ±{ci_mean:.8f}", f"IP95 nueva respuesta ±{pi_new:.8f}", "nmol/mol")
print("I pesos 1/u2", np.round(1/uw**2, 6).tolist())
# Incertidumbre inversa de la recta B: u(y) total=0,20, sin doble conteo del residual.
param_var = covb[0,0] + x_use**2*covb[1,1] + 2*x_use*covb[0,1]
u_x = np.sqrt((.20**2 + param_var)/b**2)
nu = (.20**2+param_var)**2/(param_var**2/(len(x)-2))
k = stats.t.ppf(.975, nu)
print("I uso inverso", f"u(xhat)={u_x:.8f}", f"nu_eff={nu:.6f}", f"k95={k:.6f}", f"U95={k*u_x:.8f}")
xr = np.repeat([0.,100.,200.,300.], 3)
yr = np.array([.1,.2,.3,100.2,100.1,100.3,200.,200.1,200.2,301.,301.1,301.2])
br, _, _, _ = ols(xr, yr)
means = np.array([yr[xr == v].mean() for v in np.unique(xr)])
sslof = sum(3*(m-(br[0]+br[1]*v))**2 for v,m in zip(np.unique(xr),means))
sspe = sum(np.sum((yr[xr==v]-yr[xr==v].mean())**2) for v in np.unique(xr))
F = (sslof/2)/(sspe/8); p = stats.f.sf(F,2,8)
print("I falta de ajuste", f"SS_LOF={sslof:.6f}", f"SS_PE={sspe:.6f}", f"F(2,8)={F:.6f}", f"p={p:.8g}")

# A: conjunto común simulado y el contraste numérico publicado de ISO/TS 28037.
xa=np.array([0.,100.,200.,300.,400.,500.]); ya=np.array([.3,100.4,200.7,300.5,401.,500.9])
ux=np.full(6,.25); uy=np.full(6,.4); Vx=np.diag(ux**2)+.12**2*np.ones((6,6)); Vy=np.diag(uy**2)
fit,cov=ggmr(xa,ya,Vx,Vy); ag,bg=fit.x[:2]
Xg=np.column_stack((np.ones(6),xa)); ol=np.linalg.lstsq(Xg,ya,rcond=None)[0]; wl=np.linalg.lstsq(Xg/uy[:,None],ya/uy,rcond=None)[0]
fit0,cov0=ggmr(xa,ya,np.diag(ux**2),Vy)
print("A mismo conjunto OLS",np.round(ol,8).tolist(),"WLS",np.round(wl,8).tolist(),"GGMR",np.round([ag,bg],8).tolist())
Q = float(fit.fun@fit.fun)
p_upper = stats.chi2.sf(Q, 4)
print("A x ajustadas",np.round(fit.x[2:],5).tolist(),"Q",f"{Q:.8f}","df=4",f"p_superior={p_upper:.8f}")
print("A residuos blanqueados zx",np.round(fit.fun[:6],8).tolist(),"zy",np.round(fit.fun[6:],8).tolist(),"suma cuadrados",f"{np.sum(fit.fun**2):.8f}")
print("A componente común",f"u(a) sin={np.sqrt(cov0[0,0]):.8f}",f"con={np.sqrt(cov[0,0]):.8f}",f"u(b)={np.sqrt(cov[1,1]):.8f}")
# Ejemplo publicado de ISO/TS 28037:2010 §10.3, tablas 25–26; datos/matrices sin cambios.
xp=np.array([50.4,99.,149.9,200.4,248.5,299.7,349.1]); yp=np.array([52.3,97.8,149.7,200.1,250.4,300.9,349.2])
vxp=np.array([[.50,0,.25,0,.25,0,.25],[0,1.25,1,0,0,1,1],[.25,1,1.50,0,.25,1,1.25],[0,0,0,1.25,1,1,1],[.25,0,.25,1,1.50,1,1.25],[0,1,1,1,1,2.25,2],[.25,1,1.25,1,1.25,2,2.50]])
vyp=4*np.eye(7)+np.ones((7,7)); fp,cp=ggmr(xp,yp,vxp,vyp)
q=float(fp.fun@fp.fun)
print("A ISO publicado",f"a={fp.x[0]:.7f}",f"b={fp.x[1]:.7f}",f"Q={q:.6f}","objetivo norma: 0,3424; 1,0012; 1,772")
assert np.allclose(fp.x[:2],[.3424,1.0012],atol=5e-5,rtol=0) and abs(q-1.772)<.0005
assert np.allclose(np.sqrt(np.diag(cp)),[2.0569,.0090],atol=5e-5,rtol=0)
print("A comprobación publicada: PASS (parámetros, Q y errores estándar al redondeo de tabla)")
