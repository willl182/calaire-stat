# Revisión de redacción y errores: M02, Estadística descriptiva y elección de la respuesta

Revisor: Haiku. Objeto: `curso/S1_fundamentos/M02_libreto.md` (sin modificar). Fecha: 24 de octubre de 2026.

## Plan de revisión

**Qué leí.** La guía `curso/guia_libreto.md` completa (§1–§8); `prop_e.md` en su encabezado (§1–§4, para las convenciones), en M2 (§5), y en §6, §7, §8 y §10; el libreto M02 completo; `curso/S1_fundamentos/M02_bitacora_luna.md` (para ver qué queda marcado como pendiente) y `curso/S1_fundamentos/calc/M02_examples.py`.

**Cómo lo revisé.**

- **a) Redacción.** Lectura completa en orden. Búsquedas con `grep` de decimales con punto, palabras sin tilde frecuentes, viñetas en la narración y etiquetas de acotación fuera de la lista permitida. Comparé los encabezados con los de M00, M01, M03 y M04.
- **b) Errores.** Ejecuté `curso/.venv/bin/python -I curso/S1_fundamentos/calc/M02_examples.py` y comparé cada cifra del libreto con la salida. Recalculé a mano las cifras que dependen del redondeo. Revisé la notación, los signos y los conjuntos de datos (todos rotulados como simulados).
- **c) Formato libreto.** Estructura de §2 (ficha, niveles con escenas, señales, cierre, referencias), etiquetas de §1, marcadores de práctica (uno por nivel, sin desarrollar), y que cada nivel narre lo que añade y diga qué da por visto.
- **d) Referencias.** Cada cita entre corchetes la comparé con el PDF correspondiente en `docs/` usando `pdftotext` (con `-layout` cuando hizo falta). Para los numerales que no aparecían en el texto, busqué el término clave en el documento completo y en otros documentos de `docs/`.
- **e) Alcance.** Cotejé cada subpunto de prop_e M2 (B, I, A) y cada señal de escalamiento de §2 con el texto. Comprobé que no aparezcan los temas excluidos de §6.

## Hallazgos

