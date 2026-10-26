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
        "prediction_120": pred_120,
        "ci_mean_120": (pred_120 - tcrit * se_mean_120, pred_120 + tcrit * se_mean_120),
        "pi_future_120": (pred_120 - tcrit * se_future_120, pred_120 + tcrit * se_future_120),
        "drift_180": slope * 180,
    }


def ewma_cusum_risk():
    # Simulación determinista: observaciones normales iid, sigma=1, bajo H0 estable.
    seed = 11026
    rng = np.random.default_rng(seed)
    paths, horizon = 100_000, 50
    z = rng.normal(size=(paths, horizon))
    lam, L = 0.2, 2.7
    ewma = np.zeros(paths)
    ewma_alarm = np.zeros(paths, dtype=bool)
    for i in range(horizon):
        ewma = lam * z[:, i] + (1 - lam) * ewma
        limit = L * np.sqrt(lam / (2 - lam) * (1 - (1 - lam) ** (2 * (i + 1))))
        ewma_alarm |= np.abs(ewma) > limit
    # CUSUM bilateral tabular con k=0.5 sigma y h=5 sigma.
    k, h = 0.5, 5.0
    pos = np.zeros(paths)
    neg = np.zeros(paths)
    cusum_alarm = np.zeros(paths, dtype=bool)
    for i in range(horizon):
        pos = np.maximum(0, pos + z[:, i] - k)
        neg = np.maximum(0, neg - z[:, i] - k)
        cusum_alarm |= (pos > h) | (neg > h)
    p_ewma = ewma_alarm.mean()
    p_cusum = cusum_alarm.mean()

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
    p_ewma_shift = ewma_detected.mean() / ewma_survivors.mean()
    p_cusum_shift = cusum_detected.mean() / cusum_survivors.mean()
    p_ewma_shift_all = ewma_detected.mean()
    p_cusum_shift_all = cusum_detected.mean()
    # Ocasión 26 (índice 25) cuenta como demora de una observación.
    delay_ewma = np.mean(first_ewma[ewma_detected] - 24)
    delay_cusum = np.mean(first_cusum[cusum_detected] - 24)
    return (seed, horizon, paths, p_ewma, p_cusum,
            p_ewma_shift, p_cusum_shift, p_ewma_shift_all, p_cusum_shift_all,
            delay_ewma, delay_cusum)


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
