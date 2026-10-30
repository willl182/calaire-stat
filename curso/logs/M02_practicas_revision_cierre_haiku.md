# Revisión de cierre — prácticas M02 (B, I, A) y narración M06 pendiente

Revisor: Haiku 5.5. Fecha: 2026-10-28. Alcance: `curso/S1_fundamentos/M02_libreto.md` (bloques `[PRÁCTICA]` B, I, A), `curso/S1_fundamentos/calc/M02_practicas_luna.py`, `curso/logs/M02_practicas_luna.md`, y, para M06, las líneas ~152, ~219 y ~237 de `curso/S2_modelos_calibracion/M06_libreto.md`. Hallazgos previos: `curso/logs/M02_practicas_revision_haiku.md`. No se editó ningún libreto ni script; no se tocaron referencias ni citas; no se hizo ningún commit.

## Verificación ejecutada

- **Script M02:** copiado a un directorio temporal (`/tmp/m02cierre.uGrc/calc/`) y ejecutado con `curso/.venv/bin/python -I`. Código de salida 0. Los tres HTML generados son idénticos byte a byte a los del curso. La salida coincide con `curso/logs/M02_practicas_luna_ejecucion.txt`.
- **Cifras del libreto frente a la ejecución (B, I, A):** todas coinciden. B: medias, medianas, s(y)=0,28123, s(e)=0,14460, cuartiles lineales, cajas por día, histograma 1; 2; 3; 3; 2; 1, media del cero 0 frente a 0,06 truncado. I: medias diarias 0,50; 0,58; 0,66; MAD 0,20 y 0,06; s dentro de celda 0,0516398 (las 15 celdas); s agrupada 0,23664; intercepto 0,100 y pendiente 0,002; predicciones 0,26 a 0,90; residuos ±0,14. A: s 0,08165 y 0,43425; MAD 0,05, 0,40; media de centros 0,025 frente a media de seis lecturas 0,150; con +1,6: 0,17778; 0,53333; mediana 0,30; MAD 0,60; s 0,67041.
- **Enunciados I y A:** coinciden con el script (60 parejas en I; grupos ±0,3…0,5 en A).
- **Paleta:** la tercera serie es `#199e70`; contraste calculado sobre `#fcfcfb` = 3,32:1 (≥3:1). Se resuelve H-05 de la revisión previa. El validador de la habilidad no se volvió a ejecutar.
- **Escena I1:** ahora describe las doce observaciones de B (cuatro por día), como pedía H-07 previo.
- **M06, línea ~237:** la atribución al script es correcta. `M06_ejemplos.py` (líneas 109–121) hace la optimización REML acotada del cociente λ; la salida (`M06_ejemplos_final_sol.out`, líneas 28–29) da σ²=0,014824, u_trunc=0,037268 y u_REML=0,035148, lo que coincide con las cifras del libreto.
- **M06, línea ~152:** el valor crítico 0,628724 se reproduce (`M06_ejemplos.py` línea 146, salida línea 58). Verificado además que P(una varianza supera el umbral) ≈ 0,05 con el criterio beta de Bonferroni.
- **M06, línea ~219:** el valor crítico F(2;30) al 0,5 % es 6,35, correcto. **No verificados:** las afirmaciones «135 y 405 lo superan; 360 y 455 quedan por debajo», que dependen de `calc/M06_RR_CALAIRE.py`, no ejecutado en esta revisión.

## Estado de los hallazgos previos (H-01 a H-11)

| Previo | Estado | Comentario |
|---|---|---|
| H-01 histograma y cajas | Resuelto | Presentes en el script, en el HTML y en la solución docente. |
| H-02 tres paneles en I | Resuelto | Escalas comunes verificadas en el código. |
| H-03 recta y medias temporales | Resuelto | Recta y predicciones en cada panel; panel temporal presente. |
| H-04 coma decimal | Resuelto | No se encontraron números con punto en texto visible de los HTML. |
| H-05 paleta | Resuelto | 3,32:1 (ver verificación). |
| H-06 escena A1 vs práctica A | **Sigue abierto** | Rechazado en la ronda anterior; ver H-04 de este informe. |
| H-07 escena I1 con datos de B | Resuelto | |
| H-08 leyendas | Resuelto | «Día 1…3» y «Grupo 1/2». |
| H-09 bitácora | Parcial | Ver H-03 de este informe. |
| H-10 función con dependencia global | Parcial | Ver H-06 de este informe. |
| H-11 contexto ozono/SRP | **No resuelto** | Ver H-01 de este informe. |

