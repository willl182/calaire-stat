# Bitácora de desarrollo — M06

## Plan

### Alcance por nivel (tomado literalmente de `prop_e.md`, §5, M6)

- **B:** «repetibilidad y precisión intermedia. Se entregan `s_r` y `s_entre` ya calculadas como estimaciones de `σ` y `τ` del modelo equilibrado `e_dj = μ + D_d + ε_dj`, donde los efectos de día `D_d` son independientes, de varianza `τ²`, y los errores de lectura `ε_dj` son independientes, de varianza `σ²`, e independientes de los efectos de día. Con `n` lecturas en cada uno de `d` días, el participante interpreta cada componente y calcula la contribución de precisión al promedio de errores: `u²_prec(ē) = s²_entre/d + s²_r/(d·n)` (con `s_entre = τ̂` y `s_r = σ̂`). No ejecuta el ANOVA ni aplica un divisor automático. Si se entregan desviaciones de promedios diarios, se identifican como tales y, bajo el mismo modelo, se usa `s²_medias/d` sin volver a sumar repetibilidad. La fórmula requiere diseño equilibrado y los supuestos indicados; dependencia, desequilibrio o confusión entre día y ciclo exigen revisar el modelo. Las demás contribuciones del presupuesto se incorporan en M8.»
- **I añade:** «ANOVA de un factor aleatorio (sumas de cuadrados, grados de libertad, cuadrados medios, F); estimación de componentes y su incertidumbre; efectos fijos y aleatorios; dos factores e interacción; residuos y heterogeneidad (Cochran); ISO 5725 cuando el diseño corresponda.»
- **A añade:** «analista × campaña con días anidados; elección de denominadores; componentes negativas y alternativas de estimación; aplicabilidad de ISO 5725, incluido el sesgo de un laboratorio.»

### Escenas previstas

1. Ficha del capítulo: competencia estadística, prerrequisitos M4–M5, contenido aditivo por nivel, datos rotulados, anexos AX.4 y AX.11, referencias.
2. B1: qué pregunta responde cada componente; modelo por días y lecturas; separar repetibilidad de precisión intermedia.
3. B2: cálculo de `u_prec(ē)` con componentes ya entregadas; caso de desviaciones de medias diarias; interpretación de diseño balanceado y supuestos. Marcador de práctica B.
4. Señales de escalamiento B: dependencia, desequilibrio, ciclo confundido con día, heterogeneidad, falta de trazabilidad del componente entregado.
5. I1: ANOVA de un factor aleatorio; sumas de cuadrados, grados de libertad, cuadrados medios y prueba F; ejemplo numérico reproducible.
6. I2: estimación por momentos de componentes y su incertidumbre; si una estimación resulta negativa, remisión a A2 para su interpretación y alternativas.
7. I3: fijo/aleatorio, dos factores cruzados e interacción, denominadores de F; ejemplo reproducible y residuales.
8. I4: diagnósticos de residuos, heterogeneidad entre concentraciones y Cochran; cuándo analizar por nivel o modelar varianza. Marcador de práctica I.
9. A1: estructura real del estudio CALAIRE R&R: analista × campaña, días anidados; modelos admisibles, selección de denominadores, límites de potencia.
10. A2: componentes negativas y alternativas; aplicación y límites de ISO 5725 en un laboratorio, sesgo respecto de referencia, reporte. Marcador de práctica A.
11. Señales de escalamiento ampliadas y cierre narrado con transición a M7.

### Datos y rótulo de origen

- Ejemplos pequeños generados para explicar el cálculo ANOVA y sus componentes: **simulados**, con regla generadora documentada en el libreto y en `calc/M06_*.py`; no se atribuirán a CALAIRE.
- Estudio R&R 2022–2023, hojas por nivel, archivo `docs/Resultados R&r_2022 2023 (1).xlsx`: **propio**, según `guia_libreto.md` §6. Se usará solo para describir su diseño y los resultados que M6 asigna explícitamente; los scripts reproducirán los resúmenes numéricos que se incluyan.
- No se tomarán los datos crudos del certificado F-PSMT-01 para que el nivel B ejecute ANOVA: en B se entregan componentes, como exige prop_e.

### Cálculos previstos

- Calcular contribución de precisión al promedio de errores desde `s_r`, `s_entre`, `n`, `d`; comparar con componente entre días omitida y con `s_medias` (sin doble conteo).
- En conjuntos simulados balanceados, reproducir SS total/entre/dentro, grados de libertad, MS, estadístico F, componentes por momentos y su incertidumbre/precisión.
- Reproducir un ejemplo de dos factores cruzados con interacción y el denominador adecuado de F.
- Calcular estadístico de Cochran en un conjunto pequeño de varianzas para ilustrar heterogeneidad, no como permiso para eliminar datos.
- Verificar y reproducir los rangos/resultados R&R que se narren, cuando las hojas y estructura lo permitan.
- Todos los cálculos numéricos que aparezcan en el capítulo deben tener correspondencia con scripts `curso/.venv/bin/python` en `curso/S2_modelos_calibracion/calc/M06_*.py`.

