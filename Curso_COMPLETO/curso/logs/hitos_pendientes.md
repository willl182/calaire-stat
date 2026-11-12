# Supervisión de pendientes 2–4 — claude-sol

Fecha: 2026-10-27. Se leyeron `curso/guia_libreto.md`, `curso/revision_final.md` y el alcance de `prop_e.md`. La petición actual autoriza iniciar ejercicios; no modifica el ámbito del curso ni autoriza auditorías de archivos como prácticas. Ejecutor: `claude-luna --effort low`; revisión intentada con el comando exacto `claude --model claude-haiku-5-5 --effort low`. No se hicieron commits ni se modificaron referencias bibliográficas. `revision_final.md` se conserva para evitar conflictos con el supervisor paralelo.

**Bloqueo transversal comprobado:** Haiku no está disponible en el proveedor configurado. Tanto la revisión A/B como la revisión M00 terminaron con código 1 y `API Error: 400 unknown provider for model claude-haiku-5-5`. Véanse `curso/logs/AB_revision_haiku.log` y `curso/logs/M00_practicas_revision.log`. No son hallazgos de contenido, no se generaron hallazgos H-xx y no hubo revisión Haiku. No se sustituyó silenciosamente el modelo, no se cambió autenticación/proveedor y no se declararon aprobaciones inexistentes. Se detuvo el pipeline antes de M01; las correcciones de errores comprobados por el supervisor sí se delegaron a luna.

## Hito 1 — A: grafía del criterio QAPP en S3 — 2026-10-27 13:54

**Qué se hizo.** Luna extrajo el texto de `docs/srp_qapp.pdf` y modificó el párrafo de M10-I2. El supervisor leyó el resultado y contrastó personalmente la fuente mediante extracción y renderizado de la página PDF 23, Element 7, página impresa 3/4. La primera afirmación de luna de que visualmente aparecía `<+`, no `±`, era incorrecta: la ampliación a 400 dpi muestra el signo más con una raya debajo. La extracción pierde ese rasgo. La grafía visible es **«<± 1 ppb»**, mientras que el texto extraído devuelve «<+ 1 ppb».

Se emitió S-01 y luna corrigió tanto el libreto como su informe. El supervisor volvió a leer el párrafo final: diferencia expresamente grafía visible y extracción, sin convertir `<±` en `|intercepto| < 1` ni inventar una interpretación autorizada. El significado operativo sigue requiriendo confirmación documental del responsable.

**Archivos tocados por este hito:**

- `curso/S3_comparacion_decision/M10_libreto.md`: únicamente el párrafo de la grafía; citas y bibliografía conservadas.
- `curso/logs/A_qapp_luna.md`.
- Evidencia de ejecución/revisión: `AB_ejecucion_luna.log`, `AB_revision_haiku.log`, `pendientes_correccion_luna.log`.
- `curso/logs/pendientes_revision_supervisor.md`: S-01 y reproducción exacta de la ampliación; la imagen temporal utilizada fue `/tmp/calaire_qapp_supervisor_signo.png`.

**Hallazgos Haiku y decisión.** No disponibles: error API 400, no H-xx. S-01 es del supervisor, no de Haiku; aplicado por luna y comprobado visualmente por el supervisor.

**Estado: bloqueado para cierre del pipeline.** La corrección tipográfica está realizada y verificada; falta la revisión Haiku obligatoria. El uso operativo del criterio, además, queda bloqueado por interpretación semántica no autorizada. No se afirma que se haya resuelto esa interpretación.

## Hito 2 — B: suficiencia y validación histórica del R&R de S2 — 2026-10-27 13:54

**Qué se hizo.** Luna examinó `docs/Resultados R&r_2022 2023 (1).xlsx`, las advertencias de `curso/S2_modelos_calibracion/calc/M06_RR_CALAIRE.py`, la revisión previa S2 y los datos/documentos de `casos_taller/`. Hay datos propios, pero **no hay información suficiente para validar históricamente un R&R con errores firmados y componentes físicos identificados**.

El supervisor abrió también el libro R&R y confirmó `BASE DE DATOS!B70 = VALORES ABSOLUTOS`, las referencias a las pruebas 171/173 y las hojas por nivel. Inspeccionó el inventario del otro libro `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm`: contiene un certificado y hojas Dia0–Dia6; su mera existencia no acredita la reconstrucción del estudio histórico de dos analistas ni resuelve el mapeo de bloques. No se confundieron resúmenes de una calibración o comparaciones externas NIST con un R&R histórico validado de CALAIRE.

