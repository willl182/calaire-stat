# Revisión Haiku 5.5 — reanudación de pendientes 2–4 (A, B, M00)

Fecha: 2026-10-27. Revisor: claude-haiku-5-5 (esta sesión). Alcance: `curso/guia_libreto.md`, `curso/revision_final.md`, `curso/logs/hitos_pendientes.md`, `curso/logs/A_qapp_luna.md`, `curso/logs/B_RR_luna.md`, `curso/logs/M00_practicas_luna.md`, bloques de práctica de `curso/S1_fundamentos/M00_libreto.md`, `curso/S1_fundamentos/calc/M00_practicas_luna.py`, párrafo QAPP de `curso/S3_comparacion_decision/M10_libreto.md`. No se editaron libretos, scripts ni bibliografía. No se revisaron citas bibliográficas.

Comprobaciones ejecutadas:

- `curso/.venv/bin/python -I curso/S1_fundamentos/calc/M00_practicas_luna.py` → rc=0. Reproduce B (`e = −0,2; 0,4; 0,8`; antes 2/1/2; después 3 completas, P04 faltante, 0 huérfanas), I (7 completas, 1 faltante; medias de `y` 50,3 / 50,1 / 49,8 / 50,2; medias de `e` 0,3 / 0,1 / −0,2 / 0,2) y A (máximo desacuerdo 0,1 > 1e-6; sin acuerdo).
- `curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M06_RR_CALAIRE.py` → rc=0. Lee `docs/Resultados R&r_2022 2023 (1).xlsx` (variable `BOOK`, líneas 17 y 48); no genera datos. Salida: F máx. analista 1,238163 (45→455 ppb, nivel 315); interacciones que superan Bonferroni (α/10, F = 6,354689): niveles 135 y 405. Coincide con `B_RR_luna.md`.
- `docs/srp_qapp.pdf`: página 23 (Element 7, Tabla 7-1) renderizada a 300 dpi y a 400 dpi (imagen del supervisor): la intersección muestra «<±» (raya inferior del signo). La pendiente de la misma tabla también se ve como «±». Confirmado: la extracción «<+» es un artefacto de texto.
- `docs/srp_qapp.pdf`: página 18 (Element 6.0, §6.2.1) renderizada a 300 dpi: el texto dice «the intercept must be ± 1ppb» (sin «<»). Esto no aparece en el párrafo M10 (véase H-01).
- `docs/srp_qapp.pdf`, §6.2.1 en texto: «averaging 10 points per concentration with a minimum of 12 concentration points, which includes a zero at the start and at the end»; «3 cycles»; «average of all the cycles» (coincide con M10). Tabla 7-1: «3 evaluation cycles of 10 concentrations and zero» (véase H-02).

---

## A — Hito QAPP (grafía del criterio de intercepto en M10)

Veredicto: la corrección tipográfica de luna es correcta (confirmada en la página renderizada). Hay dos hallazgos de contenido en el párrafo M10 que no quedan reflejados.

### H-01
- **Severidad:** mayor
- **Ubicación:** `curso/S3_comparacion_decision/M10_libreto.md`, párrafo de la reverificación SRP #7–SRP regional (línea 85).
- **Hallazgo:** el párrafo cita «[SRP-QAPP, §6.2.1 y Tabla 7-1]» y presenta el criterio de intercepto solo como «extracción «<+» / grafía visible «<±»», atribuyendo el «<» a la tabla. §6.2.1 de la misma QAPP (página 18, Element 6.0, página impresa 2/4) escribe «the intercept must be ± 1ppb», sin «<». Por tanto, el texto normativo y la tabla difieren en la presencia del «<», y el párrafo no lo dice. Esto importa para la decisión que el párrafo deja pendiente («confirmar la interpretación autorizada»): la discrepancia es entre dos partes del mismo documento y es precisamente lo que habría que confirmar.
- **Corrección propuesta:** añadir una frase tras la grafía: «El §6.2.1 del mismo documento enuncia el intercepto como «± 1 ppb», sin el «<» de la tabla; la diferencia entre ambos pasajes es parte de lo que debe confirmar el responsable antes de un uso operativo.» No convertir en desigualdad. Mantener el escalamiento.

### H-02
- **Severidad:** menor
- **Ubicación:** mismo párrafo, frase «al menos doce concentraciones por ciclo incluidos los ceros inicial y final» (cita «[SRP-QAPP, §6.2.1 y Tabla 7-1]»).
- **Hallazgo:** §6.2.1 dice «a minimum of 12 concentration points, which includes a zero at the start and at the end». Tabla 7-1 dice «3 evaluation cycles of 10 concentrations and zero». Son dos cifras distintas para el mismo procedimiento en el mismo documento; el párrafo cita ambas fuentes pero solo reporta la de §6.2.1 sin señalar la discrepancia.
- **Corrección propuesta:** indicar «§6.2.1 fija un mínimo de doce concentraciones (incluidos ceros); la Tabla 7-1 dice diez concentraciones más cero. El párrafo sigue §6.2.1; la discrepancia se anota para confirmación.»

