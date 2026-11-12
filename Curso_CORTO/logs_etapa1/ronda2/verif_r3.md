# Verificación ronda 3 — hallazgos asignados a r3

Fecha: 2026-11-11. Directorio: `Curso_CORTO/`. Referencias `archivo:línea` relativas a ese directorio. No se editó ningún archivo del curso.

## Veredicto

**CON OBSERVACIONES**

Los hallazgos de r3 que se pueden comprobar en el texto están resueltos y no encontré daño en el texto vecino. Falta, sin embargo, el registro de cambios de la ronda: `logs_etapa1/ronda2/cambios_r3.md` no existe, y `estado.txt` marca la ronda 3 con "cambios:  ítems" vacío.

## Fuentes revisadas

- `logs_etapa1/verif_sol_etapa1.md` (informe global).
- `logs_etapa1/ronda2/cambios_r3.md`: **no existe**.
- `logs_etapa1/ronda2/luna_r3.log`: el agente declara que la tarea quedó incompleta. Dice que dos de las tres referencias a `curso/logs/...` en M02 fallaron por edición paralela y que no creó `cambios_r3.md`.
- `logs_etapa1/ronda2/estado.txt`: `r3 luna FIN (exit 0)` con cambios vacío. `haiku_r3.log` está vacío (0 bytes).

## Comprobación de los hallazgos de r3

Tomo como alcance de r3 lo que el propio log de r3 dice que tocó: rutas de F07, observaciones 5.1 y 5.7, comentario `AX.4` e inventario de scripts.

| Punto | Estado actual | Evidencia |
|---|---|---|
| F07 — intérprete y ruta de M04 | Resuelto | `M04_libreto.md:152`: `../Curso_COMPLETO/curso/.venv/bin/python -I calc/M04_ejemplos.py`, desde la raíz de `Curso_CORTO/`. |
| F07 — intérprete y ruta de M06 | Resuelto | `M06_libreto.md:189`: `../Curso_COMPLETO/curso/.venv/bin/python -I calc/M06_practicas_luna.py`. Ahora incluye `-I`. |
| F07 — HTML de M03 | Resuelto | `M03_libreto.md:220`: `calc/M03_practica_I_probabilidad.html`, con la ruta real. |
| F07 — registros `curso/logs/...` en M02 | Resuelto | `grep "logs/" M02_libreto.md` no devuelve nada. Las tres líneas `:120`, `:176` y `:216` ya no contienen esa ruta. Contrario a lo que dice `luna_r3.log`, el estado actual está limpio. |
| 5.7 — comentario `AX.4` | Resuelto | `calc/M05_diseno.py:48` ya no menciona AX.4. El comentario es ahora «Precisión simulada del promedio bajo el modelo planteado en el capítulo.» |
| Remisiones M7–M13 / AX.x en libretos | Sin remanentes | `grep "AX\.[0-9]\|M7\|M1[^0-9]"` sobre `M0*_libreto.md` y `calc/*.py` no devuelve ningún identificador de módulo excluido. Sí aparece M05 en `M04_libreto.md:280`, que es un capítulo incluido. |
| 5.1 — inventario de scripts | Resuelto según el log | El log dice que se actualizó a 12. Ver nota abajo sobre `calc/`. |

## Ejecución de `calc/` (sí hubo cambios en `calc/`)

Se detectó que `calc/M05_diseno.py` cambió: el comentario de AX.4 desapareció. Por la regla, ejecuté los 12 scripts `.py` con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I`, sobre una copia temporal (`/tmp/verif_r3_MjyB/Curso_CORTO`) para no escribir HTML dentro del árbol:

- 12/12 terminaron con código 0 y stderr vacío.
- Ningún script falló ni dio `assert` fallido.

## Hallazgos

Ninguno bloqueante. Observaciones:

1. **Falta el registro de la ronda 3.** `logs_etapa1/ronda2/cambios_r3.md` no existe. Sin él no se puede saber qué archivos tocó r3 ni confirmar que el cambio es el que se pretendía. Hay que reconstruirlo desde el estado actual o re-ejecutar r3 para que lo escriba. Es la única causa de que el veredicto no sea APROBADO.
2. **Inventario de `calc/`.** `calc/` tiene 13 entradas, pero 12 son `.py`; la decimotercera no es un script. Conviene confirmar qué es antes de cerrar el inventario de `00_plan_corto.md`.
3. **Sin comprobar.** No se verificó que `M03_practica_I_probabilidad.html` se regenerara en su nueva ruta. Tampoco se revisaron los PDF bibliográficos citados en `M05_libreto.md:14` y otros, que apuntan a `../Curso_COMPLETO/docs/`.

## Condición para APROBADO

Crear `cambios_r3.md` con los cambios reales (archivo:línea) y confirmar el inventario de `calc/` (ítem 2). Con eso el veredicto puede pasar a APROBADO.
