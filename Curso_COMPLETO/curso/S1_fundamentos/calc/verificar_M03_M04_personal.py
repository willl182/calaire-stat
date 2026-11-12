"""Verificación independiente M03/M04; ejecutar con curso/.venv/bin/python -I -B.
Extrae nuevamente PDF locales y actualiza solo salidas calculadas en S1/calc.
No convierte las fuentes históricas referencias_34 en ejecuciones nuevas.
"""
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
from pathlib import Path
import json
import platform
import re
import runpy
import subprocess
import sys

import numpy as np
import scipy
from scipy import stats
import statsmodels

CALC = Path(__file__).resolve().parent
ROOT = CALC.parents[2]
OUT = CALC / "verificacion_personal_M03_M04"
OUT.mkdir(exist_ok=True)
PDFS = [
    "statistical_concepts_c04.pdf", "statistical_concepts_c05.pdf",
    "statistical_concepts_c06.pdf", "statistical_concepts_c07.pdf",
    "statistical_concepts_c08.pdf", "statistical_concepts_c09.pdf",
    "metrology_measure_uncer_c03.pdf", "intro_stats_metro_c04.pdf",
    "intro_stats_metro_c07.pdf", "milton2006.pdf",
    "Chemometrics Statistics and Computer Application.pdf",
    "Statistical Concepts – A First Course.pdf",
    "ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf",
    "ISO_IEC Guide 98-3_2008 Suppl.2_2011 - libgen.li.pdf",
]
manifest = []
for index, filename in enumerate(PDFS):
    source = ROOT / "docs" / filename
    target = OUT / f"{index:02}.txt"
    command = ["pdftotext", "-layout", str(source), str(target)]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    (OUT / f"{index:02}.stderr").write_text(result.stderr)
    manifest.append(dict(command=command, sha256=sha256(source.read_bytes()).hexdigest(),
                         returncode=result.returncode))
