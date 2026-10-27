"""Reproduce los ejemplos numéricos docentes del capítulo M11."""

import numpy as np
from scipy import stats


def carta_imr():
    # Serie simulada: desviaciones de pendiente respecto de 1, en unidades de pendiente.
    x = np.array([0.0000, 0.0004, -0.0002, 0.0001, 0.0005, 0.0018, 0.0002, -0.0001])
    baseline = x[:5]
    baseline_mr = np.abs(np.diff(baseline))
    mr = np.abs(np.diff(x))
    mr_bar = baseline_mr.mean()
    center = baseline.mean()
    lcl = center - 2.66 * mr_bar
    ucl = center + 2.66 * mr_bar
    mr_ucl = 3.267 * mr_bar
    signals = np.flatnonzero((x < lcl) | (x > ucl)) + 1
    mr_signals = np.flatnonzero(mr > mr_ucl) + 2
    return x, mr, center, mr_bar, lcl, ucl, mr_ucl, signals, mr_signals


def carta_nist_publicada():
    # NISTIR 6963, Tabla 4, p. 20; orden de las diez corridas publicadas.
    slopes = np.array([0.99897, 1.00007, 0.99997, 1.00041, 0.99996,
                       1.00026, 1.00071, 1.00073, 1.00013, 0.99910])
    deviations = slopes - 1
    center = deviations.mean()
    mr = np.abs(np.diff(deviations))
    mr_bar = mr.mean()
    lcl, ucl = center - 2.66 * mr_bar, center + 2.66 * mr_bar
    mr_ucl = 3.267 * mr_bar
    np.testing.assert_allclose([center, mr_bar, lcl, ucl, mr_ucl],
                               [0.000031, 0.000498889, -0.001296044,
                                0.001358044, 0.001629870], atol=1e-9, rtol=0)
    assert not np.any((deviations < lcl) | (deviations > ucl))
    assert not np.any(mr > mr_ucl)
    print("I — NISTIR 6963 Tabla 4: pendientes publicadas", slopes.tolist())
    print(f"centro={center:.9f}; MR medio={mr_bar:.9f}; LIC={lcl:.9f}; LSC={ucl:.9f}; LSC_MR={mr_ucl:.9f}; sin señales de punto ni MR")


def regresion_deriva():
    # Serie docente simulada en nmol/mol; intervalos de 30 días.
    t_days = np.arange(0, 181, 30, dtype=float)
    y = np.array([0.10, 0.18, 0.25, 0.37, 0.44, 0.56, 0.63])
    slope, intercept, r, p, se_slope = stats.linregress(t_days, y)
    residuals = y - (intercept + slope * t_days)
    s = np.sqrt(np.sum(residuals**2) / (len(y) - 2))
    xbar = t_days.mean()
    sxx = np.sum((t_days - xbar) ** 2)
    tcrit = stats.t.ppf(0.975, len(y) - 2)
    se_mean_120 = s * np.sqrt(1 / len(y) + (120 - xbar) ** 2 / sxx)
    pred_120 = intercept + slope * 120
    se_future_120 = s * np.sqrt(1 + 1 / len(y) + (120 - xbar) ** 2 / sxx)
    return {
        "slope": slope,
        "intercept": intercept,
        "se_slope": se_slope,
        "ci_slope": (slope - tcrit * se_slope, slope + tcrit * se_slope),
        "p": p,
        "residual_sd": s,
        "residuals": residuals,
        "prediction_120": pred_120,
        "ci_mean_120": (pred_120 - tcrit * se_mean_120, pred_120 + tcrit * se_mean_120),
        "pi_future_120": (pred_120 - tcrit * se_future_120, pred_120 + tcrit * se_future_120),
        "drift_180": slope * 180,
    }