### Referencias a verificar en `docs/`

- Intro. Statistics in Metrology, §§9.3.1–9.3.6, en capítulos PDF disponibles: cuadrados medios esperados, efectos aleatorios/mixtos, supuestos y R&R.
- Otto, §2.3; Statistical Concepts, cap. 9: ANOVA y distribución F.
- ISO 5725-3:1994, §§5–6, §8 y §§9.3–9.5; Partes 2 y 6: alcance y diseños pertinentes.
- GUM JCGM 100:2008, Anexo H.5 y G.4; Metrology and Measurement Uncertainty, §4.4.
- Deldossi y Zappa (2009); EN 14625, §8.2.
- Estudio R&R CALAIRE 2022–2023, hojas de 45 a 455 ppb.
- Cualquier numeral que no pueda verificarse con `pdftotext` se omitirá de la cita en el libreto y quedará como pendiente aquí.

### Anexos previstos

- Remitir a **AX.4** para deducción de cuadrados medios esperados del ANOVA de un factor aleatorio y de `u²_prec(ē) = s²_entre/d + s²_r/(d·n)`; explicar y usar las fórmulas sin derivarlas.
- Remitir a **AX.11** si se presenta la incertidumbre/intervalo de componentes de precisión, sin derivar en clase.

## Ejecución

### Libreto y prácticas

Se escribió `M06_libreto.md` con ficha, escenas B1–B2, señales de escalamiento de B, escenas I1–I5, escenas A1–A2, señales de escalamiento avanzado, cierre y referencias. Se incluyeron los alcances B, I y A de prop_e §5, M6; advertencias narradas para errores críticos; datos simulados rotulados expresamente y el estudio propio R&R identificado por archivo y hojas. Se insertaron únicamente los tres marcadores requeridos —contribución de precisión del promedio (B), ANOVA de días en un nivel (I), análisis R&R analista × campaña con días anidados (A)—; no se escribieron prácticas, ejercicios, soluciones, evidencias evaluables ni rúbricas.

### Scripts y resultados reproducidos

Se ejecutaron ambos scripts con `curso/.venv/bin/python` desde la raíz:

- `calc/M06_ejemplos.py` (datos ilustrativos **simulados**): para el ejemplo B reprodujo `u²_prec = 0,0162 (nmol/mol)²`, `u_prec = 0,127279 nmol/mol`, `U_prec = 0,254558 nmol/mol`, repetibilidad sola `0,034641 nmol/mol` y `s_medias = 0,311769 nmol/mol`, con `u` de medias `0,127279 nmol/mol`. Para la ANOVA de un factor reprodujo medias diarias `0,00; 0,50; 0,10`, `SS_entre = 0,56`, `SS_dentro = 0,18`, `SS_total = 0,74`, g.l. `2; 9; 11`, `MS_entre = 0,28`, `MS_dentro = 0,02`, `F = 14,0`, `F_crítico = 4,2565`, `s_r = 0,141421` y `s_entre = 0,254951 nmol/mol`. El intervalo chi-cuadrado de 95 % para la varianza residual reprodujo aproximadamente `[0,00946; 0,06666] (nmol/mol)²`; la aproximación de error estándar de `τ̂²` dio `0,070040 (nmol/mol)²` y la aproximación delta para `s_entre`, `0,137359 nmol/mol`. El ejemplo simulado de componente entre días negativa, ahora ubicado en A2, reprodujo `MS_entre = 0,006533`, `MS_dentro = 0,016667` y estimación por momentos no restringida `−0,002533 (nmol/mol)²`. El ejemplo cruzado reprodujo sumas de cuadrados, g.l. y F para A, el factor segundo y su interacción (`1,5625; 5,25; 2,6667`). El ejemplo Cochran reprodujo `C = 0,45`; no se tomó una decisión de significación al no definir en el ejemplo un valor crítico.
- `calc/M06_RR_CALAIRE.py` (datos **propios** del libro XLSX): extracción de seis días por bloque y analista, en los diez niveles. Las hojas por nivel contienen tres bloques; su asignación a campañas listadas en BASE DE DATOS y la razón por la que no se incluyen otros pares no están documentadas en el libro y quedan como pendiente de confirmación. El cálculo reprodujo `F_analista` máximo `1,2382`, valor crítico `18,5128`, e interacciones sobre `F_crítico = 3,3158` en `135, 360, 405 y 455 nmol/mol`, con F `6,6115; 4,3087; 6,4735; 5,0654`. El `F_bloque` osciló irregularmente entre `0,0163` y `9,6994` (aprox. `0,02` a `9,70`); no sustenta una tendencia monotónica. Se renombraron en el script los ejes «campaña» a «bloque» para no presentar la asignación inferida como confirmada; al recalcular, los valores no cambiaron. La desviación entre días anidados quedó entre `0,1061` y `0,2062 nmol/mol`. En el nivel 405, las medias de los tres bloques por analista fueron `[0,2712; 0,4209; 0,2189]` y `[0,2484; 0,7290; 0,1317]`; en 455, `[0,2851; 0,4914; 0,1290]` y `[0,1985; 0,8279; 0,2487]`. Esto respalda los valores aproximados `0,73` y `0,83` citados en el libreto, referidos al segundo bloque, no a una campaña confirmada. El cómputo conserva bloques de seis días por analista y no empareja días por el número de fila.

