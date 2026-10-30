# Guía del libreto: estilo, estructura y referencias

Esta guía es obligatoria para todos los agentes. Complementa [prop_e.md](../prop_e.md), que fija el contenido por nivel. Si hay conflicto, prop_e manda en el contenido y esta guía en la forma.

## 1. Qué es un libreto

El libreto es **lo que el instructor dice en clase**, en orden, de principio a fin. No es un libro de texto, ni apuntes, ni una lista de viñetas.

- Se escribe en **español**, en prosa hablada, dirigida a los operadores del SRP de CALAIRE («ustedes», «vamos a», «miren esta columna»). Frases cortas, ritmo oral, sin jerga innecesaria.
- Todo se narra: la motivación, la definición, la fórmula (se escribe y además se dice en palabras), el ejemplo resuelto y el cierre.

> **Fase actual: solo contenido.** Las prácticas, los ejercicios, sus soluciones, las evidencias evaluables, las rúbricas y el taller integrador se desarrollan en una fase posterior. En esta fase cada capítulo desarrolla la explicación narrada de todos los temas de prop_e, con **ejemplos ilustrativos** resueltos con números (forman parte de la explicación), y deja en el lugar de cada práctica de prop_e un marcador:
>
> > **[PRÁCTICA — fase de ejercicios]** <título breve de la práctica que fija prop_e para ese nivel>
>
> El marcador no se desarrolla: no lleva enunciado, datos, solución ni rúbrica.
- Las **acotaciones** indican lo que no se dice: qué se escribe en la pizarra, qué diapositiva se proyecta, cuándo se reparte material, cuándo se hace una pregunta y qué respuesta se espera. Van en bloque de cita con etiqueta en mayúsculas:

  > **[PIZARRA]** $u_c^2(y)=\sum_i c_i^2\,u^2(x_i)$
  >
  > **[PREGUNTA AL GRUPO]** ¿Qué pasa con esta suma si las dos entradas comparten el mismo patrón? — *Respuesta esperada:* aparece un término de covarianza.

  Etiquetas permitidas: `[PIZARRA]`, `[DIAPOSITIVA]`, `[MATERIAL]`, `[PREGUNTA AL GRUPO]`, `[PAUSA]`, `[EJEMPLO]`, `[PRÁCTICA — fase de ejercicios]` (solo como marcador), `[ERROR CRÍTICO]`, `[ESCALAMIENTO]`, `[TRANSICIÓN]`, `[NOTA AL INSTRUCTOR]`.
- No se usan viñetas para el contenido narrado. Las tablas se permiten para datos, presupuestos de incertidumbre, rúbricas y la ficha del capítulo.
- Nada de filosofar: cada concepto se presenta porque el caso lo necesita, y se aplica de inmediato.

## 2. Estructura de cada capítulo

```
# MXX. Título estadístico

## Ficha del capítulo
(tabla: competencia estadística, prerrequisitos, contenido por nivel, datos de los ejemplos con su
 rótulo de origen, anexos a los que remite, referencias clave)

## Nivel B — <subtítulo>
### Escena B1. <título>          (narración + acotaciones + ejemplo ilustrativo con números)
### Escena B2. ...
> [PRÁCTICA — fase de ejercicios] <título de la práctica B de prop_e>
### Señales de escalamiento      (cuándo el operador de B se detiene y consulta)

## Nivel I — lo que se añade
### Escena I1. ...
> [PRÁCTICA — fase de ejercicios] ...

## Nivel A — lo que se añade
### Escena A1. ...
> [PRÁCTICA — fase de ejercicios] ...

## Cierre del capítulo           (síntesis narrada por nivel y transición al capítulo siguiente)

## Referencias del capítulo      (lista completa; formato §5)
```

Los niveles son acumulativos (I comprende B; A comprende B e I). En la sección de un nivel solo se narra lo que ese nivel **añade**, y se indica al inicio qué se da por visto. Si prop_e no asigna contenido a un nivel en un módulo (por ejemplo, M13 es solo A), se dice expresamente en la ficha.

## 3. Contenido

- El contenido de cada nivel es el de prop_e §5 para ese módulo, sin quitar ni añadir temas. Si un tema parece necesitar un prerrequisito que no está, se anota en la bitácora; no se amplía el temario.
- Cada tema incluido en un nivel tiene explicación narrada y, cuando el tema es cuantitativo, al menos un ejemplo ilustrativo resuelto con números. Las prácticas, evidencias y rúbricas quedan para la fase de ejercicios (marcador de §1).
- Las deducciones no se hacen en clase: se remite al anexo correspondiente (§7) con una frase del tipo «la deducción está en el Anexo AX.4; aquí la usamos».
- Señales de escalamiento, errores críticos (como advertencias narradas) y exclusiones: según prop_e §2, §6 y §8.

