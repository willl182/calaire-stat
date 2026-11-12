# Revisión de redacción y errores: M01. Modelo de medición y variables de análisis

Revisor: Haiku. Objeto: `curso/S1_fundamentos/M01_libreto.md` (197 líneas). El libreto no se modificó. Las líneas citadas son las del archivo.

## Plan de revisión

**Lectura.** `curso/guia_libreto.md` (§1 a §8), `prop_e.md` (§1 a §4, §5 M1, §6, §8), `M01_libreto.md` completo y `curso/S1_fundamentos/calc/M01_modelo_variables.py`. Consulté `M01_bitacora_luna.md` solo para ver qué referencias declara.

**Cálculos (c).** Ejecuté el script con `curso/.venv/bin/python -I` y recalculé de forma independiente todas las cifras de los ejemplos (B, I y A). Compare cada cifra del libreto con el valor recalculado.

**Referencias (d).** Extraje texto con `pdftotext -layout` de `docs/JCGM_GUM_6_2020.pdf`, `docs/nistir6963.pdf` y `docs/Appendix D to Part 50_ Title 40 (up to date as of 10-16-2026).pdf`, y de la GUM 1995 (`ISO_IEC Guide 98-3_2008 … (GUM_1995) - libgen.li.pdf`). Comprobé el numeral de cada cita del libreto. También busqué el valor 1,1329 en los PDF de Daumont y Malicet.

**Formato (c).** Con grep comprobé viñetas, etiquetas de acotación, marcadores de práctica, separador decimal y uso de código frente a LaTeX. Medí las frases de la narración con 38 palabras o más.

**Alcance (e).** Cotejé cada tema de prop_e §5 M1 (B, I y A) con sus escenas. Busqué en el libreto los términos excluidos por prop_e §6.

**Redacción (a) y errores (b).** Leí el texto completo. Revisé ortografía, puntuación, claridad para leer en voz alta, terminología, notación y coherencia interna.

## Hallazgos