### Referencias verificadas con `pdftotext`

| Clave | Numeral comprobado | Archivo de `docs/` | Página(s) PDF donde se comprobó |
|---|---|---|---|
| Intro | §§9.3.1–9.3.6: modelos aleatorios y mixtos, supuestos, R&R y resumen ANOVA | `intro_stats_metro_c09.pdf` | 7–12 |
| ISO 5725-3 | §§5–6: factores y términos de precisión intermedia | `ISO 5725-3_1994.pdf` | 10–13 |
| ISO 5725-3 | §8: estudio dentro del laboratorio | `ISO 5725-3_1994.pdf` | 14 |
| ISO 5725-3 | §§9.3–9.5: diseños anidados y anidados escalonados | `ISO 5725-3_1994.pdf` | 15–17 |
| GUM | G.4: grados de libertad efectivos | `ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf` | 81–84 |
| GUM | H.5: análisis de varianza | mismo archivo GUM | 106–112 |
| M&MU | §4.4: repetibilidad y reproducibilidad (título y contenido) | `Metrology and Measurement Uncertainty.pdf` | 147–148 (páginas impresas 131–132) |

Los numerales internos `prop_e §…`, `guia_libreto §…` y `AX.…` remiten a documentos del curso, no a numerales de fuentes PDF. VIM se cita sin numeral porque no está disponible en `docs/`. Las referencias a ISO 5725-1, -2, -4 y -6 se citan sin cláusula; no se introdujeron numerales no verificados para ellas. Se consultaron sus nombres de archivo, pero no se usaron cláusulas específicas en el libreto.

### Decisiones y pendientes

- Se usaron solo fuentes retenidas en el libreto y con numerales verificados; Otto, Deldossi y Zappa, EN 14625 y Statistical Concepts quedaron como referencias candidatas del plan y no se citaron, por lo que no se les atribuye contenido.
- El ejemplo de componente negativa se muestra como estimación no restringida; no se impone una regla universal para truncarla. El texto explica opciones y deja la elección a un procedimiento validado.
- El caso Cochran enseña estadístico e interpretación como señal diagnóstica, pero no declara una decisión de significación sin un valor crítico asociado al diseño.
- Los datos del R&R son propios. Los ejemplos sintéticos y sus resultados son didácticos; no se atribuyen a CALAIRE.
- **Pendiente de fase posterior:** revisión de redacción/contenido por los revisores definidos en el plan maestro; desarrollo de prácticas y materiales de evaluación, fuera de la fase actual. La referencia específica para la aproximación delta usada en el error estándar de `s_entre` queda pendiente de verificación; no se cita como referencia técnica en el libreto.

## Correcciones (revisión Haiku)

