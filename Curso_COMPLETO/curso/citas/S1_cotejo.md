# Cotejo bibliográfico — S1 Fundamentos

Fecha: 2026-10-27. Alcance: versiones actuales M00–M04. Estados estrictos: **verificada** = pasaje/artefacto comprobado con el alcance indicado; **corregida** = atribución, localizador o registro ajustado frente a evidencia; **no verificable** = soporte insuficiente comprobado. Cuando un grupo de citas múltiples solo está parcialmente cotejado, el estado global es **no verificable** y se identifican por separado las partes verificadas. El inventario literal de ocurrencias, fichas, bibliografías y hashes está en `S1_inventario.md`. Prácticas M00 se conservan sin edición; no se tocó `curso/citas/inventario.md`.

## M00

| Ubicación | Clave/grupo | Estado | Evidencia y límite |
|---|---|---|---|
| Ficha y menciones curriculares | `prop_e` | no verificable | Documento curricular; no es fuente técnica ni se cotejó para afirmaciones estadísticas. |
| 30 | GUM B.2.19 | verificada | PDF local: error como resultado menos valor verdadero; `y−x` se declara convención del curso. |
| 36 | EN 14625 §8.2, tabla 1, nota | verificada | `pdftotext -f 20 -l 20`: “NOTE nmol/mol = ppb” en PDF 20, pie impreso 18. Solo equivalencia de unidades; no la explicación de fracción molar. |
| 60 | GUM C.2.19 | verificada | Define media aritmética; promedio particular es cálculo interno. |
| 76, 82, 155, 188, 233, 255, 295 | ISO/IEC 17025 §§7.5.1–7.5.2, 7.11.2, 7.11.6 | verificada | Cláusulas sobre registros, enmiendas, sistemas y comprobación de cálculos/transferencias. Convenciones analíticas docentes no se atribuyen a la norma. |
| 88–115, 192–213, 259–278 | Prácticas B/I/A | verificada | Contenido didáctico autorizado; datos simulados y registro R03 son internos al ejercicio. Se mantienen prácticas, soluciones y bloques; no se borraron ni reescribieron. |
| 298 | Script de cálculos | verificada | Recurso interno referido por el libreto; no es fuente bibliográfica. |

## M01

| Ubicación | Clave/grupo | Estado | Evidencia y límite |
|---|---|---|---|
| 18, 24, 54–58, 72, 100 | GUM-6 §§5.1–5.2, 5.6, 5.8, 6.1 | verificada | PDF local: mensurando/modelo y propósito; modelo explícito y adecuación. No avala cada simplificación fuera de la explicación acotada. |
| 24, 236–244 | GUM B.2.9 | verificada | B.2.9: “measurand — particular quantity subject to measurement”. |
| 24, 34–38, 158–159, 236, 243 | GUM-6 §5.1; VIM 2.3 | no verificable | GUM-6 §5.1 verifica la remisión a JCGM 200, 2.3; VIM primario no está en `docs/`, así que el grupo no es globalmente verificado. |
| 26, 40, 136, 146, 148, 162 | GUM B.2.19–B.2.20, B.2.23 | verificada | Definiciones cotejadas; signos `y−x`/`x−y` son convención del curso. |
| 60–72, 82–84, 152–156 | NISTIR 6963 §8; CFR50-D §§4.1, 4.5.2.5, 4.5.3.10 ec. 4 | verificada | Pasajes PDF localizados para relación/coeficiente y factores; omisiones operativas declaradas didácticas, no cálculo certificado. |
| 78, 92, 96, 100 | GUM §5.1.3; GUM-6 Anexo A, símbolo c; §5.8 | verificada | Definición de coeficiente de sensibilidad como derivada parcial; diferencias finitas/cálculos son propios, no derivada analítica. |
| 188–206, 232 | GUM §5.2.2; AX.2 | no verificable | GUM respalda propagación con covarianza; AX.2 es remisión interna, no se cotejó aquí su contenido. Grupo múltiple parcial. |
| 12, 130, 152, 241 | BIPM-K1 §1.1 / “Absorption cross-section for ozone”, p. 3 | verificada | Protocolo local: pasaje de sección eficaz y valor central declarados. No se extiende a contenido general del protocolo. |
| 156, 180 | Diferencia entre cocientes de sección eficaz y coeficientes | corregida | Los pares numéricos publicados producen cocientes distintos; la causa de esa diferencia no queda determinada en este cotejo. Se conserva la comparación numérica, sin atribuirla a redondeo ni a constantes de referencia. |
| 236–244 | Referencias M01 | corregida | BIPM-K1 p. 3 corresponde a página impresa según el documento; VIM primario ausente declarado expresamente. |