Luna y supervisor ejecutaron el script reproducible **ya existente** `M06_RR_CALAIRE.py`, sin alterarlo, con `curso/.venv/bin/python -I`: rc=0. F máximo de analista 1,238163; tras Bonferroni las interacciones que exceden el umbral corresponden a niveles 135 y 405. Son cálculos exploratorios condicionales de magnitudes tabuladas, no ANOVA validado de errores con signo. No se estima repetibilidad intradía desde un único resumen diario. S-03 pidió reproducibilidad adicional del inventario: luna dejó en el informe un comando completo de lectura con openpyxl; no añadió otro script permanente redundante.

**Datos exactos requeridos para desbloquear:**

1. Archivo fuente con una fila por lectura: referencia SRP `x`, indicación Level 2 `y`, unidades, escala y error firmado reproducible `e=y−x`; no solo `|e|`.
2. Nivel nominal/observado, identificador de pareja SRP–Level 2, lectura, ciclo y orden de adquisición.
3. Identificador inequívoco del operador por observación, aclaración documental de A1/A2 e identificación/SN de los equipos.
4. Fecha/hora, campaña/calibración y mapeo documental de cada uno de los tres bloques de seis días a sus campañas/días; confirmación de qué factores están cruzados o anidados y qué días son comparables.
5. Correspondencia de las series 171/173 y explicación de las discrepancias previamente señaladas de conteos y tres bloques frente a cinco pares.
6. Réplicas originales intradía por operador×día×nivel, necesarias para separar lectura de día; estado del SRP y Level 2, mantenimiento y cambios de configuración.
7. Fórmulas y transformaciones que produjeron los valores absolutos, exclusiones —incluido día 0—, faltantes y trazabilidad de cualquier promedio previo.

**Archivos tocados por este hito:** `curso/logs/B_RR_luna.md`, `curso/logs/B_RR_verificacion_supervisor.out`; logs compartidos A/B y `pendientes_revision_supervisor.md`. Se preservaron libros originales, el script histórico y los libretos S2.

**Hallazgos Haiku y decisión.** No disponibles por el error API registrado; no H-xx. S-03 es del supervisor: atendido mediante diagnóstico reproducible incluido en el informe, sin promover el cálculo exploratorio a validación histórica.

**Estado: bloqueado.** Datos reales presentes pero insuficientes en signo, trazabilidad y diseño para la validación histórica; se requiere la información enumerada. Además falta revisión Haiku. La búsqueda, diagnóstico y reproducción del cálculo exploratorio sí se realizaron.

## Hito 3 — C/M00: prácticas de estructura de datos y reproducibilidad — 2026-10-27 13:54

**Qué se hizo.** Luna desarrolló las tres prácticas de M00, una B, una I y una A, como ejercicios aplicados a un caso docente Level 2/ozono. Incluyen datos rotulados simulados, enunciado, tareas, solución docente, interpretación y criterio de logro; no atribuyen resultados simulados a CALAIRE. Se escribió y ejecutó `calc/M00_practicas_luna.py`.

La revisión Haiku falló antes de leer el capítulo. El supervisor sí leyó los tres ejercicios y su script: detectó una contradicción de claves/conteos en B y emitió S-02. La primera corrección de luna seguía sin aportar evidencia suficiente para resolver la pareja desplazada; el supervisor la rechazó y precisó los datos y el registro autorizado docente R03. Luna aplicó la segunda corrección. El supervisor leyó de nuevo el bloque y el script y los ejecutó con rc=0:

- B: antes del cotejo, dos parejas completas, una indicación P99 huérfana y dos referencias sin pareja; R03 autoriza explícitamente P99→P03 sin borrar el original. Después: tres errores `−0,2; 0,4; 0,8` nmol/mol, P04 faltante y ninguna indicación huérfana. No hay reasignación por magnitud ni por orden.
- I: cuatro grupos analista-día con tamaños `2, 2, 1, 2`; siete valores completos y un faltante; medias de error `0,3; 0,1; −0,2; 0,2` nmol/mol.
- A: máximo desacuerdo entre salidas `0,1` nmol/mol, superior a tolerancia predeclarada `0,000001`; no se declara acuerdo. Se preservan originales y se investiga la salida discrepante.

**Archivos tocados por este hito:**