## 4. Convenciones (prop_e §3)

- `x` referencia, `y` indicación, `e = y − x` error con signo; recta `y = a + b·x`; uso inverso `x̂ = (y − a)/b`; corrección aditiva `x̂ − y`.
- `u` estándar, `U = k·u` expandida; `k = t(0,975; ν_eff)` para un intervalo bilateral del 95 % con Student.
- `s_r` (estima `σ`, dentro del día) y `s_entre` (estima `τ`, efecto de día sin repetibilidad); `n` lecturas por día, `d` días.
- Unidades: nmol/mol. Coma decimal (0,975). Fórmulas en LaTeX (`$…$` en línea, `$$…$$` en bloque o dentro de `[PIZARRA]`), y siempre leídas en voz alta en la narración.
- Cada conjunto de datos lleva rótulo de origen: **propio** (archivo del laboratorio), **publicado** (fuente citada), **adaptado** (de una fuente, modificado; se dice qué se cambió) o **simulado** (generado; se dice cómo). Ningún resultado adaptado o simulado se atribuye a CALAIRE.

## 5. Referencias

Toda definición, fórmula, criterio, valor tabulado o afirmación técnica no trivial lleva referencia.

- **En la narración**, la referencia va entre corchetes justo después del concepto, con clave y ubicación: `[GUM 5.1.2]`, `[ISO 5725-3 §8]`, `[Crowder 2020 §9.3]`. Cuando sea natural, el instructor la nombra en voz alta («la GUM, en su apartado 4.3, dice…»).
- **Al final del capítulo**, «Referencias del capítulo» con la cita completa de cada clave usada (autor u organismo, título, edición/año, editorial o emisor) y el archivo en `docs/` si existe.
- **Verificación.** Antes de citar un numeral, se comprueba en el documento de `docs/` (por ejemplo, `pdftotext -f 20 -l 25 "docs/ARCHIVO.pdf" - | less`). El mapa de referencias por módulo de [temario_curso.md](../temario_curso.md) es un punto de partida, no una garantía.
- **Fuentes que no están en `docs/`** (VIM, JCGM 106, ILAC-G8, textos de control estadístico): se citan con su referencia completa y la marca «(no disponible en docs/)». Solo se cita un numeral si se conoce con seguridad; si no, se cita el documento sin numeral y se anota como pendiente en la bitácora.
- **Nunca** se inventa un numeral, página, tabla o ecuación.
- Citar prop_e solo justifica el alcance del curso; **no es referencia técnica**. Cada concepto, definición o fórmula se respalda con una fuente externa (VIM, GUM, ISO, textos de `docs/`).

### Claves bibliográficas

