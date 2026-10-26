# Revisión de redacción y errores — M06 «ANOVA y componentes de varianza»

Revisor: Haiku. Fecha: 24 de octubre de 2026. Libreto revisado: `curso/S2_modelos_calibracion/M06_libreto.md` (sin cambios).

## Plan de revisión

**Qué se leyó.** `curso/guia_libreto.md` completa; `prop_e.md` (§§1–4, §5 módulo M6, §6, §7, §8 y §10); `M06_libreto.md` completo; `M06_bitacora_luna.md` (Plan y Ejecución); `calc/M06_ejemplos.py` y `calc/M06_RR_CALAIRE.py`.

**Cómo se revisó.**

1. Se ejecutaron ambos scripts con `curso/.venv/bin/python`, sin errores. Cada cifra del libreto (ejemplos B, I y A, y cocientes del caso CALAIRE) se comparó con la salida.
2. Se leyeron las hojas `405ppb` (filas 1–26) y `BASE DE DATOS` de `docs/Resultados R&r_2022 2023 (1).xlsx` para comprobar qué bloques de datos corresponden a qué calibraciones.
3. Se extrajo texto con `pdftotext` de los PDF de `docs/` (Intro c09, ISO 5725-2 y -3, GUM, M&MU) y se buscaron los numerales citados.
4. Se buscaron en el libreto las exclusiones de prop_e §6, las viñetas, los puntos decimales, las etiquetas de acotación y las notaciones de guía §4.
5. Se contrastó cada escena con el alcance por nivel de prop_e §5 M6 (ni más ni menos).
6. Se revisó la forma de libreto (guía §§1–2): narración, acotaciones, marcadores de práctica, estructura y longitud de párrafos.

**Qué no se hizo.** No se editó el libreto. No se verificó la editorial ni el año de las obras citadas (los autores sí). Los numerales de ISO 5725-2 no se buscaron más allá de Cochran.

## Hallazgos