- `curso/S1_fundamentos/M00_libreto.md`: solo los tres bloques de prácticas.
- `curso/S1_fundamentos/calc/M00_practicas_luna.py`.
- `curso/logs/M00_practicas_luna.md`.
- `curso/logs/M00_practicas_verificacion_supervisor.out`.
- Logs: `M00_practicas_ejecucion.log`, `M00_practicas_revision.log`, `M00_correccion_supervisor_final.log`, `pendientes_correccion_luna.log`.
- `curso/scripts/desarrollar_practicas_pendientes.py`: orquestación por capítulo de luna → Haiku → luna; se detuvo correctamente ante fallo de revisión y no ejecutó M01.

**Hallazgos Haiku y decisión.** No hubo revisión ni H-xx por error de proveedor. S-02 es del supervisor: primera corrección rechazada por insuficiente; segunda aplicada y verificada. No se presenta esta supervisión como sustitución de Haiku.

**Estado: bloqueado.** Tres prácticas desarrolladas y corregidas en estado de borrador; NO aprobadas ni cerradas mediante el pipeline obligatorio. Falta Haiku y la ronda luna de decisiones sobre los hallazgos que emita realmente.

## Cierre

**Resultado parcial y bloqueado, no entrega completa.**

| Pendiente | Resultado real |
|---|---|
| 3 — grafía QAPP | Corregida a representación visible `<±`, distinguiéndola de extracción `<+`; comprobada visualmente por el supervisor. Falta Haiku y confirmación de significado operativo. |
| 2 — R&R histórico | Fuentes localizadas y cálculo exploratorio reproducido; validación bloqueada por datos de signo/diseño/trazabilidad faltantes, enumerados en Hito 2. |
| 4 — M00 | Tres prácticas desarrolladas, corregidas y con cálculo reproducido; revisión Haiku bloqueada. |
| 4 — M01–M12 | No iniciados: siguen sus 36 marcadores. No se declara desarrollo ni revisión. |
| 4 — M13 | No iniciado: sigue su marcador A. |
| 1 — citas | Fuera de alcance, reservado al otro supervisor; no se modificaron bibliografía ni citas existentes. |
| 5 — git | No se hicieron commits ni acciones de publicación. |

Comprobación final: **37 marcadores pendientes** en M01–M13; tres bloques `[PRÁCTICA]` desarrollados únicamente en M00. `git diff --check` terminó con rc=0. Los dos scripts ejecutados por el supervisor terminaron con rc=0; sus resultados están en los archivos `.out` registrados. No se atribuyen a esta tarea los cambios concurrentes del supervisor de citas ni archivos preexistentes del lanzador.

Para reanudar: restablecer disponibilidad del modelo exacto `claude-haiku-5-5` en el entorno autorizado, realizar revisiones reales A/B/M00, delegar a luna decisiones y correcciones de cada H-xx y volver a verificar; después iniciar M01–M13, **un capítulo por hito** con sus rondas luna/Haiku/luna. No se cambió el proveedor ni se usó otro modelo para aparentar cumplir la revisión exigida.

## Hito 4 — A: revisión reanudada y cierre tipográfico QAPP — 2026-10-27 14:15

**Qué se hizo.** Se leyó el historial sin repetir el desarrollo. Haiku se invocó con `env -u ANTHROPIC_BASE_URL -u ANTHROPIC_API_KEY -u CLAUDE_CODE_AUTO_MODE_SERVER`; esta vez sí produjo revisión real. El supervisor abrió la ampliación de la Tabla 7-1 y confirmó `<±`; reprodujo extracción de p. 23. Luna cotejó además p. 18 y corrigió únicamente el párrafo QAPP de M10: §6.2.1 presenta `± 1ppb` sin `<`, y las descripciones de concentraciones de texto y tabla se conservan separadas, sin armonización inventada. El supervisor leyó el párrafo final en disco.

**Archivos tocados.** `curso/S3_comparacion_decision/M10_libreto.md` (solo párrafo QAPP); `curso/logs/A_qapp_luna.md`; `reanudacion_AB_M00_revision_haiku.md`, `reanudacion_AB_M00_decisiones_luna.md` y logs de reanudación. Ninguna referencia bibliográfica modificada por esta supervisión.

**Hallazgos Haiku y decisión.** H-01 y H-02 aplicados por luna: diferencias entre §6.2.1 y Tabla 7-1 explicitadas; no se infiere desigualdad de valor absoluto. La corrida de corrección alcanzó su límite de 600 s; se verificaron los cambios guardados, no se atribuye éxito a la terminación del proceso.

