# Verificación global — etapa 1, puntos 1, 2 y 3

Fecha: 2026-11-11. Directorio revisado: `Curso_CORTO/`. Los localizadores `archivo:línea` de este informe son relativos a ese directorio y corresponden al estado leído durante esta revisión.

## Veredicto

**CON OBSERVACIONES — NO CERRAR TODAVÍA LA ETAPA 1.**

Se conserva la cobertura temática de M2–M6 del PDF y están presentes las tres intervenciones previstas: apertura de M02, sustitución de remisiones externas y puente de atípicos M02 → M04. No encontré evidencia de pérdida de esas intervenciones ni de escenas duplicadas por las ediciones paralelas. Sin embargo, persisten una referencia explícita a M1, remisiones implícitas a módulos excluidos y algunas incoherencias de prerrequisitos y alcance. Los hallazgos F01–F06 impiden dar por terminada la adaptación de contenido; F07 recoge problemas de localización y reproducción documental.

**Ejecución: 12/12 scripts Python existentes en `calc/` terminan con código 0, sin salida en stderr.** El plan anuncia 13, pero el inventario real contiene 12. Los cinco HTML regenerados son idénticos byte a byte a los existentes. Que los programas corran no acredita por sí solo la concordancia de todas sus cifras y etiquetas con el libreto: se señalan dos discrepancias heredadas al final.

No se modificó ningún libreto, script, Excel ni HTML del curso. La única entrega persistente de esta revisión es este informe.

## 1. Referencia y alcance de la comprobación

- Fuente normativa de alcance: PDF `/home/w421/.t3/userdata/attachments/a4307bec-cdcb-489e-82fa-5e2e16ccbd98-3ba09308-7d01-4dd1-9c26-73aa937425e7-pdf.pdf`, título «Temario resumido SRP», **página 1 de 1**. Se extrajo su texto y se contrastaron sus cinco entradas M2–M6, no un temario reconstruido desde los libretos.
- Plan: `00_plan_corto.md:19–26`, especialmente puntos 1–3.
- Registros leídos íntegramente: `logs_etapa1/cambios_p1.md`, `cambios_p2.md`, `cambios_p3.md`, `verif_p1.md`, `verif_p2.md` y `verif_p3.md`. Sus conclusiones se contrastaron con los archivos actuales; no se tomaron como prueba suficiente.
- Lectura de los cinco libretos y comparación con sus fuentes actuales en `../Curso_COMPLETO/curso/S1_fundamentos/` y `../Curso_COMPLETO/curso/S2_modelos_calibracion/`.
- Comprobación de referencias explícitas e implícitas, secuencia de prerrequisitos, integridad de cambios, rutas locales y ejecución de todos los `.py` de `calc/`.
- No se auditó la validez histórica de los datos de CALAIRE, no se revalidaron las fuentes bibliográficas externas y no se abordó el recorte a diez horas de la etapa 2.

### Cobertura contra el PDF

| Módulo y requisito literal del PDF | Evidencia en el curso corto | Resultado |
|---|---|---|
| M2: «resumen y gráficos de las lecturas; valores atípicos» | `M02_libreto.md:34–90`, resúmenes, histogramas, caja y orden temporal; `:92–100`, detección exploratoria y puente a pruebas | Cubierto; observaciones F04 y F06 sobre la escena añadida |
| M3: «modelos de la variabilidad y del ruido del SRP» | `M03_libreto.md:20–118`, variables y distribuciones, ruido independiente/común y deriva; `:156–246`, dependencia y escalas temporales | Cubierto; autonomía respecto de M1 pendiente en F01/F05 |
| M4: «intervalos de confianza y pruebas de hipótesis» | `M04_libreto.md:22–90`, inferencia de una media; `:98–188`, métodos y pruebas; `:224–274`, multiplicidad, equivalencia y consistencia | Cubierto |
| M5: «planificación de las comparaciones» | `M05_libreto.md:20–112`, factores, réplicas y bloques; `:118–287`, aleatorización, factoriales, esfuerzo y diseño R&R | Cubierto |
| M6: «repetibilidad, precisión intermedia y estudios R&R» | `M06_libreto.md:20–76`, interpretación de precisión; `:82–189`, ANOVA y componentes; `:195–267`, estructura R&R y límites | Cubierto |

