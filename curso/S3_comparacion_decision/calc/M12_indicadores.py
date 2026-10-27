"""Reproduce las cifras didácticas de M12; todos los datos son simulados."""

import numpy as np
from scipy.stats import chi2, t


def main():
    # Diferencias porcentuales firmadas de cuatro verificaciones simuladas.
    audit_b = np.full(4, 100.0)
    meas_b = np.array([98.0, 101.0, 99.0, 102.0])
    errors_b = meas_b - audit_b
    d = errors_b / audit_b * 100
    near_zero_error = 0.50 - 0.20
    near_zero_percent = near_zero_error / 0.20 * 100
    n = d.size
    dbar = float(np.mean(d))
    abs_mean = float(np.mean(np.abs(d)))
    mean_abs = float(abs(dbar))
    s_d = float(np.std(d, ddof=1))
    se_mean = s_d / np.sqrt(n)
    t975 = float(t.ppf(0.975, n - 1))
    mean_ci = (dbar - t975 * se_mean, dbar + t975 * se_mean)
    q10 = float(chi2.ppf(0.10, n - 1))
    cv_upper90 = s_d * np.sqrt((n - 1) / q10)

    abs_d = np.abs(d)
    ab = float(np.mean(abs_d))
    as_ = float(np.std(abs_d, ddof=1))
    t95 = float(t.ppf(0.95, n - 1))
    bias_upper95 = ab + t95 * as_ / np.sqrt(n)

    # Cambio didáctico de escala del monitor; la referencia y el denominador no cambian.
    audit, meas = 100.0, 101.0
    scale = 1.01
    d_before = (meas - audit) / audit * 100
    d_after = (scale * meas - audit) / audit * 100

    # Respuesta del cero simulada; s0 es desviación muestral.
    zero = np.array([-0.2, -0.1, 0.0, 0.1, 0.2])
    s0 = float(np.std(zero, ddof=1))
    threshold_3s = 3 * s0

    # Serie simulada agrupada por dos periodos: componente común de periodo
    # más fluctuación intraperiodo. Se contrasta el SE iid con el de dos medias.
    checks = np.array([0.5, 1.5, 2.5, 3.5])
    naive_se = float(np.std(checks, ddof=1) / np.sqrt(checks.size))
    period_means = checks.reshape(2, 2).mean(axis=1)
    period_se = float(np.std(period_means, ddof=1) / np.sqrt(period_means.size))

    # Contribución común de trazabilidad: promedio de n contribuciones comunes
    # iguales no la reduce por sqrt(n).
    common = 0.8
    common_mean_n2 = float(np.mean([common, common]))
    common_mean_n8 = float(np.mean([common] * 8))

    # Modelo de covarianza declarado; unidades: puntos porcentuales al cuadrado.
    uc, ur = 0.8, 0.6
    aggregate_u = {}
    for count in (2, 8):
        covariance = uc**2 * np.ones((count, count)) + ur**2 * np.eye(count)
        weights = np.full(count, 1.0 / count)
        variance_matrix = float(weights @ covariance @ weights)
        variance_components = uc**2 + ur**2 / count
        assert np.all(np.linalg.eigvalsh(covariance) > 0)
        assert np.isclose(variance_matrix, variance_components)
        aggregate_u[count] = np.sqrt(variance_matrix)

    assert np.allclose(d, [-2, 1, -1, 2])
    assert np.isclose(near_zero_percent, 150)
    assert np.isclose(s_d**2, 10 / 3)
    assert np.isclose(abs_mean, 1.5)
    assert np.isclose(mean_abs, 0)
    assert np.isclose(cv_upper90, 4.136704, atol=5e-7)
    assert np.isclose(bias_upper95, 2.179358, atol=5e-7)
    assert np.isclose(d_after, 2.01)
    assert np.isclose(period_se, 1)
    assert np.allclose([common_mean_n2, common_mean_n8], common)

    print("Origen: ejemplos simulados; no son datos ni desempeño de CALAIRE.")
    print(f"parejas B: audit={audit_b.tolist()}; meas={meas_b.tolist()}; errores={errors_b.tolist()} nmol/mol")
    print(f"cerca de cero: e={near_zero_error:.6f} nmol/mol; d={near_zero_percent:.6f}%; denominador cero: indefinido")
    print(f"modelo común: u(media), n=2: {aggregate_u[2]:.6f}; n=8: {aggregate_u[8]:.6f} puntos porcentuales")
    print(f"d (%)={d.tolist()}; media(d)={dbar:.6f}%; media(|d|)={abs_mean:.6f}%; |media(d)|={mean_abs:.6f}%")
    print(f"s(d)={s_d:.6f}%; SE media={se_mean:.6f}%; IC bilateral 95% media=[{mean_ci[0]:.6f}%, {mean_ci[1]:.6f}%]; t_0.975,3={t975:.6f}")
    print(f"chi2_0.10,3={q10:.6f}; CV/limite superior unilateral 90%={cv_upper90:.6f}%")
    print(f"AB=media(|d|)={ab:.6f}%; AS=s(|d|)={as_:.6f}%; t_0.95,3={t95:.6f}; limite superior 95% sesgo absoluto={bias_upper95:.6f}%")
    print(f"escala monitor {scale:.3f}: d antes={d_before:.6f}%; d despues={d_after:.6f}%")
    print(f"cero={zero.tolist()} nmol/mol; media={np.mean(zero):.6f}; s0={s0:.6f} nmol/mol; 3*s0={threshold_3s:.6f} nmol/mol")
    print(f"verificaciones agrupadas={checks.tolist()}%; medias de periodo={period_means.tolist()}%; SE iid={naive_se:.6f}%; SE de dos periodos={period_se:.6f}%")
    print(f"componente común={common:.6f}%; promedio de dos={common_mean_n2:.6f}%; promedio de ocho={common_mean_n8:.6f}%")


if __name__ == "__main__":
    main()
