"""Cálculos reproducibles para los ejemplos didácticos de M06.

Las observaciones ilustrativas son simuladas y no describen resultados de CALAIRE.
Ejecutar con curso/.venv/bin/python desde la raíz del repositorio.
"""
from math import sqrt

import numpy as np
from scipy.stats import beta, chi2, f
from scipy.optimize import minimize_scalar


def one_way(values):
    groups = [np.asarray(group, dtype=float) for group in values]
    a = len(groups)
    n = len(groups[0])
    all_values = np.concatenate(groups)
    grand = all_values.mean()
    means = np.array([group.mean() for group in groups])
    ss_between = n * np.sum((means - grand) ** 2)
    ss_within = sum(np.sum((group - group.mean()) ** 2) for group in groups)
    ss_total = np.sum((all_values - grand) ** 2)
    df_between = a - 1
    df_within = a * (n - 1)
    ms_between = ss_between / df_between
    ms_within = ss_within / df_within
    f_stat = ms_between / ms_within
    sigma2 = ms_within
    tau2 = (ms_between - ms_within) / n
    return {
        "means": means,
        "grand": grand,
        "ss_between": ss_between,
        "ss_within": ss_within,
        "ss_total": ss_total,
        "df_between": df_between,
        "df_within": df_within,
        "ms_between": ms_between,
        "ms_within": ms_within,
        "f": f_stat,
        "f_crit_05": f.ppf(0.95, df_between, df_within),
        "sigma2": sigma2,
        "tau2": tau2,
        "sr": sqrt(sigma2),
        "s_between": sqrt(tau2) if tau2 >= 0 else float("nan"),
    }


def two_way_with_replication(values):
    """Balanced crossed 2x3 example, two observations per cell."""
    x = np.asarray(values, dtype=float)
    a, b, r = x.shape
    grand = x.mean()
    mean_a = x.mean(axis=(1, 2))
    mean_b = x.mean(axis=(0, 2))
    mean_cell = x.mean(axis=2)
    ss_a = b * r * np.sum((mean_a - grand) ** 2)
    ss_b = a * r * np.sum((mean_b - grand) ** 2)
    ss_ab = r * np.sum((mean_cell - mean_a[:, None] - mean_b[None, :] + grand) ** 2)
    ss_e = np.sum((x - mean_cell[:, :, None]) ** 2)
    df_a, df_b = a - 1, b - 1
    df_ab = (a - 1) * (b - 1)
    df_e = a * b * (r - 1)
    ms_a, ms_b, ms_ab, ms_e = ss_a / df_a, ss_b / df_b, ss_ab / df_ab, ss_e / df_e
    # Random-factor denominator identities for balanced crossed factors.
    f_a = ms_a / ms_ab
    f_b = ms_b / ms_ab
    f_ab = ms_ab / ms_e
    return locals()


def cochran_c(variances):
    variances = np.asarray(variances, dtype=float)
    return variances.max() / variances.sum()


