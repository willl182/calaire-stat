# Verificación global de la etapa 2 — Curso_CORTO

**Veredicto: ETAPA 2 NO CERRADA.**

La cobertura de M2–M6 frente al **PDF original** se cumple; la secuencia de contenidos y las revisiones de tarea son coherentes; los doce scripts de `calc/` terminan correctamente. Las agendas suman cinco sesiones de 120 min, pero **no queda acreditada la temporización de 10 h con el criterio solicitado de narración a 130 palabras/min más actividades temporizadas**. Queda por explicitar el uso del margen incluido dentro de los bloques denominados «narración». Hay, además, una discrepancia de un minuto en el plan y una descripción residual de un ejemplo retirado de A. No se exige añadir contenido del temario ampliado para cerrar esta etapa.

## Alcance y fuentes

- Directorio auditado: `/home/w421/w421/calaire-stat/Curso_CORTO`.
- Leídos `00_plan_corto.md`, los cinco `logs_etapa2/cambios_M0*.md`, los cinco `logs_etapa2/verif_M0*.md` y el material final pertinente. Se contrastaron las correcciones del orquestador, no solamente los estados anteriores descritos en las verificaciones.
- Base de cobertura: `/home/w421/.t3/userdata/attachments/a4307bec-cdcb-489e-82fa-5e2e16ccbd98-3ba09308-7d01-4dd1-9c26-73aa937425e7-pdf.pdf`, una página, «TEMARIO RESUMIDO / Estadística aplicada», M2–M6. Se extrajo su texto con `pdftotext -layout`.
- **No se utilizó `Curso_COMPLETO/temario_curso.md` como criterio de cobertura.** Los requisitos del PDF son: M2, resumen y gráficos de las lecturas y valores atípicos; M3, modelos de la variabilidad y del ruido del SRP; M4, intervalos de confianza y pruebas de hipótesis; M5, planificación de las comparaciones; M6, repetibilidad, precisión intermedia y estudios R&R.
- No se modificaron libretos, scripts, recursos, plan ni registros previos. El único archivo escrito en el árbol del curso es este informe. Las ejecuciones y regeneraciones se hicieron en una copia temporal.

## Método de temporización

Se separó la prosa conceptual B/I de las prácticas, de las indicaciones visuales y de los bloques con presupuesto propio —apertura, revisión de tarea y cierre del curso—. Los enunciados y las soluciones de prácticas **no se sumaron otra vez** a la narración: ya pertenecen al tiempo asignado a práctica.

Conteo homogéneo y conservador de prosa explícita: en los intervalos indicados en cada tabla se excluyen líneas vacías y las que empiezan por `>`, `#`, `|` o `$`; se retiran citas entre corchetes, fórmulas entre `$…$` y código entre backticks; se cuentan palabras alfanuméricas, incluidos guiones y apóstrofos internos (`[[:alnum:]_]+([-’'][[:alnum:]_]+)*`). Minutos = palabras / 130, redondeando solo la presentación.

**Límite de la medición:** no equivale a un ensayo de impartición. Verbalizar fórmulas, dibujar, esperar respuestas y comentar salidas lleva tiempo adicional. La diferencia se informa como **margen didáctico por explicitar**, no como prueba de que la clase necesariamente termine antes. Tampoco se considera que menos texto sea por sí solo un defecto: el problema de cierre es presentar ese margen como «narración» sin una distribución verificable de sus actividades.

Para comparar las sesiones se mantuvieron los tiempos nominales de apertura, revisión, preguntas y cierre. Por ello, el «total con prosa medida» de las tablas **no es una duración real observada**; sustituye únicamente el bloque de narración por su tiempo de lectura base. La apertura y el cierre se examinan también por separado.

## Sesión 1 — M02, descriptiva

