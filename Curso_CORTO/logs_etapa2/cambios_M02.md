# Cambios de etapa 2 — M02

## Cambios

- `M02_libreto.md:1-41`: encabezado de Sesión 1 (120 min), agenda según 00_plan_corto.md y apertura del curso de 10 min sobre objetivos, SRP/datos, entorno de cálculo y dinámica clase/tarea.
- `M02_libreto.md:11`: ficha sin Nivel A.
- `M02_libreto.md:171-184`: práctica I dividida en trabajo en clase (15 min) con solución docente y tarea con enunciado y solución docente verificable.
- `M02_libreto.md:182-223`: retirado el bloque Nivel A; cierre y referencias conservan B e I.
- `calc/M02_practicas_luna.py:79-`: retirados los cálculos y la generación de gráfico usados solo por A; quedan B e I.
- HTML B e I regenerados con el script de prácticas; se mantiene su contenido accesible.

## Archivos retirados

- `M02_practica_A_grafico.html` — práctica visual del nivel A.
- `calc/M02_practicas_luna.py` ya no contiene cálculos ni generador HTML exclusivos de A.

## Palabras y minutos de narración

Conteo aproximado de narración (excluye títulos, tablas, consignas/soluciones en bloque de práctica y elementos de pizarra/diapositiva):

- B: 3 187 palabras; 24,5 min a 130 palabras/min.
- I: 1 214 palabras; 9,3 min a 130 palabras/min.

Total narrativo medido: 4 401 palabras, ≈33,9 min a 130 palabras/min. La planificación asigna hasta 47 min a narración B+I e incluye margen para pausas y demostraciones.

## Verificación

- Ejecutados sin error con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I`: `calc/M02_examples.py` y `calc/M02_practicas_luna.py`.
- El segundo script genera `M02_practica_B_grafico.html` y `M02_practica_I_grafico.html` y verifica cálculos mediante aserciones.

## Correcciones del orquestador tras verif_M02.md
- `calc/M02_examples.py`: retirados el bloque y las etiquetas del nivel A (hallazgo 1); el script corre.
- `M02_libreto.md:126`: práctica B marcada «(en clase, 25 min)» (hallazgo 3).
