# Cambios de etapa 2 — M05

## Cambios

- `M05_libreto.md:3–15`: agenda de Sesión 4 (120 min) según `00_plan_corto.md` y guion de 15 min para revisar la tarea I de M04, sin volver a resolverla.
- `M05_libreto.md:19–27`: ficha ajustada a B e I; retiradas las referencias al nivel A.
- `M05_libreto.md:110`: práctica B identificada como trabajo en clase de 25 min.
- `M05_libreto.md:170–186`: I3 condensada; conserva comparación de un factor a la vez frente al factorial, robustez, reparto del esfuerzo y la ilustración simulada de precisión/potencia.
- `M05_libreto.md:188–219`: práctica I organizada como «en clase (15 min)» y «tarea», ambas con enunciado y solución docente.
- `M05_libreto.md:221–225`: cierre limitado a B e I; se retiró toda mención al nivel A.
- `calc/M05_diseno.py:20–24, 46–60`: se retiró el cálculo de pendiente que no se usaba en B/I y se conservaron los ejemplos, el conteo, la precisión y la potencia narrados.
- `calc/M05_practicas_luna.py:1–4, 72–81`: encabezado y cálculos limitados a B/I; se eliminaron los conteos, estratos, grados de libertad y diseños exclusivos de la práctica A.

## Archivos retirados

- Se retiró del libreto la sección completa «Nivel A», incluidas sus escenas y la práctica A (antes ocupaban la parte final del capítulo).
- No había HTML `M05_*` ni archivos de cálculo separados usados exclusivamente por A que hubiera que borrar. Los dos scripts de `calc/` también sirven para B/I; solo se eliminaron las partes A.

## Palabras finales y tiempo de narración

Conteo reproducible por nivel: se cuentan los enunciados y narración de B/I, excluyendo soluciones docentes, tablas y marcadores de formato; fórmulas se cuentan como texto cuando contienen palabras. Resultado: **B: 3 565 palabras (27,4 min); I: 2 631 palabras (20,2 min); total: 6 196 palabras, 47,7 min a 130 palabras/min**. La estimación queda cerca del objetivo aproximado de 5 850 palabras/45 min; puede variar según cuánto se lea literalmente de símbolos y ejemplos.

## Verificación

Ejecutados ambos scripts con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I`:

- `calc/M05_diseno.py`: terminó correctamente; reproduce media 0,40, diferencia 0,60 nmol/mol, conteo 576, factorial 2³ y potencias 0,495; 0,501; 0,873.
- `calc/M05_practicas_luna.py`: terminó correctamente; reproduce 576 = 480 + 96, resultados factoriales y orden reproducible con semilla 20261027; en la tarea de potencia, 4 × 12 da 0,284 y 6 × 8 da 0,495.
- Las salidas numéricas corresponden a las cifras narradas y a las soluciones docentes de M05.

## Correcciones del orquestador tras verif_M05.md
- `M05_practicas_luna.md` (bitácora heredada con la práctica A) movido a `logs_etapa2/archivo/`; ningún libreto lo cita.