El PDF no exige trasladar todas las pruebas formales de atípicos a M2. El puente que autoriza expresamente `00_plan_corto.md:24` es una solución válida. Tampoco exige enseñar M1 completo ni desarrollar la forma general del modelo como un módulo adicional.

### Cumplimiento de los tres puntos

1. **Prerrequisitos de M1: parcial.** Las fichas de M02 y M03 se adaptaron (`M02_libreto.md:8`, `M03_libreto.md:8`) y la apertura aparece una sola vez (`M02_libreto.md:16–18`). Define referencia, indicación, signo del error y ecuación del SRP. Subsisten F01 y F05. Las fichas de M04–M06 remiten a módulos incluidos; no encontré otra dependencia explícita de M1 en esos tres capítulos.
2. **Remisiones fuera del curso: parcial.** En los libretos ya no aparecen identificadores de M7–M13 ni AX.x. Sí quedan remisiones por nombre, por promesa de continuidad y por contenido excluido: F02/F03. `GUM-S2` en `M03_libreto.md:14,310,372` es una referencia bibliográfica válida, no un módulo S2 colgante.
3. **Atípicos en M2 y puente a M4: cumplido en lo esencial, con observaciones.** `M02_libreto.md:94` presenta las cercas de 1,5·IQR como detección exploratoria, no como límites de aceptación; `:96–100` exige conservar e investigar. `:98` remite a Grubbs/Dixon y `M04_libreto.md:180` retoma expresamente la detección de M2. I5 conserva condiciones, ejemplo y advertencias contra la exclusión automática. Quedan F04 y F06.

## 2. Hallazgos de adaptación pendientes

### F01 — Referencia explícita a M1 todavía activa

**Prioridad: necesaria para cerrar el punto 1.** `M03_libreto.md:18` conserva «No sustituye el modelo de medición de M1 ni la descripción de M2». M1 no existe en este curso. La ficha modificada en `:8` no resuelve esa dependencia en el cuerpo del texto. Debe referirse al punto de partida de M02 o reformularse sin remisión externa.

Es el mismo pendiente señalado en `logs_etapa1/verif_p1.md:12,16,30`; sigue sin resolverse. No es evidencia de que el cambio de la ficha se haya perdido: ambos estados coexisten.

### F02 — Remisiones implícitas a formación que el curso ya no incluye

**Prioridad: necesaria para cerrar el punto 2.**

- `M06_libreto.md:283`: «En el siguiente módulo vamos a pasar […] a ajustar una relación entre referencia e indicación». M06 es el último capítulo del curso corto; la promesa corresponde a M7/regresión, no copiado.
- `M05_libreto.md:78`: atribuye el análisis de la evolución temporal a «los módulos de estadística descriptiva, regresión y control». Descriptiva existe; regresión y control no. Falta conservar la remisión útil a M02 y delimitar las otras como externas al curso.
- `M03_libreto.md:326`: «Para GGMR trabajaremos solo con covarianza cero entre ejes» promete un trabajo que `:256` acaba de excluir. `:354` vuelve a invocar sus exclusiones como si definieran un procedimiento del curso. No queda un identificador M7, pero sí una expectativa incompatible con el nuevo alcance.

Una búsqueda limitada a códigos M7/M8/AX no detecta estas referencias. Son pendientes de adaptación al curso corto, aunque esas frases ya existieran en el completo.

### F03 — La práctica de M02 sigue exigiendo el ajuste declarado fuera del curso

