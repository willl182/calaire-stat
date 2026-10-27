"""Recálculo independiente de la revisión Opus (paso 5) de S3.

No reutiliza funciones de los scripts del capítulo: reimplementa cada cálculo
para contrastar las cifras citadas en los libretos M09–M12.
Ejecutar con curso/.venv/bin/python.
"""
from pathlib import Path
import csv
import math

import numpy as np
from scipy import stats, integrate, optimize

ROOT = Path(__file__).resolve().parents[3]
N = stats.norm


def chk(label, value, cited, tol):
    ok = abs(value - cited) <= tol
    print(f"{'OK ' if ok else 'XX '} {label}: calculado={value:.9g}; libreto={cited}")
    return ok


res = []
print("== M09")
res.append(chk("B u(Δ)", math.hypot(.20, .15), .25, 1e-12))
res.append(chk("B E_n", .35 / math.hypot(.40, .30), .70, 1e-12))
res.append(chk("B cobertura k=2 (%)", 100 * (2 * N.cdf(2) - 1), 95.45, 5e-3))
uD = math.sqrt(.2**2 + .15**2 - 2 * 1 * .8 * .15**2)
res.append(chk("I u(Δ) con cov=c1c2u²(R)", uD, .1628, 5e-5))
res.append(chk("I Δ/U(Δ)", .35 / (2 * uD), 1.0750, 5e-5))
res.append(chk("I cov límite u1u2 -> u(Δ)", math.sqrt(.04 + .0225 - 2 * .03), .05, 1e-12))
res.append(chk("I u(D) interpolación", math.sqrt(.1**2 + 200**2 * .0005**2 + 2 * 200 * -3.5e-5), .07746, 5e-6))
res.append(chk("A cuantil chi2 0,95;10", stats.chi2.ppf(.95, 10), 18.3070, 5e-5))

# GGMR independiente: mínimos cuadrados generalizados sobre (a, b, xi) con V_xy=0
rows = list(csv.DictReader((ROOT / "casos_taller/datos_caso_B.csv").open(encoding="utf-8")))
x = np.array([float(r["srp7_nmol_mol"]) for r in rows])
y = np.array([float(r["srp36_nmol_mol"]) for r in rows])
sx = np.array([float(r["sd_srp7_nmol_mol"]) for r in rows])
sy = np.array([float(r["sd_srp36_nmol_mol"]) for r in rows])


def ggmr_indep(ub):
    Ux = np.diag(sx**2 / 12) + ub**2 * np.outer(x, x)
    Uy = np.diag(sy**2 / 12) + ub**2 * np.outer(y, y)
    V = np.block([[Ux, np.zeros_like(Ux)], [np.zeros_like(Uy), Uy]])
    L = np.linalg.cholesky(V)
    m = len(x)

    def r(p):
        a, b, xi = p[0], p[1], p[2:]
        return np.linalg.solve(L, np.concatenate([x - xi, y - a - b * xi]))

    p0 = np.concatenate([[0, 1], x])
    sol = optimize.least_squares(r, p0, xtol=1e-15, ftol=1e-15, gtol=1e-15)
    J = sol.jac
    C = np.linalg.inv(J.T @ J)[:2, :2]
    return sol.x[:2], C, float(sol.fun @ sol.fun)


beta, C, chi = ggmr_indep(.00292)
res.append(chk("A GGMR a", beta[0], -0.184237, 2e-6))
res.append(chk("A GGMR b", beta[1], 0.998350748, 2e-8))
res.append(chk("A GGMR u(a)", math.sqrt(C[0, 0]), 0.031189, 2e-6))
res.append(chk("A GGMR u(b)", math.sqrt(C[1, 1]), 0.004125035, 2e-8))
res.append(chk("A GGMR cov(a,b)", C[0, 1], -3.83046e-6, 2e-10))
res.append(chk("A GGMR chi2", chi, 6.3183, 5e-5))
for x0, Dc, uc in ((80, -0.316177, 0.330548), (420, -0.876923, 1.731867)):
    z = np.array([1, x0])
    res.append(chk(f"A D({x0})", beta[0] + (beta[1] - 1) * x0, Dc, 2e-6))
    res.append(chk(f"A u(D({x0}))", math.sqrt(z @ C @ z), uc, 2e-6))
b0, C0, chi0 = ggmr_indep(0.0)
z = np.array([1, 420])
res.append(chk("A sensibilidad u(D420) sin común", math.sqrt(z @ C0 @ z), 0.048853, 2e-6))
res.append(chk("A sensibilidad chi2 sin común", chi0, 6.318456, 2e-6))
res.append(chk("A GoE u(D) 420", math.hypot(.6, .5), 0.781025, 1e-6))

print("== M10")
u, T = .8, 10
res.append(chk("I P(rechazo|θ=9, g=0)", 1 - (N.cdf((T - 9) / u) - N.cdf((-T - 9) / u)), 0.10564977, 1e-8))
res.append(chk("I P(acept|θ=10,5, g=0)", N.cdf((T - 10.5) / u) - N.cdf((-T - 10.5) / u), 0.26598553, 1e-8))
res.append(chk("I P(acept|θ=10,5, g=1)", N.cdf((9 - 10.5) / u) - N.cdf((-9 - 10.5) / u), 0.03039636, 1e-8))
post = lambda lo, hi: N.cdf((hi - 9.5) / u) - N.cdf((lo - 9.5) / u)
res.append(chk("A P(conforme|y=9,5)", post(-10, 10) / post(-12, 12), 0.73466761, 1e-8))


