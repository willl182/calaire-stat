"""Cálculos reproducibles para los ejemplos didácticos del capítulo M13.

Todos los conjuntos son simulados; no representan resultados de CALAIRE.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import least_squares
from scipy.stats import norm
import statsmodels.api as sm
from math import comb

SEED = 13024
N_MC = 400_000
N_BOOT = 20_000
LEVELS = np.array([40.0, 100.0, 180.0, 260.0, 340.0, 440.0])
DAY_OFFSETS = np.array([-0.38, -0.19, -0.08, 0.11, 0.23, 0.31])
POINT_NOISE = np.array(
    [0.11, -0.07, 0.04, -0.12, 0.09, -0.03,
     -0.06, 0.13, -0.10, 0.05, -0.02, 0.08,
     0.04, -0.09, 0.12, -0.01, -0.11, 0.06,
     -0.13, 0.02, 0.07, -0.04, 0.10, -0.05,
     0.08, -0.03, -0.12, 0.11, -0.06, 0.01,
     -0.02, 0.09, -0.05, 0.12, -0.08, 0.03]
).reshape(6, 6)
X_ROBUST = np.array([20., 70., 120., 170., 220., 270., 320., 370.])
Y_CLEAN = np.array([20.64, 70.46, 120.88, 170.75, 221.00, 270.91, 321.30, 371.20])


def daily_observations(x_grid: np.ndarray) -> np.ndarray:
    return 0.65 + 1.0015 * x_grid + DAY_OFFSETS[:, None] + POINT_NOISE


def linear_fit(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    design = np.column_stack((np.ones_like(x), x))
    beta = np.linalg.lstsq(design, y, rcond=None)[0]
    residuals = y - design @ beta
    covariance = (residuals @ residuals / (len(y) - 2)) * np.linalg.inv(design.T @ design)
    return beta, covariance


def daily_fit(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    daily_beta = np.array([linear_fit(xi, yi)[0] for xi, yi in zip(x, y)])
    return daily_beta.mean(axis=0), np.cov(daily_beta, rowvar=False, ddof=1) / len(daily_beta)


def huber_fit(x: np.ndarray, y: np.ndarray, scale: float) -> np.ndarray:
    design = np.column_stack((np.ones_like(x), x))
    initial = np.linalg.lstsq(design, y, rcond=None)[0]
    result = least_squares(
        lambda beta: design @ beta - y,
        initial,
        loss="huber",
        f_scale=scale,
        max_nfev=10_000,
    )
    return result.x


def main() -> None:
    rng = np.random.default_rng(SEED)
    np.set_printoptions(precision=12, suppress=True)

    # A1: inversa de calibración. a y b comparten una covarianza negativa.
    mean_inputs = np.array([420.0, 0.40, 1.002])  # y [nmol/mol], a [nmol/mol], b
    sd_inputs = np.array([0.80, 0.50, 0.002])
    corr_inputs = np.array(
        [[1.0, 0.0, 0.0], [0.0, 1.0, -0.60], [0.0, -0.60, 1.0]]
    )
    cov_inputs = np.outer(sd_inputs, sd_inputs) * corr_inputs
    draws = rng.multivariate_normal(mean_inputs, cov_inputs, size=N_MC)
    y_draw, a_draw, b_draw = draws.T
    inverse_draw = (y_draw - a_draw) / b_draw
    inverse_mean = float(np.mean(inverse_draw))
    inverse_sd = float(np.std(inverse_draw, ddof=1))
    inverse_interval = np.quantile(inverse_draw, [0.025, 0.975])
    gradient = np.array([1 / mean_inputs[2], -1 / mean_inputs[2], -(mean_inputs[0] - mean_inputs[1]) / mean_inputs[2] ** 2])
    linear_value = (mean_inputs[0] - mean_inputs[1]) / mean_inputs[2]
    linear_sd = float(np.sqrt(gradient @ cov_inputs @ gradient))
    print("A1 inverse calibration")
    print(f"inputs mean={mean_inputs}; sd={sd_inputs}; corr(a,b)={corr_inputs[1,2]:.2f}")
    print(f"MC trials={N_MC}; mean={inverse_mean:.6f}; sd={inverse_sd:.6f}; 95% interval={inverse_interval}")
    print(f"linear value={linear_value:.6f}; linear u={linear_sd:.6f}; MC-linear u difference={inverse_sd-linear_sd:.6f}")

    linear_interval = linear_value + np.array([-1, 1]) * norm.ppf(0.975) * linear_sd
    differences = np.abs(linear_interval - inverse_interval)
    delta = 0.05  # u = 1.0 to two significant digits, GUM-S1 7.9.2.
    print(f"linear 95% interval={linear_interval}; endpoint differences={differences}; delta={delta}; favourable={np.all(differences <= delta)}")
    print(f"MC standard errors: mean={inverse_sd/np.sqrt(N_MC):.6f}; sd (normal approximation)={inverse_sd/np.sqrt(2*(N_MC-1)):.6f}")

    # A2/A3: six-level calibration, six complete day blocks; shared day offsets.
    levels = LEVELS
    day_offsets = DAY_OFFSETS
    x_grid = np.tile(levels, (6, 1))
    y_grid = daily_observations(x_grid)
    beta, cov_beta = daily_fit(x_grid, y_grid)
    _, cov_classical = linear_fit(x_grid.ravel(), y_grid.ravel())
    outputs_y = np.array([80.0, 250.0, 420.0])
    inverse_values = (outputs_y - beta[0]) / beta[1]
    corrections = inverse_values - outputs_y
    # Delta method for [a, b, corrected(y1), corrected(y2), corrected(y3)].
    jacobian = np.zeros((5, 2))
    jacobian[:2, :] = np.eye(2)
    jacobian[2:, 0] = -1 / beta[1]
    jacobian[2:, 1] = -(outputs_y - beta[0]) / beta[1] ** 2
    covariance_outputs = jacobian @ cov_beta @ jacobian.T
    sd_outputs = np.sqrt(np.diag(covariance_outputs))
    corr_outputs = covariance_outputs / np.outer(sd_outputs, sd_outputs)
    print("\nA2 joint outputs")
    print(f"daily mean: df={len(day_offsets)-1}; u(a),u(b)={np.sqrt(np.diag(cov_beta))}")
    print(f"classical OLS corr(a,b)={cov_classical[0,1]/np.sqrt(np.prod(np.diag(cov_classical))):.6f}; u(c250)={np.sqrt(jacobian[3] @ cov_classical @ jacobian[3]):.6f}")
    print(f"observations={x_grid.size}; days={x_grid.shape[0]}; levels={levels}")
    print(f"a={beta[0]:.8f}; b={beta[1]:.8f}; cov(a,b)={cov_beta[0,1]:.10f}")
    print(f"cov(a,b) matrix=\n{cov_beta}")
    for i, y_use in enumerate(outputs_y):
        print(f"y={y_use:.1f}; inverse={inverse_values[i]:.6f}; correction={corrections[i]:.6f}; u(correction)={sd_outputs[i+2]:.6f}")
    print(f"joint covariance [a,b,c80,c250,c420]=\n{covariance_outputs}")
    print(f"joint correlation=\n{corr_outputs}")

    # A3: cluster bootstrap; each selected day contributes its complete 6-level block.
    boot = np.empty((N_BOOT, 2))
    for i in range(N_BOOT):
        selected_days = rng.integers(0, len(day_offsets), size=len(day_offsets))
        b_beta, _ = linear_fit(x_grid[selected_days].ravel(), y_grid[selected_days].ravel())
        boot[i] = (b_beta[1], (250.0 - b_beta[0]) / b_beta[1] - 250.0)
    boot_interval = np.quantile(boot, [0.025, 0.975], axis=0)
    print("\nA3 cluster bootstrap")
    print(f"bootstrap replicates={N_BOOT}; resampled unit=complete day; blocks per replicate={len(day_offsets)}")
    print(f"slope percentile interval={boot_interval[:,0]}")
    print(f"correction at y=250 percentile interval={boot_interval[:,1]}")

    print(f"distinct unordered day multisets={comb(11,6)}; percentile halfwidth/1.96={np.diff(boot_interval,axis=0)[0]/(2*1.96)}")

    # A4: simulated influence point; Huber is defined by SciPy's standard Huber loss.
    x_robust = X_ROBUST
    y_clean = Y_CLEAN
    y_influential = y_clean.copy()
    y_influential[-1] += 8.0
    beta_ols_clean, _ = linear_fit(x_robust, y_clean)
    beta_ols, covariance_ols = linear_fit(x_robust, y_influential)
    robust = sm.RLM(y_influential, sm.add_constant(x_robust), M=sm.robust.norms.HuberT(t=1.345)).fit(scale_est="mad", cov="H1", maxiter=1000, tol=1e-12)
    assert robust.fit_history["iteration"] < 1000
    beta_huber = robust.params
    print("\nA4 OLS versus Huber")
    print(f"influence point x={x_robust[-1]:.1f}; ordinary simulated y={y_clean[-1]:.6f}; altered y={y_influential[-1]:.6f}; alteration=8.0")
    print(f"OLS without alteration: a={beta_ols_clean[0]:.8f}; b={beta_ols_clean[1]:.8f}")
    print(f"OLS with alteration: a={beta_ols[0]:.8f}; b={beta_ols[1]:.8f}")
    print(f"Huber with alteration (k=1.345, MAD scale): a={beta_huber[0]:.8f}; b={beta_huber[1]:.8f}")
    print(f"MAD scale={robust.scale:.9f}; c={1.345*robust.scale:.9f}; H1 standard errors={robust.bse}; altered point weight={robust.weights[-1]:.9f}; OLS standard errors={np.sqrt(np.diag(covariance_ols))}")
    for c in (0.2, 0.35, 1.0, 2.0, 5.0):
        print(f"sensitivity fixed c={c}: slope={huber_fit(x_robust,y_influential,c)[1]:.8f}")
    print(f"prediction at x=200: OLS={beta_ols[0]+beta_ols[1]*200:.6f}; Huber={beta_huber[0]+beta_huber[1]*200:.6f}")
    print(f"OLS residual at influence point={y_influential[-1]-(beta_ols[0]+beta_ols[1]*x_robust[-1]):.6f}; Huber residual={y_influential[-1]-(beta_huber[0]+beta_huber[1]*x_robust[-1]):.6f}")


if __name__ == "__main__":
    main()
