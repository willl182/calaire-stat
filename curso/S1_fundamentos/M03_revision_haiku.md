# Revisión de redacción y errores: M03 «Probabilidad, distribuciones y dependencia»

Revisor: Haiku. Libreto revisado: `curso/S1_fundamentos/M03_libreto.md` (no modificado).

## Plan de revisión

1. **Marco normativo.** Lectura de `curso/guia_libreto.md` completa (§1 a §8).
2. **Alcance.** Lectura de `prop_e.md`: §5 (módulo M3, líneas 89–100), §6 (inclusiones y exclusiones), §7 (casos), §8 (evaluación y errores críticos) y §9–§10 para la fase de preparación. Se cotejó cada tema de B, I y A con el texto del libreto, y se buscaron temas añadidos o ausentes.
3. **Redacción y formato.** Lectura completa del libreto (292 líneas). Se revisaron ortografía, puntuación, frases largas (con conteo de palabras por frase), coma decimal, unidades `nmol/mol`, notación (`s` frente a `σ`, `s_r`, `s_entre`, `τ`), etiquetas de acotación permitidas, ausencia de viñetas en contenido narrado, estructura de §2 (ficha, niveles, escenas, marcadores, señales de escalamiento, cierre, referencias) y lectura en voz alta de las fórmulas.
4. **Cálculos.** Se ejecutó `curso/S1_fundamentos/calc/M03_ejemplos.py` con `curso/.venv/bin/python -I` y se compararon todos los valores del libreto con la salida. Se recalcularon además los valores no presentes en el script (cuantiles de posición de gráfico de probabilidad y un ejemplo multipunto propuesto).
5. **Fuentes.** Se buscó en el repositorio cada valor atribuido a propuestas (`grep` sobre `prop_*.md`) y al certificado F-PSMT-01 (`openpyxl`). Se extrajo texto con `pdftotext` de los PDF de `docs/` citados en el libreto, y se comprobaron numerales, títulos, autores, editorial y año.
6. **Marcadores.** Se comprobó que cada práctica de prop_e (B, I, A) aparece como `[PRÁCTICA — fase de ejercicios]` con el título correcto y sin desarrollo, y que no hay prácticas desarrolladas.

No consulté `M03_bitacora_luna.md` ni otros módulos. Los numerales del capítulo 3 de MMU que cito como «título verificado» se comprobaron por su encabezado; el contenido de cada fórmula se leyó solo cuando aparece en el extracto (ver Verificaciones).

## Hallazgos

