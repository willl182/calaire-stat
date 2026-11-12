# M05 — Bitácora de correcciones de prácticas (luna)

Bitácora única de las prácticas B, I y A de M05. Unifica la versión previa de `curso/logs/` y la de `curso/S2_modelos_calibracion/M05_practicas_luna.md`; esta última queda como historial y no se modificó.

## Alcance y método

Ronda de correcciones sobre los hallazgos H-01–H-14 de `curso/logs/M05_practicas_revision_haiku.md`, y ronda de cierre sobre los hallazgos H-01–H-07 de `curso/logs/M05_practicas_revision_cierre_haiku.md` (sección «Ronda de cierre», al final). Se editaron únicamente los tres bloques `[PRÁCTICA]` de `curso/S2_modelos_calibracion/M05_libreto.md` y su script `curso/S2_modelos_calibracion/calc/M05_practicas_luna.py`. No se cambiaron bibliografía, claves, citas ni referencias; `curso/guia_libreto.md` no se tocó. Sin commits.

## Tabla de decisiones (ronda de correcciones)

| Hallazgo | Decisión | Ubicación | Resultado |
|---|---|---|---|
| H-01 | Aplicado | M05_libreto.md, práctica I, solución docente | Se eliminó 1,23, que no aparecía; el contraste correcto queda 1,22 nmol/mol. |
| H-02 | Aplicado | M05_libreto.md, práctica I, enunciado y solución | Se declara que la regla determinista produce ocho valores esperados, no 16 resultados observados ni error de corrida. Las dos réplicas son planificadas; el orden contiene sus 16 etiquetas. |
| H-03 | Aplicado | M05_libreto.md, práctica I, enunciado, solución e interpretación | Umbral definido para efectos principales y contrastes simples de F, C y T. |
| H-04 | Aplicado | M05_libreto.md, práctica I; calc/M05_practicas_luna.py | F×C bajo la convención de I2: mitad de la diferencia de efectos simples = 0,30; diferencia sin dividir = 0,60. |
| H-05 | Aplicado | M05_libreto.md, práctica A; calc/M05_practicas_luna.py | Alternativa 6 analistas × 4 días × 2 ciclos × 1 lectura: 48 lecturas; gl 5, 18, 24, 0. Ciclo y error de lectura no se separan. |
| H-06 | Aplicado con delimitación | M05_libreto.md, práctica A y escena A1 | Patrón escalonado publicado de ISO 5725-3 (4 resultados por laboratorio) frente al totalmente anidado (8); ahorro del 50 %. No se transfieren sus grados de libertad al R&R base. |
| H-07 | Revisado y aplicado | M05_libreto.md, práctica I, subtarea de reparto de esfuerzo y potencia; calc/M05_practicas_luna.py | Subtarea evaluable con dos repartos de 48 lecturas, parámetros simulados declarados, potencias con t no central y criterio de elección. La tabla determinista de ocho valores esperados no recibe error residual. |
| S-M05-01 | Aplicado | M05_libreto.md, práctica I; calc/M05_practicas_luna.py | Evidencia observable de distribución del esfuerzo y potencia (subtarea de H-07), en lugar de considerar suficiente la narración de I3. Días como unidades independientes; lecturas subordinadas. |
| H-08 | Aplicado | M05_libreto.md, prácticas B, I y A | B: jornada de calibración/seis días y ciclo no identificado; I: jornada experimental/corridas; A: campaña/días/ciclos. |
| H-09 | Aplicado | M05_libreto.md, práctica B, enunciado, solución e interpretación | Ubicación fuente exacta (nota, hoja Fotometro, E17); el conteo 576 de la nota se distingue de las filas del archivo; la discrepancia se investiga fuera de la práctica. |
| H-10 | Aplicado | `curso/logs/M05_practicas_luna.md` | Esta bitácora unificada está en `curso/logs/`; la bitácora de la sección se conserva como historial. |
| H-11 | Aplicado | M05_libreto.md, práctica I | Secuencia especificada para una jornada; el script genera las 16 etiquetas con semilla 20261027. |
| H-12 | Aplicado | M05_libreto.md, práctica I | Se quitó el nominal de 100 nmol/mol como si formara parte de la regla; la referencia queda como contexto didáctico. |
| H-13 | Aplicado | calc/M05_practicas_luna.py | Efectos, interacción, diferencia simple, contraste 1,22, orden y tablas con dos decimales y coma decimal. |
| H-14 | Aplicado | M05_libreto.md, práctica A, solución docente | Fijo limita la población de inferencia; aleatorio permite generalizar a la población muestreada bajo el modelo. |

## Ejecución y resultados

Ejecutado desde la raíz del repositorio:

```text
curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M05_practicas_luna.py
```

