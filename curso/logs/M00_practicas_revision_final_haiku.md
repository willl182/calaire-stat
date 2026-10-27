# Revisión final — prácticas M00 restituidas (B, I, A)

Fecha: 2026-10-27. Revisor: claude-haiku-5-5. Alcance: `curso/S1_fundamentos/M00_libreto.md` (bloques de práctica B, I, A) y `curso/S1_fundamentos/calc/M00_practicas_luna.py`; cotejo con `curso/logs/reanudacion_AB_M00_revision_haiku.md` y `curso/logs/reanudacion_AB_M00_decisiones_luna.md`. No se editó libreto ni script. No se revisaron citas bibliográficas. La fase de ejercicios está autorizada; no se propone retirar prácticas.

Ejecución: `curso/.venv/bin/python -I curso/S1_fundamentos/calc/M00_practicas_luna.py` → rc=0. Salida coincide con las cifras del libreto.

## Verificación de H-05 a H-07

| Hallazgo | Estado | Evidencia |
|---|---|---|
| H-05 (cotejo R03 pre-resuelve la práctica B) | Resuelto en el enunciado | El MATERIAL de B solo da el extracto de adquisición «R03 — asociación de referencia registrada: P03» y declara que no hay cotejo docente. La frase literal de resolución aparece solo en la solución docente. Queda un residuo menor: F-H05b. |
| H-06 (A afirma unicidad, faltantes y unidades no reproducidos) | Parcialmente resuelto | Unicidad (`assert len(set(keys)) == 6`) y faltantes (`assert ... is not None`) sí se comprueban. La comprobación de unidades no: F-H06. |
| H-07 (campaña C1 ausente en el script del bloque I) | Resuelto | `calc/M00_practicas_luna.py` incluye `C1` en las tuplas y en la clave única; reproduce 8 claves, 7 completas, 1 faltante y las cuatro medias de `y` y `e`. |

## Conteos y números (verificados)

- B: antes de R03, 2 completas / 1 huérfana / 2 no emparejadas; errores −0,2; 0,4; 0,8 (P01–P03); P04 sin indicación. Coincide con libreto.
- B: suma de la rúbrica 2+2+2+2+2 = 10. I: 2+2+2+2+2 = 10. A: 2+2+2+2+2 = 10.
- I: medias de `y` 50,3 / 50,1 / 49,8 / 50,2 y de `e` 0,3 / 0,1 / −0,2 / 0,2 para A1-d1, A1-d2, A2-d1, A2-d2. Coinciden.
- I, Escena I1: 16 registros = 2 campañas × 2 analistas × 2 días × 2 ciclos; 8 por campaña, 8 por analista, 4 por campaña×analista, 2 por campaña×analista×día. Aritmética correcta.
- I, Escena I2: 3 valores no faltantes → 3 registros largos con indicación más 1 registro de faltante. Correcto.
- A: errores recalculados [−0,1; 0,2; 0,5; 0,8; 0,6; 1,0]; diferencias [0; 0; 0; 0; 0; 0,1]; máxima 0,1 en Q06 frente a tolerancia 10⁻⁶; sin acuerdo. Coincide.
- Escena B1: media de los cuatro errores disponibles = (−0,2+0,4+0,8+0,7)/4 = 0,425. Correcto. El valor espurio 100,8 − 50,0 = 50,8. Correcto.

## Hallazgos

### F-H06
- **Severidad:** menor
- **Ubicación:** `curso/S1_fundamentos/calc/M00_practicas_luna.py`, líneas 84–86 (bloque A).
- **Hallazgo:** la comprobación de unidades está hardcodeada: `unit_x = unit_y = "nmol/mol"` y después `assert unit_x == unit_y`. Es tautológica y no puede fallar. El enunciado de A pide verificar que las unidades declaradas sean compatibles, y la solución afirma que lo son. El script no comprueba nada sobre unidades reales.
- **Failure scenario:** si una de las columnas se cargara en ng/m³ o ppb con escala distinta, el script seguiría dando «unidades_compatibles= True» y el contrato parecería verificado.
- **Corrección propuesta:** declarar las unidades como metadatos de entrada (p. ej., un diccionario `unidades = {"x": "nmol/mol", "y": "nmol/mol"}`) y comprobar la igualdad entre ese diccionario y la unidad esperada, o reformular la salida como «unidades declaradas», sin llamarlo verificación. Alternativamente, aceptar explícitamente que es una declaración y ajustar la frase de la solución docente.

### F-H05b
- **Severidad:** baja
- **Ubicación:** `curso/S1_fundamentos/calc/M00_practicas_luna.py`, línea 13 (diccionario `cotejo_autorizado`) y línea 46 (`print`).
- **Hallazgo:** H-05 retiró el cotejo literal del enunciado, pero el script imprime en su salida «B cotejo R03: El registro de adquisición R03 vincula la indicación con la pareja de referencia P03; P04 no fue adquirido». Es la misma resolución que el libreto ya no debe dar al alumno. Si el script se entrega como material de práctica, la solución queda revelada.
- **Corrección propuesta:** si el script es solo de reproducción docente, dejarlo y anotarlo en su cabecera; si puede llegar a alumnos, eliminar la línea 46 o reemplazar el texto por una referencia («cotejo: ver solución docente»).

## Sin otros hallazgos

- Enunciados B, I y A: el alcance es M0 (`prop_e` §§3 y 5). No hay desbordes a M1 o M2 en las tareas ni en las rúbricas.
- Referencias `calc/M00_ejemplos.py` de la ficha y de las escenas existen en `curso/S1_fundamentos/calc/`.
- Los rangos de tolerancia son coherentes: 10⁻¹² en la escena A2 (comparación Python/Calc) y 10⁻⁶ en la práctica A (predeclarada). Están etiquetados distintos.

## Nota sobre el documento de decisiones

`reanudacion_AB_M00_decisiones_luna.md` marca H-06 como «Aplicado» y dice que el script «comprueba unicidad, faltantes, tipo numérico, compatibilidad de unidades». La parte de unidades no está comprobada (F-H06). La decisión debería actualizarse a «aplicado parcialmente».

## Veredicto

Con F-H06 corregido o explicitado, las tres prácticas M00 cumplen la revisión. F-H05b es opcional según el destino del script. No hay defectos de conteo ni de cifras.