| id | Ubicación (escena y texto citado) | Tipo | Severidad | Problema | Corrección propuesta |
|---|---|---|---|---|---|
| R01 | Escena B1: «La probabilidad de que ocurra al menos uno de dos eventos se obtiene sumando las probabilidades y restando la probabilidad de que ambos ocurran a la vez» y `[EJEMPLO]` de «20 resultados igualmente posibles» (con pizarra `P(A∪B)=…`) | alcance / referencias | mayor | La regla de la unión no está en prop_e §5 M3 (ni en B, ni en I, ni en A). Guía §3 prohíbe añadir temas. Además la cita `[Statistical Concepts §5.1]` no la respalda: la sección 5.1 (verificada) es introductoria y no contiene esa regla. | Retirar el párrafo, la pizarra y el ejemplo de unión. Sustituir por un ejemplo discreto de variable aleatoria con números (p. ej., número de lecturas fuera de banda en cinco ciclos independientes, con valores posibles 0 a 5 y su probabilidad si se declara el modelo). Si se quiere conservar la regla, anotarla en la bitácora como prerrequisito no cubierto por prop_e. |
| R02 | Escena B2, `[EJEMPLO]` «Ejemplo adaptado de resolución: resolución total de 0,1 nmol/mol según el dato de referencia de prop_e M3»; Ficha, fila Datos: «valor indicado como especificación del analizador en prop_e» | rótulo de origen / fuente | mayor | prop_e no contiene 0,1 nmol/mol en M3 (búsqueda en `prop_e.md`: sin resultados). El valor aparece en `prop_b.md` (M3-B: «resolución del Level 2 (0,1 nmol/mol)») y en `prop_c.md` (M3: «0,1 nmol/mol del 49C»). No aparece en el certificado F-PSMT-01 (búsqueda de «resol» en el `.xlsm`). La atribución a prop_e es incorrecta y el rótulo queda sin fuente. | Citar la fuente real: «resolución de 0,1 nmol/mol citada en la propuesta B (M3-B)», rotulada como adaptada. En la Ficha, cambiar «especificación del analizador en prop_e» por esa fuente. Anotar en la bitácora que la resolución debe confirmarse con el manual del 49C o con el certificado antes de impartir. |
| R03 | Escena A1: «La propuesta del curso cita un ejemplo de razón de canales con desviación estándar 0,000012, frente a 0,000089» | fuente / referencias | mayor | Los valores están en `prop_b.md` (M3-A: «covarianza entre canales (0,000012 frente a 0,000089)»), no en prop_e. «La propuesta del curso» es inexacto. Además, guía §5 indica que prop_e no es referencia técnica: el número queda sin fuente técnica ni rótulo. | Eliminar la frase y dejar solo el ejemplo sintético. Si se conserva, citar la propuesta B como origen del número, rotularlo como adaptado, no atribuirlo a CALAIRE y anotarlo en la bitácora. |
| R04 | Escena B3: «Supongan que cada lectura independiente tiene desviación estándar s. Para el promedio de n lecturas independientes, la desviación estándar del promedio es s sobre raíz de n.» | notación | mayor | `s` es la estimación muestral (guía §4, prop_e §3), pero aquí designa la desviación del proceso. La pizarra siguiente usa `σ` para el proceso y `s/√n` para el estimado, y el texto lo aclara después («la desviación estándar del proceso, sigma»). La frase inicial contradice la convención. | «Supongan que cada lectura independiente tiene desviación estándar σ. Para el promedio de n lecturas independientes, la desviación estándar del promedio es σ sobre raíz de n.» Reservar `s/√n` para la estimación. |
| R05 | Escena B3, pizarra: «$\nu=n-1$ para una muestra independiente bajo el modelo de media normal con varianza común» | exactitud técnica | menor | «Varianza común» es el término de dos muestras agrupadas. Aquí la varianza es desconocida y se estima con una sola muestra. | «… bajo un modelo de media normal con varianza desconocida». |
| R06 | Escena I2: «F con dos grados de libertad es el cociente entre dos chi cuadrados, cada uno dividido por sus grados de libertad» | exactitud técnica | mayor | Una F depende de dos grados de libertad, ν₁ y ν₂, no de uno. La pizarra lo escribe bien (`F_{ν₁,ν₂}`), pero la narración lo dice mal. | «F con ν₁ y ν₂ grados de libertad es el cociente de dos chi cuadrados, cada uno dividido por su grado de libertad.» |
| R07 | Escena I2, gráficos de probabilidad («¿Cómo comprobamos si una distribución normal es una aproximación razonable…?») | contenido (guía §3) | menor | Tema cuantitativo sin ejemplo numérico. Solo hay una diapositiva conceptual. | Añadir `[EJEMPLO]`: cinco valores ordenados y los cuantiles normales de las posiciones (i − 0,5)/5: −1,282; −0,524; 0,000; 0,524; 1,282 (verificado, ver Verificaciones). |
| R08 | Escena A1, último párrafo: «En sistemas con varios puntos, un componente común puede generar covarianza entre todas las concentraciones…» | contenido (prop_e M3-A; guía §3) | mayor | prop_e exige «covarianzas comunes entre canales y puntos». Los puntos se tratan solo en forma abstracta (`u²(y)=cᵀVc`), sin ejemplo con números. | Añadir `[EJEMPLO]` simulado: dos puntos de 100 y 400 nmol/mol con un factor multiplicativo común de 1 % (desviación relativa). Resultados: incertidumbres 1,0 y 4,0 nmol/mol; covarianza 4,0 (nmol/mol)²; correlación 1; matriz V = [[1, 4], [4, 16]] (nmol/mol)²; diferencia con u = 3,0 frente a 4,1 bajo independencia. Verificado con `numpy`. |
| R09 | Escena A2: «Secuencia ilustrativa simulada con correlación de retardo uno 0,5, correspondiente a una estructura AR(1) conceptual» | terminología / alcance | menor | «AR(1)» no se define en el libreto y prop_e solo pide autocorrelación. | Quitar «AR(1)», o definirlo en una frase (cada valor depende en parte del anterior). |
| R10 | Todo el capítulo: `[Statistical Concepts §5.1]`, `[Metrology and Measurement Uncertainty §3.2.1]`, `[Introduction to Statistics in Metrology §7.4.1]`, etc. | referencias (guía §5) | menor | La guía fija como clave la de la tabla de §5 (Hahs-Vaughn, MMU, Crowder 2020). El libreto usa títulos abreviados, lo que no coincide con la tabla. | Sustituir por `[Hahs-Vaughn §5.1]`, `[MMU §3.2.1]`, `[Crowder 2020 §7.4.1]`, etc. Aplicar en todas las escenas y en la lista de referencias. |
| R11 | Ficha del capítulo, «Referencias clave»: «… NISTIR 6963» | referencias | menor | NISTIR 6963 no aparece en la narración ni en «Referencias del capítulo». La ficha y la lista no coinciden. | Quitar NISTIR 6963 de la ficha, o citarla donde se use (en M03 no se usa). |
| R12 | Escena B2, tras la pizarra `$u=U/k$`: «U es una cobertura reportada, no una segunda desviación estándar» | errores críticos (prop_e §8; guía §3) | mayor | prop_e §8 incluye «confundir u y U» entre los errores críticos. M03 introduce `u = U/k`, pero el libreto no tiene `[ERROR CRÍTICO]` sobre ello. | Añadir tras el párrafo: `> **[ERROR CRÍTICO]** «No confundan U con u. U es la incertidumbre expandida y u la estándar. Cambiar entre ambas sin declarar k da un resultado mal reportado.»` |
| R13 | Escena I3, pizarra `$X_{dj}=\mu+D_d+\varepsilon_{dj}$` con «desviación estándar dentro de una jornada» | notación (guía §4) | menor | Guía §4 y prop_e §3 fijan `σ` (`s_r`) y `τ` (`s_entre`) para estas dos escalas. El modelo no los nombra, y en M6 podría confundirse. | Añadir a la pizarra: `$\operatorname{sd}(D_d)=\tau$`, `$\operatorname{sd}(\varepsilon_{dj})=\sigma$`, y decir en voz alta que sus estimadores son `s_entre` y `s_r`. |
| R14 | Señales de escalamiento del nivel I: «Si el gráfico temporal muestra rachas, tendencia, ciclos o cambios…» y, en la pizarra de escalamiento, «autocorrelación aparente» | alcance | menor | La autocorrelación es contenido de A (escena A2). En I solo corresponde dependencia temporal. | Sustituir por «dependencia temporal aparente (rachas, tendencia, ciclos)» y dejar «autocorrelación» para el nivel A. |
| R15 | Escena I1, ejemplo: «Dos entradas simuladas con desviaciones estándar 0,8 y 0,6 unidades» y «La covarianza es 0,36 unidades al cuadrado» | unidades (guía §4) | menor | La guía fija `nmol/mol`. «Unidades» genéricas no cumple la convención en un ejemplo de la fase de contenido. | «0,8 y 0,6 nmol/mol», «covarianza de 0,36 (nmol/mol)²». Los números no cambian. |
| R16 | Nivel A, primer párrafo: «En esta formación se limita el trabajo avanzado a covarianzas cruzadas entre ejes nulas para la regresión GGMR» (y en la escalamiento A: «con la covarianza cruzada entre ejes nula») | claridad oral | menor | La frase es densa y difícil de oír. Mezcla «ejes nulos» y «covarianza nula». | Decir: «Para GGMR trabajaremos solo con covarianza cero entre ejes, V_xy = 0. El caso con V_xy distinto de cero queda fuera del curso.» Usar la misma formulación en la escalamiento A. |
| R17 | Escena B1, primera pizarra `$0 \leq P(A) \leq 1$, $P(\Omega)=1$`; Escena B3, pizarra `$u(\bar X)=\sigma/\sqrt{n}$` y `$s/\sqrt{n}$` | formato (guía §4: fórmulas leídas en voz alta) | menor | Ninguna de las dos fórmulas se lee en voz alta; la narración se refiere a ellas («La primera expresión…»). La primera de B1 pertenece a la regla de la unión (R01) y debería salir con ella. | Añadir «Leo: u de la media igual a sigma sobre raíz de n; con s estimada, s sobre raíz de n.» Si se aplica R01, eliminar la pizarra de B1. |
| R18 | Escena A1, pizarra de propagación y la lectura posterior: «Leo: la varianza de A sobre B es aproximadamente la varianza de A dividida por B al cuadrado, más A al cuadrado por la varianza de B dividida por B a la cuarta, menos dos A por la covarianza de A y B dividida por B al cubo.» | frases largas (oral) | menor | Frase de unas 50 palabras, difícil de decir y de seguir. | Dividir en tres frases: «Leo: la varianza de A sobre B. Es la varianza de A dividida por B al cuadrado, más…» (y así con cada término). |
| R19 | Escena A1: «la razón real entre canales incorpora covarianza»; Escena A2: «0,407; 0,750; y 1,843» | estilo | menor | «Razón real» es una expresión confusa para el lector. En la enumeración sobra el punto y coma antes de «y». | «La razón entre dos canales incorpora la covarianza.» Y «0,407; 0,750 y 1,843». |