Resultados que reproduce el script (las cifras del libreto coinciden con su salida):

- B, conteo descrito por la nota: 12 × 8 × 6 = 576 = 480 de concentraciones + 96 de ceros; no equivale a conteo de filas ni de réplicas independientes.
- I, respuestas esperadas: −0,13; −0,17; −0,13; −0,37; 0,41; 0,29; 0,85; 0,85 nmol/mol.
- I, efectos marginales: F = 0,80; C = 0,20; T = −0,10 nmol/mol. Efectos simples de F: C bajo = 0,50 y C alto = 1,10 nmol/mol; diferencia = 0,60; interacción F×C (convención I2) = 0,30.
- I, doce contrastes simples (cada factor condicionado a los otros dos): cuatro superan 0,50 nmol/mol: F con C bajo y T bajo = 0,54; F con C alto y T bajo = 0,98; F con C alto y T alto = 1,22; C con F alto y T alto = 0,56. El máximo es 1,22.
- I, semilla 20261027: orden reproducible de 16 etiquetas tratamiento-réplica.
- I, subtarea de potencia (48 lecturas por plan; Δ = 0,20, τ = 0,20, σ = 0,10 nmol/mol, simulados): 4 días × 12 lecturas, sd de media diaria = 0,2021 y potencia = 0,284; 6 días × 8 lecturas, sd = 0,2031 y potencia = 0,495. Cálculo con t no central, gl d − 1.
- A base: 3 analistas, 12 días, 24 ciclos, 192 lecturas; gl 2, 9, 12, 168.
- A con 6 analistas y una lectura por ciclo: 6 analistas, 24 días, 48 ciclos, 48 lecturas; gl 5, 18, 24, 0.
- A seis analistas y plan base por analista: 24 días, 48 ciclos, 384 lecturas y 5 gl de analista.
- A escalonado publicado: 4 resultados por laboratorio frente a 8 totalmente anidados, ahorro de 4 (50 %); el script calcula ese conteo a partir de las etapas.

No se requieren gráficos según el alcance de M5 en prop_e; las salidas de la práctica son tablas y esquemas con unidades.

## Estado (correcciones)

H-01–H-14 tienen decisión explícita arriba. El S-M05-01 y la subtarea de H-07 están aplicados; la evidencia de potencia ya no queda fuera de la práctica I.

## Ronda de cierre

Revisión de cierre: `curso/logs/M05_practicas_revision_cierre_haiku.md` (sus H-01 a H-07 son distintos de los H-01 a H-14 de arriba).

Verificaciones hechas en esta ronda: la celda `Fotometro!E17` del certificado `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm` contiene la nota «10 puntos de concentración, 2 puntos de cero, 8 repeticiones por punto», sin número de días; y en `docs/ISO 5725-3_1994.pdf`, §9.5 (figura 2) y §9.8 confirman el patrón escalonado de cuatro resultados frente a 2^n (ocho en el caso de la práctica A). No se modificaron las citas.

| H-xx | decisión | ubicación | rc |
|---|---|---|---|
| H-01 | Aplicado: se calculan los doce contrastes simples; cuatro superan 0,50 nmol/mol y se citan en la solución y la interpretación | M05_libreto.md, práctica I (solución e interpretación); calc/M05_practicas_luna.py, `factorial()` | 0 |
| H-02 | Aplicado: esta bitácora unificada reemplaza la divergente; H-07 de la ronda previa figura como aplicado con subtarea de potencia, y S-M05-01 queda registrado | curso/logs/M05_practicas_luna.md | 0 |
| H-03 | Aplicado: «casi duplica la potencia» pasa a «eleva la potencia de 0,284 a 0,495», con sd 0,2031 frente a 0,2021 | M05_libreto.md, práctica I, solución del reparto de esfuerzo | 0 |
| H-04 | Aplicado: el escalonado se calcula desde operadores, días y resultados por día, y la secuencia desde sus etapas | calc/M05_practicas_luna.py, `design_counts()` | 0 |
| H-05 | Aplicado: la frase sobre la revisión se retira de la solución y pasa a un bloque `[NOTA AL INSTRUCTOR]` | M05_libreto.md, práctica B, después de la solución | 0 |
| H-06 | Rechazado: `curso/guia_libreto.md` no se modifica en esta fase (decisión del orquestador; la etiqueta [PRÁCTICA] es la convención aceptada) | — | — |
| H-07 | Aplicado en parte: la celda E17 se verificó y no declara seis días, así que el número de días pasa a supuesto de la práctica; el patrón ISO 5725-3 queda verificado en §9.5 y §9.8. Las citas no se tocan | M05_libreto.md, práctica B (enunciado y solución) | 0 |

Ejecución final tras las correcciones: `curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M05_practicas_luna.py`, **rc=0**.