**Prioridad: coherencia de alcance y prerrequisitos.** `M02_libreto.md:160` dice que el procedimiento para ajustar la recta queda fuera del alcance y que se entrega una recta ya calculada. Sin embargo, `:174` pide «Ajusten descriptivamente la recta […] a las 60 observaciones», sin que el capítulo enseñe el procedimiento. La solución de `:176` da coeficientes, pero no explica cómo estimarlos.

La sustitución de la remisión a M07 dejó intacta una tarea que necesita ese contenido. Para mantener los cambios mínimos del plan, se puede proporcionar el ajuste y pedir su lectura, en vez de exigir aprender a estimarlo fuera de los contenidos disponibles. No hace falta incorporar M7 completo.

### F04 — MAD aparece en B antes de su definición en I

**Prioridad: coherencia de la escena de atípicos.** `M02_libreto.md:96` introduce «la mediana y la MAD» sin expandir ni definir MAD. La ficha la reserva a I (`:10`) y su explicación operativa llega en `:146–148`. B6 incorpora así un prerrequisito del nivel posterior que no necesita para aplicar la regla IQR.

El pendiente de `logs_etapa1/verif_p3.md:18` continúa vigente. Basta retirar esa mención de B o introducirla de forma autosuficiente y armonizar la ficha; no es necesario trasladar toda I1.

### F05 — La ecuación del SRP pierde unidades y condición de simplificación al sustituir M1

**Prioridad: completar el mínimo autónomo del punto 1.** `M02_libreto.md:18` presenta `c=-ln(T)/(αL)` como concentración, pero no declara unidades de `c`, `α` o `L`, ni que es un modelo simplificado bajo condiciones declaradas. El resto de M02 usa nmol/mol, de modo que no queda visible que ese resultado intermedio no necesariamente está ya en esa unidad.

En la fuente, `../Curso_COMPLETO/curso/S1_fundamentos/M01_libreto.md:60–64` explicita el supuesto estándar y distingue `c` en atm, con `α` en atm⁻¹ cm⁻¹ y `L` en cm, de `Y=(c/p₀)·10⁹` en nmol/mol. No se necesita copiar la física ni la deducción: sí identificar salida, unidades y condición del modelo que ahora debe sostenerse sin M1.

No considero obligatorio añadir además `Y=f(X₁,…,Xₙ)` solo para satisfacer la expresión «modelo de medición» de `M03_libreto.md:8`: la ecuación concreta ya puede cumplir esa función si se presenta adecuadamente.

### F06 — La nueva cita a Otto no se puede resolver dentro de la bibliografía de M02

**Prioridad: cerrar la trazabilidad de la escena añadida.** `M02_libreto.md:98` cita «Otto §2.2», pero `:230–240` no incluye una entrada Otto ni remite a su referencia en M04. La bibliografía de otro capítulo no es un destino declarado en esta cita. Debe añadirse la identificación correspondiente o remitirse expresamente a M04-I5 y su fuente.

Se confirma el pendiente de `logs_etapa1/verif_p3.md:19`. No se verificó aquí si los pasajes de Otto/Crowder respaldan cada afirmación: el hallazgo es la falta de resolución bibliográfica local, no una acusación de atribución estadística incorrecta.

### F07 — Rutas heredadas impiden seguir algunas instrucciones, aunque los scripts sí corren

**Prioridad: reproducción y localización del material.**

- `M04_libreto.md:152` prescribe `curso/.venv/bin/python -I curso/S1_fundamentos/calc/M04_ejemplos.py`. Desde `Curso_CORTO/` no existen esas rutas. La estructura actual requiere el intérprete `../Curso_COMPLETO/curso/.venv/bin/python` y el script `calc/M04_ejemplos.py`.
- `M06_libreto.md:189` conserva el mismo problema con `curso/S2_modelos_calibracion/calc/M06_practicas_luna.py`; además, su instrucción no incluye `-I`.
- `M03_libreto.md:220` anuncia `M03_practica_I_probabilidad.html` sin prefijo. El archivo está y se vuelve a generar en `calc/M03_practica_I_probabilidad.html`, porque `calc/M03_practicas_luna.py:94` escribe junto al script. No aparece una copia en la raíz al ejecutar.
- `M02_libreto.md:120,176,216` remite a `curso/logs/M02_practicas_luna_ejecucion.txt`, archivo no incluido en el curso corto. La ejecución actual imprime resultados en stdout, no crea ese registro.

