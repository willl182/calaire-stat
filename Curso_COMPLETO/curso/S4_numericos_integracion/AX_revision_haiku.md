# AX. Revisión de redacción y errores (Haiku)

Revisado: `curso/S4_numericos_integracion/AX_libreto.md` (320 líneas). No se modificó el libreto.

## Plan de revisión

**Qué se revisó**

- Marco: `curso/guia_libreto.md` completa (§1 a §8) y `prop_e.md` en las partes que aplican: §1–§4, §6, §9 y §10, más los módulos M0–M13 para comprobar las remisiones del capítulo.
- Libreto AX completo, con la ficha, los trece anexos AX.1–AX.13, el cierre y las referencias.
- Bitácora `AX_bitacora_luna.md` solo como fuente de contraste (remisiones, alcance declarado).

**Cómo se revisó**

- **a) Redacción.** Lectura completa en orden. Se marcaron frases largas o difíciles de decir en voz alta, términos inconsistentes, notación (símbolos, coma decimal, unidades), palabras mal formadas y frases ambiguas.
- **b) Errores.** Se rederivó cada fórmula de las pizarras (identidades de AX.1, AX.2, AX.3, AX.4, AX.5, AX.6, AX.7, AX.9, AX.10, AX.11, AX.12, AX.13). Se ejecutaron los doce scripts `calc/AX_*.py` con `curso/.venv/bin/python -I` (AX_01 a AX_13). Se recalcularon a mano los ejemplos numéricos y se comparó con la salida de los scripts y con el texto. Se buscaron contradicciones internas entre narración, pizarra, ejemplo y script.
- **c) Formato libreto.** Se comprobó que no haya viñetas en contenido narrado, que las etiquetas sean de la lista permitida de guía §1, que las acotaciones estén en bloque de cita y que cada anexo tenga su estructura. Se comparó la estructura con guía §2.
- **d) Referencias.** Se comprobó con `pdftotext -layout -f P -l P` en `docs/` una muestra de numerales (ver Verificaciones). Se revisó que las claves sigan guía §5 y que no haya numerales inventados ni notas de pendiente dentro de la narración.
- **e) Alcance.** Se contrastó cada remisión «Se usa desde …» y cada consumidor con prop_e §5 (módulos), §6 (inclusiones y exclusiones) y §9 (anexos). Se comprobó que no haya prácticas ni marcadores (correcto: AX no tiene práctica asignada).

**Límites de la revisión**

- No se verificó de forma independiente el ARL de EWMA/CUSUM de AX.12. Se reprodujo la salida del script, pero la aproximación de cadena de Markov de 240 estados no se validó contra una tabla externa.
- No se localizó en `docs/` la cláusula de la predicción inversa en ISO/TS 28037 (AX.6). Queda como pendiente, tal como declara el libreto.
- Montgomery y JCGM 106 / ILAC-G8 no están en `docs/`; no se pudieron comprobar.

## Hallazgos

