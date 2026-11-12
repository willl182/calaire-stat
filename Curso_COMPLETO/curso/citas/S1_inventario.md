# Inventario de citas — S1 Fundamentos

Actualizado: 2026-10-27. Alcance: versiones actuales M00–M04. Los estados permitidos son **verificada**, **corregida** y **no verificable**. `verificada` indica pasaje concreto cotejado con el alcance declarado; `corregida` indica registro/localizador/atribución ajustado frente a evidencia; `no verificable` indica evidencia insuficiente. Cotejo por afirmación y límites: `S1_cotejo.md`. No se editó `curso/citas/inventario.md`.

## Ocurrencias literales

La fuente literal única de ocurrencias es [S1_ocurrencias.tsv](S1_ocurrencias.tsv), regenerable desde la raíz del repositorio con `python -I curso/citas/_extrae_s1.py`. Contiene archivo, línea actual y texto literal íntegro de las 184 ocurrencias entre corchetes detectadas en M00–M04; no se mantiene una tabla parcial paralela. Las líneas y huellas corresponden a los bytes actuales indicados más abajo. Claves como `prop_e` y `AX` son curriculares/internas, no referencias externas. Los contenidos de ficha y bibliografía final se registran en las secciones siguientes.

## Fichas, referencias finales y recursos inventariados

| Archivo / tramo | Familia o recurso | Clave canónica | Grupo de cotejo | Estado |
|---|---|---|---|---|
| M00 ficha y referencias finales | `prop_e`; GUM; EN 14625; ISO 17025; script y prácticas | varias | M00 | verificada / no verificable según alcance; prácticas y script no son citas |
| M01 ficha y referencias finales | VIM; GUM/GUM-6; NISTIR 6963; CFR50-D; BIPM-K1; AX.2; `prop_e` | varias | M01 | verificada / corregida / no verificable por fuente, según `S1_cotejo.md` |
| M02 ficha y referencias finales | Hahs-Vaughn; Crowder; GUM; ASQ; MMU; NIST/SEMATECH; ISO 28037; AX.1 | varias | M02 | verificada / corregida / no verificable por afirmación |
| M03 ficha y referencias finales | MMU; Hahs-Vaughn; GUM/GUM-S2; Crowder; NIST/SEMATECH; AX.2/AX.3 | varias | M03 | verificada / corregida / no verificable por afirmación |
| M04 ficha y referencias finales | Hahs-Vaughn; Otto; GUM; NIST/SEMATECH; statsmodels; Lakens; Milton; AX.1/AX.7 | varias | M04 | verificada / corregida / no verificable por afirmación |

## Catálogo normalizado de referencias

| Clave | Referencia y disponibilidad | Estado general |
|---|---|---|
| GUM | JCGM 100:2008, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement* (ISO/IEC Guide 98-3:2008), PDF en `docs/`. | Verificada por pasajes indicados, no todas las aplicaciones. |
| GUM-6 | JCGM GUM-6:2020, *Guide to the expression of uncertainty in measurement — Part 6: Developing and using measurement models*, `docs/JCGM_GUM_6_2020.pdf`. | Verificada por pasajes citados. |
| GUM-S2 | JCGM 102:2011, *Evaluation of measurement data — Supplement 2 to the GUM*, PDF en `docs/`. | Verificada §§3.20 nota 4 y 3.21 nota 4. |
| VIM | JCGM 200:2012, *International vocabulary of metrology*, 3.ª ed.; no está en `docs/`. | No verificable localmente; remisión indirecta por GUM-6 §5.1. |
| ISO 17025 | BS EN ISO/IEC 17025:2017, `docs/BS EN ISO_IEC 17025_2017.pdf`. | Verificada en cláusulas citadas, con límites. |
| EN 14625 | BS EN 14625:2012, `docs/BS EN 14625_2012.pdf`. | Verificada equivalencia de unidades, PDF 20 / impresa 18. |
| CFR50-D | Electronic Code of Federal Regulations, 40 CFR Part 50, Appendix D, PDF fechado 2026-10-16. | Verificada en secciones especificadas. |
| NISTIR 6963 | Paur et al., *Standard Reference Photometer for the Assay of Ozone in Calibration Atmospheres*, NISTIR 6963 (2003), `docs/nistir6963.pdf`. | Verificada §8 en alcance citado. |
| BIPM-K1 | BIPM, *Protocol for BIPM.QM-K1, On-demand Key Comparison of Ozone at ambient level*, v2.1 (2025), `docs/BIPM.QM-K1_2.protocol.pdf`. | Verificada sección eficaz indicada. |
| Hahs-Vaughn | Hahs-Vaughn y Lomax, *Statistical Concepts: A First Course*, 4.ª ed., Routledge, 2020; PDF/extractos en `docs/`. | No verificable como grupo global; pasajes delimitados sí verificados, incluido F §9.1.1; construcción de chi-cuadrado no verificada. |
| Crowder 2020 | Crowder et al., *Introduction to Statistics in Metrology*, Springer, 2020; PDFs/extractos en `docs/`. | No verificable como grupo global; §4.3 apoya cualitativamente análisis exploratorio, no agrupación diaria, precisión ni calibración. |
| MMU | Novellino do Rosario y Mendes, *Metrology and Measurement Uncertainty: Concepts and Applications*, Springer, 2025, PDF en `docs/`. | No verificable como grupo global; §3.2.5.2 (distribución triangular) verificada, otras afirmaciones del grupo no comprobadas aquí. |
| ASQ | Wade (ed.), *The ASQ Metrology Handbook*, 3.ª ed., 2022, PDF en `docs/`. | Verificada: PDF 605, impresa 572, entrada CV. |
| NIST/SEMATECH | *e-Handbook of Statistical Methods*, recursos web. | Solo pasajes delimitados; fuentes y fechas/URLs en cotejo; varias atribuciones no verificables. |
| ISO 28037 | ISO/TS 28037:2010, `docs/ISO 28037.pdf`. | No verificable como grupo global; se localizaron encabezados/forma OLS, sin soporte suficiente para todos los detalles atribuidos. |
| Otto | *Chemometrics: Statistics and Computer Application in Analytical Chemistry*, 3.ª ed. (2017), `docs/Chemometrics Statistics and Computer Application.pdf`. | No verificable en detalle §2.2/tablas según evidencia documentada. |
| Lakens 2017 | Lakens, “Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses”, *Social Psychological and Personality Science* 8(4), 355–362 (2017). | No verificable: evidencia de TOST/IC90 sin pasaje/fecha archivados; el margen docente no es requisito del laboratorio. |
| Milton et al. 2006 | “Implementation of a generalized least-squares method…”, *Metrologia* 43, S291–S298, `docs/milton2006.pdf`. | Parcialmente verificada en contexto GLS. |
| statsmodels | `statsmodels.stats.multitest.multipletests`, documentación web y clases de potencia usadas en M04. | Método/resultados documentados; ejecución local solo según alcance descrito. |
| prop_e | *Propuesta E*, `prop_e.md`. | Curricular, no soporte técnico. |
| AX.1–AX.3, AX.7 | Anexos internos del curso. | Remisiones internas, cotejables solo como artefactos del curso. |