### A — sin otros hallazgos
- `A_qapp_luna.md`: la afirmación «la grafía visible es «<±»» coincide con la página renderizada. La corrección de la afirmación previa del supervisor/luna está registrada correctamente.
- Ninguna cifra de pendiente (1,00 ± 0,01), tres ciclos o promedio de diez lecturas está mal transcrita.

---

## B — Suficiencia de datos históricos del R&R (S2)

Veredicto: la conclusión de luna es correcta: los datos existentes no permiten validar históricamente el R&R. Los cálculos son exploratorios y están bien etiquetados como tales en `M06_RR_CALAIRE.py` (cabecera: «EXPLORATORIO CONDICIONAL»). La lista de datos pedidos (7 puntos en `B_RR_luna.md`) es coherente con el diseño descrito. Hallazgos:

### H-03
- **Severidad:** mayor
- **Ubicación:** `curso/logs/B_RR_luna.md`, sección «Método y resultados exploratorios»; `curso/logs/hitos_pendientes.md`, Hito 2.
- **Hallazgo:** el informe resume el resultado como «F máximo de analista 1,238163; interacciones que exceden el umbral: niveles 135 y 405», pero no informa que, sin corrección, el script marca también las interacciones 360 y 455 (`significant_interactions= [135, 360, 405, 455]`). Con Bonferroni quedan 135 y 405. Que la lista se reduzca tras corrección está bien; omitir la lista sin corregir puede llevar a un lector a pensar que solo dos niveles tienen interacción significativa a α = 0,05. Además, el umbral Bonferroni (`Fcrit_interaccion_Bonferroni = 6,354689`) no aparece en el informe.
- **Corrección propuesta:** añadir a `B_RR_luna.md` una línea: «Sin corrección, la interacción supera F crítico 3,3158 en los niveles 135, 360, 405 y 455; con Bonferroni (α/10, F = 6,354689), en 135 y 405. Todos son exploratorios.»

### H-04
- **Severidad:** menor
- **Ubicación:** `curso/logs/B_RR_luna.md`, sección «Datos de casos y faltantes».
- **Hallazgo:** el informe describe `datos_caso_C1.csv` como «seis resúmenes diarios de CALAIRE de febrero de 2023». No lo he comprobado en esta revisión y no debería afirmarse como hecho sin abrir el archivo. Si la afirmación es correcta, debería citarse el archivo como fuente. No altera la conclusión.
- **Corrección propuesta:** citar `casos_taller/caso_C_historial_level2.md` como fuente de esa descripción, o verificar `datos_caso_C1.csv` antes de mantener la cifra «seis».

### B — sin otros hallazgos
- No se confunden cálculos exploratorios con validación: el informe lo dice explícitamente en tres lugares (script, log, Hito 2).
- El libro `docs/Resultados R&r_2022 2023 (1).xlsx` tiene 36 valores numéricos por hoja de nivel (B6:C23) y no contiene errores firmados (confirmado por la lectura de solo lectura del informe; verificado: `curso/.venv/bin/python -I` lee `BOOK` sin escribir). Coincide con el diagnóstico.
- El libro de calibración `docs/F-PSMT-01 Certificado…xlsm` (hojas `Dia0`–`Dia6`, `BD_DIAS`, `Fotometro`) no fue abierto en detalle en esta revisión; el informe lo descarta para validación histórica del R&R. Esa exclusión es razonable, pero queda sin verificación por contenido.

---

## M00 — prácticas B, I y A

Veredicto: las tres prácticas son reproducibles con `M00_practicas_luna.py` (rc=0) y las cifras del libreto coinciden con la salida. Hay un hallazgo mayor de diseño pedagógico y dos menores de reproducibilidad.

### H-05
- **Severidad:** mayor
- **Ubicación:** `curso/S1_fundamentos/M00_libreto.md`, práctica B, bloque «[MATERIAL]» y «Cotejo docente autorizado R03» (líneas 88–118 aprox.).
- **Hallazgo:** la práctica pide «detectar la pareja desplazada usando el cotejo docente autorizado R03», pero el propio MATERIAL transcribe el cotejo literal que resuelve la discrepancia: «La indicación transcrita como P99 pertenece a P03». La tarea deja de ser detectar y pasa a copiar. Esto contradice prop_e (§ M00, práctica de «detectar una pareja desplazada y un faltante, y documentar la corrección sin borrar el original»): el alumno debe poder inferir la pareja con evidencia del propio material. La guía de estilo también pide que las prácticas tengan evidencias evaluables; con el cotejo dentro del enunciado, la evidencia está pre-resuelta.
- **Corrección propuesta:** retirar la frase literal del cotejo del MATERIAL. Dejar en el enunciado un registro de adquisición que permita la inferencia (p. ej., la hoja de adquisición R03 con la fecha/orden) y mover el texto literal del cotejo a la solución docente. El script no cambia si el cálculo se mantiene igual; solo cambia la presentación del enunciado.

