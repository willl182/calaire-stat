# Cambios de etapa 2 — M03

## Cambios

- `M03_libreto.md:3-15`: agregué encabezado de Sesión 2 (120 min), agenda del plan y guion de revisión de la tarea I de M02 (15 min). La revisión contempla los 60 pares simulados, resúmenes por día y nivel, dispersión intra-celda, lectura de recta ya ajustada y tendencia/escalamiento.
- `M03_libreto.md:17-28`: actualicé la ficha para retirar el nivel A y añadí las palabras/minutos de narración B e I estimados.
- `M03_libreto.md:225-243`: dividí la práctica I en inicio en clase (15 min) y tarea, con enunciado y solución docente propios; la práctica de tarea completa el gráfico normal y la lectura temporal.
- `M03_libreto.md:267-274`: retiré la sección A, sus escenas y su práctica; eliminé también la mención de A del cierre. Conservé B e I, sus citas, y sus menciones a los límites de formación técnica.
- `calc/M03_ejemplos.py:50-72`: quité cálculos que solo se usaban en A (cociente de canales, covarianza entre puntos y matrices/autocorrelación), manteniendo ejemplos de B e I.
- `calc/M03_practicas_luna.py:1-95`: retuve cálculos B/I, quité bloques y salidas A; el script ya no escribe el HTML al ejecutarse. La función `write_probability_html(path)` permite regenerarlo explícitamente.
- `calc/M03_practica_I_probabilidad.html:1-26`: se conserva como recurso I; no había HTML exclusivo A en los assets M03.

## Archivos retirados

- Ningún archivo M03 retirado: los dos scripts son mixtos y ambos conservan ejemplos/prácticas B o I. No había archivo HTML exclusivo A.

## Palabras y minutos estimados de narración

Conteo del cuerpo narrado, excluyendo títulos, tablas, fórmulas aisladas, rótulos y consignas/soluciones de práctica:

| Nivel | Palabras | Minutos a 130 palabras/min |
|---|---:|---:|
| B | 3065 | 23,6 (≈24) |
| I | 2781 | 21,4 (≈21) |
| Total | 5846 | 45,0 |

La agenda asigna 49 min a B+I, con unos cuatro minutos para pausas, pizarra y transiciones; las estimaciones son de narración continua a 130 palabras/min.

## Verificación

- Ejecuté `calc/M03_ejemplos.py` y `calc/M03_practicas_luna.py` con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I`: ambos terminaron con código 0; el primero imprimió `comprobaciones_M03=OK` y la práctica I imprimió `comprobaciones_M03_practicas=OK`.
- Invocación explícita de `write_probability_html(Path('/tmp/M03_prueba.html'))`: terminó con código 0 y produjo HTML de 4245 bytes; el HTML de trabajo no se sobrescribe al ejecutar el script de cálculos.
- Comparé las cifras reproducibles con el libreto: conversiones rectangulares/triangular/U, t(0,975;15), semiancho t, componente común, diferencia con covarianza, varianza descriptiva, cuantiles de Blom y medias/bloques de la serie con deriva coinciden con las soluciones docentes.

## Correcciones del orquestador tras verif_M03.md
- `M03_libreto.md:139`: práctica B marcada «(en clase, 25 min)».
- `calc/M03_ejemplos.py:24`: comentario sin la escena A2.
- Nota: `M03_practicas_luna.py` no imprime «OK»; solo valida con assert (corre sin errores).