| id | Ubicación (escena y texto citado) | Tipo | Severidad | Problema | Corrección propuesta |
|---|---|---|---|---|---|
| R01 | Nivel B, ficha («Repetibilidad y precisión intermedia») y Nivel I, intro («damos por vistos los conceptos del básico: la diferencia entre repetibilidad y precisión intermedia»); Escena B1 no la define | Contenido (cobertura) | mayor | prop_e §5 M6-B exige «repetibilidad y precisión intermedia» en B. En B1–B2 no aparece el término «precisión intermedia»; se introduce por primera vez en I5 («la precisión intermedia describe condiciones dentro de un laboratorio…»). El Nivel I da por visto algo que B no enseña. | En B1, tras la frase de repetibilidad, añadir 2–3 frases narradas: la precisión intermedia es la dispersión cuando cambian dentro del laboratorio factores como el día o el operador; citar [VIM; ISO 5725-3 §§5–6]; el día de la pizarra (D_d) es ese factor. En I5 dejar el marco ISO 5725 y la distinción con reproducibilidad. |
| R02 | Escena I2, «Puede ocurrir que MS_entre sea menor que MS_dentro…» y el EJEMPLO «(0,00653 − 0,01667)/4 = −0,00253» | Alcance (más de prop_e) | mayor | prop_e §5 M6-A asigna «componentes negativas y alternativas de estimación» al Nivel A. El libreto lo narra en I2 y lo repite en A2 («Cuando una componente estimada por momentos resulta negativa…»). La bitácora (Plan, punto 6) también ubica el caso negativo en I2, pero prop_e manda (guía, encabezado). | Trasladar los párrafos y el EJEMPLO de I2 a la Escena A2, al inicio. En I2 dejar el estimador por momentos y una frase: «si el estimador sale negativo, lo tratamos en A2». Actualizar el Plan de la bitácora. |
| R03 | Escena I2, «En un segundo conjunto simulado, también incluido en el script, el cuadrado medio entre días es 0,01583 y el cuadrado medio dentro es 0,01528…» | Reproducibilidad | mayor | El conjunto no está en `calc/M06_ejemplos.py`; el único conjunto de componentes cercanas a cero es 0,00653 / 0,01667. La aritmética (0,00014) es correcta, pero la frase afirma que el script lo incluye y no es así. Guía §6 exige que cada número se pueda reproducir. El párrafo además mezcla dos conjuntos en una frase. | Añadir el conjunto a `M06_ejemplos.py` con su salida, o eliminar la cifra. Partir la frase en dos y quitar «para ilustrar una negativa», que solo corresponde al EJEMPLO siguiente. |
| R04 | Escena I2, párrafo «También necesitamos decir cuánto confiamos en una componente estimada…» (≈290 palabras) | Redacción (oral) y referencias | menor | Un solo párrafo de ≈290 palabras, con cuatro ideas (IC chi-cuadrado, error estándar de τ̂², aproximación delta, alcance de AX.11). No se puede decir en voz alta. «No son intervalos de cobertura» contradice «intervalo de confianza» de la misma escena. [GUM G.4] no respalda el IC chi-cuadrado, y la aproximación delta no tiene referencia. | Dividir en 4–5 párrafos: (1) IC chi-cuadrado de σ²; (2) error estándar de τ̂²; (3) delta para s_entre; (4) advertencia sobre los grados de libertad del día. Sustituir «No son intervalos de cobertura» por «no son intervalos de confianza exactos para τ». Citar [AX.11] para el IC. Marcar la referencia del método delta como pendiente en la bitácora. |
| R05 | Escena A1, «El libro de datos apila tres campañas de calibración del Level 2… Las campañas identificadas en el expediente son las calibraciones 116/118 de enero de 2022, 142/143 de agosto de 2022 y 171/173 de febrero de 2023.» | Datos (origen) y descripción | mayor | La hoja BASE DE DATOS lista cinco pares: 83/85 (mayo 2021), 116/118, 142/143, 166/169 (diciembre 2022) y 171/173; su nota dice «4 calibraciones». Las hojas por nivel tienen tres bloques de seis días por analista (filas 6–23), sin etiqueta de campaña: la asignación bloque→campaña es inferencia. No se explica por qué se excluyen 83/85 y 166/169. Además 171 y 173 tienen la misma fecha (9 de febrero de 2023), y la nota dice que se hicieron en días diferentes. | Decir en el libreto qué hojas y bloques se usan y por qué (criterio de exclusión o motivo documentado). Sustituir «tres campañas» por «tres de las cinco calibraciones pareadas de la hoja BASE DE DATOS». Indicar la asignación de bloques como inferencia, en una acotación [NOTA AL INSTRUCTOR]. Confirmar con el responsable del libro antes de impartir. |
| R06 | Escena A1, «…destaca la campaña de agosto de 2022 del analista 2, con errores medios diarios cercanos a 0,73 y 0,83 nmol/mol, frente a valores del orden de 0,2 en las demás combinaciones.» | Número (descripción) | mayor | Según `M06_RR_CALAIRE.py`: en 405, las campañas del analista 1 dan 0,27 / 0,42 / 0,22 y las del analista 2, 0,25 / 0,73 / 0,13; en 455, 0,29 / 0,49 / 0,13 y 0,20 / 0,83 / 0,25. El resto de combinaciones va de 0,13 a 0,49, no «del orden de 0,2». Los valores 0,73 y 0,83 sí coinciden. | Sustituir por «frente a medias entre 0,13 y 0,49 nmol/mol en las demás combinaciones». |
| R07 | Escena A1, «La variación entre campañas crece al subir la concentración.» | Afirmación no sustentada | mayor | El script no calcula una variación entre campañas por nivel. Su único indicador, el cociente F de campaña, va así (45→455): 0,02; 1,70; 1,07; 1,27; 9,70; 1,30; 4,80; 0,94; 3,95; 5,95. No es monótono. | Reemplazar por lo que muestra el cálculo: «el cociente de campaña cambia de forma irregular entre niveles (de 0,02 a 9,7)». Si se quiere hablar de tendencia, calcularla en el script y citar la cifra. |
| R08 | Escena I3, `$y_{ijk}=\mu+A_i+D_j+(AD)_{ij}+\varepsilon_{ijk}$`; Escena A1, `$y_{ijk}=\mu+A_i+C_j+(AC)_{ij}+D_{k(ij)}$` y «la respuesta usada es un error medio por día» | Notación (convención §4) | mayor | Guía §4 y prop_e §3 fijan `y` = indicación y `e = y − x` = error con signo. En I1–I2 el modelo ya usa `e_dj`. En estos modelos `y` representa un error, así que el símbolo contradice la convención y chocará con M7, donde `y` es indicación. | Cambiar `y_{ijk}` por `e_{ijk}` en ambas fórmulas y en la pizarra de A1. En I3 o A1, mencionar una vez «error con signo e». |
| R09 | Escenas I1–I3 (pizarra y texto): `SS_D`, `SS_entre`, `MS_D`, `MS_E`, `MS_dentro`, `D_j`, `F_D`; «hay `a` días» | Notación (consistencia) | menor | Un mismo símbolo significa dos cosas: D es el factor 2 en I3 (D_j, MS_D, F_D), pero es el día en B1 (D_d), en I1 (SS_D, MS_D) y en I2 (MS_D). También se alternan SS_D/MS_E (pizarra) con SS_entre/MS_dentro (texto y ejemplo). `a` como número de días va contra prop_e §3, que define `d`. | Usar las mismas etiquetas en narración y pizarra (SS_entre/SS_dentro o SS_D/SS_E en todas partes). Renombrar el factor 2 de I3 (por ejemplo, P) y reservar D para el día. Usar `d` para el número de días. |
| R10 | Escena I5, «Una prueba t entre dos operadores responde a una pregunta sobre diferencia de medias… [Intro §9.3.4; ISO 5725-3 §8]» | Referencia no respaldada; alcance | mayor | Intro c09 §9.3.4 es «Gauge R&R Study (Random Effects Model)»; en el capítulo 9 no hay ninguna prueba t. ISO 5725-3 §8 trata la precisión intermedia, no esa prueba. La prueba t es contenido de M4 (prerrequisito), no de M6 según prop_e §5 M6, así que la frase añade un tema del Nivel I sin el marco que lo soporte. | Quitar la cita de Intro §9.3.4. Si se mantiene la frase, remitirla a M4 como prerrequisito y como contraste entre medias. Si no, reducirla a una frase de contraste sin referencia numeral. |
| R11 | Todo el capítulo: `[Intro §…]` y `[M&MU §4.4]`; «Referencias del capítulo» (líneas 232 y 238); Ficha, «Referencias clave» | Formato de referencias | menor | Guía §5 fija las claves «Crowder 2020» y «MMU». El libreto usa «Intro» y «M&MU», tanto en la narración como en la lista. | Renombrar a `[Crowder 2020 §9.3.1]` y `[MMU §4.4]` en todo el capítulo, incluida la lista y la ficha. |
| R12 | Escenas A1 («[prop_e §5 M6-A]», «[guía_libreto §6]»), I2 («[prop_e §5 M6-A]»), B2 y otras (33 ocurrencias en total de prop_e, guía_libreto o AX) | Formato de referencias y voz | menor | `prop_e` y `guia_libreto` son documentos internos del proyecto. No son fuentes que el alumno consulte y se leen en voz alta como ruido. Guía §5 solo pide claves bibliográficas; guía §3 pide remitir a los anexos con una frase del tipo «la deducción está en el Anexo AX.4». | Quitar `prop_e` y `guia_libreto` de los corchetes narrados. Si el instructor necesita el origen, ponerlo en una acotación [NOTA AL INSTRUCTOR] o en la bitácora. Mantener las referencias a AX.x en la forma de guía §3. |
| R13 | Escena B2, «Antes de calcular, declaramos la respuesta… unidad de repetición…» y cierre «Insisto en “parcial”…» | Convención prop_e §3 | menor | prop_e §3 pide declarar antes de calcular «respuesta, resultado de interés, unidad de repetición y escala temporal», y al cerrar, «resultado con unidades, interpretación estadística y acción». B2 declara respuesta y unidad, pero no la escala temporal. Cierra con interpretación, sin acción. | Añadir la escala temporal: «la escala es la campaña de seis días». Cerrar con una acción: «el informe declara U_prec como componente parcial y deja el presupuesto completo a M8». |
| R14 | Escena I2, «$E(MS_E)=\sigma^2$ y $E(MS_D)=\sigma^2+n\tau^2$ … [GUM H.5; Intro §9.3.1]» | Referencia imprecisa | menor | Intro §9.3.1 presenta el modelo de dos factores (Part/Oper) y la tabla 9.9 es de ese caso. La forma de un factor no aparece allí. La cita apoya el concepto, pero no estas esperanzas. | Citar [AX.4] para las esperanzas de un factor y, si se quiere, [Intro §9.3.1, tabla 9.9] como caso de dos factores. GUM H.5 existe (p. 98) y puede mantenerse. |
| R15 | Escena I3, «0,0833; 0,2800; 0,0533; y 0,0200»; «error de réplica» (I3) frente a «error de lectura» (B1, I2) | Puntuación y terminología | menor | Punto y coma antes de «y» en una lista sin subgrupos. «Error de réplica» y «error de lectura» designan el mismo ε sin aviso. | Escribir «0,0833, 0,2800, 0,0533 y 0,0200». Usar «error de lectura (ε)» y, en la primera aparición de I3, aclarar que es el error de réplica. |

