# Revisión de las prácticas de M01 (B, I, A)

Revisor: Haiku 5.5 (solo lectura; no se modificó ningún libreto ni script).
Alcance: `curso/S1_fundamentos/M01_libreto.md` (bloques `[PRÁCTICA]` de B, I y A), `curso/S1_fundamentos/calc/M01_practicas_luna.py`, `curso/logs/M01_practicas_luna.md`. Referencias y citas no auditadas (las trabaja otro supervisor).

## Verificación ejecutada

- `curso/.venv/bin/python curso/S1_fundamentos/calc/M01_practicas_luna.py`: rc=0. Cifras impresas: B 100,000 → 101,291; 250,000 → 253,228; 500,000 → 506,456 nmol/mol; ΔY +1,291 / +3,228 / +6,456; cambio relativo +1,2911068 % en los tres puntos. I: 1,147/1,1329 = 1,012445935 (+1,2445935 %); 308,32/304,39 = 1,012911068 (+1,2911068 %). A: Y1 = 2,3, Y2 = 1,9, Δ = 0,4; con sensibilidad 0,8, Y2 = 1,5 y Δ = 0,8.
- `curso/.venv/bin/python curso/S1_fundamentos/calc/M01_modelo_variables.py`: rc=0.
- `git diff -- curso/S1_fundamentos/M01_libreto.md`: solo se eliminan los tres marcadores `[PRÁCTICA — fase de ejercicios]` y se añaden los bloques B, I y A. El resto del archivo no cambia en este diff. `git diff --check`: sin errores.
- Recalculo independiente de todas las cifras de los bloques (tablas, solución B, solución I, solución A, y las cifras de escenas B3, I1 y A1 que los bloques citan): coinciden con el libreto dentro del redondeo mostrado. Coma decimal correcta en todos los bloques nuevos. Sin gráficos.
- Comprobación de alcance contra `prop_e.md` §2, §5 (M1), §6 y §8.

## Hallazgos

### H-01 — Medio — I: el par implementado no se declara (prop_e §5, M1-I)
- **Ubicación:** `M01_libreto.md` líneas 170–174 (enunciado y solución de I). El marcador original decía «con el par declarado».
- **Problema:** prop_e dice que el ejercicio «declara cuál usa» el valor implementado. El enunciado presenta los dos pares sin decir cuál se implementó, y la tarea (4) pregunta qué hacer si no se sabe. Sin embargo, la solución toma en silencio que la salida de referencia $x=400,0$ se obtuvo con $\alpha=308,32$ y la salida reescalada se obtuvo con $\alpha=304,39$. Si el operador invierte esa suposición, el signo de $e$ cambia.
- **Corrección propuesta:** añadir al enunciado de I una frase explícita, por ejemplo: «El par implementado en la escala de esta comparación es α = 308,32 → 304,39 atm⁻¹cm⁻¹; el valor base simulado x = 400,0 nmol/mol corresponde a la salida con 308,32 y la salida y se calcula con 304,39.» Dejar la tarea (4) como caso de contraste. No cambiar las cifras.

### H-02 — Medio — I: las cifras de la solución no las reproduce el script que se cita (guía §8; prop_e §8)
- **Ubicación:** `M01_libreto.md` línea 174 (405,164; e = +5,164; 100e/x = +1,2911 %) y línea 178 («`calc/M01_practicas_luna.py` reproduce ambos cocientes y porcentajes; la multiplicación por 400,0 verifica el resultado aplicado»). También `logs/M01_practicas_luna.md` línea 14.
- **Problema:** el script solo imprime los cocientes e incrementos de I (`calc/M01_practicas_luna.py` líneas 33–38). No calcula $y$, $e$ ni $100e/x$ para $x=400,0$. Las cifras son correctas (recalculadas: 400 × 308,32/304,39 = 405,1644; e = 5,1644; 100e/x = 1,29111 %), pero la afirmación de reproducibilidad no está respaldada por el script, y la bitácora la da por verificada.
- **Corrección propuesta:** añadir al script, después de la línea 38, el cálculo `y = 400.0 * ratio`, `e = y - 400.0` y `100 * e / 400.0`, con una aserción `isclose` frente a 405,164, 5,164 y 1,2911. O bien corregir la frase de la línea 178 y la bitácora para que no atribuyan al script ese cálculo.

