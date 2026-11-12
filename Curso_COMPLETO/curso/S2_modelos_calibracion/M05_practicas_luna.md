# M05 — Bitácora de correcciones de prácticas (luna)

## Alcance y método

Ronda de correcciones sobre los hallazgos H-01–H-14 de `curso/logs/M05_practicas_revision_haiku.md`. Se editaron únicamente los tres bloques `[PRÁCTICA]` de `curso/S2_modelos_calibracion/M05_libreto.md` y su script `curso/S2_modelos_calibracion/calc/M05_practicas_luna.py`; se registra aquí la decisión de cada hallazgo. No se cambiaron bibliografía, claves, citas existentes, referencias ni otros capítulos. Sin commits.

## Tabla de decisiones

| Hallazgo | Decisión | Ubicación | Resultado |
|---|---|---|---|
| H-01 | Aplicado | M05_libreto.md, práctica I, solución docente | Se eliminó 1,23, que no aparecía; el contraste correcto queda 1,22 nmol/mol. |
| H-02 | Aplicado | M05_libreto.md, práctica I, enunciado y solución | Se declara que la regla determinista produce ocho valores esperados, no 16 resultados observados ni error de corrida. Las dos réplicas son planificadas; el orden contiene sus 16 etiquetas. No se inventa variación aleatoria que la tabla no tiene. |
| H-03 | Aplicado | M05_libreto.md, práctica I, enunciado, solución e interpretación | Umbral definido para efectos principales y contrastes simples de F, C y T. Se indica escalamiento por F marginal = 0,80 y contraste simple = 1,22 nmol/mol. |
| H-04 | Aplicado | M05_libreto.md, práctica I; calc/M05_practicas_luna.py | Se expresa F×C bajo la convención de I2: mitad de la diferencia de efectos simples = 0,30; diferencia sin dividir = 0,60. El script imprime ambas y el contraste simple 1,22. |
| H-05 | Aplicado | M05_libreto.md, práctica A; calc/M05_practicas_luna.py | Se añadió la alternativa 6 analistas × 4 días × 2 ciclos × 1 lectura: 48 lecturas; gl 5, 18, 24 y 0. Se explica que ciclo y error de lectura no se separan. |
| H-06 | Aplicado con delimitación | M05_libreto.md, práctica A y referencia a escena A1 | Se compara el patrón escalonado publicado de ISO 5725-3 (4 resultados por laboratorio) con el totalmente anidado (8), su secuencia y ahorro del 50 %. Se identifica como patrón publicado y se distingue de la adaptación didáctica a campañas; no se transfieren sus grados de libertad al R&R base ni se presenta como requisito. |
| H-07 | Revisado y aplicado | M05_libreto.md, práctica I, subtarea de reparto de esfuerzo y potencia; calc/M05_practicas_luna.py | Se añadió una subtarea evaluable con dos repartos de 48 lecturas, parámetros poblacionales simulados declarados, efecto prefijado, potencias calculadas con t no central, criterio de elección y reproducción en script. La tabla determinista de ocho valores esperados del factorial permanece separada del modelo de planificación; no se le añade error residual. |
| S-M05-01 | Aplicado | M05_libreto.md, práctica I; calc/M05_practicas_luna.py | Se incorporó evidencia observable por contenido de distribución del esfuerzo y potencia, en vez de considerar suficiente la aplicación narrada en I3. El contraste de planes usa días como unidades independientes y lecturas subordinadas; conserva explícitos los supuestos simulados. |
| H-08 | Aplicado | M05_libreto.md, prácticas B, I y A | B declara jornada de calibración/seis días y ciclo no identificado; I, jornada experimental/corridas; A, campaña/días/ciclos. |
| H-09 | Aplicado | M05_libreto.md, práctica B, enunciado, solución e interpretación | Se cita ubicación fuente exacta (nota, hoja Fotometro, E17) y se distingue explícitamente el conteo 576 de la nota de las filas del archivo; se advierte que la discrepancia se investiga fuera de la práctica, sin transformarla en actividad de clase. |
| H-10 | Aplicado | `curso/logs/M05_practicas_luna.md` | Esta ronda queda registrada en la ubicación solicitada `curso/logs/`; se conserva intacta la bitácora previa de la sección como historial. |
| H-11 | Aplicado | M05_libreto.md, práctica I | La secuencia se especifica para una jornada y el script genera las 16 etiquetas con semilla 20261027. |
| H-12 | Aplicado | M05_libreto.md, práctica I | Se quitó el nominal de 100 nmol/mol como si formara parte de la regla; el error se define contra una referencia fija solo como contexto. |
| H-13 | Aplicado | calc/M05_practicas_luna.py | Se imprimen efectos e interacción, diferencia simple, contraste 1,22, orden, y salidas de tabla/contrastes con dos decimales y coma decimal. |
| H-14 | Aplicado | M05_libreto.md, práctica A, solución docente | Se especifica que fijo limita la población de inferencia y aleatorio permite generalizar a la población muestreada bajo el modelo; el denominador del efecto de analista (día dentro de analista) no cambia por esa elección en la estructura descrita. |