**Estado: cerrado para la grafía (pendiente 3).** La confirmación del significado operativo permanece bloqueada hasta respuesta autorizada del responsable; no se declara resuelta mediante una transcripción.

## Hito 5 — B: revisión reanudada de suficiencia histórica R&R — 2026-10-27 14:15

**Qué se hizo.** Haiku revisó la evidencia y ejecutó el script histórico. Luna añadió comparación nominal/Bonferroni y comprobó abriendo el CSV los seis resúmenes diarios de febrero de 2023. El supervisor ejecutó de nuevo `M06_RR_CALAIRE.py` con `curso/.venv/bin/python -I`, rc=0; salida en `curso/logs/reanudacion_RR_supervisor.out`. Se conserva el script existente, sin simular signos ni diseño histórico.

**Archivos tocados.** `curso/logs/B_RR_luna.md`, `reanudacion_AB_M00_decisiones_luna.md`, revisión y logs compartidos A/B/M00, salida del supervisor. Ningún libro fuente ni libreto S2 modificado por este hito.

**Hallazgos Haiku y decisión.** H-03 aplicado como transparencia adicional: umbral nominal 3,315830, niveles 135/360/405/455; Bonferroni 6,354689, niveles 135/405. La lista corregida anterior no era errónea. H-04 rechazado como defecto no verificado por el revisor; luna abrió las seis filas del CSV y afinó procedencia. Ambas decisiones están documentadas. Haiku confirma insuficiencia para validar, no ausencia de datos reales.

**Estado: bloqueado para validación histórica (pendiente 2), diagnóstico cerrado.** Sigue siendo necesaria la lista exacta de siete categorías del Hito 2: lecturas x/y y errores firmados; nivel/pareja/lectura/ciclo/orden; operador y SN; fecha/hora/campaña y mapeo de bloques; correspondencia 171/173 y conteos; réplicas intradía y configuración; transformaciones, exclusiones y faltantes. La revisión Haiku ya no está bloqueada por proveedor.

## Hito 6 — C/M01: modelo y cambio de escala — 2026-10-27 14:18

**Qué se hizo.** Luna desarrolló tres prácticas B/I/A con datos simulados rotulados: recálculo óptico de tres concentraciones; aplicación de los dos pares de coeficientes declarados y error relativo; identificación de entradas comunes en absolutos y diferencias. Haiku revisó el capítulo real y luna decidió cada hallazgo. El supervisor leyó los tres bloques, la revisión, las decisiones y el script; ejecutó este último con `python -I`, rc=0. Incrementos de los pares: 1,2445935 % y 1,2911068 %; salida sobre 400: 405,164427; diferencias A: 0,4 y 0,8 nmol/mol.

**Archivos tocados.** `curso/S1_fundamentos/M01_libreto.md` (prácticas y aclaración adyacente registrada por luna); `calc/M01_practicas_luna.py`; `curso/logs/M01_practicas_luna.md`, `M01_practicas_revision_haiku.md`, logs de ejecución/revisión/corrección y `reanudacion_M01_supervisor.out`. No se editaron claves ni referencias bibliográficas.

**Hallazgos Haiku y decisión.** H-01–H-09 aplicados (H-09 con ajuste): par implementado explícito, cálculos I automatizados, evidencia de error/corrección/conversión, nomenclatura y origen, contraste de cocientes, conclusión A y claridad del script/generación. Supervisor S-M01-01 detectó una confusión dimensional introducida al ampliar la conversión: luna distinguió presión parcial en atm, fracción molar adimensional y nmol/mol. Se leyó la corrección final y se reejecutó el script.

**Estado: cerrado.** Tres ejercicios aplicados con solución y criterio de logro, revisión Haiku real y decisiones comprobadas. El cierre no valida escalas ni instrumentos reales del laboratorio.

## Hito 7 — C/M00: revisión final de las tres prácticas — 2026-10-27 14:28

**Qué se hizo.** Se restituyeron los tres bloques completos bajo la autorización actual de ejercicios, sin retirar datos ni soluciones por la antigua fase de contenido. Supervisor leyó bloques, script y revisión real; volvió a ejecutar con `python -I`, rc=0. B conserva originales y asociación documental R03, I incluye campaña C1 en las claves, A detecta discrepancia 0,1 > 0,000001. La prueba negativa de metadatos rechaza y en ng/m3.

