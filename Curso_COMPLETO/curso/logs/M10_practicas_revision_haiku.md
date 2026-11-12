# Revisión de prácticas M10 (B, I, A)

Fecha: 2026-10-27. Revisor: Haiku 5.5. Alcance: `curso/S3_comparacion_decision/M10_libreto.md` (bloques `[PRÁCTICA]` B, I y A), `curso/S3_comparacion_decision/calc/M10_practicas_luna.py` y `curso/logs/M10_practicas_luna.md`. No se editaron libretos ni scripts; no se auditaron referencias.

## Verificaciones realizadas

- Ejecución de `curso/.venv/bin/python curso/S3_comparacion_decision/calc/M10_practicas_luna.py`: código 0; todas las cifras impresas coinciden con las de la solución docente de B, I y A.
- Recalculo independiente fuera del repositorio (`/tmp/m10rev_check/check.py`, cuadratura y malla numérica):
  - A, global, g=0: falsa aceptación 0,02646254; falso rechazo 0,02659615. Coincide.
  - A, global, g=1: falsa aceptación 0,00337106; falso rechazo 0,08670579. Coincide.
  - A, θ=10,5 con g=1: 0,00400497 (independiente) y 0,02251044 (con covarianza). Coincide.
  - A, riesgo específico y=0, u=6, previa uniforme truncada en [-12;12]: P(no conforme | y=0) = 0,05246774 (cada cola 0,02623387). Coincide con la solución, **pero el script no lo calcula** (ver H-02).
- I: P(rechazo | θ=9) con g=0 y g=1 (0,10564977 y 0,5) y P(aceptación falsa | θ=10,5) (0,26598553 y 0,03039636) comprobados en forma cerrada. Coinciden.
- B: intervalos [98,8;101,2], [101,0;103,4], [104,8;107,2]; zonas [99,2;101,8] y y<96,8 o y>104,2. Coinciden con la regla suministrada.
- Varianzas: covarianza 0,48 (nmol/mol)²; u(Ȳ) = 0,74833148 con dependencia y 0,56568542 sin ella. Coinciden.
- Alcance: contrastado con `prop_e.md` §2 y §5 (M10). Las tres prácticas corresponden a su nivel (B: certificado y regla suministrada; I: elegir entre dos reglas; A: riesgo global/específico y dependencia). Anclas AX.2, AX.9 y AX.10 existen en `AX_libreto.md`.
- Unidades nmol/mol y coma decimal en el libreto y en la bitácora: correctas.

## Hallazgos

### H-01 — Mayor — Estadístico de decisión indefinido en A

- **Ubicación:** `M10_libreto.md`, bloque `[PRÁCTICA] A` (enunciado, línea del "Enunciado narrado", y tarea "en el punto verdadero θ=10,5 … calculen la falsa aceptación con guarda uno en ambos supuestos").
- **Descripción:** el enunciado dice «La regla acepta una estimación si cae en [-9;9]», es decir, una única estimación. Pero en la tarea de dependencia y en la solución, la falsa aceptación en θ=10,5 se calcula para Ȳ, el promedio de las dos estimaciones (0,00400497 y 0,02251044). Los riesgos globales usan una sola estimación (desviación 0,8). Así, las cifras de falsa aceptación en θ=10,5 con g=1 son 0,0304 (I, una estimación), 0,0040 y 0,0225 (A, promedio): tres valores que parecen comparables y no lo son.
- **Consecuencia:** el alumno no sabe a qué estadístico se aplica la regla y no puede reproducir la comparación con/sin covarianza de forma inequívoca.
- **Corrección propuesta:** en el enunciado de A, definir la decisión: «La regla se aplica al promedio Ȳ = (Y₁+Y₂)/2 de las dos estimaciones» para toda la práctica, y recalcular los riesgos globales sobre Ȳ (σ = 0,56568542 sin covarianza, 0,74833148 con covarianza). Alternativamente, separar explícitamente el caso de una estimación (globales) y el caso del promedio (dependencia), y no comparar sus cifras entre sí. Actualizar la solución y el script en consecuencia.

