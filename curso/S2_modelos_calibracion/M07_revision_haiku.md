# Revisión Haiku de M07 «Regresión y calibración inversa»

Revisor: Haiku 5.5 (redacción y errores). Libreto revisado: `curso/S2_modelos_calibracion/M07_libreto.md`. No se editó el libreto.

## Plan de revisión

**Qué se leyó.** `curso/guia_libreto.md` completa (§§1–8); `prop_e.md` §2 (señales del básico), §3 (convenciones), §5 módulo M7 (B, I, A y sus prácticas), §6 (exclusiones), §8 (errores críticos y evidencias) y §9 (anexos); el libreto completo (235 líneas); la bitácora `M07_bitacora_luna.md`; el script `calc/M07_ejemplos.py`.

**Cómo se revisó.**

1. **Cálculos.** Se ejecutó `curso/.venv/bin/python calc/M07_ejemplos.py` (salida sin errores; solo avisos de `sys.prefix` por la ruta relativa del intérprete) y se cotejó cada cifra narrada en el libreto con la salida impresa. Se recalculó a mano la semiamplitud de la media en `x₀ = 250` (`u²(ŷ₀) = u²(a) + x₀²u²(b) + 2x₀cov(a,b)`) y la fórmula inversa de la pizarra de I1 (derivadas parciales respecto de `y`, `a` y `b`).
2. **Referencias.** Se extrajo con `pdftotext` el texto de `docs/intro_stats_metro_c10.pdf`, `docs/ISO 28037.pdf`, `docs/ISO 6143 2001.pdf` y `docs/statistical_concepts_c10.pdf`; se localizó la página PDF de cada numeral citado y se comprobaron los autores y ediciones en la portada de los libros.
3. **Datos de ejemplo.** Se leyó la hoja `BD_DIAS` de `docs/F-PSMT-01 …xlsm` para comprobar el diseño que el libreto describe.
4. **Redacción y formato.** Lectura completa en voz alta (mentalmente): frases, puntuación, tratamiento de la persona gramatical, uso de coma decimal y unidades, viñetas en contenido narrado, etiquetas de acotación permitidas, orden de secciones de la guía §2.
5. **Alcance.** Cotejo de cada punto de prop_e §5 M7 (B, I, A) contra las escenas; exclusiones de §6; marcadores de práctica de los tres niveles.

## Hallazgos