| Comprobación | Resultado y evidencia |
|---|---|
| Cobertura del PDF | **Cumple.** Resumen, histograma, cuantiles, caja, media y dispersión: `M02_libreto.md:52–80`; orden temporal: `:102–108`; atípicos mediante inspección e IQR, investigación y conservación del dato: `:110–118`. El puente a Grubbs/Dixon de M04 está en `:116`. |
| Solo B e I | Sin sección ni práctica A en el material activo. Los bloques A de `calc/M02_examples.py` fueron retirados: el archivo final termina con comprobaciones B/I en `:90–93`. Queda una descripción heredada en la ficha, señalada en H3. |
| Agenda | `M02_libreto.md:5–12`: apertura 10 + narración 47 + B 25 + I 15 + repaso/preguntas 23 = **120 min**. Coincide con `00_plan_corto.md:80`. |
| Narración a 130 palabras/min | Prosa de `:36–124`, `:144–186`, `:208–211`: **4 382 palabras = 33,7 min**. Frente a los 47 min asignados: **13,3 min** de margen dentro de «narración». |
| Total con prosa medida y restantes bloques nominales | 33,7 + 10 + 25 + 15 + 23 = **106,7 min**. Falta explicitar el empleo del margen para certificar los 120 min con este criterio. |
| Apertura | Presente y adecuada: objetivos, datos SRP, entorno Python y dinámica clase/tarea (`:14–20`). Su prosa base es **211 palabras ≈ 1,6 min** frente al bloque de 10 min. La preparación del entorno/interacción puede ocupar el resto, pero no tiene acciones y tiempos desglosados. No hay revisión de tarea previa, como corresponde. |
| Prácticas y continuidad | B en clase 25 min (`:126`); I iniciada en clase 15 min y tarea con solución (`:188–204`). El cierre enlaza con distribuciones y promedios (`:206–211`). La revisión en M03 recupera el mismo conjunto de 60 pares y la misma pregunta. |
| Scripts | `M02_examples.py` y `M02_practicas_luna.py`: **2/2, código 0**, stderr vacío. Los HTML B/I regenerados son idénticos a los originales. |
| Estado de sesión | Contenido y ejecución correctos; **temporización pendiente de explicitar** y residuo menor de ficha. |

## Sesión 2 — M03, probabilidad y distribuciones

| Comprobación | Resultado y evidencia |
|---|---|
| Cobertura del PDF | **Cumple.** Modelos probabilísticos de lecturas, variables y distribución (`M03_libreto.md:33–61`); normal, rectangular/cuanti­zación y triangular (`:63–97`); ruido de lectura, promedio, componente común y deriva (`:99–137`); covarianza y dependencia temporal en I1/I3 (`:169–197`, `:237–255`). Los ejemplos se declaran didácticos/simulados, sin atribuir datos falsos al SRP. |
| Solo B e I | Sin sección/práctica A ni referencia residual a A2 en el script final; `calc/M03_ejemplos.py:24` dice «Deriva B3». |
| Agenda | `M03_libreto.md:5–11`: revisión 15 + narración 49 + B 25 + I 15 + preguntas/cierre 16 = **120 min**, conforme a `00_plan_corto.md:81`. |
| Narración a 130 palabras/min | Prosa de `:33–137`, `:157–221`, `:239–269`: **4 368 palabras = 33,6 min**. Frente a 49 min: **15,4 min** de margen. |
| Total con prosa medida y restantes bloques nominales | 33,6 + 15 + 25 + 15 + 16 = **104,6 min**. `:13` reconoce pausas, pizarra y transiciones, pero no distribuye sus tiempos; sus 3 065 + 2 781 palabras no son el mismo conteo homogéneo aplicado aquí. |
| Revisión de M02-I | **Corresponde** (`:15–17` frente a `M02_libreto.md:194–204`): 60 pares, tres días, cinco niveles, cuatro lecturas por celda; media/mediana/MAD, dispersión intragrupo, recta suministrada y escalamiento. Es selectiva: no exige recuperar por separado todos los coeficientes y cifras de la solución anterior. No cambia los datos ni inventa otra tarea. |
| Prácticas y continuidad | B 25 min (`:139–155`); I en clase 15 min (`:223–225`) y tarea sobre gráfico normal/interpretación (`:227–235`), con solución. Cierre hacia inferencia (`:263–269`). |
| Scripts | `M03_ejemplos.py` y `M03_practicas_luna.py`: **2/2, código 0**, stderr vacío. El segundo no imprime salida: valida mediante aserciones. Invocada explícitamente `write_probability_html(path)` en la copia temporal: HTML idéntico al recurso conservado. |
| Estado de sesión | Cobertura y continuidad correctas; **temporización pendiente de explicitar**. |

