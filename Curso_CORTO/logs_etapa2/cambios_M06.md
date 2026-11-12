# Cambios Etapa 2 — M06

## Cambios realizados

- `M06_libreto.md:3-13` — encabezado «Sesión 5 (120 min)» y agenda conforme a etapa 2; incluye revisión de tarea de M05 (10 min), B en clase (25 min), I en clase (10 min), I6 (~15 min) y cierre del curso (15 min).
- `M06_libreto.md:21-25` — ficha actualizada a B e I; retiro de descripción de nivel A y referencias a anexos/destinos fuera del curso.
- `M06_libreto.md:27-29` — guion narrado breve de revisión de la tarea I de M05.
- `M06_libreto.md:183-208` — práctica I separada en inicio en clase (10 min) y tarea, con solución docente y criterios conservados.
- `M06_libreto.md:211-249` — nueva escena I6 R&R con datos de CALAIRE, denominadores, resultados por nivel, ajuste por multiplicidad, limitaciones y advertencia explícita de análisis exploratorio y condicional; cierre integrador del curso M2–M6.
- `M06_libreto.md:261-265` — cierre del capítulo depurado de contenido A.
- `calc/M06_practicas_luna.py:1-3,46-` — eliminados cálculos y salidas que solo correspondían a la práctica A; permanecen cálculos B/I.
- `calc/M06_ejemplos.py:104-` — eliminados ejemplos exclusivos de A (componente negativa/REML y sesgo de laboratorio); permanecen ejemplos B/I, incluido ANOVA cruzado I.
- `calc/M06_RR_CALAIRE.py` — sin cambios funcionales; conserva advertencia, agrupación condicional y texto de salida exploratorio.
- `M06_practica_I_residuos.html` — se conserva: corresponde a la práctica I, no a una práctica A.

## Archivos retirados

- Se retiró del libreto la sección completa de Nivel A, sus escenas y la práctica A simulada. No había un HTML independiente de práctica A en M06. En `calc/M06_practicas_luna.py` se retiraron únicamente los bloques A; en `calc/M06_ejemplos.py` se retiraron los ejemplos exclusivos de A. No se borraron archivos fuente.

## Palabras finales y duración estimada

Conteo de narración en libreto (excluye encabezados, tablas y líneas de práctica/citas):

- B: **1 338 palabras**, ≈ **10,3 min** a 130 palabras/min.
- I, sin I6: **2 745 palabras**, ≈ **21,1 min** a 130 palabras/min.
- I6 R&R: **1 624 palabras**, ≈ **12,5 min** a 130 palabras/min (condensada; objetivo aproximado 1 950 palabras/15 min).
- Total narrativo B + I + I6: **5 707 palabras**, ≈ **43,9 min** a 130 palabras/min.

## Verificación

Ejecutados con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I`:

- `calc/M06_ejemplos.py` — correcto; reproduce ANOVA simulado y Cochran.
- `calc/M06_practicas_luna.py` — correcto; reproduce práctica B e I.
- `calc/M06_RR_CALAIRE.py` — correcto; reproduce los resultados narrados. Imprime advertencia de análisis exploratorio condicional; los niveles con interacción nominal son 135, 360, 405 y 455, y tras Bonferroni 135 y 405.

La fuente original en `../Curso_COMPLETO/curso/` no se modificó. El único HTML M06 existente se mantuvo porque corresponde a la práctica I.

## Correcciones del orquestador tras verif_M06.md
- `M06_libreto.md:75`: práctica B marcada «en clase (25 min)».
- `M06_libreto.md:211`: «Escena I6».
- `M06_libreto.md:204`: «Por el método de momentos».
- `calc/M06_practicas_luna.py:21`: comentario con las columnas reales.