| id | ubicación (escena y texto citado) | tipo | severidad | problema | corrección propuesta |
|---|---|---|---|---|---|
| R01 | Escena I1, párrafo «También podemos someter una correlación…»: «[Statistical Concepts §10.1, PDF pp. 2–7; script …]». Ficha, fila «Referencias clave»: «Statistical Concepts, cap. 10». | referencia | mayor | §10.1 de ese PDF (pp. 1–2) es introductorio (definiciones, potencia, tamaño de efecto, supuestos). La prueba de significancia de Pearson con `t` aparece en §10.2.1 (SPSS, pp. 3–5). El cap. 10 trata solo asociación bivariada; no cubre regresión, por lo que no es referencia para M7 como está en la ficha. La fórmula `t = r√(n−2)/√(1−r²)` no aparece en el capítulo. | Citar «[Statistical Concepts §10.2.1, PDF pp. 3–5]» para la interpretación de la prueba, y marcar la fórmula como de fuente no verificada en `docs/` (pendiente) o citar un numeral que se compruebe. En la ficha, indicar que el cap. 10 cubre solo asociación bivariada y quitarlo de «referencias clave» para regresión. |
| R02 | Escena I4: «el contraste de `b = 1` produce `t = 1,51445633` … [script …; Intro §10.4.2, PDF p. 10]». | referencia | mayor | (a) §10.4.2 empieza y se desarrolla en PDF p. 9; la p. 10 solo tiene el inicio de §10.4.3. (b) La fuente describe la prueba de pendiente nula (el intervalo del 95 % contiene cero o no). El contraste `b = 1` es una extensión del curso (`t = (b − 1)/u(b)`) que la fuente no respalda. | Cambiar a «PDF p. 9» y separar: «La prueba de pendiente nula está en [Intro §10.4.2, PDF p. 9]; el contraste frente a `b = 1` es una extensión que usamos aquí: `t = (b − 1)/u(b)`». |
| R03 | Escena I4: «La aplicación mecánica de esa prueba a las ocho observaciones por punto del F-PSMT-01». | dato / exactitud | mayor | `BD_DIAS` declara «Datos por Día» = 96 y «Total Datos» = 576 = 12 puntos × 8 lecturas × 6 días. Son 8 lecturas por punto **y día**, es decir 48 por punto en total. La frase describe mal el dato propio. | «a las 48 lecturas de cada punto del F-PSMT-01 (8 lecturas por día durante 6 días)». |
| R04 | «### Señales de escalamiento» de B: «si los puntos muestran curvatura, deriva…». | contenido | mayor | prop_e §2 fija para el básico, como señales que hay que reconocer con casos: dependencia no contemplada, cambio de escala, atípico sin causa, residuos con estructura, incertidumbre relevante en ambos ejes, **pocos grados de libertad** y **resultado próximo a un límite**. La lista de B omite pocos grados de libertad y resultado próximo a un límite, y no nombra la dependencia no contemplada (solo la deriva). La guía §3 exige cubrir las señales según prop_e §2. | Añadir una frase: «si hay pocos grados de libertad, si la dependencia entre puntos no está contemplada o si el resultado queda próximo a un límite de aceptación». |
| R05 | Escena I1, párrafo «…`cov(a,b) = −0,0002224490` con las unidades correspondientes al producto de parámetros». | unidades | mayor | `a` está en nmol/mol y `b` es adimensional, así que `cov(a,b)` está en nmol/mol. «Unidades del producto de parámetros» es incorrecto. | «…`cov(a,b) = −0,0002224490 nmol/mol`, porque `a` tiene unidades de nmol/mol y `b` es adimensional». |
| R06 | Escena I3, párrafo «Si la incertidumbre solo se conoce hasta un factor común, las estimaciones puntuales pueden coincidir con ciertos mínimos cuadrados ordinarios…». | exactitud técnica | mayor | Multiplicar todos los pesos por una constante no cambia la estimación puntual de WLS. Lo que cambia es la escala de la incertidumbre de los parámetros y del χ². La frase «pueden coincidir con ciertos OLS» no describe esto y puede llevar a error. | «Si las incertidumbres solo se conocen hasta un factor común, multiplicar todos los pesos por una misma constante no cambia β̂; sí cambia la escala de las incertidumbres de los parámetros y del χ²». |
| R07 | Escena I3, párrafo de validación: «…`ν = n − 2 = 10` grados de libertad». | exactitud / alcance | menor | prop_e §5 M7 dice «No se fija automáticamente ν = n − 2». El libreto lo fija sin condición. `ν = n − 2` vale solo con dos parámetros y observaciones independientes con varianzas declaradas. | Añadir: «ν = n − 2 vale porque la recta tiene dos parámetros y suponemos observaciones independientes; si el modelo cambia o hay dependencia, el número de grados de libertad se revisa». |
| R08 | Escena I3, mismo párrafo: «…el máximo simulado es `0,61604636`, menor que 2» (criterio atribuido a «ISO 6143 §5.2.2»). | referencia / claridad | menor | El criterio de ISO 6143 §5.2.2 se enuncia como condiciones sobre `|x̂ᵢ − xᵢ|` y `|ŷᵢ − yᵢ|`, cada una menor o igual que 2 veces su incertidumbre (la nota 1 lo relaciona con k = 2). El libreto cita la norma pero no enuncia la regla, y no dice que la comprobación del eje `x` es parte del criterio. | Enunciar la regla completa en la narración: «ISO 6143 §5.2.2 pide que cada punto cumpla `|x̂ᵢ − xᵢ| ≤ 2u(xᵢ)` y `|ŷᵢ − yᵢ| ≤ 2u(yᵢ)`; con `x` fijo, la primera es cero». |
| R09 | Escena B1 («Fijé seis referencias … y seis indicaciones»); Escena I3 («un segundo ejemplo simulado de 12 niveles»); Escena A1 («Usamos seis referencias observadas y seis indicaciones simuladas»). | claridad / reproducibilidad | menor | Los datos no se enuncian en el texto: ni los seis pares de B1, ni el rango 0–550 y las incertidumbres 0,30–0,85 de la validación de I3, ni `u(x) = 0,25`, la componente común `0,12` y `u(y) = 0,40` de A1. La guía §4 pide que las cifras se puedan reproducir con el script, pero el instructor no puede mostrar a la clase el ejemplo sin abrir el archivo. | Añadir una acotación `[DIAPOSITIVA]` o `[MATERIAL]` con la tabla de pares (x, y) de B1, y enunciar en A1 las tres magnitudes de incertidumbre; en I3, el rango y los valores de `u(y)`. |
| R10 | Escena I1, pizarra: «$u^2(\hat x)\approx…$, para las contribuciones independientes declaradas en este ejemplo». | claridad | menor | La fórmula incluye el término `2x̂cov(a,b)`, que no es una contribución independiente. Lo que se supone independiente es la nueva indicación respecto de los parámetros. La frase confunde dos supuestos. | «…con la nueva indicación independiente de los parámetros y con la covarianza `cov(a,b)` incluida». |
| R11 | Escena I1, párrafo «La matriz de covarianza… `s_e`» y B2 («El tamaño residual global … `s_e = 0,39460649`»). | notación | menor | `s_e` usa la letra `e`, que en prop_e §3 y guía §4 es el error con signo (`e = y − x`). `s_r` ya designa la repetibilidad. El símbolo no está en la lista de convenciones. | Usar `s_res` (o `s_y·x`) en todo el capítulo y añadirlo, con su definición, a la ficha o a la primera aparición. |
| R12 | ERROR CRÍTICO de I2 («No fuerce el origen…»), I3 («No use pesos…»), I4 («No aplique la prueba…»), A1 («No llame GGMR…») y A2 («No interprete un chi-cuadrado alto…»). En B3 y en los demás pasajes se usa el plural («No inviertan»). | estilo / forma | menor | El tratamiento es mixto: la narración y las acotaciones usan «ustedes» (guía §1), pero estas advertencias usan el singular «usted» («No use», «No aplique», «No llame»). Es inconsistente y suena a otra persona. | Pasar las advertencias a plural: «No fuercen», «No usen», «No apliquen», «No llamen», «No interpreten», «No introduzcan». |
| R13 | Claves en el texto: «[Intro §10.1, pp. 228–230]», «[Statistical Concepts §10.1…]»; «Referencias del capítulo»: «**Intro** —», «**Statistical Concepts** — Hahs-Vaughn, D. L.; Lomax, R. G.». | referencia / formato | menor | La guía §5 fija las claves de la tabla: «Crowder 2020», «Hahs-Vaughn» (o la forma de la tabla), no «Intro» ni «Statistical Concepts». En la portada del PDF de Statistical Concepts las reseñas citan «Lomax and Hahs-Vaughn», y la guía y el libreto ponen a Hahs-Vaughn primero: hay que verificar el orden de autores en la portada. | Usar las claves de la guía §5 («[Crowder 2020 §10.1, pp. 228–230]», «[Hahs-Vaughn 2020 §10.2.1, PDF pp. 3–5]»). Verificar el orden de autores en la portada antes de imprimir la referencia. |
| R14 | Referencias en el texto: «pp. 228–230» (paginación del libro) junto a «PDF pp. 7–8», «PDF p. 8», «PDF pp. 9–10» (paginación del archivo) en la misma escena. | referencia / formato | menor | Dos sistemas de paginación en la misma escena, sin aviso de cuál se usa. El lector no puede comprobar la cita sin saber cuál es. | Usar un solo criterio en todo el capítulo: «PDF p.» para los archivos de `docs/`, con una línea en la ficha que lo diga; o dar los dos números una vez. |
| R15 | Línea 76: «### Práctica B», seguida del marcador en línea 78. | estructura | menor | La guía §2 no incluye un encabezado propio para la práctica; el marcador va como cita al final de las escenas del nivel, sin título de sección. El encabezado rompe la estructura de nivel. Lo mismo ocurre con la práctica de I y de A (no tienen encabezado, pero la de B sí). | Quitar «### Práctica B» y dejar el marcador como cita tras la última escena de B, igual que en I y A. |
| R16 | Línea 78: «[PRÁCTICA — fase de ejercicios] Ajustar la recta OLS, revisar residuos y comprobar el signo de la corrección». | estructura / fidelidad | menor | El título del marcador debe ser el título breve que fija prop_e para ese nivel (guía §1). prop_e §5 M7-B dice: «ajustar la recta de un conjunto del Level 2, revisar residuos y comprobar el signo de la corrección». El libreto omite «de un conjunto del Level 2» sin decirlo. | Recuperar el título de prop_e: «Ajustar la recta de un conjunto del Level 2, revisar residuos y comprobar el signo de la corrección». |
| R17 | Línea 96 («También podemos someter una correlación de Pearson a una prueba de hipótesis…», un párrafo de unas 80 palabras con cuatro cifras y tres citas) y línea 136 («El peso no es una preferencia del analista… WLS con pesos diagonales no representa covarianza entre puntos»). | redacción | menor | Son frases largas con varias ideas subordinadas. Para decirlo en voz alta, la clase pierde el hilo. La guía §1 pide frases cortas y ritmo oral. | Dividir en tres o cuatro oraciones: una para la prueba, otra para el valor, otra para lo que no demuestra. |
| R18 | Escena I1, párrafo «Ahora invirtamos la predicción… el intervalo expandido ilustrativo tiene semiamplitud `1,30532699 nmol/mol`». | errores críticos / alcance | menor | prop_e §8 lista «confundir u y U» como error crítico que exige corrección. El libreto habla de «intervalo expandido» y de «semiamplitud» sin advertir que no es `u`. Es el lugar natural para la advertencia. | Añadir un `[ERROR CRÍTICO]`: «La semiamplitud 1,30532699 nmol/mol es `U = k·u`, no `u`. No reporten `u(x̂)` como si fuera la expandida, ni al revés». |

