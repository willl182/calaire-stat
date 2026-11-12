# S1. Revisión de contenido y entrega — Sol

Fecha: 25 de octubre de 2026. Alcance de edición: exclusivamente `curso/S1_fundamentos/`. Fase: solo contenido; no acredita preparación de prácticas ni autorización para impartir.

## Nota del supervisor

Supervisor: claude-sol (gpt-6.1-sol). Reanudación: 2026-10-26, 05:27:40 −05:00 (hora local obtenida con `date -Is`). Se conserva íntegro el plan y la nota del orquestador. Las ediciones interrumpidas son candidatas, no resultados previamente aprobados.

Supervisor actual: Opus 5.5 con esfuerzo bajo, en sustitución de claude-sol por cuota agotada. Reanudación: 2026-10-26T05:41:21−05:00. Conserva plan, registros previos y nota del orquestador; añade decisiones de M03/M04 (C, D2 y R3 de `auditoria_respaldo_20261026_053907/`) y estado de entrega.

Reanudación tras revisión Opus: 2026-10-26. Supervisor: claude-sol (gpt-6.1-sol). Las notas anteriores se conservan como antecedentes; la decisión vigente se registra en «Correcciones tras la revisión Opus» y «Estado de entrega».

## Plan de revisión

Plan registrado antes de revisar los capítulos. Se han leído íntegramente `curso/00_plan_maestro.md`, `curso/guia_libreto.md`, `prop_e.md` y `revision_final_prop_e.md`.

1. Leer, en orden M00 → M04, cada libreto, bitácora y revisión Haiku, sin dar por verificados sus dictámenes. Construir una correspondencia entre todos los contenidos B/I/A de prop_e §5 y las escenas; comprobar niveles acumulativos y exclusiones de §6.
2. Revisar corrección estadística y metrológica, notación, supuestos, unidad de repetición, escala, signo, cobertura, errores críticos y escalamiento. Distinguir ejemplos docentes resueltos de prácticas: conservar exactamente un marcador por práctica curricular y no desarrollar ejercicios, soluciones ni rúbricas.
3. Leer y ejecutar los cinco scripts con `curso/.venv/bin/python`, sin generar archivos fuera de S1. Recalcular los valores clave con una segunda implementación o identidades independientes; comprobar correspondencia entre resultados y narración. Incorporar comprobaciones reproducibles en `calc/` cuando sea necesario.
4. Verificar las referencias técnicas y sus numerales mediante `pdftotext` sobre los PDF de `docs/`; guardar la evidencia de verificación dentro de S1. No usar prop_e como respaldo técnico. Para fuentes ausentes, identificar expresamente esa condición y no inventar numerales.
5. Revisar el formato hablado, acotaciones, lectura de fórmulas, ejemplos por tema cuantitativo, rótulos de origen, transiciones, prerrequisitos y referencias AX; eliminar duplicaciones innecesarias sin suprimir la recapitulación acumulativa.
6. Registrar hallazgos con id S-…, capítulo, ubicación, severidad, problema y corrección. Aplicar las correcciones personalmente; conservar las bitácoras y revisiones previas como antecedentes, sin reescribirlas como si fueran esta revisión.
7. Crear el índice de entrega con escenas por nivel, los quince marcadores pendientes, datos y rótulos, anexos, estado y pendientes. Cerrar con pruebas ejecutadas, límites de la verificación y estado de entrega; no declarar listo para impartir el curso.

Severidad: crítica (resultado o decisión inválidos), alta (error técnico, referencia equivocada o contenido curricular ausente), media (ambigüedad de supuestos, reproducibilidad o forma), baja (claridad editorial). No se modificarán archivos externos a S1.

## Hallazgos por capítulo

Las dos interrupciones dejaron cambios sin dictamen. Esta reanudación distingue la propuesta anterior de su verificación actual. `Cxx` identifica la primera auditoría; `D2-xx` identifica el bloque global número xx, contando cada encabezado `@@` de `auditoria_interrupcion_sol_2/cambios_sol.diff` desde el principio. La ubicación usa escena y encabezado para sobrevivir a cambios de líneas. Severidad describe el defecto que motivó la corrección, no un defecto necesariamente abierto.

### M00 — estructura y cálculo reproducible

| Hallazgo | Candidata | Ubicación | Severidad | Problema y decisión técnica |
|---|---|---|---|---|
| S-001 | C01 | Introducción B, definición de error | alta | prop_e solo justifica convención curricular. **Conservada**: GUM B.2.19 define el error y su nota 1 admite valor convencional de referencia cuando no se conoce el verdadero. |
| S-002 | C02 | Introducción B, unidades | alta | Equivalencia nmol/mol–ppb correcta, pero C02 inventariaba tabla 2. **Ajustada**: EN 14625 §8.2, tabla 1, nota, contiene la equivalencia; tabla 2 no. |
| S-003 | C03 | Marcador B | media | Marcador abreviado omitía pareja desplazada, faltante y trazabilidad. **Conservada**: restaura práctica completa sin desarrollarla. |
| S-004 | C04 | I2, pizarra de tabla larga | media | `lectura` designaba índice y concentración. **Conservada**: magnitud `y (nmol/mol)`, índice separado. |
| S-005 | C05 | I2, narración ancho/largo | media | Colisión de nombre con índice de lectura. **Conservada**: `y` contiene indicación; ciclo identifica evento. |
| S-006 | C06 | Referencias del capítulo | alta | Faltaban entradas de GUM/EN para las citas técnicas. **Ajustada**: conservar entradas, corregir EN a tabla 1 e incorporar GUM C.2.19. |
| S-007 | C07 | calc/M00_ejemplos.py, contraste Calc | media | Criterio numérico solo se imprimía. **Conservada**: aserciones de longitud y tolerancia detectan discrepancias; ejecución real satisfactoria. |
| S-028 | D2-02 | B1, promedio 0,425 | media | Media respaldada solo por alcance curricular. **Conservada**: GUM C.2.19 respalda media aritmética; cálculo Decimal independiente confirma 0,425 nmol/mol. No se interpreta como precisión del instrumento. |
| S-029 | D2-03 | I2, ejemplo y script | media | Enumeración aún usaba lectura como magnitud y no documentaba salida explícita del faltante. **Conservada**: `y`, lectura oral, tres indicaciones y estado separado con clave; script verifica 3+1=4 celdas. |
| S-030 | D2-01 | Introducción B, unidades | alta | Numeral falso de C02. **Conservada**: tabla 1 verificada con pdftotext; complementa S-002. |
| S-031 | D2-04 | Referencias del capítulo | alta | Bibliografía mantenía tabla falsa y no registraba C.2.19. **Conservada**: referencias sincronizadas con narración y PDF, sin ampliar alcance. |