## Ejecución y resultados finales

Ejecutado desde la raíz del repositorio:

```text
curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M05_practicas_luna.py
```

Resultado: rc=0. Reproduce:

- B, conteo descrito por la nota: 576 = 480 de concentraciones + 96 de ceros; no equivale a conteo de filas ni de réplicas independientes.
- I, respuestas esperadas: −0,13; −0,17; −0,13; −0,37; 0,41; 0,29; 0,85; 0,85 nmol/mol.
- I, subtarea de potencia: 4 días × 12 lecturas, sd de media diaria=0,2021 nmol/mol y potencia=0,284; 6 días × 8 lecturas, sd=0,2031 y potencia=0,495 (48 lecturas en cada plan).
- I, efectos marginales: F=0,80; C=0,20; T=−0,10 nmol/mol. Efectos simples de F: C bajo=0,50 y C alto=1,10 nmol/mol; diferencia=0,60; interacción F×C según convención de I2=0,30. Contraste simple F con C alto y T alto=1,22 nmol/mol. Se escala por F marginal y por el contraste simple conforme al criterio didáctico de 0,50.
- I, subtarea de potencia (48 lecturas por plan; parámetros simulados Δ=0,20, τ=0,20, σ=0,10 nmol/mol): 4 días × 12 lecturas, sd de media diaria=0,2021 y potencia bilateral=0,284; 6 días × 8 lecturas, sd=0,2031 y potencia=0,495. El cálculo usa t no central, gl d−1.
- I, semilla 20261027: orden reproducible de 16 etiquetas tratamiento-réplica, impreso por script.
- A base: 3 analistas, 12 días, 24 ciclos, 192 lecturas; gl 2, 9, 12, 168.
- A con 6 analistas y una lectura por ciclo: 6 analistas, 24 días, 48 ciclos, 48 lecturas; gl 5, 18, 24, 0. Cero gl en lectura dentro de ciclo; no separa ciclo de error.
- A seis analistas y plan base por analista: 24 días, 48 ciclos, 384 lecturas y 5 gl de analista.
- A escalonado publicado: 4 resultados por laboratorio frente a 8 totalmente anidados, ahorro de 4 (50 %); script registra las etapas descritas.

No se requieren gráficos según el alcance de M5 en prop_e; la revisión confirma que no se omite gráfico exigido. Las salidas de la práctica son tablas/esquemas con unidades y no hay visualización creada en esta ronda.

## Estado

H-01–H-14 tienen decisión explícita arriba. H-07 es un rechazo deliberado y documentado; queda pendiente una evidencia evaluable directa de potencia/reparto de esfuerzo en la práctica I. No se modificaron referencias/citas existentes ni archivos fuera del alcance autorizado.