| id | Ubicación (escena, línea y texto citado) | Tipo | Severidad | Problema | Corrección propuesta |
|---|---|---|---|---|---|
| R01 | Ficha, «Referencias clave» (L14): «Numerales comprobados en los archivos indicados al final». | Referencia (afirmación de verificación) | mayor | La frase afirma que los numerales están comprobados. No lo están: CV y MAD no se localizan (R02, R03); §4.3 de Crowder no trata lo que se le atribuye (R04, R06); §5.2 no contiene la fórmula de s/√n (R05). La bitácora sí los marca como pendientes. | Sustituir por: «Numerales localizados en los PDF: Statistical Concepts §§2.1–2.3 y 3.2.2–3.3; Crowder §4.3; MMU §3.1.1. CV y MAD sin numeral (pendiente, ver bitácora).» |
| R02 | Escena B4, párrafo del CV (L70): «[Statistical Concepts, cap. 3; ubicación específica pendiente]». | Referencia no soportada; nota de trabajo en la narración | crítica | El CV no aparece en los capítulos 1–6 de Statistical Concepts que hay en `docs/` (búsqueda de «coefficient of variation»). La nota «ubicación específica pendiente» es un apunte interno que se diría en voz alta. El término sí aparece en The ASQ Metrology Handbook (PDF p. ~606: «coefficient of variation — the standard deviation divided by…»). | Citar The ASQ Metrology Handbook (`docs/asq_metrological_handbook_c*.pdf`) tras identificar el capítulo que contiene la p. ~606 y su numeral. Quitar «ubicación específica pendiente» de la narración. Mientras tanto, citar sin numeral en las referencias y dejar el pendiente en la bitácora. |
| R03 | Escena I1, párrafo de la MAD (L114): «[Introduction to Statistics in Metrology, cap. 4; ubicación específica pendiente]». | Referencia no soportada; nota de trabajo en la narración | crítica | La MAD no aparece en el texto completo de Crowder (búsqueda de «absolute deviation» y «MAD»). Tampoco aparece en Statistical Concepts, MMU, ASQ ni Chemometrics de `docs/`. Atribuir la definición a Crowder cap. 4 es una atribución falsa que se diría como cita. | Quitar la cita a Crowder y la nota. Citar la MAD como fuente externa marcada: «NIST/SEMATECH e-Handbook of Statistical Methods (no disponible en docs/)», sin numeral, como permite §5. Registrar el pendiente en la bitácora. |
| R04 | Escena B4, párrafo de las indicaciones negativas (L74): «truncarla altera media, dispersión y forma de la distribución. [Introduction to Statistics in Metrology §4.3]». | Referencia no soportada | mayor | §4.3 de Crowder trata la exploración de datos, los atípicos y las tendencias. No trata lecturas negativas ni truncamiento (búsqueda de «negative» y «truncat» en el capítulo 4). | Quitar la cita de este párrafo. Añadir un ejemplo numérico con un conjunto que contenga −0,2 frente al mismo conjunto con 0, calculado en `M02_examples.py`. Citar una fuente solo si se localiza su numeral. |
| R05 | Escena B3, párrafo del error estándar (L56): «el error estándar se calcula como $s/\sqrt{n}$ … [Statistical Concepts §5.2]». | Referencia que no contiene la fórmula | mayor | §5.2 de Statistical Concepts («Sampling and Estimation») trata la distribución muestral de la media. La fórmula $s/\sqrt{n}$ no aparece en su texto; «standard error» solo figura en el índice del capítulo y en un ejercicio. La cita respalda el concepto, no la fórmula. | Para la fórmula, citar **[GUM 4.2.3]**: ecuación (5), $s^2(\bar q)=s^2(q_k)/n$, verificada en `docs/ISO_IEC Guide 98-3_2008 … (GUM_1995) - libgen.li.pdf`. Mantener **[Statistical Concepts §5.2]** solo para la idea de distribución muestral del promedio. |
| R06 | Escena A1, párrafo del valor influyente (L156): «…[Introduction to Statistics in Metrology §4.3]». | Referencia no soportada | mayor | §4.3 de Crowder habla de valores atípicos, pero no define «observación influyente» (la palabra «influential» no aparece). Las cifras sí son aritmética verificada. | Citar **[Crowder 2020 §4.3]** solo para «valores atípicos», que ya se usa en B5. Para la definición de observación influyente, citar una fuente externa marcada «(no disponible en docs/)», sin numeral. |
| R07 | Escena I2, párrafo del modelo y de la predicción (L124 y L128): «Esta es una forma de expresar el modelo lineal… [prop_e §5, M2]» y «Al ajustar descriptivamente una recta con mínimos cuadrados ordinarios». | Referencia inadecuada: prop_e como única fuente técnica | mayor | Según §5, prop_e solo justifica el alcance y no es referencia técnica. La recta de calibración y el ajuste OLS no tienen fuente técnica en el texto. ISO/TS 28037 trata la recta de calibración, $Y = A + BX$ (§5), y el ajuste OLS (§5.8) (numeral leído en el índice del PDF; confirmar en el cuerpo). | Añadir **[ISO 28037 §5]** para la recta de calibración y **[ISO 28037 §5.8]** para el ajuste OLS. Dejar **[prop_e §5, M2]** solo para el alcance. |
| R08 | Escena A1, párrafo de signo y magnitud (L146): «…[prop_e §5, M2]». Defiende el error con signo, \|e\| y la media de magnitudes. | Definición sin fuente técnica | mayor | Las definiciones de error con signo, de $|e|$ y de media de magnitudes no tienen fuente técnica. La búsqueda de «absolute deviation» en Statistical Concepts c03 no da resultados. | Citar como fuente externa marcada «(no disponible en docs/)», sin numeral. Si tras buscar en `docs/` se halla un numeral para la media de magnitudes, citarlo; prop_e queda solo para el alcance. |
| R09 | Escena B5, párrafo de redondeo (L88) y pizarra (L90): «Mantengan suficiente precisión durante las operaciones y redondeen una sola vez al final…». | Falta un ejemplo ilustrativo | mayor | El redondeo es un tema cuantitativo de B. §3 exige un ejemplo resuelto con números, y aquí solo hay narración. | Añadir un ejemplo con los seis errores de B4 (0,2; 0,1; −0,1; 0,1; 0,3; 0,1 nmol/mol). Redondeados a enteros antes de promediar, todos dan 0 y la media es 0. Sin redondear, la media es 0,117 nmol/mol (0,11667). Añadir la línea correspondiente a `M02_examples.py`. |
| R10 | Escena B3, párrafo de dispersión (L52): «pero uno concentrarse cerca del centro y el otro distribuirse ampliamente entre los extremos». | Sintaxis | menor | Dos infinitivos sin sujeto concordado; la frase no es correcta. | «…pero en uno los valores se concentren cerca del centro y en el otro se distribuyan ampliamente entre los extremos». |
| R11 | Escena B3, fórmula de la varianza (L52): $s^2=\frac{1}{n-1}\sum_{i=1}^{n}(z_i-\bar{z})^2$. | Notación no definida | menor | $z_i$ no se define en el capítulo; el resto del libreto usa $y$ para la indicación. | Cambiar a $y_i$ y $\bar{y}$, o añadir «z es una variable genérica». |
| R12 | Escena B5 (L80): «Un histograma puede resumir la distribución sin saber en qué orden aparecieron los datos; una serie temporal conserva ese orden y permite que el instructor pregunte…». Escena A1 (L160): «La sensibilidad se estudia comparando conclusiones bajo transformaciones o agregaciones justificadas…». | Frases largas (§1: ritmo oral) | menor | Son frases de más de 40 palabras que resultan difíciles de decir en voz alta. | Dividir cada una en dos o tres frases cortas, por ejemplo: «Un histograma no conserva el orden. La serie temporal sí. Así el instructor puede preguntar si la estructura parece aleatoria». |
| R13 | Escena B4, párrafos del CV (L70 y L72). | Redundancia | menor | L72 repite lo que L70 ya dijo: el CV es inestable cerca de cero y no es una medida universal. | Fundir ambos párrafos en uno, conservando la regla «antes de calcular un CV, pregunten si el denominador es interpretable» y la indicación de usar nmol/mol cerca de cero. Al hacerlo, aplicar la corrección de R02. |
| R14 | Citas en la narración: «[Statistical Concepts §3.3]» (L52, L64), «[Introduction to Statistics in Metrology §4.3]» (8 veces), «[Metrology and Measurement Uncertainty §3.1.1]» (L88). | Formato de referencias (§5: clave y ubicación) | menor | Las citas de la narración usan el título completo, no la clave de la tabla de §5 (Hahs-Vaughn, Crowder 2020, MMU). Son 18 ocurrencias. | Cambiar a **[Hahs-Vaughn §3.3]**, **[Crowder 2020 §4.3]**, **[MMU §3.1.1]**. |
| R15 | Escena B3 (L56) y Escena I2 (L124–L126): «el error estándar se calcula como $s/\sqrt{n}$»; «$\hat e(x)=\hat a+(\hat b-1)x$ se escribe». | Fórmulas no leídas en voz alta (§4) | menor | §4 exige que cada fórmula se lea en voz alta en la narración. Estas fórmulas se escriben, pero no se dicen en palabras. | Después de cada una, decir: «el error estándar es s dividida por la raíz cuadrada de n» y «el error predicho es a estimada, más b estimada menos uno, por x». |

