"""Reproduce los ejemplos numéricos didácticos de M10.

Todos los datos son simulados; no describen resultados de CALAIRE.
"""
from math import sqrt
from scipy.integrate import quad
from scipy.stats import norm


def risk_for_rule(true_value, tolerance, guard, u):
    """Normal model: accept iff measured result lies in the guarded interval."""
    lower = -tolerance + guard
    upper = tolerance - guard
    p_accept = norm.cdf((upper - true_value) / u) - norm.cdf((lower - true_value) / u)
    p_reject = 1.0 - p_accept
    return p_accept, p_reject


def main():
    # B: supplied interval-containment rule.
    tolerance = (98.0, 103.0)
    U = 1.2
    k = 2.0
    u = U / k
    print("B: U, k, u =", U, k, u)
    for y in (100.0, 102.2, 106.0):
        interval = (y - U, y + U)
        if interval[0] >= tolerance[0] and interval[1] <= tolerance[1]:
            decision = "aceptar"
        elif interval[1] < tolerance[0] or interval[0] > tolerance[1]:
            decision = "rechazar"
        else:
            decision = "zona de incertidumbre: retener/escalar"
        print(f"B: y={y:.1f}; intervalo={interval}; decisión={decision}")

    # B: simulated zero/span use function and additive correction.
    indicated, zero_indication, span_indication, span_value = 205.0, 5.0, 405.0, 398.0
    corrected = (indicated - zero_indication) * span_value / (span_indication - zero_indication)
    additive_correction = corrected - indicated
    print(f"B: valor corregido x_hat={corrected:.2f} nmol/mol")
    print(f"B: corrección aditiva x_hat-y={additive_correction:.2f} nmol/mol")

    # I: consistency between a single-reading uncertainty and a mean uncertainty.
    single_reading_sigma = 1.5
    single_reading_U = 2.0 * single_reading_sigma
    print(f"I: lectura individual; sigma={single_reading_sigma:.1f}; U=k*sigma={single_reading_U:.1f} nmol/mol")

    # I: two guard-band choices. Risk is evaluated at declared true values.
    spec = 10.0
    sigma = 0.8
    for guard in (0.0, 1.0):
        print(f"I: TUR={spec / (2 * sigma):.3f}; g={guard:.1f}; acceptance=[{-spec + guard:.1f},{spec - guard:.1f}]")
        for theta in (0.0, 9.0, 10.5):
            p_accept, p_reject = risk_for_rule(theta, spec, guard, sigma)
            print(f"I: theta={theta:.1f}; P_accept={p_accept:.8f}; P_reject={p_reject:.8f}")

    # Risk averaged over explicit prior models for the true value.
    # Global FA: prior probability of an out-of-tolerance value AND acceptance.
    # Global FR: prior probability of an in-tolerance value AND rejection.
    # The prior is uniform on [-12,12], so the denominator is 24.
    def global_risks(guard):
        def pa(theta):
            return risk_for_rule(theta, spec, guard, sigma)[0]
        gfa = (quad(pa, -12, -10)[0] + quad(pa, 10, 12)[0]) / 24.0
        gfr = quad(lambda theta: 1.0 - pa(theta), -10, 10)[0] / 24.0
        return gfa, gfr

    for guard in (0.0, 1.0):
        gfa, gfr = global_risks(guard)
        print(f"A: prior=Uniform[-12,12], g={guard:.1f}; global_FA={gfa:.8f}; global_FR={gfr:.8f}")

    # Bilateral limits and dependence: average of two estimates with common error.
    # Both estimates have standard uncertainty 0.8; correlation is 0.75.
    u1 = u2 = 0.8
    rho = 0.75
    cov = rho * u1 * u2
    u_ind = sqrt((u1**2 + u2**2) / 4.0)
    u_dep = sqrt((u1**2 + u2**2 + 2 * cov) / 4.0)
    theta = 10.5
    limit = 10.0
    decision_bound = 9.0
    print(f"A: two-sided spec=[{-limit:.1f},{limit:.1f}], guard={limit - decision_bound:.1f}, theta={theta:.1f}")
    print(f"A: mean_u_ind={u_ind:.8f}; mean_u_dep={u_dep:.8f}; cov={cov:.8f}")
    for label, u_mean in (("independencia", u_ind), ("dependencia", u_dep)):
        p_accept = norm.cdf((decision_bound - theta) / u_mean) - norm.cdf((-decision_bound - theta) / u_mean)
        print(f"A: {label}; P_FA_at_theta={p_accept:.8f}; P_FR_at_theta={1-p_accept:.8f}")


if __name__ == "__main__":
    main()