## Sesión 3 — M04, inferencia

| Comprobación | Resultado y evidencia |
|---|---|
| Cobertura del PDF | **Cumple.** Intervalo t y su interpretación (`M04_libreto.md:53–65`); hipótesis, significación, valor p y errores de decisión (`:67–83`); pareadas/Welch e inferencia de variabilidad (`:111–145`). Potencia, incertidumbre de s y Grubbs/Dixon permanecen en I3–I5 (`:147–177`). |
| Solo B e I y correcciones finales | Sin sección/práctica A. Retiradas las referencias a AX.1/AX.7 y M8: `:47`, `:55`; referencias documentales finales con prefijo `../Curso_COMPLETO/docs/` (`:209–212`). No se repiten como vigentes los tres hallazgos ya corregidos de `verif_M04.md`. |
| Agenda | `M04_libreto.md:5–11`: revisión 15 + narración 45 + B 25 + I 15 + preguntas/cierre 20 = **120 min**, conforme a `00_plan_corto.md:82`. |
| Narración a 130 palabras/min | Prosa de `:33–83`, `:99–177`, `:203–205`: **3 399 palabras = 26,1 min**. Frente a 45 min: **18,9 min** de margen. |
| Total con prosa medida y restantes bloques nominales | 26,1 + 15 + 25 + 15 + 20 = **101,1 min**. La reducción de I3/I4 existe; falta distribuir el margen de aula que no es lectura de prosa. |
| Revisión de M03-I | **Corresponde** (`:13–15` frente a `M03_libreto.md:227–235`): seis puntos, posiciones de Blom, patrón del gráfico y límites de su interpretación; enlace a chi-cuadrado/F. |
| Prácticas y continuidad | B 25 min (`:85–97`); I en clase 15 min (`:179–185`) y tarea (`:187–199`), con soluciones. Cierre hacia el diseño y la réplica independiente (`:201–205`). |
| Scripts | `M04_ejemplos.py` y `M04_practicas_luna.py`: **2/2, código 0**, stderr vacío. |
| Estado de sesión | Contenido y continuidad correctos; **temporización pendiente de explicitar**. |

## Sesión 4 — M05, diseño de experimentos

| Comprobación | Resultado y evidencia |
|---|---|
| Cobertura del PDF | **Cumple.** Planificación de comparaciones: respuesta, factores, niveles, unidades y réplicas (`M05_libreto.md:34–52`); bloques, anidamiento/cruce y pseudorreplicación (`:54–72`); estructura Level 2 y diseños publicados (`:74–108`); aleatorización, factorial y reparto del esfuerzo (`:132–186`). |
| Solo B e I | Sin sección/práctica A activa. La bitácora heredada fue trasladada a `logs_etapa2/archivo/M05_practicas_luna.md`, como anota `cambios_M05.md:31–32`; no es material docente activo ni está citada por los libretos. |
| Agenda | `M05_libreto.md:5–12`: revisión 15 + narración 45 + B 25 + I 15 + preguntas/cierre 20 = **120 min**, conforme a `00_plan_corto.md:83`. |
| Narración a 130 palabras/min | Prosa de `:32–108`, `:124–186`, `:223–225`: **4 389 palabras = 33,8 min**. Frente a 45 min: **11,2 min** de margen. |
| Total con prosa medida y restantes bloques nominales | 33,8 + 15 + 25 + 15 + 20 = **108,8 min**. No se demuestra un exceso de narración a partir de los 47,7 min de `cambios_M05.md:21`: aquel conteo incluye enunciados y no separa de igual manera la práctica. |
| Revisión de M04-I | **Corresponde** (`:14–16` frente a `M04_libreto.md:187–199`): pareadas, Welch, varianzas, planificación y Grubbs/Dixon. Es un repaso selectivo, no una nueva resolución completa; no menciona expresamente u(s). No hay sustitución por una tarea distinta. |
| Prácticas y continuidad | B 25 min (`:110–122`); I factorial en clase 15 min (`:188–209`) y tarea sobre reparto/potencia (`:211–219`), con soluciones. Cierre hacia componentes/ANOVA (`:221–225`). |
| Scripts | `M05_diseno.py` y `M05_practicas_luna.py`: **2/2, código 0**, stderr vacío. |
| Estado de sesión | Cobertura y continuidad correctas; **temporización pendiente de explicitar**. Los supuestos huecos frente al temario ampliado no bloquean la cobertura del PDF. |