(OUT / "fuentes.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

modules = {}
for module in ("M03", "M04"):
    capture = StringIO()
    with redirect_stdout(capture):
        modules[module] = runpy.run_path(str(CALC / f"{module}_ejemplos.py"))
    (CALC / f"{module}_ejemplos_salida_sol.txt").write_text(capture.getvalue())
a, b = modules["M03"], modules["M04"]
checks = []

def verify(name, condition):
    assert bool(condition), name
    checks.append(name)

verify("un_ciclo_probabilidades", np.allclose(
    [a["probability_zero_out"], a["probability_one_out"]], [.9, .1]))
verify("rectangular", np.isclose(a["rect_h"]**2, .6**2 / 12))
verify("resolucion", np.isclose(a["rect_resolution"]**2, .1**2 / 12))
verify("triangular", np.isclose(a["triangular_h"]**2, .3**2 / 6))
# Construcción explícita de la matriz de 16 lecturas con causa común.
vc = .8**2 * np.eye(16) + .3**2 * np.ones((16, 16))
w = np.ones(16) / 16
verify("promedio_covarianza_completa", np.isclose(w @ vc @ w, a["u_mean_with_common"]**2))
c = np.array([1 / .8, -1 / .8**2])
v = np.array([[.00005**2, .9*.00005*.00004], [.9*.00005*.00004, .00004**2]])
verify("razon_jacobiano", np.isclose(c @ v @ c, a["u_ratio_correlated"]**2, rtol=1e-12, atol=1e-20))
x = a["series"]
verify("Pearson_desplazado", np.isclose(stats.pearsonr(x[:-1], x[1:]).statistic, .5))
acf = np.dot((x-x.mean())[:-1], (x-x.mean())[1:]) / np.dot(x-x.mean(), x-x.mean())
verify("ACF_no_es_Pearson", not np.isclose(acf, a["lag1"]))
verify("covarianzas_diagonal", np.allclose(np.diag(a["V"]), np.array([.2,.3,.4])**2))
verify("matriz_invalida", np.linalg.det(a["invalid_R"]) < 0)
verify("puntos_matriz_singular_admisible", np.linalg.det(a["V_points"]) == 0)
verify("t_una_media", np.isclose(stats.ttest_1samp(b["error_level"], 0).pvalue, b["pvalue"]))
verify("t_pareada", np.isclose(stats.ttest_rel(b["paired_a"], b["paired_b"]).pvalue, b["p_pair"]))
verify("t_Welch", np.isclose(stats.ttest_ind(b["welch_a"], b["welch_b"], equal_var=False).pvalue, b["p_w"]))
lo, hi = b["var_ci"]
verify("IC_varianza_colas", np.allclose([stats.chi2.cdf(b["df"]*b["var_sample"]/hi, b["df"]), stats.chi2.sf(b["df"]*b["var_sample"]/lo, b["df"])], [.025,.025]))
verify("incertidumbre_s", np.isclose(b["u_s"], .1406526333393944))

def power_nct(effect, n, groups=False):
    df = 2*n-2 if groups else n-1
    nc = effect*np.sqrt(n/2 if groups else n)
    critical = stats.t.ppf(.975, df)
    return stats.nct.cdf(-critical, df, nc) + stats.nct.sf(critical, df, nc)

verify("potencia_media_16", np.isclose(power_nct(.5,16), .4648699556355762))
verify("n_minimo_media_pares", power_nct(.5,33) < .8 <= power_nct(.5,34))
verify("potencia_grupos_12", np.isclose(power_nct(.8,12,True), b["power_groups"]))
verify("n_minimo_dos_grupos", power_nct(.8,25,True) < .8 <= power_nct(.8,26,True))
verify("Grubbs_critico_unilateral", round(b["gcrit_one"], 2) == 2.22)
verify("Grubbs_critico_bilateral", np.isclose(b["gcrit_two"], 2.274365127, rtol=1e-7))
verify("Dixon_estadistico", np.isclose(b["q_dixon"], .23/.28))
verify("Bonferroni", np.allclose(b["bonf_adjusted"], [.036,.093,.6]))
verify("TOST_A_IC90", b["ci_eq"][0] > -.3 and b["ci_eq"][1] < .3)
verify("TOST_A_p", b["p_lower"] < .05 and b["p_upper"] < .05)
verify("TOST_B_no_equivalente", b["b_ci90"][0] < -.3 and b["b_ci90"][1] > .3)
verify("consistencia", np.isclose(stats.chi2.sf(2.33,3), b["p_consistency"]))
for module in ("M03", "M04"):
    text = (CALC.parent / f"{module}_libreto.md").read_text()
    verify(f"{module}_tres_marcadores", text.count("[PRÁCTICA — fase de ejercicios]") == 3)
    levels = re.split(r"^## Nivel [BIA]", text, flags=re.M)[1:]
    verify(f"{module}_un_marcador_por_nivel", all(s.count("[PRÁCTICA — fase de ejercicios]") == 1 for s in levels))
# Numeración de @@ global desde el inicio del diff, sin reiniciar por archivo.
hunks = []
number = 0
file = ""
for line in (CALC.parent / "auditoria_interrupcion_sol_2/cambios_sol.diff").read_text().splitlines():
    if line.startswith("--- "):
        file = line
    if line.startswith("@@"):
        number += 1
        if "M03" in file or "M04" in file:
            hunks.append((number, file, line))
verify("bloques_globales_19_a_37", [h[0] for h in hunks] == list(range(19,38)))
report = dict(python=sys.version, executable=sys.executable, numpy=np.__version__,
              scipy=scipy.__version__, statsmodels=statsmodels.__version__,
              platform=platform.platform(), checks=checks, checks_count=len(checks),
              Pearson_lag1=float(a["lag1"]), ACF_media_global=float(acf), hunks=hunks,
              limits=["No valida datos reales ni desempeño CALAIRE.",
                      "Dixon crítico tabulado en Otto, no recalculado de su distribución.",
                      "Fuentes web no se descargan ni verifican con este script.",
                      "Comparaciones numéricas no equivalen a validación de otra herramienta."])
(OUT / "pruebas.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
print(f"OK: {len(checks)} comprobaciones; evidencias en {OUT}")
