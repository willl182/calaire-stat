# Revisión de M08 — Propagación de incertidumbre

Revisor: Haiku (redacción y errores). Revisado: `curso/S2_modelos_calibracion/M08_libreto.md`. El libreto no se modificó.

## Plan de revisión

Leí, en este orden: `curso/guia_libreto.md` (§§1–8), `prop_e.md` §§1–4 y 8, §5 módulos M7 (contexto de convenciones), M8 y M9 (frontera del módulo), §6 (inclusiones y exclusiones) y §7 (casos) y el libreto M08 completo, de la ficha a las referencias.

Cómo lo revisé:

1. **Redacción (a).** Lectura completa en voz alta mental: frases largas, puntuación, terminología (`q`, «indicación corregida», «resultado inverso», «valor de uso»; `u` frente a `u_c`), notación de la guía §4 (coma decimal, `nmol/mol`, `$…$`, rótulos de origen). Búsqueda de repeticiones y errores tipográficos. No pasé un corrector ortográfico automático; la revisión de ortografía es de lectura.
2. **Errores (b).** Reproduje todos los números de los ejemplos con `curso/.venv/bin/python curso/S2_modelos_calibracion/calc/M08_ejemplos.py` (salida sin modificar) y recalculé a mano las cifras que el script no imprime (tabla de A2, `0,30/√3`, `0,10/√12`, covarianza y `u(Δ)`). Comparé cada cifra del texto con la salida. Revisé fórmulas (pizarras), signos de correcciones y covarianzas, y la coherencia interna entre escenas.
3. **Formato libreto (c).** Comprobé que no hay viñetas en contenido narrado (solo en referencias), que las acotaciones usan etiquetas permitidas (`DIAPOSITIVA`, `PIZARRA`, `NOTA AL INSTRUCTOR`, `PREGUNTA AL GRUPO`, `EJEMPLO`, `ERROR CRÍTICO`, `ESCALAMIENTO`, `TRANSICIÓN`, `PRÁCTICA — fase de ejercicios`), y la estructura de §2 (ficha, niveles con «lo que se da por visto», señales en B, cierre, referencias).
4. **Referencias (d).** Para cada numeral citado busqué el encabezado en el PDF correspondiente, extrayendo el texto con `pdftotext -layout` a un directorio temporal fuera de `docs/` (no se tocó `docs/`). Muestra y resultados en «Verificaciones hechas».
5. **Alcance (e).** Cotejé cada subapartado de prop_e §5 (M8 B, I, A) con las escenas y con los marcadores de práctica. Revisé §6 (exclusiones: Monte Carlo, GGMR con covarianza cruzada, PCR/PLS, etc.) y §8 (errores críticos). En esta fase solo busqué marcadores ausentes o prácticas desarrolladas; no señalo la falta de desarrollo de las prácticas.

## Hallazgos