Conteo: 0 críticos, 8 mayores (R01, R02, R03, R05, R06, R07, R08, R10), 7 menores (R04, R09, R11, R12, R13, R14, R15).

## Verificaciones hechas

**Cálculos (ejecución de `calc/M06_ejemplos.py` y `calc/M06_RR_CALAIRE.py` con `curso/.venv/bin/python`, sin errores).**

- **B2.** u²_prec = 0,0162 (nmol/mol)² ✓; u_prec = 0,1273 ✓; U_prec con k = 2 = 0,2546 ✓; sin componente entre días, 0,0346 ✓; s_medias = 0,3118 ✓, y s_medias/√6 = 0,1273 ✓.
- **I1.** SS_entre 0,56 ✓, SS_dentro 0,18 ✓, SS_total 0,74 ✓; g.l. 2, 9 y 11 ✓; MS 0,28 y 0,02 ✓; F = 14,0 ✓; cuantil 0,95 con (2, 9) = 4,256 → 4,26 ✓; medias diarias 0,00 / 0,50 / 0,10 ✓; media general 0,20 ✓.
- **I2.** τ̂² = 0,065 ✓; s_entre = 0,2550 ✓; s_r = 0,1414 ✓; IC chi-cuadrado 95 % de σ² = [0,00946; 0,06666] ✓; error estándar de τ̂² = 0,0700 ✓; delta para s_entre = 0,1374 ✓; caso negativo: (0,00653 − 0,01667)/4 = −0,00253 ✓.
- **I2, segundo conjunto (0,01583 y 0,01528).** Aritmética (0,00014) ✓; no está en el script ✗ (R03).
- **I3.** SS 0,0833 / 0,5600 / 0,1067 / 0,1200 ✓; g.l. 1 / 2 / 2 / 6 ✓; MS 0,0833 / 0,2800 / 0,0533 / 0,0200 ✓; F_A = 1,5625 → 1,56 ✓; F_D = 5,25 ✓; F_AD = 2,667 → 2,67 ✓; denominadores coherentes con el modelo aleatorio cruzado ✓.
- **I4.** C = 0,060 ... (0,027 / 0,060) = 0,45 ✓.
- **A1, estructura.** Diez niveles (45 a 455) ✓; F máximo de analista 1,2382 → 1,24 ✓; valor crítico de analista 18,5128 → 18,51 ✓; valor crítico de interacción 3,3158 → 3,32 ✓; niveles con interacción 135, 360, 405 y 455 ✓; F de interacción 6,61 / 4,31 / 6,47 / 5,07 ✓; desviación entre días 0,106–0,206 → «0,11 a 0,21» ✓; medias de analista 2 campaña 2 en 405 y 455 = 0,729 y 0,828 → 0,73 y 0,83 ✓; seis días por analista y campaña ✓.
- **A1, descripción.** «Del orden de 0,2 en las demás combinaciones» ✗ (R06); «la variación entre campañas crece» ✗ (R07).
- **A1, campañas.** Fechas de BASE DE DATOS: 116/118 = 14 y 20 de enero de 2022 ✓; 142/143 = 12 de agosto de 2022 ✓; 171/173 = 9 de febrero de 2023 ✓. La asignación bloque→campaña no es verificable desde las hojas ✗ (R05).