| id | Ubicación (escena y texto citado) | Tipo | Severidad | Problema | Corrección propuesta |
|---|---|---|---|---|---|
| R01 | Escena B3. «[prop_e §5, M1-B; GUM-6 5.4]» (l. 78); «[cálculos: `calc/M01_modelo_variables.py`; GUM-6 5.4]» (l. 92); «[GUM-6 5.4]» (l. 96) | referencia | mayor | GUM-6 §5.4 trata de cómo se usa el modelo según su forma matemática (propagación, Monte Carlo). No define la sensibilidad. La definición está en la GUM 5.1.3, que comprobé en el PDF de la GUM 1995 de `docs/`: las derivadas parciales «describe how the output estimate y varies with changes in the input estimates». También está en el glosario de GUM-6, Anexo A, símbolo `c`. | Sustituir por [GUM 5.1.3] en l. 78, 92 y 96. Añadir [GUM-6 Anexo A] a la definición de `c_i`. Incluir la entrada «GUM» en «Referencias del capítulo» (ver R12). |
| R02 | Escena A1. «[prop_e §5, M1-A; GUM-6 5.4]» (l. 154); «[GUM-6 5.4; AX.2]» (l. 160 y 166); «[prop_e §5, M1-A; GUM-6 5.4]» (l. 168) | referencia | mayor | El tratamiento de entradas comunes que se correlacionan es la GUM 5.2.2. Comprobé en el PDF: «When the input quantities are correlated, the appropriate expression for the combined variance u_c²(y) …». GUM-6 §5.4 solo menciona la matriz de covarianza de forma incidental. | Cambiar a [GUM 5.2.2] en las cuatro citas. Mantener [AX.2] para la deducción. |
| R03 | Escena B2. «…formula la misma conversión como concentración en ppm y da el coeficiente de absorción de 304,39 atm⁻¹ cm⁻¹ a 0 °C y 1 atm en 40 CFR 50, Appendix D §4.1.» (l. 64) | referencia / error | mayor | §4.1 da el coeficiente 304,39 y la ley de Beer-Lambert con `c` en atm (comprobado). La concentración en ppm (ecuación 4) está en §4.5.3.10, no en §4.1. Esa ecuación no es solo una conversión: usa temperatura en K, presión en torr y el factor de pérdidas `L` (§4.5.2.5). Por eso «la misma conversión» es inexacto. La simplificación de l. 72 también omite `L`, pero el texto no lo dice. | Reescribir: «…da 304,39 atm⁻¹ cm⁻¹ a 0 °C y 1 atm en §4.1; la concentración en ppm, con temperatura, presión y pérdidas de ozono, aparece en §4.5.3.10 (ecuación 4).» En l. 72, añadir que la simplificación omite también el factor de pérdidas. Actualizar la ficha (l. 14) y la referencia de l. 195 con §4.5.3.10. |
| R04 | Escena I. «Comparemos ahora dos pares numéricos …: 1,147 dividido por 1,1329» (l. 130). «Los valores de sección eficaz y sus unidades deben acompañar el contexto de uso» (l. 134). | unidades / terminología | mayor | Ni 1,147 ni 1,1329 llevan unidad. NISTIR 6963 §8 da 1,147 × 10⁻¹⁷ cm² por molécula, equivalente a 308,32 atm⁻¹ cm⁻¹ (comprobado). En B el mismo número se llama «coeficiente de absorción» (l. 82) y en I «sección eficaz». El lector no ve que σ (cm²) y α (atm⁻¹ cm⁻¹) son magnitudes relacionadas pero distintas. | En l. 130 escribir «secciones eficaces 1,147 y 1,1329, en 10⁻¹⁷ cm² por molécula» (la unidad de 1,1329 se confirma según R05). Antes del par, explicar: «el coeficiente de 308,32 atm⁻¹ cm⁻¹ es la misma cantidad que 1,147 × 10⁻¹⁷ cm² por molécula, según NISTIR 6963 §8». Mantener la advertencia de que los dos cocientes no son iguales. |
| R05 | Ficha, fila «Datos de los ejemplos» (l. 12): «Los valores de sección eficaz 1,147 y 1,1329; 308,32 y 304,39 se toman de prop_e.md M1/I; el nuevo coeficiente 304,39 también se verifica en 40 CFR 50, Appendix D §4.1» | referencia | mayor | prop_e es el documento curricular, no una fuente numérica. 1,147 y 308,32 están en NISTIR 6963 §8 (comprobado), y la ficha no lo dice. 304,39 está en Appendix D §4.1 con ±0,94 (comprobado). 1,1329 no aparece en `nistir6963.pdf`, en Appendix D ni en los PDF de Daumont y Malicet (búsqueda de «1,1329» y «1.1329» sin resultados). «El nuevo coeficiente» no lo sostiene ningún documento de `docs/`. | Sustituir por: «1,147 × 10⁻¹⁷ cm² por molécula = 308,32 atm⁻¹ cm⁻¹ (NISTIR 6963 §8); 304,39 atm⁻¹ cm⁻¹ ± 0,94 (40 CFR 50, Apéndice D §4.1); 1,1329: pendiente de verificación en `docs/`». Buscar 1,1329 en Daumont 1992 o Malicet 1995 y citar el numeral solo si se confirma; si no, anotarlo como pendiente en la bitácora. |
| R06 | Todo el capítulo. Ejemplos: l. 48 «`e=y−x`»; l. 60 «`c=−ln(T)/(αL)`»; l. 92 «`T`», «`α`» y «`L`»; l. 120 «`y=sx`»; l. 124 «`e/x`» | formato libreto | mayor | La guía §4 pide fórmulas en LaTeX (`$…$` en línea). El libreto tiene 101 segmentos en código y 20 fragmentos en LaTeX. Usa las dos notaciones en el mismo capítulo: la pizarra en LaTeX y la narración en código. Además, el código no se lee bien en voz alta. | Pasar a `$…$` toda expresión con operadores (p. ej. `$e=y-x$`, `$c=-\ln(T)/(\alpha L)$`, `$y=sx$`, `$e/x$`). Las variables sueltas también pasan a `$x$`, `$\alpha$`, `$L$`. Las unidades pueden quedar en `\mathrm{}` como en l. 62 y l. 68. |
| R07 | Escena B2: «puede escribirse como `c=−ln(T)/(αL)`: `T` es transmitancia…» (l. 60). Escena B3: «Diferencia finita: $(f(X+h)-f(X))/h$…» (l. 94). Escena I1: «escribimos `y=sx`» (l. 120). | formato libreto | mayor | La guía §4 exige que las fórmulas se escriban y se lean en voz alta en la narración. Estas tres no se leen. La narración dice «puede escribirse como» o «escribimos» y no pronuncia la expresión. | Añadir una frase hablada tras cada una. l. 60: «c es igual a menos el logaritmo natural de T, dividido entre alfa por L». l. 94: «el cambio de salida, entre el cambio de entrada: f de X más h, menos f de X, dividido entre h». l. 120: «y es igual a s por x». |
| R08 | Escena I1: «El cociente entre coeficientes expresa el factor de escala de la salida en ese modelo inversamente proporcional.» (l. 134) | redacción | menor | Frase rota. «Inversamente proporcional» queda suelto y no se entiende a qué se refiere. | «En ese modelo la salida es inversamente proporcional al coeficiente; por eso el cociente entre dos coeficientes es el factor de escala de la salida.» |
| R09 | Escena B1: «el sesgo responde a una pregunta de centro» (l. 36) | redacción / claridad | menor | «Pregunta de centro» no está definida y el oyente no tiene cómo interpretarla. | «el sesgo responde a una pregunta sobre la posición de los errores: en las condiciones estudiadas, ¿tienden a quedar por encima o por debajo de cero?» |
| R10 | Escena B3: «Si cambian a la vez sección eficaz, presión, longitud y transmitancia» (l. 88) | coherencia | menor | El modelo del capítulo no tiene presión como entrada. El factor de temperatura y presión se fija en uno (l. 60 y l. 66). | «…sección eficaz (o coeficiente), longitud, transmitancia o factor de temperatura y presión». |
| R11 | Escena «Señales de escalamiento» del nivel B (l. 108): «Cuando trabajen con este procedimiento en el nivel B, deténganse y consulten si no pueden identificar qué magnitud se está informando, si no conocen la unidad de una entrada, …» (53 palabras) | redacción (voz) | menor | Frase demasiado larga para leer en voz alta. El oyente pierde la lista de condiciones antes de llegar al verbo final. | Dividir en tres o cuatro frases cortas, conservando el mismo contenido. Por ejemplo: «Cuando trabajen en el nivel B, deténganse y consulten. Deténganse si no pueden identificar qué magnitud informan o qué unidad tiene una entrada.» |
| R12 | Ficha (l. 14) y «Referencias del capítulo» (l. 195): «40 CFR 50, Appendix D». La GUM (98-3) no aparece en «Referencias del capítulo». | referencia | menor | La guía §5 pide que cada cita use una clave de su tabla. «40 CFR 50, Appendix D» no tiene clave en esa tabla. La GUM 98-3, necesaria para R01, no figura en la lista del capítulo. | Añadir una clave para Appendix D a la tabla de §5 (p. ej. «CFR50-D») y usarla en la ficha y en el texto. Añadir la entrada «GUM» en «Referencias del capítulo» si se aplica R01. La tabla de §5 pertenece a la guía, así que el cambio lo decide quien la mantiene. |