| id | Ubicación (escena · texto citado) | Tipo | Severidad | Problema | Corrección propuesta |
|---|---|---|---|---|---|
| R01 | Escena I1 · ejemplo: «`u_c` lineal aproximada `0,2632 nmol/mol`» (L127) | numérico | mayor | El texto de la misma escena (L125) y el script dan `u_c≈0,2637` (script: `0,2636774`). Dos cifras distintas para la misma cantidad en la misma escena. | Cambiar `0,2632` por `0,2637 nmol/mol` en el ejemplo de L127. |
| R02 | Escena I2 · pizarra «`$$\nu_{\mathrm{eff}}\approx\frac{u_c^4}{\sum_i u_i^4/\nu_i}$$`» (L143) | fórmula | mayor | En Welch–Satterthwaite el término es la contribución `c_i·u(x_i)`, no la incertidumbre de entrada `u_i`. Tal como está, la pizarra da un resultado distinto del que obtiene el script (`ν_eff≈657,95`, que usa `c_i²u²(x_i)` al cuadrado, dividido por `ν_i`). | Escribir `$$\nu_{\mathrm{eff}}\approx\frac{u_c^4}{\sum_i c_i^4\,u^4(x_i)/\nu_i}$$` y añadir «donde `c_i u(x_i)` es la contribución de la entrada `i` a `u_c`». |
| R03 | Escena B3 · «Este procedimiento numérico, conocido como método de Kragten … [MMU §6.1; Intro §7.2; AX.2]» (L70) | referencia | mayor | La cita no respalda el método. Ni MMU §6.1 ni Crowder §7.2 mencionan Kragten (comprobado con `pdftotext`). Kragten aparece en GUM-6, Anexo F.2, ecuación (47) y nota 3 (ref. [108] de GUM-6). La ecuación (47) usa diferencias centrales `(f₊−f₋)/(2u)`, mientras la tabla de B3 usa `f(x+u)−f(x)`; la nota 3 lo describe como «closely related approach». La ficha (L14) afirma que los numerales «se verificaron», y esta cita no lo está. | Sustituir la cita por `[GUM-6 F.2, ecuación (47) y nota 3]` y reescribir la frase: «Es un procedimiento emparentado con el de Kragten, citado en la nota 3 de GUM-6; la ecuación (47) de esa guía usa diferencias centrales, y nuestra tabla usa una perturbación hacia arriba». Corregir la ficha tras esto. |
| R04 | Nivel A, intro (L190) y escena A2 (L220): «una CMC expresada en la misma magnitud…» y «la CMC pertinente» | concepto sin referencia | mayor | «CMC» (capacidad de medición y calibración) aparece dos veces, en la ficha y en A, sin definición ni referencia. La guía §5 exige referencia para toda definición. | En la primera aparición (L190) añadir: «la capacidad de medición y calibración (CMC) es la incertidumbre que un laboratorio puede declarar como su mejor capacidad [VIM, JCGM 200:2012, término CMC (no disponible en docs/); numeral pendiente en la bitácora]». No inventar numeral. |
| R05 | Escena I4 · «Ese conteo describe el diseño; no autoriza a tratar las 576 lecturas… dividirla por `√576` no estima…» (L185) | alcance | mayor | prop_e §5 M8-B exige en la práctica B «explicar por qué dividir una dispersión de varios niveles y días por √576 no estima la incertidumbre buscada». Ese contenido solo aparece en I4. La sección B no lo narra y el marcador de práctica B (L95) no lo recoge, así que el nivel B queda sin la explicación que su práctica requiere. | Trasladar el párrafo de los 576 lecturas (datos propios, F-PSMT-01, 12 × 8 × 6) a la escena B3, antes del marcador de práctica, con su rótulo de origen. En I4 dejar solo la cadena SRP 55 → Level 2 → cliente y la referencia cruzada «ver B3». |
| R06 | Escena B1 · «la indicación corregida `q` se obtiene restando el intercepto…» (L26); pizarra «`q=f(y,a,b)`» (L28); «resultado inverso `q=100,000`» (L40); también L76, L123, L147 | notación / terminología | mayor | prop_e §3 fija `x̂ = (y − a)/b` para el uso inverso. El libreto usa `q` y lo llama de tres formas distintas («indicación corregida», «resultado inverso», «valor de uso» en L24). El lector no sabe si `q` es una indicación o un valor de referencia. | Usar `x̂` en todo el capítulo: «valor de uso `x̂ = (y − a)/b`». Definirlo una vez en B1 y eliminar «indicación corregida». Corregir en L26, L28, L40, L76, L123 y L147. |
| R07 | Escena B1 · «desviación estándar `s=0,24 nmol/mol`» (L36); escena B2 · «`s` describe la dispersión de observaciones individuales» (L58); pizarra «`$u(\bar y)=s/\sqrt n$`» (L60) | notación | mayor | prop_e §3 reserva `s_r` para la desviación de lectura dentro del día (σ) y `s_entre` para el efecto de día. Las ocho lecturas de B1 son de un mismo día. Con `s` a secas el capítulo no sigue la convención de módulos anteriores. | Escribir `s_r` en L36, L58 y L60, y en las fórmulas `s_r/√8`. Mantener `s` solo como nombre genérico si hace falta, con una frase que lo diga. |
| R08 | Todo el capítulo · fórmulas narradas en línea, p. ej. «`0,24/√8=0,0849 nmol/mol`» (L36), «`u=U/k`» (L50), «`ν_eff≈658`» (L147) | formato | mayor | La guía §4 exige LaTeX `$…$` en línea para fórmulas. El libreto usa comillas invertidas en todas las fórmulas narradas. Solo las pizarras están en LaTeX. | Convertir las fórmulas en línea a `$…$`, con coma decimal entre llaves para evitar espacios (`$0{,}24/\sqrt{8}=0{,}0849\ \mathrm{nmol/mol}$`). Dejar las comillas invertidas para código y nombres de archivo. |
| R09 | Todo el capítulo · «[Intro §6.3–6.4; M7]» (L26) y ~25 usos de «Intro»; «[GUM Anexo G.4]» (L141, L147); «[prop_e §3]» como respaldo técnico (L58, L87, L161) | referencia / formato | menor | La clave «Intro» no está en la tabla de claves de la guía §5 (la clave es «Crowder 2020»). «GUM Anexo G.4» no sigue el formato `[GUM G.4]`. Citar prop_e como respaldo técnico contradice la guía §5 (prop_e solo justifica el alcance). | Sustituir «Intro» por «Crowder 2020» en todas las citas; «GUM Anexo G.4» por «GUM G.4»; quitar prop_e de las citas técnicas y dejarlo solo donde justifique convención o alcance. |
| R10 | Referencias del capítulo (L255–258) | referencia | menor | Los anexos AX.2, AX.3 y AX.7 se citan como fuente técnica y no aparecen en la lista. La guía §5 pide la cita completa de cada clave usada. | Añadir una entrada: «Anexos AX.2, AX.3, AX.7 de la guía §7 (documentos internos; no están en docs/)». Añadir «VIM (no disponible en docs/)» cuando se resuelva R04. |
| R11 | Escena A2 · «La teoría de propagación y sus límites se discute en los textos de incertidumbre … [GUM 5.1; Intro §7.5–7.7; JCGM GUM-6 11.9 …]» (L216) | referencia | menor | La frase es vaga («los textos de incertidumbre») y la cita a GUM-6 11.9 no trata la linealización: su título es «Estimation and uncertainty evaluation for statistical models». El tratamiento directo de la linealización y de la validez de la ley de propagación está en GUM-6 Anexo F.1 y F.2. | Sustituir la frase vaga por «[GUM-6 F.1–F.2; Crowder 2020 §7.7]» y cambiar «JCGM GUM-6 11.9» por esa cita. |
| R12 | Final del Nivel B, después del marcador de práctica I (L187–188) | formato | menor | Falta línea en blanco entre el marcador «> **[PRÁCTICA — fase de ejercicios]**…» y el encabezado «## Nivel A». Puede romper el bloque de cita al renderizar. | Insertar una línea en blanco antes de «## Nivel A — covarianza común…». |
| R13 | Escena I3 · «con lo que `u≈0,4847 nmol/mol`» (L163) frente a «`u_c=0,4847`» en el ejemplo (L165) | notación | menor | El mismo valor combinado aparece con dos símbolos. La convención del capítulo es `u_c` para la combinada. | Cambiar «`u≈0,4847`» por «`u_c≈0,4847`» en L163. |
| R14 | Escena B1 (L36), I2 (L141), I2 (L147) y I3 (L161) | redacción | menor | Frases de más de 100 palabras, difíciles de decir en voz alta. La guía §1 pide frases cortas y ritmo oral. | Dividir cada una en 3–4 frases. Ejemplo para L36: «Veamos un ejemplo con números. Es un conjunto simulado, preparado para esta clase. Ocho lecturas dan una media de 100,60 y una desviación de 0,24. La resolución digital es 0,10. La parte tipo A de la media es 0,24/√8, es decir, 0,0849.» |
| R15 | Ficha · «AX.13 corresponde a Monte Carlo, que no se desarrolla en este módulo» (L13) | alcance / redacción | menor | AX.13 pertenece a M13 (guía §7) y no a M8. Mencionarlo en la ficha de M8 introduce un anexo que este módulo no usa. | Eliminar la frase de M8; si se quiere mantener la nota, decir «AX.13 queda para M13». |
| R16 | Escena B2 · pizarra «`$u=δ/\sqrt{12}$`» (L52) | formato | menor | Símbolo `δ` Unicode dentro de LaTeX. En algunos renderizadores no se compila. | Usar `\delta`: `$u=\delta/\sqrt{12}$`. Revisar `h` y `δ` en las demás pizarras. |