## Hallazgos

### H-01 — H-11 declarado resuelto y no lo está (ozono/SRP en B)
- **Severidad:** media.
- **Ubicación:** `curso/S1_fundamentos/M02_libreto.md`, enunciado de B (línea ~98: «doce parejas de referencia e indicación de un nivel nominal medido en tres días»); `curso/logs/M02_practicas_luna.md`, tabla de correcciones, fila H-11 («Enunciado B identifica explícitamente el nivel de ozono del SRP»).
- **Problema:** el bloque B no contiene ni «ozono» ni «SRP» (verificado: cero coincidencias en las líneas 96–119). La bitácora afirma lo contrario. Sí están bien las unidades nmol/mol y el rótulo «simulado», y en A se precisó «estudio tipo R&R del Level 2».
- **Corrección propuesta:** en el enunciado de B, sustituir «un nivel nominal» por «un nivel nominal del ozono medido con el SRP (nmol/mol)», o bien corregir la fila H-11 de la bitácora si se decide no aplicarlo.

### H-02 — Fondo del gráfico A con atributo `fill` literal inválido
- **Severidad:** alta (si se confirma en navegador; no se renderizó aquí).
- **Ubicación:** `curso/S1_fundamentos/calc/M02_practicas_luna.py`, función `save_a_chart()`: la lista `svg=[...]` incluye `'<rect width="100%" height="100%" fill="{surface}"/>'` sin prefijo `f`. Confirmado: `M02_practica_A_grafico.html` contiene el texto literal `fill="{surface}"`; en I y B no aparece.
- **Problema:** `{surface}` no es un color válido. El atributo se ignora y el rectángulo de fondo toma el relleno por defecto (negro). Eso oculta o hace ilegibles las marcas y las etiquetas de tinta oscura del gráfico A. La bitácora dice que todas las figuras tienen «colores… leyenda y tabla», pero esa comprobación no detecta el defecto.
- **Corrección propuesta:** añadir la `f` al literal: `f'<rect width="100%" height="100%" fill="{surface}"/>'`. Reejecutar el script y abrir el HTML en navegador para confirmar el fondo claro (y en modo oscuro). Actualizar la bitácora.

### H-03 — La bitácora dice que los gráficos no se regeneraron
- **Severidad:** baja.
- **Ubicación:** `curso/logs/M02_practicas_luna.md`, sección «Reejecución final»: «Los gráficos no se regeneraron y se conservaron intactos».
- **Problema:** el script escribe los tres HTML cada vez que se ejecuta. El contenido resultante es idéntico (verificado), pero la frase es falsa como descripción del proceso.
- **Corrección propuesta:** decir «se regeneraron; el contenido coincide byte a byte con la versión anterior». Tras aplicar H-02, la afirmación cambia y debe registrarse el nuevo hash.

### H-04 — Escena A1 y práctica A siguen con cifras distintas para el mismo ejemplo (H-06 previo)
- **Severidad:** media.
- **Ubicación:** `curso/S1_fundamentos/M02_libreto.md`, escena A1 (párrafos «Veamos esa diferencia…» y «Ahora añadamos un valor influyente… +1,8»; media firmada 0 a 0,2; media absoluta 0,400 a 0,556; s 0,434 a 0,725) frente al bloque «[PRÁCTICA] A» (punto +1,6; media firmada 0,17778; s 0,67041).
- **Problema:** dos ejemplos del mismo capítulo con el mismo punto influyente y cifras diferentes. El alumno puede comparar valores incompatibles. La escena también usa dos grupos con reglas distintas a la práctica.
- **Corrección propuesta:** alinear la escena con los valores verificados de la práctica (punto +1,6; resúmenes del script), o declarar explícitamente que la escena es un ejemplo distinto. Decisión del autor del capítulo, como ya se indicó.