**Resumen por severidad:** crítica 0, mayor 7 (R01, R02, R03, R04, R06, R08, R12), menor 12 (R05, R07, R09, R10, R11, R13, R14, R15, R16, R17, R18, R19).

## Verificaciones hechas

### Cálculos (`curso/S1_fundamentos/calc/M03_ejemplos.py`, ejecutado con `curso/.venv/bin/python -I`)

| Valor del libreto | Salida del script | Resultado |
|---|---|---|
| Rectangular, `h/√3`, h = 0,3 → «aproximadamente 0,173» | 0,1732050808 | Correcto |
| Resolución, `δ/√12`, δ = 0,1 → «aproximadamente 0,0289» | 0,02886751346 | Correcto |
| Triangular, `h/√6`, h = 0,3 → «aproximadamente 0,122» | 0,1224744871 | Correcto |
| `u = U/k`, U = 0,60, k = 2 → 0,30 | 0,3 | Correcto |
| Error estándar, s = 0,8, n = 16 → 0,20 | 0,2 | Correcto |
| Promedio con componente común (0,3) y ruido 0,8/√16 → «aproximadamente 0,361», «no puede bajar de 0,30» | 0,3605551275 | Correcto (0,3605 redondea a 0,361; cota inferior 0,30 correcta) |
| Covarianza 0,75 · 0,8 · 0,6 → 0,36 | 0,36 | Correcto |
| Suma independiente → 1,00; suma correlacionada → «aproximadamente 1,31» | 1; 1,311487705 | Correcto |
| Diferencia correlacionada → «aproximadamente 0,529» | 0,5291502622 | Correcto |
| Razón con correlación → «aproximadamente 0,00002795»; sin correlación → «0,00008839» | 2,795084972e-05; 8,838834765e-05 | Correcto. Fórmula de la pizarra `u²(A/B) ≈ u²(A)/B² + A²u²(B)/B⁴ − 2A·Cov/B³` comprobada por derivación: ∂R/∂A = 1/B, ∂R/∂B = −A/B² |
| Unión 3/20 + 5/20 − 1/20 = 0,35 | 0,35 | Aritmética correcta; el tema es fuera de alcance (R01) |
| z = (421,6 − 420,0)/0,8 = 2 | 2 | Correcto |
| t(0,975; 4) → «aproximadamente 2,776»; normal → «1,960» | 2,776445105; 1,959963985 | Correcto |
| χ² con normales 1 y −1 → 2; F = (6/3)/(4/2) → 1 | 2; 1 | Correcto |
| Matriz de correlación 3 × 3: simétrica; autovalores «0,407; 0,750; 1,843»; admisible | simétrica = True; 0,40692967; 0,75; 1,84307033; admisible = True | Correcto |
| Autocorrelación de retardo 1 = 0,5 | 0,5 | Correcto como valor ilustrativo (ver R09) |
| Cuantiles normales para (i − 0,5)/5 (propuesto en R07) | −1,2816; −0,5244; 0; 0,5244; 1,2816 | Calculado con `scipy` |
| Ejemplo multipunto (propuesto en R08): u = 1 y 4; Cov = 4; ρ = 1; u(suma) = 5,0; u(diferencia) = 3,0 | matriz [[1, 4], [4, 16]] | Calculado con `numpy` |