def main():
    print("B. Precisión del promedio (valores de entrada simulados/ilustrativos)")
    sr, s_between, n, d, k = 0.24, 0.30, 8, 6, 2.0
    u2 = s_between**2 / d + sr**2 / (d * n)
    u = sqrt(u2)
    u_without_between = sr / sqrt(d * n)
    s_daily_means = sqrt(s_between**2 + sr**2 / n)
    u_from_daily_means = s_daily_means / sqrt(d)
    print(f"s_r={sr:.6f}; s_entre={s_between:.6f}; n={n}; d={d}; k={k}")
    print(f"u2_prec={u2:.9f}; u_prec={u:.9f}; U_prec={k*u:.9f}")
    print(f"u_without_between={u_without_between:.9f}")
    print(f"s_medias={s_daily_means:.9f}; u_from_daily_means={u_from_daily_means:.9f}")

    print("\nI. ANOVA un factor aleatorio (datos simulados, tres días y cuatro lecturas/día)")
    groups = [[-0.2, 0.0, 0.1, 0.1], [0.3, 0.5, 0.6, 0.6], [-0.1, 0.1, 0.2, 0.2]]
    result = one_way(groups)
    for key, value in result.items():
        print(f"{key}={np.asarray(value)}")
    df_e = result["df_within"]
    ss_e = result["ss_within"]
    variance_ci = (ss_e / chi2.ppf(0.975, df_e), ss_e / chi2.ppf(0.025, df_e))
    print(f"sigma2_95pct_CI={variance_ci}")
    n_per_day = 4
    tau2_se = sqrt(2 * (result["ms_between"]**2 / result["df_between"] + result["ms_within"]**2 / result["df_within"]) / n_per_day**2)
    tau_se_delta = tau2_se / (2 * result["s_between"])
    print(f"tau2_approx_se={tau2_se:.9f}; s_entre_delta_approx_se={tau_se_delta:.9f}")

    print("\nA. Componente entre días negativa (datos simulados)")
    low_day_shift = [[0.0, 0.2, -0.1, 0.1], [0.05, 0.25, -0.05, 0.15], [-0.03, 0.17, -0.13, 0.07]]
    neg = one_way(low_day_shift)
    print(f"MS_between={neg['ms_between']:.9f}; MS_within={neg['ms_within']:.9f}; raw_tau2={(neg['ms_between']-neg['ms_within'])/4:.9f}")

    # REML normal equilibrado: optimización del cociente lambda=tau2/sigma2.
    # Se perfila sigma2; la constante omitida no depende de los componentes.
    def reml_profile(lam):
        q = neg["ss_within"] + neg["ss_between"]/(1 + 4*lam)
        sigma2 = q/(neg["df_within"] + neg["df_between"])
        return 11*np.log(sigma2) + 2*np.log1p(4*lam)
    fit = minimize_scalar(reml_profile, bounds=(0, 10), method="bounded")
    lam = min((0.0, fit.x), key=reml_profile)
    sigma2_reml = (neg["ss_within"] + neg["ss_between"]/(1+4*lam))/11
    tau2_reml = lam*sigma2_reml
    print(f"REML_restringido_sigma2={sigma2_reml:.9f}; tau2={tau2_reml:.9f}")
    print(f"u_media_truncamiento={sqrt(neg['sigma2']/12):.9f}; "
          f"u_media_REML={sqrt(tau2_reml/3+sigma2_reml/12):.9f}")

    print("\nI. ANOVA cruzado con interacción (datos simulados; A=2, P=3, r=2)")
    crossed = np.array([
        [[0.0, 0.2], [0.1, 0.3], [0.4, 0.6]],
        [[0.3, 0.5], [0.0, 0.2], [0.7, 0.9]],
    ])
    t = two_way_with_replication(crossed)
    for key in ("grand", "ss_a", "ss_b", "ss_ab", "ss_e", "df_a", "df_b", "df_ab", "df_e", "ms_a", "ms_b", "ms_ab", "ms_e", "f_a", "f_b", "f_ab"):
        print(f"{key}={t[key]}")

    signed_daily = crossed - 0.4
    signed = two_way_with_replication(signed_daily)
    print("\nA. Analista x campaña, dos medias diarias firmadas por celda (simulado)")
    print("datos_firmados=", signed_daily.tolist())
    print("componentes_A_B_AB_dia=", (signed["ms_a"]-signed["ms_ab"])/6,
          (signed["ms_b"]-signed["ms_ab"])/4,
          (signed["ms_ab"]-signed["ms_e"])/2, signed["ms_e"])
    print("F_A_B_AB=", signed["f_a"], signed["f_b"], signed["f_ab"])
    print("\nA. Sesgo simulado de un laboratorio, ocho resultados de una jornada")
    print(f"sesgo={100.30-100.00:.9f}; u_media={0.2/sqrt(8):.9f}; "
          f"u_sesgo={sqrt(0.2**2/8+0.05**2):.9f}")

    print("\nI. Cochran C ilustrativo: cuatro grupos normales, n=5 cada uno")
    variances = [0.010, 0.012, 0.011, 0.027]
    c_critical = beta.ppf(1-0.05/4, 4/2, 3*4/2)
    assert c_critical > 0.5  # Las cuatro colas son disjuntas: umbral exacto.
    print(f"variances={variances}; C={cochran_c(variances):.9f}; "
          f"Ccrit_05_n5_p4={c_critical:.9f}; "
          f"senal={cochran_c(variances)>c_critical}")


if __name__ == "__main__":
    main()
