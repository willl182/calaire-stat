# Hito A — cotejo visual de «<± 1 ppb» en SRP QAPP

Fecha: 2026-10-27. Alcance: hallazgo del supervisor S-01, grafía y significado en M10. No es un hallazgo Haiku.

## Evidencia documental

Fuente: `docs/srp_qapp.pdf`, US EPA, *Quality Assurance Project Plan for the Standard Reference Photometer Program*, Element 6.0, Rev. 1, fecha 02/17.

- La extracción de texto reproduce «intercept <+ 1 ppb» en el criterio y en la Tabla 7-1; la extracción omite el rasgo inferior del signo.
- El supervisor revisó la página PDF 23 (Element 7, página impresa 3/4) a 400 dpi. La ampliación indicada en `curso/logs/pendientes_revision_supervisor.md` está disponible en `/tmp/calaire_qapp_supervisor_signo.png`. Se observa un signo más con raya debajo: la grafía visible es «±», por tanto «<± 1 ppb», no «<+ 1 ppb».
- La grafía observada corrige la transcripción tipográfica. No autoriza a interpretar el operador, transformar el criterio en `|intercepto| < 1`, ni establecer otra desigualdad o regla operativa.
- El contexto es la reverificación SRP #7–SRP regional: al menos tres ciclos, al menos doce concentraciones por ciclo incluidos ceros inicial y final, y diez lecturas promediadas por concentración [SRP-QAPP, §6.2.1 y Tabla 7-1].

## Cotejo de H-01 y H-02, y acción limitada

Se cotejaron las páginas PDF 18 y 23, sin derivar una interpretación normativa:

- Página 18, §6.2.1: la extracción de texto dice «the intercept must be ± 1ppb», sin «<». Para el diseño, indica un mínimo de 12 puntos de concentración, incluidos cero inicial y final; además especifica tres ciclos y diez lecturas promediadas por concentración.
- Página 23, Tabla 7-1: la extracción textual del intercepto aparece como «<+ 1 ppb»; la inspección visual documentada en la revisión muestra «<± 1 ppb». La descripción del ciclo dice «3 evaluation cycles of 10 concentrations and zero».

Por tanto, el texto del criterio de intercepto y el número de concentraciones difieren entre §6.2.1 y Tabla 7-1. Se reportan ambos pasajes literalmente, sin decidir cuál prevalece ni inventar una operación o interpretación. En `curso/S3_comparacion_decision/M10_libreto.md`, párrafo QAPP de I2, se anotaron las divergencias y se mantuvo la confirmación autorizada antes del uso operativo. No se alteraron bibliografía ni citas.

## Conclusión y decisión S-01

S-01 aplicado. La afirmación anterior de que la inspección visual confirmaba «<+» se corrige: era una extracción que no reflejaba la raya inferior visible. El significado del criterio permanece sin resolver; no se infiere valor absoluto ni desigualdad autorizada.