## Sesión 5 — M06, ANOVA, precisión y R&R

| Comprobación | Resultado y evidencia |
|---|---|
| Cobertura del PDF | **Cumple.** Repetibilidad y precisión intermedia (`M06_libreto.md:35–73`, `:173–181`); ANOVA y componentes (`:97–155`); estudio R&R con datos reales conservado en **I6** (`:211–249`). El PDF no exige %R&R, categorías de distinción ni validación histórica del archivo. |
| Solo B e I | Sin sección/práctica A activa. I6 es la excepción de contenido que el plan ordenó conservar en I (`00_plan_corto.md:61`, `:88–89`), no un residuo indebido de A. Las «evaluaciones tipo A» de incertidumbre (`M06_libreto.md:179`) no designan un nivel del curso. |
| Agenda | `M06_libreto.md:5–13`: revisión 10 + narración 59 + B 25 + I 10 + cierre 15 + preguntas/transición 1 = **120 min**. La fila del plan (`00_plan_corto.md:84`) suma **119 min**, no 120: el libreto incorpora el minuto faltante. |
| Narración a 130 palabras/min | Prosa de `:33–73`, `:87–181`, `:215–247`, `:263`: **5 169 palabras = 39,8 min**, incluida I6. Frente a 59 min: **19,2 min** de margen. |
| Total con prosa medida y restantes bloques nominales | 39,8 + 10 + 25 + 10 + 15 + 1 = **100,8 min**. I6 no se suma de nuevo fuera de la narración. |
| I6 R&R | **Presente, pertinente y reproducible.** Prosa base: **1 552 palabras ≈ 11,9 min**, compatible con un bloque aproximado de 15 min si se destinan unos 3,1 min a discusión/apoyo visual. Se conservan modelo, denominadores, multiplicidad y advertencias de análisis exploratorio condicional, sin emparejar días por posición (`:217–247`). |
| Revisión de M05-I | **Corresponde** (`:27–29` frente a `M05_libreto.md:211–219`): 48 lecturas, reparto 4 × 12 frente a 6 × 8, día como unidad independiente y mayor potencia del plan de seis días. Es selectiva en cifras; no exige repetir cada desviación y potencia numérica. |
| Prácticas y cierre | B 25 min (`:75–85`); I en clase 10 min y tarea (`:183–208`), con solución. Cierre integrador M2–M6 y actividad oral por equipos (`:251–259`); no anuncia una sexta sesión. Su prosa base ocupa **368 palabras ≈ 2,8 min**; el intercambio puede ocupar el resto del bloque de 15 min, pero sin distribución temporal. |
| Scripts | `M06_ejemplos.py`, `M06_practicas_luna.py`, `M06_RR_CALAIRE.py`, `M06_practica_I_grafico.py`: **4/4, código 0**, stderr vacío. HTML de residuos regenerado idéntico. R&R reproduce interacción nominal en 135, 360, 405 y 455; Bonferroni conserva 135 y 405. |
| Estado de sesión | Cobertura, R&R y cierre presentes; **temporización pendiente de explicitar** y diferencia de un minuto respecto del plan. La tarea final no indica mecanismo posterior de devolución, observación no bloqueante. |