### H-03 — Medio — B: no hay evidencia para error con signo, sesgo, corrección ni conversión explícita (prop_e §8)
- **Ubicación:** `M01_libreto.md` líneas 104–126 (bloque B). Enunciado de B en línea 106.
- **Problema:** prop_e §8 exige que cada contenido separado por punto y coma tenga al menos una evidencia observable. El contenido de B incluye «mensurando, error, sesgo, corrección» y «conversión explícita a nmol/mol». La práctica solo evidencia la sensibilidad numérica (ΔY y cambio relativo). El operador no tiene que calcular ningún $e=y-x$ con signo ni una corrección aditiva, ni tiene que hacer la conversión a nmol/mol: la fórmula ya incluye $\times10^9$ y la solución la aplica sin pedirla.
- **Corrección propuesta:** añadir una tarea (4): tomar $Y_2$ como indicación y $Y_1$ como referencia del mismo punto, calcular $e=Y_2-Y_1$ con signo y la corrección aditiva que lleva $Y_2$ a $Y_1$ (signo opuesto); pedir además que expliquen en un punto la conversión de la salida en atm a nmol/mol. Añadir su solución (e = +1,291; +3,228; +6,456 nmol/mol; corrección −1,291; −3,228; −6,456 nmol/mol) y ajustar el criterio de logro. Con $Y_1$ frente al objetivo el error sería nulo, así que no sirve como evidencia.

### H-04 — Bajo — B: el título y la magnitud no coinciden con el marcador de prop_e
- **Ubicación:** `M01_libreto.md` línea 104 (título «Sensibilidad de tres concentraciones a la sección eficaz») y línea 106 («dos coeficientes declarados»).
- **Problema:** el marcador original habla de «dos valores de sección eficaz declarados», pero los datos son coeficientes de absorción $\alpha$ (atm⁻¹cm⁻¹). No se dice que $\alpha = \sigma \cdot n_0$, así que el título y el enunciado usan términos distintos para la misma magnitud.
- **Corrección propuesta:** título «Sensibilidad de tres concentraciones al coeficiente de absorción (sección eficaz declarada)». En el enunciado, una frase: «α se relaciona con la sección eficaz σ por un factor de número molecular constante; aquí trabajamos directamente con α, como en la ecuación del capítulo.»

### H-05 — Bajo — I y A: origen de los datos sin rótulo en el enunciado (guía §4)
- **Ubicación:** `M01_libreto.md` línea 170 (I: «dos pares numéricos declarados»); la ficha (línea 12) ya da las fuentes.
- **Problema:** los pares 1,147/1,1329 y 308,32/304,39 son valores **publicados** (NISTIR 6963 §8; 40 CFR 50 App. D §4.1; BIPM-K1 p. 3), pero el enunciado solo los llama «declarados». La guía §4 exige el rótulo de origen en cada conjunto de datos. Los valores base de 400,0 nmol/mol y las secciones con la regla de B están bien rotulados como simulados.
- **Corrección propuesta:** en el enunciado de I, añadir «(valores publicados; ver ficha)» junto a cada par, sin repetir las referencias bibliográficas.