## M02

| Ubicación | Clave/grupo | Estado | Evidencia y límite |
|---|---|---|---|
| 14 | Ficha | corregida | Ficha distingue localizadores comprobados de los parciales y no verificados. |
| 32–44, 50–54, 200 | Hahs-Vaughn §§2.1–2.3, 3.2.2–3.3 | verificada | Extractos/PDF: tabulación, gráficos, cuantiles/caja, media/mediana y dispersión; estadísticos concretos son cálculos propios. |
| 56, 200 | GUM §4.2.3 ec. (5); Hahs-Vaughn §5.2 | no verificable | GUM respalda varianza de media bajo independencia; §5.2 es contexto de muestreo, no se comprobó como fuente de s/√n. Grupo parcialmente cotejado. |
| 42, 74, 205 | ASQ Apéndice C, CV | verificada | Inspección individual: PDF 605, pie impreso 572 y entrada coefficient of variation; PDF 598 no contiene la entrada. H-11 rechazado correctamente. |
| 82, 84, 86, 140, 156, 201 | Crowder §4.3 | no verificable | §4.3 se comprobó para EDA, valores atípicos/tendencias; no respalda agrupación diaria ni precisión/calibración. Alcance global parcial. |
| 106, 110, 140 | Crowder §4.3 | corregida | Se limitó/eliminó atribución excesiva; sin cambio de datos ni ejercicios. |
| 118, 134, 166, 180, 206 | NIST/SEMATECH MAD y definiciones generales | no verificable | MAD §1.3.5.6 comprobado externamente; atribuciones de error absoluto e influencia carecen de pasaje exacto comprobado. No presentar grupo entero como verificado. |
| 66, 203 | GUM §5.2.2 | verificada | Ley de propagación/combinación; identidad de muestra es álgebra propia. |
| 90, 202 | MMU §§3.1.1, 3.1.3 | verificada | PDF local: redondeo y cifras durante operaciones; resultado SRP no proviene de la fuente. |
| 128, 132, 204 | ISO 28037 §§5, 5.8 | no verificable | Se localizaron encabezados/forma OLS, pero no evidencia de pasaje suficiente para certificar todos los detalles atribuidos. |
| Referencias M02 | Hahs-Vaughn, AX.1, NIST web | corregida | Año 2020 comprobado en créditos; AX.1 es interna; recurso NIST declarado web externa. |

## M03

| Ubicación | Clave/grupo | Estado | Evidencia y límite |
|---|---|---|---|
| 18–74 | MMU §§3.2.1, 3.2.3–3.2.5.2 | verificada | PDF local sobre probabilidad/distribuciones; ejemplos numéricos hipotéticos propios. |
| 18, 50, 110, 348 | Hahs-Vaughn | no verificable | PDF local y temas/capítulos identificados; soporte de afirmaciones listadas no comprobado línea a línea. Año 2020 comprobado en créditos. |
| 76, 82 | GUM §4.3.3 | verificada | u=U/k en contexto de especificación/certificado; no generalizar sin factor aplicable. |
| 86–98, 108–110 | GUM §§4.2.3, 4.2.7, 5.2 | no verificable | Pasajes respaldan promedio/correlación en alcance señalado; serie, subperiodos y resúmenes son simulados/cálculos propios, por lo que grupo completo es parcial. |
| 106, 108, 266 | GUM F.1.1.3 | verificada | Apoyo cualitativo sobre influencias supuestamente aleatorias; no demuestra modelo ni medias del libreto. |
| 110 | GUM G.3.2–G.3.4 | verificada | G.3.2 trata t de Student; grados de libertad del ejemplo son modelo elemental propio. |
| 140–148, 182, 246, 288 | Crowder §§4.4.3, 7.2, 7.4.1 | verificada | Pasajes consultados para ajuste gráfico, esperanza/combinación y covarianza/correlación; cifras y aplicación propias. |
| 170, 174–180 | Hahs-Vaughn §9.1.1 | no verificable | §9.1.1, “Characteristics of the F Distribution”, sí respalda F; no se comprobó soporte para construcción de chi-cuadrado. La definición/derivación de chi-cuadrado se registra como del libreto, no atribuida a esa fuente. |
| 196, 252, 260, 319 | NIST/SEMATECH Autocorrelation | no verificable | La referencia/tema se identifican, pero el registro presente no conserva copia/pasaje web que permita verificarlo ahora. No confundir el estimador NIST con Pearson entre listas desplazadas ni respaldar cálculos propios. |
| 276, 318, 352 | GUM-S2 §3.20 nota 4; §3.21 nota 4 | verificada | PDF: problemas de definitud positiva/varianza negativa numérica y relación entre matrices de correlación/covarianza en alcance descrito; no cada regla docente. |
| Referencias M03 | AX.2, AX.3; NIST web | corregida | AX.2/AX.3 añadidas como referencias internas completas; NIST se describe como consulta web, no PDF local. |