def ewma_cusum_risk(seed=11026, paths=100_000, horizon=50,
                    lam=0.2, L=2.7, k=0.5, h=5.0):
    """Cuenta trayectorias; cambio +1 sigma en la ocasión 26, sin reiniciar cartas."""
    if paths < 1 or horizon < 26 or not 0 < lam <= 1 or min(L, k, h) <= 0:
        raise ValueError("Se requieren N positivo, horizonte >=26 y parámetros de carta válidos")
    # Simulación reproducible: observaciones normales iid, sigma=1, bajo H0 estable.
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(paths, horizon))
    ewma = np.zeros(paths)
    ewma_alarm = np.zeros(paths, dtype=bool)
    for i in range(horizon):
        ewma = lam * z[:, i] + (1 - lam) * ewma
        limit = L * np.sqrt(lam / (2 - lam) * (1 - (1 - lam) ** (2 * (i + 1))))
        ewma_alarm |= np.abs(ewma) > limit
    # CUSUM bilateral tabular; k y h se expresan en unidades de sigma.
    pos = np.zeros(paths)
    neg = np.zeros(paths)
    cusum_alarm = np.zeros(paths, dtype=bool)
    for i in range(horizon):
        pos = np.maximum(0, pos + z[:, i] - k)
        neg = np.maximum(0, neg - z[:, i] - k)
        cusum_alarm |= (pos > h) | (neg > h)
    p_ewma = ewma_alarm.mean()
    p_cusum = cusum_alarm.mean()
    for name, alarms, p in (("EWMA", ewma_alarm, p_ewma),
                            ("CUSUM bilateral", cusum_alarm, p_cusum)):
        count = int(alarms.sum())
        se = np.sqrt(p * (1 - p) / paths)
        assert p == count / paths
        print(f"A — conteo {name}: {count}/{paths}; p={p:.6f}; error estándar={se:.9f} ({100 * se:.4f} puntos porcentuales)")
    # Valores de regresión solo para la configuración publicada en el libreto.
    if (seed, paths, horizon, lam, L, k, h) == (11026, 100_000, 50, 0.2, 2.7, 0.5, 5.0):
        assert int(ewma_alarm.sum()) == 19909
        assert int(cusum_alarm.sum()) == 9177

    # Alternativa ilustrativa: desplazamiento +1 sigma desde la observación 26.
    alt = rng.normal(size=(paths, horizon))
    alt[:, 25:] += 1.0
    ewma = np.zeros(paths)
    pos = np.zeros(paths)
    neg = np.zeros(paths)
    first_ewma = np.full(paths, horizon, dtype=int)
    first_cusum = np.full(paths, horizon, dtype=int)
    for i in range(horizon):
        ewma = lam * alt[:, i] + (1 - lam) * ewma
        limit = L * np.sqrt(lam / (2 - lam) * (1 - (1 - lam) ** (2 * (i + 1))))
        new_ewma = (first_ewma == horizon) & (np.abs(ewma) > limit)
        first_ewma[new_ewma] = i
        pos = np.maximum(0, pos + alt[:, i] - k)
        neg = np.maximum(0, neg - alt[:, i] - k)
        new_cusum = (first_cusum == horizon) & ((pos > h) | (neg > h))
        first_cusum[new_cusum] = i
    ewma_survivors = first_ewma >= 25
    cusum_survivors = first_cusum >= 25
    ewma_detected = ewma_survivors & (first_ewma < horizon)
    cusum_detected = cusum_survivors & (first_cusum < horizon)
    for name, first, survivors, detected in (
            ("EWMA", first_ewma, ewma_survivors, ewma_detected),
            ("CUSUM bilateral", first_cusum, cusum_survivors, cusum_detected)):
        n_survivors, n_detected = int(survivors.sum()), int(detected.sum())
        n_previous = paths - n_survivors
        n_censored = n_survivors - n_detected
        assert n_previous + n_detected + n_censored == paths
        p_cond = n_detected / n_survivors if n_survivors else np.nan
        se_cond = np.sqrt(p_cond * (1 - p_cond) / n_survivors) if n_survivors else np.nan
        delays = first[detected] - 24
        assert np.all((delays >= 1) & (delays <= horizon - 25))
        print(f"A — alternativa {name}: previas={n_previous}; elegibles={n_survivors}; "
              f"detectadas={n_detected}; censuradas={n_censored}; "
              f"p_cond={p_cond:.9f}; error estándar condicional={se_cond:.9f}")
    p_ewma_shift = ewma_detected.sum() / ewma_survivors.sum() if ewma_survivors.any() else np.nan
    p_cusum_shift = cusum_detected.sum() / cusum_survivors.sum() if cusum_survivors.any() else np.nan
    p_ewma_shift_all = ewma_detected.mean()
    p_cusum_shift_all = cusum_detected.mean()
    # Ocasión 26 (índice 25) cuenta como demora de una observación.
    delay_ewma = np.mean(first_ewma[ewma_detected] - 24) if ewma_detected.any() else np.nan
    delay_cusum = np.mean(first_cusum[cusum_detected] - 24) if cusum_detected.any() else np.nan
    return (seed, horizon, paths, p_ewma, p_cusum,
            p_ewma_shift, p_cusum_shift, p_ewma_shift_all, p_cusum_shift_all,
            delay_ewma, delay_cusum)