### H-05 — Escena I2 y práctica I usan rectas distintas para los mismos niveles
- **Severidad:** baja.
- **Ubicación:** `M02_libreto.md`, escena I2 (líneas ~148–152: a=0,080; pendiente 0,002075; predicciones 0,246…0,910 con errores 0,23…0,88) frente a la práctica I (a=0,100; pendiente 0,002; predicciones 0,26…0,90).
- **Problema:** mismos niveles (80–400) con dos ajustes diferentes en el mismo capítulo. No estaba en la revisión previa. No es un error numérico, pero puede confundir al alumno sobre cuál es «el» ajuste.
- **Corrección propuesta:** o usar la recta de la práctica en la escena, o indicar que la escena es un ejemplo de cinco pares distinto del conjunto de la práctica.

### H-06 — `scatter_panel` sigue leyendo la variable global `levels` y `coef`
- **Severidad:** baja.
- **Ubicación:** `curso/S1_fundamentos/calc/M02_practicas_luna.py`, `scatter_panel()`: bucle de predicciones `for x, y in zip(levels, np.polyval(...))`.
- **Problema:** H-10 quitó la dependencia de `groups_for_plot`, pero la función aún usa `levels` como global. Hoy el resultado es correcto, pero el problema de H-10 persiste en menor grado.
- **Corrección propuesta:** pasar `levels` y los coeficientes como parámetros de `scatter_panel`.

### H-07 — M06 línea ~152: «las cuatro colas son disjuntas» (redacción)
- **Severidad:** baja.
- **Ubicación:** `curso/S2_modelos_calibracion/M06_libreto.md`, línea ~152.
- **Problema:** la justificación es correcta: si el umbral es mayor que 0,5, como mucho una varianza puede superarlo, así que los cuatro sucesos «esta varianza supera el umbral» son mutuamente excluyentes. Pero la frase habla de «colas», que no son los sucesos que se suman, y no dice por qué son disjuntas.
- **Corrección propuesta:** «…aquí el umbral es mayor de 0,5; por tanto, como mucho una varianza puede superarlo y los cuatro sucesos de superación son disjuntos, lo que hace exacta la corrección de Bonferroni [ISO 5725-2 §7.3.3 y §8.1, tabla 4].»

### H-08 — M06 línea ~219: «esperaríamos en promedio medio falso positivo» (redacción)
- **Severidad:** baja.
- **Ubicación:** `curso/S2_modelos_calibracion/M06_libreto.md`, línea ~219.
- **Problema:** la cifra es correcta (10 × 0,05 = 0,5 falsos positivos esperados), pero «medio falso positivo» se lee como una frase hecha, no como un número. Para un público de operadores conviene decirlo en cifras.
- **Corrección propuesta:** «…esperaríamos en promedio 0,5 falsos positivos; este cálculo no requiere independencia…». Además, las cifras de F que siguen en la misma línea («135 y 405… 360 y 455») deben verificarse ejecutando `calc/M06_RR_CALAIRE.py`; no se hizo en esta revisión.

## Conclusión

Las cifras de las tres prácticas M02 coinciden con la ejecución del script, y los HTML son reproducibles. La mayoría de los hallazgos de la revisión previa (H-01 a H-05, H-07, H-08) están bien resueltos. Quedan abiertos H-06 y H-11 previos (H-04 y H-01 de este informe). **Antes de dar M02 por cerrado conviene corregir H-02** (fondo del gráfico A con `fill` inválido), que es un defecto visible en un entregable, y **H-01**, porque la bitácora afirma una corrección que no se aplicó. En M06, la atribución de la línea ~237 es correcta; las líneas ~152 y ~219 son correctas en cifras, con redacción mejorable (H-07 y H-08).
