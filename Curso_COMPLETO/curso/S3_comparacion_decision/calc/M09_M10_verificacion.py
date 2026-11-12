"""Contrastes independientes de ejemplos docentes M09/M10; no resuelve prácticas.
Ejecutar desde la raíz: curso/.venv/bin/python -I <ruta de este archivo>.
"""
from pathlib import Path
import runpy
import math
import hashlib
import re

import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from scipy.stats import norm

CALC = Path(__file__).resolve().parent
S3 = CALC.parent
ROOT = S3.parents[1]
m09 = runpy.run_path(str(CALC / "M09_ejemplos.py"))
m10 = runpy.run_path(str(CALC / "M10_ejemplos.py"))


def check_close(actual, expected, atol=1e-8):
    np.testing.assert_allclose(actual, expected, atol=atol, rtol=0)


def profile_fit(x, y, vx, vy):
    # Segundo algoritmo: eliminar abscisas latentes y resolver GLS a pendiente fija.
    # No reutiliza la función residual ni el optimizador de ggmr().
    one = np.ones(len(x))

    def evaluate(b):
        v = vy + b*b*vx
        z = y-b*x
        a = (one @ np.linalg.solve(v, z)) / (one @ np.linalg.solve(v, one))
        residual = z-a
        return a, float(residual @ np.linalg.solve(v, residual))

    fit = minimize_scalar(lambda b: evaluate(b)[1], bounds=(0.98, 1.02),
                          method="bounded", options={"xatol": 1e-14})
    assert fit.success
    a, q = evaluate(fit.x)
    return np.array([a, fit.x]), q


m09["validate_ggmr"]()
x, y, sx, sy = m09["case_b_data"]()
# Cotejo independiente de la transcripción del informe publicado QAPP p. PDF 37.
check_close(x, [.2, 787.4, 681.5, 585.5, 493.7, 408.5, 325.1, 242.4, 145.4, 45.9, 16.1, .1])
check_close(y, [0., 785.9, 680.3, 584.1, 492.7, 407.8, 324.4, 241.8, 144.9, 45.6, 16., -.1])
check_close(sx, [.1, .6, .5, .5, .4, .3, .3, .2, .2, .1, .1, .2])
check_close(sy, [.2, .2, .2, 1., .4, .5, .4, .2, .2, .2, .2, .1])
for common in (0., .00292):
    vx = np.diag(sx*sx/12) + common**2*np.outer(x, x)
    vy = np.diag(sy*sy/12) + common**2*np.outer(y, y)
    for v in (vx, vy):
        check_close(v, v.T)
        assert np.linalg.eigvalsh(v).min() > 0
    beta, covariance, q = m09["ggmr"](x, y, vx, vy)
    beta_alt, q_alt = profile_fit(x, y, vx, vy)
    check_close(beta, beta_alt, 5e-5)
    check_close(q, q_alt, 1e-7)
    assert np.linalg.eigvalsh(covariance).min() > 0
    print(f"GGMR common={common}: perfil GLS independiente coincide; beta={beta_alt}; chi2={q_alt:.9f}")

# Casos inválidos: no basta con que Cholesky acepte un triángulo de la matriz.
for bad_x, bad_y, bad_vx, bad_vy in (
    (x, y, vx + np.triu(np.ones_like(vx), 1), vy),
    (x, y, vx[:-1, :-1], vy),
    (x, y, np.full_like(vx, np.nan), vy),
    (x, y, -np.eye(len(x)), vy),
    (np.ones_like(x), y, vx, vy),
):
    try:
        m09["ggmr"](bad_x, bad_y, bad_vx, bad_vy)
    except (ValueError, np.linalg.LinAlgError):
        pass
    else:
        raise AssertionError("GGMR aceptó una entrada inválida")
print("GGMR: rechaza asimetría, dimensiones erróneas, NaN, varianzas negativas y x constante")