Hallazgo adicional de esta reanudación:

| Hallazgo | Origen | Ubicación | Severidad | Problema y corrección |
|---|---|---|---|---|
| S-100 | R3-01 | M00 I2, criterio de validación | media | Tras conservar el faltante, «número de registros resultantes» podía incluir también registros sin indicación y contradecir el conteo 3+1. **Corregida**: comparar valores no faltantes solo con registros que contienen indicación y comprobar aparte las claves/estados faltantes. No cambia ninguna cifra ni requiere cambiar el script. |

Verificación directa M00: lectura íntegra de libreto, bitácora, revisión Haiku y scripts; cotejo curricular B/I/A completo. Tablas largas, faltantes y exclusiones se presentan como convenciones del análisis, no como mandatos textuales de ISO 17025. No hay temas excluidos ni deducciones nuevas; tres marcadores, sin desarrollo de prácticas.

### M01 y M02 — modelo, escala y respuesta

| Hallazgo | Candidata | Capítulo y ubicación | Severidad | Problema y decisión técnica |
|---|---|---|---|---|
| S-008 | C08 | M01, ficha | media | No constaba prerrequisito real de parejas/unidades. **Conservada**: M00 prepara esas entradas; no amplía temario. |
| S-009 | C09 | M02 B4, CV | alta | Cita sin localización comprobada. **Conservada**: ASQ, apéndice C, entrada coefficient of variation, p. 572 (PDF 605), verificada. |
| S-012 | C12 | M01 B2, trayecto óptico | alta | Entradas simplificadas podían confundirse con configuración real del SRP. **Conservada**: longitud y transmitancia corresponden a un trayecto hipotético, no a combinación de canales reales. |
| S-013 | C13 | M02 B4, parejas | alta | Ejemplo anterior mezclaba niveles cuando M2-B exige un nivel durante varios días. **Conservada**: seis parejas de tres días en nivel nominal 200; errores preservados. |
| S-016 | C16 | M02 B4, dispersión de y | alta | 154,27 pertenecía al conjunto anterior. **Conservada**: desviación muestral actual 0,240138849 nmol/mol, comprobada independientemente. |
| S-019 | C19 | M01 I1, error y error relativo | alta | prop_e usado como respaldo técnico. **Conservada**: GUM B.2.19–B.2.20 respalda definiciones y denominador; prop_e queda como alcance. |
| S-020 | C20 | M02 B4, interpretación | alta | La diferencia entre dispersiones no constituye atribución causal completa a la referencia. **Conservada**: se evita descomposición injustificada; referencia y error covarían en el conjunto. |
| S-023 | C23 | M01, marcador B | media | Marcador abreviado no explicitaba las tres concentraciones ni signo/cambio relativo. **Conservada**: práctica curricular completa, sin desarrollo. |
| S-024 | C24 | M01 A1, párrafo eliminado | baja | Repetía cancelación ya explicada con las mismas cifras. **Conservado el borrado**: permanece explicación suficiente; D2-08 incorpora caso distinto de cancelación parcial. |
| S-025 | C25 | M02 B4, diapositiva | alta | Arrastre de s(y)=154,27 tras cambio de datos. **Conservada**: s(y)=0,240 nmol/mol coherente con C13/C16. |
| S-032 | D2-05 | M01, ficha/origen de 1,1329 | alta | Valor sin fuente ni unidad confirmadas. **Conservada**: BIPM-K1 p. 3 documenta 1,1329(35)×10⁻¹⁷ cm²/molécula; se usa valor central sin propagar incertidumbre ni enseñar protocolo. |
| S-033 | D2-06 | M01 B3, conversión | media | ppb y nmol/mol no ilustraban un factor de conversión numérico distinto. **Conservada**: contraste ppm–nmol/mol sí exige conversión. |
| S-034 | D2-07 | M01 I1, cocientes y reescalamiento | alta | Unidades pendientes, corrección confundida con ajuste y pregunta ambigua sobre qué valor cambia. **Conservada**: unidades documentadas, corrección separada de ajuste físico y escenarios solo y/ambos explícitos. Resultados +6,73477 y +1,31677 nmol/mol comprobados; se conserva también el marcador I con el par de coeficientes declarado. |
| S-035 | D2-08 | M01 A1, cancelación parcial | media | Condición de igual sensibilidad quedaba solo verbal. **Conservada**: sensibilidades 1 y 0,8 dejan cambio residual 0,2 por unidad de entrada común; no se interpreta como incertidumbre. |
| S-036 | D2-09 | M01, marcador A | media | Título genérico. **Conservada**: identifica contribuciones canceladas y persistentes como pide M1-A. |
| S-037 | D2-10 | M01, bibliografía | alta | Nuevas afirmaciones requerían fuentes completas. **Conservada**: GUM B.2.19–20 y BIPM-K1, versión 2.1, 09-10-2025, p. 3, verificados. |
| S-038 | D2-11 | M02, ficha/referencias clave | media | Ficha seguía diciendo CV sin numeral. **Conservada**, con ajuste adicional S-065 para MMU; ASQ p. 572 correcto. |
| S-039 | D2-12 | M02 B2, histograma/caja | media | Bordes no explícitos y caja sin convención numérica. **Conservada**: intervalos coherentes con numpy.histogram, conteos 2/3/3; bigotes mínimo–máximo declarados y admitidos por Hahs-Vaughn §2.3.4. |
| S-040 | D2-13 | M02, marcador B | media | Título insuficiente respecto de M2-B. **Conservada**: un nivel, varios días, referencia variable y negativos del cero, sin ejercicio. |
| S-041 | D2-14 | M02 I2, recta descriptiva | media | Enseñar ajuste aquí adelantaba M07. **Conservada**: recta entregada ya calculada; ISO 28037 §5.8 respalda preparación docente. Parámetros comprobados. |
| S-042 | D2-15 | M02 A1, error con signo | alta | Numeral VIM no contrastable en docs/. **Conservada**: GUM B.2.19 disponible respalda signo y definición. |
| S-043 | D2-16 | M02 A1, agregación | media | Efecto de tamaños desiguales quedaba sin ejemplo. **Conservada**: media de grupos cero frente a media de seis lecturas +0,133333 nmol/mol; conjunto distinto declarado, no exclusión de datos reales. |
| S-044 | D2-17 | M02, marcador A | media | Título no identificaba práctica de sesgos opuestos R&R. **Conservada**: restitución curricular sin desarrollo. |
| S-045 | D2-18 | M02, bibliografía | alta | Archivos parciales no contenían todos los pasajes; CV pendiente y VIM no cotejado. **Conservada**, con ajuste S-065: libro completo Hahs-Vaughn, GUM y ASQ localizados; MMU incluye §3.1.3. |
| S-065 | R3-03, R3-04, R3-05 | M02 B5, ficha y bibliografía | alta | Regla de redondear al final está en MMU §3.1.3, no solo §3.1.1. **Corregida**: conservar §3.1.1 para redondeo de un número y añadir §3.1.3 para operaciones. |
| S-066 | R3-02 | M01, cierre | media | «Corregir físicamente» volvía a confundir corrección y ajuste. **Corregida**: cambio de escala no constituye automáticamente corrección individual ni ajuste físico. |
| S-067 | Reanudación actual | calc/, salidas M01/M02 | alta | Salidas antiguas no correspondían a scripts/libretos actuales; M02 aún mostraba 154,266493. **Corregida**: regeneradas ambas salidas; ahora s(y)=0,240139 y M01 incluye ambos reescalamientos/cancelación parcial. |

