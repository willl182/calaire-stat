# Revisión de las prácticas M11 (B, I, A)

Fecha: 2026-10-27. Revisor: Haiku 5.5. Alcance: `curso/S3_comparacion_decision/M11_libreto.md` (bloques de práctica y diff frente a HEAD), `calc/M11_practicas_luna.py`, `M11_practica_B_grafico.html` generado, `curso/logs/M11_practicas_luna.md`. No se editaron libretos ni scripts. No se auditaron referencias bibliográficas, salvo el cambio detectado en H-01, que se reporta por contradecir la instrucción de no tocar referencias.

## Verificación ejecutada

- `curso/.venv/bin/python curso/S3_comparacion_decision/calc/M11_practicas_luna.py` → rc=0. Hash SHA-1 del HTML antes y después: idéntico (`9692167b…`), salida determinista.
- B: MR = 0,4; 0,6; 0,3; 0,4; 1,3; 1,6; 0,3. Centro 0,16; MR medio 0,425; LIC −0,9705; LSC 1,2905; LSC MR 1,388475. Señales I = [6], MR = [7]. Coincide con el libreto.
- I: a = 0,089286; b = 0,00302381 nmol/mol/d; EE(b) = 0,0000922; IC95 de b [0,0027868; 0,0032609]; predicción media día 210 = 0,724286, EE = 0,012372, IC95 [0,692483; 0,756088]; sin día 90 → 0,722857. p de la pendiente = 4,96·10⁻⁷ (coincide con I2). Todo coincide con el libreto.
- A: EWMA 19 909/100 000 (EE 0,001263); CUSUM 9 177/100 000 (EE 0,000913); tras +1σ desde la ocasión 26, elegibles 89 347 y 96 059, detectadas 88 270 y 94 441, censuradas 1 077 y 1 618, detección condicional 0,987946 y 0,983156, demoras 8,3239 y 9,3056. Coinciden con el libreto (98,795 %, 98,316 %, 8,324, 9,306).
- Riesgo de exceder +0,20 nmol/mol: 30 d ≈ 0; **60 d = 0,000394362**; 90 d ≈ 1. Ver H-04.
- Contraste de colores del gráfico (fondo #fcfcfb): serie azul 4,3:1; límites naranja 3,1:1; centro gris 5,2:1; texto 7,7:1. Cumple 3:1 para elementos gráficos no textuales.

## Hallazgos

### H-01 — Alta — Cambio en una referencia bibliográfica (Montgomery 2013)

- **Ubicación:** `curso/S3_comparacion_decision/M11_libreto.md:282` (sección «Referencias del capítulo»); en HEAD era la línea 241 del mismo archivo.
- **Evidencia:** `git diff` muestra que la entrada «Montgomery 2013» pasó de «…Wiley, 2013 (año y editorial según la bibliografía de Crowder 2020; edición no verificada; no disponible en `docs/`).» a «…7.ª ed., Wiley, 2013. El índice editorial ubica CUSUM en cap. 9, §9.1, y EWMA en cap. 9, §9.2; se verificó el índice, no el texto íntegro…». El cambio no aparece en `M11_practicas_luna.md`, que declara no haber editado referencias. Además, la afirmación «se verificó el índice» no tiene evidencia en `docs/` ni en los logs revisados, y los numerales 9.1/9.2 no están verificados en el texto.
- **Riesgo:** incumple la instrucción de no cambiar referencias ni secciones de referencias (supervisor paralelo). Si el cambio es de otra pasada (p. ej., del supervisor de referencias), no es un defecto de la práctica; hay que confirmarlo antes de cerrar.
- **Corrección propuesta:** comprobar la autoría del cambio (`git log -p`/bitácora del supervisor de referencias). Si es de luna, restaurar la línea original de HEAD y dejar la nota de índice como pendiente en la bitácora para el supervisor de referencias. No tocar la sección desde esta revisión.

### H-02 — Alta — El gráfico B marca como señal dos puntos que no lo son

- **Ubicación:** `curso/S3_comparacion_decision/calc/M11_practicas_luna.py:106` (`shape = 'circle' if i not in (5, 6) else 'rect'`), salida en `curso/S3_comparacion_decision/M11_practica_B_grafico.html`.
- **Evidencia:** el código usa índices fijos 5 y 6 en ambos paneles. En el panel de individuales el índice 6 corresponde a la ocasión 7 (0,2), que no es señal; en el panel MR el índice 6 corresponde a la ocasión 8 (MR 0,3), que tampoco es señal. Los cuadrados del HTML están en x=613 (ocasión 7 individual) y x=703 (ocasión 8 MR). La leyenda dice «Cuadrados: puntos señalados», por lo que el lector recibe una señal falsa en una práctica cuyo objetivo es ubicar señales.
- **Failure scenario:** el operador lee la carta y concluye que la ocasión 7 también rebasa el límite, o que el rango 8 es una señal. Contradice la solución docente («dos señales: punto 6 y rango 6→7»).
- **Corrección propuesta:** marcar por datos y no por índice fijo, por ejemplo `shape = 'rect' if i in signal_idx else 'circle'`, pasando `signals - 1` (individuales) y `mr_signals - 2` (MR) a `write_chart`. Después regenerar el HTML y comprobar que solo hay un cuadrado en cada panel (ocasión 6 individual y ocasión 7 MR).

### H-03 — Media — Formato decimal con punto en el HTML

- **Ubicación:** `calc/M11_practicas_luna.py` en `write_chart`: etiquetas de eje (`{val:.2f}`), tabla (`{v:.4f}`, `{mr[i-2]:.4f}`) y títulos de tooltip.
- **Evidencia:** la salida contiene «-1.20», «0.4000», «0.0000». Las reglas de la sección exigen coma decimal.
- **Corrección propuesta:** formatear con coma, por ejemplo `f"{v:.4f}".replace(".", ",")`, y revisar también la salida de consola si se va a mostrar al operador. Los nombres de variables y código no cambian.

### H-04 — Media — Cifra de riesgo a 60 días no coincide con el cálculo

- **Ubicación:** `M11_libreto.md:260` (práctica A, solución: «aproximadamente 0,000395 (0,0395 %)»). La narración de A3 (`M11_libreto.md:238`) dice «0,00039, o 0,039 %». La bitácora de luna dice 0,000394362.
- **Evidencia:** el script da 0,0003943619 → 0,000394 (0,0394 %). El valor 0,000395 no coincide con el cálculo, y las dos cifras del libreto no coinciden entre sí.
- **Corrección propuesta:** usar «aproximadamente 0,000394 (0,0394 %)» en la práctica A y en A3, o un único formato.

### H-05 — Media — La comprobación de A no es independiente ni prueba recurrencias

- **Ubicación:** `M11_libreto.md:262` («…conteos con una implementación de referencia en `calc/M11_ejemplos.py`» y «…pruebas de recurrencia»); `calc/M11_practicas_luna.py:61–72` (`practica_a`).
- **Evidencia:** `practica_a` llama con `runpy` a `ewma_cusum_risk` de `M11_ejemplos.py`, la misma rutina que dice validar; no hay implementación alternativa. El script solo afirma conteos (19 909, 9 177, 88 270, 94 441), sin ninguna prueba de la recurrencia EWMA ni CUSUM. La bitácora lo describe como «rutina de referencia del propio capítulo», lo que contradice el texto del libreto.
- **Corrección propuesta:** o bien reescribir la frase como «reproduce la rutina de `M11_ejemplos.py` y fija sus conteos», o bien añadir una comprobación real, por ejemplo una serie corta de cinco valores fijos con EWMA y CUSUM calculados a mano y aserción sobre cada estado. Quitar «pruebas de recurrencia» si no se añade.

### H-06 — Media — El logro de I (distinguir predicción media de observación futura) no se evidencia

- **Ubicación:** `M11_libreto.md:166–176` (práctica I, solución y logro).
- **Evidencia:** la solución dice que la observación futura «añade la dispersión residual», pero no calcula ese intervalo. El logro pide distinguirlas. Calculado con los datos de la práctica: s_res = 0,014639 nmol/mol y EE(observación futura) = √(s² + EE_media²) = 0,019166; IC95 [0,675017; 0,773554] nmol/mol, frente al IC de la media [0,692483; 0,756088].
- **Corrección propuesta:** añadir a la solución la línea con s_res, el EE de la observación futura y su IC95, y una frase que los compare con el IC de la media. Añadir al script la línea de cálculo y una aserción sobre s_res.

### H-07 — Baja — La práctica B no pide evaluar «recalibrar»

- **Ubicación:** `M11_libreto.md:71–88` (tareas B). prop_e §M11 B enumera «investigar, repetir, retener o recalibrar».
- **Evidencia:** la tarea lista investigar, repetir, retener y escalar, pero no recalibrar. La solución menciona la recalibración solo como acción que requiere autorización.
- **Corrección propuesta:** añadir «o recalibrar» en la lista de la tarea, con la condición de autorización ya escrita en la solución.

### H-08 — Baja — Interpretación de β como distribución de la deriva sin declararla

- **Ubicación:** `M11_libreto.md:260`: «P(D(T)>0,20)=1−Φ((0,20/T−μ_β)/u_β)».
- **Evidencia:** el modelo trata la incertidumbre del estimador como si fuese la distribución de la deriva verdadera. Es un supuesto de tipo bayesiano (distribución de β), y la práctica no lo dice. La práctica sí declara el modelo como «docente»; falta solo señalar la interpretación.
- **Corrección propuesta:** añadir una frase en la solución: «aquí tratamos β como normal con la media y el error estándar dados; esa probabilidad es condicional a ese supuesto y no es la probabilidad frecuentista de un intervalo de confianza».

### H-09 — Baja — Validación visual del gráfico pendiente

- **Ubicación:** `curso/logs/M11_practicas_luna.md`, sección «Comprobaciones».
- **Evidencia:** la bitácora dice «pendiente inspección en navegador». Esta revisión no renderizó el HTML; sí comprobó la paleta (contraste en H-02 sección de verificación). Los marcadores incorrectos de H-02 no se detectaron por inspección visual.
- **Corrección propuesta:** tras corregir H-02 y H-03, abrir el HTML en el navegador o en un renderizador y confirmar leyenda, marcadores y tabla. Anotar el resultado en la bitácora.

## Lo que sí cumple

- Números de B, I y A coinciden con el script y con el libreto (salvo H-04).
- Rótulos de origen: las tres series se declaran simuladas y deterministas; no se atribuyen a CALAIRE.
- Alcance: B usa límites establecidos, no reestima límites ni tolerancias; I no declara conformidad y separa el análisis principal de la sensibilidad del día 90; A separa falsa alarma de detección y no convierte el intervalo en política.
- Escalamientos presentes en B, I y A.
- Los bloques de práctica sustituyen los tres marcadores; el resto del libreto no cambió salvo H-01.

## Resumen

Hay 9 hallazgos: 2 altos (H-01, H-02), 4 medios (H-03 a H-06) y 3 bajos (H-07 a H-09). Los altos deben corregirse antes de cerrar M11. H-01 requiere primero confirmar de quién es el cambio en la referencia.