| id | ubicación (escena y texto citado) | tipo | severidad | problema | corrección propuesta |
|---|---|---|---|---|---|
| R01 | Escena AX.8, línea 190: «La raíz de la distancia por sus grados de libertad es un resumen reducido» y, después, «el valor reducido es 0,8» (3,2 con 4 grados). | error (fórmula) | crítica | La narración describe la raíz de la distancia dividida por los grados de libertad, y el ejemplo calcula el cociente sin raíz: 3,2/4 = 0,8. `calc/AX_08.py` hace `d2/df`. Lo que se enseña no coincide con lo calculado. Si el alumno aplica la raíz, obtiene √3,2/4 ≈ 0,447 o √(3,2/4) ≈ 0,894. | Escribir: «El cociente de la distancia entre sus grados de libertad, Q/ν = 3,2/4 = 0,8, es un resumen reducido». Quitar la palabra «raíz» de esa frase. Si se quiere la raíz, cambiar el ejemplo y el script. |
| R02 | Escena AX.4, línea 108: «se usa la varianza de esas medias dividida por D». | notación y error de fórmula | mayor | `D` es el efecto aleatorio de día (`D_d`, línea 94). El número de días es `d` (guía §4 y prop_e §3). La frase, leída en voz alta, da una fórmula con otro símbolo. prop_e M6 da `s²_medias/d`. | «… se usa la varianza de esas medias dividida por d, el número de días, sin volver a sumar la repetibilidad». |
| R03 | Escena AX.11, línea 244: «Se usa desde I (M12-I; M6 cuando se expresan límites para indicadores).» Línea 262: «M6 puede emplearlos al caracterizar indicadores de precisión.» | alcance | mayor | prop_e M6 no asigna límites de confianza chi-cuadrado ni t para indicadores. Esa asignación está en M12-I (indicadores, límites chi-cuadrado y t). Es una remisión a contenido no asignado a M6 (prop_e §5 y «ni más ni menos», §8). | Quitar «M6» de la línea 244 y de la línea 262. Dejar «Se usa desde I (M12-I)» y «M12-I usa estos límites para indicadores de precisión y sesgo». |
| R04 | Notas de verificación dentro de la narración: línea 22 (AX.1, «numerales pendientes de verificación»), línea 92 (AX.4, «numeral pendiente»), línea 118 y línea 124 (AX.5, «numerales pendientes», «Crowder, numeral pendiente»), línea 140 (AX.6, «numeral y página pendientes de comprobar»), línea 248 (AX.11, «numeral pendiente de verificación»), línea 254 (AX.11, «verificados en el PDF, p. 207»), línea 262 (AX.11, «numeral de chi-cuadrado pendiente»), línea 270 y línea 276 (AX.12, «numeral pendiente», «pendiente de página verificable»), línea 317 (Referencias, Montgomery, «pendientes de verificación»). | formato, referencia | mayor | Guía §5 pide que los pendientes se anoten en la bitácora y no en el texto. Estas frases son notas del desarrollador que el instructor leería en voz alta. Además, «verificados en el PDF» afirma una verificación que el lector no ve. | Quitar las notas de la narración y dejar la clave sin numeral, por ejemplo «[Crowder 2020]» o «[Hahs-Vaughn y Lomax, cap. de grados de libertad]». Pasar los pendientes a la bitácora (sección Pendientes). En línea 254 cambiar a «[Statistical Concepts, inferencia t]». |
| R05 | Nombres de scripts en la narración: línea 80 (AX.3, «se reproducen en `AX_03.py`»), línea 150 (AX.6, «`AX_06.py`»), línea 192 (AX.8, «`AX_08.py` calcula ese cociente»), línea 236 (AX.10, «se evalúa numéricamente en `AX_10.py`»), línea 258 (AX.11, «`AX_11.py` imprime los cuantiles»). | formato | menor | Son referencias a artefactos del desarrollador dentro de la narración hablada. Guía §8 las pide en la bitácora y en el mapa de cálculo; el libreto no las necesita. | Quitar el nombre de archivo de la narración. Si se quiere mantener la trazabilidad, usar una acotación «[NOTA AL INSTRUCTOR] Cifras reproducibles en calc/AX_03.py». |
| R06 | Escena AX.12, línea 274: «cuando lambda es pequeño»; línea 276: «el umbral h»; línea 278: «CUSUM unilateral con referencia k=0,5». | notación, terminología | menor | Mezcla «lambda» en letras con la notación `λ` del ejemplo (línea 278). `h` ya designa la semiamplitud en AX.3 (línea 70–72), y en AX.12 designa el umbral de CUSUM. «Referencia» en la guía (§4) es el valor de referencia `x`; aquí es el parámetro de holgura `k`. | Línea 274: «cuando λ es pequeño». Línea 276: «el umbral h_C» (o «umbral de decisión»). Línea 278: «CUSUM unilateral con holgura k = 0,5». |
| R07 | Escena AX.10, línea 236: «Cerca del límite, para θ=10, ambos lados dan 0,5 para una regla sin guarda». | redacción, claridad conceptual | menor | Para θ = L el valor está dentro, no fuera: solo corresponde el riesgo de falso rechazo (P(Y>L | θ=10) = 0,5). «Ambos lados» da a entender que existen a la vez falsa aceptación y falso rechazo, y que los dos valen 0,5. | «Para θ = 10, justo en el límite, la probabilidad de aceptar es 0,5 y la de rechazar también. Ninguna regla sin guarda da un riesgo pequeño en ese punto». |
| R08 | Escena AX.8, línea 190: «contamos las observaciones independientes que entran en la distancia y restamos las restricciones efectivamente ajustadas». | claridad, precisión | menor | El conteo de grados de libertad del ejemplo (6 puntos, 2 parámetros, 4 grados) no está escrito. Es 2n − (n + 2) = n − 2, con n abscisas ajustadas `ξ_i` además de `a` y `b`. Sin esa cuenta el alumno puede confundirla con la regla fija ν = n − 2 que AX.5 prohíbe (línea 130). | Añadir: «Hay 2n observaciones (x e y de cada punto) y n + 2 parámetros (las n abscisas ajustadas, a y b). Quedan 2n − (n + 2) = n − 2 grados; con seis puntos, 4». |
| R09 | Escena AX.7, línea 164: «Welch–Satterthwaite aproxima la distribución … igualando sus primeros momentos». | precisión | menor | La aproximación iguala media y varianza, es decir, los dos primeros momentos. «Primeros momentos» es ambiguo al leerlo en voz alta. | «… igualando su media y su varianza». |
| R10 | Escena AX.6, línea 148: «Si el nuevo y comparte datos con el ajuste». | redacción | menor | «El nuevo y» es ambiguo: la `y` es el símbolo de la indicación, no un sustantivo. Al leerlo en voz alta, «el nuevo y» suena a error. | «Si la nueva indicación y₀ comparte datos con el ajuste». |
| R11 | Escena AX.2, línea 46 (`cov(X_i,X_j)`) y línea 54 (`u(x_i,x_j)`). Línea 46 y línea 212–214 usan `cov(…)` también en otras escenas. | notación | menor | Se usan dos notaciones de covarianza en la misma escena: `cov` (variables aleatorias) y `u(x_i,x_j)` (GUM). Guía §4 pide consistencia terminológica. | Usar `cov(x_i,x_j)` en las dos pizarras y añadir una vez: «en la GUM aparece como u(x_i,x_j)». |
| R12 | Escena AX.9, línea 212 (`D_i=R_i-R`) y línea 214 (`D_i=x_i-x_{ref}`). | notación | menor | La misma definición aparece con dos símbolos: `R_i` y `x_i`. Hay dos nombres para el resultado y para la referencia. | Unificar en la línea 214 a `R_i − R` (o cambiar la narración a `x_i − x_ref`). |
| R13 | Escena AX.11, línea 252: «La intervalación requiere normalidad e independencia…». | ortografía, léxico | menor | «Intervalación» no es un término de la lengua ni de la guía. | «La construcción del intervalo requiere normalidad e independencia…». |
| R14 | Referencias, líneas 315–316: «Crowder. *Introduction to Statistics in Metrology*. Archivo: …» y «Statistical Concepts. Hahs-Vaughn, D. L. y Lomax, R. G.». Narración: «[Crowder, *Introduction…*, …]» y «[Statistical Concepts, …]». | referencia | menor | Guía §5 fija claves («Crowder 2020», «Hahs-Vaughn») y pide la cita completa (autor, título, edición/año, editorial). La entrada de Crowder no tiene autor, año ni editorial. En la narración se usan títulos largos en vez de la clave. | Usar «[Crowder 2020 §…]» y «[Hahs-Vaughn y Lomax]» en narración (sin numeral si no se verificó). En la lista de referencias completar autor, año y editorial de Crowder 2020 desde el PDF (o marcar «verificar editorial en el PDF», como en guía §5). |
| R15 | Escena AX.9, línea 216: «[GUM 5.2.2; prop_e §6 fija este alcance curricular]». | referencia | menor | Guía §5 dice que prop_e solo justifica el alcance y «no es referencia técnica». Aquí aparece dentro del corchete de referencias técnicas. | Sacar `prop_e §6` del corchete y, si se quiere, decir en la narración: «El alcance del curso excluye el KCRV combinado (propuesta E, §6)». |
| R16 | Escena AX.8, línea 190 (párrafo «Después del ajuste…»); Escena AX.12, línea 274 («Para ver la suma…») y línea 276 («Se deriva de la probabilidad…»). | claridad oral | menor | Frases de 60 a 90 palabras con varias subordinadas. Son difíciles de decir en voz alta y de seguir. | Partir cada párrafo en 3 o 4 frases. En AX.8 separar «conteo de grados» y «diagnóstico»; en AX.12 separar la recurrencia, la suma geométrica y la matriz de transición. |
| R17 | Estructura del capítulo (ficha y niveles). Guía §2 pide secciones «Nivel B / I / A» con la indicación de lo que cada nivel añade. | estructura | menor | AX no tiene secciones de nivel. La ficha dice «las secciones indican desde qué nivel se usa el resultado», pero no hay una tabla por nivel. El cierre sí es narrado por nivel. La forma es una adaptación razonable para anexos, pero no está declarada como tal. | Añadir en la ficha una tabla breve «Anexo | nivel de primer uso | consumidores», que reúna la información que hoy está dispersa en «Se usa desde». Así la estructura queda explícita para anexos. |
| R18 | Ficha, línea 11: «identificadas al cierre de cada anexo y en la matriz de remisiones de la bitácora». | coherencia | menor | La bitácora no tiene una «matriz de remisiones»: tiene una lista en la sección «Remisiones que deben coincidir con los libretos». Y las remisiones de cada anexo no siempre están en el cierre (no es estrictamente cierto que estén al cierre de cada anexo). | Cambiar a: «identificadas en cada anexo (líneas «Se usa desde …») y en la lista de remisiones de la bitácora». |
| R19 | Ficha, línea 9 («AX.1–AX.13 según guía §7 y prop_e §9») y alcance de prop_e §9. | alcance | menor | prop_e §9 enumera «deducciones de estimadores, cuadrados medios esperados, ecuaciones normales, propagación y formulación matricial (GGMR)». No menciona Welch–Satterthwaite (AX.7), riesgos de decisión (AX.10), límites de confianza (AX.11), EWMA/CUSUM (AX.12) ni Monte Carlo (AX.13). La guía §7 (que fija los identificadores) sí los incluye, así que no hay contradicción dura, pero el alcance no está escrito en el mismo lugar. | Confirmar con el responsable del curso que §9 es lista indicativa y que guía §7 manda sobre los identificadores. Si se confirma, agregar en la ficha: «Según guía §7, incluye también…». |

