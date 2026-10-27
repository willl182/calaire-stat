"""Recalcula cifras de la ficha común sin modificar archivos."""
import numpy as np
from scipy.stats import chi2, norm, t


def main():
    baseline = np.array([0, 0.0004, -0.0002, 0.0001, 0.0005])
    moving_range = np.abs(np.diff(baseline)).mean()
    differences = np.array([-2.0, 1.0, -1.0, 2.0])
    absolute = np.abs(differences)
    values = {
        "I-MR centro": baseline.mean(),
        "I LIC": baseline.mean() - 2.66 * moving_range,
        "I LSC": baseline.mean() + 2.66 * moving_range,
        "MR LSC": 3.267 * moving_range,
        "M12 precisión 90 %": differences.std(ddof=1) * np.sqrt(3 / chi2.ppf(0.1, 3)),
        "M12 sesgo absoluto 95 %": absolute.mean() + t.ppf(0.95, 3) * absolute.std(ddof=1) / 2,
        "M12 semianchura IC bilateral 95 %": t.ppf(0.975, 3) * differences.std(ddof=1) / 2,
        "M12 cero 3s0": 3 * np.std([-0.2, -0.1, 0, 0.1, 0.2], ddof=1),
        "M11 riesgo deriva día 60": norm.sf((0.2 - 60 * 0.0030238095) / (60 * 0.0000922139)),
    }
    expected = [0.00016, -0.0009705, 0.0012905, 0.001388475,
                4.136703735091946, 2.1793575062919275, 2.905162715754765,
                0.4743416490252569, 0.0003945566872609004]
    for (label, value), target in zip(values.items(), expected):
        assert np.isclose(value, target, rtol=1e-9, atol=1e-12), (label, value, target)
        print(f"{label}: {value}")


if __name__ == "__main__":
    main()