Verificación M01/M02: extracción nueva con pdftotext de diez PDF, ejecución de ambos scripts con `curso/.venv/bin/python -I`, aserciones, contraste Decimal/statistics y compilación en memoria satisfactorios. Evidencia: `calc/verificacion_M01_M02_personal/pruebas.txt` y extractos del mismo directorio. Auxiliares `referencias_12/` preservados como históricos, no como pruebas nuevas. VIM y NIST/SEMATECH ausentes de docs/: citas sin numeral, limitación explícita.

### M03 y M04 — probabilidad, dependencia e inferencia

`R3-xx` identifica el bloque xx de `auditoria_respaldo_20261026_053907/cambios.diff` (tercera interrupción, 05:26–05:39). Los bloques R3-01 a R3-05 (M00–M02) corresponden a S-100, S-066 y S-065 ya registrados arriba.

| Hallazgo | Candidata | Capítulo y ubicación | Severidad | Problema y decisión técnica |
|---|---|---|---|---|
| S-010 | C10 | M03, ficha | alta | Resolución 0,1 nmol/mol atribuida a «propuesta B» sin fuente técnica del 49C. **Conservada**: se rotula como entrada hipotética simulada, no especificación. |
| S-011 | C11 | M04, citas | media | Clave «Statistical Concepts» distinta de la usada en M02/M03. **Conservada**: clave uniforme Hahs-Vaughn en la sección. |
| S-014 | C14 | M03 B1, axiomas | alta | «Cero representa un evento imposible» es falso en continuas. **Conservada**: P=0 no implica imposibilidad. |
| S-015 | C15 | M04 B1, ejemplo | alta | Unidad independiente y supuestos no declarados. **Conservada**: una pareja por jornada, ocho jornadas, un nivel, independencia y normalidad declaradas. |
| S-017 | C17 | M03 B1, variable aleatoria | media | Binomial adelantada sin presentar antes la variable de un ciclo. **Conservada**: Bernoulli de un ciclo P(X=0)=0,9, P(X=1)=0,1 (script reproduce). |
| S-018 | C18 | M04 I1, pareadas | media | Símbolo $d$ colisionaba con índice de día de M03. **Conservada**: diferencias $\Delta_i$. |
| S-021 | C21 | M03 B2, rectangular | alta | Igual que S-010. **Conservada**: resolución supuesta, sin atribución. h=0,05; u=0,0289 verificado. |
| S-022 | C22 | M04 I1, Welch | media | Fórmula de ν remitida solo a AX.7. **Conservada**: fórmula operativa en pizarra; derivación sigue en AX.7. ν=10,927 reproducido. |
| S-026 | C26 | M03 B2, procedencia | media | Igual que S-010. **Conservada**. |
| S-027 | C27 | M04, bibliografía | alta | §7.5.3 no coincide con encabezado del cuerpo. **Conservada**: §7.5.2 (cuerpo del PDF; el índice dice 7.5.3, aclarado en bibliografía). |
| S-046 | D2-19 | M03, ficha | media | Claves GUM-1/GUM-6 sin numeral. **Conservada**: GUM y GUM-S2 con numerales verificados. |
| S-047 | D2-20 | M03 B2, U/k | alta | prop_e como respaldo técnico de u=U/k. **Conservada**: GUM §4.3.3 y §6.2.1 (verificados con pdftotext). |
| S-048 | D2-21 | M03 B3, promedio/común y SE | alta | MMU sin numeral. **Conservada**: GUM §4.2.3 ec. (5), §4.2.7, §5.2. |
| S-049 | D2-22 | M03 I2, F | alta | Definición de F omitía independencia de los χ². **Conservada**. |
| S-050 | D2-23 | M03 I3, modelo de dos escalas | media | Supuestos de independencia de efectos no declarados. **Conservada**. |
| S-051 | D2-24 | M03 A1, $c^TVc$ | alta | Igualdad presentada como exacta en modelo no lineal. **Conservada**: aproximación, exacta si lineal. |
| S-052 | D2-25 | M03 A2, autocorrelación | alta | Ejemplo sin datos ni cálculo. **Conservada**: serie determinista, Pearson de listas desplazadas = 0,5 (reproducido); GUM-S2 §3.20–3.21 para semidefinición. |
| S-053 | D2-26 | M03 A2, V desde R | media | Faltaba ejemplo numérico de construir V y usar covarianzas de enlace. **Conservada**: V, u(x3−x1)=0,40 reproducidos; matriz inválida con autovalor −0,2. |
| S-054 | D2-27 | M03, bibliografía | alta | Entradas sin numeral. **Conservada**: GUM y GUM-S2 con numerales. |
| S-055 | D2-28 | M04, ficha | alta | §7.5.3. **Conservada** (= S-027). |
| S-056 | D2-29 | M04 B2 | baja | Sin cambio sustantivo en ese bloque respecto al previo salvo nota de incertidumbre común. **Conservada**; ajustada por R3-11 (S-108). |
| S-057 | D2-30 | M04 B, escalamiento | media | Pocos gl podían leerse como invalidez automática. **Conservada**. |
| S-058 | D2-31 | M04 I1, pareada/Welch | alta | Unidad y supuestos de los ejemplos no declarados. **Conservada**: jornadas, un nivel, independencia. Cifras reproducidas. |
| S-059 | D2-32 | M04 I2, χ² y F | alta | Pivote mezclado con estadístico bajo H0; faltaban intervalos. **Conservada**: IC de σ² y de razón, colas iguales; Hahs-Vaughn §9.1–9.3. IC reproducidos. |
| S-060 | D2-33 | M04 I3 (potencia) e I4 (u(s)) | alta | Supuestos del cálculo de dos grupos y fuente de u(s) incompletos. **Conservada**: varianza común declarada; GUM §4.3.2 nota y E.4.3 ec. (E.7) verificadas. |
| S-061 | D2-34 | M04 I5, atípicos | media | Datos no visibles y cola no declarada. **Conservada**: vector, fórmulas, tablas 2.10/2.11 de Otto (0,59 verificado), cola unilateral. |
| S-062 | D2-35 | M04 A2, equivalencia | alta | Margen ±0,50 impedía comparar con B; p-valores del margen anterior. **Conservada**: margen didáctico ±0,30 común; p=0,000217 y 0,01183; IC90 B (−0,315; 0,390) no equivalente. Reproducido. |
| S-063 | D2-36 | M04 A3, χ² consistencia | alta | Inversión de V sin condición; gl sin justificar. **Conservada**: V definida positiva, sin parámetros estimados, gl=3. |
| S-064 | D2-37 | M04, cierre y bibliografía | alta | Clave y numerales GUM ausentes. **Conservada**. |
| S-104 | R3-06 | M03 B3, componente común y t | alta | Independencia común–ruido implícita; t citada a MMU sin numeral. **Conservada**: supuestos declarados; GUM G.3.2–G.3.4 y Hahs-Vaughn §6.1. 0,3606 reproducido. |
| S-105 | R3-07 | M03 I3, cita NIST | media | Cita genérica. **Conservada** con ajuste S-115. |
| S-106 | R3-08 | M03 A1–A2, citas | media | $c^TVc$ sin fuente. **Conservada**: GUM §5.2.2 y Crowder §§7.2, 7.4 (verificados). |
| S-107 | R3-09 | M03, bibliografía | media | Capítulo 6 y PDF completo no listados. **Conservada**; URL NIST ajustada en S-115. |
| S-108 | R3-11 | M04 B2 | media | t central exige media planteada verdadera. **Conservada**. |
| S-109 | R3-10 | M04, ficha | media | Ficha sin GUM y con fuentes pendientes genéricas. **Conservada**, ajustada en S-115. |
| S-110 | R3-12 | M04 B3, relevancia | media | Comparación con margen solo verbal en B. **Conservada**: IC95 (−0,402; 0,477) cubre ±0,30; criterio didáctico declarado. |
| S-111 | R3-13 | M04 I5, atípicos | media | Unidad y supuestos de H0 no declarados. **Conservada**. |
| S-112 | R3-14 | M04 A1, Bonferroni | media | «Aumenta» siempre y omisión de que no exige independencia. **Conservada**: FWER controlado sin independencia. |
| S-113 | R3-15 | M04 A2, equivalencia | media | Supuestos del resumen sintético no declarados. **Conservada**. |
| S-114 | R3-16 | M04, bibliografía NIST | media | Sección genérica. **Conservada** con ajuste S-115. |
| S-115 | Revisión actual | M03/M04 bibliografía; M04 ficha | media | Se afirmaba «verificado en la web»/«consultado el 26» sin evidencia guardada en S1. **Corregida**: recurso web externo sin numeral, no cotejado con pdftotext. |