| Id del hallazgo | Decisión | Cambio hecho | Ubicación | Justificación |
|---|---|---|---|---|
| R01 | aplicado | Se definió precisión intermedia en B1 y se vinculó el efecto de día como factor variable dentro del laboratorio. | Libreto, B1 | Cumple el alcance B; ISO 5725-3 §§5–6 describe factores y precisión intermedia. |
| R02 | aplicado | Se retiró de I2 el desarrollo y ejemplo de componentes negativas; se mantuvo la fórmula por momentos y se remite a A2. El caso negativo y las alternativas quedaron en A2. | Libreto, I2 y A2; Plan § escenas previstas | Respeta prop_e §5 M6: componentes negativas y alternativas son contenido de A. |
| R03 | aplicado con cambios | Se eliminó el conjunto 0,01583/0,01528 no reproducible; se conservó el ejemplo negativo, ya reproducido por el script y trasladado a A2. | Libreto, I2 y A2 | No se añade una cifra a `calc/M06_ejemplos.py` sin necesidad: se elimina la cifra sin soporte y permanece el ejemplo que sí reproduce el cálculo. |
| R04 | aplicado con cambios | Se separó la explicación en párrafos, se distinguió el IC chi-cuadrado de los errores estándar aproximados y se corrigió la frase sobre cobertura. Se atribuyó el IC de precisión a AX.11; la referencia técnica de la aproximación delta queda pendiente. | Libreto, I2; Decisiones y pendientes | GUM G.4 trata grados de libertad efectivos, no el IC chi-cuadrado señalado. Los errores estándar aproximados no son intervalos de confianza exactos para `τ`; no se inventa una referencia para el método delta. |
| R05 | aplicado con cambios | Se describen los tres bloques de las hojas por nivel, se aclara que la asignación a campañas es inferida, se añade una nota al instructor para confirmar la selección y la discrepancia entre cinco pares listados y la nota de cuatro calibraciones; el script etiqueta el factor como bloque. | Libreto, A1; `calc/M06_RR_CALAIRE.py` | El libro no documenta la asignación bloque→campaña ni el criterio de exclusión; no se presenta la inferencia como hecho. |
| R06 | aplicado | Se cambió «del orden de 0,2» por el rango 0,13–0,49 nmol/mol para las demás combinaciones en 405 y 455. | Libreto, A1 | Coincide con las medias reproducidas por `calc/M06_RR_CALAIRE.py`. |
| R07 | aplicado | Se sustituyó la tendencia no sustentada por el rango irregular de `F_bloque`, aproximadamente 0,02–9,70. | Libreto, A1; `calc/M06_RR_CALAIRE.py` | Se ejecutó el script actualizado: rango exacto 0,016346–9,699396; la secuencia no es monótona. El cambio de etiqueta no altera los cálculos. |
| R08 | aplicado | Se usó `e` (error con signo) en los modelos cruzado y analista × bloque; la fórmula A1 y su pizarra ahora coinciden, y campaña queda como interpretación condicionada a confirmar la asignación. | Libreto, I3 y A1 | Mantiene la convención del curso: `y` es indicación y `e = y − x` es error; evita presentar la asignación de bloques como hecho. |
| R09 | aplicado | En ANOVA de un factor se uniformaron SS/MS como entre y dentro, se usó `d` para días y se renombró el segundo factor cruzado como P, reservando D para día. | Libreto, I1–I3 | Evita la colisión de D y conserva la notación de `prop_e` §3. |
| R10 | aplicado con cambios | Se retiró la afirmación específica sobre prueba t en I5, no respaldada por las citas ni asignada a M6; se dejó un contraste breve con la comparación de medias de M4 y componentes de varianza. | Libreto, I5 | Crowder 2020 §9.3.4 trata Gauge R&R, no prueba t; ISO 5725-3 §8 cubre precisión intermedia. |
| R11 | aplicado | Se cambiaron las claves a `Crowder 2020` y `MMU` en el texto, ficha y referencias. | Libreto, ficha, escenas y referencias | Sigue las claves bibliográficas definidas en `guia_libreto.md` §5. |
| R12 | aplicado | Se eliminaron citas internas a `prop_e` y `guia_libreto` del texto narrado; las remisiones a AX se expresan como «Anexo AX.x». | Libreto, escenas | La guía §5 establece referencias técnicas externas; `prop_e` fija alcance curricular, no fundamentación técnica. |
| R13 | aplicado | Se añadió la escala temporal de seis días en B2 y se cerró con la acción de reportar `U_prec` como componente parcial y completar el presupuesto en M8. | Libreto, B2 | Cumple la declaración previa del resultado, unidad de repetición y escala temporal; especifica la acción de reporte. |
| R14 | aplicado | Se mantuvo GUM H.5 y se hizo remisión explícita al Anexo AX.4 para la deducción de las esperanzas del ANOVA de un factor. | Libreto, I2 | Crowder 2020 §9.3.1 no presenta allí el caso unifactorial; AX.4 es el anexo de deducción definido para esa fórmula. |
| R15 | aplicado | Se normalizó la puntuación de la lista y se identificó `ε` como error de lectura o de réplica. | Libreto, I3 | Evita variación terminológica accidental y deja explícito que se trata del término residual del modelo. |

### Correcciones adicionales por iniciativa propia

- Corregí referencias narradas que aún usaban la clave abreviada «Intro» y armonicé la ficha con `Crowder 2020` y `MMU`.
- Añadí en A1 una cautela explícita sobre la inconsistencia documental (cinco pares enumerados frente a la nota de cuatro calibraciones), para no resolverla por inferencia.
- Revisé puntuación y restos de citas tras retirar las referencias internas; eliminé la atribución a una campaña específica de los valores 0,73/0,83, pues la asignación de bloques no está confirmada.