Nota: el script no imprime la «correlación 0,75 entre entradas con desviaciones 0,8 y 0,6» como valor separado, pero la covarianza y las sumas sí se calculan; no hay discrepancia.

### Referencias en `docs/` (extracción con `pdftotext`)

| Cita del libreto | Comprobación | Resultado |
|---|---|---|
| `[Statistical Concepts §5.1]` | `statistical_concepts_c05.pdf`: «5.1 Brief Introduction to Probability» | Sección existe, pero no contiene la regla de la unión (R01) |
| `[Statistical Concepts §4.1]` (normal) | `statistical_concepts_c04.pdf`: «4.1 The Normal Distribution and How It Works» | Sección existe y trata la normal |
| `[Statistical Concepts §§8.2 y 9.1.1]` (χ² y F) | `statistical_concepts_c08.pdf`: «8.2 … Chi-Square Distribution»; `statistical_concepts_c09.pdf`: «9.1.1 Characteristics of the F Distribution» | Correcto |
| `[Metrology and Measurement Uncertainty §3.2.1]` | `metrology_measure_uncer_c03.pdf`: «3.2.1 Random Variable, Random Experiment, and Sample» | Correcto |
| `[MMU §3.2.3]` (densidad) | «3.2.3 Probability Density Function (PDF)» | Correcto |
| `[MMU §3.2.4]` (media y desviación) | «3.2.4 Mean and Standard Deviation of a Probability Distribution» | Correcto |
| `[MMU §§3.2.5.1–3.2.5.2]` (rectangular y triangular) | «3.2.5.1 Rectangular or Uniform Distribution», «3.2.5.2 Symmetrical Triangular Distribution». En 3.2.5.2 (ec. 3.21): σ = (b − a)/√24 = h/√6 con h = (b − a)/2 | Triangular confirmada. La ecuación de la rectangular no se leyó en el extracto, pero el título coincide |
| `[MMU §3.2.5.5]` (t de Student) | «3.2.5.5 Student's T Distribution» | Título correcto (la sección contiene una simulación con N = 5) |
| `[Introduction to Statistics in Metrology §7.4.1]` (covarianza, correlación) | `intro_stats_metro_c07.pdf`: «7.4.1 Covariance, Correlation, and Effect on Uncertainty»; ec. (7.20) r = u(x_i, x_j)/(u(x_i)u(x_j)); rango de −1 a 1 | Correcto |
| `[Introduction to Statistics in Metrology §7.2]` | «7.2 Mathematical Basis» | Título correcto |
| `[Introduction to Statistics in Metrology §4.4.3]` (gráfico de probabilidad) | `intro_stats_metro_c04.pdf`: «4.4.3 Assessing Distributional Fit»: QQ plot, puntos aproximadamente lineales | Correcto. La cita del libreto se refiere al concepto, sin numeral en el texto narrado; no hay discrepancia |
| Lista: Hahs-Vaughn, D. L. y Lomax, R. G., 4.ª ed., Routledge, 2020 | Página de créditos del PDF: «Debbie L. Hahs-Vaughn … Richard G. Lomax»; «First published 2020 by Routledge»; prólogo: «fourth edition» | Correcto |
| Lista: Novellino do Rosario, P. P. y Mendes, A., Springer 2025 | «P. P. Novellino do Rosario, A. Mendes, Metrology and Measurement Uncertainty»; «© … 2025 Springer Nature Switzerland AG» | Correcto |
| Lista: Crowder, S., Delker, C., Forrest, E. y Martin, N., Springer 2020 | «Stephen Crowder, Collin Delker, Eric Forrest, Nevin Martin»; «© Springer Nature Switzerland AG 2020» | Correcto |
| `docs/JCGM_GUM-1.pdf`, `docs/JCGM_GUM_6_2020.pdf` | Archivos presentes; el libreto no da numerales (correcto según guía §5) | Sin numeral; pendiente en bitácora |
| NIST/SEMATECH e-Handbook | No está en `docs/`; el libreto lo marca como tal | Correcto |