Verificación M03/M04: ejecución de `M03_ejemplos.py`, `M04_ejemplos.py` y `verificar_M03_M04_personal.py` (33 comprobaciones OK) con `curso/.venv/bin/python -I`; salidas idénticas a `*_salida_sol.txt`. pdftotext: GUM §§4.2.7, 4.3.3, 5.2.2, 6.2.1, E.4.3 (E.7), G.3.2; Otto tabla 2.10 (n=8: 0,59); Crowder cap. 7 §§7.2, 7.4. Lakens 2017 y NIST/SEMATECH fuera de docs/: sin numeral. Tres marcadores por capítulo; exclusiones §6 respetadas (sin ANOVA de M6, ajuste de M7 ni presupuesto de M8).

### Control transversal y auxiliares

| Hallazgo | Ubicación | Severidad | Problema | Corrección |
|---|---|---|---|---|
| S-101 | calc/verificar_entrega_sol.py | media | Control heredado solo comprobaba C01–C27 y podía admitir id/candidata en filas distintas; no cubría la segunda interrupción. | Comprueba en ambos registros la asociación por fila de los 27 Cxx y 37 D2-xx con su S-…, nota del supervisor, ausencia de «En revisión.» y quince marcadores en capítulos/índice. El control estructural no sustituye la revisión técnica. |
| S-102 | calc/informe_00.md; referencias_12/ y referencias_34/ | media | Auxiliares antiguos podían leerse como evidencia de una ejecución actual. | Informe M00 identifica procedencia histórica y recomprobación; LEEME de ambos directorios diferencia extractos/salidas históricos de las pruebas nuevas. No se borran antecedentes ni se atribuyen consultas inexistentes. |
| S-103 | S1_00_indice.md | media | Índice previo fechado el 25 solo remitía a primera interrupción, aunque la entrega necesita ambas. | Actualizada fecha al 26 y enlace a las dos auditorías, decisiones Cxx/D2-xx y evidencia vigente; conserva escenas B/I/A, quince marcadores, rótulos, AX y pendientes. |

## Correcciones aplicadas

Las correcciones conservadas ya estaban materializadas en el árbol recibido: se revisan y ratifican, no se atribuyen falsamente a una nueva edición. Las ajustadas identifican el estado final autorizado. No se alteran los antecedentes de Luna/Haiku ni las instantáneas de auditoría.