**Referencias (`docs/`, con `pdftotext`; más de cinco numerales comprobados).**

- **Intro c09 §§9.3.1–9.3.6.** Títulos verificados: 9.3.1 «Random Effects Models», 9.3.2 «Mixed Effects Models», 9.3.3 «Underlying ANOVA Assumptions», 9.3.4 «Gauge R&R Study (Random Effects Model)», 9.3.5 «Voltage Standard Uncertainty Analysis», 9.3.6 «Summary of ANOVA Method» ✓. Autores: Crowder, Delker, Forrest, Martin ✓ (portada). Tabla 9.9 es del caso de dos factores (R14). §9.3.4 no contiene prueba t (R10).
- **ISO 5725-3.** §§5–6 («Important factors», «Statistical model») ✓; §8 («Within-laboratory study and analysis of intermediate precision») ✓; §§9.3–9.5 («Nested experiment», «Fully-nested», «Staggered-nested») ✓.
- **ISO 5725-2.** §7.3.3 «Cochran's test» ✓ (el libreto no cita numeral; correcto según guía §5).
- **GUM.** G.4 «Effective degrees of freedom» ✓; H.5 «Analysis of variance» ✓ (índice, p. 98). G.4 no respalda el IC chi-cuadrado (R04).
- **M&MU.** §4.4 «Repeatability and Reproducibility» ✓; autores Rosario y Mendes ✓. Editorial y año no verificados.
- **Archivos.** Los archivos de `docs/` citados en la lista de referencias existen ✓ (intro c09, ISO 5725-1 a -4 y -6, GUM, M&MU, libro CALAIRE).