## M04

| Ubicación | Clave/grupo | Estado | Evidencia y límite |
|---|---|---|---|
| 20–132, 270–276 | Hahs-Vaughn | no verificable | Capítulos/pasajes de inferencia identificados, pero no cada atribución se cotejó al nivel de afirmación. Welch §§7.3.1/7.5.3 y §7.1.3.2 son localizadores admisibles; este último no era incorrecto. |
| 138–164 | statsmodels/SciPy | verificada | Evidencia de revisión reporta ejecución de `calc/M04_ejemplos.py` con statsmodels 0.15.0 y contraste `scipy.stats.nct`; verifica esa ejecución concreta, no documentación completa. No se afirma nueva ejecución en esta continuidad. |
| 150 | G*Power, Hahs-Vaughn §6.5 | verificada | PDF completo: “Power Using G*Power”, p. impresa 215 y pasaje sobre potencia a priori/post hoc; libreto deja claro que es fuente libro. |
| 160, 164, 172–176 | GUM §4.3.2 nota; §E.4.3 ec. E.7 | verificada | Pasajes comprobados bajo normalidad/supuestos declarados; E.7 apoya u(s)≈s/√(2ν). |
| 184–186, 279 | Otto §2.2 | no verificable | No hay pasaje/página individual suficientemente documentado en este cotejo. |
| 188–224, 220, 258 | NIST Bonferroni; statsmodels `multipletests` | no verificable | NIST sí apoya intervalos simultáneos/cobertura conjunta; statsmodels documenta método Bonferroni y p corregidos. Citas múltiples y regla derivada no quedan globalmente verificadas; independencia es deducción por cota de unión. |
| 198–206 | Lakens 2017 | no verificable | Evidencia heredada de cotejo externo/PDF abierto afirma TOST/IC90, pero no conserva URL/pasaje/fecha verificables en el registro; no se eleva a verificada en este cotejo. Margen docente no es requisito del laboratorio. |
| 212–248 | Milton et al. 2006 | no verificable | Extracto local apoya chi-cuadrado/residuos en contexto GLS y gl m−n; alcance no universal, por tanto grupo de afirmaciones no es globalmente verificado. |
| Referencias M04 | AX.1, AX.7, bibliografía | corregida | AX son remisiones internas; bibliografía armonizada a alcances disponibles. |

## URLs y pasajes web registrados

| Fuente | URL | Pasaje / límite | Fecha | Estado |
|---|---|---|---|---|
| NIST/SEMATECH, Bonferroni's method | https://itl.nist.gov/div898/handbook/prc/section4/prc473.htm | Intervalos simultáneos/cobertura conjunta; no fórmula explícita de p ajustado ni independencia. | 2026-10-27 (fecha de actualización del cotejo; hora/fecha de acceso no archivada). | verificada |
| statsmodels, `multipletests` | https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html | `method='bonferroni'` y p-valores corregidos; no independencia. | No registrada. | verificada |
| NIST/SEMATECH, Autocorrelation | https://www.itl.nist.gov/div898/handbook/eda/section3/eda35c.htm | Autocorrelación temporal; no Pearson entre listas desplazadas ni cálculos propios. | Libreto dice consulta 2026-10-27, pero no se conserva captura/pasaje verificable. | no verificable |
| Lakens 2017 | https://doi.org/10.1177/1948550617697177 | TOST/IC90 según evidencia heredada; sin pasaje ni fecha de acceso archivados. | No registrada. | no verificable |

## Decisiones H-01–H-18 y continuidad

- H-01: prácticas M00 autorizadas se conservan; ningún borrado ni reescritura en esta continuidad.
- H-11 rechazado: comprobación directa ASQ PDF 605, impresa 572, entrada CV.
- H-18 aceptado: comprobación directa EN PDF 20, impresa 18, nota “nmol/mol = ppb”.
- H-05: Hahs-Vaughn §9.1.1 apoya características de F; construcción de chi-cuadrado no verificable como fuente externa y no se atribuye a §9.1.1.
- Se normalizaron estados ambiguos: no se usa “parcialmente verificada” como estado; los alcances parciales quedan explicados en evidencia y el estado de grupo múltiple es no verificable.
- No se alteraron libretos, prácticas ni cifras en esta continuidad. No se ejecutó ni se declara salida exitosa de una ejecución previa que alcanzó límite de tiempo.
- No se crearon commits; no se tocó `curso/citas/inventario.md`.
