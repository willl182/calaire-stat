# Revisión de redacción y errores — M04 «Inferencia: estimación y contraste»

Revisor: Haiku. Objeto: `curso/S1_fundamentos/M04_libreto.md` (202 líneas). El libreto no se modificó.

## Plan de revisión

**Qué leí.** `curso/guia_libreto.md` completa (§§1–8), en la versión vigente tras un cambio posterior en disco (se añadió en §5 la regla sobre prop_e como referencia; la revisión la tiene en cuenta); `prop_e.md` §§1–3 (enfoque, niveles, convenciones), §4 (secuencia), §5 módulo M4 (líneas 100–111), §6 (inclusiones y exclusiones), §7 (casos, para comprobar que M4 no tiene familia de casos asignada), §8 (evaluación y errores críticos) y el módulo M3 de prop_e (prerrequisitos de M4); el libreto completo; `curso/S1_fundamentos/M04_bitacora_luna.md` (plan y ejecución); y `curso/S1_fundamentos/calc/M04_ejemplos.py`.

**Cómo lo revisé.**

- *a) Redacción.* Lectura completa en voz alta, frase a frase. Terminología (error estándar, unidad de repetición, nivel, ejemplo), coma decimal y unidades (§4), y frases largas.
- *b) Errores.* Ejecuté `curso/.venv/bin/python -I curso/S1_fundamentos/calc/M04_ejemplos.py` y comparé cada cifra del libreto con la salida, con el redondeo de la guía. Comprobé además los valores críticos de Grubbs y Dixon con las tablas de Otto, y las fórmulas de las PIZARRA (signos, n−1, χ², Welch, TOST, Bonferroni).
- *c) Formato.* Grep de acotaciones fuera de bloque de cita, etiquetas no permitidas, viñetas, decimales con punto y referencias internas en la narración. Estructura comparada con la plantilla de §2.
- *d) Referencias.* Con `pdftotext -layout` extraje a un directorio temporal (`/tmp/m04chk`, fuera del repositorio) el índice y el texto de `statistical_concepts_c05`…`c09`, `Chemometrics Statistics and Computer Application.pdf` (Otto) y `milton2006.pdf`. Verifiqué más de cinco numerales (detalle en «Verificaciones hechas»).
- *e) Alcance.* Comparé, nivel por nivel, el contenido narrado con prop_e §5 M4 y con §6; comprobé que las tres prácticas aparecen solo como marcador y que no hay marcadores ausentes.

## Hallazgos