**Archivos tocados.** `S1_fundamentos/M00_libreto.md` (prácticas y normalización trivial de encabezados); `calc/M00_practicas_luna.py`; `M00_bitacora_luna.md`; `logs/M00_practicas_luna.md`; revisión final `M00_practicas_revision_final_haiku.md`, decisiones `reanudacion_AB_M00_decisiones_luna.md`, logs de reanudación y `reanudacion_M00_supervisor.out`.

**Hallazgos Haiku y decisión.** H-05 y H-07 resueltos; H-06 ampliado por F-H06: luna aplicó metadatos explícitos, comparación con unidad esperada y prueba negativa. F-H05b aplicado: script exclusivamente docente, no plantilla del alumnado. Supervisor comprobó decisiones en bitácora y archivo compartido, no solo stdout.

**Estado: cerrado.** Tres prácticas aplicadas, revisión y decisiones reales; cálculo y control negativo reproducidos.

## Hito 8 — C/M04: inferencia y planificación — 2026-10-27 14:28

**Qué se hizo.** Supervisor leyó tres bloques, script, revisión y decisiones; reprodujo medias, intervalos t, pruebas pareada/Welch/varianzas, potencia, equivalencia y consistencia matricial. Tras las correcciones finales, `python -I calc/M04_practicas_luna.py` termina rc=0; salida en `logs/reanudacion_M04_supervisor.out`.

**Archivos tocados.** `S1_fundamentos/M04_libreto.md` (prácticas y ajustes adyacentes registrados); `calc/M04_practicas_luna.py`; `logs/M04_practicas_luna.md`, revisión Haiku, logs de ejecución/corrección y `supervisor_M04_adicional.md`. Referencias preservadas.

**Hallazgos Haiku y decisión.** H-01–H-08 decididos individualmente por luna: vectores, comprobaciones independientes, rúbrica, definición de Dixon, IC95, redacción, incertidumbre de s y implementación de potencia. Supervisor S-M04-01–03 aplicados: efecto 0,30/0,60 para d=0,5; distinción Q de Dixon/Q matricial; crítico Grubbs unilateral calculado y Dixon didáctico sin alfa atribuido. S-M04-04 aplicado: AND para excluir magnitudes en ambos sentidos. La primera aserción falló por identidad de numpy.bool_ con False; luna corrigió y supervisor reejecutó satisfactoriamente. El IC95 de B contiene +0,30, por lo que el control es False.

**Estado: cerrado.** Tres prácticas completas y reproducibles; no se confunde no rechazo con equivalencia ni se autoriza exclusión automática de extremos.

## Hito 9 — C/M09: comparación con dependencia y referencia común — 2026-10-27 14:30

**Qué se hizo.** Supervisor leyó las tres prácticas, script completo, revisión y decisiones; ejecutó `python -I S3_comparacion_decision/calc/M09_practicas_luna.py`, rc=0 (`logs/reanudacion_M09_supervisor.out`). B obtiene En 0,6000 y −0,2561; I obtiene covarianza 0,0180, U de diferencia 0,325576 y cociente 1,0750 frente a 0,7000 sin covarianza. A calcula diferencias 0,30 y 0,90 con sensibilidad a dos hipótesis admisibles, sin emitir conformidad.

**Archivos tocados.** `S3_comparacion_decision/M09_libreto.md` (tres prácticas), `calc/M09_practicas_luna.py`, `logs/M09_practicas_luna.md`, revisión Haiku y logs por capítulo, salida del supervisor. No bibliografía.

**Hallazgos Haiku y decisión.** H-01–H-07 aplicados individualmente por luna: sensibilidad numérica de covarianza, identificación de herramienta y controles, datos propios del punto A, decisiones trazables, ritmo narrado y explicitación del cambio de lado del criterio. Supervisor cotejó las cifras nuevas y las restricciones de admisibilidad en archivos reales.

**Estado: cerrado.** Tres ejercicios aplicados; compatibilidad, grado de equivalencia y conformidad se mantienen separados.

## Hito 10 — C/M12: indicadores, límites y periodos — 2026-10-27 14:32

**Qué se hizo.** Supervisor leyó prácticas B/I/A, script, revisión y decisiones; ejecutó con `python -I`, rc=0 (`logs/reanudacion_M12_supervisor.out`). B diferencia media firmada 0 % de media de magnitudes 2 %. I obtiene límites unilaterales 4,1699 % y 2,7358 %, IC bilateral ±2,4834 % y media de magnitudes 2,0200 % tras cambio de escala. A evalúa las tres verificaciones posteriores, el agregado del periodo y la señal anterior al mantenimiento; u de media con componente común =0,8718 puntos porcentuales.

