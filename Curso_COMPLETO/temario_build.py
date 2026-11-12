"""Genera temario_curso.html y temario_curso.md desde una sola fuente de datos.

Uso: python3 temario_build.py
Marcado en los textos: `fórmula` (código) y _{x} (subíndice).
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).parent
HEAD = ROOT / "temario_head.html"  # título, fuentes y estilos de la página

# ---------------------------------------------------------------- bibliografía
BIB = [
    ("SRP y medición de ozono", [
        ("bipm", "BIPM.QM-K1", "BIPM. <i>Protocol for BIPM.QM-K1, On-demand Key Comparison of Ozone at Ambient Level</i>, v2.1, 9-10-2025.", "BIPM.QM-K1_2.protocol.pdf"),
        ("nistir", "NISTIR 6963", "Paur, R. J.; Bass, A. M.; Norris, J. E.; Buckley, T. J. <i>Standard Reference Photometer for the Assay of Ozone in Calibration Atmospheres</i>. NIST, 2003.", "nistir6963.pdf"),
        ("srp6008", "NIST SRP 6008", "NIST. <i>Standard Reference Instrument Series 6008: Ozone Standard Reference Photometer</i>, especificación y certificado, 2017.", "SRP6008_spec_cert.pdf"),
        ("sop", "SRP SOP", "US EPA. <i>SOP for the Verification and Re-Verification of EPA's Ozone Standard Reference Photometers</i>, SRP/SOP-1, rev. 1, 2015.", "srp_sop.pdf"),
        ("qapp", "SRP QAPP", "US EPA. <i>Quality Assurance Project Plan for the Standard Reference Photometer Program</i>, 2017.", "srp_qapp.pdf"),
        ("tad", "EPA TAD", "US EPA. <i>Transfer Standards for Calibration of Air Monitoring Analyzers for Ozone</i>, EPA-454/B-22-003, 2023.", "o3_tad_508_20230906_final.pdf"),
        ("daumont", "Daumont et al. 1992", "Daumont, D.; Brion, J.; Charbonnier, J.; Malicet, J. <i>Ozone UV spectroscopy I: Absorption cross-sections at room temperature</i>. J. Atmos. Chem. 15, 145–155.", "Ozone UV spectroscopy I_ Absorption cross-sections at room.pdf"),
        ("malicet", "Malicet et al. 1995", "Malicet, J. et al. <i>Ozone UV spectroscopy II: Absorption cross-sections and temperature dependence</i>. J. Atmos. Chem. 21, 263–273.", "Ozone UV spectroscopy_ II_ Absorption cross-sections .pdf"),
        ("13964", "ISO 13964", "BS ISO 13964:1998. <i>Air quality — Determination of ozone in ambient air — Ultraviolet photometric method</i>.", "Air quality_ Determination of ozone in ambient air_ ISO 13964.pdf"),
        ("14625", "EN 14625", "BS EN 14625:2012. <i>Ambient air — Standard method for the measurement of the concentration of ozone by ultraviolet photometry</i>.", "BS EN 14625_2012.pdf"),
    ]),
    ("Regulación y aseguramiento de la calidad (EE. UU.)", [
        ("cfr50d", "40 CFR 50, Apéndice D", "eCFR vigente al 16-10-2026; incluye la nueva sección eficaz (304,39 atm⁻¹ cm⁻¹).", "Appendix D to Part 50_ Title 40 (up to date as of 10-16-2026).pdf"),
        ("cfr50", "40 CFR 50", "Texto completo y Apéndices A-1 y C (eCFR, 19-10-2026).", "USEPA - 40 CFR Part 50.pdf; Appendix A-1 to Part 50_ ….pdf; Appendix C to Part 50_ ….pdf"),
        ("cfr53", "40 CFR 53", "Métodos de referencia y equivalentes: pruebas de desempeño de analizadores.", "USEPA - 40 CFR Part 53.pdf"),
        ("cfr58a", "40 CFR 58, Apéndice A", "Requisitos de aseguramiento de calidad de las redes, eCFR vigente al 20-10-2026.", "Appendix A to Part 58_ Title 40 (up to date as of 10-20-2026).pdf"),
        ("qah", "EPA QA Handbook Vol. II", "US EPA. <i>Quality Assurance Handbook for Air Pollution Measurement Systems, Volume II</i>.", "USEPA - Quality Handbook.pdf"),
        ("valid", "Plantilla de validación EPA", "US EPA. Apéndice D, plantilla de validación (v. 03/2017); idéntica a <code>USEPA - Appendix D Air Quality Handbook.pdf</code>.", "app_d_validation_template_version_03_2017_for_amtic_rev_1.pdf"),
    ]),
    ("Incertidumbre, calibración y precisión (GUM e ISO)", [
        ("gum", "GUM (JCGM 100)", "ISO/IEC Guide 98-3:2008. <i>Guide to the expression of uncertainty in measurement</i>.", "ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ ….pdf"),
        ("gums1", "GUM Suplemento 1", "ISO/IEC Guide 98-3/Suppl. 1:2008, método de Monte Carlo, con su corrigendum 1:2009.", "ISO_IEC Guide 98-3_2008 Suppl.1_2008 ….pdf; … Suppl.1_2008_Cor 1_2009 ….pdf"),
        ("gums2", "GUM Suplemento 2", "ISO/IEC Guide 98-3/Suppl. 2:2011, cualquier número de magnitudes de salida.", "ISO_IEC Guide 98-3_2008 Suppl.2_2011 ….pdf"),
        ("gum1", "JCGM GUM-1", "Introducción a la expresión de la incertidumbre de medida.", "JCGM_GUM-1.pdf"),
        ("gum6", "JCGM GUM-6", "JCGM GUM-6:2020. Desarrollo y uso de modelos de medición.", "JCGM_GUM_6_2020.pdf"),
        ("17025", "ISO/IEC 17025", "BS EN ISO/IEC 17025:2017. Requisitos generales para la competencia de los laboratorios de ensayo y calibración.", "BS EN ISO_IEC 17025_2017.pdf"),
        ("6143", "ISO 6143", "ISO 6143:2001. <i>Gas analysis — Comparison methods for determining and checking the composition of calibration gas mixtures</i>.", "ISO 6143 2001.pdf"),
        ("28037", "ISO/TS 28037", "ISO/TS 28037:2010. <i>Determination and use of straight-line calibration functions</i>.", "ISO 28037.pdf"),
        ("5725", "ISO 5725", "ISO 5725-2, -3, -4 y -6:1994 y 5725-5:1998. Exactitud (veracidad y precisión) de métodos y resultados de medición, con los corrigenda de las Partes 1, 2, 3, 5 y 6.", "ISO 5725-*.pdf"),
        ("deldossi", "Deldossi y Zappa 2009", "Deldossi, L.; Zappa, D. Comparación entre ISO 5725 y GUM, 2009.", "2009 - Deldossi - ISO 5725 vs GUM comparison.pdf"),
        ("milton", "Milton et al. 2006", "Milton, M. J. T. et al. <i>Implementation of a generalized least-squares method for determining calibration curves from data with general uncertainty structures</i>. Metrologia, 2006.", "milton2006.pdf"),
        ("enothers", "EN 14211, 14212 y 14626", "BS EN 14211:2012 (NO/NO₂), BS EN 14212:2012 (SO₂) y BS EN 14626:2012 (CO).", "BS EN 14211_2012.pdf; BS EN 14212_2012 .pdf; BS EN 14626_2012 .pdf"),
    ]),
    ("Libros de estadística, metrología y quimiometría", [
        ("sc", "Statistical Concepts", "<i>Statistical Concepts – A First Course</i>, por capítulos.", "statistical_concepts_c01–c10.pdf"),
        ("ism", "Intro. Statistics in Metrology", "<i>Introduction to Statistics in Metrology</i>, por capítulos.", "intro_stats_metro_c01–c11.pdf; a01–a05.pdf"),
        ("mmu", "Metrology and Measurement Uncertainty", "<i>Metrology and Measurement Uncertainty</i>, por capítulos.", "metrology_measure_uncer_c01–c10.pdf"),
        ("asq", "ASQ Metrology Handbook", "<i>The ASQ Metrology Handbook</i>, caps. 27, 29 y 30.", "asq_metrological_handbook_c*.pdf"),
        ("otto", "Otto", "Otto, M. <i>Chemometrics: Statistics and Computer Application in Analytical Chemistry</i>, 3.ª ed. Wiley-VCH, 2017.", "Chemometrics Statistics and Computer Application.pdf"),
        ("brereton", "Brereton", "Brereton, R. G. <i>Chemometrics: Data Driven Extraction for Science</i>, 2.ª ed. Wiley, 2018.", "chemometrics_c01–c07.pdf; chemometrics_a01.pdf"),
        ("mw", "Mark y Workman", "Mark, H.; Workman, J. <i>Chemometrics in Spectroscopy</i>, 2.ª ed. Elsevier, 2018, secciones.", "chemometrics_spectroscopy_s03, s05, s06, s020, s021.pdf"),
        ("huq", "Handbook of Uncertainty Quantification", "Consulta de apoyo.", "Handbook of Uncertainty Quantification.pdf"),
        ("ai", "AI-Assisted Statistics", "<i>AI-Assisted Statistics for Data Scientists</i>, material de apoyo.", "AI-Assisted Statistics for Data Scientists_.epub"),
    ]),
    ("Caso del proyecto", [
        ("ryr", "Estudio R&R CALAIRE 2022–2023", "Resultados del estudio de repetibilidad y reproducibilidad del Level 2 contra el SRP 55: dos analistas, 10 niveles, tres campañas de 6 días (hoja BASE DE DATOS).", "Resultados R&r_2022 2023 (1).xlsx"),
        ("cert", "Certificado F-PSMT-01", "Plantilla del certificado de calibración del patrón Level 2 de CALAIRE (Thermo 49C, S/N 59756-324) contra el SRP 55.", "F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm"),
    ]),
]
BIBKEY = {k: (short, full, f) for _, items in BIB for (k, short, full, f) in items}

# -------------------------------------------------------------------- módulos
# Cada módulo: id, num, título, nivel, horas, objetivo, partes [(título, [items])],
# tabla opcional, nota opcional, práctica [items], refs [(clave, ubicación)]
BLOCKS = [
    ("I", "Medición y tratamiento estadístico de las lecturas", "Qué mide el SRP y cómo, y la estadística que hace falta para entender sus lecturas: describirlas, modelar su variación como variable aleatoria y saber qué se puede concluir de unas pocas.", ["m1", "m3", "m4", "m5"]),
    ("II", "La calibración por comparación", "Con esa base se planea la comparación, se separan las fuentes de variación, se ajusta la recta y se expresa el resultado con su incertidumbre.", ["m6", "m7", "m8", "m9"]),
    ("III", "Diseminación de la trazabilidad", "Lo que solo hace este laboratorio: su comparación con el BIPM, la decisión sobre los fotómetros del país, el control de sus propios patrones y su relación con las redes.", ["m10", "m11", "m12", "m13"]),
    ("Cierre", "Integración y temas avanzados", "El taller junta todo el curso sobre un caso real; el optativo abre los temas que superan el nivel del curso.", ["taller", "m14"]),
]
# Números nuevos de módulo (las claves internas se conservan). m2 se fusionó en m1 y m4.
RENUM = {1: 1, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 11, 13: 12, 14: 13}

DESIGN_TABLE = (["Documento", "Diseño"], [
    ["BIPM.QM-K1", "12 niveles: 0, 220, 80, 420, 120, 320, 30, 370, 170, 500, 270, 0 nmol/mol. 10 lecturas por punto. Estabilización ≥ 8 h; acondicionar ≥ 2 h con más de 500 nmol/mol."],
    ["SRP QAPP", "12 concentraciones con ceros, 10 lecturas, ≥ 3 ciclos."],
    ["SRP SOP", "Igual, pero ≥ 6 ciclos. La diferencia con el QAPP se enseña tal cual."],
    ["EPA TAD (Level 2/3)", "3 ciclos, cada uno con cero y ≥ 6 concentraciones."],
    ["EN 14625 (linealidad)", "≥ 6 niveles, ≥ 5 lecturas, secuencia 80-40-0-60-20-95 %."],
    ["ISO 13964", "Cero y ≥ 5 concentraciones."],
    ["Calibración del Level 2 de CALAIRE (certificado F-PSMT-01)", "12 puntos × 8 repeticiones × 6 días."],
])

MODULES = {
"m1": dict(num="M1", title="Fundamentos de la fotometría UV de ozono y trazabilidad metrológica", nav="Fotometría UV y trazabilidad", level="B", hours=4,
    goal="Comprender el principio de medida del SRP, su ecuación de medida y la posición del laboratorio en la cadena de trazabilidad del ozono.",
    parts=[("Medición y trazabilidad", [
        "Mensurando: la fracción molar de O₃ en nmol/mol.",
        "Error, sesgo, corrección, exactitud, veracidad y precisión: el vocabulario que el resto del curso cuantifica.",
        "Calibración, verificación y ajuste: tres actos distintos.",
        "Trazabilidad metrológica: cadena documentada e ininterrumpida, con incertidumbre en cada eslabón.",
        "CIPM MRA, laboratorio designado y CMC publicadas en la KCDB.",
    ]), ("Cómo mide el SRP", [
        "Ley de Beer-Lambert; absorbancia natural frente a decimal.",
        "Ecuación de medida: `x = −R·T / (2·σ·L·N_{A}·P) · ln D`.",
        "Medida diferencial con dos celdas: `D = (f_{11}·f_{22})/(f_{21}·f_{12})` cancela la deriva común de la lámpara.",
        "Correcciones de temperatura y presión.",
        "La sección eficaz σ es parte del modelo y depende de la temperatura y de la longitud de onda.",
    ]), ("En el SRP", [
        "Cadena propia: BIPM-SRP27 → SRP 55 → Level 2 → fotómetros y analizadores del país; contraste con NIST → SRP de la EPA → Level 2/3 → estaciones.",
        "Línea de Hg de 253,7 nm, celdas de unos 89,5 cm, semiciclos de 5 s, rango 0–1000 nmol/mol.",
        "Sección eficaz: de 1,147 a 1,1329(35)×10⁻¹⁷ cm²/molécula (304,39 atm⁻¹ cm⁻¹) desde 2025. Los resultados suben un 1,25 %; con el par 308,32/304,39 sale 1,29 %. Siempre hay que declarar el valor y sus unidades.",
        "Cerca de 253,6 nm, σ baja alrededor de 1 % entre 218 y 295 K.",
    ])],
    practice=["Dibujar la cadena del laboratorio con fechas, criterios e incertidumbre de cada eslabón.",
              "Recalcular 80, 420 y 500 nmol/mol con la sección eficaz antigua y la nueva.",
              "Comparar la dependencia térmica de σ en 210 nm, 253,6 nm y la banda de Huggins."],
    refs=[("mmu", "§§4.3–4.4 (error, sesgo, exactitud, precisión)"), ("ism", "caps. 2–3"), ("mmu", "§2.3.6 y cap. 7"), ("gum1", ""),
          ("nistir", "§§4–8"), ("srp6008", "pp. 1–2"), ("bipm", "§§1–1.1; Apéndice 1, ec. 8"), ("cfr50d", "§§2.2 y 4.1"),
          ("13964", "§7.1"), ("daumont", "§§2–3, Tabla II"), ("malicet", "§3, Tablas III–IV"), ("mw", "cap. 29 (ley de Beer)"),
          ("qapp", "Elementos 4–6 y 10"), ("sop", "§§1.2–1.3"), ("tad", "§§2.1–2.9"), ("17025", "§§6.4–6.5")]),

"m3": dict(num="M3", title="Estadística descriptiva y análisis exploratorio de datos", nav="Estadística descriptiva", level="B", hours=4, base="M1",
    goal="Resumir y representar un conjunto de lecturas con las medidas y gráficos adecuados, e identificar y tratar con criterio los valores atípicos.",
    parts=[("Teoría", [
        "Población y muestra; parámetro y estadístico.",
        "Tipos de variables y escalas de medida (nominal, ordinal, de intervalo y de razón).",
        "Notación de sumatoria.",
        "Distribución de frecuencias, histograma, percentiles, cuartiles y diagrama de caja.",
        "Tendencia central: media, mediana y moda, y cuándo usar cada una.",
        "Dispersión: rango, rango intercuartílico, varianza y desviación estándar muestral (por qué se divide por n − 1), coeficiente de variación, error estándar `s/√n`.",
        "Puntuación z, asimetría y curtosis.",
        "Cifras significativas y reglas de redondeo; redondear una sola vez, al final.",
        "Valores atípicos: un dato es atípico respecto de un modelo. Con n observaciones, `P = 1 − (1 − P_{i})^n`. Pruebas de Grubbs (simple y doble), Dixon y Cochran; estadísticos h y k de Mandel. Ningún dato se elimina sin una causa documentada.",
    ]), ("En el SRP", [
        "BIPM: 10 lecturas por punto; el conjunto se acepta si s_{SRP27} < 1 nmol/mol.",
        "Calibración del Level 2 (certificado F-PSMT-01): 8 réplicas por punto y por día, 48 lecturas por nivel.",
        "Las lecturas de cero negativas son ruido, no ozono físico: por qué no se truncan a cero.",
    ])],
    practice=["Con las 48 lecturas de un nivel del certificado: tabla de frecuencias, histograma, diagrama de caja, media, mediana, s y CV.",
              "Con un día: media y s por punto, serie de lecturas y decisión sobre un extremo con una lista de verificación (cero, purga, estabilización, celda)."],
    refs=[("sc", "§§1.3–1.5 (definiciones, variables, escalas)"), ("sc", "§§2.1–2.3 (distribuciones, histograma, percentiles)"),
          ("sc", "§§3.1–3.3 (sumatoria, tendencia central, dispersión)"), ("sc", "§§4.2–4.3 (puntuación z, asimetría, curtosis)"),
          ("ism", "§4.3 (análisis exploratorio)"), ("mmu", "§3.1 (cifras significativas, redondeo); §3.2.2"),
          ("otto", "§2.2, Tablas 2.10–2.11 (Dixon, Grubbs)"), ("5725", "Parte 2: Cochran, Grubbs, Mandel y tablas"),
          ("mw", "caps. 119–121 (valores atípicos)"), ("bipm", "§5"), ("nistir", "Tabla 2")]),

"m4": dict(num="M4", title="Probabilidad, variables aleatorias y distribuciones", nav="Probabilidad y distribuciones", level="B–I", hours=5, base="M1 · M2",
    goal="Modelar la variabilidad de una medida mediante variables aleatorias y distribuciones de probabilidad, y aplicar las propiedades de la esperanza y la varianza al ruido del SRP.",
    parts=[("Teoría", [
        "Probabilidad: definición y reglas básicas.",
        "Variable aleatoria discreta y continua; función de densidad y función de distribución acumulada.",
        "Esperanza y varianza de una variable aleatoria.",
        "Reglas para combinaciones lineales: `E[aX + bY] = a·E[X] + b·E[Y]` y `Var(aX + bY) = a²·Var X + b²·Var Y + 2ab·Cov(X,Y)`. Es la base de la ley de propagación de M9.",
        "Covarianza y coeficiente de correlación.",
        "Distribuciones y su uso: normal y normal estándar; rectangular (`u = a/√3`; resolución `δ/√12`); triangular (`u = a/√6`); t de Student; chi-cuadrado; F.",
        "Estimar los parámetros de una distribución y evaluar el ajuste: histograma y gráfico de probabilidad normal.",
    ]), ("En el SRP", [
        "¿Son normales las lecturas de un nivel? ¿Y las del cero?",
        "La resolución del analizador (0,1 nmol/mol) como variable rectangular.",
        "Ruido de conteo: la cuantización de ±0,5 cuentas es una variable rectangular, `0,5/√3` cuentas.",
        "Primera propagación con las reglas de la varianza: `u(x)/x = u(D)/|D·ln D|`. Con U(D) = 0,000017, U(x) ≈ 0,31 nmol/mol en todo el rango: 17 % a 1,8 nmol/mol y 0,06 % a 553 nmol/mol. El cero está limitado por la fotometría.",
        "Varianza de un promedio: promediar n lecturas reduce el ruido como 1/√n solo si son independientes; no reduce deriva ni sesgos.",
        "Covarianza en acción: la razón real entre canales tiene s = 0,000012, frente a 0,000089 si se supone independencia.",
        "Dos puntos medidos con el mismo patrón tienen covarianza: anticipo del término `u_{b}` del SRP27.",
    ])],
    practice=["NISTIR 6963, Tabla 5: de D a x y U(x) en cinco niveles.",
              "NISTIR 6963, Tabla 2: nueve lecturas de cero con valores negativos. ¿Hay ozono negativo?",
              "Con las 48 lecturas de un nivel: histograma y gráfico de probabilidad normal.",
              "Deducir la desviación estándar de una distribución rectangular y comprobarla con números aleatorios.",
              "Verificar con datos simulados la regla de la varianza de una suma, con y sin covarianza."],
    refs=[("sc", "§4.1 (normal)"), ("sc", "§5.1 (probabilidad)"), ("sc", "§8.2 (chi-cuadrado)"), ("sc", "§9.1.1 (distribución F)"),
          ("mmu", "§§3.2.1–3.2.5 (variable aleatoria, densidad, media y s de una distribución, rectangular, triangular, normal, t)"),
          ("ism", "§4.4 (distribuciones, estimación de parámetros, ajuste)"), ("ism", "§7.2 y §7.4.1 (base matemática, covarianza y correlación)"),
          ("brereton", "apéndice A (distribuciones y tablas)"), ("nistir", "§§8–11, Tablas 2, 3 y 5"), ("bipm", "Apéndice 1, ec. 11")]),

"m5": dict(num="M5", title="Inferencia estadística: estimación y contraste de hipótesis", nav="Inferencia estadística", level="I", hours=5, base="M2 · M3",
    goal="Estimar parámetros y contrastar hipótesis sobre un instrumento a partir de una muestra de lecturas, cuantificando el riesgo de cada decisión.",
    parts=[("Teoría", [
        "Muestreo aleatorio; estimador y estadístico; sesgo y varianza de un estimador; grados de libertad.",
        "Distribución muestral de la media y teorema central del límite; error estándar.",
        "Intervalo de confianza para una media (normal y t) y su interpretación.",
        "Prueba de hipótesis: H_{0} y H_{1}, estadístico de prueba, región crítica, nivel α y valor p.",
        "Errores tipo I y II, potencia y tamaño del efecto; tamaño de muestra (`n ≈ 15·(S/D)²` como regla rápida).",
        "Prueba t para una media; para dos medias independientes (incluida la versión de Welch) y para datos pareados.",
        "Pruebas sobre varianzas: una varianza (chi-cuadrado) y dos varianzas (F).",
        "Prueba chi-cuadrado de bondad de ajuste.",
        "Supuestos (independencia, normalidad) y cómo verificarlos.",
        "Significación estadística frente a relevancia metrológica; comparaciones múltiples.",
    ]), ("En el SRP", [
        "¿El sesgo de un fotómetro en un nivel es distinto de cero?",
        "SRP y fotómetro midiendo el mismo gas: el caso natural de la prueba t pareada.",
        "¿Cambió la dispersión del Level 2 de un año a otro? Prueba F.",
        "¿Cuántas réplicas hacen falta para detectar 1 nmol/mol?",
    ])],
    practice=["Intervalo de confianza al 95 % de la media de un nivel, con t.",
              "Prueba t pareada SRP frente a Level 2 en un día del certificado.",
              "Prueba F entre las varianzas de dos días; cálculo de potencia para un sesgo de 1 nmol/mol."],
    refs=[("sc", "§5.2 (muestreo, estimación, distribuciones muestrales)"), ("sc", "§§6.1, 6.4 (una media: potencia, tamaño del efecto, supuestos)"),
          ("sc", "§§7.1–7.2 (dos medias independientes y dependientes)"), ("sc", "§§8.2–8.3 (chi-cuadrado)"), ("sc", "§§9.1–9.3 (varianzas)"),
          ("mmu", "§§3.2.5.5–3.2.5.9 (t de Student, efecto de N)"), ("ism", "§4.4.2"), ("brereton", "apéndice A.3 (tablas t y F)"),
          ("mw", "cap. 15 (tamaño de muestra)"), ("asq", "cap. 27")]),

"m6": dict(num="M6", title="Diseño de experimentos aplicado a la calibración por comparación", nav="Diseño de experimentos", level="I", hours=5, base="M4",
    goal="Planificar experimentos que permitan estimar los efectos de interés y separar las fuentes de variación, y aplicarlos a las comparaciones del laboratorio.",
    parts=[("Teoría", [
        "Respuesta, factores, niveles y unidad experimental.",
        "Aleatorización y bloques; el día como bloque.",
        "Replicación verdadera frente a pseudorreplicación: diez lecturas seguidas no son diez réplicas independientes.",
        "Diseños anidados (lecturas dentro de corridas, corridas dentro de días) y anidados escalonados para la precisión intermedia.",
        "Factorial completo (`N = ∏ n_{i}`; 2^k con k factores a dos niveles): efectos principales e interacciones.",
        "Un factor a la vez frente a un factorial; estudios de robustez.",
        "Potencia aplicada al diseño (M5): cuántas corridas para detectar un efecto dado.",
    ]), ("En el SRP", [
        "Robustez del SRP y del Level 2: flujo, tiempo de acondicionamiento, temperatura del laboratorio y calentamiento. Hoy esos efectos se suponen o se toman de la literatura.",
        "Los ensayos de sensibilidad de la EN 14625 son diseños de un factor a la vez: presión a 80 y 110 kPa, gas a 0 y 30 °C, tres mediciones por condición.",
        "Validación del Level 2 como método del laboratorio (ISO/IEC 17025 §7.2.2).",
        "¿Cuántas corridas hacen falta para detectar un cambio de pendiente de 0,005 en el Level 2?",
    ])],
    table=("Diseños reales de comparación que conviene contrastar", DESIGN_TABLE),
    practice=["Diseñar un factorial 2³ de robustez del Level 2 (flujo, acondicionamiento, temperatura) con el día como bloque, y decir qué efectos e interacciones se podrán estimar.",
              "Identificar qué fuentes de variación puede separar cada diseño de la tabla y cuáles quedan confundidas.",
              "Analizar el diseño que usa hoy la calibración del Level 2 (12 × 8 × 6): qué fuentes separa, cuáles confunde y si los 6 días bastan para estimar la componente entre días."],
    refs=[("ism", "§9.2 (experimentos factoriales en metrología)"), ("brereton", "cap. 2 (diseño experimental, factoriales)"), ("mw", "caps. 8–16"),
          ("5725", "Parte 3: diseños anidados escalonados"), ("14625", "§§8.4.6–8.4.8"), ("17025", "§7.2.2"),
          ("bipm", "protocolo A §§3–7; protocolo B §§5–8"), ("qapp", "Elementos 6.2.1 y 7.1, Tabla 7-1"), ("sop", "§§9.7.19–9.7.20"),
          ("tad", "Tabla 4-1"), ("13964", "§6.2"), ("nistir", "§§8–10 (independencia de los ciclos)")]),

"m7": dict(num="M7", title="Análisis de varianza y evaluación de la precisión", nav="Análisis de varianza y precisión", level="I–A", hours=7, base="M4 · M5",
    goal="Descomponer la variabilidad mediante el análisis de varianza, estimar la repetibilidad, la precisión intermedia y sus componentes, y diseñar e interpretar estudios de repetibilidad y reproducibilidad.",
    parts=[("Teoría 1 · Modelo y descomposición de la variación", [
        "Modelo de un factor `y_{ij} = μ + τ_{i} + ε_{ij}`; supuestos: errores independientes, normales y de varianza común.",
        "Descomposición de sumas de cuadrados: `SS_{total} = SS_{entre} + SS_{dentro}`, con `a − 1` y `N − a` grados de libertad.",
        "Cuadrados medios y prueba `F = MS_{entre}/MS_{dentro}`: por qué el cociente sigue una distribución F cuando no hay efecto.",
        "Modelo de dos factores cruzados con interacción: `y_{ijk} = μ + A_{i} + D_{j} + (AD)_{ij} + ε_{ijk}`. Qué significa la interacción y cuándo hace falta réplica para estimarla.",
        "Diseño cruzado (todos los niveles de un factor con todos los del otro) frente a anidado (cada nivel de un factor aparece dentro de uno solo del otro, como lecturas dentro de ciclos y ciclos dentro de días).",
        "Revisión de supuestos con residuos; heterocedasticidad entre niveles de concentración y por qué obliga a analizar cada nivel por separado o a modelar la varianza.",
    ]), ("Teoría 2 · Efectos aleatorios y componentes de varianza", [
        "Efecto fijo (interesan esos niveles concretos) frente a efecto aleatorio (los niveles son una muestra de una población: días, analistas). Modelo mixto.",
        "Cuadrados medios esperados del modelo cruzado de efectos aleatorios con r réplicas: `E[MS_{e}] = σ_{e}²`; `E[MS_{AD}] = σ_{e}² + r·σ_{AD}²`; `E[MS_{D}] = σ_{e}² + r·σ_{AD}² + a·r·σ_{D}²`; `E[MS_{A}] = σ_{e}² + r·σ_{AD}² + d·r·σ_{A}²`.",
        "Estimadores por el método de los momentos: `σ̂_{A}² = (MS_{A} − MS_{AD})/(d·r)` y análogos. Estimaciones negativas: qué significan y cómo se informan.",
        "La prueba correcta de un efecto aleatorio usa como denominador el cuadrado medio cuyo valor esperado coincide salvo por ese efecto: el analista se contrasta contra MS_{AD}, no contra MS_{e}.",
        "Cuadrados medios esperados en un diseño anidado; diseño anidado escalonado para estimar varias componentes con pocos ensayos.",
        "Grados de libertad de cada componente y de su combinación (Welch-Satterthwaite): una componente estimada con 1 o 2 grados de libertad es muy imprecisa, y solo mejora aumentando el número de niveles de ese factor.",
        "Réplica verdadera frente a pseudorréplica: las lecturas consecutivas de un mismo ciclo subestiman la repetibilidad.",
    ]), ("Teoría 3 · Precisión y estudios R&R", [
        "Modelo de la ISO 5725 `y = m + B + e`; repetibilidad s_{r}, reproducibilidad s_{R} y precisión intermedia con M factores (tiempo, operador, equipo, calibración): `s_{I(T,O)} = √(σ_{e}² + σ_{T}² + σ_{O}² + …)`.",
        "Límites `r = 2,8·s_{r}` y `R = 2,8·s_{R}`; veracidad frente a un valor de referencia.",
        "Estudio R&R como ANOVA de efectos aleatorios: repetibilidad = σ_{e}², reproducibilidad = σ_{operador}² + σ_{interacción}², R&R = suma de ambas.",
        "El %R&R y el número de categorías distintas comparan el R&R con la variación entre piezas. Cuando las \"piezas\" son niveles de concentración fijados por diseño, esa variación no es del proceso y esos índices pierden sentido: en calibración se usa el marco de la ISO 5725-3.",
        "Una prueba t entre dos operadores contrasta medias; no estima componentes de varianza. Un resultado no significativo con pocos operadores no demuestra que la reproducibilidad sea despreciable.",
        "Las componentes estimadas por ANOVA son evaluaciones tipo A que entran al presupuesto de incertidumbre (GUM, Anexo H.5); s_{R} solo cubre las fuentes que variaron en el estudio.",
    ]), ("En el SRP", [
        "Estudio R&R de CALAIRE 2022–2023: para cada nivel, el libro apila tres campañas de calibración del Level 2 (116/118 de enero de 2022, 142/143 de agosto de 2022 y 171/173 de febrero de 2023), cada una de 6 días, con un error medio por día. Cada analista hizo su propia calibración: los días están anidados en analista × campaña, y el \"día 1\" de un analista no es el del otro. Identificar esta estructura es el primer paso; una prueba t sobre las 18 cifras de cada analista la ignora.",
        "Analizado con el modelo analista × campaña con días anidados: no hay efecto medio del analista (F ≤ 1,24 frente a F_{0,05; 1, 2} = 18,5, una prueba de muy poca potencia), pero la interacción analista × campaña es significativa en 135, 360, 405 y 455 ppb (F de 4,3 a 6,6 frente a F_{0,05; 2, 30} = 3,32): la diferencia entre analistas cambia de una campaña a otra, y esa interacción forma parte de la reproducibilidad.",
        "La variación entre días dentro de una campaña es de 0,11 a 0,21 ppb; la componente entre campañas crece con la concentración y domina en 405 y 455 ppb, donde destaca la campaña de agosto de 2022 del analista 2 (errores medios de 0,73 y 0,83 ppb frente a unos 0,2 en las demás).",
        "Diseño que permite estimar repetibilidad, día y analista: varios analistas × varios días × al menos 2 ciclos independientes por analista y día, con orden sorteado. Para la componente entre analistas, los grados de libertad dependen del número de analistas, no del número de lecturas.",
        "Para un solo laboratorio sirve la Parte 3 de la ISO 5725; las Partes 2 y 4 son para estudios interlaboratorio.",
    ])],
    practice=["Identificar la estructura de un diseño antes de analizarlo: a partir de la descripción de un estudio (quién midió, cuándo, cuántas veces), reconocer los factores, decidir si están cruzados o anidados, identificar la unidad de réplica y escribir el modelo con sus cuadrados medios esperados. Ejemplo: el estudio R&R de CALAIRE, cuyos días están anidados en analista × campaña; analizarlo como si los días fueran comunes a los dos analistas cambia la conclusión.",
              "Construir a mano la tabla ANOVA de un nivel del certificado (SS, g.l., MS, F) y revisar los supuestos con los residuos.",
              "Deducir los cuadrados medios esperados de un modelo cruzado de dos factores con réplicas y de un modelo con un factor anidado, y a partir de ellos los estimadores de cada componente y la prueba correcta de cada efecto.",
              "Reanalizar el estudio R&R de CALAIRE con el modelo analista × campaña con días anidados y comparar la conclusión con la prueba t del libro.",
              "Calcular los grados de libertad de cada componente para un diseño de 2, 3 y 4 analistas y decidir cuál justifica el esfuerzo.",
              "Analizar el factorial de robustez diseñado en M6 con un ANOVA de dos o tres factores."],
    refs=[("ism", "§§9.3.1–9.3.6 (efectos aleatorios y mixtos, Tablas 9.9–9.10, supuestos, estudio R&R)"), ("otto", "§2.3 (ANOVA de uno y varios factores)"),
          ("mw", "cap. 115 (ANOVA)"), ("brereton", "cap. 2 (ANOVA y error puro)"), ("sc", "cap. 9 (distribución F)"),
          ("5725", "Parte 3 §§5–6 (factores y modelo), §8 (estudio dentro del laboratorio), §§9.3–9.5 (diseños anidados)"),
          ("5725", "Partes 2 y 6, con sus corrigenda"), ("gum", "Anexo H.5 (análisis de varianza); G.4 (Welch-Satterthwaite)"),
          ("mmu", "§4.4 (repetibilidad y reproducibilidad)"), ("deldossi", "ISO 5725 frente a GUM"), ("14625", "§8.2"), ("ryr", "hojas 45ppb a 455ppb")]),

"m8": dict(num="M8", title="Análisis de regresión y funciones de calibración", nav="Análisis de regresión", level="I", hours=5, base="M3 · M4 · M6",
    goal="Estimar y validar una función de calibración, eligiendo el método de ajuste según la estructura de incertidumbre de los datos.",
    parts=[("Teoría", [
        "Correlación de Pearson y su inferencia; por qué la correlación no valida una calibración.",
        "Mínimos cuadrados: criterio, ecuaciones normales y solución `b = S_{xy}/S_{xx}`, `a = ȳ − b·x̄`; forma matricial `β = (XᵀX)⁻¹Xᵀy`.",
        "Supuestos del modelo; residuos y s_{e}.",
        "Incertidumbre de los parámetros: u(a), u(b) y `cov(a,b) = −x̄·s²/S_{xx}`.",
        "Bandas de confianza y de predicción; predicción inversa con incertidumbre.",
        "Prueba de la pendiente; R² y sus límites.",
        "Falta de ajuste con réplicas: `F = [SS_{LOF}/(m−2)] / [SS_{PE}/(N−m)]`; residuo relativo por nivel.",
        "Recta con intercepto frente a recta forzada por el origen.",
        "Mínimos cuadrados ponderados y regresión con incertidumbre en x e y (ver tabla).",
        "Validación de un ajuste ponderado: χ²_{obs} frente a χ²_{0,95; n−2} (ν = 10 con 12 puntos); en la ISO 6143, |residuo ponderado| ≤ 2.",
        "Función de análisis frente a función de calibración; prueba de compatibilidad.",
    ])],
    table=("Qué regresión usar según la incertidumbre (ISO/TS 28037)", (["Incertidumbre en", "Método"], [
        ["Solo y", "WLS; con incertidumbres iguales, OLS"],
        ["x e y, sin correlación", "GDR (distancia generalizada)"],
        ["x e y, covarianza dentro de cada par", "GDR correlacionada (cercana a York)"],
        ["Covarianzas entre valores de y", "GMR (Gauss-Markov)"],
        ["Covarianzas generales en ambos ejes", "GGMR: la comparación con el BIPM (M10)"],
    ])),
    note="Ejemplo real del QAPP (SRP36 contra SRP7): pendiente 1,00169 ± 0,00012, intercepto 0,152 ± 0,050 ppb, R² = 0,99999985. Un R² casi perfecto no dice si la recta cumple los criterios de aceptación.",
    practice=["Deducir las ecuaciones normales y comprobarlas con los promedios del certificado.",
              "Regresión del Level 2 contra el SRP, falta de ajuste con las 8 réplicas y gráfico de residuos.",
              "Los mismos 12 pares por OLS y por WLS/GDR, reportando a, b, u(a), u(b), cov(a,b) y χ²_{obs}.",
              "Reproducir un ejemplo resuelto de la ISO/TS 28037 y el ejemplo B.2.1 de la ISO 6143 (NO medido por absorción UV)."],
    refs=[("ism", "§§10.1–10.4 (mínimos cuadrados, WLS, incertidumbre de parámetros, bandas, residuos, prueba de pendiente)"),
          ("sc", "§§10.1, 10.4 (correlación, linealidad)"), ("otto", "§6.1 (Tabla 6.1) y §6.2"), ("brereton", "§2.2 y cap. 6"),
          ("mw", "cap. 21 (forma matricial); caps. 117–118"), ("gum", "Anexo H.3"), ("28037", "cláusulas 6–10 y ejemplos"),
          ("6143", "§§4–7 y Anexo B"), ("qapp", "Elemento 14.2")]),

"m9": dict(num="M9", title="Evaluación de la incertidumbre de medida y capacidad de medición y calibración", nav="Incertidumbre de medida y CMC", level="I", hours=6, base="M1 · M3 · M4 · M6 · M7",
    goal="Evaluar la incertidumbre de medida conforme a la GUM, construir el presupuesto del SRP nacional y el de una calibración, y relacionarlos con la CMC.",
    parts=[("Teoría", [
        "Modelo de medición (GUM-6): medición directa e indirecta.",
        "Incertidumbre estándar; evaluación tipo A (de M3 y M5) y tipo B (de las distribuciones de M4).",
        "Ley de propagación: desarrollo de Taylor de primer orden y coeficientes de sensibilidad `c_{i} = ∂f/∂x_{i}`.",
        "Entradas correlacionadas: `u_{c}² = Σ c_{i}²u_{i}² + 2·Σ c_{i}c_{j}·u(x_{i},x_{j})`.",
        "Términos de orden superior, varias magnitudes de salida y límites del método analítico.",
        "Grados de libertad efectivos (Welch-Satterthwaite) y `k = t(ν_{eff})` en lugar de k = 2 fijo.",
        "Incertidumbre expandida `U = k·u_{c}`, nivel de cobertura, presentación y redondeo.",
        "De la U de una calibración a la CMC; la plantilla aplica la regla `max(U, CMC)`.",
        "Propagación por la cadena: la incertidumbre del Level 2 (de su calibración contra el SRP) entra en el presupuesto de cada calibración de cliente.",
    ]), ("En el SRP: presupuestos reales", [
        "NIST SRP 6008: `u = √(0,28² + (0,011·x)²)` nmol/mol.",
        "BIPM-SRP27: `u = √(0,28² + (0,00292·x)²)`. El 0,00292 combina longitud óptica (2,89×10⁻³), presión (3,37×10⁻⁴) y temperatura (2,29×10⁻⁴); el 0,28 es la razón de intensidades D.",
        "La diferencia es la sección eficaz: el NIST incluye su incertidumbre (1,06×10⁻²·x) y el BIPM no, porque se cancela entre fotómetros UV con el mismo σ. ¿Cuándo debe entrar σ en un certificado?",
        "Componente común: `u(x_{i},x_{j}) = x_{i}·x_{j}·u_{b}²`, con u_{b} = 2,92×10⁻³.",
        "Pérdidas de ozono, pureza del aire cero y lámpara no tienen cifra en la literatura: son sesgos que el operador vigila y cuantifica con datos propios.",
        "Las EN convierten cada característica de desempeño en una contribución y comparan con el objetivo de calidad (15 % en mediciones fijas).",
    ])],
    practice=["Derivar los coeficientes de sensibilidad de la ecuación del SRP respecto de L, P, T, σ y D.",
              "Presupuesto completo de un punto de la calibración del Level 2: fuentes, sensibilidades, ν_{eff}, k y U.",
              "Llevar esa U al presupuesto de la calibración de un fotómetro de cliente hecha con el Level 2.",
              "Presupuesto del SRP nacional a 80 y 420 nmol/mol."],
    refs=[("mmu", "§§5.1–5.9 (tipo A y B, combinada, ν_eff, k, expandida, presentación)"), ("mmu", "§§6.1–6.2 (ley de propagación, variables dependientes)"),
          ("ism", "§§6.2–6.4 (marco de incertidumbre, modelos directo e indirecto)"), ("ism", "§§7.2–7.7 (base matemática, correlación, orden superior, salidas múltiples, límites)"),
          ("gum", "§§4–7 y Anexo H"), ("gum1", ""), ("gum6", "§§11–12"), ("srp6008", "p. 2"), ("bipm", "Apéndice 1"),
          ("nistir", "§§10–11, Tabla 6"), ("14625", "anexos E–G"), ("asq", "cap. 29")]),

"m10": dict(num="M10", title="Comparaciones clave: mínimos cuadrados generalizados y grado de equivalencia", nav="Comparaciones clave", level="I–A", hours=4, core=True, base="M7 · M8",
    goal="Comprender, reproducir y sustentar el resultado del laboratorio en la comparación clave BIPM.QM-K1.",
    parts=[("Teoría", [
        "Protocolo A (comparación directa) y protocolo B (con patrón de transferencia).",
        "Ajuste GLS: estima a la vez la recta y los valores \"verdaderos\" de x, con la matriz de covarianza completa de x e y; se resuelve por Gauss-Newton, da cov(a,b) y se valida con χ² y residuos.",
        "OLS, WLS, Deming y la ISO 6143 son casos particulares; ninguno admite la covarianza entre puntos que impone el SRP27.",
        "La covarianza se construye desde causas comunes: `u_{b}²·x·xᵀ` viene de la temperatura, la presión y la longitud óptica compartidas.",
        "Grado de equivalencia `D = x_{NS} − x_{SRP27}` a 80 y 420 nmol/mol, con u(D) y sus covarianzas.",
    ]), ("En el SRP", [
        "El BIPM ajusta con el software OzonE; Milton 2006 describe XGENLINE.",
        "Una rutina ODR que solo acepta errores independientes por punto no reproduce el ajuste del BIPM.",
        "Para reproducir la comparación propia: los 12 pares medidos, las incertidumbres en ambos ejes y las matrices U_{x}, U_{y} y U_{xy} (justificando si U_{xy} = 0).",
        "Los ceros inicial y final se tratan con su posible deriva, no como datos independientes duplicados.",
        "El resultado de la comparación respalda las CMC del laboratorio.",
    ])],
    practice=["Armar U_{x} para la secuencia BIPM con u_{b} = 0,00292 y compararla con la matriz diagonal que supone el OLS.",
              "Con los datos de una comparación real del laboratorio: contrastar OLS, ISO 6143 y GLS, y calcular los grados de equivalencia."],
    refs=[("milton", "§§2–5, 7 y Apéndice A"), ("28037", "cláusula 10 (GGMR)"), ("bipm", "§§7–9; protocolo B §§9–11; Apéndices 1 y 3"), ("6143", "§§4–7")]),

"m11": dict(num="M11", title="Evaluación de la conformidad y certificado de calibración", nav="Conformidad y certificado", level="I", hours=3, base="M4 · M8 · M9",
    goal="Aplicar reglas de decisión que incorporen la incertidumbre y emitir certificados de calibración técnicamente sustentados.",
    parts=[("Teoría", [
        "Conformidad con una especificación; regla de decisión, banda de guarda y riesgo de falsa aceptación o rechazo.",
        "TUR (relación de incertidumbre de ensayo).",
        "Compatibilidad entre un valor medido y uno de referencia.",
        "Corrección de lecturas: `c = (y − y_{0})·c_{c}/(y_{c} − y_{0})`.",
        "Contenido del certificado: mensurando, intervalo, método, resultados, U con k, trazabilidad, sección eficaz usada y regla de decisión.",
    ])],
    table=("Criterios reales (cada uno vale solo en su documento)", (["Documento", "Criterio"], [
        ["SRP QAPP", "Pendiente 1,00 ± 0,01; intercepto 0 ± 1 ppb"],
        ["SRP SOP", "1 ± 0,04 y 0 ± 4 ppb al calificar; 1 ± 0,03 y 0 ± 3 ppb al reverificar"],
        ["EPA TAD", "Pendiente 1,00 ± 0,03; intercepto 0 ± 3 ppb; s de pendientes < 0,0075"],
        ["BIPM.QM-K1", "Grado de equivalencia a 80 y 420 nmol/mol"],
    ])),
    practice=["Decidir si un patrón de transferencia pasa, primero sin la incertidumbre y luego con ella, y redactar la declaración de conformidad."],
    refs=[("ism", "cap. 5 (incertidumbre y riesgo en la decisión)"), ("mmu", "caps. 8–9"), ("asq", "cap. 30 (riesgo, TUR)"),
          ("17025", "§§7.6 y 7.8.6"), ("qapp", "Tabla 7-1"), ("sop", "§9.1"), ("tad", "§4"), ("14625", "§9.5.3")]),

"m12": dict(num="M12", title="Control estadístico de procesos y aseguramiento de la validez de los patrones", nav="Control estadístico de los patrones", level="I", hours=3, base="M2 · M4 · M7",
    goal="Vigilar la estabilidad del SRP y del Level 2 mediante control estadístico, modelar su deriva y fundamentar el intervalo de recalibración.",
    parts=[("Teoría", [
        "Control estadístico de procesos: variación por causas comunes y especiales.",
        "Cartas de control de Shewhart: línea central, límites de control y reglas de alarma.",
        "Deriva y predicción de valores futuros con su incertidumbre.",
        "Análisis del intervalo de calibración.",
        "Aseguramiento de la validez de los resultados.",
    ]), ("En el SRP", [
        "SOP: controles tan seguido como sea posible; temperatura y presión pueden derivar en 2–3 días.",
        "QAPP: aire cero 0 ± 0,2 ppb; presión ± 0,2 mbar.",
        "EPA TAD: Level 2 contra Level 1 cada año; 3 ciclos; s de pendientes < 0,0075; s de interceptos < 1,00 ppb. Son criterios directamente aplicables a la calibración del Level 2 de CALAIRE.",
        "NIST: con humedad por encima de 50 % se ha visto deriva del detector.",
    ])],
    practice=["Carta de control de la pendiente con las diez comparaciones SRP-0 contra SRP-2 del NISTIR 6963 (pendiente media 1,00003, s = 0,00056; intercepto −0,131 ppb, s = 0,142), o con el historial propio del Level 2.",
              "Ajustar la deriva de la pendiente en el tiempo y decidir si hay que recalibrar antes de lo previsto."],
    refs=[("ism", "§11.2 (control estadístico de procesos)"), ("ism", "§§10.8–10.9 (deriva, valores futuros, intervalo de calibración)"),
          ("otto", "cap. 9, Tablas 9.1–9.2 (cartas de control)"), ("sop", "§§9–11"), ("qapp", "Tabla 7-1"), ("tad", "§4 y Tabla 4-1"),
          ("nistir", "Tabla 4"), ("srp6008", "pp. 2–3"), ("17025", "§7.7")]),

"m13": dict(num="M13", title="Indicadores de precisión y sesgo en las redes de monitoreo", nav="Precisión y sesgo en redes", level="I", hours=3, base="M4 · M8 · M10",
    goal="Conocer los indicadores estadísticos con que las redes de monitoreo evalúan sus datos y su relación con los valores que certifica el laboratorio.",
    parts=[("Estadística oficial de la red (40 CFR 58, Apéndice A)", [
        "Diferencia de cada verificación: `d_{i} = (meas − audit)/audit · 100`.",
        "CV con límite superior al 90 %: `CV = s(d_{i})·√[(n−1)/χ²_{0,1; n−1}]` (intervalo para una varianza, M5).",
        "Sesgo absoluto con límite superior al 95 %: `|sesgo| = AB + t_{0,95; n−1}·AS/√n`, con el signo según los percentiles 25 y 75.",
        "Objetivo para O₃: CV ≤ 7 % y |sesgo| ≤ 7 %.",
        "Datos de origen: control de un punto, auditoría anual con patrones independientes y NPAP. Las concentraciones de ensayo vienen de un patrón de transferencia trazable: ahí entra el laboratorio.",
    ]), ("Contexto de los analizadores", [
        "El CV y el sesgo resumen un año de verificaciones de un monitor; la U de un certificado describe una sola calibración. No se sustituyen.",
        "Desempeño del analizador (40 CFR 53): ruido, límite detectable inferior, deriva de cero y span, precisión al 20 % y 80 % del rango.",
        "EN 14625: repetibilidad ≤ 1 nmol/mol en cero y ≤ 3 en el nivel de ensayo; deriva de cero ≤ 2 nmol/mol en 12 h. Las EN 14211, 14212 y 14626 sirven de contraste con otros gases.",
        "Datos regulatorios: promedio móvil de 8 h, cuarto máximo anual, valor de diseño comparado con 0,070 ppm, completitud.",
    ])],
    practice=["Con d_{i} = 1; 2; 0,5; 3; 1,5; 2,5 %: CV = 1,65 % y |sesgo| = 2,52 %, positivo.",
              "¿Cómo aparece en los d_{i} de una red un sesgo de +1,25 % por usar la sección eficaz antigua?",
              "Ejemplo de la EPA 2014–2016 sobre el valor de diseño."],
    refs=[("cfr58a", "§§2.3, 2.6, 3.1, 4.1 y 5.1"), ("qah", ""), ("cfr53", ""), ("cfr50", "Apéndices A-1, C y P/U"), ("valid", ""),
          ("14625", "§8 y Tabla E.1"), ("enothers", "")]),

"taller": dict(num="T", title="Taller integrador: casos reales del laboratorio", nav="Taller integrador", level="I–A", hours=8, base="M2–M12",
    goal="Integrar los métodos del curso en cuatro casos que corresponden a las funciones del laboratorio: calibrar el Level 2, compararse con el BIPM, vigilar sus patrones y evaluar su sistema de medición.",
    parts=[("Caso A · Calibración del Level 2 contra el SRP 55", [
        "Datos reales de CALAIRE: certificado F-PSMT-01, Thermo 49C contra SRP 55, 12 puntos × 8 repeticiones × 6 días.",
        "Descripción y atípicos (M3), normalidad (M4), ANOVA por días (M7), regresión y falta de ajuste (M8), presupuesto GUM con ν_{eff} y k (M9), decisión (M11).",
        "Comparar con lo que reporta la plantilla actual y discutir las diferencias.",
    ]), ("Caso B · Comparación clave con ajuste GLS", [
        "Datos publicados: comparación SRP36 contra SRP7 (QAPP, Fig. 14.2), tratada con el método del BIPM.",
        "OLS frente a GGMR con la covarianza común `u_{b}`, en dos variantes de incertidumbre; validación del código con un ejemplo de la ISO/TS 28037; χ² y su interpretación (M8, M10).",
        "Grados de equivalencia a 80 y 420 nmol/mol por interpolación con la recta, y por qué difiere de la ecuación del protocolo para mediciones directas (M10).",
        "Inconsistencias internas del propio QAPP (covarianza y desviación residual) como ejercicio de lectura crítica.",
    ]), ("Caso C · Historial y control estadístico del Level 2", [
        "Datos reales de CALAIRE (pendientes e interceptos de los 6 días) y diez comparaciones publicadas (NISTIR 6963, Tabla 4).",
        "Evaluación de los 6 días contra la verificación 6x6 del QAPP, que es el criterio directamente aplicable, y contraste con la EPA TAD 2023 (M11).",
        "Cartas de individuales y rango móvil a 3σ, prueba de deriva y prueba F (M5, M12).",
    ]), ("Caso D · Estudio R&R de CALAIRE 2022–2023", [
        "Datos reales: errores medios diarios del Level 2 frente al SRP 55 de dos analistas en 10 niveles, en tres campañas de 6 días cada una.",
        "Lectura crítica: reconstruir la estructura real (campañas, días anidados en analista × campaña), ver qué responde una prueba t entre analistas y qué no, y localizar los errores de fórmula del libro (varianzas con 12 de 18 datos, α distinto en un nivel).",
        "Reanálisis con el modelo analista × campaña con días anidados (M7): efecto del analista, interacción, componente entre campañas y entre días; los datos no están pareados por día. Qué diseño haría falta para estimar bien la reproducibilidad.",
    ])],
    practice=["Los casos B y C tienen enunciado paso a paso, datos con su fuente y solución de referencia reproducible en la carpeta casos_taller/ (datos en CSV y el script calc_casos.py). Los casos A y D se trabajan directamente sobre los libros de Excel de CALAIRE."],
    refs=[("cert", "plantilla .xlsm"), ("qapp", "Elemento 14.2, Fig. 14.2; §6.2.3 y Tabla 7-1"), ("bipm", "protocolo A §8; Apéndices 1 y 3"),
          ("milton", ""), ("28037", "cláusula 10, Tablas 25–26"), ("nistir", "Tabla 4"), ("tad", "Tabla 4-1, §4.4"),
          ("ism", "§11.2"), ("otto", "cap. 9"), ("ryr", "hojas 45ppb a 455ppb")]),

"m14": dict(num="M14", title="Temas avanzados (optativo)", nav="Temas avanzados", level="A", hours=4, base="M3 · M7 · M8",
    goal="Introducir métodos que superan la propagación lineal y la regresión de una sola respuesta.",
    parts=[("Temas", [
        "Monte Carlo frente a propagación lineal; Monte Carlo en ajuste de curvas.",
        "Pendiente e intercepto como salidas conjuntas.",
        "Regresión no lineal y regresión de distancia ortogonal.",
        "Implementación propia del ajuste GGMR/GLS y su validación.",
        "Bootstrap remuestreando días completos; regresión robusta y métodos robustos de la ISO 5725-5.",
        "Calibración multivariada (PCR, PLS): por qué no aporta en un fotómetro de una sola longitud de onda.",
        "Uso responsable de herramientas de IA para análisis, siempre verificando datos, unidades y supuestos.",
    ])],
    practice=[],
    refs=[("gums1", "y corrigendum"), ("gums2", ""), ("ism", "cap. 8; §§10.5–10.6"), ("28037", "cláusula 10"), ("milton", ""),
          ("5725", "Parte 5"), ("brereton", "cap. 6"), ("mw", "caps. 21–27"), ("huq", "§§1–2"), ("ai", "caps. 1, 4, 10 y 11")]),
}
ORDER = [m for b in BLOCKS for m in b[3]]
for _m in MODULES.values():
    if _m["num"].startswith("M"):
        _m["num"] = f"M{RENUM[int(_m['num'][1:])]}"

# ----------------------------------------------------------- listado de conceptos
# (grupo, [(concepto, qué se enseña, módulo, [(clave, ubicación)])])
CONCEPTS = [
    ("Datos y estadística descriptiva", [
        ("Población, muestra, parámetro y estadístico", "Distinguir lo que se quiere conocer de lo que se mide; notación.", "M3", [("sc", "§1.3")]),
        ("Tipos de variables y escalas de medida", "Discretas y continuas; escalas nominal, ordinal, de intervalo y de razón.", "M3", [("sc", "§§1.4–1.5"), ("ism", "§4.2")]),
        ("Distribución de frecuencias e histograma", "Tablas de frecuencia absoluta, relativa y acumulada; formas de una distribución.", "M3", [("sc", "§§2.1–2.2"), ("ism", "§4.3.2")]),
        ("Percentiles, cuartiles y diagrama de caja", "Posición relativa de un dato; rango intercuartílico; lectura de la caja.", "M3", [("sc", "§2.3"), ("ism", "§4.3.2")]),
        ("Tendencia central", "Media, mediana y moda; propiedades y cuándo usar cada una.", "M3", [("sc", "§3.2"), ("ism", "§4.3.1")]),
        ("Dispersión", "Rango, varianza, desviación estándar muestral (n − 1), coeficiente de variación.", "M3", [("sc", "§3.3"), ("mmu", "§3.2.2")]),
        ("Error estándar de la media", "`s/√n`: dispersión de la media, no de las lecturas.", "M3, M5", [("ism", "§4.3.1"), ("sc", "§5.2")]),
        ("Puntuación z, asimetría y curtosis", "Estandarización; medidas de forma de la distribución.", "M3", [("sc", "§§4.2–4.3")]),
        ("Cifras significativas y redondeo", "Reglas de redondeo y de operación; redondear al final.", "M3, M9", [("mmu", "§3.1")]),
        ("Valor atípico", "Definición respecto de un modelo; Grubbs, Dixon, Cochran, h y k de Mandel; criterios de exclusión.", "M3", [("otto", "§2.2"), ("5725", "Parte 2"), ("mw", "caps. 119–121")]),
    ]),
    ("Probabilidad y distribuciones", [
        ("Probabilidad", "Definición y reglas básicas; intuición frente a probabilidad.", "M4", [("sc", "§5.1")]),
        ("Variable aleatoria", "Discreta y continua; experimento aleatorio y muestra.", "M4", [("mmu", "§3.2.1")]),
        ("Función de densidad y de distribución", "Densidad de probabilidad discreta y continua; distribución acumulada.", "M4", [("mmu", "§3.2.3")]),
        ("Esperanza y varianza", "Media y desviación estándar de una distribución.", "M4", [("mmu", "§3.2.4")]),
        ("Reglas de la esperanza y la varianza", "Combinaciones lineales; varianza de una suma con covarianza. Base de la propagación.", "M4, M9", [("ism", "§7.2")]),
        ("Covarianza y correlación", "Definición, signo, rango de r y efecto sobre la varianza combinada.", "M4, M9", [("ism", "§7.4.1"), ("sc", "§10.1")]),
        ("Distribución normal", "Propiedades, normal estándar y uso de tablas.", "M4", [("sc", "§4.1"), ("mmu", "§3.2.5.4")]),
        ("Distribuciones rectangular y triangular", "Cuándo se usan y su desviación estándar (`a/√3`, `a/√6`).", "M4, M9", [("mmu", "§§3.2.5.1–3.2.5.3"), ("mmu", "§5.3")]),
        ("Distribución t de Student", "Origen, grados de libertad y convergencia a la normal.", "M4, M5", [("mmu", "§3.2.5.5"), ("sc", "§6.1")]),
        ("Distribuciones chi-cuadrado y F", "Origen y uso en pruebas sobre varianzas y en el ANOVA.", "M4, M5", [("sc", "§8.2"), ("sc", "§9.1.1")]),
        ("Ajuste a una distribución", "Estimar parámetros; gráfico de probabilidad normal; pruebas de normalidad.", "M4", [("ism", "§§4.4.1–4.4.3"), ("sc", "§6.4")]),
    ]),
    ("Inferencia", [
        ("Muestreo aleatorio y estimación", "Estimador, sesgo y varianza de un estimador; grados de libertad.", "M5", [("sc", "§5.2")]),
        ("Distribución muestral y teorema central del límite", "Comportamiento de la media de n lecturas.", "M5", [("sc", "§5.2.2"), ("mmu", "§§3.2.5.6–3.2.5.9")]),
        ("Intervalo de confianza", "Construcción con normal y con t; interpretación correcta.", "M5", [("sc", "§6.1"), ("ism", "§4.4.2")]),
        ("Prueba de hipótesis", "H₀, H₁, estadístico, región crítica, α y valor p.", "M5", [("sc", "§§6.1, 7.1.2")]),
        ("Errores tipo I y II, potencia, tamaño del efecto", "Riesgos de una prueba y tamaño de muestra.", "M5, M6", [("sc", "§§6.1.2–6.1.4"), ("mw", "cap. 15")]),
        ("Prueba t", "Una media, dos medias independientes (Welch) y datos pareados.", "M5", [("sc", "§6.1"), ("sc", "§§7.1–7.2")]),
        ("Pruebas sobre varianzas", "Una varianza (chi-cuadrado) y dos varianzas (F).", "M5", [("sc", "§§9.1–9.3")]),
        ("Prueba chi-cuadrado de bondad de ajuste", "Comparar frecuencias observadas y esperadas.", "M5", [("sc", "§8.3.1")]),
        ("Supuestos de las pruebas", "Independencia y normalidad; cómo verificarlos.", "M5, M7", [("sc", "§§6.1.5, 6.4"), ("ism", "§9.3.3")]),
        ("Significación frente a relevancia", "Un efecto detectable puede no importar metrológicamente, y al revés.", "M5", [("sc", "§6.1.4"), ("mw", "cap. 15")]),
    ]),
    ("Diseño experimental y ANOVA", [
        ("Elementos de un experimento", "Respuesta, factores, niveles y unidad experimental.", "M6", [("ism", "§§9.2.1–9.2.3"), ("brereton", "cap. 2")]),
        ("Aleatorización, bloques y replicación", "Replicación verdadera frente a pseudorreplicación.", "M6", [("brereton", "cap. 2"), ("mw", "caps. 8–12")]),
        ("Diseño factorial", "Efectos principales e interacciones; 2^k.", "M6", [("ism", "§9.2"), ("brereton", "cap. 2"), ("mw", "caps. 8–16")]),
        ("Diseño anidado", "Lecturas dentro de corridas dentro de días; diseño escalonado.", "M6, M7", [("5725", "Parte 3")]),
        ("ANOVA de un factor", "Descomposición de sumas de cuadrados, cuadrados medios y prueba F.", "M7", [("otto", "§2.3"), ("mw", "cap. 115")]),
        ("Efectos fijos y aleatorios; componentes de varianza", "Cuadrados medios esperados y estimación de σ²_{día}.", "M7", [("ism", "§§9.3.1–9.3.2")]),
        ("ANOVA de dos factores, anidado y mixto", "Interacción y factores anidados.", "M7", [("otto", "§2.3"), ("ism", "§9.3.2")]),
        ("Supuestos del ANOVA", "Independencia, normalidad y varianza homogénea; residuos.", "M7", [("ism", "§9.3.3")]),
        ("Estudio R&R del sistema de medición", "Modelo cruzado con efectos aleatorios, componentes de varianza y R&R total; diferencia con la ISO 5725 y con una prueba t entre operadores.", "M7", [("ism", "§9.3.4")]),
        ("Cuadrados medios esperados", "Valor esperado de cada cuadrado medio en modelos cruzados y anidados; base de los estimadores y de la elección del denominador de F.", "M7", [("ism", "§9.3.1, Tablas 9.9–9.10")]),
        ("Diseño cruzado frente a anidado", "Qué componentes permite estimar cada estructura; diseño anidado escalonado.", "M6, M7", [("5725", "Parte 3 §§9.3–9.5")]),
        ("Grados de libertad de una componente de varianza", "Precisión de una componente según el número de niveles de su factor; Welch-Satterthwaite para combinaciones.", "M7", [("gum", "G.4"), ("ism", "§9.3.4")]),
        ("Repetibilidad, reproducibilidad y precisión intermedia", "Definiciones, estimación y límites r y R.", "M7", [("mmu", "§4.4"), ("5725", "Partes 2, 3 y 6")]),
        ("Veracidad y sesgo", "Sesgo frente a un valor de referencia.", "M7, M11", [("5725", "Partes 4 y 6"), ("mmu", "§4.3.2")]),
    ]),
    ("Regresión y calibración", [
        ("Correlación de Pearson", "Cálculo, inferencia y por qué no valida una calibración.", "M8", [("sc", "§10.1")]),
        ("Mínimos cuadrados", "Criterio, ecuaciones normales y forma matricial.", "M8", [("ism", "§10.2.1"), ("mw", "cap. 21")]),
        ("Incertidumbre de los parámetros", "u(a), u(b) y su covarianza.", "M8", [("ism", "§§10.2.2, 10.3.1")]),
        ("Bandas de confianza y de predicción", "Incertidumbre de la recta y de una nueva observación.", "M8", [("ism", "§§10.3.2–10.3.3")]),
        ("Análisis de residuos y prueba de pendiente", "Diagnóstico gráfico y cuantitativo del modelo.", "M8", [("ism", "§10.4")]),
        ("Falta de ajuste", "Error puro frente a falta de ajuste con réplicas.", "M8", [("otto", "§6.1, Tabla 6.1"), ("brereton", "§2.2")]),
        ("Calibración inversa", "Predecir x a partir de una nueva y, con incertidumbre.", "M8", [("otto", "§6.2"), ("28037", "")]),
        ("Mínimos cuadrados ponderados", "Pesos según u(y).", "M8", [("ism", "§10.2.3"), ("28037", "cláusula 6")]),
        ("Incertidumbre en x e y", "GDR, Deming y York como casos particulares.", "M8", [("ism", "§10.2.4"), ("28037", "cláusulas 7–8")]),
        ("Mínimos cuadrados generalizados", "Matriz de covarianza completa; GMR y GGMR.", "M8, M10", [("milton", ""), ("28037", "cláusulas 9–10")]),
        ("Validación con chi-cuadrado", "χ²_{obs} frente a sus grados de libertad; residuos ponderados.", "M8, M10", [("28037", ""), ("6143", "")]),
    ]),
    ("Incertidumbre de medición", [
        ("Modelo de medición", "Mensurando, magnitudes de entrada y ecuación del modelo.", "M9", [("gum6", ""), ("ism", "§§6.3–6.4")]),
        ("Evaluación tipo A y tipo B", "De los datos y de otra información.", "M9", [("mmu", "§§5.2–5.3"), ("ism", "§§6.2.2–6.2.3")]),
        ("Ley de propagación", "Desarrollo de Taylor de primer orden y coeficientes de sensibilidad.", "M9", [("mmu", "§6.1"), ("ism", "§§7.2–7.3")]),
        ("Entradas correlacionadas", "Término de covarianza en la propagación.", "M9", [("mmu", "§6.2"), ("ism", "§7.4")]),
        ("Incertidumbre combinada y expandida", "u_{c}, k, U y nivel de cobertura.", "M9", [("mmu", "§§5.5, 5.7–5.8"), ("ism", "§§6.2.4–6.2.5")]),
        ("Grados de libertad efectivos", "Welch-Satterthwaite y k con t.", "M9", [("mmu", "§5.6")]),
        ("Presentación del resultado", "Resultado ± U con k y unidades; redondeo.", "M9", [("mmu", "§5.9"), ("gum", "§7")]),
        ("Método de Monte Carlo", "Propagación de distribuciones.", "M14", [("ism", "cap. 8"), ("gums1", "")]),
        ("Varias magnitudes de salida", "Pendiente e intercepto como salida conjunta.", "M14", [("ism", "§7.6"), ("gums2", "")]),
    ]),
    ("Decisión y control", [
        ("Regla de decisión y riesgo", "Banda de guarda, falsa aceptación y falso rechazo.", "M11", [("ism", "cap. 5"), ("mmu", "cap. 8"), ("asq", "cap. 30")]),
        ("TUR", "Relación de incertidumbre de ensayo.", "M11", [("asq", "cap. 30")]),
        ("Grado de equivalencia", "Diferencia con la referencia y su incertidumbre con covarianzas.", "M10", [("bipm", "§8 y Apéndice 1")]),
        ("Cartas de control", "Shewhart: línea central, límites y reglas.", "M12", [("ism", "§11.2"), ("otto", "cap. 9")]),
        ("Deriva e intervalo de calibración", "Predicción de valores futuros y elección del intervalo.", "M12", [("ism", "§§10.8–10.9")]),
        ("Estadística de precisión y sesgo de la red", "CV y sesgo con límites de confianza (chi-cuadrado y t).", "M13", [("cfr58a", "§4.1")]),
    ]),
]

# ------------------------------------------------------------------ utilidades
def renum(t):
    return re.sub(r"\bM(\d+)\b", lambda mm: f"M{RENUM[int(mm.group(1))]}", t)

def to_html(t):
    t = html.escape(renum(t), quote=False)
    t = re.sub(r"_\{([^}]*)\}", r"<sub>\1</sub>", t)
    t = re.sub(r"`([^`]*)`", r'<span class="f">\1</span>', t)
    return t

def to_md(t):
    return re.sub(r"_\{([^}]*)\}", r"_\1", renum(t))

def used_by():
    used = {}
    for mid in ORDER:
        m = MODULES[mid]
        for k, _ in m["refs"]:
            used.setdefault(k, []).append(m["num"])
    for _, items in CONCEPTS:
        for _, _, mod, refs in items:
            for k, _ in refs:
                used.setdefault(k, [])
    out = {}
    for k, v in used.items():
        seen = []
        for x in v:
            if x not in seen:
                seen.append(x)
        out[k] = seen
    return out

def ref_html(k, loc):
    short = BIBKEY[k][0]
    loc = f" {to_html(loc)}" if loc else ""
    return f'<a href="#b-{k}">{html.escape(short)}</a>{loc}'

def ref_md(k, loc):
    short = BIBKEY[k][0]
    return f"{short} {to_md(loc)}".strip()

core_hours = sum(MODULES[m]["hours"] for m in ORDER if m != "m14")
opt_hours = core_hours + MODULES["m14"]["hours"]
n_core_mods = len([m for m in ORDER if m.startswith("m") and m != "m14"])

CHAIN = [
    ("BIPM-SRP27", "Referencia común de la comparación clave BIPM.QM-K1", "M9"),
    ("SRP 55 (NIST)", "Patrón Nivel 1 de CALAIRE, laboratorio designado", "M1 · M3 · M8 · M11"),
    ("Level 2: Thermo 49C", "Patrón de uso diario; caso integrador del curso", "M2–M8 · M11"),
    ("Fotómetros del país", "Clientes calibrados con certificado y CMC", "M7 · M8 · M10"),
    ("Redes de monitoreo", "Uso del certificado en verificaciones y auditorías", "M12"),
]

INTRO = ("El curso avanza con el trabajo del laboratorio y cada concepto estadístico aparece cuando la tarea lo necesita, apoyado en los anteriores. "
         "Primero se ve qué mide el SRP y cómo; con sus lecturas se aprende a describir datos, a modelar su variación con probabilidad y distribuciones "
         "(lo que explica el ruido del SRP) y a sacar conclusiones con pocas lecturas. Esa inferencia permite planear la comparación (diseño experimental), "
         "separar sus fuentes de variación (ANOVA), ajustar la recta (regresión) y expresar el resultado con su incertidumbre. Al final, todo se aplica a lo que "
         "solo hace el laboratorio designado: la comparación con el BIPM, la decisión y el certificado, el control diario de sus patrones y la relación con las redes. "
         "Cada módulo indica en qué módulos anteriores se apoya.")

# ------------------------------------------------------------------- HTML
def build_html():
    used = used_by()
    o = [HEAD.read_text()]
    o.append('<style>.concepts td:nth-child(3){white-space:nowrap;font-family:var(--font-mono);font-size:.82rem;color:var(--accent)}'
             '.concepts td:first-child{font-family:var(--font-display);font-weight:600;font-size:.9rem;min-width:11rem}'
             '.concepts td:last-child{font-size:.85rem;color:var(--muted);min-width:12rem}.concepts td:last-child a{font-family:var(--font-display);font-weight:600;font-size:.82rem}'
             '.concepts tr.block td{background:var(--accent-soft);font-family:var(--font-display);font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;font-weight:600;color:var(--ink)}'
             'section.concepts-sec{display:grid;gap:1rem}section.concepts-sec p{margin:0;max-width:68ch}'
             '.base{margin:0;font-family:var(--font-display);font-size:.8rem;color:var(--muted);letter-spacing:.02em}</style>\n')
    o.append('<div class="wrap-page">\n<header class="top">\n')
    o.append('  <div class="eyebrow">Propuesta de temario · Laboratorio designado de ozono</div>\n')
    o.append('  <h1>Estadística aplicada a la fotometría de ozono con el SRP</h1>\n')
    o.append('  <p class="lede">Curso de estadística para los operadores del SRP de CALAIRE, laboratorio designado por el INM. Desarrolla la estadística a medida que la necesita el trabajo del laboratorio, desde las lecturas del SRP hasta la comparación con el BIPM, la calibración de los fotómetros del país y el mantenimiento del patrón Level 2.</p>\n')
    o.append('  <dl class="facts">\n')
    o.append('    <div><dt>Público</dt><dd>Operadores del SRP de CALAIRE, laboratorio designado por el INM</dd></div>\n')
    o.append(f'    <div><dt>Duración</dt><dd>{core_hours} h de núcleo ({n_core_mods} módulos y taller final) + {MODULES["m14"]["hours"]} h optativas</dd></div>\n')
    o.append('    <div><dt>Caso integrador</dt><dd>Calibración del Level 2 de CALAIRE (Thermo 49C) contra el SRP 55, certificado F-PSMT-01: 12 puntos × 8 repeticiones × 6 días</dd></div>\n')
    o.append('    <div><dt>Niveles</dt><dd>B básico · I intermedio · A avanzado</dd></div>\n  </dl>\n')
    o.append('  <div class="chain" aria-label="Cadena de trazabilidad del ozono">\n    <h2>Cadena de trazabilidad y módulos que la cubren</h2>\n    <div class="chain-scroll">\n      <ol>\n')
    for n, d, mods in CHAIN:
        o.append(f'        <li><strong>{n}</strong><span>{d}</span><div class="mods">{mods}</div></li>\n')
    o.append('      </ol>\n    </div>\n  </div>\n</header>\n\n<div class="layout">\n\n<nav class="toc" aria-label="Índice">\n  <h2>Índice</h2>\n  <ol>\n')
    o.append('    <li><a href="#resumen"><b>—</b>Mapa del curso</a></li>\n')
    for bnum, btitle, _, mids in BLOCKS:
        label = f"{bnum} · {btitle}" if bnum != "Cierre" else "Cierre"
        o.append(f'    <li class="blk">{html.escape(label)}</li>\n')
        for mid in mids:
            m = MODULES[mid]
            short = m.get("nav", m["title"])
            o.append(f'    <li><a href="#{m["num"].lower() if m["num"] != "T" else "taller"}"><b>{m["num"]}</b>{html.escape(short)}</a></li>\n')
    o.append('    <li class="blk">Referencia</li>\n')
    o.append('    <li><a href="#conceptos"><b>—</b>Conceptos estadísticos</a></li>\n')
    o.append('    <li><a href="#bibliografia"><b>—</b>Bibliografía</a></li>\n  </ol>\n</nav>\n\n<main>\n\n')
    # mapa
    o.append(f'<section class="intro" id="resumen">\n  <h2>Mapa del curso</h2>\n  <p>{html.escape(INTRO)}</p>\n  <div class="tbl">\n    <table class="overview">\n')
    o.append('      <thead><tr><th>Módulo</th><th>Tema</th><th>Nivel</th><th class="num">Horas</th></tr></thead>\n      <tbody>\n')
    for bnum, btitle, _, mids in BLOCKS:
        label = f"{bnum} · {btitle}" if bnum != "Cierre" else "Cierre"
        o.append(f'        <tr class="block"><td colspan="4">{html.escape(label)}</td></tr>\n')
        for mid in mids:
            m = MODULES[mid]
            o.append(f'        <tr><td>{m["num"]}</td><td>{html.escape(m["title"])}</td><td>{m["level"]}</td><td class="num">{m["hours"]}</td></tr>\n')
    o.append(f'      </tbody>\n      <tfoot><tr><td colspan="3">Núcleo / con optativo</td><td class="num">{core_hours} / {opt_hours}</td></tr></tfoot>\n    </table>\n  </div>\n</section>\n\n')
    # módulos
    for bnum, btitle, bdesc, mids in BLOCKS:
        bid = f"b{bnum}".replace(" ", "")
        eyebrow = f"Bloque {bnum}" if bnum != "Cierre" else "Cierre"
        o.append(f'<section class="block" aria-labelledby="{bid}">\n  <div class="block-head">\n    <div class="eyebrow">{eyebrow}</div>\n    <h2 id="{bid}">{html.escape(btitle)}</h2>\n    <p>{html.escape(bdesc)}</p>\n  </div>\n\n')
        for mid in mids:
            m = MODULES[mid]
            cls = "mod core" if m.get("core") else "mod"
            o.append(f'  <article class="{cls}" id="{m["num"].lower() if m["num"] != "T" else "taller"}">\n    <div class="mod-head">\n      <div class="mod-num">{m["num"]}</div>\n      <h3>{html.escape(m["title"])}</h3>\n')
            chips = f'<span class="chip lvl">{m["level"]}</span><span class="chip">{m["hours"]} h</span>'
            if m.get("core"):
                chips += '<span class="chip key">Módulo central</span>'
            o.append(f'      <div class="meta">{chips}</div>\n    </div>\n')
            o.append(f'    <p class="goal">{to_html(m["goal"])}</p>\n')
            if m.get("base"):
                o.append(f'    <p class="base">Se apoya en {m["base"]}</p>\n')
            parts = m["parts"]
            if parts:
                two = len(parts) >= 2
                o.append(f'    <div class="parts{" two" if two else ""}">\n')
                for i, (pt, items) in enumerate(parts):
                    o.append(f'      <div class="part">\n        <h4>{html.escape(pt)}</h4>\n        <ul>\n')
                    for it in items:
                        o.append(f'          <li>{to_html(it)}</li>\n')
                    o.append('        </ul>\n      </div>\n')
                o.append('    </div>\n')
            if m.get("table"):
                tt, (hdr, rows) = m["table"]
                o.append(f'    <div class="part">\n      <h4>{html.escape(tt)}</h4>\n      <div class="tbl">\n        <table>\n          <thead><tr>')
                o.append("".join(f"<th>{html.escape(h)}</th>" for h in hdr))
                o.append('</tr></thead>\n          <tbody>\n')
                for r in rows:
                    o.append("            <tr>" + "".join(f"<td>{to_html(c)}</td>" for c in r) + "</tr>\n")
                o.append('          </tbody>\n        </table>\n      </div>\n    </div>\n')
            if m.get("note"):
                o.append(f'    <p class="note">{to_html(m["note"])}</p>\n')
            if m["practice"]:
                o.append('    <div class="part practice">\n      <h4>Práctica</h4>\n      <ul>\n')
                for it in m["practice"]:
                    o.append(f'        <li>{to_html(it)}</li>\n')
                o.append('      </ul>\n    </div>\n')
            o.append('    <div class="refs">\n      <h4>Referencias</h4>\n      <ul>\n')
            for k, loc in m["refs"]:
                o.append(f'        <li>{ref_html(k, loc)}</li>\n')
            o.append('      </ul>\n    </div>\n  </article>\n\n')
        o.append('</section>\n\n')
    # conceptos
    o.append('<section class="concepts-sec" id="conceptos" aria-labelledby="concH">\n  <div class="block-head">\n    <div class="eyebrow">Referencia</div>\n    <h2 id="concH">Conceptos estadísticos del curso</h2>\n')
    o.append('    <p>Cada concepto con lo que se enseña de su teoría, el módulo donde se trata y la fuente teórica con sección.</p>\n  </div>\n')
    o.append('  <div class="tbl">\n    <table class="concepts">\n      <thead><tr><th>Concepto</th><th>Qué se enseña</th><th>Módulo</th><th>Fuente teórica</th></tr></thead>\n      <tbody>\n')
    for g, items in CONCEPTS:
        o.append(f'        <tr class="block"><td colspan="4">{html.escape(g)}</td></tr>\n')
        for c, what, mod, refs in items:
            rs = "; ".join(ref_html(k, loc) for k, loc in refs)
            o.append(f'        <tr><td>{to_html(c)}</td><td>{to_html(what)}</td><td>{renum(mod)}</td><td>{rs}</td></tr>\n')
    o.append('      </tbody>\n    </table>\n  </div>\n</section>\n\n')
    # bibliografía
    o.append('<section class="biblio" id="bibliografia" aria-labelledby="bibh">\n  <div class="block-head">\n    <div class="eyebrow">Fuentes</div>\n    <h2 id="bibh">Bibliografía</h2>\n')
    o.append('    <p>Todas las fuentes están en la carpeta <code>docs/</code> del proyecto. Debajo de cada una se indica en qué módulos se usa.</p>\n  </div>\n\n')
    for g, items in BIB:
        o.append(f'  <div class="bib-group">\n    <h3>{html.escape(g)}</h3>\n    <dl>\n')
        for k, short, full, f in items:
            u = used.get(k, [])
            utxt = " · ".join(u) if u else "Listado de conceptos"
            files = "; ".join(f"<code>{html.escape(x.strip())}</code>" for x in f.split(";"))
            o.append(f'      <div id="b-{k}"><dt>{html.escape(short)}</dt><dd>{full} {files}<span class="used">{utxt}</span></dd></div>\n')
        o.append('    </dl>\n  </div>\n\n')
    o.append('</section>\n\n<footer>Propuesta de temario · 22 de octubre de 2026</footer>\n\n</main>\n</div>\n</div>\n')
    return "".join(o)

# --------------------------------------------------------------------- MD
def build_md():
    used = used_by()
    o = ["# Estadística aplicada a la fotometría de ozono con el SRP\n\n",
         "**Propuesta de temario**, 22-10-2026. Versión web: `temario_curso.html`.\n\n",
         "- **Público:** los operadores del SRP de CALAIRE, laboratorio designado por el INM. Este laboratorio compara su SRP contra el BIPM-SRP27 (BIPM.QM-K1), calibra los fotómetros y analizadores de ozono del país (certificados con CMC) y mantiene un patrón Level 2 para uso diario.\n",
         f"- **Duración:** {core_hours} h de núcleo ({n_core_mods} módulos y taller final) más {MODULES['m14']['hours']} h optativas.\n",
         "- **Caso integrador:** calibración del Level 2 de CALAIRE (Thermo 49C, S/N 59756-324) contra el SRP 55, certificado F-PSMT-01: 12 puntos × 8 repeticiones × 6 días.\n",
         "- **Niveles:** B básico · I intermedio · A avanzado.\n\n",
         "## Cadena de trazabilidad y módulos que la cubren\n\n| Eslabón | Papel | Módulos |\n|---|---|---|\n"]
    for n, d, mods in CHAIN:
        o.append(f"| {n} | {d} | {mods} |\n")
    o.append(f"\n## Mapa del curso\n\n{INTRO}\n\n| Módulo | Tema | Nivel | Horas |\n|---|---|---|---:|\n")
    for bnum, btitle, _, mids in BLOCKS:
        label = f"{bnum} · {btitle}" if bnum != "Cierre" else "Cierre"
        o.append(f"| **{label}** | | | |\n")
        for mid in mids:
            m = MODULES[mid]
            o.append(f"| {m['num']} | {m['title']} | {m['level']} | {m['hours']} |\n")
    o.append(f"| | **Núcleo / con optativo** | | **{core_hours} / {opt_hours}** |\n\n")
    for bnum, btitle, bdesc, mids in BLOCKS:
        head = f"Bloque {bnum} · {btitle}" if bnum != "Cierre" else "Cierre"
        o.append(f"---\n\n# {head}\n\n{bdesc}\n\n")
        for mid in mids:
            m = MODULES[mid]
            extra = "; módulo central" if m.get("core") else ""
            num = m["num"] if m["num"] != "T" else "T"
            o.append(f"## {num}. {m['title']} ({m['level']}, {m['hours']} h{extra})\n\n**Objetivo:** {to_md(m['goal'][0].lower() + m['goal'][1:])}\n\n")
            if m.get("base"):
                o.append(f"**Se apoya en:** {m['base']}\n\n")
            for pt, items in m["parts"]:
                o.append(f"**{pt}**\n")
                for it in items:
                    o.append(f"- {to_md(it)}\n")
                o.append("\n")
            if m.get("table"):
                tt, (hdr, rows) = m["table"]
                o.append(f"**{tt}**\n\n| " + " | ".join(hdr) + " |\n|" + "---|" * len(hdr) + "\n")
                for r in rows:
                    o.append("| " + " | ".join(to_md(c) for c in r) + " |\n")
                o.append("\n")
            if m.get("note"):
                o.append(f"> {to_md(m['note'])}\n\n")
            if m["practice"]:
                o.append("**Práctica**\n")
                for it in m["practice"]:
                    o.append(f"- {to_md(it)}\n")
                o.append("\n")
            o.append("**Referencias:** " + " · ".join(ref_md(k, loc) for k, loc in m["refs"]) + "\n\n")
    o.append("---\n\n# Conceptos estadísticos del curso\n\nCada concepto con lo que se enseña de su teoría, el módulo donde se trata y la fuente teórica con sección.\n\n")
    for g, items in CONCEPTS:
        o.append(f"## {g}\n\n| Concepto | Qué se enseña | Módulo | Fuente teórica |\n|---|---|---|---|\n")
        for c, what, mod, refs in items:
            o.append(f"| {to_md(c)} | {to_md(what)} | {renum(mod)} | " + "; ".join(ref_md(k, loc) for k, loc in refs) + " |\n")
        o.append("\n")
    o.append("---\n\n# Bibliografía\n\nTodas las fuentes están en `docs/`. Entre corchetes, los módulos donde se usa cada una.\n\n")
    for g, items in BIB:
        o.append(f"## {g}\n\n")
        for k, short, full, f in items:
            full_md = re.sub(r"</?i>", "*", full).replace("<code>", "`").replace("</code>", "`")
            u = used.get(k, [])
            utxt = ", ".join(u) if u else "listado de conceptos"
            files = ", ".join(f"`{x.strip()}`" for x in f.split(";"))
            o.append(f"- **{short}.** {full_md} {files} [{utxt}]\n")
        o.append("\n")
    return "".join(o)

(ROOT / "temario_curso.html").write_text(build_html())
(ROOT / "temario_curso.md").write_text(build_md())
print("núcleo", core_hours, "con optativo", opt_hours)
