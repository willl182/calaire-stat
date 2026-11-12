# Cambios de etapa 2 — M04

## Cambios

- `M04_libreto.md:3-18`: añadí la tabla de Sesión 3 (120 min), con revisión de tarea de M03 (15 min), narración B+I (45 min), práctica B (25 min), inicio de práctica I (15 min) y preguntas/cierre (20 min). La revisión retoma la comparación de resultados correlacionados y el efecto de covarianza.
- `M04_libreto.md:20-30`: actualicé ficha y referencias para los contenidos B e I; retiré alcance A y sus fuentes exclusivas.
- `M04_libreto.md:88-100`: precisé la práctica B de clase con enunciado, solución, interpretación y criterio de logro.
- `M04_libreto.md:108-140`: condensé las escenas I3/I4 sobre potencia e incertidumbre de la desviación; conservé I5 Grubbs/Dixon con sus límites de uso.
- `M04_libreto.md`: dividí la práctica I en inicio de clase (selección y cálculo inicial de t pareada/Welch) y tarea (varianzas, potencia, incertidumbre de s y Grubbs/Dixon), con enunciado y solución docente para cada tramo.
- `M04_libreto.md`: eliminé el contenido A de multiplicidad, equivalencia y consistencia conjunta, así como menciones y referencias exclusivas de ese nivel.
- `calc/M04_ejemplos.py`: retiré bloques A de Bonferroni, TOST y consistencia conjunta, con sus validaciones; preservé cálculos y comprobaciones B/I.
- `calc/M04_practicas_luna.py`: retiré bloques A de Bonferroni, TOST y consistencia conjunta, con validaciones; preservé B/I y ordené imports.

## Archivos retirados

- Ninguno. Los dos scripts son mixtos y conservan ejemplos/prácticas B o I. No se encontraron archivos HTML M04 exclusivos de A.

## Palabras y minutos estimados de narración

Conteo aproximado del cuerpo narrado de las escenas B e I, a 130 palabras/min; excluye encabezados, tablas, fórmulas aisladas, rótulos y enunciados/soluciones de práctica.

| Nivel | Palabras | Minutos |
|---|---:|---:|
| B | 1668 | 12,8 |
| I | 467 | 3,6 |
| Total | 2135 | 16,4 |

La agenda reserva 45 min para B+I; la diferencia permite pausas, pizarra, práctica guiada y transiciones. La práctica B se ejecuta en su bloque de 25 min; la práctica I inicia en clase y continúa como tarea.

## Verificación

- Ejecuté `calc/M04_ejemplos.py` y `calc/M04_practicas_luna.py` desde `Curso_CORTO` con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I`; ambos terminaron con código 0.
- El script de ejemplos imprimió `comprobaciones_M04=OK`; el script de prácticas imprimió `comprobaciones_practicas_M04=OK`.
- Se verificaron las salidas de B, t pareada/Welch, chi-cuadrado/F, potencia, incertidumbre de s y Grubbs/Dixon. Ninguna de las salidas conservadas corresponde a bloques A.