**Archivos tocados.** `S3_comparacion_decision/M12_libreto.md` (prácticas), `calc/M12_practicas_luna.py`, `logs/M12_practicas_luna.md`, revisión Haiku, logs por capítulo y salida de supervisión. Referencias no modificadas por esta tarea.

**Hallazgos Haiku y decisión.** H-01–H-06 aplicados individualmente: tres incumplimientos posteriores explícitos, señal de control también anterior, muestra y cobertura definidas, reproducción ampliada del script, contexto ozono/SRP y redacción B sin una escala temporal inventada. Se cotejaron los cambios con datos y resultados reales en disco.

**Estado: cerrado.** Tres prácticas aplicadas; incertidumbre de la media, límites de confianza, desempeño agregado, control y conformidad individual no se intercambian.

## Hito 11 — C/M03: distribuciones, dependencia y promedios — 2026-10-27 14:41

**Qué se hizo.** Supervisor leyó tres prácticas, revisión, decisiones y script; ejecutó con `python -I`, rc=0 (`logs/reanudacion_M03_supervisor.out`). Comprobó conversiones rectangular/triangular/resolución/U, dependencia de diferencias, seis puntos de Blom, matrices y razón u=0,40625 frente a 0,53125 sin covarianza, y estrategias temporales. Renderizó y abrió captura Chromium del gráfico final, con tabla, unidades y coma decimal; sin colisiones visibles.

**Archivos tocados.** `S1_fundamentos/M03_libreto.md` (prácticas), `calc/M03_practicas_luna.py`, `calc/M03_practica_I_probabilidad.html`, `logs/M03_practicas_luna.md`, revisión y logs; `supervisor_M03_adicional.md`. Se retiró solo el artefacto generado mal denominado .svg, que realmente contenía HTML.

**Hallazgos Haiku y decisión.** H-01–H-09 aplicados por luna: datos/cuantiles correctos, razón sin covarianza, inferencia de varianzas reservada a M04, seis pares explícitos, figura reproducible, estimador temporal definido, triangular/t, tarea temporal y supuesto normal diferenciado del origen sintético. S-M03-01/02 aplicados: extensión HTML y formato decimal. S-M03-03 aplicado: valores A=1/B=0,8 entregados en enunciado y lista normalizada de 13 valores para Pearson separada inequívocamente de 16 lecturas con deriva para los bloques. Supervisor comprobó los cambios y reejecutó.

**Estado: cerrado.** Tres ejercicios aplicados con soluciones verificadas; figura inspeccionada visualmente, no solo como texto.

## Hito 12 — C/M08: presupuesto, cobertura y función en intervalo — 2026-10-27 14:41

**Qué se hizo.** Supervisor leyó prácticas, script, revisión y decisiones, y ejecutó `python -I calc/M08_practicas_luna.py`, rc=0 (`logs/reanudacion_M08_supervisor.out`). B u=0,293598/U=0,587197; I distingue lectura, media y futuro, cobertura condicional y cadena sin doble conteo; A encuentra cruce 81,347138 en [0,500] y contrasta perturbaciones exactas con linealización. Tabla y malla verifican el intervalo; prop_e no exige gráfica en este módulo.

**Archivos tocados.** `S2_modelos_calibracion/M08_libreto.md` (prácticas y ajustes adyacentes registrados), `calc/M08_practicas_luna.py`, `logs/M08_practicas_luna.md`, revisión y logs de capítulo/supervisión. Referencias preservadas.

**Hallazgos Haiku y decisión.** H-01–H-05 y H-07 aplicados; H-06 resuelto mediante alternativa tabular documentada, sin gráfica ficticia. H-02 se atendió con subtareas y agrupación explícita. Supervisor S-M08-01 detectó que las nuevas subtareas no estaban realmente reproducidas pese a la bitácora: luna añadió conversión/perturbación, sensibilidades, covarianza y comparación de diferencias, y diagnóstico de linealización al script. Supervisor leyó los cálculos nuevos y reejecutó: u diferencia 0,320212 con covarianza/0,534917 sin ella, cambios exactos −16,6667/+25 frente a ±20 local.

**Estado: cerrado.** Tres prácticas aplicadas con reproducción completa de las subtareas; sin atribuir incertidumbres o CMC simuladas al laboratorio.

## Hito 13 — C/M10: regla, riesgo y dependencia — 2026-10-27 14:44

