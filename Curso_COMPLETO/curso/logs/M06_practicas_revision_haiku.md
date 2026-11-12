# Revisión de las prácticas B, I y A de M06 — Haiku

Fecha: 2026-10-27. Revisor: Haiku 5.5. Alcance: `curso/S2_modelos_calibracion/M06_libreto.md` (bloques `[PRÁCTICA]` y el texto narrativo que los sustenta), `curso/S2_modelos_calibracion/calc/M06_practicas_luna.py`, `calc/M06_ejemplos.py`, `calc/M06_RR_CALAIRE.py` y `curso/logs/M06_practicas_luna.md`. Contra `prop_e.md` (M6). No se han editado libretos ni scripts. No se han auditado referencias (lo hace otro supervisor).

## Resumen

Hay hallazgos. Las cifras de las tres prácticas son correctas y reproducibles. Los problemas son de alcance frente a prop_e, de trazabilidad de datos y de una edición narrativa no registrada en la bitácora. Ningún hallazgo es de severidad alta.

## Verificación numérica (ejecutado)

| Cifra del libreto | Resultado de la ejecución | Estado |
|---|---|---|
| B: `u²=0,0162`, `u=0,1273`, `U(k=2)=0,2546` nmol/mol | `0.016200`, `0.127279`, `0.254558` | OK |
| B sin `s_entre`: `u=0,03464`, `U=0,06928` | `0.034641`; `U` = 0,069282 | OK |
| B: `s_medias=0,3118`, `s_medias/√6=0,1273` | `0.311769`; `0.127279` | OK |
| I: medias 0,00; 0,50; 0,10; general 0,20 | `[0.0, 0.5, 0.1]`, `0.2` | OK |
| I: SS entre/dentro/total = 0,56/0,18/0,74; g.l. 2/9; MS 0,28/0,02; `F=14` | idem | OK |
| I: `F_{0,95}(2,9)=4,2565` | `4.256495` | OK |
| I: `τ̂²=0,065`, `s_entre=0,2550`, `s_r=0,1414` | `0.065`, `0.254951`, `0.141421` | OK |
| I: Cochran `C=0,45`; crítico 0,6287 (k=4, n=5) | `0.45`; `0.628724` (distribución beta) | OK |
| I (residual): IC chi-cuadrado 95 % de σ² ≈ [0,00946; 0,06666] | `[0.009462, 0.066657]` | OK |
| I: error estándar de `τ̂²` ≈ 0,0700; de `s_entre` ≈ 0,1374 | `0.070040`; `0.137359` | OK |
| A: SS = 0,08333 / 0,56 / 0,10667 / 0,12; MS; `F=1,5625 / 5,25 / 2,6667` | idem | OK |
| A: componentes por momentos 0,005 / 0,05667 / 0,01667 / 0,02 | idem | OK |
| A: `τ̂²=−0,002533`; REML frontera `τ²=0`, `σ²=0,014824`; contribuciones 0,03727 (truncado) y 0,03515 (REML) | `−0.002533`; `0.014824`; `0.037268`; `0.035148` (M06_ejemplos.py, con optimización) | OK |
| A-RR (ejemplo, A2): `F_analista` máx. 1,24 frente a 18,51; interacciones 6,61 / 4,31 / 6,47 / 5,07 en 135/360/405/455; Bonferroni 0,5 % → 6,35 | `1.238`, `18.5128`; `6.6115`, `4.3087`, `6.4735`, `5.0654`; `6.3547` | OK |
| Práctica A: pares por celda = (datos I3) − 0,4 | Coinciden con el enunciado (ver H-05 sobre la trazabilidad) | OK |

Comprobación de formato: no hay decimales con punto en la prosa; las cifras usan coma decimal y unidades nmol/mol.

## Hallazgos

### H-01 — Práctica I no usa un nivel del Level 2 como pide prop_e (media)