**Observación documental adicional, no hueco temático del PDF:** las bibliografías siguen presentando numerosos PDF como archivos locales de `docs/`, pero el directorio corto solo contiene los dos Excel. Ejemplos: `M02_libreto.md:232–237`, `M03_libreto.md:368–372`, `M04_libreto.md:284–291`, `M05_libreto.md:297–306`, `M06_libreto.md:288–295,297`. También `M02_libreto.md:239` cita `prop_e.md`, no copiado, y `M05_libreto.md:14` remite a una bitácora sin destino incluido. Conviene indicar su ubicación real en `Curso_COMPLETO` o distinguir bibliografía externa de archivos suministrados; no es necesario duplicar toda la biblioteca para cerrar los temas M2–M6.

## 3. Integridad de las ediciones paralelas

**Resultado: no encontré evidencia de sobrescritura ni duplicación de las intervenciones en el estado final.**

- M02 mantiene simultáneamente la ficha sin M1 (`:8`), la apertura (`:16–18`), la limpieza de anexos/remisiones y B6 (`:92–100`). Apertura y B6 aparecen una sola vez. No se detectaron identificadores de escena repetidos ni párrafos largos idénticos duplicados en M02/M03.
- M03 mantiene la nueva ficha (`:8`) y las sustituciones de remisiones. Su M1 residual de `:18` ya estaba en la fuente y no fue adaptado: no demuestra una reversión de la ficha.
- M04 conserva tanto la limpieza de referencias como la entrada nueva de I5 (`:180`); no se sustituyó el ejemplo ni se movió fuera del capítulo.
- La comparación de M04–M06 con las fuentes muestra sustituciones de remisiones, entradas sobre anexos y el enlace de I5, sin pérdida ni duplicación de escenas, prácticas, fórmulas o resultados numéricos por estas ediciones.
- Las diferencias de M02/M03 corresponden a las intervenciones previstas y a las sustituciones de alcance. Los dos primeros scripts de M02 y `calc/M03_practicas_luna.py` son idénticos byte a byte a sus fuentes del curso completo; no se observa una edición paralela sobre su contenido.

Esto verifica la integración visible frente a los originales actuales. No reconstruye la secuencia histórica de escrituras concurrentes ni certifica lo que pudo ocurrir en estados intermedios no conservados.

## 4. Ejecución completa de `calc/`

### Método

Se inventariaron recursivamente todos los `.py` de `calc/`: **12 archivos**. Se hizo una copia temporal del curso con igual estructura, incluyendo los dos Excel; se comprobó SHA-256 idéntico de cada script antes de ejecutarlo. Las exclusiones de copia fueron `.git`, `__pycache__` y los registros de etapa, no las dependencias de cálculo.

Cada script se ejecutó como proceso independiente con **Python 3.14.7**, opción **`-I`**, directorio de trabajo en la raíz de la copia y límite de 120 s por archivo. Se usó `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python`, la ruta absoluta normalizada del mismo intérprete solicitado como `../Curso_COMPLETO/curso/.venv/bin/python`; no el Python del sistema ni otro entorno.

La copia evita que los tres generadores de HTML sobrescriban los archivos del curso. Se compararon hashes de los 32 archivos preexistentes de contenido, código, HTML, Excel y registros Markdown antes y después: ninguno cambió.