## Verificaciones hechas

**Cálculos (script ejecutado y recalculo independiente).**

| Cifra del libreto | Valor recalculado | Resultado |
|---|---|---|
| `e = 421,3 − 420,0 = +1,3`; corrección `x−y = −1,3` (l. 30 a 42) | 1,30; −1,30 | OK |
| `x = 499,845853` y «499,846» (l. 66, 68) | 499,8458531636 | OK |
| `493,475` con α = 308,32 (l. 82) | 493,474569 | OK (redondeo) |
| Diferencia `+6,371` y `1,291 %` (l. 82) | 6,371284; 1,291107 % | OK |
| `−37 004,286` por unidad de T (l. 92) | −37 004,2864 | OK |
| `−1,642` por atm⁻¹ cm⁻¹ (l. 92) | −1,642069 | OK |
| 100 → 101,29 (+1,29); 500 → 506,45 (+6,45); `e/x = +1,29 %` en ambos (l. 122 a 128) | 101,29; 506,45; 1,29 % | OK |
| `1,147/1,1329 = 1,012446`; incremento `1,2446 %` (l. 130) | 1,01244594; 1,244594 % | OK |
| `308,32/304,39 = 1,012911`; incremento `1,2911 %` (l. 130) | 1,01291107; 1,291107 % | OK |
| Descomposición `2,3`, `1,9`, `Δ=0,4` (l. 156 a 164) | 2,3; 1,9; 0,4 | OK |

**Referencias (`pdftotext`, 13 numerales o pasajes comprobados).**