## Verificaciones hechas

**Cálculos (script `calc/M07_ejemplos.py`, ejecutado con `curso/.venv/bin/python`).** Todas las cifras narradas en el libreto coinciden con la salida:

| Cifra en el libreto | Salida del script | Resultado |
|---|---|---|
| `r = 0,99999823`; `R² = 0,99999645` | `r=0.99999823`; `R2=0.99999645` | coincide |
| `a = 0,24285714`; `b = 1,0014285714` | `a=0.24285714`; `b=1.0014285714` | coincide |
| residuos `−0,04286; 0,31429; −0,42857; 0,32857; −0,41429; 0,24286` | residuos idénticos (8 decimales) | coincide |
| mayor residuo `≈ 0,429` | `max = 0,42857` | coincide |
| `s_e = 0,39460649` | `s_e=0.39460649` | coincide |
| `u(a) = 0,28559521`; `u(b) = 0,0009432899`; `cov(a,b) = −0,0002224490` | idénticos | coincide |
| `t = 1061,63388878`; `p = 4,72 × 10⁻¹²`; 4 g.l. | `t=1061.63388878`; `p=4.7233441e-12` | coincide |
| prueba `b = 1`: `t = 1,51445633`; `p = 0,20447788` | idénticos | coincide |
| `x̂ = 249,90014265`; `x̂ − y = −0,59985735` | idénticos | coincide |
| `u(x̂) = 0,47014327`; `t(0,975;4) = 2,77644511`; `U = 1,30532699` | idénticos | coincide |
| `ŷ(250) = 250,60000000`; IC95 media `0,44727816`; IP95 `1,18338678` | idénticos | coincide |
| `b` forzada al origen `1,0020909091` | idénticos | coincide |
| OLS `a = 0,44761905`, `b = 1,0007428571`; WLS `a = 0,41685160`, `b = 1,0009213402` | idénticos | coincide |
| pesos `16,0` … `0,694444` | `16.0 … 0.694444` | coincide |
| `χ²_obs = 1,27964725`; `χ²_0,95;10 = 18,30703805`; máximo `0,61604636` | idénticos | coincide |
| `SS_LOF = 0,966`; `SS_PE = 0,080`; `F(2,8) = 48,3`; `p = 0,00003422` | idénticos | coincide |
| GGMR `a = 0,30472537`; `b = 1,0013144319`; `χ² = 0,40890065` | idénticos | coincide |
| abscisas ajustadas `≈ 0,00; 99,99; 200,04; 299,94; 400,05; 499,98` | `−0,0013; 99,9898; 200,0372; 299,9441; 400,0476; 499,9826` | coincide tras redondeo |
| GGMR casi lineal `χ² ≈ 3,48 × 10⁻²⁹`; con +5 en un punto `χ² = 83,36173290` | `3.47860069642e-29`; `83.36173290` | coincide |