Nota: los hallazgos R01 a R04 afectan al contenido o a la trazabilidad y deben corregirse antes de la siguiente fase. Los R05 a R19 son de forma o de claridad.

## Verificaciones hechas

### Cálculos (recalculados a mano y comparados con `calc/AX_*.py`)

| Anexo | Verificación | Resultado |
|---|---|---|
| AX.1 | Datos 2, 4, 6: media 4; suma de cuadrados 8; s² = 8/2 = 4; s = 2; ν = 2. Con divisor 3: 8/3 ≈ 2,667. Identidad Σ(X−X̄)² = Σ(X−μ)² − n(X̄−μ)². | Correcto. `AX_01.py`: 4; 8; 4; 2; ν = 2; 2,66666667. |
| AX.2 | Varianzas 0,30² + 0,20² = 0,13; cov = 0,09; Var(Δ) = 0,13 + 0,13 − 2·0,09 = 0,08; u(Δ) = 0,28284; sin covarianza, √0,26 = 0,50990. | Correcto. `AX_02.py` coincide. |
| AX.3 | Rectangular: ∫(x²)/(2h) = h²/3, u = h/√3; triangular: 2∫₀ʰ x²(h−x)/h² dx = h²/6, u = h/√6; resolución: u = δ/√12. Ejemplos: 0,60/√3 = 0,34641; 0,60/√6 = 0,24495; 0,12/√12 = 0,03464. | Correcto. `AX_03.py`: 0,346410162; 0,244948974; 0,0346410162. |
| AX.4 | d = 4, n = 3, s_entre = 0,20, s_r = 0,30: 0,04/4 + 0,09/12 = 0,01 + 0,0075 = 0,0175; u = 0,13229. Sin efecto de día: 0,0075; u = 0,08660. E(MS_dentro) = σ²; E(MS_entre) = σ² + nτ²; var(ē) = τ²/d + σ²/(dn). | Correcto. `AX_04.py` coincide. Error de símbolo en R02. |
| AX.5 | X = [[1,0],[1,1]]; XᵀX = [[2,1],[1,1]]; inversa = [[1,−1],[−1,2]]; cov(a,b) = −σ²; var(b) = 2σ². | Correcto. `AX_05.py` coincide. |
| AX.6 | x̂ = (11 − 1)/2 = 5; derivadas: ∂/∂y = 1/b, ∂/∂a = −1/b, ∂/∂b = −x̂/b; numerador 0,04 + 0,01 + 25·0,0004 + 2·5·(−0,001) = 0,05; /4 = 0,0125; u = 0,11180. Signo del término cruzado: (−1/b)(−x̂/b)·2·cov = +2x̂cov/b², correcto. | Correcto. `AX_06.py`: x̂ = 5; 0,05; 0,0125; 0,111803399. |
| AX.7 | u_c² = 0,09 + 0,16 = 0,25; denominador 0,30⁴/5 + 0,40⁴/20 = 0,00162 + 0,00128 = 0,0029; ν_eff = 0,0625/0,0029 = 21,55. | Correcto. `AX_07.py`: 0,25; 0,0029; 21,5517241. |
| AX.8 | Distancia 3,2 y ν = 4 (n − 2 con n = 6): 3,2/4 = 0,8. | Cociente correcto (`AX_08.py` hace `d2/df`). La narración dice «raíz»: R01. |
| AX.9 | Var(Δ) = u₁² + u₂² − 2 cov = 0,13 + 0,13 − 0,18 = 0,08; u = 0,28284. Covarianza de diferencias con referencia: cov(D_i,D_j) = cov(x_i,x_j) − cov(x_i,x_ref) − cov(x_ref,x_j) + u²(x_ref). | Correcto. `AX_09.py` coincide. |
| AX.10 | L = 10, u = 1: P_FA(12) = Φ(−2) = 0,0227501 ≈ 0,0228; P_FR(8) = 1 − Φ(2) = 0,0227501; P(Y≤L | θ = 10) = 0,5. | Correcto. `AX_10.py` coincide. Redacción de θ = 10: R07. |
| AX.11 | n = 10, ν = 9; χ²_{0,025;9} = 2,7004, χ²_{0,975;9} = 19,0228; σ_inf = 0,30·√(9/19,0228) = 0,20635; σ_sup = 0,30·√(9/2,7004) = 0,54768; t_{0,975;9} = 2,26216; semiancho 2,26216·0,30/√10 = 0,21461; IC de la media (−0,0146; 0,4146). | Correcto. `AX_11.py`: σ (0,206350562; 0,547683055); t 2,26215716; media (−0,0146070718; 0,414607072). Ninguna fórmula invierte los cuantiles. |
| AX.12 | λ = 0,20: factor λ/(2 − λ) = 0,1111; desviación 0,3333; límite 3·0,3333 = 1; geométrica p = 0,01 → 100. ARL bajo control EWMA (cadena 240 estados) 559,679; CUSUM (k = 0,5, h = 5, 240 estados) 921,016. | Factor, desviación y geométrica: correcto. ARL: reproducido por `AX_12.py`; no validado contra tabla externa (límite de esta revisión). |
| AX.13 | M = 10 000 y s = 2: 2/√10 000 = 0,02; M = 40 000: 0,01. Cuatro veces más ensayos para la mitad del error. | Correcto. `AX_13.py`: 0,0202339 y 0,00995442 (empíricos, semilla fija). |