**Qué se hizo.** Supervisor leyó tres prácticas, script, revisión y decisiones. Ejecutó con `python -I`, rc=0 (`logs/reanudacion_M10_supervisor.out`). B aplica intervalos y regla suministrada; I compara cuatro probabilidades condicionales y ambas reglas inclusivas aceptan y=9; A separa riesgo global conjunto, riesgo condicional del promedio y riesgo específico posterior con ambas colas.

**Archivos tocados.** `S3_comparacion_decision/M10_libreto.md` (prácticas; se conserva párrafo QAPP del hito A), `calc/M10_practicas_luna.py`, `logs/M10_practicas_luna.md`, revisión Haiku, logs y salida de supervisión. No referencias.

**Hallazgos Haiku y decisión.** H-01–H-09 aplicados individualmente: estadístico de decisión, posterior reproducida/normalizada, decisión específica, extremos inclusivos, comprobaciones reales, recomendación condicionada, origen fijo y limpieza de afirmaciones/código. Supervisor S-M10-01 detectó que la separación de modelos anunciada por bitácora no estaba en el enunciado: luna definió explícitamente tres subcasos y tareas, con u=0,8 para riesgo global de una medición, u del promedio con covarianza para theta fijo y u=6 para posterior específica. Supervisor leyó esa corrección real y reejecutó.

**Estado: cerrado.** Tres prácticas aplicadas; eventos, condicionamientos y modelos no se intercambian. El significado operativo del signo QAPP permanece fuera de este cierre, como se documentó en A.

## Hito 14 — C/M13: práctica integrada de métodos numéricos — 2026-10-27 14:44

**Qué se hizo.** Supervisor leyó la práctica A completa con cuatro apartados, script, revisión y decisiones; ejecutó con `python -I`, rc=0 (`logs/reanudacion_M13_supervisor.out`). Se contrastan propagación lineal/Monte Carlo, cinco salidas correlacionadas, bootstrap por días y OLS/Huber. MC conserva u=1,041437 sin redondear para decidir; diferencias de extremos 0,011715/0,000601 <0,05. Bootstrap de pendiente [1,00143187;1,00159362]; Huber conserva peso no nulo del punto alterado.

**Archivos tocados.** `S4_numericos_integracion/M13_libreto.md` (práctica y precisión adyacente registrada), `calc/M13_practicas_luna.py`, `calc/M13_ejemplos.py` (constantes/reglas compartidas), `logs/M13_practicas_luna.md`, revisión, logs y salida de supervisión. No bibliografía.

**Hallazgos Haiku y decisión.** H-01–H-07 aplicados: precisión sin redondeo, comprobación por jacobiana finita con alcance limitado, secuencia RNG bootstrap coherente, escalamiento y criterio por apartado, 36 datos accesibles y datos centralizados. Supervisor S-M13-01 detectó fallo de importación con -I; luna reemplazó import implícito por carga explícita del archivo hermano mediante importlib y ruta relativa a __file__. Supervisor leyó el cambio y ejecutó satisfactoriamente en aislamiento.

**Estado: cerrado.** Una práctica A de cuatro apartados, no un taller adicional; reproducibilidad y criterios individuales comprobados, sin validación de resultados reales atribuida al laboratorio.

## Hito 15 — C/M02: ronda de cierre — 2026-10-28 16:20

**Qué se hizo.** Reanudación con Opus 5.5 como supervisor y Haiku como ejecutor (continúa a luna) y revisor en corridas separadas. Haiku hizo la revisión de cierre, que había quedado vacía; el ejecutor aplicó o rechazó cada hallazgo; el supervisor reejecutó `calc/M02_practicas_luna.py` con `-I`, rc=0, y leyó la tabla de decisiones.
**Archivos.** `S1_fundamentos/M02_libreto.md` (enunciado B, escena A1 y su diapositiva, escena I2), `calc/M02_practicas_luna.py` (fondo con f-string, `scatter_panel` sin variable global), HTML regenerados, `logs/M02_practicas_luna.md`, `logs/M02_practicas_revision_cierre_haiku.md`, `logs/cierre_M02_*.log`.
**Hallazgos Haiku y decisión.** Se aplicaron H-01–H-06. Se rechazaron H-07 y H-08: son del capítulo M06 y de citas, y se trataron en el Hito 17 o quedan para el otro supervisor.
**Estado: cerrado.**

## Hito 16 — C/M05: ronda de cierre — 2026-10-28 16:20