| Hallazgo y edición | Decisión | Cambio autorizado | Ubicación final |
|---|---|---|---|
| S-001, C01 | conservada | Respaldo externo GUM para error, convención curricular separada. | M00, introducción B |
| S-002, C02 | ajustada | Sustituir tabla 2 por tabla 1 en EN 14625. | M00, introducción B |
| S-003, C03 | conservada | Marcador B completo, sin ejercicio. | M00, final B2 |
| S-004, C04 | conservada | Columna `y` con unidad; índice lectura separado. | M00, I2 pizarra |
| S-005, C05 | conservada | Narración coherente con esquema. | M00, I2 |
| S-006, C06 | ajustada | Bibliografía GUM/EN correcta y ampliación C.2.19. | M00, referencias |
| S-007, C07 | conservada | Aserciones de longitud y tolerancia en contraste real Python/Calc. | calc/M00_ejemplos.py, bloque A |
| S-028, D2-02 | conservada | Referencia GUM C.2.19 para promedio, no prop_e. | M00 B1 |
| S-029, D2-03 | conservada | Nombrar `y`, conservar faltante identificado; script comprueba tres indicaciones y un faltante. | M00 I2; calc/M00_ejemplos.py, bloque I2 |
| S-030, D2-01 | conservada | Corregir numeral a tabla 1. | M00, introducción B |
| S-031, D2-04 | conservada | Sincronizar tabla 1 y C.2.19 en bibliografía. | M00, referencias |

### M01 y M02 — decisiones materializadas

| Hallazgo y edición | Decisión | Cambio autorizado | Ubicación final |
|---|---|---|---|
| S-008, C08 | conservada | Prerrequisito M00 explícito. | M01, ficha |
| S-009, C09 | conservada | CV localizado en ASQ apéndice C p. 572. | M02 B4 |
| S-012, C12 | conservada | Trayecto hipotético, no configuración real SRP. | M01 B2 |
| S-013, C13 | conservada | Parejas de tres días en un único nivel nominal. | M02 B4 |
| S-016, C16 | conservada | s(y)=0,240 nmol/mol. | M02 B4 |
| S-019, C19 | conservada | GUM para error/error relativo; prop_e solo alcance. | M01 I1 |
| S-020, C20 | conservada | Interpretación sin atribución causal injustificada de dispersiones. | M02 B4 |
| S-023, C23 | conservada | Marcador B completo. | M01, final B3 |
| S-024, C24 | conservado el borrado | Suprimir párrafo redundante sin perder explicación de cancelación. | M01 A1 |
| S-025, C25 | conservada | Diapositiva sincronizada a 0,240. | M02 B4 |
| S-032, D2-05 | conservada | Fuente/unidad de 1,1329 documentadas. | M01 ficha |
| S-033, D2-06 | conservada | Ejemplo ppm frente a nmol/mol. | M01 B3 |
| S-034, D2-07 | conservada | Cocientes documentados, corrección distinta de ajuste, dos escenarios de reescalamiento y marcador I completo. | M01 I1 |
| S-035, D2-08 | conservada | Ejemplo de sensibilidades distintas y cancelación parcial. | M01 A1; calc/M01_modelo_variables.py |
| S-036, D2-09 | conservada | Marcador A completo. | M01, final A1 |
| S-037, D2-10 | conservada | Referencias completas GUM/BIPM. | M01 bibliografía |
| S-038, D2-11 | conservada; complementada S-065 | CV localizado; ficha MMU ampliada a §3.1.3. | M02 ficha |
| S-039, D2-12 | conservada | Bordes explícitos y bigotes mínimo–máximo declarados. | M02 B2 |
| S-040, D2-13 | conservada | Marcador B completo. | M02, final B |
| S-041, D2-14 | conservada | Recta entregada, ajuste se enseña en M07. | M02 I2 |
| S-042, D2-15 | conservada | Sustituir numeral VIM no cotejado por GUM B.2.19. | M02 A1 |
| S-043, D2-16 | conservada | Ejemplo numérico de agregación desigual. | M02 A1; calc/M02_examples.py |
| S-044, D2-17 | conservada | Marcador A de sesgos opuestos R&R. | M02, final A |
| S-045, D2-18 | conservada; complementada S-065 | Bibliografía cotejada, MMU actualizado. | M02 bibliografía |
| S-065, R3-03, R3-04, R3-05 | aplicada en esta reanudación | Citas MMU §§3.1.1 y 3.1.3 para operaciones y redondeo final. | M02 ficha, B5 y bibliografía |
| S-066, R3-02 | aplicada en esta reanudación | Corrección individual separada de ajuste físico también en cierre. | M01 cierre |
| S-067 | aplicada en esta reanudación | Salidas regeneradas desde scripts actuales sin alterar cálculos correctos. | calc/M01_modelo_variables_salida_sol.txt; calc/M02_examples_salida_sol.txt |
| S-100, R3-01 | aplicada en esta reanudación | Distinguir conteo de registros con indicación y estados faltantes. | M00 I2, validación ancho/largo |

### M03 y M04 — decisiones materializadas