### Referencias comprobadas con `pdftotext` en `docs/` (muestra de 13 numerales)

| Clave y numeral citado | Archivo (en `docs/`) | Página PDF | Resultado |
|---|---|---:|---|
| GUM 4.3.7 (rectangular, cota de límites) | `ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ … (GUM_1995) - libgen.li.pdf` | 21 | Confirmado: texto de 4.3.7 sobre límites y distribución rectangular. |
| GUM 4.4.5 y 4.4.6 (rectangular y triangular) | mismo PDF | 21–22 | Confirmado: 4.4.5 citado en 4.3.7; 4.4.6 citado en la distribución triangular. |
| GUM 5.1.2 (incertidumbre combinada) | mismo PDF | 27 | Confirmado: encabezado «5.1.2 The combined standard uncertainty…». |
| GUM 5.2.2 (entradas correlacionadas) | mismo PDF | 29 | Confirmado: encabezado «5.2.2 When the input quantities are correlated…». |
| GUM G.4, ecuación G.2b (Welch–Satterthwaite) | mismo PDF | 81 | Confirmado: G.4 «Effective degrees of freedom» y G.2b. |
| GUM H.5 (ANOVA) | mismo PDF | 106–107 | Confirmado: H.5 «Analysis of variance»; ejemplo H.5.2 con σ_W de J − 1 grados. |
| ISO/TS 28037 5.2.2, 5.5, 5.6 | `ISO 28037.pdf` | 14, 15, 16 | Confirmado: encabezados 5.2.2 y 5.5; 5.6 «Validation of the model», con χ² de ν = m − 2 (5.6.2). |
| ISO/TS 28037 10.1 (caso general) | mismo PDF | 39 | Confirmado: 10.1 «General», modelo de incertidumbres y covarianzas de x e y. |
| GUM-S1 5.9, 5.10 | `ISO_IEC Guide 98-3_2008 Suppl.1_2008 - libgen.li.pdf` | 23, 24–25 | Confirmado: 5.9 «Monte Carlo approach…»; 5.10 «Conditions for the valid application…». |
| GUM-S1 7.2 (número de ensayos) | mismo PDF | 37 | Confirmado: 7.2 «Number of Monte Carlo trials». |
| Statistical Concepts, grados de libertad n − 1 de la t para una media | `Statistical Concepts – A First Course.pdf` | 207 | Confirmado: «…the number of degrees of freedom… n − 1 in general». |