## URLs/pasajes web

| Fuente | URL exacta | Pasaje/alcance | Consulta | Estado |
|---|---|---|---|---|
| NIST/SEMATECH Autocorrelation | https://www.itl.nist.gov/div898/handbook/eda/section3/eda35c.htm | Define/describe autocorrelación temporal; no respalda que Pearson entre dos listas desplazadas sea el estimador de NIST ni los cálculos propios. | 2026-10-27, fecha registrada en libreto; evidencia local de página no archivada en este cotejo. | no verificable como evidencia web preservada; afirmación acotada en libreto |
| NIST/SEMATECH Bonferroni | https://itl.nist.gov/div898/handbook/prc/section4/prc473.htm | Intervalos simultáneos/cobertura conjunta; no la fórmula de p corregida ni independencia. | 2026-10-27, según fecha de actualización del cotejo; fecha específica no registrada en libreto. | verificada con límite |
| Lakens 2017 | https://doi.org/10.1177/1948550617697177 | TOST e interpretación mediante IC90; no justifica margen didáctico como requisito CALAIRE. | Fecha exacta no registrada en las versiones actuales consultadas. | verificada con límite; pasaje web no preservado aquí |
| statsmodels | https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html | Método Bonferroni y salida de p-valores corregidos. | Fecha exacta no registrada. | verificada con límite |

## Huellas de las versiones cotejadas

SHA-256 calculado sobre bytes de los libretos actuales el 2026-10-27; una modificación posterior invalida la correspondencia con este inventario hasta repetir el cotejo.

| Archivo | SHA-256 |
|---|---|
| `curso/S1_fundamentos/M00_libreto.md` | `4ca1223bf87281288ac0b9961cc826e929af7a2de33159fe373302d1a70ebefc` |
| `curso/S1_fundamentos/M01_libreto.md` | `58b8e1211bc146cfe9a3eedac8662fff2bbe29a64d39126697362fbf72b8f25c` |
| `curso/S1_fundamentos/M02_libreto.md` | `c2f3104bf7cd65a22f539d694b40ed24de88040c1943f4a686ddba783c07de71` |
| `curso/S1_fundamentos/M03_libreto.md` | `ab775192a7efcbc7765d218c73e2f9aec364e80d3760b30f1385d97910c33e0a` |
| `curso/S1_fundamentos/M04_libreto.md` | `63d29724a55b0fbb3f609216934c80b124c6fb89c266fa96f80fc92156bc0be6` |

## Cobertura y límites

La extracción reportó 184 ocurrencias entre corchetes. Las 184 filas literales completas están publicadas en [S1_ocurrencias.tsv](S1_ocurrencias.tsv), con archivo, línea y cita literal; se reproducen con `python -I curso/citas/_extrae_s1.py`. El supervisor publicó este artefacto que la ejecución de luna había dejado solo en `/tmp/`; la tabla temática precedente agrupa el soporte y no sustituye el listado literal completo. No se modificaron prácticas M00 ni el catálogo común `inventario.md`. H-11 se rechaza (ASQ PDF 605 / impresa 572) y H-18 se acepta (EN PDF 20 / impresa 18) según inspección directa documentada en `S1_decisiones_luna.md`. Para chi-cuadrado M03, la construcción no se atribuye a Hahs-Vaughn §9.1.1: soporte externo de construcción no verificable; el apartado respalda F.
