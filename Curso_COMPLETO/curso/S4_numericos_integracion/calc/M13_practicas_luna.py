"""Solución reproducible de la práctica A del M13.

Datos y perturbación didácticos simulados; no proceden de CALAIRE.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import norm
import statsmodels.api as sm
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("M13_ejemplos", Path(__file__).with_name("M13_ejemplos.py"))
if _spec is None or _spec.loader is None:
    raise ImportError("No se pudo cargar M13_ejemplos.py")
ejemplos = module_from_spec(_spec)
_spec.loader.exec_module(ejemplos)


def main() -> None:
    rng = np.random.default_rng(ejemplos.SEED)
    np.set_printoptions(precision=10, suppress=True)

    # Apartado 1: entradas normales conjuntas y calibración inversa.
    means = np.array([420.0, 0.40, 1.002])
    sds = np.array([0.80, 0.50, 0.002])
    corr = np.array([[1, 0, 0], [0, 1, -0.60], [0, -0.60, 1]], dtype=float)
    cov = np.outer(sds, sds) * corr
    gradient = np.array([1 / means[2], -1 / means[2], -(means[0] - means[1]) / means[2] ** 2])
    estimate = (means[0] - means[1]) / means[2]
    u_linear = np.sqrt(gradient @ cov @ gradient)
    draws = rng.multivariate_normal(means, cov, size=ejemplos.N_MC)
    inverse = (draws[:, 0] - draws[:, 1]) / draws[:, 2]
    interval_mc = np.quantile(inverse, [0.025, 0.975])
    interval_linear = estimate + np.array([-1, 1]) * norm.ppf(0.975) * u_linear
    endpoint_diff = np.abs(interval_linear - interval_mc)
    print("A1: xhat, u_lineal =", estimate, u_linear)
    print("A1: media_MC, sd_MC, IC95_MC =", inverse.mean(), inverse.std(ddof=1), interval_mc)
    print("A1: IC95_lineal, diferencias_extremos =", interval_linear, endpoint_diff)
    assert np.all(endpoint_diff <= 0.05)

    # Apartados 2-3: seis días como bloques completos.
    levels = ejemplos.LEVELS
    x = np.tile(levels, (6, 1))
    y = ejemplos.daily_observations(x)
    beta, cov_beta = ejemplos.daily_fit(x, y)
    uses = np.array([80., 250., 420.])
    inverses = (uses - beta[0]) / beta[1]
    corrections = inverses - uses
    jac = np.zeros((5, 2))
    jac[:2, :] = np.eye(2)
    jac[2:, 0] = -1 / beta[1]
    jac[2:, 1] = -(uses - beta[0]) / beta[1] ** 2
    cov_outputs = jac @ cov_beta @ jac.T
    # Diferencias finitas centradas validan la jacobiana analítica de las salidas.
    step = 1e-5
    finite_jac = np.empty_like(jac)
    for j in range(2):
        plus = beta.copy()
        minus = beta.copy()
        plus[j] += step
        minus[j] -= step
        q_plus = np.r_[plus, (uses - plus[0]) / plus[1] - uses]
        q_minus = np.r_[minus, (uses - minus[0]) / minus[1] - uses]
        finite_jac[:, j] = (q_plus - q_minus) / (2 * step)
    finite_cov_outputs = finite_jac @ cov_beta @ finite_jac.T
    max_relative_difference = np.max(
        np.abs(finite_cov_outputs - cov_outputs)
        / np.maximum(np.abs(cov_outputs), np.finfo(float).tiny)
    )
    assert cov_outputs.shape == (5, 5)
    assert np.allclose(cov_outputs, cov_outputs.T, atol=1e-14)
    assert np.linalg.eigvalsh(cov_outputs).min() >= -1e-12
    print("A2: a, b =", beta)
    print("A2: inversas =", inverses, "correcciones =", corrections)
    print("A2: sd(a,b,c80,c250,c420) =", np.sqrt(np.diag(cov_outputs)))
    print("A2: covarianza conjunta [a,b,c80,c250,c420] =\n", cov_outputs)
    print("A2: discrepancia relativa máxima, jacobiana centrada vs analítica =", max_relative_difference)
    print("A2: observaciones y [nmol/mol], filas=días, columnas=niveles =\n", y)

    bootstrap_rng = rng
    boot = np.empty((ejemplos.N_BOOT, 2))
    for i in range(ejemplos.N_BOOT):
        selected = bootstrap_rng.integers(0, len(ejemplos.DAY_OFFSETS), size=len(ejemplos.DAY_OFFSETS))
        b_rep, _ = ejemplos.linear_fit(x[selected].ravel(), y[selected].ravel())
        boot[i] = (b_rep[1], (250.0 - b_rep[0]) / b_rep[1] - 250.0)
    boot_ci = np.quantile(boot, [0.025, 0.975], axis=0)
    print("A3: IC95 bootstrap pendiente y corrección(250) =\n", boot_ci)
    assert boot.shape == (20_000, 2)

    # Apartado 4: observación final alterada de forma deliberada.
    x_robust = ejemplos.X_ROBUST
    y_clean = ejemplos.Y_CLEAN
    y_altered = y_clean.copy()
    y_altered[-1] += 8.0
    ols_clean, _ = ejemplos.linear_fit(x_robust, y_clean)
    ols_altered, _ = ejemplos.linear_fit(x_robust, y_altered)
    huber = sm.RLM(
        y_altered, sm.add_constant(x_robust),
        M=sm.robust.norms.HuberT(t=1.345),
    ).fit(scale_est="mad", cov="H1", maxiter=1000, tol=1e-12)
    pred_ols = ols_altered[0] + ols_altered[1] * 200
    pred_huber = huber.params[0] + huber.params[1] * 200
    print("A4: OLS limpio =", ols_clean, "OLS alterado =", ols_altered)
    print("A4: Huber =", huber.params, "escala, umbral, peso =", huber.scale, 1.345 * huber.scale, huber.weights[-1])
    print("A4: predicciones a x=200 =", pred_ols, pred_huber)
    assert huber.fit_history["iteration"] < 1000


if __name__ == "__main__":
    main()