No comprobado (queda pendiente, como declara el libreto): ISO/TS 28037, cláusula de la predicción inversa (AX.6); Crowder 2020 (numerales de ANOVA, regresión, covarianza, chi-cuadrado); Montgomery (no está en `docs/`); JCGM 106 e ILAC-G8 (no están en `docs/`).

### Formato y alcance

- **Etiquetas.** Solo se usan etiquetas permitidas: `[PIZARRA]` (23), `[ERROR CRÍTICO]` (13), `[ESCALAMIENTO]` (3). No hay `[PRÁCTICA]` ni marcadores de práctica (correcto, AX no tiene práctica asignada).
- **Viñetas.** Ninguna en contenido narrado. Solo en la lista de referencias (correcto por guía §1).
- **Coma decimal.** Narración y ejemplos usan coma (0,30; 0,20; 21,55; 0,0228). Las cifras de las pizarras LaTeX usan punto decimal solo dentro de `$…$` (correcto por guía §4, que deja la notación LaTeX libre).
- **Unidades.** nmol/mol en todos los ejemplos de concentración. Sin uso de ppb.
- **Datos.** Todos los ejemplos numéricos están rotulados como simulados. Ninguno se atribuye a CALAIRE (guía §4).
- **Exclusiones (prop_e §6).** AX.8 restringe a `V_xy = 0` y declara la exclusión de GGMR general; AX.9 declara que no es KCRV combinado. Sin Allan, PCR/PLS, ISO 13528, z/ζ/Mandel ni protocolo BIPM.
- **Remisiones.** Todas las remisiones de «Se usa desde» coinciden con prop_e §5 salvo AX.11 (R03). AX.1 (M2-B, M4-B), AX.2 (M1-A, M3-I, M8), AX.3 (M3-B), AX.4 (M6-B, M6-I, M8), AX.5 y AX.6 (M7-I), AX.7 (M4-I, M8-I), AX.8 (M7-A, M9-A), AX.9 (M9-I, M10, M9-A), AX.10 (M10-I, M10-A), AX.12 (M11-A) y AX.13 (M13-A) concuerdan con prop_e M1–M13.

## Resumen

**Hallazgos por severidad:**

- **Crítica (1):** R01. Narración de AX.8 describe una raíz donde el ejemplo y el script calculan un cociente.
- **Mayor (3):** R02 (símbolo `D` en lugar de `d` en AX.4), R03 (remisión a M6 no asignada en AX.11), R04 (notas de verificación y numerales pendientes dentro de la narración).
- **Menor (15):** R05 a R19.

**Qué hace falta antes de la siguiente fase:** corregir R01 a R04 en el libreto. Los menores pueden agruparse en una sola pasada de redacción.

**Observaciones fuera del libreto (no se corrigen aquí):**

- La bitácora `AX_bitacora_luna.md` lista AX.9, AX.10 y AX.11 como de nivel B en «Alcance por nivel» y como de nivel I en la misma sección. El libreto los sitúa en I. Conviene corregir la bitácora.
- La bitácora no tiene la sección «Correcciones» que pide guía §8.
- La sección de referencias pendientes de la bitácora debe recoger los pendientes de R04.
