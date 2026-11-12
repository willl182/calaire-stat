# Revisión de cierre — prácticas M11 (B, I, A)

Fecha: 2026-10-27. Revisor: Haiku 5.5. Alcance: sección de prácticas de `curso/S3_comparacion_decision/M11_libreto.md`, `calc/M11_practicas_luna.py`, `calc/M11_ejemplos.py` (dependencia de A), `M11_practica_B_grafico.html` y `curso/logs/M11_practicas_luna.md`. No se editaron libretos ni scripts. No se hicieron commits. Referencias bibliográficas no revisadas salvo lo indicado en H-02.

## Verificación ejecutada

- `curso/.venv/bin/python -I curso/S3_comparacion_decision/calc/M11_practicas_luna.py` se ejecutó completo: todas las impresiones de B, I y A aparecen y las aserciones previas a cada impresión pasaron. (El código de salida se leyó a través de una tubería con `head`; no se capturó de forma aislada, pero la última impresión del script se produjo, lo que implica que no hubo excepción.)
- Recalculado a mano: rangos móviles de B (0,4; 0,6; 0,3; 0,4; 1,3; 1,6; 0,3), centro 0,16, MR medio 0,425, límites ±2,66·0,425, LSC MR 3,267·0,425 = 1,388475; señales I=[6], MR=[7]. Coincide con enunciado y solución.
- Recalculado: pendiente I 0,00302381 (con días 0–180 y sin el día 90), EE 0,00009221, t(0,975;5)=2,5706, IC95 pendiente, predicción día 210 = 0,724286, IP95 de observación futura. Coincide con la solución.
- Verificado: el día 90 es la media de los días (90), así que retirarlo no cambia la pendiente; ver H-04.
- Riesgo de exceder +0,20 nmol/mol: `norm.sf((0,20/t − 0,00302381)/0,00009221)` da ≈0 (30 d), 0,000394 (60 d), ≈1 (90 d). Coincide con A y con la fórmula de la pizarra.
- Recurrencias de A (Z_t = 1−0,8^t, límites 0,5400 y 0,6915 en t=1,2, C⁺=0,5t, primera señal en la ocasión 11 en ambos métodos): coinciden con la narración.
- Conteos y detección de A (19 909; 9 177; 88 270/89 347; 94 441/96 059; censuras 1 077 y 1 618; demoras 8,324 y 9,306 con la ocasión 26 contada como 1): coinciden entre script, solución y narración. La definición de demora en `M11_ejemplos.py` (`first − 24`) es consistente con "ocasión 26 = demora 1".
- Cifras NISTIR de I1 (media 0,000031; MR medio 0,000498889; límites) recalculadas: coinciden.

Coherencia numérica enunciado–solución–script: sin discrepancias de cifras en B, I ni A.

## Verificación de decisiones registradas en `curso/logs/M11_practicas_luna.md`

| Decisión | Presente en el libreto | Comentario |
|---|---|---|
| H-02 índices de señal del gráfico | Script | Correcto: I=6 y MR=7 como cuadrados. |
| H-03 coma decimal | Script (`fmt`) | Presente. |
| H-04 cifra 0,000394362 | Sí, A solución | La referencia a "escena A3" es errónea (ver H-03). |
| H-05 no verificación independiente | Sí, A comprobaciones (línea ~262) | Presente. |
| H-06 predicción individual e IP95 | Sí, I solución | Presente. |
| H-07 recalibrar condicionada | Sí, B tareas | Presente. |
| H-08 β normal condicional | Sí, A solución | Presente. |
| H-09 renderizado y tabindex | Script (tabindex) | El PNG de `/tmp` citado no existe ahora; no se pudo repetir la inspección visual (ver H-05). |
| "únicamente los tres marcadores" modificados | No verificable contra HEAD | Ver H-02. |

## Hallazgos