| Hallazgo y edición | Decisión | Cambio autorizado | Ubicación final |
|---|---|---|---|
| S-010, C10 | conservada | Resolución como entrada simulada. | M03 ficha |
| S-011, C11 | conservada | Clave Hahs-Vaughn. | M04 global |
| S-014, C14 | conservada | P=0 no implica imposible. | M03 B1 |
| S-015, C15 | conservada | Unidad jornada y supuestos. | M04 B1 |
| S-017, C17 | conservada | Variable de un ciclo. | M03 B1 |
| S-018, C18 | conservada | Notación $\Delta_i$. | M04 I1 |
| S-021, C21 | conservada | Resolución supuesta. | M03 B2 |
| S-022, C22 | conservada | Fórmula $\nu_W$. | M04 I1 |
| S-026, C26 | conservada | Procedencia simulada. | M03 B2 |
| S-027, C27 | conservada | §7.5.2. | M04 bibliografía |
| S-046, D2-19 | conservada | Claves GUM/GUM-S2. | M03 ficha |
| S-047, D2-20 | conservada | GUM §4.3.3, §6.2.1. | M03 B2 |
| S-048, D2-21 | conservada | GUM §4.2.3, §4.2.7, §5.2. | M03 B3 |
| S-049, D2-22 | conservada | Independencia en F. | M03 I2 |
| S-050, D2-23 | conservada | Supuestos del modelo de días. | M03 I3 |
| S-051, D2-24 | conservada | Aproximación lineal. | M03 A1 |
| S-052, D2-25 | conservada | Serie y cálculo de autocorrelación. | M03 A2; calc/M03_ejemplos.py |
| S-053, D2-26 | conservada | Ejemplo V=ρuu. | M03 A2; calc/M03_ejemplos.py |
| S-054, D2-27 | conservada | Bibliografía GUM. | M03 referencias |
| S-055, D2-28 | conservada | §7.5.2. | M04 ficha |
| S-056, D2-29 | conservada | Sin cambio adicional. | M04 B2 |
| S-057, D2-30 | conservada | Pocos gl no invalidan. | M04 B, señales de escalamiento |
| S-058, D2-31 | conservada | Supuestos ejemplos I1. | M04 I1 |
| S-059, D2-32 | conservada | IC σ² y razón F. | M04 I2 |
| S-060, D2-33 | conservada | Potencia y u(s) con GUM. | M04 I3 (potencia) e I4 (u(s)) |
| S-061, D2-34 | conservada | Vector y críticos de Otto. | M04 I5 |
| S-062, D2-35 | conservada | Margen ±0,30 común. | M04 A2; calc/M04_ejemplos.py |
| S-063, D2-36 | conservada | Condición V definida positiva. | M04 A3 |
| S-064, D2-37 | conservada | Cierre y bibliografía. | M04 cierre |
| S-104, R3-06 | conservada | Supuestos y citas t. | M03 B3 |
| S-105, R3-07 | conservada; ajustada S-115 | Cita NIST. | M03 I3 |
| S-106, R3-08 | conservada | GUM §5.2.2; Crowder. | M03 A1 |
| S-107, R3-09 | conservada; ajustada S-115 | Bibliografía. | M03 referencias |
| S-108, R3-11 | conservada | Condición t central. | M04 B2 |
| S-109, R3-10 | conservada; ajustada S-115 | Ficha. | M04 ficha |
| S-110, R3-12 | conservada | Relevancia ±0,30 en B. | M04 B3 |
| S-111, R3-13 | conservada | Supuestos atípicos. | M04 I5 |
| S-112, R3-14 | conservada | Bonferroni sin independencia. | M04 A1 |
| S-113, R3-15 | conservada | Supuestos equivalencia. | M04 A2 |
| S-114, R3-16 | conservada; ajustada S-115 | Bibliografía NIST. | M04 referencias |
| S-115 | aplicada en esta revisión | «consultado/verificado en la web» sustituido por «recurso web externo no cotejado». | M03 y M04 referencias; M04 ficha |
| R3-01 a R3-05 | conservadas | Ya registradas como S-100, S-066, S-065. | M00 I2; M01 cierre; M02 |

### Controles y documentación de esta reanudación

| Hallazgo | Cambio aplicado | Ubicación |
|---|---|---|
| S-101 | Ampliar comprobación estructural a 64 candidatas, asociaciones por fila, nota del supervisor y cierre documental sin marcador pendiente de revisión. | calc/verificar_entrega_sol.py |
| S-102 | Identificar procedencia y vigencia de auxiliares; preservar originales de auditoría y resultados anteriores como históricos. | calc/informe_00.md; calc/referencias_12/LEEME.md; calc/referencias_34/LEEME.md |
| S-103 | Actualizar fecha, enlaces de ambas auditorías y alcance de decisiones en índice de entrega. | S1_00_indice.md, cabecera y estado |

### Nota del orquestador: ediciones previas a la interrupción

Antes de la interrupción, sol aplicó 27 ediciones sin registrarlas: 25 en los libretos M00–M04 y una en `calc/M00_ejemplos.py`. Están reconstruidas y verificadas byte a byte en `auditoria_interrupcion_sol/LEEME.md` (tabla C01–C27, versiones previas `*.pre_sol.*` y `cambios_sol.diff`). Al reanudar, cada Cxx debe quedar aquí asociada a un hallazgo S-…, con su decisión (conservada, ajustada o revertida) y su justificación.

### Ediciones de calc/ de la segunda interrupción

Registro retrospectivo de los bloques heredados, cotejados contra `437e8bf`; no se atribuyen a esta reanudación. La segunda auditoría no contiene instantánea propia previa de los scripts: las asociaciones se hacen por contenido, no por una cronología que no puede reconstruirse. Los cambios nuevos O-… se registran aparte abajo.

| Archivo | Bloque heredado | Decisión | S-… asociado y fundamento |
|---|---|---|---|
| `calc/M00_ejemplos.py` | I2: faltante con clave, conteo 3+1 y aserciones | conservada | S-029, S-100: preserva estados y valores no faltantes sin inventar lecturas. O-01 corrige aparte la clave de conteo de I1. |
| `calc/M01_modelo_variables.py` | Reescalar solo indicación o ambos miembros; aserciones de signo, razón y cancelación | conservada | S-034: reproduce +6,73477 y +1,31677 y conserva el relativo al reescalar ambos. |
| `calc/M01_modelo_variables.py` | Entrada común con sensibilidades iguales/distintas | conservada | S-035: comprueba cancelación total y residual 0,2. |
| `calc/M02_examples.py` | Cuartiles/caja, histogramas y varianza; seis parejas en un nivel nominal | conservada | S-013, S-016, S-025, S-039: coherencia de diseño y s(y)=0,240139. O-02 añade la identidad descriptiva que faltaba. |
| `calc/M02_examples.py` | Agregación desigual, comprobaciones de recta, cero, redondeo y MAD | conservada | S-041, S-043, S-067: cálculo reproducible y medias con ponderaciones explícitas. |
| `calc/M03_ejemplos.py` | Variable de un ciclo y normalización de probabilidades | conservada | S-017: Bernoulli antes que conteos de varios ciclos. |
| `calc/M03_ejemplos.py` | Serie desplazada, V desde R, propagación y admisibilidad | conservada | S-048, S-052, S-053: diferencia entre estimadores, simetría y semidefinición comprobadas. |
| `calc/M04_ejemplos.py` | Supuestos B y críticos de Grubbs unilateral/bilateral | conservada | S-015, S-061, S-111: unidad jornada y crítico compatible con cola declarada. |
| `calc/M04_ejemplos.py` | Margen ±0,30, TOST de B, aserciones SciPy/statsmodels y cálculo matricial | conservada | S-058, S-060, S-062, S-063: contraste de API, potencia mínima entera y misma regla de equivalencia. |