Los marcadores de práctica (B, I y A) están presentes y no están desarrollados, en el formato de §2. No los incluyo como hallazgos.

## Verificaciones hechas

**Cálculos** (salida de `curso/.venv/bin/python -I curso/S1_fundamentos/calc/M02_examples.py`, comparada con el libreto):

| Cifra del libreto | Resultado del cálculo | Estado |
|---|---|---|
| Ocho lecturas: media y mediana 100,15 | 100,15 y 100,15 | correcto |
| Varianza 0,0600; desviación estándar 0,245 (0,24495) | 0,060000; 0,244949 | correcto |
| Rango 0,7 | 0,7 | correcto |
| $Q_1=99{,}975$, $Q_3=100{,}325$, IQR 0,350 | 99,975; 100,325; 0,350 | correcto (método lineal) |
| Error estándar 0,08660 | 0,086603 | correcto |
| Histograma: conteos 2, 3, 3; frecuencias relativas 0,25; 0,375; 0,375 | [2, 3, 3]; [0,25; 0,375; 0,375] | correcto |
| CV 0,2446 % | 0,24458 % (recalculado a mano: 100 × 0,24495 / 100,15 = 0,24458) | correcto |
| Seis pares: $s(y)=154{,}27$ nmol/mol | 154,2665 | correcto |
| Errores 0,2; 0,1; −0,1; 0,1; 0,3; 0,1; $s(e)=0{,}133$ | iguales; 0,132916 | correcto |
| Medias por día 0,15; 0,00; 0,20; desviaciones 0,071; 0,141; 0,141 | 0,15; 0,0; 0,2; 0,0707; 0,1414; 0,1414 | correcto |
| MAD de cinco valores: mediana 0,2, MAD 0,1 | 0,2; 0,1 | correcto |
| Ajuste: intercepto 0,080; pendiente 0,002075; $\hat b=1{,}002075$ | 0,080000; 0,002075; 1,002075 | correcto |
| Predichos 0,246; 0,412; 0,578; 0,744; 0,910 | 0,246; 0,412; 0,578; 0,744; 0,910 | correcto |
| Grupos ±0,4: media firmada ±0,4, media de magnitudes 0,4; combinado: media 0, $|\text{media}(e)|=0$ | iguales | correcto |
| Con +1,8: media 0,2; media de magnitudes 0,556; $s$ 0,725 (y 0,434 sin él); mediana 0,3; MAD 0,6 | 0,2; 0,5556; 0,72457 (0,43425); 0,3; 0,6 | correcto |
| Propuesta R09: media de los errores 0,117; redondeo a enteros da media 0 | 0,11667; todos los redondeos dan 0 | comprobado a mano; aún no está en el script |