| Script | Código de salida | stderr | Tiempo (s) |
|---|---:|---|---:|
| `calc/M02_examples.py` | 0 | vacío | 0,176 |
| `calc/M02_practicas_luna.py` | 0 | vacío | 0,200 |
| `calc/M03_ejemplos.py` | 0 | vacío | 1,163 |
| `calc/M03_practicas_luna.py` | 0 | vacío | 1,086 |
| `calc/M04_ejemplos.py` | 0 | vacío | 1,383 |
| `calc/M04_practicas_luna.py` | 0 | vacío | 1,388 |
| `calc/M05_diseno.py` | 0 | vacío | 1,088 |
| `calc/M05_practicas_luna.py` | 0 | vacío | 1,083 |
| `calc/M06_RR_CALAIRE.py` | 0 | vacío | 1,268 |
| `calc/M06_ejemplos.py` | 0 | vacío | 1,050 |
| `calc/M06_practica_I_grafico.py` | 0 | vacío | 0,626 |
| `calc/M06_practicas_luna.py` | 0 | vacío | 0,967 |

No hubo fallos, timeouts ni comprobaciones `assert` fallidas. Los programas no se ejecutaron con `-O`. El lanzador inicial, invocado con la ruta relativa pedida, emitió dos `RuntimeWarning` de `site` por la representación no normalizada de `sys.prefix`/`sys.exec_prefix`; por eso se normalizó la ruta para los procesos de prueba. **Ninguno de los doce procesos de script emitió esos avisos ni otros mensajes en stderr.**

### Resultados contrastados y artefactos

- M04-I5 reproduce `G=2,4374295323`, crítico unilateral `2,2208334515`, crítico bilateral `2,2743651271` y `Q_Dixon=0,8214285714`, concordantes con `M04_libreto.md:184`.
- M06-I reproduce `F=1,072952436`, `s_r=0,248261659` y `s_entre=0,023707434`, concordantes con `M06_libreto.md:185`.
- `M06_RR_CALAIRE.py` conserva su advertencia «EXPLORATORIO CONDICIONAL: signo, fechas y cruce de bloques pendientes». Que corra no valida esas condiciones históricas; la delimitación narrativa se mantiene.
- Se regeneraron y compararon los cinco HTML: `M02_practica_B_grafico.html`, `M02_practica_I_grafico.html`, `M02_practica_A_grafico.html`, `calc/M03_practica_I_probabilidad.html` y `M06_practica_I_residuos.html`. **Los cinco son idénticos byte a byte a los suministrados.** Esto comprueba reproducción del archivo, no una revisión visual en navegador.
- Evidencia completa de la ejecución disponible temporalmente en `/tmp/curso_corto_verif_sol_qgh_2lfs/results.json` y `/tmp/curso_corto_verif_sol_qgh_2lfs/stdout_stderr.txt`; copia ejecutada en `/tmp/curso_corto_verif_sol_qgh_2lfs/Curso_CORTO/`. Es evidencia temporal, no un recurso permanente exigido para usar el curso.

## 5. Registros y observaciones menores