## Correcciones tras la revisión Opus

Fecha: 2026-10-26. Supervisor: claude-sol (gpt-6.1-sol). Se aplica la revisión `S1_revision_opus.md`: cuatro hallazgos mayores y diez menores; no hubo críticos. Ningún hallazgo se rechaza. Las referencias pendientes se identifican como tales, sin inventar respaldo. Las auditorías e informes anteriores permanecen como antecedentes.

| Id | Decisión | Cambio | Ubicación | Justificación |
|---|---|---|---|---|
| O-01 | aplicado | Agrupar por campaña × analista × día: ocho combinaciones de dos ciclos; aclarar día relativo a campaña. Script, aserciones y salida sincronizados. | M00 I1; `calc/M00_ejemplos.py` | No se mezcla el día 1 de campañas distintas; 8 × 2 = 16 filas. |
| O-02 | aplicado con cambios | Añadir s(x)=0,179 y descomposición 0,03200 + 0,01767 + 0,00800 = 0,05767; porcentajes 55,5 / 30,6 / 13,9 y lectura oral. | M02 B4; `calc/M02_examples.py`; `calc/verificar_opus_sol.py` | Identidad descriptiva verificada con numpy y Decimal; no atribución causal ni componentes independientes. Completa B sin adelantar la teoría de M03-I. |
| O-03 | aplicado con cambios | Serie determinista de 16 lecturas con deriva 0,05 por minuto; comparar ventanas, media global, bloques y corrección a instante declarado. | M03 B3 y A2; `calc/M03_ejemplos.py` | Medias de mitades 420,175 / 420,575; global 420,375; corregida a t=0, 420,000. Se declaran residuos construidos, no iid, y no se valida s/√n. GUM F.1.1.3 respalda investigar deriva por subperiodos. |
| O-04 | aplicado con cambios | Fórmulas aproximadas normales, efecto estandarizado por diseño, llamadas statsmodels y explicación de t no central; efecto de Cohen escrito $d_C$ para reservar $d$ a días. | M04 I3; `calc/M04_ejemplos.py` | Aproximaciones 31,3955 y 24,5277 por grupo; solución t 33,3671 / 25,5246 y redondeo 34 / 26. Se distingue varianza común de Welch. |
| O-05 | aplicado | Mensurando GUM B.2.9 y VIM 2.3; error GUM B.2.19; corrección GUM B.2.23; bibliografía actualizada. | M01 B1 y referencias; `calc/referencias_opus_sol.txt` | Numerales GUM verificados con pdftotext; GUM-6 §5.1 cita explícitamente VIM 2.3. Sesgo conserva VIM sin numeral; prop_e solo convención curricular. |
| O-06 | aplicado con cambios | Retirar atribución de construcción chi-cuadrado a §§8.2/9.1.1; mantener §9.1.1 para F; registrar pendiente específico. | M03 I2; M03 bitácora | No se localizó respaldo explícito de suma de cuadrados en las fuentes consultadas. Se conserva definición matemática correcta, sin fingir verificación documental. |
| O-07 | aplicado | Sustituir secciones de salida de software por §§7.1.3.2 y 7.1.7. | M04 I1 | Numerales cotejados con pdftotext: Welch y supuestos, no salida de software. |
| O-08 | aplicado con cambios | Cita ASQ solo junto a definición; límite cerca de cero explicado por denominador; pendiente bibliográfico registrado. | M02 B4; M02 bitácora | Con dispersión fija, cociente crece al disminuir magnitud de media y no existe con media cero; argumento aritmético, no afirmación atribuida a ASQ. |
| O-09 | aplicado | Quitar comillas de narración, definir variable aleatoria antes del ejemplo y dejar exclusión GGMR una sola vez con remisión. | M03 B1, A2 y escalamiento A | Homogeneidad del guion oral y secuencia de prerrequisitos, sin borrar contenido. |
| O-10 | aplicado | Unificar imperativos a ustedes. | M00 A2; M01 B2 e I1 | No declaren, no informen, no mezclen, no inviertan; mismo tratamiento que resto de sección. |
| O-11 | aplicado | Enlazar covarianza con M03-I antes de M8/M9, también en ficha, A1 y cierre. | M01 ficha, introducción A, A1 y cierre | Refleja secuencia real y remisión AX.2 sin desarrollar teoría en M01. |
| O-12 | aplicado | Traducir residuos, ambos ejes y pocos grados de libertad al contexto de plantilla; conservar lista y señales locales. | M00–M02, señales B | Operador puede detenerse ante condición no cubierta sin necesitar teoría futura; remisiones a M3/M4/M5/M7. |
| O-13 | aplicado | Corregir ubicaciones: S-060 I3 e I4; S-061/S-111 I5; S-057 señales B. | Tablas de hallazgos y decisiones de esta revisión | Registro localizable según encabezados reales; no cambia dictámenes técnicos históricos. |
| O-14 | aplicado | Tabla retrospectiva de scripts heredados; individualizar R3-01–05 y extender verificador a los 16 R3, además de 14 O. | Tabla «Ediciones de calc/ de la segunda interrupción»; `calc/verificar_entrega_sol.py` | Asociaciones por fila en hallazgos y decisiones; reconocer que faltan instantáneas propias de scripts, sin atribuir cronología no demostrada. |

### Decisiones sobre el respaldo posterior a Opus

Se cotejó la fecha de `S1_revision_opus.md` con las carpetas `auditoria_respaldo_*`: `auditoria_respaldo_20261026_053907/` es anterior y conserva sus decisiones R3; `auditoria_respaldo_20261026_200841/` es posterior. Sus 23 bloques se numeran P6-01–P6-23 en el orden de los encabezados `@@` de `cambios.diff`. Se revisaron como candidatas, no como correcciones aprobadas por el intento interrumpido. La nota del orquestador atribuye el corte a un reinicio del servidor, no a cuota. Se preservan respaldo, instantánea y nota sin alteración.