| Cita del libreto | Resultado de la comprobación |
|---|---|
| GUM-6 §5.1 (mensurando, modelo, entradas, salida) | OK |
| GUM-6 §5.2, ecuación (1): `Y = f(X₁,…,X_N)` | OK |
| GUM-6 §5.4 usada para sensibilidad (l. 78, 92, 96) | **No respalda la afirmación** (R01) |
| GUM-6 §5.4 usada para correlación (l. 154 a 168) | **No respalda la afirmación** (R02) |
| GUM-6 §5.6 y §5.8 (adecuación al uso; dominio de validez) | OK |
| GUM-6 §6.1 (elección del mensurando según el propósito) | OK |
| GUM-6 Anexo A, símbolo `c` (sensitivity coefficient) | OK. No se cita aún; propuesto en R01 |
| GUM 1995 §5.1.3 (coeficientes de sensibilidad) | OK. Propuesto en R01 |
| GUM 1995 §5.2.2 (magnitudes de entrada correlacionadas) | OK. Propuesto en R02 |
| NISTIR 6963 §8 (relación de medida, factor de temperatura y presión, 308,32 atm⁻¹ cm⁻¹ = 1,147 × 10⁻¹⁷ cm²/molécula) | OK |
| NISTIR 6963: autores (Paur, Bass, Norris, Buckley) y año (febrero de 2003) | OK |
| 40 CFR 50, Appendix D §4.1 (304,39 atm⁻¹ cm⁻¹ a 0 °C y 1 atm, ±0,94; Beer-Lambert con `c` en atm) | OK |
| 40 CFR 50, Appendix D: concentración en ppm | **Ubicación incorrecta**: §4.5.3.10, ecuación 4 (R03) |
| Valor 1,1329 en `docs/` (NISTIR, Appendix D, Daumont y Malicet) | **No encontrado** (R05) |
| VIM, JCGM 106, ILAC-G8 | No verificables: no están en `docs/` (correctamente marcados como tales) |

**Formato y estructura (c).**

- Estructura de la guía §2: ficha, nivel B con «Señales de escalamiento», nivel I y nivel A con «qué se da por visto», cierre y referencias. OK.
- Etiquetas de acotación: solo se usan las permitidas (DIAPOSITIVA, PIZARRA, PREGUNTA AL GRUPO, EJEMPLO, ERROR CRÍTICO, ESCALAMIENTO, TRANSICIÓN, PRÁCTICA). OK.
- Viñetas: solo en la lista de «Referencias del capítulo», que la guía admite. El contenido narrado no tiene viñetas. OK.
- Marcadores de práctica: tres, uno por nivel (B en l. 104, I en l. 144, A en l. 180), con el formato de la guía y sin desarrollo. OK.
- Separador decimal: sin cifras con punto decimal en el texto narrado. OK.
- Notación y fórmulas: no cumple (R06 y R07).
- Frases largas: solo una frase supera las 38 palabras (l. 108, 53 palabras; R11).

**Alcance (e).**

- Nivel B: mensurando, error, sesgo y corrección; `Y=f(X₁,…,X_N)`; sensibilidad numérica en plantilla; caso SRP con conversión a nmol/mol. Presente. Práctica marcada.
- Nivel I: cambio de escala como cambio de parámetro; efecto sobre `e` y sobre el error relativo con denominador; diferencia entre cambiar la escala y corregir el instrumento. Presente. Práctica marcada.
- Nivel A: entradas comunes; efecto en una diferencia frente a un resultado absoluto; preparación de M8 y M9. Presente. Práctica marcada.
- Exclusiones de prop_e §6 (Allan, PCR/PLS, ISO 13528, KCRV, BIPM.QM-K1, GGMR con `V_xy ≠ 0`, Monte Carlo como contenido): no aparecen en el libreto. OK.
- Nada del nivel A aparece en B ni I como contenido propio. OK.

## Resumen

El capítulo no tiene errores de cálculo: las 11 familias de cifras coinciden con el script y con mi recálculo independiente. Tampoco tiene contenidos de más ni de menos frente a prop_e M1 en los tres niveles, y respeta las exclusiones de §6.

Los problemas están en las referencias (R01, R02, R03 y R05), donde el numeral citado no respalda la afirmación o la ubicación es incorrecta, y en el valor 1,1329, que no tiene fuente comprobada en `docs/`. También hay problemas de unidades (R04) y de convención de formato y lectura en voz alta (R06 y R07). Los hallazgos menores son de redacción y de coherencia (R08 a R12).

Recomiendo corregir primero R05 y R03, porque afectan a datos y a referencias que el alumno puede verificar.

**Hallazgos por severidad:** crítica 0 · mayor 7 · menor 5