| id | ubicación (escena · línea · texto citado) | tipo | severidad | problema | corrección propuesta |
|---|---|---|---|---|---|
| R01 | Escena B3 · l. 68 · «En el caso del Level 2 frente al SRP 55, prop_e pide estimar el intervalo…» | formato (narración) / contenido | mayor | Se nombra un documento de planificación (`prop_e`) dentro de la narración dirigida a los operadores, que no lo tienen. Es metatexto del curso, no explicación. Además, la guía §5 (l. 81, versión vigente) indica que citar prop_e solo justifica el alcance y no es referencia técnica. | Sustituir por: «En el caso del Level 2 frente al SRP 55, lo que estimamos es el intervalo del error medio en un nivel, y lo contrastamos con cero y con una magnitud relevante.» |
| R02 | Escena I1 · l. 90 y l. 94 · «[Statistical Concepts §7.1]» (en ambas) | referencia | mayor | El capítulo 7 de Statistical Concepts no trata Welch en §7.1 (ni en §7.2). Welch aparece en §7.3.1 (salida SPSS: fila «equal variances not assumed») y en §7.5.3 (código R «Independent t and Welch t′»). La cita apunta a una sección que no contiene la afirmación. | Cambiar a «[Statistical Concepts §7.3.1; §7.5.3]» en ambas líneas. |
| R03 | Escena A3 · l. 176 y l. 180 · «[Statistical Concepts §8.3.1]»; también la ficha, l. 14 · «…8.3.1…» | referencia | mayor | §8.3.1 del capítulo 8 es la prueba de bondad de ajuste χ² para conteos (categorías), no la suma de residuos estandarizados con incertidumbres conocidas ni la regla de grados de libertad. El numeral no sostiene la afirmación. Milton 2006 sí la sostiene. | Quitar «§8.3.1» de la l. 176 y de la l. 180, y citar «[Milton et al. 2006]» (prueba χ² con `p = m − n`, ec. (14), `docs/milton2006.pdf`). Quitar «8.3.1» de la ficha (l. 14). |
| R04 | Escena I4 · l. 126 y l. 130 · «[Statistical Concepts §§9.1–9.2]» | referencia | mayor | La aproximación `u(s) ≈ s/√(2ν)` no aparece en §§9.1–9.2 de Statistical Concepts (cap. 9 trata varianzas con chi-cuadrado y F, sin esa expresión). La cita es un numeral no verificado, que la guía §5 prohíbe. | Dejar la fórmula y citar «[Statistical Concepts, cap. 9, sin numeral]» o, mejor, buscar una fuente verificada; anotar el pendiente en la bitácora («fuente de la aproximación de u(s), no localizada en docs/»). |
| R05 | Escena A3 · l. 176 · «[Statistical Concepts §8.3.1; Milton et al. 2006, no disponible en docs/]» | referencia | mayor | Contradicción interna: Milton 2006 se marca «no disponible en docs/», pero la lista de referencias (l. 200) da `docs/milton2006.pdf` y el archivo existe. | Quitar «no disponible en docs/» de la l. 176 (el resto de la corrección está en R03). |
| R06 | Escena B1 · l. 22 · «[DIAPOSITIVA: una población de errores posibles, una muestra seleccionada y la media muestral que se calcula.]» | formato | menor | La acotación no va en bloque de cita, y usa «:» en lugar del formato de §1 (etiqueta en mayúsculas en bloque de cita). Es la única acotación con ese formato. | `> **[DIAPOSITIVA]** Una población de errores posibles, una muestra seleccionada y la media muestral que se calcula.` |
| R07 | Escena B3 · l. 60 · «…predeclarado en el cálculo docente…» | lenguaje | menor | «Cálculo docente» es jerga de la preparación, no algo que se diga a operadores. | «…con el nivel de significación del cinco por ciento que fijamos de antemano…» |
| R08 | Escenas B2, B3, I5, A2 · l. 34 «El script produce»; l. 46 «usado por el script»; l. 88 «El script obtiene»; l. 138 «el script genera»; l. 140 «se reproducen en el script»; l. 168 «calculado por el script» | lenguaje / formato | menor | Mencionar el script en la narración mezcla la explicación con la trazabilidad. La guía §6 pide que las cifras se reproduzcan con `calc/`, pero eso no es parte del discurso. | Eliminar «el script» de la narración («Los resultados son…», «Obtenemos…»). Añadir una vez por nivel una acotación `[NOTA AL INSTRUCTOR] Cifras reproducibles con calc/M04_ejemplos.py.` |
| R09 | Escena B3 · l. 62 · «La potencia es la probabilidad de detectar ese efecto definido… Sin especificar el efecto que importa no existe una única potencia del estudio.» | alcance | menor | La potencia y su dependencia del efecto son contenido de I («potencia y tamaño de muestra»); B solo incluye «errores de decisión». La guía §2 indica que cada nivel narra solo lo que añade. | Mantener la definición de error de tipo II y cerrar con «La potencia, es decir, la probabilidad de detectar un efecto, la veremos en el nivel I». |
| R10 | Encabezados · l. 78 «## Nivel I — elegir y justificar métodos de inferencia»; l. 146 «## Nivel A — conclusiones simultáneas, equivalencia y consistencia» | formato | menor | La plantilla de §2 pide «Nivel I — lo que se añade» y «Nivel A — lo que se añade». Los encabezados no lo indican. | Renombrar: «## Nivel I — lo que se añade: elegir y justificar métodos» y «## Nivel A — lo que se añade: conclusiones simultáneas, equivalencia y consistencia». |
| R11 | Escena B2 · PIZARRA l. 42 · `\bar e\ \pm\ t_{1-\alpha/2,\,\nu}\,\frac{s}{\sqrt n}` | notación | menor | Guía §4 fija `k = t(0,975; ν)` para el intervalo bilateral del 95 % con Student. El libreto usa α; el resultado es el mismo, pero se aparta de la convención. | `$\bar e\ \pm\ t_{0,975;\,\nu}\,\frac{s}{\sqrt n}$`, y en la frase: «para el 95 %, el cuantil t de 0,975 con ν grados de libertad». |
| R12 | Escena B2 · l. 40 · «el cociente entre la diferencia de la media observada y la media planteada, y el error estándar, sigue una distribución t» | redacción | menor | Frase larga y ambigua al oído; «el cociente entre … y el error estándar» no indica qué va dividido por qué. | «La diferencia entre la media observada y la planteada, dividida por el error estándar, sigue una distribución t.» |
| R13 | Escena I2 · l. 102 · «La estadística se basa en los grados de libertad multiplicados por la varianza muestral, divididos por la varianza que plantea la hipótesis.» | redacción | menor | «La estadística se basa en» es ambiguo: la fórmula es el estadístico χ², no la estadística en general. | «El estadístico es los grados de libertad por la varianza muestral, dividido por la varianza que plantea la hipótesis; se llama χ².» (Revisar la concordancia.) |
| R14 | Escena A3 · l. 176 · «Si hay covarianzas, la suma simple no es válida: usamos la matriz de covarianza completa y una forma cuadrática, con grados de libertad coherentes con el ajuste.» (y frase previa de ~70 palabras) | redacción | menor | Frase de unas 70 palabras con tres ideas (modelo, covarianza, grados de libertad). Difícil de decir en voz alta (guía §1). | Partir en tres: «Bajo residuos independientes normales, sumamos cuadrados estandarizados. Ese estadístico sigue una chi-cuadrado cuyos grados de libertad dependen de los residuos y de los parámetros estimados. Si hay covarianzas, la suma simple no vale: usamos la matriz completa y una forma cuadrática.» |
| R15 | Escena A3 · PIZARRA l. 178 · «Se lee: … o, con dependencia, «el residuo transpuesto por la inversa de su covarianza y por el residuo».» | redacción | menor | La lectura oral no nombra el vector ni la matriz; «el residuo transpuesto» es confuso. | «…o, con dependencia: el vector de residuos, transpuesto, multiplicado por la inversa de su matriz de covarianza y por el vector de residuos.» |
| R16 | B1 l. 50 «error medio de un solo nivel»; B3 l. 60 «error medio en un nivel»; Señales B l. 74 «se mezclan niveles»; A-l. 50 «…varios niveles de concentración» | terminología | menor | «Nivel» designa dos cosas: nivel de concentración (prop_e §5 M4, «en un nivel») y nivel del curso (B/I/A). En la narración se confunden. Además, los ejemplos se llaman «ilustrativo», «docente», «didáctico» y «simulado» de forma indistinta. | Usar «nivel de concentración» en la primera mención de cada escena y «nivel» solo para B/I/A. Fijar «ejemplo ilustrativo» (guía §1) y reservar «simulado» para el rótulo de origen (guía §4). |
| R17 | B2 l. 58 y B3 l. 24, l. 58, l. 60 · referencias al final de párrafo | referencia | menor | La guía §5 pide la referencia entre corchetes justo después del concepto, no al final del párrafo. Al final de párrafo el instructor no sabe a qué concepto corresponde. | Mover cada cita junto al concepto: p. ej. «El valor p [Statistical Concepts §6.1] es…» (l. 58). |
| R18 | Referencias · l. 196 · «Routledge, 2020» | referencia | menor | La edición (4.ª) y la editorial (Routledge) se confirman en el PDF; el año no se localizó en las páginas 1–20 de `docs/statistical_concepts_*`. | Mantener la editorial y la edición; quitar «2020» o confirmarlo en la página de créditos y anotarlo en la bitácora. |