### H-02 — Mayor — El riesgo específico de A no está en el script y la solución afirma que sí

- **Ubicación:** `M10_libreto.md`, solución docente de A: «Estos números se reproducen con las integrales y fórmulas de `calc/M10_practicas_luna.py`» (la frase cubre 0,05246774 y 0,02623387). Script `calc/M10_practicas_luna.py`, función `a_risks()`.
- **Descripción:** `a_risks()` calcula los riesgos globales, la varianza de Ȳ y P(aceptación | θ=10,5). No calcula el riesgo específico para y=0, u=6 ni sus colas. La bitácora (`curso/logs/M10_practicas_luna.md`) reporta esas cifras como resultados del script.
- **Consecuencia:** una cifra central del caso avanzado (0,05246774) no es reproducible con el código del capítulo; la afirmación de reproducibilidad de la solución es falsa para ese número. (El valor sí es correcto: lo confirmé por cálculo independiente.)
- **Corrección propuesta:** añadir a `a_risks()` el cálculo de la posterior truncada (φ(θ/6) en [-12;12], normalizada) con P(|θ|>10 | y=0) y sus dos colas, e incluir una aserción que verifique la suma conforme + no conforme = 1. Alternativamente, retirar la frase de reproducibilidad para ese número.

### H-03 — Medio — Riesgo específico sin decisión explícita

- **Ubicación:** `M10_libreto.md`, bloque A, enunciado («Para riesgo específico bilateral, consideren además el ejemplo de una medición y=0, u=6») y solución.
- **Descripción:** el ejercicio habla de «riesgo de una decisión», pero el riesgo específico que se calcula, P(no conforme | y=0) = 0,0525, no depende de la regla de aceptación. No se indica si y=0 se acepta con g=1 (y=0 está dentro de [-9;9], así que se acepta). Como y=0 se acepta, el riesgo específico de **falsa aceptación dado el resultado** es precisamente 0,0525; el texto no lo dice.
- **Consecuencia:** el alumno puede confundir P(no conforme | y) con un falso rechazo o con el riesgo global, y el criterio de logro («distingue los riesgos condicionales y globales») no queda verificado.
- **Corrección propuesta:** añadir a la solución: «y=0 queda dentro de [-9;9]: la regla acepta; por tanto el riesgo específico de falsa aceptación dado y=0 es P(θ fuera de [-10;10] | y=0) = 0,05246774». Y en el enunciado, aclarar que la pregunta es el riesgo específico asociado a la decisión tomada.

### H-04 — Medio — Resultado observado y=9 de I introducido y no resuelto

- **Ubicación:** `M10_libreto.md`, bloque `[PRÁCTICA] I`, enunciado («El resultado observado es y=9») y solución.
- **Descripción:** el enunciado pide «resolver un resultado próximo al límite con dos reglas», pero la solución nunca dice qué decide cada regla para y=9. Sin guarda, y=9 queda dentro de [-10;10]: se acepta. Con guarda g=1, y=9 cae exactamente en el borde de [-9;9]; el texto no indica si el límite es inclusivo. Las probabilidades calculadas son condicionadas a θ y no sustituyen la decisión sobre y=9.
- **Consecuencia:** el criterio de logro («resolver…») no se puede verificar; el borde inclusivo queda sin definir.
- **Corrección propuesta:** añadir en la solución: «Con g=0, y=9 se acepta. Con g=1, y=9 está en el límite: declarar la convención (p. ej., aceptar si |y| ≤ 9, inclusivo) o retener; las probabilidades anteriores describen el riesgo de la regla, no la decisión sobre este resultado». Fijar la convención de límite en el enunciado.

### H-05 — Medio — Bitácora afirma comprobaciones que el script no ejecuta