- **Ubicación:** `M06_libreto.md` líneas 170–174 (Práctica I) y 172 (origen de los datos). `prop_e.md`, M6, «I añade», *Práctica*: «ejecutar el ANOVA de días en un nivel del Level 2 con errores con signo».
- **Problema:** la práctica usa 12 valores simulados. Es admisible por la regla de datos (simulados con regla reproducible), pero prop_e fija un nivel del Level 2. La bitácora (`M06_practicas_luna.md`, líneas 10 y 31) declara «datos nuevos: simulados» sin justificar por qué no se usa el Level 2 propio. El archivo F-PSMT-01 es propio y tiene ruta verificable (`guia_libreto.md` §6).
- **Corrección propuesta:** o bien (a) usar un subconjunto limpio de un nivel de `docs/F-PSMT-01 …xlsm`, con ruta, hoja y celdas anotadas en la bitácora y en el script, o bien (b) dejar constancia en la bitácora de la decisión, del motivo y de quién la aprobó, y escalar al instructor. No convertir defectos del archivo en actividad.

### H-02 — Práctica A no analiza el caso R&R ni trabaja la multiplicidad (media)

- **Ubicación:** `M06_libreto.md` líneas 246–258 (Práctica A). `prop_e.md`, M6, «A añade», *Práctica*: «analizar el caso R&R con errores con signo; comparar modelos admisibles y justificar conclusiones considerando interacción y multiplicidad».
- **Problema:** (a) el enunciado sustituye el caso R&R por datos simulados. La razón (signo y agrupación no confirmados) es válida y está en el libreto, pero la bitácora solo la menciona como «pendiente», no como desviación de prop_e. (b) La multiplicidad aparece en la narrativa (línea 210), no en la práctica: ningún paso pide controlarla ni decidir la lista de niveles antes de mirar resultados.
- **Corrección propuesta:** añadir a la Práctica A una tarea de multiplicidad sobre el conjunto simulado (por ejemplo, tres contrastes de interacción con su criterio de Bonferroni y la solución numérica `F_crit(2,6)` calculada en el script). Añadir una tarea condicional sobre el caso R&R que solo se active si se confirma signo y agrupación (la nota de instructor de la línea 190 ya lo prevé). Registrar la desviación en la bitácora.

### H-03 — «Estimación de componentes y su incertidumbre» (prop_e, I) sin evidencia en la práctica I (media)

- **Ubicación:** `M06_libreto.md` líneas 114–116 (narrativa con IC chi-cuadrado y error estándar de `τ̂²`); tareas de la práctica I, línea 174.
- **Problema:** prop_e exige la incertidumbre de las componentes como contenido de I, y la guía (§1, `guia_libreto.md`) pide una evidencia observable por contenido. La práctica I pide estimar `σ̂²` y `τ̂²`, pero no su incertidumbre. Los números ya están en `M06_ejemplos.py` (IC `[0,00946; 0,06666]`, error estándar 0,0700 y 0,1374), pero no hay tarea ni solución docente que los use.
- **Corrección propuesta:** añadir a la tarea de I «calculen el intervalo chi-cuadrado al 95 % de `σ²` con 9 g.l. y el error estándar aproximado de `s_entre` por aproximación delta; expliquen por qué no es un intervalo exacto para `τ`». Añadir la solución numérica al bloque de solución docente con las cifras del script.

### H-04 — Edición narrativa fuera de los bloques de práctica, no registrada (media)

- **Ubicación:** `M06_libreto.md` línea 210 (Escena A1, párrafo «Ojo con la multiplicidad»). Diff contra HEAD: el hunk `@@ -192 +210 @@` cambia la cita de Bonferroni de `[Hahs-Vaughn §8.2.1]` a `[NIST/SEMATECH, «Bonferroni’s method», §7.4.7.3, https://…prc473.htm (consultado 2026-10-27)]`.
- **Problema:** (a) la bitácora dice que solo se editaron los bloques de práctica B/I/A (`M06_practicas_luna.md`, línea 25). Esta edición es fuera de ese alcance y no está registrada. (b) Cambia una cita existente, lo que la instrucción de la tarea prohíbe. (c) La fuente NIST y el numeral §7.4.7.3 no están en `docs/` y no son verificables aquí. Esta revisión no audita referencias, pero el cambio debe pasar por el supervisor de referencias.
- **Corrección propuesta:** restaurar la cita original (`[Hahs-Vaughn §8.2.1]`) o, si se quiere la nueva fuente, registrar el cambio en la bitácora y pedir al supervisor de referencias que la valide y la añada a la sección de referencias. Sin cambiar la cita por cuenta propia.

### H-05 — Trazabilidad de la matriz de la Práctica A (baja)

