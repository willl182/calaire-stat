"""Cálculos reproducibles para las prácticas M12; datos simulados deterministas."""
import math
import numpy as np
from scipy.stats import chi2, t


def resumen(ds):
    x = np.asarray(ds, dtype=float)
    n = len(x)
    return {
        "n": n,
        "mean": float(x.mean()),
        "mean_abs": float(np.abs(x).mean()),
        "abs_mean": float(abs(x.mean())),
        "sd": float(x.std(ddof=1)),
    }


def main():
    # B/I: referencia 100 nmol/mol; indicaciones y diferencias firmadas.
    audit = np.full(6, 100.0)
    meas = np.array([98.0, 101.0, 99.0, 102.0, 97.0, 103.0])
    d = (meas - audit) / audit * 100
    print("B/I", resumen(d))
    print("B abs errors nmol/mol", np.abs(meas - audit).tolist())

    # I: límites para d y |d|, intervalo bilateral de la media firmada.
    n = len(d)
    sd = d.std(ddof=1)
    l90_sd = sd * math.sqrt((n - 1) / chi2.ppf(0.10, n - 1))
    ad = np.abs(d)
    ab, ass = ad.mean(), ad.std(ddof=1)
    l95_ab = ab + t.ppf(0.95, n - 1) * ass / math.sqrt(n)
    half = t.ppf(0.975, n - 1) * sd / math.sqrt(n)
    print("I limits", {"chi2_10": chi2.ppf(.10,n-1), "L90_sd": l90_sd,
          "AB": ab, "AS": ass, "t95_one": t.ppf(.95,n-1),
          "L95_AB": l95_ab, "CI95_mean": [d.mean()-half,d.mean()+half]})
    scaled = 1.01 * meas
    d_scaled = (scaled - audit) / audit * 100
    print("I scale", {"before": d.tolist(), "after": d_scaled.tolist(),
          "after_mean_abs": np.abs(d_scaled).mean()})
    zero = np.array([-0.2, -0.1, 0, 0.1, 0.2])
    print("I zero", {"mean": zero.mean(), "s0": zero.std(ddof=1), "3s0": 3*zero.std(ddof=1)})

    # I scene examples: four differences and the scale / zero examples.
    d4 = np.array([-2.0, 1.0, -1.0, 2.0])
    sd4 = d4.std(ddof=1)
    ad4 = np.abs(d4)
    l90_4 = sd4 * math.sqrt((len(d4) - 1) / chi2.ppf(.10, len(d4) - 1))
    ab4, as4 = ad4.mean(), ad4.std(ddof=1)
    l95_4 = ab4 + t.ppf(.95, len(d4) - 1) * as4 / math.sqrt(len(d4))
    half4 = t.ppf(.975, len(d4) - 1) * sd4 / math.sqrt(len(d4))
    d_scale_example = (1.01 * 101.0 - 100.0) / 100.0 * 100
    zero5 = np.array([-0.2, -0.1, 0.0, 0.1, 0.2])
    print("I scene examples", {"L90_four": l90_4, "L95_AB_four": l95_4,
          "CI95_mean_four": [-half4, half4], "scaled_single_d": d_scale_example,
          "s0_five": zero5.std(ddof=1), "3s0_five": 3*zero5.std(ddof=1)})

    # A: dos periodos distintos; errores absolutos en porcentaje.
    periods = {"antes": np.array([0.5, 1.0, 1.5]),
               "despues": np.array([2.5, 3.0, 3.5])}
    all_d = np.concatenate(list(periods.values()))
    print("A periods", {k: resumen(v) for k, v in periods.items()})
    print("A pooled", resumen(all_d))
    print("A individual errors after", periods["despues"].tolist(), "nmol/mol")
    print("A control signals", {"before": (periods["antes"] > 1.0).tolist(),
          "after": (periods["despues"] > 1.0).tolist()})
    # Common traceability component plus independent standard uncertainty.
    u_common, u_ind = 0.8, 0.6
    print("A common", {n: math.sqrt(u_common**2 + u_ind**2/n) for n in (2, 3, 8)})
    print("A common covariance", u_common**2)


if __name__ == "__main__":
    main()
