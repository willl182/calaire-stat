from pathlib import Path
import csv
import math

import numpy as np
from scipy.optimize import least_squares
from scipy.stats import chi2


ROOT = Path(__file__).resolve().parents[3]


def case_b_data():
    path = ROOT / "casos_taller" / "datos_caso_B.csv"
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    srp36 = np.array([float(row["srp36_nmol_mol"]) for row in rows])
    srp7 = np.array([float(row["srp7_nmol_mol"]) for row in rows])
    sd36 = np.array([float(row["sd_srp36_nmol_mol"]) for row in rows])
    sd7 = np.array([float(row["sd_srp7_nmol_mol"]) for row in rows])
    return srp7, srp36, sd7, sd36


def ggmr(x, y, ux, uy):
    """Fit y=a+b*x with V_xy=0; x and y each may have within-axis covariance."""
    n = len(x)
    covariance = np.block(
        [[ux, np.zeros((n, n))], [np.zeros((n, n)), uy]]
    )
    chol = np.linalg.cholesky(covariance)
    initial = np.r_[x, np.polyfit(x, y, 1)[::-1]]

    def residuals(params):
        latent_x, a, b = params[:n], params[n], params[n + 1]
        raw = np.r_[x - latent_x, y - a - b * latent_x]
        return np.linalg.solve(chol, raw)

    result = least_squares(residuals, initial, xtol=1e-13, ftol=1e-13, gtol=1e-13, max_nfev=10000)
    latent_x, a, b = result.x[:n], result.x[n], result.x[n + 1]
    jac = np.zeros((2 * n, n + 2))
    jac[:n, :n] = -np.eye(n)
    jac[n:, :n] = -b * np.eye(n)
    jac[n:, n] = -1.0
    jac[n:, n + 1] = -latent_x
    whitened_jac = np.linalg.solve(chol, jac)
    parameter_covariance = np.linalg.inv(whitened_jac.T @ whitened_jac)[-2:, -2:]
    chi_square = float(result.fun @ result.fun)
    return np.array([a, b]), parameter_covariance, chi_square


def validate_ggmr():
    x = np.array([50.4, 99.0, 149.9, 200.4, 248.5, 299.7, 349.1])
    y = np.array([52.3, 97.8, 149.7, 200.1, 250.4, 300.9, 349.2])
    U_x = np.array([
        [.50, 0, .25, 0, .25, 0, .25],
        [0, 1.25, 1, 0, 0, 1, 1],
        [.25, 1, 1.50, 0, .25, 1, 1.25],
        [0, 0, 0, 1.25, 1, 1, 1],
        [.25, 0, .25, 1, 1.50, 1, 1.25],
        [0, 1, 1, 1, 1, 2.25, 2],
        [.25, 1, 1.25, 1, 1.25, 2, 2.50],
    ])
    U_y = np.ones((7, 7)) + 4 * np.eye(7)
    beta, parameter_covariance, chi_square = ggmr(x, y, U_x, U_y)
    result = np.array([
        beta[0], beta[1], math.sqrt(parameter_covariance[0, 0]),
        math.sqrt(parameter_covariance[1, 1]), parameter_covariance[0, 1], chi_square,
    ])
    expected = np.array([.3424, 1.0012, 2.0569, .0090, -.0129, 1.772])
    if not np.allclose(result, expected, atol=2e-4, rtol=0):
        raise RuntimeError(f"Validación ISO/TS 28037 no coincide: {result}")
    print("VALIDACION ISO/TS 28037 cl. 10, Tablas 25-26: coincide dentro de atol=0.0002")
    print("a=0.3424; b=1.0012; u(a)=2.0569; u(b)=0.0090; cov(a,b)=-0.0129; chi2=1.772")