## Verificaciones hechas

**Cálculos** (`curso/.venv/bin/python -I curso/S1_fundamentos/calc/M04_ejemplos.py`). Todas las cifras del libreto coinciden con la salida del script, dentro del redondeo.

| Lugar (línea) | Cifras del libreto | Script | Resultado |
|---|---|---|---|
| B (34–46, 60) | media 0,0375; s 0,5263; EE 0,1861; t 2,3646 con 7 gl; IC [−0,4025; 0,4775]; t 0,2015; p 0,8460 | 0,03750; 0,52627; 0,18607; 2,36462; [−0,40248; 0,47748]; 0,20154; 0,84601 | Coincide |
| I pareada (88) | media 0,1625; s 0,1188; EE 0,0420; IC [0,0632; 0,2618]; t 3,8697; p 0,0061 | 0,1625; 0,11877; 0,04199; [0,06320; 0,26180]; 3,86971; 0,006134 | Coincide |
| I Welch (94) | medias 10,0167 y 10,9571; dif. −0,9405; EE 0,1531; gl 10,9272; t −6,1418; p 0,000075; IC [−1,2778; −0,6032] | 10,01667; 10,95714; −0,94048; 0,15313; 10,9272; −6,14181; 7,50e-05; [−1,27778; −0,60317] | Coincide |
| I varianza (106) | s² 0,2770; IC [0,1211; 1,1473]; χ² 7,7550; p 0,7094 | 0,27696; [0,12108; 1,14728]; 7,755; 0,70939 | Coincide |
| I cociente F (110) | razón 0,8408; IC [0,1404; 5,8669]; p 0,8678 | 0,84080; [0,14043; 5,86688]; 0,86783 | Coincide |
| I potencia (120) | n 33,37 → 34; potencia 0,4649 (n=16); 25,52 → 26 por grupo; potencia 0,4658 (12 por grupo) | 33,3671; 0,46487; 25,5246; 0,46576 | Coincide |
| I u(s) (130) | 0,1407 | 0,140653 | Coincide |
| I Grubbs/Dixon (138) | G 2,4374 > 2,22; Q 0,8214 > 0,59 | G 2,43743; Q 0,82143; críticos fijados 2,22 y 0,59 | Coincide. Los críticos están fijados en el script; comprobados en Otto, Tabla 2.11 (n=8, T(0,99)=2,22) y Tabla 2.10 (n=8, Q(0,99)=0,59) |
| A Bonferroni (156) | α por prueba 0,0167; p ajustados 0,036; 0,093; 0,600 | 0,016667; [0,036; 0,093; 0,600] | Coincide |
| A TOST (168) | IC90 [−0,0747; 0,2347]; p inf. 0,00000163; p sup. 0,0000787; equivalencia | [−0,07466; 0,23466]; 1,629e-06; 7,871e-05; True | Coincide |
| A χ² (180) | Q 2,33; crítico 7,8147; p 0,5068 | 2,33; 7,81473; 0,50680 | Coincide |