1. **Inventario desactualizado:** `00_plan_corto.md:16–17` anuncia 13 scripts; se localizaron y ejecutaron 12. No se identifica en el plan el nombre de un supuesto decimotercer archivo: el hallazgo es una discrepancia del inventario, no prueba de que falte un cálculo concreto.
2. **Líneas de cambios desplazadas:** `logs_etapa1/cambios_p3.md:3` sitúa B6 en M02:80–92; su localizador actual es `M02_libreto.md:92–100`. `cambios_p2.md:3` conserva localizadores anteriores a las inserciones de M02. Además, `cambios_p2.md:4,7` no enumera las sustituciones actuales de `M03_libreto.md:306` y `M06_libreto.md:108,211`. La comparación con las fuentes sí las muestra; no son pérdidas de contenido.
3. **Conclusión del verificador 2 demasiado amplia:** `logs_etapa1/verif_p2.md:9–13` y `cambios_p2.md:9` no bastan para certificar ausencia de remisiones colgantes. Subsisten F02 y rutas con `S1_fundamentos`/`S2_modelos_calibracion` en F07. El `M1` de F01 también debe entrar en el cierre global, aunque se asignara al punto 1.
4. **Pendientes de las verificaciones anteriores:** siguen vigentes el M1, la falta de unidades, la MAD y la cita Otto. «Ya damos por visto» en `M02_libreto.md:22` es una transición mejorable, pero la apertura inmediatamente anterior evita que sea por sí misma una dependencia de otro módulo.
5. **Ficha de B6:** `M02_libreto.md:9` solo anuncia detección gráfica, mientras `:94` añade una regla numérica IQR. Conviene reflejarla en la ficha; la regla no contradice la caja de bigotes mínimo/máximo de `:46`, pues esta declara expresamente su convención y B6 presenta un criterio exploratorio distinto.
6. **Redundancias de redacción, no duplicación por colisión:** `M02_libreto.md:128` y `M06_libreto.md:46` repiten exclusiones en un mismo párrafo; `M04_libreto.md:13,34,292` repite la exclusión de la deducción de n−1. `M06_libreto.md:140` conserva «no cubre estas tablas» sin referente claro, y `:211` coloca «fuera del alcance» dentro de la cita de una explicación que sí se enseña. Conviene restringir inequívocamente la exclusión a las deducciones.
7. **Remisión residual en un comentario auxiliar:** `calc/M05_diseno.py:48` aún menciona «modelo de AX.4». No impide ejecutar ni constituye un requisito del alumno, pero la limpieza de anexos no fue exhaustiva fuera de los libretos.

## 6. Discrepancias heredadas detectadas durante la verificación

No son efectos de las tres ediciones ni pruebas de que se hayan pisado. Se registran separadamente para no equiparar «todos los scripts corren» con «todo el material coincide».

| Localizador actual | Discrepancia y efecto | Origen comprobado |
|---|---|---|
| `calc/M02_examples.py:94` frente a `M02_libreto.md:198` | El script de ejemplos añade **+1,8**, pero la escena narra **+1,6**. La ejecución obtiene media firmada 0,200000, media absoluta 0,555556 y s=0,724569; el texto da 0,178, 0,533 y 0,670. `calc/M02_practicas_luna.py:83` sí usa +1,6 y reproduce los valores del texto. | Script de ejemplos idéntico al original; el original del libreto ya narra +1,6. |
| `calc/M06_practica_I_grafico.py:39,94` frente a `M06_libreto.md:172` | La figura se titula nivel nominal de **90 nmol/mol**, mientras el enunciado de la práctica y la salida de `M06_practicas_luna.py` identifican **94 nmol/mol** para la misma selección BD_DIAS, filas 31–38. El HTML se reproduce fielmente, pero conserva la etiqueta discrepante. | El generador del curso completo ya contiene el rótulo 90. No se auditó aquí la asignación física del nivel en el Excel. |
| `M05_libreto.md:64` frente a `:98,102` | La escena atribuye al certificado el diseño de seis días; la práctica precisa que los seis días son un supuesto no declarado en la nota citada. La procedencia del supuesto debe formularse de manera consistente. | Ambas formulaciones ya están en el original; se identifica una diferencia de atribución textual, no se dicta un juicio sobre el certificado. |

## 7. Condición de cierre recomendada

Mantener la estructura M2–M6 y el puente exploración → pruebas: no requieren rediseño ni traslado completo de I5. Antes de cerrar la etapa 1, resolver la remisión a M1, las promesas de módulos/procedimientos excluidos, la tarea de ajuste no enseñada y los mínimos de autonomía y trazabilidad de la apertura y de B6 (F01–F06). Ajustar las rutas de uso de F07 y actualizar los registros/inventario para que describan el estado final.

**Balance final:** cobertura del PDF conservada; integración final de las ediciones sin pérdida o duplicación detectada; ejecución completa satisfactoria; adaptación todavía no completamente autocontenida ni libre de remisiones colgantes.