**Recalculo a mano.** La semiamplitud de la media `t·√(s²_e·h)` con los parámetros del script (`u²(a) + x₀²u²(b) + 2x₀cov(a,b) = 0,025925`, `u = 0,16103`, `t = 2,776` ⇒ `0,4471`) coincide con `0,44727816`. La fórmula inversa de la pizarra de I1 coincide con las derivadas parciales de `x̂ = (y − a)/b` respecto de `y`, `a` y `b` (factores `1/b`, `x̂/b`, `x̂/b` y la covarianza `2x̂/b²`).

**Datos del F-PSMT-01 (`docs/F-PSMT-01 …xlsm`, hoja `BD_DIAS`).** «Datos por Día» = 96; «Total Datos» = 576 = 12 × 8 × 6. Esto confirma R03.

**Referencias (`pdftotext` sobre `docs/`).**

| Cita del libreto | Comprobación | Resultado |
|---|---|---|
| Intro §10.2.1 (`pp. 231–232`) | encabezado «10.2.1 Linear Least Squares», PDF p. 5 | correcto |
| Intro §10.2.3, PDF p. 6 | «10.2.3 Weighted Least Squares: Non-constant u(y)», PDF p. 6 | correcto |
| Intro §10.3.1, PDF pp. 7–8; §10.3.2 y §10.3.3, PDF p. 8 | 10.3 en PDF p. 7; 10.3.1, 10.3.2 y 10.3.3 en PDF p. 8 | correcto |
| Intro §10.4.1, PDF pp. 9–10 | «10.4.1 Residual Analysis» en PDF p. 9 | correcto (con margen) |
| Intro §10.4.2, **PDF p. 10** | «10.4.2 Slope Test» en PDF p. 9; el texto se desarrolla íntegro en p. 9 y la p. 10 empieza con las figuras | **incorrecto** → R02 |
| Intro §10.4.2 como respaldo de `b = 1` | la fuente describe la prueba de pendiente nula | **no respalda** → R02 |
| ISO 28037 §5.2.2, §5.7, §5.8 | encabezados en el texto del PDF y en el índice | correcto |
| ISO 28037 §6.3 (χ²obs frente a cuantil 95 %) | «6.3 Validation of the model» con «Check whether χ²obs exceeds the 95 % quantile» | correcto |
| ISO 28037 §§10.1–10.3 (GGMR y validación) y §11.1 (predicción) | «10.1 General», «10.2 …», «10.3 Validation of the model», «11.1 Prediction» | correcto (encabezados) |
| ISO 6143 §5.2.2 (criterio por punto) | texto de §5.2.2: comprobación por punto y nota 1 con k = 2 | correcto en el concepto; la regla debe enunciarse → R08 |
| Statistical Concepts §10.1, PDF pp. 2–7 (t de ρ = 0) | §10.1 en PDF pp. 1–2 (introductorio); la prueba con `t` aparece en §10.2.1, PDF pp. 3–5 | **incorrecto** → R01 |
| Statistical Concepts como referencia de regresión (ficha) | el cap. 10 trata asociación bivariada, no regresión | **no respalda la ficha** → R01 |
| Crowder, Delker, Forrest, Martin (Springer, 2020) | portada de `Introduction to Statistics in Metrology.pdf` | correcto |
| Otto, 3.ª ed., Wiley-VCH, 2017 | portada: «Third Edition», «© 2017 Wiley-VCH» | correcto |
| Hahs-Vaughn y Lomax, 4.ª ed., Routledge, 2020 | portada/reseñas: «fourth edition»; orden «Lomax and Hahs-Vaughn» | edición correcta; orden de autores por verificar → R13 |
| Brereton, 2.ª ed., Wiley, 2018 | no verificado en las primeras páginas de `Chemometrics _ data driven extraction for science.pdf` | **no verificado** (pendiente) |