Comprobaciones adicionales de fórmulas (sin discrepancias): PIZARRA de B2 y B3 (t y valor p bilateral); I1 (diferencias `A−B`, n−1 gl); I1 Welch (EE combinado; gl de Welch–Satterthwaite, AX.7); I2 (`χ² = (n−1)s²/σ₀²`, F con gl (n₁−1, n₂−1)); A1 (`min(mp, 1)`); A2 (TOST: intervalo del 90 % dentro de los márgenes; equivalencia con `p<0,05` en ambas colas); A3 (`Q = Σ(r/u)²`, gl = número de residuos cuando no hay parámetros ajustados).

**Referencias** (`pdftotext -layout` sobre `docs/`, extractos en `/tmp/m04chk`):

| Referencia del libreto | Qué comprobé en el PDF | Resultado |
|---|---|---|
| Statistical Concepts §5.2 (`statistical_concepts_c05.pdf`) | Índice: «5.2 Sampling and Estimation», con 5.2.1 y 5.2.2 | Confirmado |
| §6.1, §§6.1.2–6.1.5, §6.4 (`c06`) | Índice: 6.1 «Inferences About a Single Mean», 6.1.2 Sample Size, 6.1.3 Power, 6.1.4 Effect Size, 6.1.5 Assumptions; 6.4 Data Screening | Confirmado |
| §§7.1.4–7.1.7 y §§7.2.2–7.2.3 (`c07`) | Índice: 7.1.4–7.1.7 y 7.2.2–7.2.3 (muestra, potencia, efecto, supuestos) | Confirmado |
| §7.1 para Welch (`c07`) | §7.1 y §7.2 no mencionan Welch. Aparece en §7.3.1 (salida SPSS, «equal variances not assumed») y §7.5.3 (R) | **No confirmado** → R02 |
| §8.3.1 para la χ² de residuos (`c08`) | §8.3.1 = «The Chi-Square Goodness-of-Fit Test» (conteos) | **No confirmado** → R03 |
| §§9.1–9.3 (`c09`) | Índice: 9.1 Inferences About Variances; 9.2.1 Assumptions for a Single Variance; 9.3 Sample Size, Power, and Effect Size. Texto: χ² para una varianza y F (§9.1); sensibilidad a la normalidad | Confirmado |
| §§9.1–9.2 para `u(s) ≈ s/√(2ν)` (`c09`) | Búsqueda de la aproximación en el capítulo: no aparece | **No confirmado** → R04 |
| Otto §2.2 (Dixon, Grubbs) | Sección 2.2 «Statistical Tests» (pp. 28–43). Dixon's Q-Test y Grubbs's Test en pp. 42–43. Tabla 2.10 (n=8, Q(0,99)=0,59) y Tabla 2.11 (n=8, T(0,99)=2,22). Cita textual: «uncritical elimination of outliers may lead to wrong conclusions» | Confirmado |
| Otto, 3.ª ed., Wiley-VCH, 2017 | «Third Edition» y «© 2017 Wiley-VCH» en la portada | Confirmado |
| Milton et al. 2006 (`milton2006.pdf`) | Título: «Implementation of a generalized least-squares method…»; Metrologia 43 (2006) S291. Prueba χ² con `χ²(p)`, `p = m − n` grados de libertad (ec. (14)) | Confirmado (sin numeral en el libreto; ver R03 y R05) |
| Statistical Concepts, 4.ª ed., Routledge | «fourth edition» y «by Routledge» en las primeras páginas. Año no localizado | Editorial y edición confirmadas; año **no confirmado** → R18 |
| Lakens 2017; NIST/SEMATECH | Ausentes de `docs/` (no hay archivo) | Correcto como «no disponible en docs/» |
| Clave «Statistical Concepts» en el texto | Coincide con la usada en M02 (11 usos) y M03 (6 usos) | Consistente con el resto del curso |