def complementos_auditoria():
    """Propagación, recurrencias y riesgo: ejemplos narrados, no ejercicios."""
    d = regresion_deriva()
    phase1 = carta_imr()[0][:5]
    phase2 = phase1 + 0.001
    print(f"I — fases: media1={phase1.mean():.9f}; media2={phase2.mean():.9f}; media mezclada={np.concatenate((phase1, phase2)).mean():.9f}")
    u_delta = 120 * d['se_slope']
    # El resultado calibrado y la pendiente se suponen independientes SOLO aquí.
    u_use = np.hypot(0.020, u_delta)
    print(f"I — incremento a 120 días: {120 * d['slope']:.9f}; u_delta={u_delta:.9f}; u_uso={u_use:.9f} nmol/mol")
    # Recurrencias comprobadas frente a la suma ponderada y suma acumulada.
    x = np.ones(12)
    z = cp = cm = 0.0
    first_e = first_c = None
    for t, value in enumerate(x, 1):
        z = 0.2 * value + 0.8 * z
        cp = max(0, cp + value - 0.5)
        cm = max(0, cm - value - 0.5)
        bound = 2.7 * np.sqrt(0.2 / 1.8 * (1 - 0.8 ** (2 * t)))
        np.testing.assert_allclose(z, 1 - 0.8 ** t)
        np.testing.assert_allclose(cp, 0.5 * t)
        if abs(z) > bound and first_e is None:
            first_e = t
        if max(cp, cm) > 5 and first_c is None:
            first_c = t
        if t in (1, 2):
            print(f"A — ocasión {t}: Z={z:.6f}; límite EWMA={bound:.6f}; C+={cp:.6f}; C-={cm:.6f}")
    print(f"A — serie constante +1: primera señal EWMA={first_e}; CUSUM={first_c} (umbral estricto)")
    # Modelo docente explícito beta~N(b, u_b²), sin ruido adicional ni saltos.
    # Deriva D(t)=beta*t; intervalo de revisión T_r, origen corregido a cero.
    risks = [stats.norm.sf((0.20 / t - d['slope']) / d['se_slope']) for t in (30, 60, 90)]
    for t, risk in zip((30, 60, 90), risks):
        print(f"A — P(exceder +0.20 antes de {t} días)={risk:.9g}; P(cumplir)={1-risk:.9g}")
    assert risks[1] < 0.05 < risks[2]
    rounded_risk = stats.norm.sf((0.20 / 60 - 0.00302381) / 0.00009221)
    assert round(rounded_risk, 5) == round(risks[1], 5) == 0.00039
    print(f"A — riesgo 60 días con parámetros narrados={rounded_risk:.9g}; redondeo común={risks[1]:.5f}")
    np.testing.assert_allclose(d['residuals'],
        [0.010714, 0, -0.020714, 0.008571, -0.012143, 0.017143, -0.003571],
        atol=5e-7, rtol=0)
    carta_nist_publicada()
    a = carta_imr()
    assert a[-2].tolist() == [6] and a[-1].tolist() == [7]
    # Verificación independiente de OLS mediante álgebra matricial.
    times = np.arange(0, 181, 30, dtype=float)
    y = np.array([.10, .18, .25, .37, .44, .56, .63])
    design = np.column_stack((np.ones(7), times))
    beta = np.linalg.lstsq(design, y, rcond=None)[0]
    covariance = d['residual_sd'] ** 2 * np.linalg.inv(design.T @ design)
    np.testing.assert_allclose(beta, [d['intercept'], d['slope']])
    np.testing.assert_allclose(np.sqrt(covariance[1, 1]), d['se_slope'])
    print("Pruebas: I-MR, OLS matricial, EWMA cerrada, CUSUM acumulado y riesgo: OK")