## Hallazgos globales

### H1 — No queda verificada la duración efectiva de las cinco sesiones con el criterio solicitado

**Evidencia:** bloques de narración en `M02_libreto.md:8`, `M03_libreto.md:8`, `M04_libreto.md:8`, `M05_libreto.md:8` y `M06_libreto.md:8`; apertura en `M02_libreto.md:14–20`; cierre en `M06_libreto.md:251–259`.

Las agendas son aritméticamente correctas: **600 min** en total. La prosa conceptual homogéneamente medida suma **21 707 palabras ≈ 167,0 min**, mientras se reservan **245 min** a narración: diferencia aproximada de **78,0 min**, distribuida entre las cinco sesiones. Manteniendo nominales los otros bloques, el cálculo combinado da **522,0 min**, no 600. Este es un diagnóstico de asignación temporal, no una predicción del tiempo real de enseñanza.

Los conteos de los registros no permiten resolverlo por suma: `cambios_M04.md:21` excluye prácticas/fórmulas/código; `cambios_M05.md:21` incluye enunciados; los restantes aplican otras exclusiones. `verif_M03.md:45` reconoce que no recontó las palabras. Incluso los registros originales ya advierten márgenes: M02, 33,9 frente a 47 min (`cambios_M02.md:19–24`); M06, 43,9 frente a 59 min (`cambios_M06.md:22–27`).

**Para cerrar:** distinguir «narración a 130 palabras/min» de pausas, pizarra, lectura de gráficos, discusión o trabajo guiado, asignando minutos a estas actividades sin duplicar los de prácticas y verificando 120 por sesión. No es necesario rellenar el margen con más teoría. El criterio estricto de duración solicitado queda pendiente; no se certifican 10 h únicamente porque las celdas de la agenda sumen 600.

### H2 — El plan de la sesión 5 declara 120 min, pero enumera 119

**Evidencia:** `00_plan_corto.md:84`: (44 + 15) + 25 + 10 + 10 + 15 = **119**. `M06_libreto.md:12` añade 1 min de preguntas/transición y su agenda sí llega a 120.

Es una discrepancia documental menor, no un desbordamiento de M06. `logs_etapa2/verif_M06.md:12` da por exacta una coincidencia que no lo es. **Para cerrar:** hacer concordar la fila final del plan con la distribución vigente, además de resolver H1. No se editó aquí.

### H3 — Residuo descriptivo del ejemplo de A retirado en M02

**Evidencia:** `M02_libreto.md:30` sigue diciendo que los ejemplos del script ilustran «sesgos opuestos». El bloque de grupos con sesgos opuestos que motivó `logs_etapa2/verif_M02.md:37` fue retirado por el orquestador (`cambios_M02.md:31–33`); `calc/M02_examples.py:79–93` conserva tendencia y comprobaciones B/I, no aquel ejemplo.

No queda una sección ni una práctica A, pero sí una descripción heredada que ya no corresponde a los ejemplos presentes. **Para cerrar el requisito literal de no dejar restos:** ajustar la ficha a lo que efectivamente permanece, sin reintroducir A. Hallazgo menor.

### Observación — Tarea final sin devolución especificada

`M06_libreto.md:202` asigna trabajo posterior y `:251–259` cierra el curso, sin indicar cómo se entregará o recibirá retroalimentación. No incumple por sí solo el plan, que permite terminar I como tarea, ni exige inventar una sexta sesión. Conviene declarar un mecanismo fuera de las 10 h si se espera revisión. Las revisiones M03–M06 corresponden a las tareas anteriores; que sean selectivas no constituye una tarea equivocada.

## Cobertura: resolución de observaciones previas