def main():
    validate_ggmr()
    print("\nB — diferencia independiente simulada")
    value_1, value_2 = 100.00, 100.35
    u_1, u_2, k = 0.20, 0.15, 2.0
    delta = value_2 - value_1
    U_1, U_2 = k * u_1, k * u_2
    u_delta = math.sqrt(u_1**2 + u_2**2)
    denominator = math.sqrt(U_1**2 + U_2**2)
    E_n = delta / denominator
    print(f"y1={value_1:.6f}; y2={value_2:.6f}; Delta=y2-y1={delta:.6f} nmol/mol")
    print(f"u1={u_1:.6f}; u2={u_2:.6f}; k={k:.6f}; U1={U_1:.6f}; U2={U_2:.6f}")
    print(f"u(Delta)={u_delta:.9f}; denominator_En={denominator:.9f}; E_n={E_n:.9f}; abs(E_n)<=1: {abs(E_n) <= 1}")

    print("\nI — diferencia con patrón compartido simulada")
    u_1, u_2, covariance, k_delta = 0.20, 0.15, 0.018, 2.0
    u_delta_sq = u_1**2 + u_2**2 - 2 * covariance
    if u_delta_sq < 0:
        raise ValueError("La varianza simulada de la diferencia no puede ser negativa")
    u_delta = math.sqrt(u_delta_sq)
    print(f"u1={u_1:.6f}; u2={u_2:.6f}; u1^2={u_1**2:.9f}; u2^2={u_2**2:.9f}; cov12={covariance:.6f} (nmol/mol)^2")
    print(f"u(Delta)^2={u_delta_sq:.9f} (nmol/mol)^2; u(Delta)_independencia={math.sqrt(u_1**2 + u_2**2):.9f}; u(Delta)_cov={u_delta:.9f}")
    print(f"U(Delta)=k_delta*u(Delta), k_delta={k_delta:.6f}: {k_delta*u_delta:.9f} nmol/mol")
    print(f"termino expandido -2*k_delta^2*cov12={-2*k_delta**2*covariance:.9f} (nmol/mol)^2")
    covariance_max = u_1 * u_2
    u_delta_max = math.sqrt(u_1**2 + u_2**2 - 2 * covariance_max)
    print(f"covarianza positiva maxima admisible={covariance_max:.6f} (nmol/mol)^2; u(Delta)={u_delta_max:.6f} nmol/mol")

    print("\nI — interpolacion con parametros simulados")
    a, b = 0.12, 1.001
    u_a, u_b, cov_ab, x0 = 0.10, 0.0005, -0.000035, 200.0
    interpolated_y = a + b * x0
    D = a + (b - 1) * x0
    contribution_a = u_a**2
    contribution_b = x0**2 * u_b**2
    contribution_covariance = 2 * x0 * cov_ab
    variance_D = contribution_a + contribution_b + contribution_covariance
    if variance_D < 0:
        raise ValueError("La varianza interpolada no puede ser negativa")
    print(f"a={a:.6f} nmol/mol; b={b:.9f}; x0={x0:.6f} nmol/mol; interpolated_y={interpolated_y:.9f}; D=a+(b-1)*x0={D:.9f} nmol/mol")
    print(f"u(a)={u_a:.6f}; u(b)={u_b:.9f}; cov(a,b)={cov_ab:.9f} nmol/mol")
    print(f"variance_terms: a={contribution_a:.9f}; b={contribution_b:.9f}; covariance={contribution_covariance:.9f} (nmol/mol)^2")
    print(f"u(D)={math.sqrt(variance_D):.9f} nmol/mol; variance_D={variance_D:.12f} (nmol/mol)^2")

    print("\nA — SRP 36/SRP 7, datos publicados y modelo adaptado")
    x, y, sd_x, sd_y = case_b_data()
    u_common = 0.00292
    u_rand_x = sd_x / math.sqrt(12.0)
    u_rand_y = sd_y / math.sqrt(12.0)
    U_x = np.diag(u_rand_x**2) + u_common**2 * np.outer(x, x)
    U_y = np.diag(u_rand_y**2) + u_common**2 * np.outer(y, y)
    beta, covariance_beta, chi_square = ggmr(x, y, U_x, U_y)
    a, b = beta
    dof = len(x) - 2
    print(f"n={len(x)}; orientation: x=SRP 7; y=SRP 36; u_common={u_common:.9f}; V_xy=0")
    print(f"a={a:.9f} nmol/mol; b={b:.9f}; u(a)={math.sqrt(covariance_beta[0,0]):.9f}; u(b)={math.sqrt(covariance_beta[1,1]):.9f}")
    print(f"cov(a,b)={covariance_beta[0,1]:.12g}; chi2_obs={chi_square:.9f}; dof={dof}; chi2_95={chi2.ppf(0.95,dof):.9f}; CDF={chi2.cdf(chi_square,dof):.9g}")
    for x0 in (80.0, 420.0):
        D = a + (b - 1) * x0
        variance_D = covariance_beta[0, 0] + x0**2 * covariance_beta[1, 1] + 2 * x0 * covariance_beta[0, 1]
        if variance_D < 0:
            raise ValueError("La varianza del grado de equivalencia no puede ser negativa")
        print(f"x0={x0:.1f}; D={D:.9f} nmol/mol; u(D)={math.sqrt(variance_D):.9f} nmol/mol")


if __name__ == "__main__":
    main()
