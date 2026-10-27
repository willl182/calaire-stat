# Corrección S-M04-04 — M04

Se corrigió en `curso/S1_fundamentos/calc/M04_practicas_luna.py` el booleano `descarta_magnitud`: ahora exige con `and` que el IC95 quede dentro del intervalo de equivalencia `(-margen, +margen)`. Para el IC95 de B (aprox. `[-0.1218, 0.4218]`) y margen `0.30`, no se descarta magnitud relevante (`False`). Se añadió una aserción explícita de ese resultado.

La solución del libreto ya era correcta y no se modificó. No se tocaron otras escenas, citas, referencias ni capítulos/hitos.

La ejecución solicitada con `python -I curso/S1_fundamentos/calc/M04_practicas_luna.py` no pudo completar: terminó con `ModuleNotFoundError: No module named 'scipy'` (código 1). También se comprobó que el Python predeterminado carece de SciPy. No se instalaron dependencias ni se alteró el entorno.