- `logs_etapa2/verif_M03.md:35–41` deriva exigencias específicas de la razón entre canales, conteo y propagación del temario ampliado, no del PDF base. No son huecos obligatorios frente a «modelos de la variabilidad y del ruido del SRP». Ese objetivo sí queda cubierto por lectura, promedio, componente común, covarianza y deriva, con límites explícitos.
- `logs_etapa2/verif_M05.md:24–33` exige un diseño escalonado y un juicio particular sobre seis días desde `Curso_COMPLETO/temario_curso.md`. El PDF solo exige «planificación de las comparaciones»; está cubierta. No se requiere restaurar la práctica A para satisfacerlo.
- `logs_etapa2/verif_M06.md:28–34` utilizó el Markdown como proxy del PDF. Esta verificación sustituye aquel cotejo por el PDF suministrado y confirma repetibilidad, precisión intermedia y R&R.
- Los registros históricos, `00_plan_corto.md` en sus tablas de origen y `logs_etapa2/archivo/` contienen menciones a A como historia del recorte. No se confunden con una oferta docente activa de nivel A. La búsqueda de «Nivel A», «Práctica A», «Escena A…» y rótulos A1… en libretos y scripts activos no detectó secciones o cálculos A residuales. H3 es el resto semántico menor identificado.

## Ejecución reproducible de calc/

Copia utilizada: **`/tmp/verif_sol_e2_w6dwgxdt/Curso_CORTO`**. Intérprete absoluto: **`/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python`**. Cada script se lanzó como proceso independiente con `-I`, ruta del script en la copia, directorio de trabajo en la copia, captura de stdout/stderr y límite de 120 s. No se usó el intérprete Python del sistema para ejecutarlos.

| Sesión | Scripts ejecutados | Resultado |
|---|---|---|
| M02 | `calc/M02_examples.py`; `calc/M02_practicas_luna.py` | 2/2, código 0, sin stderr |
| M03 | `calc/M03_ejemplos.py`; `calc/M03_practicas_luna.py` | 2/2, código 0, sin stderr |
| M04 | `calc/M04_ejemplos.py`; `calc/M04_practicas_luna.py` | 2/2, código 0, sin stderr |
| M05 | `calc/M05_diseno.py`; `calc/M05_practicas_luna.py` | 2/2, código 0, sin stderr |
| M06 | `calc/M06_ejemplos.py`; `calc/M06_practicas_luna.py`; `calc/M06_RR_CALAIRE.py`; `calc/M06_practica_I_grafico.py` | 4/4, código 0, sin stderr |
| **Total** | **12 scripts** | **12/12 correctos** |

Salidas completas y resumen de ejecución conservados en `/tmp/verif_sol_e2_w6dwgxdt/`: `<nombre>.stdout.txt`, `<nombre>.stderr.txt` y `results.json`. Los HTML M02 B/I y M06 I regenerados coinciden byte a byte con los recursos originales. Para M03 se invocó adicionalmente `write_probability_html(path)` mediante `runpy.run_path` con el mismo intérprete y `-I`, siempre sobre la copia; el HTML también coincide byte a byte.

El script R&R produce máximo F de analista **1,238163**, umbral **18,512821**, interacciones nominales **135/360/405/455**, umbral Bonferroni **6,354689** y niveles restantes **135/405**; coincide con `M06_libreto.md:223–229`. Se verificó la ejecución y esta correspondencia; no se convirtió el resultado exploratorio en una validación metrológica de los libros.

## Condiciones de cierre

1. **Explicitar y verificar la temporización por sesión**, separando prosa, actividades guiadas, prácticas y márgenes; conservar cinco bloques de 120 min sin sumar tarea domiciliaria ni contar I6 dos veces.
2. **Concordar el minuto faltante de la sesión 5 en el plan** con la agenda del libreto.
3. **Retirar la descripción residual de «sesgos opuestos» de la ficha de M02** o hacerla corresponder a los ejemplos B/I realmente conservados, sin restaurar A.

**Conclusión final: ETAPA 2 NO CERRADA por la comprobación temporal pendiente y los ajustes documentales descritos. Cobertura PDF M2–M6: cumplida. Continuidad entre sesiones: cumplida. Nivel A docente: retirado, con un residuo descriptivo menor. Scripts: 12/12 correctos.**
