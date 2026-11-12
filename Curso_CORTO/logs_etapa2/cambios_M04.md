# Cambios M04 — Etapa 2

## Cambios

- `M04_libreto.md:3-14`: añadida agenda de Sesión 3 (120 min) y guion de revisión de la tarea I de M03.
- `M04_libreto.md:17-27`: actualizada ficha a B e I; retirado el alcance avanzado y sus referencias.
- `M04_libreto.md:29-103`: conservado el nivel B y su práctica, ahora rotulada «en clase (25 min)»; eliminado el puente a equivalencia avanzada.
- `M04_libreto.md:147-166`: condensadas las escenas I3 (potencia) e I4 (incertidumbre de s), manteniendo decisiones de diseño, fórmulas operativas y cifras esenciales.
- `M04_libreto.md:167-177`: conservada I5; verificado Dixon $Q_{crit}=0,59$ en Otto, tabla 2.10, $Q(0,99;n=8)$ para la variante $Q_n$ (hueco superior/rango completo). El script de prácticas suministra explícitamente el mismo valor.
- `M04_libreto.md:179-199`: dividida la práctica I original en «en clase (15 min)» y «tarea», cada parte con enunciado y solución docente; eliminada la sección avanzada.
- `M04_libreto.md:201-213`: ajustados cierre y referencias a B/I; retiradas las referencias usadas solo por A.
- `calc/M04_ejemplos.py:138-`: eliminados cálculos y comprobaciones exclusivos de A. Se ejecutó con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I calc/M04_ejemplos.py`; terminó con `comprobaciones_M04=OK`.
- `calc/M04_practicas_luna.py:70-`: eliminados cálculos y comprobaciones exclusivos de A. Se ejecutó con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I calc/M04_practicas_luna.py`; terminó con `comprobaciones_practicas_M04=OK`.

## Archivos retirados

No había archivos `M04_*` HTML en `Curso_CORTO`; por tanto, no se retiró ningún HTML. No se borraron scripts completos: ambos scripts de cálculo mezclaban B/I con A, así que se quitaron únicamente los bloques A. La fuente original bajo `../Curso_COMPLETO/curso/` quedó intacta.

## Palabras de narración y tiempo a 130 palabras/min

Conteo reproducible sobre `M04_libreto.md`: se separan las secciones B e I; se excluyen encabezados, tablas, prácticas (enunciados y soluciones), notas al instructor, citas bibliográficas, fórmulas en `$...$` y código en backticks; se cuentan palabras con `\b\w+(?:[-’']\w+)*\b`. Resultado: **B 1 961 palabras (15,1 min)**; **I 2 116 palabras (16,3 min)**; **total 4 077 palabras (31,4 min)**. Los minutos son el cociente entre palabras y 130, redondeado a una décima; las pausas, pizarra y transiciones pueden alargar el tiempo de aula. La agenda conserva los 45 min de narración del plan.

## Correcciones del orquestador tras verif_M04.md (2.º intento)
- Reintroducidas desde el original y retiradas de nuevo: AX.1/AX.7 (ficha, :26, :47), M8 (:55).
- Rutas `docs/` de la bibliografía cambiadas a `../Curso_COMPLETO/docs/`.