def glob(g):
    pa = lambda t: N.cdf((T - g - t) / u) - N.cdf((-T + g - t) / u)
    fa = (integrate.quad(pa, -12, -10)[0] + integrate.quad(pa, 10, 12)[0]) / 24
    fr = integrate.quad(lambda t: 1 - pa(t), -10, 10, limit=200)[0] / 24
    return fa, fr


for g, fa_c, fr_c in ((0, 0.02646254, 0.02659615), (1, 0.00337106, 0.08670579)):
    fa, fr = glob(g)
    res.append(chk(f"A global FA g={g}", fa, fa_c, 1e-8))
    res.append(chk(f"A global FR g={g}", fr, fr_c, 1e-8))
ui, ud = .8 / math.sqrt(2), math.sqrt((.64 * 2 + 2 * .48) / 4)
res.append(chk("A u(media) dep", ud, 0.74833148, 1e-8))
res.append(chk("A P_FA indep", N.cdf((9 - 10.5) / ui) - N.cdf((-9 - 10.5) / ui), 0.00400497, 1e-8))
res.append(chk("A P_FA dep", N.cdf((9 - 10.5) / ud) - N.cdf((-9 - 10.5) / ud), 0.02251044, 1e-8))
res.append(chk("B x̂ cero/span", (205 - 5) * 398 / (405 - 5), 199.00, 1e-9))

print("== M11")
v = np.array([0, 4, -2, 1, 5, 18, 2, -1]) * 1e-4
mr = np.abs(np.diff(v))
c, mrb = v[:5].mean(), mr[:4].mean()
res.append(chk("B LSC I", c + 3 * mrb / 1.128, 0.0012905, 2e-6))  # 3/1,128 = 2,6596
res.append(chk("B LSC I (2,66)", c + 2.66 * mrb, 0.0012905, 1e-10))
res.append(chk("B LSC MR", 3.267 * mrb, 0.0013885, 1e-7))
t = np.arange(0, 181, 30.0)
yd = np.array([.10, .18, .25, .37, .44, .56, .63])
lr = stats.linregress(t, yd)
res.append(chk("I pendiente", lr.slope, 0.003024, 5e-7))
res.append(chk("I se pendiente", lr.stderr, 0.0000922, 5e-8))
res.append(chk("I p", lr.pvalue, 4.96e-7, 5e-9))
resid = yd - (lr.intercept + lr.slope * t)
s = math.sqrt(resid @ resid / 5)
X = np.column_stack([np.ones(7), t])
x0 = np.array([1, 120])
h = x0 @ np.linalg.inv(X.T @ X) @ x0
tq = stats.t.ppf(.975, 5)
res.append(chk("I IP futuro 120 sup", x0 @ [lr.intercept, lr.slope] + tq * s * math.sqrt(1 + h), 0.4930, 5e-5))
res.append(chk("I u_uso", math.hypot(120 * lr.stderr, .02), 0.02286, 5e-6))
r1 = np.corrcoef(resid[:-1], resid[1:])[0, 1]
print(f"   (info) autocorrelación lag-1 de residuos de deriva: r1={r1:.4f}; Durbin-Watson={np.sum(np.diff(resid)**2)/np.sum(resid**2):.4f}")
lam, L = .2, 2.7
lim = lambda k: L * math.sqrt(lam / (2 - lam) * (1 - (1 - lam)**(2 * k)))
res.append(chk("A límite EWMA t=2", lim(2), 0.6915, 5e-5))
z = 0
first = None
for k in range(1, 30):
    z = lam + (1 - lam) * z
    if abs(z) > lim(k) and first is None:
        first = k
res.append(chk("A primera alarma EWMA serie de unos", first, 11, 0))
rng = np.random.default_rng(20261026)
Xs = rng.standard_normal((100000, 50))
Z = np.zeros(100000); Cp = np.zeros(100000); Cm = np.zeros(100000)
ae = np.zeros(100000, bool); ac = np.zeros(100000, bool)
for k in range(50):
    Z = lam * Xs[:, k] + (1 - lam) * Z
    ae |= np.abs(Z) > lim(k + 1)
    Cp = np.maximum(0, Cp + Xs[:, k] - .5); Cm = np.maximum(0, Cm - Xs[:, k] - .5)
    ac |= (Cp > 5) | (Cm > 5)
res.append(chk("A MC EWMA falsa alarma (otra semilla)", ae.mean(), 0.19909, 4e-3))
res.append(chk("A MC CUSUM falsa alarma (otra semilla)", ac.mean(), 0.09177, 3e-3))
res.append(chk("A riesgo 60 d", 1 - N.cdf((0.2 / 60 - 0.00302381) / 0.00009221), 0.00039456, 2e-7))

print("== M12")
d = np.array([-2, 1, -1, 2.0])
res.append(chk("I L90", d.std(ddof=1) * math.sqrt(3 / stats.chi2.ppf(.10, 3)), 4.1367, 5e-5))
res.append(chk("I L95 AB", 1.5 + stats.t.ppf(.95, 3) * np.abs(d).std(ddof=1) / 2, 2.1794, 5e-5))
res.append(chk("I IC media", stats.t.ppf(.975, 3) * d.std(ddof=1) / 2, 2.9052, 5e-5))
res.append(chk("I 3s0", 3 * np.array([-.2, -.1, 0, .1, .2]).std(ddof=1), 0.4743, 5e-5))
g = np.array([.5, 1.5, 2.5, 3.5])
res.append(chk("A SE iid", g.std(ddof=1) / 2, 0.6455, 5e-5))
res.append(chk("A SE periodos", np.array([1, 3.]).std(ddof=1) / math.sqrt(2), 1.0, 1e-12))
res.append(chk("A u(media) n=8", math.sqrt(.64 + .36 / 8), 0.8276, 5e-5))
print("TODOS OK" if all(res) else f"FALLOS: {res.count(False)}")