| Bloque | Id O-… | Decisión | Cambio y ubicación | Justificación |
|---|---|---|---|---|
| P6-01 | O-12 | aplicado | Conservar traducción de señales, M00 B. | Permite detenerse sin anticipar teoría. |
| P6-02 | O-01 | aplicado | Conservar clave campaña–analista–día, M00 I1. | Los días son relativos a campaña. |
| P6-03 | O-01 | aplicado | Conservar conteo dos por clave, M00 I1, tabla. | Ocho combinaciones por dos ciclos dan dieciséis. |
| P6-04 | O-10 | aplicado | Conservar «No declaren», M00 A2. | Tratamiento ustedes. |
| P6-05 | O-11 | aplicado | Conservar M03-I en ficha M01. | Secuencia curricular real. |
| P6-06 | O-05 | aplicado | Conservar respaldo de mensurando y error, M01 B1. | GUM y cita explícita VIM en GUM-6. |
| P6-07 | O-05 | aplicado | Conservar GUM B.2.23 para corrección, M01 B1. | prop_e queda como convención. |
| P6-08 | O-10 | aplicado | Conservar imperativos plurales, M01 B2. | Tratamiento ustedes. |
| P6-09 | O-12 | aplicado | Conservar traducción de señales, M01 B. | Prioriza modelo y unidades. |
| P6-10 | O-10 | aplicado | Conservar «No mezclen / No inviertan», M01 I1. | Tratamiento ustedes. |
| P6-11 | O-11 | aplicado | Conservar remisión M03-I, introducción A de M01. | La covarianza precede a M8/M9. |
| P6-12 | O-11 | aplicado | Conservar remisión M03-I, M01 A1. | Enlaza cálculo posterior sin adelantarlo. |
| P6-13 | O-05, O-11 | aplicado | Conservar cierre y bibliografía M01. | Numerales y secuencia coherentes con narración. |
| P6-14 | O-02, O-08 | aplicado con cambios | Conservar identidad descriptiva y separar cita ASQ, M02 B4; precisar lectura de valores redondeados. | No confundir descomposición aritmética con atribución causal; CV singular en cero. |
| P6-15 | O-12 | aplicado | Conservar traducción de señales, M02 B. | No exige reconocer conceptos aún no enseñados. |
| P6-16 | O-02 | aplicado | Conservar GUM §5.2.2 en bibliografía M02. | Respalda combinación con covarianza. |
| P6-17 | O-03, O-09 | aplicado | Conservar secuencia de variable aleatoria, narración sin comillas y ejemplo de deriva, M03 B. | Ventanas y supuestos explícitos; residuos deterministas no son iid. |
| P6-18 | O-06, O-09 | aplicado con cambios | Conservar narración sin comillas y retirar atribución incorrecta de chi-cuadrado, M03 I. | La construcción matemática no se atribuye a secciones que no la contienen. |
| P6-19 | O-03, O-09 | aplicado | Conservar comparación global/bloques/corrección y exclusión única, M03 A y referencias. | Estrategia depende del resultado y del instante objetivo. |
| P6-20 | O-04 | aplicado | Conservar referencias de planificación, ficha M04. | Distingue cálculo de potencia de salida de software Welch. |
| P6-21 | O-07 | aplicado | Conservar §§7.1.3.2 y 7.1.7, M04 I1. | Respaldan Welch y supuestos. |
| P6-22 | O-04 | aplicado con cambios | Conservar efectos por diseño, aproximación normal y llamadas t no central; usar $d_C$ para efecto de Cohen, M04 I3. | Permite reconstruir tamaños y potencia. |
| P6-23 | O-04, O-07 | aplicado | Conservar cierre y bibliografía M04, incluida herramienta statsmodels. | Sincroniza fuentes con método enseñado. |

### Comprobaciones de cierre tras Opus

Reanudación de cierre: se ratificaron las correcciones heredadas, se decidió cada bloque P6 y se amplió el control estructural a sus 23 asociaciones O-…. Correcciones adicionales: aproximación explícita de cifras redondeadas en M02 B4 y magnitud del CV cuando la media tiende a cero por valores negativos (O-02/O-08); notación $d_C$ en M04 I3 (O-04); sustitución del extracto erróneo H.5.2.2 por el verdadero §5.2.2, cotejado con `pdftotext -layout`, en `calc/referencias_opus_sol.txt` (O-02, corrección de evidencia, sin cambio de fórmula).

Los cinco scripts se ejecutan con `curso/.venv/bin/python -I`; sus salidas se comparan byte a byte con los cinco `*_salida_sol.txt`. `verificar_M03_M04_personal.py` mantiene 33 comprobaciones; `verificar_opus_sol.py` contrasta O-02 con Decimal, sin numpy; `verificar_entrega_sol.py` controla C, D2, R3, O y quince marcadores. Resultados de cierre: `calc/pruebas_opus_sol.txt`. Evidencia bibliográfica nueva de M01/M02: `calc/referencias_opus_sol.txt`; M03/M04 verificaron los pasajes indicados mediante pdftotext. Estas comprobaciones no constituyen revisión final de todo el curso ni validación de datos reales del laboratorio.

## Estado de entrega

Fecha: 2026-10-26. Supervisor: claude-sol (gpt-6.1-sol), tras revisión Opus.

- Decisiones: O-01–O-14 aplicados o aplicados con cambios; cuatro mayores resueltos, ningún rechazo. Los 23 bloques P6 del respaldo posterior a Opus tienen decisión individual y asociación al hallazgo atendido; control estructural satisfactorio. C01–C27, D2-01–D2-37 y R3-01–R3-16 conservan hallazgo y decisión explícitos.
- Cálculos: cinco scripts y salidas sincronizados; verificaciones Decimal, 33 comprobaciones M03/M04 y control estructural ampliado. Evidencia de ejecución en `calc/pruebas_opus_sol.txt`.
- Formato: cinco libretos B/I/A, quince marcadores de prácticas, sin ejercicios desarrollados. Índice actualizado con cambios y límites.
- Pendientes documentales: fuente explícita para construcción chi-cuadrado (O-06) y fuente específica sobre limitación del CV (O-08, razonamiento aritmético ya expuesto); cotejo de recursos externos NIST/SEMATECH, Lakens y VIM salvo 2.3 corroborado por GUM-6.
- Estado: **sección S1 corregida tras Opus y entregada en fase de contenido**. No acredita prácticas, revisión final del curso ni autorización para impartir. Pendientes quince prácticas y preparación curricular posterior.