### H-06 — Bajo — I: diferencia entre los dos incrementos sin explicar
- **Ubicación:** `M01_libreto.md` línea 176 («los dos pares no producen incrementos idénticos»).
- **Problema:** el incremento de la sección (+1,2446 %) y el de α (+1,2911 %) difieren. No es un error de cálculo: el cociente α/σ implícito en cada fuente es 308,32/1,147 = 268,81 y 304,39/1,1329 = 268,68 (en unidades de 10¹⁷ · atm⁻¹ · cm⁻¹ · cm⁻² · molécula, es decir, por molécula por cm³ a 1 atm), y difieren en un 0,05 %. Sin esa explicación, un operador puede sospechar de un error en el cálculo.
- **Corrección propuesta:** añadir una frase en la solución de I: «La diferencia proviene de que cada fuente declara su par con redondeo y constantes propias; el cociente α/σ implícito difiere en un 0,05 % entre ambas. No es un error de cálculo ni una corrección del instrumento.»

### H-07 — Bajo — A: la conclusión pedida no está escrita en la solución (prop_e §5, M1-A)
- **Ubicación:** `M01_libreto.md` línea 218 (pide «qué se puede y qué no se puede afirmar») y solución en líneas 220–222.
- **Problema:** la solución da los valores y la decisión operativa, pero no responde explícitamente a la pregunta del enunciado.
- **Corrección propuesta:** añadir en la solución: «Se puede afirmar que, bajo el modelo idealizado, la contribución común desaparece de Δ y que Δ = 0,4 nmol/mol. No se puede afirmar que u(Δ) sea menor que la de cada resultado absoluto, ni cuantificar la incertidumbre de Δ sin un modelo conjunto de covarianzas.»

### H-08 — Bajo — Script: estilo de importación y uso de `__import__`
- **Ubicación:** `calc/M01_practicas_luna.py` líneas 4 y 13–16.
- **Problema:** `__import__("math").exp(...)` dentro de una comprensión es poco idiomático y oculta la dependencia; `exp` podría importarse junto a `isclose` y `log`.
- **Corrección propuesta:** `from math import exp, isclose, log` y usar `exp(...)` directamente.

### H-09 — Bajo — B: la regla de generación está en el enunciado
- **Ubicación:** `M01_libreto.md` línea 106.
- **Problema:** el enunciado escribe $T=\exp[-\alpha_1 L(c/10^9)p_0]$ y los objetivos 100, 250 y 500. El operador puede recuperar los objetivos invirtiendo la regla, así que la «comprobación inversa» de la solución es circular para quien conoce la regla.
- **Corrección propuesta:** o bien dejar la regla en una nota para el instructor (`[NOTA AL INSTRUCTOR]`) y mantener en el enunciado solo las T de la tabla, o bien dejarlo explícito y quitar la frase «la comprobación inversa recupera…» de la solución.

## Lo que se verificó sin hallazgos

- Todas las cifras de las tablas de B, las cifras de I (incluidas las de la escena I1: 6,73477; 1,31677; 0,309524 %) y las de A coinciden con la ejecución y el recálculo.
- Signos correctos: α en el denominador ⇒ la salida aumenta cuando α disminuye; la razón Y2/Y1 = α1/α2 se comprueba en el script.
- Cambio de escala y corrección se distinguen en I; el porcentaje declara su denominador en los tres bloques.
- A: la cancelación de la contribución común es exacta bajo igual sensibilidad; la cancelación parcial (sensibilidad 0,8) da Δ = 0,8 nmol/mol; el script lo afirma.
- Ninguna práctica usa datos propios ni atribuye simulaciones a CALAIRE. Sin gráficos. Ninguna deducción se desarrolla en el bloque; se remite a AX.2.
- Coma decimal en los bloques nuevos; unidades nmol/mol.

## Resumen

Nueve hallazgos: tres medios (H-01 par implementado no declarado en I; H-02 cifras de I no reproducidas por el script citado; H-03 falta evidencia para error/sesgo/corrección/conversión en B) y seis bajos (H-04 a H-09). Ninguno afecta a los números presentados; H-01 y H-02 afectan a la trazabilidad del caso I y deberían corregirse antes de dar el bloque por cerrado. No se editó ningún archivo distinto de este informe.
