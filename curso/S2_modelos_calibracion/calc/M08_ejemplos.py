"""Cálculos reproducibles de los ejemplos ilustrativos de M08.

Todos los conjuntos de entrada definidos aquí son simulados para docencia;
no representan resultados de CALAIRE. Ejecutar con el Python del curso.
"""
from math import sqrt
from scipy.stats import t


def main():
    print("M08 — ejemplos simulados; nmol/mol salvo indicación distinta")

    # B: valor de uso x_hat=(y-a)/b. Entradas didácticas independientes.
    y, a, b = 100.60, 0.40, 1.002
    s_read, n = 0.24, 8
    delta = 0.10
    print(f"Context own-data design count: 12 points x 8 readings x 6 days = {12*8*6}; sqrt(count)={sqrt(12*8*6):.0f}")
    print(f"Type-A degrees of freedom for n={n}: {n-1}")
    uy_a = s_read / sqrt(n)
    uy_b = delta / sqrt(12 * n)
    uy = sqrt(uy_a**2 + uy_b**2)
    ua, ub = 0.15, 0.002
    x_hat = (y - a) / b
    print(f"B individual y={y:.8f}; a={a:.8f}; b={b:.8f}; x_hat={x_hat:.10f}")
    print(f"uA(y mean)={uy_a:.10f}; uB(resolution mean)={uy_b:.10f}; u(y)={uy:.10f}")
    print(f"u(a)={ua:.10f}; u(b)={ub:.10f}")

    # Kragten: perturbar cada entrada en +u, el efecto al cuadrado se suma.
    inputs = [("y", y, uy), ("a", a, ua), ("b", b, ub)]
    kragten = []
    for name, value, u in inputs:
        shifted = {"y": y, "a": a, "b": b}
        shifted[name] += u
        x_hat_shifted = (shifted["y"] - shifted["a"]) / shifted["b"]
        effect = x_hat_shifted - x_hat
        kragten.append((name, u, x_hat_shifted, effect))
    uc_b = sqrt(sum(row[3] ** 2 for row in kragten))
    print("Kragten rows: input, u(input), x_hat(input+u), effect")
    for row in kragten:
        print(f"  {row[0]} {row[1]:.10f} {row[2]:.10f} {row[3]:.10f}")
    print(f"B uc={uc_b:.10f}; U(k=2)={2*uc_b:.10f}")

    # Student coverage and Welch-Satterthwaite: only the Type-A mean has finite df.
    c_y = 1 / b
    c_a = -1 / b
    c_b = -(y - a) / b**2
    components = [c_y**2 * uy_a**2,
                  c_y**2 * uy_b**2,
                  c_a**2 * ua**2,
                  c_b**2 * ub**2]
    uc_i = sqrt(sum(components))
    nu = uc_i**4 / (components[0]**2 / (n - 1))
    k = t.ppf(0.975, nu)
    print(f"I sensitivities: cy={c_y:.10f}; ca={c_a:.10f}; cb={c_b:.10f}")
    print(f"I components variance={components}; uc(linear)={uc_i:.10f}; nu_eff={nu:.10f}; k95={k:.10f}; U={k*uc_i:.10f}")

    # Resolución y tolerancia con distribuciones rectangulares.
    u_resolution = delta / sqrt(12)
    tolerance_halfwidth = 0.30
    u_tolerance = tolerance_halfwidth / sqrt(3)
    print(f"u(resolution δ={delta})={u_resolution:.10f}; u(tolerance ±{tolerance_halfwidth})={u_tolerance:.10f}")
    print(f"s={s_read:.8f}; s/sqrt(n)={s_read/sqrt(n):.10f}; n={n}")

    # I: tres resultados de interés, con entradas simuladas separadas explícitamente.
    u_cal_mean = sqrt(0.30**2 + 0.20**2 + 0.10**2)
    u_future = sqrt(u_cal_mean**2 + 0.25**2 + 0.18**2)
    print(f"I illustrative u(calibration mean)={u_cal_mean:.10f}; U(k=2)={2*u_cal_mean:.10f}")
    print(f"I illustrative u(future result)={u_future:.10f}; U(k=2)={2*u_future:.10f}")
    # If regression residual already includes the within-run component, adding it again is shown.
    u_nodouble = sqrt(0.30**2 + 0.20**2 + 0.10**2)
    u_double = sqrt(u_nodouble**2 + 0.20**2)
    print(f"I no-double-count uc={u_nodouble:.10f}; incorrectly duplicated uc={u_double:.10f}")

    # I propagation through three calibration links, independent didactic uncertainties.
    u_srp, u_level_cond, u_client = 0.28, 0.35, 0.42
    u_level = sqrt(u_srp**2 + u_level_cond**2)
    u_client_total = sqrt(u_level**2 + u_client**2)
    print(f"I chain: u(SRP)={u_srp:.8f}; u(Level2)={u_level:.10f}; u(client)={u_client_total:.10f}; U(k=2)={2*u_client_total:.10f}")

    # A common relative component partially cancels in a difference.
    x1, x2, ub = 100.0, 102.0, 0.003
    u1_ind, u2_ind = 0.20, 0.25
    common_cov = x1 * x2 * ub**2
    u1_sq = u1_ind**2 + (x1 * ub)**2
    u2_sq = u2_ind**2 + (x2 * ub)**2
    u_diff_ind = sqrt(u1_sq + u2_sq)
    u_diff_shared = sqrt(u1_sq + u2_sq - 2 * common_cov)
    print(f"A common x1={x1:.8f}; x2={x2:.8f}; ub={ub:.8f}; cov={common_cov:.10f}")
    print(f"A u(diff) independence={u_diff_ind:.10f}; shared={u_diff_shared:.10f}; abs diff={x2-x1:.8f}")

    # Function U(x) and a hypothetical CMC, same measurand/units/coverage by construction.
    cmc = lambda x: 0.80 + 0.004 * x
    u_function = lambda x: sqrt(0.28**2 + (0.006 * x)**2)
    k_a = 2.0
    points = [0.0, 80.0, 250.0, 500.0]
    print("A interval: x, u(x), U(k=2), hypothetical CMC, max(U, CMC)")
    for x in points:
        u = u_function(x)
        U = k_a * u
        print(f"  {x:.8f} {u:.10f} {U:.10f} {cmc(x):.10f} {max(U, cmc(x)):.10f}")



if __name__ == "__main__":
    main()