- **Ubicación:** `M06_libreto.md` línea 248 («construida restando 0,4 a cada dato del conjunto simulado de I3») y escena I3, líneas 134–136. Script línea 32.
- **Problema:** la escena I3 da los resultados (SS, F) pero no los datos crudos. Los datos crudos (`[[0,.2],[.1,.3],[.4,.6]], [[.3,.5],[0,.2],[.7,.9]]`) solo están en el script. Quien lea el libreto no puede reproducir «el conjunto de I3» sin abrir el script. Los pares del enunciado sí son suficientes para resolver la práctica, por lo que el problema es de trazabilidad y no de cálculo.
- **Corrección propuesta:** publicar la matriz cruda en la escena I3 (o en el enunciado de A) o sustituir «conjunto simulado de I3» por «matriz fijada en el script, de la que se derivan los pares listados».

### H-06 — El script de prácticas no calcula REML; el comentario y el libreto lo sugieren (baja)

- **Ubicación:** `calc/M06_practicas_luna.py` líneas 44 y 49 (`sigma2_reml=sst/11`, comentario «estimación REML restringida»). `M06_libreto.md` línea 228 («El script contrasta la solución de frontera con la optimización…»).
- **Problema:** en el script de prácticas, `σ²_REML` es la fórmula de la frontera `SST/(N−1)` y no hay optimización. La optimización de la verosimilitud restringida está en `M06_ejemplos.py` (líneas 109–118), que sí da `σ²=0,014824` y `τ²=0`, por lo que la cifra es correcta. El problema es que la solución de la práctica A (línea 254) remite al script de prácticas y el comentario sugiere un cálculo que no hace. La frase de la línea 228 atribuye al script de ejemplos lo que se lee como la práctica.
- **Corrección propuesta:** en el script de prácticas cambiar el comentario a «frontera REML: τ̂²=0 ⇒ σ̂²=SST/(N−1); la optimización se verifica en M06_ejemplos.py», y en la solución de A indicar ese archivo como fuente de la verificación. No es necesario duplicar la optimización.

### H-07 — Redacción poco clara en dos pasajes (baja)

- **Ubicación:** `M06_libreto.md` línea 152: «aquí el umbral es mayor de 0,5, por lo que las cuatro colas son disjuntas». Línea 210: «esperaríamos en promedio medio falso positivo».
- **Problema:** en la línea 152 la conclusión matemática es correcta (para umbrales superiores a 0,5, los sucesos «el grupo i es el máximo» son disjuntos, y la probabilidad de cola es `k` veces la de un grupo), pero «las cuatro colas» no lo dice. En la línea 210, «medio falso positivo» está mal construido.
- **Corrección propuesta:** línea 152: «por encima de 0,5 los sucesos «el grupo i tiene la varianza máxima» son disjuntos, de modo que la probabilidad de exceder el umbral es cuatro veces la de un grupo». Línea 210: «esperaríamos, en promedio, medio falso positivo». Esta línea forma parte de la cita H-04; si se restaura la cita original, aplicar solo la corrección de redacción.

### H-08 — La bitácora afirma una validación de paleta que no existe (baja)

- **Ubicación:** `curso/logs/M06_practicas_luna.md`, línea 34.
- **Problema:** dice «Skill dataviz leída y paleta validada en luz y oscuro», pero el propio registro indica que no se creó ningún gráfico. No hay paleta que validar. Una afirmación sin evidencia en la bitácora no es trazable.
- **Corrección propuesta:** sustituir por «No se generó ningún gráfico en M6; no aplica la validación de paleta de la skill dataviz», o eliminar la mención.

## Ajustes de alcance que no son hallazgos

- La solución docente de I y A describe con claridad la limitación de días frente a lecturas, el caso de Cochran sin eliminar datos y la escalación si la estructura no es equilibrada. Cumple la guía.
- La práctica B cumple prop_e (no ejecuta ANOVA, `k` declarado, comparación con y sin `s_entre`, resultado parcial para M8).
- Las señales de escalamiento de B y A están presentes.

## Conclusión

La revisión encuentra 8 hallazgos: 0 altos, 4 medios (H-01 a H-04) y 4 bajos (H-05 a H-08). Antes de dar por cerrado M6, convendría resolver H-01 y H-02 (decisión de alcance y de datos) y H-04 (cita y registro). H-03 es de contenido (falta evidencia de incertidumbre de componentes en I). Los hallazgos H-05 a H-08 son ajustes de redacción, trazabilidad y bitácora.