**Alcance y formato.**

- Contenido por nivel frente a prop_e §5 M4: B, I y A incluyen todos los temas enumerados, con el mismo orden y sin temas añadidos. La única excepción es el concepto de potencia en B (R09).
- Exclusiones de prop_e §6: ninguna de las excluidas aparece (ISO 13528, Mandel, z/ζ, Allan).
- Prerrequisitos de la ficha: consistentes con prop_e M3 (t para M4-B; χ² y F para M4-I).
- Prácticas: hay tres marcadores `[PRÁCTICA — fase de ejercicios]` (líneas 70, 144, 186), con los títulos de prop_e; no hay prácticas desarrolladas ni marcadores ausentes.
- Ejemplos: todos rotulados como simulados o ilustrativos, con las cifras reproducibles (ver cálculos).
- Etiquetas de acotación: todas en el conjunto permitido (PIZARRA, EJEMPLO, PREGUNTA AL GRUPO, ERROR CRÍTICO, PRÁCTICA) salvo DIAPOSITIVA fuera de bloque (R06).
- Viñetas: solo en «Referencias del capítulo», permitidas por la guía.
- Decimales: coma en todo el texto y en LaTeX; no encontré cifras con punto decimal.
- Estructura: Ficha, Nivel B con escenas y señales, Nivel I, Nivel A, Cierre y Referencias. Solo fallan los encabezados de I y A (R10).

## Resumen

- Crítica: 0. Ningún cálculo, fórmula ni número del libreto falla al comprobarlo.
- Mayor: 5 (R01–R05). Tres son referencias que no sostienen la afirmación (R02, R03, R04); una es una contradicción sobre la disponibilidad de Milton (R05); y una es metatexto en la narración (R01).
- Menor: 13 (R06–R18). Son sobre todo formato de acotación, lenguaje de preparación, redacción y terminología.
- Prioridad de corrección: R02–R05 (referencias) y R01 antes que el resto. Después, R03 también afecta a la ficha (l. 14).
- La cita de Lakens y NIST sin numeral es correcta según la guía §5.
- Pendientes que no pude resolver aquí: la fuente de `u(s) ≈ s/√(2ν)` (R04) y el año de Statistical Concepts (R18).
