import csv
import math
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent


def read_csv(name):
    with (HERE / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def simpson(f, a, b, n=6000):
    if b <= a:
        return 0.0
    if n % 2:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h / 3 * (y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum())


def gamma_p(a, x):
    if x <= 0:
        return 0.0
    norm = math.gamma(a)
    return simpson(lambda t: np.where(t > 0, t ** (a - 1) * np.exp(-t), 0.0), 0, x) / norm


def chi_critical(df, probability=0.95):
    lo, hi = 0.0, max(10.0, df * 5.0)
    for _ in range(70):
        mid = (lo + hi) / 2
        if gamma_p(df / 2, mid / 2) < probability:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def t_cdf(t, df):
    if t == 0:
        return 0.5
    sign = 1 if t > 0 else -1
    c = math.gamma((df + 1) / 2) / (math.sqrt(df * math.pi) * math.gamma(df / 2))
    area = simpson(lambda z: c * (1 + z * z / df) ** (-(df + 1) / 2), 0, abs(t))
    return 0.5 + sign * area


def t_critical(df, probability=0.975):
    lo, hi = 0.0, 20.0
    for _ in range(70):
        mid = (lo + hi) / 2
        if t_cdf(mid, df) < probability:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def f_cdf(value, d1, d2):
    if value <= 0:
        return 0.0
    z = d1 * value / (d1 * value + d2)
    a, b = d1 / 2, d2 / 2
    beta = math.gamma(a) * math.gamma(b) / math.gamma(a + b)
    return simpson(lambda q: np.where((q > 0) & (q < 1), q ** (a - 1) * (1 - q) ** (b - 1), 0.0), 0, z) / beta


def f_critical(d1, d2, probability=0.95):
    lo, hi = 0.0, 1000.0
    for _ in range(70):
        mid = (lo + hi) / 2
        if f_cdf(mid, d1, d2) < probability:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def line_fit(x, y):
    X = np.column_stack((np.ones(len(x)), x))
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    residual = y - X @ beta
    covariance = np.linalg.inv(X.T @ X) * (residual @ residual) / (len(x) - 2)
    return beta, covariance, residual


def ggmr_fit(x, y, Ux, Uy, start=None, max_iter=100):
    n = len(x)
    U = np.block([[Ux, np.zeros_like(Ux)], [np.zeros_like(Uy), Uy]])
    t = np.r_[x.copy(), line_fit(x, y)[0] if start is None else np.array(start, float)]
    for _ in range(max_iter):
        xx, a, b = t[:n], t[n], t[n + 1]
        f = np.r_[x - xx, y - a - b * xx]
        J = np.zeros((2 * n, n + 2))
        J[:n, :n] = -np.eye(n)
        J[n:, :n] = -b * np.eye(n)
        J[n:, n] = -1.0
        J[n:, n + 1] = -xx
        L = np.linalg.cholesky(U)
        ft = np.linalg.solve(L, f)
        Jt = np.linalg.solve(L, J)
        H = Jt.T @ Jt
        g = Jt.T @ ft
        delta = np.linalg.solve(H, -g)
        t += delta
        if np.max(np.abs(delta)) < 1e-11:
            break
    xx, a, b = t[:n], t[n], t[n + 1]
    f = np.r_[x - xx, y - a - b * xx]
    J = np.zeros((2 * n, n + 2))
    J[:n, :n] = -np.eye(n)
    J[n:, :n] = -b * np.eye(n)
    J[n:, n] = -1.0
    J[n:, n + 1] = -xx
    L = np.linalg.cholesky(U)
    ft = np.linalg.solve(L, f)
    Jt = np.linalg.solve(L, J)
    H = Jt.T @ Jt
    cov_all = np.linalg.inv(H)
    return np.array([a, b]), cov_all[-2:, -2:], float(ft @ ft), U


def desc(v):
    return float(np.mean(v)), float(np.std(v, ddof=1)), float(np.min(v)), float(np.max(v))


def chart(v, baseline_mean, d2=1.128):
    mr = np.abs(np.diff(v))
    mrbar = np.mean(mr)
    sigma = mrbar / d2
    xlimits = (baseline_mean - 2.66 * mrbar, baseline_mean + 2.66 * mrbar)
    rlimits = (0.0, 3.267 * mrbar)
    return mr, mrbar, sigma, xlimits, rlimits


def chi_probability(value, df):
    return gamma_p(df / 2, value / 2)


def main():
    B = read_csv("datos_caso_B.csv")
    x36 = np.array([float(r["srp36_nmol_mol"]) for r in B])
    y7 = np.array([float(r["srp7_nmol_mol"]) for r in B])
    sd36 = np.array([float(r["sd_srp36_nmol_mol"]) for r in B])
    sd7 = np.array([float(r["sd_srp7_nmol_mol"]) for r in B])
    x7, y36 = y7, x36
    beta_pub, cov_pub, res_pub = line_fit(x36, y7)
    beta_rev, cov_rev, res_rev = line_fit(x7, y36)
    print("CASO B — OLS, orientación publicada SRP36 -> SRP7")
    print(f"a={beta_pub[0]:.9f}; b={beta_pub[1]:.9f}; u(a)={math.sqrt(cov_pub[0,0]):.9f}; u(b)={math.sqrt(cov_pub[1,1]):.9f}; cov(a,b)={cov_pub[0,1]:.9g}; R2={1-(res_pub@res_pub)/np.sum((y7-y7.mean())**2):.9f}; s_res={math.sqrt(res_pub@res_pub/10):.9f}")
    print("QAPP publicado: b=1.00169431, a=0.152088621, u(b)=0.00012279, u(a)=0.050351308, R2=0.99999985, s=0.114028881, Res Std Dev=0.108722272, cov=-5.24592e-09; 12 puntos")
    print("CASO B — OLS, orientación didáctica SRP7 -> SRP36")
    print(f"a={beta_rev[0]:.9f}; b={beta_rev[1]:.9f}; s_res={math.sqrt(res_rev@res_rev/10):.9f}")

    rng = np.random.default_rng(20261022)
    n_mc = 200000
    rounded36 = x36 + rng.uniform(-0.05, 0.05, size=(n_mc, len(x36)))
    rounded7 = y7 + rng.uniform(-0.05, 0.05, size=(n_mc, len(y7)))
    xm, ym = rounded36.mean(axis=1), rounded7.mean(axis=1)
    dx = rounded36 - xm[:, None]
    slopes = np.sum(dx * (rounded7 - ym[:, None]), axis=1) / np.sum(dx * dx, axis=1)
    intercepts = ym - slopes * xm
    print(f"MC redondeo uniforme ±0.05, semilla=20261022, n={n_mc}: SD(a)={np.std(intercepts, ddof=1):.9g}; SD(b)={np.std(slopes, ddof=1):.9g}")
    print(f"QAPP publicado respecto a MC: a={0.152088621:.9f} ({(0.152088621-intercepts.mean())/np.std(intercepts,ddof=1):.3f} SD; percentil={100*np.mean(intercepts<=0.152088621):.3f}); b={1.00169431:.9f} ({(1.00169431-slopes.mean())/np.std(slopes,ddof=1):.3f} SD; percentil={100*np.mean(slopes<=1.00169431):.3f})")

    ub = 2.92e-3
    def uncertainty_cov(v, u_random):
        return np.diag(u_random**2) + ub**2 * np.outer(v, v)
    variants = (
        ("(i) Std. Dev./√12 por punto + componente común", sd7 / math.sqrt(12), sd36 / math.sqrt(12)),
        ("(ii) término genérico 0.28 + componente común", np.full(len(x7), 0.28), np.full(len(y36), 0.28)),
    )
    fits = {}
    for label, ux_random, uy_random in variants:
        Ux, Uy = uncertainty_cov(x7, ux_random), uncertainty_cov(y36, uy_random)
        beta, cov, chi, V = ggmr_fit(x7, y36, Ux, Uy)
        fits[label] = (beta, cov)
        print(f"CASO B — GGMR {label}")
        print(f"u_b={ub}; diag(Ux)={np.diag(Ux)}; diag(Uy)={np.diag(Uy)}; cov común fuera diagonal: u_b²*x_i*x_j / u_b²*y_i*y_j")
        print(f"a={beta[0]:.9f}; b={beta[1]:.9f}; u(a)={math.sqrt(cov[0,0]):.9f}; u(b)={math.sqrt(cov[1,1]):.9f}; cov(a,b)={cov[0,1]:.9g}; chi2_obs={chi:.9f}; nu=10; chi2_95={chi_critical(10):.6f}; P(chi2≤obs)={chi_probability(chi,10):.9g}")
        for nominal in (80.0, 420.0):
            D = beta[0] + (beta[1] - 1) * nominal
            uD2 = cov[0, 0] + nominal**2 * cov[1, 1] + 2 * nominal * cov[0, 1]
            uref2 = 0.28**2 + (ub * nominal)**2
            print(f"D({nominal:g})={D:.9f}; uD_interp={math.sqrt(max(0,uD2)):.9f}; uD_direct_Eq3_if_same_budget_for_both={math.sqrt(2*uref2):.9f}")

    iso_x = np.array([50.4, 99.0, 149.9, 200.4, 248.5, 299.7, 349.1])
    iso_y = np.array([52.3, 97.8, 149.7, 200.1, 250.4, 300.9, 349.2])
    iso_Ux = np.array([[.50,0,.25,0,.25,0,.25],[0,1.25,1,0,0,1,1],[.25,1,1.50,0,.25,1,1.25],[0,0,0,1.25,1,1,1],[.25,0,.25,1,1.50,1,1.25],[0,1,1,1,1,2.25,2],[.25,1,1.25,1,1.25,2,2.50]])
    iso_Uy = np.ones((7, 7)) + 4 * np.eye(7)
    iso_beta, iso_cov, iso_chi, _ = ggmr_fit(iso_x, iso_y, iso_Ux, iso_Uy)
    iso_result = np.array([iso_beta[0], iso_beta[1], math.sqrt(iso_cov[0,0]), math.sqrt(iso_cov[1,1]), iso_cov[0,1], iso_chi])
    iso_expected = np.array([0.3424, 1.0012, 2.0569, 0.0090, -0.0129, 1.772])
    if not np.allclose(iso_result, iso_expected, atol=2e-4, rtol=0):
        raise RuntimeError(f"La validación ISO/TS 28037 no coincide: {iso_result}")
    print("VALIDACIÓN ISO/TS 28037:2010, cl. 10, Tabla 25–26 (p.35–36): coincide dentro de atol=2e-4")
    print(f"a={iso_beta[0]:.4f} (ISO 0.3424); b={iso_beta[1]:.4f} (ISO 1.0012); u(a)={math.sqrt(iso_cov[0,0]):.4f} (2.0569); u(b)={math.sqrt(iso_cov[1,1]):.4f} (0.0090); cov={iso_cov[0,1]:.4f} (-0.0129); chi2={iso_chi:.3f} (1.772)")

    c1, c2 = read_csv("datos_caso_C1.csv"), read_csv("datos_caso_C2.csv")
    p1 = np.array([float(r["pendiente_mi"]) for r in c1]); i1 = np.array([float(r["intercepto_Ii_ppb"]) for r in c1])
    p2 = np.array([float(r["pendiente"]) for r in c2]); i2 = np.array([float(r["intercepto_ppb"]) for r in c2]); r2 = np.array([float(r["rsd_ppb"]) for r in c2])
    print("CASO C — descriptiva (media, s muestral, mínimo, máximo)")
    for name, a in (("C1 pendiente",p1),("C1 intercepto",i1),("C2 pendiente",p2),("C2 intercepto",i2),("C2 residual",r2)):
        print(name, "=", tuple(round(x, 9) for x in desc(a)))
    tad_sd = lambda v: math.sqrt(np.sum((v - np.mean(v))**2) / len(v))  # forma de la TAD (1/N; N = 3 en una verificación)
    print(f"TAD SD con divisor N (la TAD usa 1/3 porque N = 3); aplicación orientativa a C1/C2: SD_TAD pendiente C1={tad_sd(p1):.9g}, C2={tad_sd(p2):.9g}; SD muestral={np.std(p1,ddof=1):.9g}/{np.std(p2,ddof=1):.9g}; SD_TAD intercepto C1={tad_sd(i1):.9g}, C2={tad_sd(i2):.9g}; SD muestral={np.std(i1,ddof=1):.9g}/{np.std(i2,ddof=1):.9g}")
    print(f"Aplicación orientativa TAD (no son verificaciones de exactamente 3 regresiones): SD_TAD pendiente C1={tad_sd(p1):.9g}, C2={tad_sd(p2):.9g} (<0.0075); SD_TAD intercepto C1={tad_sd(i1):.9g}, C2={tad_sd(i2):.9g} (<1 ppb); rangos p1,p2,i1,i2 dentro de umbrales={bool(np.all(np.abs(p1-1)<=.03) and np.all(np.abs(p2-1)<=.03) and np.all(np.abs(i1)<=3) and np.all(np.abs(i2)<=3))}")
    print(f"QAPP 6x6 C1 (6 días): RSD de seis pendientes=100*s/|media|={100*np.std(p1,ddof=1)/abs(np.mean(p1)):.9g}%; SD seis interceptos={np.std(i1,ddof=1):.9g} ppb; pendiente todas en 1±3%={bool(np.all(np.abs(p1-1)<=.03))}; intercepto todos en 0±3ppb={bool(np.all(np.abs(i1)<=3))}; cumple SD intercepto <1.5 (asumido ppb)={np.std(i1,ddof=1)<1.5}")
    print(f"C2 como en el resumen publicado (desviación poblacional): media pendiente={np.mean(p2):.8f}, sigma={np.std(p2,ddof=0):.8f}; media intercepto={np.mean(i2):.6f}, sigma={np.std(i2,ddof=0):.6f}; media residual={np.mean(r2):.6f}")

    print("CASO C — carta X-MR: centro/límites fijados con C2; C1 solo superpuesto")
    chart_results = {}
    for label, v in (("pendiente", p2), ("intercepto_ppb", i2)):
        mean, sd, *_ = desc(v)
        mr, mrbar, sig, xl, rl = chart(v, mean)
        chart_results[label] = (mean, xl, rl)
        points = p1 if label == "pendiente" else i1
        mr1 = np.abs(np.diff(points))
        print(f"{label}: Xbar={mean:.9g}; s_C2={sd:.9g}; MRbar={mrbar:.9g}; sigma_hat=MRbar/1.128={sig:.9g}; X límites=({xl[0]:.9g},{xl[1]:.9g}); MR límites 3σ n=2=({rl[0]:.9g},{rl[1]:.9g}); C2 dentro de X límites={((v>=xl[0]) & (v<=xl[1]))}; C1 dentro de X límites={((points>=xl[0]) & (points<=xl[1]))}; MR C1={mr1}; MR C1 dentro={((mr1>=rl[0]) & (mr1<=rl[1]))}; MR C2={mr};")
    var1, var2 = np.var(p1,ddof=1), np.var(p2,ddof=1)
    ratio = max(var1,var2)/min(var1,var2)
    df1, df2 = (len(p1)-1, len(p2)-1) if var1 >= var2 else (len(p2)-1, len(p1)-1)
    fcrit = f_critical(df1, df2, .975)
    print(f"F varianzas pendiente C1/C2: s1²={var1:.12g}; s2²={var2:.12g}; F_mayor/menor={ratio:.9g}; gl=({df1},{df2}); F crítico bilateral 95% (cola superior .975)={fcrit:.6f}; diferencia significativa={ratio>fcrit}")
    order = np.arange(1, len(p2)+1, dtype=float)
    trend, trendcov, tres = line_fit(order, p2)
    tstat = trend[1]/math.sqrt(trendcov[1,1])
    print(f"Deriva C2 pendiente vs orden: a={trend[0]:.9g}; b/corrida={trend[1]:.9g}; SE(b)={math.sqrt(trendcov[1,1]):.9g}; t={tstat:.6f}; gl=8; t crítico bilateral 95%={t_critical(8):.6f}; significativo={abs(tstat)>t_critical(8)}")
    print("Notas cuantiles: χ²/t/F calculados por integración numérica; cifras χ²(10,.95)=18.31; t(8,.975)=2.306; F(.975;9,5)=6.68.")


if __name__ == "__main__":
    main()