def main():
    x, mr, center, mr_bar, lcl, ucl, mr_ucl, signals, mr_signals = carta_imr()
    print("B — carta I-MR simulada; datos en unidades de pendiente respecto de 1")
    print("valores:", "; ".join(f"{v:.7f}" for v in x))
    print("MR:", "; ".join(f"{v:.7f}" for v in mr))
    print("línea base: primeras cinco observaciones; límites: 3 sigma, constantes 2.66 y 3.267")
    print(f"centro={center:.9f}; MR_bar_base={mr_bar:.9f}; LIC_I={lcl:.9f}; LSC_I={ucl:.9f}; LSC_MR={mr_ucl:.9f}")
    print("señales carta I (número de observación):", signals.tolist())
    print("señales carta MR (número de observación):", mr_signals.tolist())
    y = np.array([0.10, 0.18, 0.25, 0.37, 0.44, 0.56, 0.63])
    print(f"media siete observaciones={y.mean():.9f}; media cinco últimas={y[2:].mean():.9f}; diferencia (cinco últimas - siete)={y[2:].mean() - y.mean():.9f}")

    d = regresion_deriva()
    print("\nI — regresión de deriva simulada; respuesta en nmol/mol, tiempo en días")
    for key, value in d.items():
        print(f"{key}={value}")

    (seed, horizon, paths, p_ewma, p_cusum, p_ewma_shift,
     p_cusum_shift, p_ewma_shift_all, p_cusum_shift_all,
     delay_ewma, delay_cusum) = ewma_cusum_risk()
    print("\nA — riesgo de falsa alarma bajo H0, simulación Monte Carlo iid N(0,1)")
    print(f"seed={seed}; paths={paths}; horizon={horizon}; EWMA(lambda=0.2,L=2.7): P(alarm)={p_ewma:.6f}")
    print(f"CUSUM bilateral(k=0.5,h=5): P(alarm)={p_cusum:.6f}")
    print("Alternativa: +1 sigma desde la observación 26")
    print(f"P(detección | sin alarma previa): EWMA={p_ewma_shift:.6f}; CUSUM={p_cusum_shift:.6f}")
    print(f"P(detección, total): EWMA={p_ewma_shift_all:.6f}; CUSUM={p_cusum_shift_all:.6f}")
    print(f"demora media entre señales detectadas (ocasión 26 cuenta como 1): EWMA={delay_ewma:.3f}; CUSUM={delay_cusum:.3f} observaciones")
    print("cambio esperado por la pendiente I a 30/60/90 días:", "; ".join(f"{d['slope'] * days:.6f}" for days in (30, 60, 90)), "nmol/mol")


if __name__ == "__main__":
    main()
    complementos_auditoria()
