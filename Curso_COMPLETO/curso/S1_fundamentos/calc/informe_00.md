# Revisión directa M00 y controles de sección

**Procedencia:** informe auxiliar de la segunda ejecución interrumpida (2026-10-25), preservado como antecedente. Sus identificadores S-028/S-029 se mantienen en la revisión consolidada. No acredita por sí solo la reanudación.

**Recomprobación del 2026-10-26:** se leyeron de nuevo libreto, bitácora, revisión Haiku, scripts y auditorías. Se regeneraron con `pdftotext -layout` los tres extractos `referencias_00/`; se cotejaron B.2.19, C.2.19, la nota de tabla 1 y ISO 17025 7.5.1–2/7.11.2/7.11.6. `sha256sum -c fuentes_00_sha256.txt` confirmó las nueve identidades registradas. Se volvieron a ejecutar M00 y el contraste Decimal; resultados iguales a los documentados abajo. Las decisiones vigentes están en `../S1_revision_sol.md`, incluidas D2-01–D2-04.

Leídos íntegramente: plan maestro, guía, prop_e, revisión final de prop_e, M00 libreto/bitácora/revisión Haiku, auditoría de interrupción y script M00. Se conserva el plan anterior; esta reanudación no vuelve verdaderas por sí mismas las afirmaciones de su primera ejecución.

## Candidatos de la interrupción

| Hallazgo | Candidato | Ubicación | Severidad | Problema anterior | Decisión y justificación |
|---|---|---|---|---|---|
| S-001 | C01 | M00, introducción B, definición de error | alta | prop_e no constituye respaldo técnico del error. | Conservada: GUM B.2.19 define resultado menos valor verdadero y su nota 1 admite valor convencional en la práctica. Convención x/y queda separada del respaldo técnico. |
| S-002 | C02 | M00, introducción B, unidades | alta | Equivalencia ppb y nmol/mol carecía de respaldo; la candidata atribuyó su nota a tabla 2. | Ajustada: equivalencia correcta, numeral incorrecto. PDF EN 14625 §8.2, tabla 1, nota, dice «nmol/mol = ppb»; tabla 2 trata puntos de consigna y estabilidad. Corregidas narración y bibliografía. |
| S-003 | C03 | M00, marcador B | media | Título omitía pareja desplazada, faltante y trazabilidad de corrección. | Conservada: restaura alcance exacto de M0-B; sigue siendo un único marcador sin enunciado ni solución. |
| S-004 | C04 | M00, I2, pizarra ancho/largo | media | lectura se usaba como índice y magnitud. | Conservada: columna y con unidad, lectura reservada al índice. Complementada la enumeración posterior mediante S-029. |
| S-005 | C05 | M00, I2, narración de transformación | media | Narración llamaba lectura tanto al índice como al valor. | Conservada: y contiene indicación; ciclo y lectura identifican registros. |
| S-006 | C06 | M00, referencias | alta | Faltaban entradas bibliográficas de GUM y EN usadas por C01/C02. | Ajustada: conservar ambas entradas, corregir EN a tabla 1 y añadir GUM C.2.19 por S-028. No conservar numeral falso. |
| S-007 | C07 | calc/M00_ejemplos.py, contraste Calc | media | Comparación imprimía diferencia sin hacer fallar una discrepancia. | Conservada: assert de longitudes y tolerancia convierte el criterio en comprobación ejecutable; ejecución real de Calc satisfactoria. |

## Hallazgos nuevos

| Hallazgo | Ubicación | Severidad | Problema | Corrección aplicada |
|---|---|---|---|---|
| S-028 | M00 B1, media 0,425; referencias | media | Cita de alcance prop_e usada para media aritmética. | Cita GUM C.2.19 y entrada bibliográfica ampliada. Es resumen aritmético, no inferencia ni precisión del fotómetro. |
| S-029 | M00 I2, ejemplo ancho/largo; script bloque I2 | media | Tres indicaciones supervivientes no dejaban salida separada con clave del faltante; enumeración seguía llamando lectura a la magnitud después de C04/C05. | Se identifica y en las tres filas, se narra su lectura y se conserva estado faltante C1/A2/día1/ciclo2 en lista separada. Script comprueba 3 valores, 1 faltante y 4 celdas esperadas. |

## Verificación

- Ejecutado `curso/.venv/bin/python -I curso/S1_fundamentos/calc/M00_ejemplos.py`. Resultado: 5 referencias, 4 indicaciones, 4 parejas, 1 faltante; errores −0,2/0,4/0,8/0,7, media 0,425 nmol/mol; falso pareo 50,8; conteos 16/8/4; ancho/largo 3 valores y 1 faltante conservado; Python/LibreOffice Calc coinciden con diferencia máxima 4,441e-16, tolerancia 1e-12.
- Contraste independiente Decimal e itertools en `verificar_M00_sol.py`, salida `verificar_M00_salida_sol.txt`: confirma errores, promedio, falso pareo y conteos sin reutilizar resultados del script auditado.
- PDF extraídos mediante `pdftotext -layout` a `referencias_00/`: iso17025.txt, en14625.txt, gum.txt. GUM B.2.19 líneas 2637–2647, C.2.19 líneas 2975–2987; ISO 7.5.1–2 líneas 984–995, 7.11.2 líneas 1303–1315, 7.11.6 línea 1340; EN §8.2 líneas 1018–1031 y nota de tabla 1 línea 1131. Los números de línea se refieren al texto extraído, no al PDF.
- Correspondencia curricular completa: B introducción/B1/B2; I I1/I2; A A1/A2. Tres marcadores exactos; narración acumulativa y cierre M01/M02; ninguna deducción nueva ni exclusión de §6 impartida.
- AX.1–AX.13 existen como encabezados en AX_libreto.md; M00 no los necesita. No se certifica el contenido de S4 ni se modifica.
- Revisiones Haiku y bitácora conservadas como antecedentes: sus afirmaciones previas sobre bibliografía no reemplazan esta comprobación. Resultado nuevo importante: C02 contenía referencia equivocada pese al dictamen anterior.