**Escala y unidades.** Todas las cifras van con coma decimal en el texto. Las unidades son `nmol/mol` donde corresponde, salvo el error de R05. No se encontraron cifras con punto decimal en la prosa.

**Estructura y etiquetas.** No hay viñetas en el contenido narrado (las viñetas de la lista de referencias son permitidas). Las etiquetas usadas (`[DIAPOSITIVA]`, `[PIZARRA]`, `[NOTA AL INSTRUCTOR]`, `[PREGUNTA AL GRUPO]`, `[ERROR CRÍTICO]`, `[ESCALAMIENTO]`, `[PRÁCTICA — fase de ejercicios]`) están todas en la lista permitida de la guía §1.

**Marcadores de práctica.** Hay tres marcadores (B, I y A) y ninguna práctica desarrollada. Los tres corresponden a las prácticas de prop_e §5 M7 (B, I y A; la de A se fija como «práctica evaluable» en prop_e).

**Exclusiones (prop_e §6).** El libreto no incluye PCR, PLS, Monte Carlo, Allan, ISO 13528 ni GGMR con `V_xy ≠ 0`. La exclusión de GGMR con `V_xy ≠ 0` se enuncia en A1 y en el ERROR CRÍTICO y la ESCALAMIENTO de A.

**Cobertura por nivel (prop_e §5 M7).** Todos los temas están presentes: B (OLS, pendiente, intercepto, residuos, límites de R², intervalo de uso, inversión y corrección); I (incertidumbre y covarianza de parámetros, bandas de confianza y predicción, predicción inversa, origen forzado, WLS y pesos, pendiente y falta de ajuste con réplicas, límites con `x` fijo y escalamiento); A (regresión en ambos ejes, GGMR con `V_xy = 0`, residuos ponderados y chi-cuadrado). No hay contenido de un nivel en otro que falte o que sobre, salvo lo señalado en R04.

## Resumen

- **Crítica: 0.** Ninguna cifra del libreto es incorrecta: todas las cifras de la tabla de verificaciones coinciden con el script o con el recalculo a mano.
- **Mayor: 6** (R01–R06). Referencias que no respaldan la afirmación (R01, R02), un dato propio mal descrito (R03), señales de B incompletas frente a prop_e §2 (R04), una unidad errónea (R05) y una afirmación técnica incorrecta sobre WLS (R06).
- **Menor: 12** (R07–R18). Redacción oral, forma del libreto (singular/plural, encabezado de práctica, título del marcador), notación (`s_e`), datos no enunciados y claves de referencia.
- Antes de cerrar el capítulo, conviene corregir R01–R06. Los menores son de forma y pueden corregirse en la misma pasada.
- Quedan sin verificar la edición y el año de Brereton (2.ª ed., 2018) y el orden de autores de Statistical Concepts en la portada; cada uno está anotado en la tabla.