- **Ubicación:** `curso/logs/M10_practicas_luna.md`, sección «Ejecución», línea «Comprobaciones programáticas: aserciones de varianza/covarianza, suma de colas bilaterales, simetría y resultados I». Script `calc/M10_practicas_luna.py`.
- **Descripción:** el script contiene aserciones de B (u=0,6; extremos 98,8/101,2), de I (una sola: 0,10564977) y de A (varianzas). No hay aserciones sobre la suma de colas bilaterales ni sobre simetría. La afirmación de la bitácora es inexacta.
- **Consecuencia:** el registro de verificación sobrestima lo que se comprobó.
- **Corrección propuesta:** o bien añadir las aserciones citadas al script (suma de colas = integral total; simetría de la cola en ±10; resultados I y riesgo específico de H-02), o bien corregir la bitácora para describir solo lo que el script verifica.

### H-06 — Menor — Ausencia de recomendación verificable en I

- **Ubicación:** `M10_libreto.md`, bloque I, enunciado («El equipo cliente solicita una recomendación…») y solución («Si la prioridad es reducir falsa aceptación…»).
- **Descripción:** el enunciado pide «escoger» y una recomendación; la solución da una recomendación condicional sin cifras de comparación explícitas. El alumno no sabe qué respuesta concreta se espera.
- **Corrección propuesta:** añadir una frase verificable: «Si la falsa aceptación en θ=10,5 es el riesgo prioritario, g=1 reduce P_FA de 0,2660 a 0,0304, a costa de P_FR en valores conformes cercanos al límite (0,50 en θ=9)». Esto mantiene la recomendación condicionada sin imponerla.

### H-07 — Menor — Origen de los datos de B no reproducible desde el script

- **Ubicación:** `M10_libreto.md`, bloque B, enunciado («Los números siguientes son simulados mediante una regla reproducible»).
- **Descripción:** los resultados 100,0; 102,2 y 106,0 son constantes fijadas a mano, no generadas por una regla. El texto llama «regla reproducible» a una lista de constantes.
- **Corrección propuesta:** decir «valores fijados en `calc/M10_practicas_luna.py` (`b_interval_decisions`)» en lugar de «mediante una regla reproducible», o describir la regla de generación si la hay.

### H-08 — Menor — Afirmación de validación de paleta sin artefacto

- **Ubicación:** `curso/logs/M10_practicas_luna.md`, sección «Ejecución»: «validación de paleta ejecutada … pasaron en light y dark».
- **Descripción:** no hay salida del validador ni archivo que lo respalde, y la práctica no requiere gráfico. La afirmación no es verificable.
- **Corrección propuesta:** eliminar la frase o adjuntar la salida del validador. Como no hay gráfico en M10, lo más simple es eliminarla.

### H-09 — Menor — Calidad del script y del texto de verificación

- **Ubicación:** `calc/M10_practicas_luna.py`, `i_risks()`: la línea «P(rechazo falso)» en θ=9 repite exactamente «P(rechazo conforme)»; `p_fa` fija 10,5 en vez de usar `theta`. `M10_libreto.md`, solución de A: «La suma de probabilidad conforme y no conforme verifica uno» se afirma sin que el script lo calcule.
- **Corrección propuesta:** eliminar la línea duplicada o darle una etiqueta distinta; usar la variable `theta`; añadir la comprobación de suma igual a 1 (ver H-02).

## Resumen

- Cifras: todas las cifras impresas por el script coinciden con la solución y con mi recalculo independiente. Ningún error numérico.
- Problemas que deben corregirse antes de dar la práctica por cerrada: H-01 y H-02 (Mayor), y H-03, H-04, H-05 (Medio).
- Hallazgos menores: H-06 a H-09.
- Alcance B/I/A y origen de datos (simulados, marcados como no-CALAIRE): correctos.
- No se revisaron referencias bibliográficas, claves ni citas, por encargo.
