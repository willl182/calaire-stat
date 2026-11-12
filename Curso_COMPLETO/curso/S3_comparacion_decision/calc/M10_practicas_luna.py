"""Cálculos reproducibles para las tres prácticas M10.
Todos los datos son simulados con reglas declaradas; no describen CALAIRE.
"""
from math import sqrt
from scipy.integrate import quad
from scipy.stats import norm


def b_interval_decisions():
    limits = (98.0, 103.0)
    U, k = 1.2, 2.0
    results = (100.0, 102.2, 106.0)
    assert abs(U / k - 0.6) < 1e-12
    print(f"B simulación fijada en script: límites={limits}; U={U:.1f}; k={k:.0f}; resultados={results}")
    for y in results:
        lo, hi = y - U, y + U
        if lo >= limits[0] and hi <= limits[1]:
            decision = "aceptar"
        elif hi < limits[0] or lo > limits[1]:
            decision = "rechazar"
        else:
            decision = "retener/escalar"
        print(f"B y={y:.1f}: [{lo:.1f},{hi:.1f}] -> {decision}")
    assert (100.0 - U, 100.0 + U) == (98.8, 101.2)
    print(f"B zona aceptación central=[{limits[0]+U:.1f},{limits[1]-U:.1f}]")
    print(f"B zona rechazo central: y<{limits[0]-U:.1f} o y>{limits[1]+U:.1f}")


def i_risks():
    T, u = 10.0, 0.8
    theta_conforme, theta_no_conforme = 9.0, 10.5
    for g in (0.0, 1.0):
        low, high = -T + g, T - g
        p_accept_conforme = norm.cdf((high-theta_conforme)/u) - norm.cdf((low-theta_conforme)/u)
        p_accept_no_conforme = norm.cdf((high-theta_no_conforme)/u) - norm.cdf((low-theta_no_conforme)/u)
        p_fr = 1.0 - p_accept_conforme
        print(f"I g={g:.0f}, aceptación=[{low:.0f},{high:.0f}], theta=9: P(rechazo conforme)={p_fr:.8f}")
        print(f"I g={g:.0f}, theta=10.5: P(aceptación falsa)={p_accept_no_conforme:.8f}")
    print(f"I u={u:.1f}; k=2; U={2*u:.1f}; TUR=10/{2*u:.1f}={T/(2*u):.2f}")
    assert abs((1-(norm.cdf((10-9)/u)-norm.cdf((-10-9)/u))) - 0.10564977) < 1e-7
    assert abs((norm.cdf((10-10.5)/u)-norm.cdf((-10-10.5)/u)) - 0.26598553) < 1e-7


def a_risks():
    # Especificación bilateral [-10,10], previa uniforme [-12,12].
    T, u = 10.0, 0.8
    prior_width = 24.0
    prior_low, prior_high = -12.0, 12.0
    def p_accept(theta, guard, sd=u):
        low, high = -T + guard, T - guard
        return norm.cdf((high-theta)/sd)-norm.cdf((low-theta)/sd)
    for g in (0.0, 1.0):
        gfa = (quad(lambda th: p_accept(th, g), prior_low, -T)[0] + quad(lambda th: p_accept(th, g), T, prior_high)[0]) / prior_width
        gfr = quad(lambda th: 1-p_accept(th, g), -T, T)[0] / prior_width
        print(f"A g={g:.0f}: riesgo global falsa aceptación={gfa:.8f}; falso rechazo={gfr:.8f}")
    # Decisión conjunta/dos estimaciones dependientes; bilateral.
    u1 = u2 = 0.8
    rho = 0.75
    cov = rho*u1*u2
    umean_ind = sqrt((u1*u1+u2*u2)/4)
    umean_dep = sqrt((u1*u1+u2*u2+2*cov)/4)
    theta = 10.5
    print(f"A cov={cov:.2f} (nmol/mol)^2; u_media independiente={umean_ind:.8f}; dependiente={umean_dep:.8f}")
    pfa_values = {}
    for label, sd in (("independencia", umean_ind), ("covarianza incluida", umean_dep)):
        pfa = p_accept(theta, 1.0, sd)
        pfa_values[label] = pfa
        print(f"A theta=10.5, zona bilateral [-9,9], {label}: P(aceptación falsa)={pfa:.8f}")
    assert abs(umean_ind-sqrt(0.32)) < 1e-12
    assert abs(umean_dep-sqrt(0.56)) < 1e-12
    assert abs(pfa_values["independencia"]-0.00400497) < 1e-7
    assert abs(pfa_values["covarianza incluida"]-0.02251044) < 1e-7
    # Riesgo específico para una observación única y=0, u=6, previa U[-12,12].
    specific_sd = 6.0
    posterior_norm = norm.cdf(prior_high/specific_sd)-norm.cdf(prior_low/specific_sd)
    lower_tail = (norm.cdf(-T/specific_sd)-norm.cdf(prior_low/specific_sd))/posterior_norm
    upper_tail = (norm.cdf(prior_high/specific_sd)-norm.cdf(T/specific_sd))/posterior_norm
    p_nonconforming = lower_tail + upper_tail
    p_conforming = (norm.cdf(T/specific_sd)-norm.cdf(-T/specific_sd))/posterior_norm
    assert abs(lower_tail-upper_tail) < 1e-12
    assert abs(p_conforming+p_nonconforming-1.0) < 1e-12
    assert abs(p_nonconforming-0.05246774) < 1e-7
    print(f"A específico y=0,u=6: acepta sin guarda; cola inferior={lower_tail:.8f}; superior={upper_tail:.8f}; riesgo falsa aceptación={p_nonconforming:.8f}; conforme={p_conforming:.8f}; suma={p_conforming+p_nonconforming:.8f}")


if __name__ == "__main__":
    b_interval_decisions()
    i_risks()
    a_risks()