## Verificaciones hechas

### Cálculos (script `calc/M08_ejemplos.py`, ejecutado sin cambios; recálculos a mano donde el script no imprime)

| Cifra del libreto | Dónde | Salida / recálculo | Resultado |
|---|---|---|---|
| `q=(100,60−0,40)/1,002=100,000` | B1 | `q=100,0000000000` | Correcto |
| `0,24/√8=0,0849`; `0,10/√12=0,0289`; `0,0102`; combinada `0,0855` | B1, B2 | `0,0848528`; `0,0288675`; `0,0102062`; `0,0854644` | Correcto |
| `0,30/√3=0,1732`; `U=0,30`, `k=2` → `u=0,15` | B2 | `0,1732051`; recálculo directo | Correcto |
| `c_y≈0,9980`, `c_a≈−0,9980`, `c_b≈−99,8004` | I1 | `0,998004`; `−0,998004`; `−99,8003992` | Correcto |
| Kragten: `+0,0853`, `−0,1497`, `−0,1992`; `u_c≈0,2634`; `U≈0,527` | B3 | `+0,0852938`; `−0,1497006`; `−0,1992032`; `0,2633766`; `0,5267531` | Correcto |
| `u_c` lineal `≈0,2637` (texto de I1 y de I2) | I1, I2 | `0,2636774` | Correcto |
| `u_c` lineal en el EJEMPLO de I1 | I1 (L127) | `0,2636774` | **Incorrecto**: el libreto dice `0,2632` (R01) |
| `ν_eff≈658`; `t(0,975;658)≈1,964`; `U≈0,518` | I2 | `657,954`; `1,963576`; `0,517751` | Correcto |
| `7` grados de libertad = `8 − 1` | I2 | `n−1 = 7` | Correcto |
| `√(0,30²+0,20²+0,10²)=0,3742`; futuro `0,4847`; `k=2` → `0,748`, `0,969` | I3 | `0,3741657`; `0,4846648`; `0,7483315`; `0,9693297` | Correcto |
| Doble conteo `0,4243` | I3 | `0,4242641` | Correcto |
| Cadena: `0,4482`; `0,6142`; `U≈1,2285` | I4 | `0,4482187`; `0,6142475`; `1,2284950` | Correcto |
| `576 = 12·8·6`; `√576 = 24` | I4 (B por R05) | `576`; `24` | Correcto |
| Covarianza `x₁x₂u_b² = 0,0918` | A1 | `0,0918` | Correcto |
| `u(Δ)≈0,320` (compartido); `≈0,535` (independencia) | A1 | `0,3202124`; `0,5349168` | Correcto |
| Tabla A2 (`U(x)`, CMC, `max`) en `x = 0; 80; 250; 500` | A2 | `U`: `0,560; 1,111; 3,052; 6,026`; CMC: `0,80; 1,12; 1,80; 2,80` (recálculo a mano) | Correcto |
| Ecuación de `ν_eff` (R02) | I2 | El script aplica `c²u²` al cuadrado y lo divide por `n−1`; eso equivale a `c⁴u⁴/ν` | La pizarra debe decir `c_i⁴u⁴(x_i)/ν_i` (R02) |