Números del libreto que no encontré: ninguno. Todo número del libreto que sale del script coincide con su salida.

**Referencias** (verificadas en `docs/` con `pdftotext`):

| Cita del libreto | Verificación | Resultado |
|---|---|---|
| Statistical Concepts §§2.1–2.2 (distribuciones, histograma) | Índice de `statistical_concepts_c02.pdf`: 2.1 Tabular Display; 2.2 Graphical Display, 2.2.2 Histogram | correcta |
| Statistical Concepts §2.3 (cuantiles, caja) | Índice c02: 2.3 Percentiles; 2.3.2 Quartiles; 2.3.4 Box-and-Whisker Plot | correcta |
| Statistical Concepts §§3.2.2–3.2.3 (mediana, media) | Índice de `statistical_concepts_c03.pdf`: 3.2.2 The Median; 3.2.3 The Mean | correcta |
| Statistical Concepts §3.3 (dispersión, rango) | Índice c03: 3.3 Measures of Dispersion; 3.3.1 The Range | correcta |
| Statistical Concepts §5.2 (error estándar) | Índice c05: 5.2 Sampling and Estimation. La fórmula s/√n no está en el texto | **no respalda la fórmula** (R05) |
| Statistical Concepts, cap. 3 (CV) | Búsqueda de «coefficient of variation» en c01–c06: sin resultados | **no encontrada** (R02) |
| Crowder cap. 4 §4.3 (exploración de datos, gráficos, atípicos) | Índice de `intro_stats_metro_c04.pdf`: 4.3 Exploratory Data Analysis; 4.3.1 y 4.3.2. Texto sobre atípicos y tendencias (líneas 83–85, 176, 197) | correcta para B5 |
| Crowder cap. 4 (MAD) | Búsqueda en el libro completo: «absolute deviation», «MAD» sin resultados | **no encontrada** (R03) |
| Crowder §4.3 para influencia y truncamiento | Búsqueda de «influential» y de «negative» y «truncat» en el capítulo 4 | **no respalda** (R04, R06) |
| MMU §3.1.1 (redondeo) | TOC de `metrology_measure_uncer_c03.pdf`: 3.1.1 Number Rounding. Texto: mantener los resultados sin redondeo intermedio | correcta |
| GUM 4.2.3, ecuación (5) (media) | `ISO_IEC Guide 98-3_2008…GUM_1995`: «The best estimate of σ²(q̄) = σ²/n … s²(q̄) = s²(q_k)/n (5)» | correcta (propuesta R05) |
| ISO/TS 28037 §5, §5.8 (recta, OLS) | Índice de `ISO 28037.pdf`: 5 Principles of straight-line calibration; 5.8 Determining the OLS best-fit straight line. Texto: «Y = A + BX» | numerales leídos en el índice (propuesta R07); el cuerpo no se verificó |
| The ASQ Metrology Handbook (CV) | Término en la p. ~606 del PDF completo | hallazgo localizado; capítulo no identificado (R02) |
| Ediciones y editoriales | Statistical Concepts: 4.ª ed., Routledge, © 2020 Taylor & Francis. Crowder et al.: Springer Nature Switzerland AG, 2020. MMU: Novellino do Rosario y Mendes, Springer Nature Switzerland AG, 2025 | correctas |
| Archivos de `docs/` citados en la lista | Todos los archivos citados existen | correctos |
| prop_e en las referencias (L183) | Está declarado como fuente curricular, no técnica | correcto |