### Formato y alcance (comprobaciones sobre el texto)

- **Viñetas en contenido narrado:** ninguna (`grep "^- "` y `grep "^\* "` sin resultados). Las tablas aparecen solo en la ficha.
- **Etiquetas de acotación:** solo se usan `[PIZARRA]`, `[DIAPOSITIVA]`, `[PREGUNTA AL GRUPO]`, `[EJEMPLO]`, `[ERROR CRÍTICO]` y `[ESCALAMIENTO]`, todas permitidas. Ninguna etiqueta no permitida.
- **Marcadores de práctica:** B, I y A aparecen cada uno una vez, con títulos que coinciden con prop_e §5 M3 (B: convertir especificaciones y comparar promedio con deriva; I: incertidumbre de una diferencia con y sin covarianza; A: matriz de covarianza y comparación de promediado). No hay práctica desarrollada.
- **Exclusiones (prop_e §6):** no aparecen Allan, PCR, PLS, ISO 13528, Mandel, KCDB ni `V_xy ≠ 0` desarrollado. Solo se mencionan como exclusiones explícitas (sin desarrollo).
- **Coma decimal y nmol/mol:** no se encontraron puntos decimales en la prosa. Las unidades genéricas aparecen en el ejemplo de covarianza de I1 (R15).
- **Estructura de la guía §2:** ficha, nivel B (escenas B1–B3, marcador, señales), nivel I (escenas I1–I3, marcador, señales), nivel A (escenas A1–A2, marcador, señales), cierre y referencias. Correcta.
- **Frases largas:** una frase de más de 45 palabras (R18); el resto son aceptables en voz alta.
- **Ortografía y gramática:** no se hallaron errores ortográficos. Se corrigieron como observaciones de estilo solo R05, R15, R16 y R19.
- **Cobertura de prop_e M3:** todos los temas de B, I y A están presentes. Se añadió la regla de la unión (R01), que está fuera de prop_e. Falta un ejemplo numérico para covarianzas entre puntos (R08) y para gráficos de probabilidad (R07).

## Resumen

El libreto de M03 es, en lo esencial, correcto: todos los cálculos numéricos reproducen los valores del script, los numerales de referencia que se comprobaron existen en `docs/`, y la estructura y los marcadores siguen la guía. Quedan 19 hallazgos: 0 críticos, 7 mayores y 12 menores.

Los mayores son:

- Una regla de probabilidad fuera de alcance, con una cita que no la respalda (R01).
- Dos valores atribuidos a fuentes que no los contienen: la resolución de 0,1 nmol/mol y la razón de canales (R02, R03).
- Una notación contradictoria en la desviación del promedio (R04).
- Una definición de la F dicha de forma incorrecta (R06).
- Un tema sin ejemplo numérico (covarianzas entre puntos, R08).
- Un error crítico de prop_e §8 (confundir u y U) sin marcar (R12).

Antes de cerrar el libreto conviene confirmar la resolución del 49C (R02) con el manual o el certificado. Las demás correcciones son textuales y se pueden aplicar en una sola pasada.