Sin verificar: `0,0853` y `−0,1497` de B3 coinciden con el script; la cifra `U≈0,527` se redondea desde `0,52675` (correcta).

### Referencias (`pdftotext -layout` sobre los PDF de `docs/`, extractos en directorio temporal)

Muestra de 25 numerales. Se encontró encabezado o contenido correspondiente en cada caso salvo lo indicado.

| Clave y numeral | Comprobación | Resultado |
|---|---|---|
| GUM 3.3.4–3.3.5 | Clasificación tipo A y tipo B | OK |
| GUM 4.1 «Modelling the measurement»; 4.2; 4.3 | Encabezados presentes | OK |
| GUM 5.1 «Uncorrelated input quantities»; 5.1.2 (`u_c(y)`) | Encabezado y ecuación | OK |
| GUM 5.2 «Correlated input quantities» | Encabezado | OK |
| GUM 6.2 «Expanded uncertainty»; 6.3 «Choosing a coverage factor» | Encabezados | OK |
| GUM G.3 «t-distribution and degrees of freedom»; G.4 «Effective degrees of freedom» | Encabezados | OK |
| GUM-6 8.4 «Multi-stage measurement models»; 11.2; 11.3; 11.4 | Encabezados | OK |
| GUM-6 11.9 «Estimation and uncertainty evaluation for statistical models» | Encabezado. El contenido no trata linealización. | **Cita inadecuada para A2** (R11) |
| GUM-6 F.1 (linealización); F.2 (validación de la ley de propagación); ecuación (47) y nota 3 (Kragten [108]) | Texto presente | **Fuente correcta para Kragten y A2** (R03, R11) |
| Crowder 2020 §6.2.1–6.2.5 | Encabezados | OK |
| Crowder 2020 §6.3; §6.4 | Encabezados | OK |
| Crowder 2020 §7.2; §7.3; §7.4.1 (covarianza); §7.5–7.7 | Encabezados | OK |
| MMU §5.2.2 (tipo B); §5.3.1 (resolución, distribución rectangular) | Encabezados y texto | OK |
| MMU §6.1 «Uncertainty propagation law» | Encabezado | OK como ley de propagación; **no respalda Kragten** (R03) |
| Autores: Crowder, Delker, Forrest, Martin (2020); Novellino do Rosario y Mendes (2025) | Portadas de los PDF | OK |