**H-01 — Gráfico: el eje de ocasiones del panel MR no coincide con el de individuales** (severidad media)
- Ubicación: `curso/S3_comparacion_decision/calc/M11_practicas_luna.py:134` (`coords` usa `len(vals)-1` para cada panel) y `:146–147` (etiquetas).
- Problema: el panel I tiene 8 puntos (espaciado 630/7 = 90 px) y el panel MR 7 puntos (espaciado 630/6 = 105 px). Verificado en el HTML generado: la ocasión 2 de I está en x=168 y la ocasión 2 de MR en x=78; la ocasión 7 está en x=618 (I) y x=603 (MR). El lector no puede comparar verticalmente la señal del punto 6 con la señal MR del rango que termina en 7, que es justo lo que pide la práctica B.
- Escenario: el estudiante alinea la columna del punto 7 en ambos paneles y ve el marcador MR desplazado a la izquierda; el "salto" queda visualmente en otra ocasión.
- Corrección sugerida (no aplicada): colocar el MR de la ocasión k+1 en `left + k*width/7`, igual que I.

**H-02 — Trazabilidad: el diff del libreto frente a HEAD toca referencias y prosa fuera de los tres marcadores** (severidad media)
- Ubicación: `curso/S3_comparacion_decision/M11_libreto.md`, sección "Referencias del capítulo" (entradas Hahs-Vaughn y Montgomery 2013), y prosa de Escena A1 y A2.
- Problema: `git diff` contra HEAD muestra cambios en la entrada de Hahs-Vaughn (añadidos edición, "portada/créditos") y en la de Montgomery (texto "soporte no verificable", añadido de año y "El año 2013 aparece..."). El registro dice "ninguna referencia ... editada" y "únicamente los tres marcadores". Las instrucciones del encargo prohíben tocar referencias. Parte de estos cambios pueden venir de otro trabajo en curso (el estado inicial ya tenía el libreto modificado), pero el registro no lo distingue.
- Acción sugerida: que el supervisor de referencias confirme la autoría de esos cambios o los revierta; corregir la frase de alcance de la bitácora para que no afirme algo que el diff no demuestra.

**H-03 — Bitácora: referencia a "escena A3" inexistente** (severidad baja)
- Ubicación: `curso/logs/M11_practicas_luna.md`, fila H-04.
- Problema: el libreto solo tiene Escena A1 y A2. La cifra 0,00039 (0,039 %) está en el párrafo final de la Escena A2 (`M11_libreto.md` línea ~238).
- Acción sugerida: cambiar "escena A3" por "Escena A2".

**H-04 — Práctica I: la sensibilidad sin el día 90 no mueve la pendiente, y el texto no lo explica** (severidad baja)
- Ubicación: `M11_libreto.md`, práctica I, solución docente (párrafo "Al ajustar los seis puntos distintos del día 90...").
- Problema: el día 90 es exactamente la media de las fechas (0, 30, …, 180 tienen media 90), así que su término `(t − t̄)` es cero y su retirada deja la pendiente igual (0,00302381 en ambos casos; verificado en el script). Solo cambia el intercepto y, con él, la predicción (0,724286 → 0,722857). El lector puede concluir que la pendiente es "robusta" en general.
- Acción sugerida: añadir una frase: "la pendiente no cambia porque el día 90 es el centro de las fechas; cambian el intercepto y la predicción."

**H-05 — Verificación visual de H-09 no reproducible con el registro** (severidad baja)
- Ubicación: `curso/logs/M11_practicas_luna.md`, decisión H-09.
- Problema: cita `/tmp/M11_practica_B.png`, que ya no existe (`ls` falla). La afirmación "sin colisión ni recorte" no se puede repetir aquí. No se renderizó el HTML en esta revisión.
- Acción sugerida: conservar la imagen en el repositorio de trabajo o indicar que la inspección visual quedó sin evidencia. Esto no cambia las cifras del libreto.

## Sin hallazgos en
- Cifras de B, I y A frente al script y la solución; fórmulas de pizarra (predicción, riesgo, EWMA, CUSUM).
- Consistencia de marcadores: ya no queda ningún `[PRÁCTICA — fase de ejercicios]` en M11.
- Aplicación a ozono/SRP: los datos se declaran simulados o publicados ajenos al Level 2; el techo de 0,20 nmol/mol se declara como condición inventada.