| Clave | Referencia | Archivo en `docs/` |
|---|---|---|
| VIM | JCGM 200:2012, *International vocabulary of metrology — Basic and general concepts and associated terms (VIM)*, 3.ª ed. | no disponible |
| GUM | JCGM 100:2008 (ISO/IEC Guide 98-3:2008), *Evaluation of measurement data — Guide to the expression of uncertainty in measurement* | `ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ … (GUM_1995) - libgen.li.pdf` |
| GUM-1 | JCGM GUM-1:2023, *Guide to the expression of uncertainty in measurement — Part 1: Introduction* | `JCGM_GUM-1.pdf` |
| GUM-6 | JCGM GUM-6:2020, *Part 6: Developing and using measurement models* | `JCGM_GUM_6_2020.pdf` |
| GUM-S1 | JCGM 101:2008, *Supplement 1 — Propagation of distributions using a Monte Carlo method* (y corrigendum) | `ISO_IEC Guide 98-3_2008 Suppl.1_2008 - libgen.li.pdf` |
| GUM-S2 | JCGM 102:2011, *Supplement 2 — Extension to any number of output quantities* | `ISO_IEC Guide 98-3_2008 Suppl.2_2011 - libgen.li.pdf` |
| JCGM 106 | JCGM 106:2012, *The role of measurement uncertainty in conformity assessment* | no disponible |
| ILAC-G8 | ILAC-G8:09/2019, *Guidelines on Decision Rules and Statements of Conformity* | no disponible |
| ISO 17025 | ISO/IEC 17025:2017, *General requirements for the competence of testing and calibration laboratories* | `BS EN ISO_IEC 17025_2017.pdf` |
| ISO 5725-1 … -6 | ISO 5725-1:1994 … ISO 5725-6:1994 (parte 5: 1998), *Accuracy (trueness and precision) of measurement methods and results*, con sus corrigenda | `ISO 5725-*.pdf` |
| ISO 28037 | ISO/TS 28037:2010, *Determination and use of straight-line calibration functions* | `ISO 28037.pdf` |
| ISO 6143 | ISO 6143:2001, *Gas analysis — Comparison methods for determining and checking the composition of calibration gas mixtures* | `ISO 6143 2001.pdf` |
| ISO 13964 | ISO 13964:1998, *Air quality — Determination of ozone in ambient air — Ultraviolet photometric method* | `Air quality_ Determination of ozone … ISO 13964.pdf` |
| EN 14625 | EN 14625:2012, *Ambient air — Standard method for the measurement of the concentration of ozone by ultraviolet photometry* | `BS EN 14625_2012.pdf` |
| BIPM-K1 | BIPM, *Protocol for the comparison BIPM.QM-K1* (J. Viallon) | `BIPM.QM-K1_2.protocol.pdf` |
| NISTIR 6963 | Paur, R. J. et al., *Standard Reference Photometer for the assay of ozone in calibration atmospheres*, NISTIR 6963, 2003 | `nistir6963.pdf` |
| SRP-SOP / SRP-QAPP | US EPA, *SRP Standard Operating Procedure* / *SRP Quality Assurance Project Plan* | `srp_sop.pdf`, `srp_qapp.pdf` |
| SRP6008 | NIST, especificación y certificado del SRP | `SRP6008_spec_cert.pdf` |
| EPA-TAD | US EPA, *Transfer Standards for Calibration of Air Monitoring Analyzers for Ozone — Technical Assistance Document*, 2023 | `o3_tad_508_20230906_final.pdf` |
| CFR58-A | 40 CFR Part 58, Appendix A | `Appendix A to Part 58_ Title 40 …pdf` |
| EPA-QAH | US EPA, *QA Handbook for Air Pollution Measurement Systems, Vol. II* | `USEPA - Quality Handbook.pdf` |
| Milton 2006 | Milton, M. J. T. et al., Metrologia (2006) — verificar autores, título y páginas en el PDF | `milton2006.pdf` |
| Crowder 2020 | *Introduction to Statistics in Metrology* — verificar autores y editorial en el PDF | `Introduction to Statistics in Metrology.pdf` (capítulos en `intro_stats_metro_c*.pdf`) |
| MMU | *Metrology and Measurement Uncertainty* — verificar autor y editorial | `Metrology and Measurement Uncertainty.pdf` (`metrology_measure_uncer_c*.pdf`) |
| Hahs-Vaughn | Hahs-Vaughn, D. L. y Lomax, R. G., *Statistical Concepts — A First Course* | `Statistical Concepts – A First Course.pdf` (`statistical_concepts_c*.pdf`) |
| ASQ | Wade, H. A. (ed.), *The ASQ Metrology Handbook* | `The ASQ Metrology Handbook.pdf` (`asq_metrological_handbook_c*.pdf`) |
| Deldossi 2009 | Deldossi, L. y Zappa, D., comparación ISO 5725 frente a GUM, 2009 | `2009 - Deldossi - ISO 5725 vs GUM comparison.pdf` |
| Brereton | Brereton, R. G., *Chemometrics: Data Driven Extraction for Science* | `Chemometrics _ data driven extraction for science.pdf` |
| Otto | Otto, M., *Chemometrics: Statistics and Computer Application in Analytical Chemistry* | `Chemometrics Statistics and Computer Application.pdf` |
| Mark-Workman | Mark, H. y Workman, J., *Chemometrics in Spectroscopy* | `chemometrics_spectroscopy_s*.pdf` |
| PHMU | *A Practical Handbook on Measurement Uncertainty* — verificar autor | `A Practical Handbook on Measurement Uncertainty_.pdf` |
| Daumont 1992 / Malicet 1995 | Artículos «Ozone UV spectroscopy I / II» | `Ozone UV spectroscopy …pdf` |
| Montgomery 2013 | Montgomery, D. C., *Introduction to Statistical Quality Control*, Wiley, 2013 (edición no verificada; título y año según Crowder 2020, PDF pp. 96 y 145). Contenido no cotejado. | no disponible |
| Montgomery DAE | Montgomery, D. C., *Design and Analysis of Experiments*, 9.ª ed., Wiley, 2017 (según la bibliografía de Crowder 2020; sin página verificada). Contenido no cotejado; no confundir con Montgomery 2013. | no disponible |
| Searle–Casella–McCulloch | Searle, S. R.; Casella, G.; McCulloch, C. E., *Variance Components*. Edición y editorial pendientes de cotejo. | no disponible |
| Efron–Tibshirani 1993 | Efron, B. y Tibshirani, R. J., *An Introduction to the Bootstrap*. Editorial y año pendientes de verificación; sin numeral. | no disponible |