Sin verificar: MMU §5.3.1 para la forma `δ/√12` (se halló el encabezado y el texto de la distribución rectangular, no la ecuación exacta); GUM 4.3 para `h/√3` (encabezado presente, no se extrajo la fórmula).

### Formato y alcance

- No hay viñetas en el contenido narrado. Las listas están solo en «Referencias del capítulo».
- Etiquetas de acotación: todas permitidas.
- Ficha, niveles B, I, A, cierre y referencias en el orden de guía §2. Cada nivel indica qué da por visto.
- Todo el contenido de prop_e §5 M8 está presente: B (modelo, A/B, `u=U/k`, resolución y tolerancias, `s` frente a `s/√n`, Kragten, combinada y expandida, `k≈2` condicional); I (sensibilidades analíticas, covarianzas, `ν_eff` y cobertura, individual/promedio/futuro, doble conteo, cadena, Student y Welch–Satterthwaite con su restricción); A (componentes comunes, límites de linealización, función de incertidumbre sobre el intervalo, CMC). La explicación de `√576` (B) está en I (R05).
- Marcadores de práctica: B (L95), I (L187), A (L237), con títulos que siguen prop_e §5. Ningún marcador falta y ninguna práctica está desarrollada.
- Exclusiones de prop_e §6: no aparecen GGMR con `V_xy ≠ 0`, PCR/PLS, Allan, ISO 13528, KCRV combinado ni protocolo BIPM. Monte Carlo se menciona solo para remitir a M13 (A2). Correcto.
- Errores críticos de prop_e §8 cubiertos en el texto: u frente a U, signo de correcciones y covarianzas, dependencias, Welch–Satterthwaite con covarianzas, valores simulados rotulados.
- Rótulos de origen: todos los conjuntos de datos y resultados están marcados como simulados o propios. No encontré ningún resultado simulado atribuido a CALAIRE.
- Observación para la guía (no es error del libreto): guía §1 muestra el marcador de práctica en bloque doble (`> > **[PRÁCTICA …]**`) y guía §2 y el libreto usan bloque simple. Conviene unificar la guía.

## Resumen

- **Crítica:** 0.
- **Mayor:** 8 (R01–R08): un valor distinto en el mismo ejemplo (R01); fórmula de `ν_eff` con `u_i` en lugar de `c_i u_i` (R02); cita de Kragten que no lo respalda (R03); CMC sin definición ni referencia (R04); explicación de `√576` ausente del nivel B (R05); `q` en lugar de `x̂` y varias denominaciones (R06); `s` en lugar de `s_r` (R07); fórmulas en línea sin LaTeX (R08).
- **Menor:** 8 (R09–R16): claves de referencia no normalizadas, anexos sin entrada en la lista, cita vaga de linealización, falta de línea en blanco antes de «## Nivel A», símbolo `u`/`u_c`, frases largas, AX.13 fuera de alcance, `δ` Unicode.
- Los cálculos de los ejemplos son correctos salvo R01. La estructura y el alcance de prop_e están cubiertos, con la salvedad de R05. Las cifras y referencias restantes de la muestra se corresponden con los documentos.