**Qué se hizo.** El ejecutor resolvió los hallazgos de la revisión de cierre de Haiku (`logs/M05_practicas_revision_cierre_haiku.md`), que no tenían decisión. El supervisor reejecutó el script, rc=0.
**Archivos.** `S2_modelos_calibracion/M05_libreto.md` (prácticas B e I), `calc/M05_practicas_luna.py` (`factorial`, `design_counts`) y la bitácora unificada `logs/M05_practicas_luna.md`.
**Hallazgos Haiku y decisión.** Se aplicaron H-01–H-05: doce contrastes simples, de los que cuatro superan 0,50; bitácora unificada; potencia de 0,284 a 0,495; escalonado calculado; nota al instructor. Se rechazó H-06 porque `guia_libreto.md` no se modifica. H-07 se aplicó en parte: la celda E17 no declara seis días y el dato pasa a supuesto de la práctica.
**Estado: cerrado.**

## Hito 17 — C/M06: ronda de cierre — 2026-10-28 16:20

**Qué se hizo.** Haiku hizo la revisión de cierre, que estaba vacía, y comprobó las tres frases de narración pendientes. El ejecutor corrigió. El supervisor reejecutó el script (rc=0), leyó las líneas 152 y 219 y corrigió él mismo la línea 35 de la bitácora, una corrección trivial: la afirmación de validación de paleta queda como corrida anterior no repetible.
**Archivos.** `S2_modelos_calibracion/M06_libreto.md` (enunciado I 90→94 según BD_DIAS, escenas I4, A1 y A2), `calc/M06_practicas_luna.py`, `logs/M06_practicas_luna.md`.
**Hallazgos Haiku y decisión.** Se aplicaron H-01 y H-03–H-06. H-02 lo rechazó el ejecutor y lo aplicó el supervisor. Se rechazó H-07, sobre la etiqueta `[PRÁCTICA]` frente a la guía: el orquestador lo deja como decisión del usuario. Se rechazó H-08 (cita NIST frente a Hahs-Vaughn) y se pasa al supervisor de citas.
**Estado: cerrado.**

## Hito 18 — C/M07: ronda de cierre — 2026-10-28 16:20

**Qué se hizo.** El ejecutor decidió los H-01–H-07 de la revisión de cierre de Haiku. El supervisor reejecutó el script, rc=0.
**Archivos.** `S2_modelos_calibracion/M07_libreto.md` (prácticas B e I, material A2), `logs/M07_practicas_luna.md`.
**Hallazgos Haiku y decisión.** Se aplicaron H-01, H-02 y H-04–H-07. Se rechazó H-03 (etiqueta `[PRÁCTICA]`, la convención de la fase de ejercicios).
**Estado: cerrado.**

## Hito 19 — C/M11: ronda de cierre — 2026-10-28 16:20

**Qué se hizo.** El ejecutor decidió los H-01–H-05 de la revisión de cierre de Haiku, regeneró el gráfico B y lo renderizó en Chromium. El supervisor reejecutó el script, rc=0.
**Archivos.** `S3_comparacion_decision/M11_libreto.md` (solución I), `calc/M11_practicas_luna.py` (rejilla I/MR), `M11_practica_B_grafico.html`, `logs/M11_practicas_luna.md`.
**Hallazgos Haiku y decisión.** Se aplicaron H-01 y H-03–H-05. Se rechazó H-02 porque toca referencias y citas.
**Estado: cerrado.**

## Cierre — 2026-10-28 16:20

| Pendiente | Estado |
|---|---|
| 3 — grafía QAPP | Cerrado (Hitos 1 y 4): `<±` visible frente a `<+` extraído. El significado operativo queda a confirmar por el responsable. |
| 2 — R&R histórico | **Bloqueado** (Hitos 2 y 5): hay datos reales, pero son insuficientes. La lista exacta de los siete datos requeridos está en el Hito 2. El cálculo exploratorio se reproduce con `M06_RR_CALAIRE.py`. |
| 4 — prácticas | Cerrado: M00–M12 con 3 prácticas cada uno y M13 con 1, todas aplicadas al caso ozono/SRP y revisadas por Haiku. Los 14 scripts de prácticas terminan con rc=0. Ya no queda ningún marcador `[PRÁCTICA — fase de ejercicios]`. |
| 1 — citas | Fuera de alcance. Se trasladan M06 H-08 y M11 H-02. |
| 5 — git | Sin commits. |

**Decisión abierta para el usuario.** `guia_libreto.md` §1 todavía dice «fase actual: solo contenido» y solo permite el marcador de práctica. Hay que actualizar la guía a la fase de ejercicios; no se cambió sin autorización.