Para control estadístico (EWMA, CUSUM, cartas I-MR) y riesgo de decisión pueden citarse fuentes externas reconocidas (por ejemplo, Montgomery, *Introduction to Statistical Quality Control*; NIST/SEMATECH *e-Handbook of Statistical Methods*), marcadas «(no disponible en docs/)», sin numerales no verificados.

## 6. Datos disponibles para los ejemplos

| Datos | Ubicación | Rótulo |
|---|---|---|
| Calibración del Level 2 (Thermo 49C S/N 59756-324) contra el SRP 55; 12 puntos × 8 lecturas × 6 días | `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm` | propio |
| Estudio R&R 2022–2023 (hojas por nivel) | `docs/Resultados R&r_2022 2023 (1).xlsx` | propio |
| Caso B (SRP 36/SRP 7, adaptación GGMR) | `casos_taller/caso_B_comparacion_clave.md`, `datos_caso_B.csv`, `calc_casos.py` | publicado y adaptado |
| Caso C (historial del Level 2, series docentes) | `casos_taller/caso_C_historial_level2.md`, `datos_caso_C1.csv`, `datos_caso_C2.csv` | adaptado / simulado |

Los defectos de los archivos reales no se convierten en actividades de clase (prop_e §1.6): se usan para preparar ejemplos limpios. Para leer los `.xlsx`/`.xlsm` y calcular, usar `curso/.venv/bin/python` (numpy, scipy, pandas, openpyxl, statsmodels). Los scripts de cálculo se guardan en `curso/<sección>/calc/` y cada número que aparece en el libreto debe poder reproducirse con ellos.

## 7. Anexos de deducciones (identificadores fijos)

| Id | Contenido |
|---|---|
| AX.1 | Divisor `n − 1` y grados de libertad de `s` |
| AX.2 | Varianza de combinaciones lineales y ley de propagación con covarianza |
| AX.3 | Varianza de las distribuciones rectangular y triangular (`h/√3`, `h/√6`, `δ/√12`) |
| AX.4 | Cuadrados medios esperados del ANOVA de un factor aleatorio y `u²_prec(ē) = s²_entre/d + s²_r/(d·n)` |
| AX.5 | Ecuaciones normales de OLS y WLS; covarianza de `a` y `b` |
| AX.6 | Incertidumbre de la predicción inversa por linealización |
| AX.7 | Fórmula de Welch–Satterthwaite y sus condiciones |
| AX.8 | Formulación matricial de GGMR con `V_xy = 0` y chi-cuadrado de consistencia |
| AX.9 | Varianza de una diferencia con patrón compartido; grado de equivalencia frente a referencia común |
| AX.10 | Probabilidades de falsa aceptación y falso rechazo |
| AX.11 | Límites de confianza de indicadores de precisión y sesgo (chi-cuadrado y t) |
| AX.12 | Varianza del estadístico EWMA; longitud media de corrida de EWMA y CUSUM |
| AX.13 | Fundamento del método de Monte Carlo (GUM-S1) y control del número de ensayos |

## 8. Archivos por capítulo y por sección

En `curso/<sección>/`:

- `MXX_libreto.md` — el libreto.
- `MXX_bitacora_luna.md` — bitácora del desarrollador: **Plan** (antes de escribir: alcance por nivel tomado de prop_e, escenas, datos, referencias a verificar), **Ejecución** (qué se escribió, cálculos y scripts, referencias verificadas y cómo, pendientes) y **Correcciones** (tabla hallazgo → acción → ubicación, para cada hallazgo de la revisión).
- `MXX_revision_haiku.md` — revisión de redacción y errores.
- `SX_revision_sol.md` — plan de revisión, hallazgos por capítulo, correcciones aplicadas y, al final, correcciones tras la revisión de Opus.
- `SX_00_indice.md` — índice de la sección entregada.
- `SX_revision_opus.md` — revisión de la sección entregada.
- `calc/` — scripts de cálculo.
