"""Soluciones numéricas reproducibles para las prácticas de M08.
Todos los datos de ejercicio son simulados para docencia; no representan CALAIRE.
"""
from math import sqrt
import numpy as np
from scipy.stats import t


def b_practice():
    # Un punto: precisión entre días y repetibilidad de seis días x ocho lecturas.
    sr, sentre, days, n = 0.24, 0.30, 6, 8
    u_ref, u_corr = 0.20, 0.30 / sqrt(3)
    v_precision = sentre**2 / days + sr**2 / (days * n)
    u_precision = sqrt(v_precision)
    u_total = sqrt(v_precision + u_ref**2 + u_corr**2)
    u_without_day = sqrt(sr**2 / (days * n) + u_ref**2 + u_corr**2)
    # Rectangular tolerance converted to standard uncertainty; unit sensitivity.
    u_h = 0.30 / sqrt(3)
    perturbation = (0.0 + u_h) - 0.0
    print("B simulated; target: calibration-point mean error; nmol/mol")
    print(f"u_precision={u_precision:.8f}; u_total={u_total:.8f}; U(k=2)={2*u_total:.8f}")
    print(f"u_without_between_day={u_without_day:.8f}; naive sr/sqrt(576)={sr/sqrt(576):.8f}")
    print(f"rectangular u_h={u_h:.8f}; unit-sensitivity perturbation={perturbation:.8f}")
    assert np.isclose(v_precision, 0.0162)
    assert u_total > u_without_day > sr / sqrt(576)
    assert np.isclose(u_h, 0.30 / sqrt(3))
    assert np.isclose(perturbation, u_h)


def i_practice():
    # Tres resultados simulados independientes, each with declared variance model.
    sr, sentre, days, n = 0.24, 0.30, 6, 8
    u_ref, u_corr = 0.30, 0.10
    u_precision2 = sentre**2 / days + sr**2 / (days*n)
    u_individual = sqrt(u_ref**2 + u_corr**2 + sentre**2 + sr**2)
    u_mean = sqrt(u_ref**2 + u_corr**2 + u_precision2)
    # Future mean adds an independently characterized new indication and stability.
    u_future = sqrt(u_mean**2 + 0.25**2 + 0.18**2)
    # Coverage illustration: only independent type-A precision block has finite df.
    v_terms = [sentre**2/days, sr**2/(days*n), u_ref**2, u_corr**2]
    dfs = [days-1, days*(n-1), 1e12, 1e12]
    nu_eff = sum(v_terms)**2 / sum(v*v/df for v, df in zip(v_terms, dfs))
    k = t.ppf(0.975, nu_eff)
    # Chain to client; all standard uncertainties independently supplied in final units.
    u_srp, u_transfer, u_client = 0.28, 0.35, 0.42
    u_level = sqrt(u_srp**2 + u_transfer**2)
    u_client_total = sqrt(u_level**2 + u_client**2)
    # Analytic sensitivities for inverse calibration x=(y-a)/b.
    y, a, b = 100.60, 0.40, 1.002
    c_y, c_a, c_b = 1/b, -1/b, -(y-a)/b**2
    # Difference of two results with one shared relative component.
    x1, x2, u_relative = 100.0, 102.0, 0.003
    u1_specific, u2_specific = 0.20, 0.25
    covariance = x1*x2*u_relative**2
    var_difference = (u1_specific**2 + (x1*u_relative)**2
                      + u2_specific**2 + (x2*u_relative)**2 - 2*covariance)
    u_difference = sqrt(var_difference)
    u_difference_independent = sqrt(u1_specific**2 + (x1*u_relative)**2
                                    + u2_specific**2 + (x2*u_relative)**2)
    print("I simulated; units nmol/mol")
    print(f"u_individual={u_individual:.8f}; u_calibration_mean={u_mean:.8f}; u_future={u_future:.8f}")
    print(f"mean coverage: nu_eff={nu_eff:.6f}; k95={k:.8f}; U95={k*u_mean:.8f}")
    print(f"chain: u_Level2={u_level:.8f}; u_client={u_client_total:.8f}; U(k=2)={2*u_client_total:.8f}")
    print(f"inverse sensitivities: c_y={c_y:.8f}; c_a={c_a:.8f}; c_b={c_b:.8f}")
    print(f"shared covariance={covariance:.8f}; u_difference={u_difference:.8f}; independent={u_difference_independent:.8f}")
    print("Limit: Student/Welch-Satterthwaite is conditional on independent blocks and adequate output distribution.")
    assert np.isclose(u_mean, sqrt(0.30**2+0.10**2+0.30**2/6+0.24**2/48))
    assert u_future > u_mean and u_individual > sqrt(0.30**2+0.10**2)
    assert np.isclose(c_y, 0.998003992015968)
    assert np.isclose(c_a, -c_y) and np.isclose(c_b, -99.8003992015968)
    assert np.isclose(covariance, 0.0918)
    assert np.isclose(u_difference, 0.3202124291)
    assert np.isclose(u_difference_independent, 0.5349168152)


def a_practice():
    # Simulated uncertainty function and hypothetical CMC, same coverage by construction.
    def u(x):
        return np.sqrt(0.28**2 + (0.006*x)**2)
    def U(x):
        return 2*u(x)
    def cmc(x):
        return 0.80 + 0.004*x
    grid = np.linspace(0, 500, 5001)
    delta_sq = U(grid)**2 - cmc(grid)**2
    crossings = np.where(np.signbit(delta_sq[:-1]) != np.signbit(delta_sq[1:]))[0]
    # Local linearization diagnostic for the separate inverse model x=100/b.
    x0, b0, u_b = 100.0, 1.0, 0.20
    local_change = -x0 / b0**2 * u_b
    change_plus = x0 / (b0 + u_b) - x0 / b0
    change_minus = x0 / (b0 - u_b) - x0 / b0
    # Positive functions: solve U^2-CMC^2=0; select root in declared interval.
    roots = np.roots([4*0.006**2-0.004**2, -2*0.80*0.004, 4*0.28**2-0.80**2])
    roots = [float(r.real) for r in roots if abs(r.imag) < 1e-10 and 0 <= r.real <= 500]
    print("A simulated functions; x, U, CMC, max(U,CMC); nmol/mol")
    for x in [0, 80, 250, 500]:
        print(f"{x:6.1f} {U(x):.8f} {cmc(x):.8f} {max(U(x),cmc(x)):.8f}")
    print(f"crossings on [0,500] by grid step 0.1: {len(crossings)}; analytic roots={roots}")
    print("U^2-CMC^2 coefficients:", [4*0.006**2-0.004**2, -2*0.80*0.004, 4*0.28**2-0.80**2])
    print(f"linearization: local changes=±{abs(local_change):.8f}; exact +u_b={change_plus:.8f}; exact -u_b={change_minus:.8f}")
    assert len(crossings) == 1 and len(roots) == 1
    assert roots[0] > 80 and roots[0] < 82
    assert cmc(0) > U(0) and U(250) > cmc(250)
    assert np.isclose(local_change, -20.0)
    assert np.isclose(change_plus, -100/6)
    assert np.isclose(change_minus, 25.0)
    assert not np.isclose(abs(change_plus), abs(change_minus))


if __name__ == "__main__":
    b_practice()
    i_practice()
    a_practice()