shared = np.array([[.20**2, .018], [.018, .15**2]])
assert np.linalg.eigvalsh(shared).min() > 0
check_close(np.array([-1., 1.]) @ shared @ np.array([-1., 1.]), .0265)
check_close(1*.8*.15**2, .018)
check_close(.35/(2*math.sqrt(.0265)), 1.075016454, 1e-9)
for p, r, up, ur, expected in [(80.3, 80., .2, .15, (.3, .25)),
                               (420.8, 420., .6, .5, (.8, .7810249675906654))]:
    check_close((p-r, math.hypot(up, ur)), expected)
print("M09: covarianza construida, normalización y grados de equivalencia simulados comprobados")

# Posterior: integración de densidades, independiente de la resta de CDF del ejemplo.
evidence = quad(lambda theta: norm.pdf(9.5, loc=theta, scale=.8)/24, -12, 12)[0]
pc = quad(lambda theta: norm.pdf(9.5, loc=theta, scale=.8)/24, -10, 10)[0]/evidence
check_close(pc, .73466761, 5e-9)
check_close(1-pc, .26533239, 5e-9)

# Globales: invertir orden de integración respecto al script docente (ahora sobre Y).
def joint_density_conforming(measured):
    return (norm.cdf((10-measured)/.8)-norm.cdf((-10-measured)/.8))/24


def joint_density_nonconforming(measured):
    return ((norm.cdf((-10-measured)/.8)-norm.cdf((-12-measured)/.8))
            + (norm.cdf((12-measured)/.8)-norm.cdf((10-measured)/.8)))/24


for guard, expected in [(0, (.02646254, .02659615)), (1, (.00337106, .08670579))]:
    bound = 10-guard
    fa = quad(joint_density_nonconforming, -bound, bound, epsabs=1e-12)[0]
    fr = (quad(joint_density_conforming, -np.inf, -bound, epsabs=1e-12)[0]
          + quad(joint_density_conforming, bound, np.inf, epsabs=1e-12)[0])
    check_close((fa, fr), expected, 5e-9)
    print(f"M10: g={guard}, globales por orden inverso FA={fa:.10f}, FR={fr:.10f}")

check_close(norm.cdf(2)-norm.cdf(-2), .9544997361036416)
for chapter in ("M09", "M10"):
    text = (S3 / f"{chapter}_libreto.md").read_text()
    markers = re.findall(r"^> \*\*\[PRÁCTICA — fase de ejercicios\]\*\* .+$", text, re.M)
    assert len(markers) == 3, (chapter, markers)
    for line in text.splitlines():
        if line.startswith(">"):
            labels = re.findall(r"\*\*\[([^]]+)\]\*\*", line)
            assert all(label in {"PIZARRA", "DIAPOSITIVA", "MATERIAL", "PREGUNTA AL GRUPO", "PAUSA", "EJEMPLO", "PRÁCTICA — fase de ejercicios", "ERROR CRÍTICO", "ESCALAMIENTO", "TRANSICIÓN", "NOTA AL INSTRUCTOR"} for label in labels)
    print(f"{chapter}: tres marcadores de práctica y etiquetas de acotación permitidas")

# Evidencia de integridad de las fuentes extraídas, sin modificar docs/.
for txt in sorted((CALC / "auditoria_M09_M10").glob("*.txt")):
    source = ROOT / "docs" / (txt.stem + ".pdf")
    if source.exists():
        print(f"FUENTE {source.name}; SHA256={hashlib.sha256(source.read_bytes()).hexdigest()}; páginas extraídas={len(txt.read_text().split(chr(12)))-1}")
source = CALC / "auditoria_M09_M10/jcgm106_fuente/JCGM_106_2012_E.pdf"
print(f"FUENTE JCGM106 oficial; SHA256={hashlib.sha256(source.read_bytes()).hexdigest()}")
print("OK: todos los contrastes y comprobaciones pasaron")
