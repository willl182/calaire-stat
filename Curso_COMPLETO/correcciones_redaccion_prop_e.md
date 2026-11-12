# Correcciones de redacción de prop_e.md

Revisión de redacción y coherencia de `prop_e.md`. No se han cambiado el contenido curricular, el alcance de los niveles B, I y A, las inclusiones y exclusiones ni la estructura. La numeración de líneas es la del archivo original, porque no se han añadido ni eliminado líneas.

## 1. Cambios realizados

| Ubicación | Texto original | Texto corregido | Tipo |
|---|---|---|---|
| L10 (§1) | Este es un **curso de estadística**. | Es un **curso de estadística**. | estilo |
| L42 (§3) | Al cerrar, entrega resultado con unidades, interpretación estadística y acción. | Al cerrar, se entrega el resultado con unidades, interpretación estadística y acción. | estilo |
| L52 (§4) | El orden M9 → M10 → M11 → M12 se mantiene por prerrequisitos: | El orden M9 → M10 → M11 → M12 se mantiene porque hay prerrequisitos: | estilo |
| L60 (M0, B) | datos faltantes; ceros negativos; separación | datos faltantes; lecturas negativas del cero; separación | estilo (expresión ambigua; coincide con «Conservar los negativos del cero» de L83) |
| L82 (M2, B) | CV y su límite cerca de cero | coeficiente de variación (CV) y su límite cerca de cero | coherencia (sigla sin desarrollar en primer uso) |
| L83 (M2, B) | en un nivel medido varios días | en un nivel medido durante varios días | estilo |
| L84 (M2, I) | `e = a + (b − 1)·x` conserva tendencia con `x` si hay sesgo proporcional. | `e = a + (b − 1)·x` muestra tendencia con `x` si hay sesgo proporcional. | estilo (el verbo «conservar» no describe lo que ocurre) |
| L87 (M2, A) | (caso R&R) | (caso R&R: repetibilidad y reproducibilidad) | coherencia (sigla sin desarrollar en primer uso) |
| L93 (M3, B) | Límite de `1/√n` cuando hay un componente común o deriva. | La reducción con `1/√n` tiene límite cuando hay un componente común o deriva. | estilo (fragmento sin verbo) |
| L111 (M4) | no se mezclan concentraciones en una t pareada única. | no se mezclan concentraciones en una única prueba t pareada. | estilo |
| L143 (M7, B) | OLS con intercepto en un caso con condiciones adecuadas | mínimos cuadrados ordinarios (OLS) con intercepto en un caso con condiciones adecuadas | coherencia (sigla sin desarrollar en primer uso) |
| L145 (M7, I) | WLS y elección de pesos | mínimos cuadrados ponderados (WLS) y elección de pesos | coherencia (sigla sin desarrollar en primer uso) |
| L160 (M8, A) | su relación con la CMC (misma magnitud, unidades y cobertura) | su relación con la capacidad de medición y calibración (CMC; misma magnitud, unidades y cobertura) | coherencia (sigla sin desarrollar en primer uso) |
| L169 (M9, B) | Reconoce que compartir un patrón **no invalida `E_n` en general**, pero impide suponer independencia y usar sin justificación la fórmula que la asume; identifica cuándo se requiere tratar la covarianza. | Reconoce que compartir un patrón **no invalida `E_n` en general**, pero impide suponer independencia: no debe usarse sin justificación la fórmula que la asume, y se identifica cuándo hay que tratar la covarianza. | estilo (frase larga y confusa) |
| L173 (M9, A) | diferencia frente al valor de referencia (KCRV) | diferencia frente al valor de referencia clave (KCRV) | coherencia (sigla sin desarrollar) |
| L173 (M9, A) | No se estudian el protocolo, la organización de la comparación ni la KCDB. | No se estudian el protocolo, la organización de la comparación ni la base de datos de comparaciones clave (KCDB). | coherencia (sigla sin desarrollar en primer uso) |
| L199 (M11, A) | intervalos de recalibración fundados | intervalos de recalibración justificados | estilo |
| L202 (M11) | El historial NIST sirve para aprender el método en su propia serie; | El historial publicado por el NIST sirve para aprender el método en su propia serie; | coherencia (la procedencia de la serie queda explícita, en línea con la rotulación de datos de §3) |
| L227 (§6) | PCR/PLS, aprendizaje automático y quimiometría general | regresión por componentes principales (PCR) y mínimos cuadrados parciales (PLS), aprendizaje automático y quimiometría general | coherencia (sigla sin desarrollar; PCR puede confundirse con la reacción en cadena de la polimerasa) |
| L242 (§7, tabla, caso D, B) | Dos factores preparado | Dos factores con datos preparados | estilo (concordancia) |

Se revisaron también las tildes, la puntuación, el uso de «−» en las fórmulas, la coma decimal, la coherencia de símbolos (`u`, `U`, `k`, `s_r`, `s_entre`, `x`, `y`, `e`, `x̂`, `ν_eff`), la numeración de §1 a §10, la de M0 a M13 y las referencias cruzadas (§6 desde M3; M4-B, M4-I y M6-I; caso C; M8 y M9). No se encontraron errores de ortografía ni enlaces Markdown rotos a archivos existentes. No aparecen las palabras prohibidas («solo lectura», «para mostrar», «opcional»).

## 2. Pendientes técnicos (no corregidos)

1. **L5 y L6, enlaces a `prop_d,md`.** El archivo real se llama `prop_d,md` (coma en lugar de punto). El enlace coincide con el nombre real, así que no se ha tocado. Lo probable es que el nombre correcto sea `prop_d.md`. Corregirlo exige renombrar ese archivo, que está fuera del alcance de esta tarea, y entonces habría que actualizar los dos enlaces.
2. **L130, fórmula `u²(x̄) = s²_entre/d + s²_r/(d·n)`.** La fórmula es correcta solo si `s_entre` es la componente de variación entre días, sin incluir la repetibilidad. Si `s_entre` es la desviación estándar de los promedios diarios, la repetibilidad se cuenta dos veces. Conviene fijar la definición de `s_entre` en §3 o en M6.
3. **L147, GGMR y ISO/TS 28037.** Se atribuye la regresión generalizada de Gauss-Markov a ISO/TS 28037 y se describe como mínimos cuadrados ponderados con la matriz de covarianza completa de `x` e `y`. Hay que verificar la cita y la descripción frente a la norma.
4. **L163, «SRP 27».** La cifra aparece solo en esta frase. Puede ser una referencia intencionada a otro patrón o un error por «SRP 55». Hay que confirmarlo.
5. **L169, `E_n` y dependencia.** La afirmación de que compartir un patrón «no invalida `E_n` en general» depende de cómo se defina `E_n` (con incertidumbres estándar o expandidas) y de la norma aplicable. Hay que verificarla antes de la clase.
6. **L52, covarianza en M10 y M11.** Se afirma que la covarianza de M9 se usa en M10 y M11. En el texto, M10 (A) menciona «decisiones con dependencia», pero M11 solo menciona «dependencia» sin covarianza. Conviene comprobar que M11 realmente la necesita.
7. **L260, «la condición de Allan está resuelta».** §6 condiciona la varianza de Allan a que existan series adecuadas, pero el documento no indica si existen. El estado debe verificarse antes de darlo por resuelto.
8. **L256, «Correcciones previas a la clase».** Esta lista es una nota interna de trabajo dentro de la propuesta. No se ha modificado; conviene decidir si se mantiene en la versión que se entrega.