### H-06
- **Severidad:** menor
- **Ubicación:** `curso/S1_fundamentos/calc/M00_practicas_luna.py`, bloque A (líneas 72–82).
- **Hallazgo:** la solución docente de A afirma: «Las seis claves Q01–Q06 son únicas, no hay faltantes y `x` e `y` comparten unidad». El script no comprueba unicidad de claves, ausencia de faltantes ni unidad; sólo verifica residuos. Las afirmaciones de la solución quedan sin reproducir.
- **Corrección propuesta:** añadir al bloque A `assert len({q for q,*_ in rows}) == 6` (o equivalente con las claves de la tabla) y, si se mantienen los datos, comprobar que ninguna celda de `y` es None. Así la solución es verificable como pide la sección «Solución docente verificable».

### H-07
- **Severidad:** menor
- **Ubicación:** `curso/S1_fundamentos/calc/M00_practicas_luna.py`, bloque I (líneas 51–70); libreto, práctica I, tabla de la campaña.
- **Hallazgo:** el libreto describe la campaña con la columna «Campaña = C1» y pide «verificar las claves campaña–analista–día–ciclo». El script omite la campaña (las claves son `(a, d, c)`), así que la verificación pedida en el enunciado no se reproduce completa. Es un detalle, pero la tarea sí la menciona.
- **Corrección propuesta:** incluir `"C1"` en las tuplas `data` y en la clave de unicidad, o quitar la campaña del enunciado si no aporta.

### M00 — sin otros hallazgos
- Las cifras de B, I y A del libreto coinciden con la salida del script (verificado línea a línea: `e` B = −0,2; 0,4; 0,8; I medias como arriba; A residuo 0,1 en Q06).
- La solución de B (`P01/P01 y P02/P02` completas antes del cotejo; dos referencias sin emparejar P03 y P04; una huérfana P99) coincide con el script.
- La tolerancia predeclarada de A (1e-6) y el resultado «sin acuerdo» son coherentes.

---

## Suficiencia de datos históricos (resumen transversal)

- **Cálculo exploratorio ≠ validación.** Los tres documentos (`M06_RR_CALAIRE.py`, `B_RR_luna.md`, `hitos_pendientes.md`) lo separan correctamente. Ninguna de las conclusiones afirma reproducibilidad histórica validada.
- **Datos suficientes para explorar, no para validar.** El libro del R&R contiene 360 valores absolutos (no firmados) en 10 hojas de nivel y una hoja `BASE DE DATOS` que se describe como «VALORES ABSOLUTOS». No hay errores con signo, ni trazabilidad de bloques a campañas, ni réplicas intradía. La lista de siete requisitos de `B_RR_luna.md` está completa para desbloquear la validación.
- Esta conclusión no depende de los hallazgos H-03 y H-04; estos son ajustes de redacción del informe.

---

## Resumen de hallazgos

| Id | Sección | Severidad | Ubicación | Resumen |
|---|---|---|---|---|
| H-01 | A | mayor | M10, párrafo QAPP (l. 85) | §6.2.1 enuncia «± 1ppb» sin «<»; el párrafo no lo señala |
| H-02 | A | menor | M10, párrafo QAPP (l. 85) | §6.2.1 (12 concentraciones) y Tabla 7-1 (10 + cero) difieren; no se anota |
| H-03 | B | mayor | `B_RR_luna.md`, método | Lista de interacciones sin corregir (135, 360, 405, 455) omitida; umbral Bonferroni no informado |
| H-04 | B | menor | `B_RR_luna.md`, casos | Cifra «seis resúmenes de febrero 2023» no verificada en `datos_caso_C1.csv` |
| H-05 | M00 | mayor | `M00_libreto.md`, práctica B, MATERIAL | El cotejo R03 literal resuelve la práctica; el enunciado deja de ser de detección |
| H-06 | M00 | menor | `M00_practicas_luna.py`, bloque A | La solución afirma unicidad, ausencia de faltantes y unidad que el script no comprueba |
| H-07 | M00 | menor | `M00_practicas_luna.py`, bloque I; libreto I | Campaña C1 en el enunciado no está en el script ni en la clave de unicidad |

Secciones sin hallazgos: A — ninguno de grafía (la corrección S-01 es correcta); B — ninguno sobre la conclusión de insuficiencia; M00 — ninguno sobre cifras.

## Pendientes no cubiertos

- No se revisaron citas bibliográficas (fuera de alcance).
- No se abrieron en detalle `docs/F-PSMT-01…xlsm` ni `casos_taller/datos_caso_C1.csv` (H-04).
- La confirmación del significado operativo de «<±» sigue siendo una decisión del responsable, no de esta revisión.
