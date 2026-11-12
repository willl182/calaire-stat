# Cambios de ronda 2

- `M02_libreto.md:9`: la ficha de B6 anuncia ahora la regla IQR; refleja el contenido numérico del capítulo (observación 5.5).
- `M02_libreto.md:96`: retirada la introducción prematura de mediana/MAD en B6; se reserva MAD para I, evitando prerrequisitos fuera del nivel y manteniendo autocontenida la regla IQR (F04).
- `M02_libreto.md:174`: la práctica I pide leer e interpretar la recta ya ajustada y comunicar sus coeficientes, sin exigir estimarlos; armoniza la tarea con la recta suministrada en :160 y la solución en :176 (F03).
- `M02_libreto.md:239`: añadida la referencia completa a Otto §2.2, con la ubicación bibliográfica de M04 (F06).
- `calc/M02_examples.py:94`: el valor de sensibilidad se corrigió de +1,8 a +1,6 nmol/mol, como en el libreto y en la práctica. Ejecutado con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I calc/M02_examples.py`; confirma media firmada 0,177778 (redondea 0,178), media absoluta 0,533333 (0,533) y desviación estándar muestral 0,670406 (0,670).
- `M05_libreto.md:64,70`: los seis días se declaran explícitamente supuesto didáctico del conteo, no dato atribuido a la nota del certificado; la práctica y el relato quedan consistentes (discrepancia heredada de sección 6).
- `M06_libreto.md:172`: se explicita nivel nominal 94 nmol/mol para las filas 31–38 de BD_DIAS. Verificado en `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm`: columna C, filas 31–38 contiene indicaciones alrededor de 94, no 90.
- `calc/M06_practica_I_grafico.py:3,39,94`: corregido el rótulo de 90 a 94 nmol/mol en comentario, título accesible y texto; generador ejecutado con Python indicado y HTML regenerado.
