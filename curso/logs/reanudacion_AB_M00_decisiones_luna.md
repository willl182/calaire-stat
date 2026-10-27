# Decisiones H-01–H-07 — reanudación A/B/M00

Fecha: 2026-10-27. Cotejo del informe `reanudacion_AB_M00_revision_haiku.md` con archivos reales. El informe de revisión refleja en parte una versión previa; se decidió según la evidencia actual. Alcance acotado a A/QAPP en M10, B/R&R y prácticas M00/script propio. No se revisaron ni modificaron citas o bibliografía.

| Hallazgo | Decisión | Justificación y evidencia | Acción |
|---|---|---|---|
| H-01 | Aplicado, con comprobación documental | PDF `docs/srp_qapp.pdf`, p. 18 (§6.2.1), extraído con `pdftotext -f 18 -l 18 -layout`: «the intercept must be ± 1ppb», sin «<». p. 23 (Tabla 7-1), extracción textual ` <+ 1 ppb`, mientras la inspección visual de la revisión constata la raya inferior y transcribe `<±`. No se interpreta cuál pasaje prevalece ni qué operación significa. | Se deja constancia de la discrepancia entre pasajes y se conserva escalamiento en M10, párrafo QAPP. |
| H-02 | Aplicado, con comprobación documental | p. 18 (§6.2.1) dice mínimo 12 puntos de concentración, incluyendo cero al inicio y al final; p. 23 (Tabla 7-1) dice «3 evaluation cycles of 10 concentrations and zero». Se registran las dos expresiones tal como aparecen; no se armonizan ni se interpreta si designan lo mismo. | M10 informa ambas descripciones y pide confirmación autorizada antes del uso operativo. |
| H-03 | Aplicado | Se ejecutó `./curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M06_RR_CALAIRE.py` (rc=0). La salida da F crítico nominal 3,315830, interacciones nominales [135, 360, 405, 455]; Bonferroni con m=10, α/10 y F crítico 6,354689 deja [135, 405]. F máximo de analista=1,238163. Omitir el contraste sin corregir no era una conclusión estadística errónea porque el informe ya identificaba Bonferroni, pero mostrar ambos umbrales/listas mejora la transparencia. Se mantienen las cautelas de análisis exploratorio y de que esto no valida históricamente el estudio. | B_RR_luna.md ahora reporta ambos resultados y umbrales. |
| H-04 | Rechazado como hallazgo original no verificado; descripción confirmada y afinada | Se abrió `casos_taller/datos_caso_C1.csv`: encabezado y seis filas fechadas 2023-02-02 a 2023-02-09, campos diarios y fuente de celdas `F-PSMT-01 Certificado ... .xlsm, Resumen!B6:I11`. Se cotejó `casos_taller/caso_C_historial_level2.md`, §§C1 (líneas 13–26): seis días; fechas derivadas de los nombres de archivo; valores de la hoja Resumen. Esto sustenta seis resúmenes diarios, no lecturas intradía. | B cita la descripción y CSV reales, explicita seis filas diarias y la fuente declarada; no se amplía la afirmación a datos que el CSV no contiene. |
| H-05 | Aplicado en libreto y script | El enunciado B presenta los registros de referencia e indicación y el extracto original de adquisición R03, cuyo campo de asociación documenta P03, sin incluir un cotejo docente que revele la solución. Se rechaza emparejar por orden o magnitud. | Se restituyó el bloque completo B: tareas, evidencia R03, tabla de resultado, solución trazable que conserva P99/50,8, faltante P04, decisión y rúbrica. El script ejecutó con rc=0 y reportó tres parejas completas y cero huérfanas tras aplicar R03. |
| F-H05b | Aplicado | El script queda identificado explícitamente como solución docente, no como plantilla para el alumnado. | Se conserva la salida numérica reproducible y el detalle docente del cotejo R03; no se retiraron bloques autorizados. |
| H-06 | Aplicado; F-H06 resuelto en esta ronda | La práctica A declara seis claves, datos completos y numéricos, unidades compatibles, cálculo, comparación con tolerancia, resultado y decisión. | El script declara metadatos de entrada `{"x": "nmol/mol", "y": "nmol/mol"}` y compara ambas unidades con la esperada; una prueba negativa comprueba que `y="ng/m3"` se rechaza. No se añade librería de unidades ni se cambian ejercicios. Se conservan errores recalculados y desacuerdo Q06; salida numérica reproducible. |
| H-07 | Aplicado y alineado con el libreto | La práctica I restituida conserva campaña C1 como factor y pide verificar claves campaña–analista–día–ciclo y reconstruir los resúmenes desde las parejas. | El script incorpora C1 en los registros y en la clave única; reproduce ocho claves, siete completas, un faltante y las cuatro medias de error indicadas; rc=0. |

## Salida de ejecución M00 actualizada

Comando: `./curso/.venv/bin/python -I curso/S1_fundamentos/calc/M00_practicas_luna.py` — rc=0.

```text
B antes de R03: parejas completas=2; indicaciones huérfanas=1; referencias no emparejadas=2
B cotejo R03: El registro de adquisición R03 vincula la indicación con la pareja de referencia P03; P04 no fue adquirido
B corrección trazable: id_original=P99; y_original=50.8; id_corregido=P03; motivo=el registro de adquisición R03 vincula esta lectura con P03; fuente=registro de adquisición R03
B después de R03: parejas completas=3; referencia P04 sin indicación adquirida=1; indicaciones huérfanas=0
B: errores {'P01': -0.2, 'P02': 0.4, 'P03': 0.8}
I: claves únicas campaña-analista-día-ciclo=8 (campaña C1)
I: n, media y, media e por analista-día {('A1', 1): (2, 50.3, 0.3), ('A1', 2): (2, 50.1, 0.1), ('A2', 1): (1, 49.8, -0.2), ('A2', 2): (2, 50.2, 0.2)}
I: completos=7; faltantes=1
A: controles claves_unicas=6; faltantes=0; unidades_compatibles= True prueba_negativa_ng/m3_rechazada= True
A: errores recalculados [-0.1, 0.2, 0.5, 0.8, 0.6, 1.0]
A: diferencias [0.0, 0.0, 0.0, 0.0, 0.0, 0.1] máxima= 0.1 tolerancia= 1e-06 acuerdo= False
```

## Salida de ejecución exploratoria B (M06)

Comando: `./curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M06_RR_CALAIRE.py` — rc=0. Salidas de umbral y resumen relevantes:

```text
max_F_analyst= 1.238163
significant_interactions= [135, 360, 405, 455]
multiplicidad: m=10; esperados falsos positivos bajo H0 global=0.50; Fcrit_interaccion_Bonferroni(alfa=0.05/10)=6.354689; superan=[135, 405]
```

El resultado completo se deja en esta bitácora de ejecución/decisiones, sin modificar el script M06 ni otros capítulos. El resultado sigue siendo exploratorio y condicional; no rehace el estudio histórico.