**Alcance (prop_e §5 M6, §6, §8).**

- **Nivel B.** Cubre la contribución de precisión, sus límites y el caso de medias diarias ✓. Falta precisión intermedia (R01).
- **Nivel I.** Cubre ANOVA de un factor, F, componentes y su incertidumbre, efectos fijos y aleatorios, dos factores con interacción, residuos, Cochran e ISO 5725 ✓. Añade componentes negativas (R02) y la prueba t (R10).
- **Nivel A.** Cubre analista × campaña con días anidados, denominadores, componentes negativas e ISO 5725 con sesgo ✓.
- **§6 exclusiones.** Búsqueda de GGMR, ISO 13528, PCR/PLS, Allan, Monte Carlo, bootstrap y KCRV: sin resultados ✓. «REML» aparece en A2 como alternativa de estimación; no está excluido.
- **Marcadores.** Están los tres marcadores de práctica (B, I y A) con título ✓; ninguna práctica está desarrollada ✓.

**Forma de libreto (guía §§1–2).**

- Estructura de §2 completa: ficha, niveles, escenas, marcadores, cierre y referencias ✓.
- Sin viñetas en contenido narrado ✓ (solo en la lista de referencias).
- Etiquetas de acotación dentro de las permitidas ✓.
- Coma decimal y unidades nmol/mol ✓ (sin puntos decimales en la prosa).
- Párrafos de más de 110 palabras: catorce, el mayor de ≈290 (R04).

## Resumen

El libreto está bien construido y casi todas las cifras reproducen. Los hallazgos graves se concentran en tres puntos.

1. **Alcance.** B no define «precisión intermedia» (R01), e I lleva contenido de A (componentes negativas, R02) y una prueba t sin marco (R10).
2. **Datos del caso CALAIRE.** La asignación de campañas y la descripción de la campaña de agosto de 2022 no son fieles al libro (R05, R06, R07). Antes de impartir, hay que confirmarla con el responsable del libro.
3. **Reproducibilidad y notación.** Un conjunto de datos citado no está en el script (R03) y la notación de los modelos contradice la convención de guía §4 (R08).

Los menores (R04, R09, R11–R15) son de redacción, de formato de referencias y de consistencia, y se corrigen sin cambiar el contenido. Ninguno es crítico.