**Formato y alcance:**

- Etiquetas de acotación: todas están en la lista permitida de §1. No hay viñetas en la narración.
- Cifras: no hay decimales con punto en la narración ni en las fórmulas.
- Tildes: en las palabras revisadas no hay errores.
- Estructura de §2: ficha; niveles B, I y A con escenas numeradas; señales de escalamiento solo en B; cierre con transición a M3; referencias del capítulo. Los encabezados de nivel siguen el patrón de M00, M01, M03 y M04.
- Marcadores: uno por nivel, en el lugar que indica prop_e M2 (B, I y A). No hay práctica desarrollada.
- Nivel B: cubre todo lo que prop_e M2 asigna a B, y también las señales de §2 (dependencia, cambio de escala, atípico sin causa, residuos con estructura, incertidumbre en ambos ejes, pocos grados de libertad y límite).
- Nivel I: cubre los resúmenes dentro y entre grupos, la mediana y la MAD, el modelo del error y la tendencia con x.
- Nivel A: cubre la sensibilidad a transformaciones, agregaciones y observaciones influyentes.
- Exclusiones de §6: no aparece ningún tema excluido. Las referencias a M6, M7, M11 y M12-B son solo punteros.
- No hay un contenido de §7 o §8 (evidencias, rúbricas) desarrollado en el libreto, como corresponde a esta fase.

## Resumen

Revisión de M02 con 15 hallazgos: 2 críticos, 7 mayores y 6 menores.

- **Críticos (2):** R02 (CV) y R03 (MAD) están atribuidos a capítulos de Statistical Concepts y Crowder que no contienen esos contenidos. Las notas de pendiente aparecen en la narración.
- **Mayores (7):** R01 (la ficha afirma numerales comprobados que no lo están), R04 y R06 (citas a Crowder §4.3 para afirmaciones que no trata), R05 (cita a §5.2 para una fórmula que no contiene), R07 y R08 (prop_e usada como referencia técnica), R09 (redondeo sin ejemplo numérico).
- **Menores (6):** R10 (sintaxis), R11 (notación $z_i$), R12 (frases largas), R13 (redundancia en el CV), R14 (citas con título en lugar de clave), R15 (fórmulas no leídas en voz alta).

Las cifras del libreto son correctas en todos los casos comprobados. Las etiquetas, la estructura y el alcance por nivel cumplen con la guía y con prop_e. Lo que requiere corrección es la parte de referencias. No edité el libreto.
