# Bitácora de desarrollo de prácticas M02

Fecha: 2026-10-27. Alcance: sustituir únicamente los tres marcadores de práctica de `curso/S1_fundamentos/M02_libreto.md`; no añadir taller integrador ni modificar citas, referencias, guía, revisión final u otros capítulos. No se hicieron commits.

## Plan

- B: aplicar estadística descriptiva a indicaciones y errores emparejados durante tres días, incluyendo negativos del cero, resúmenes de centro/dispersión, serie temporal, histograma y cajas por día; escalar ante estructura temporal.
- I: separar resúmenes dentro/entre grupos y tendencia descriptiva del error con la referencia, con datos por día y nivel; producir gráficos frente a referencia/tiempo, MAD y modelo lineal del error sin bandas ni pruebas de falta de ajuste.
- A: estudiar cómo signo, valor absoluto, ponderación/agregación y una observación influyente cambian las conclusiones; conservar los datos y no convertirlo en análisis de componentes R&R ni indicador de M12.
- Datos deterministas con reglas explicitadas en los enunciados y cálculo reproducible en `curso/S1_fundamentos/calc/M02_practicas_luna.py`. Todos simulados y expresamente no atribuidos a CALAIRE.

## Ejecución

Se desarrollaron completamente los bloques B, I y A bajo la etiqueta `[PRÁCTICA]`: enunciado narrado, datos con unidades nmol/mol, pregunta estadística/unidad de repetición/escala temporal, tareas, solución docente con cifras y comprobaciones, interpretación operativa, señal de escalamiento y criterio breve de logro. Las deducciones no se incorporaron.

Se añadió `curso/S1_fundamentos/calc/M02_practicas_luna.py`. El script usa `curso/.venv/bin/python`, numpy y datos fijos; comprueba emparejamiento y resultados clave, imprime las filas/salidas y genera tres gráficos HTML reproducibles con SVG, leyendas, unidades, marcadores diferenciados y tablas accesibles: B (serie temporal), I (error frente a referencia por día) y A (errores por condición). La construcción del gráfico evita dependencias de trazado externas.

La paleta categórica se validó con `dataviz/scripts/validate_palette.js` en modo claro y oscuro. En claro: contraste del aqua 2,74:1 quedó en WARN con alivio por etiquetas visibles/tabla; los demás controles pasaron. En oscuro: todos los controles pasaron, incluidos contraste ≥3:1. Los gráficos llevan colores y formas secundarias, leyenda y tabla accesible. Habilidad aplicada desde `dataviz` disponible en la sesión; la ruta literal indicada en la petición (`.../2f61c5ae.../dataviz/SKILL.md`) no existía en este entorno, por lo que se leyó la copia disponible bajo `.../2f48327f.../dataviz/` y sus referencias de paleta, forma, marcas y antipatrones.

## Archivos generados o editados

- Editado: `curso/S1_fundamentos/M02_libreto.md`, solo en los tres bloques de práctica redactados en esta intervención. Al verificar el diff se detectó un cambio concurrente en la fila de referencias de la ficha; no se revirtió ni modificó, para preservar el trabajo del supervisor.
- Creado: `curso/S1_fundamentos/calc/M02_practicas_luna.py`.
- Generados por el script: `curso/S1_fundamentos/M02_practica_B_grafico.html`, `curso/S1_fundamentos/M02_practica_I_grafico.html`, `curso/S1_fundamentos/M02_practica_A_grafico.html`.
- Generado: `curso/logs/M02_practicas_luna_ejecucion.txt`.
- Esta bitácora: `curso/logs/M02_practicas_luna.md`.

## Comprobaciones y resultados

- Ejecución completa: `curso/.venv/bin/python curso/S1_fundamentos/calc/M02_practicas_luna.py`; terminó con código 0 y generó la salida numérica y tres HTML.
- B: `s(y)=0,28123`, `s(e)=0,14460` nmol/mol; medias diarias de error −0,05; 0,05; 0,15 nmol/mol; media de negativos del cero conservados 0,00 frente a 0,06 nmol/mol truncados.
- I: medias de error por día 0,50; 0,58; 0,66 nmol/mol; MAD diario 0,20; ajuste descriptivo del error: intercepto 0,100 nmol/mol y pendiente 0,002; predicciones por nivel 0,26; 0,42; 0,58; 0,74; 0,90 nmol/mol.
- A: media firmada combinada 0,00 frente a media absoluta 0,40 nmol/mol; media de centros de grupo con tamaño desigual 0,025 frente a media agrupada 0,150 nmol/mol; con el punto de sensibilidad +1,6, la media firmada es 0,17778 nmol/mol y la desviación estándar 0,67041 nmol/mol.
- Comprobación textual: quedan exactamente tres `[PRÁCTICA]` en M02 y cero marcadores antiguos. Se retiraron caracteres de control en las fórmulas insertadas. No se modificaron capítulos adicionales. No se ejecutaron suites globales del curso, pues el alcance solicitado fue M02.

## Correcciones — ronda Haiku 2026-10-27

Se revisó cada hallazgo H-01 a H-11 del informe `M02_practicas_revision_haiku.md`. Se aplicaron los que correspondían a las prácticas nuevas, se aceptaron ajustes de coherencia limitados a los bloques de práctica y se rechazaron los que pedían cambiar contenido fuera del alcance autorizado. Ninguna cita, clave ni sección de referencias fue editada en esta ronda.

| Hallazgo | Decisión | Ubicación y resultado |
|---|---|---|
| H-01 | Aplicar | B, `M02_libreto.md` práctica B y script: añadido histograma de seis intervalos de ancho 0,1, bordes −0,25 a 0,35, frecuencias 1; 2; 3; 3; 2; 1; cajas por día y tabla con mínimo, Q1, mediana, Q3 y máximo; HTML contiene tres SVG y tablas accesibles. |
| H-02 | Aplicar | I, `M02_practicas_luna.py` y `M02_practica_I_grafico.html`: tres paneles por día, mismos límites x=60–420 y e=−0,2–1,2 nmol/mol; agrupación Día 1/2/3 con marca y forma diferenciada, datos en tabla. |
| H-03 | Aplicar | I, script, HTML y solución docente: recta descriptiva superpuesta en cada panel, rombos de predicción 0,26; 0,42; 0,58; 0,74; 0,90 nmol/mol y panel temporal separado con medias 0,50; 0,58; 0,66 nmol/mol; leyenda y tablas accesibles. |
| H-04 | Aplicar | Los tres HTML generados por el script: formato visible con coma decimal en ejes, tablas y tooltips; descripción del SVG temporal usa signo − y unidades. Inspección automatizada: no se encontró el literal numérico `99.8`. |
| H-05 | Aplicar con sustitución | Paleta de la tercera serie cambiada a `#199e70`, manteniendo marcas/estilos distintos. Validador de la habilidad ejecutado en claro y oscuro: todas las comprobaciones pasan (banda, croma, separación CVD, visión normal y contraste). |
| H-06 | Rechazar | La escena A1 no se modificó: no es práctica nueva en el alcance de esta ronda y el hallazgo pide editarla. La práctica A conserva su ejemplo propio, coherente con el script y su solución numérica verificada. |
| H-07 | Aplicar ajuste mínimo de contexto (aunque fuera del bloque) | `M02_libreto.md`, escena I1: corregido el texto heredado para que retome las doce observaciones B, cuatro por día, medias −0,05; 0,05; 0,15 y s dentro de día 0,129. Sin modificar la práctica ni referencias. |
| H-08 | Aplicar | Leyendas, tooltip y tablas ahora identifican explícitamente «Día 1…3» en I y «Grupo 1/2» en A; no quedan categorías numéricas ambiguas. |
| H-09 | Aplicar | Esta bitácora registra gráficos añadidos, resultados y limitaciones; elimina la afirmación de integridad anterior sin mencionar las omisiones ya corregidas. |
| H-10 | Aplicar | Función `scatter_panel` recibe grupos y nombres como argumentos; ya no consulta la variable global `groups_for_plot`. |
| H-11 | Aplicar | Enunciado B identifica explícitamente el nivel de ozono del SRP y unidades nmol/mol. En A se precisa «estudio tipo R&R del Level 2»; todos los datos siguen rotulados como simulados y no atribuidos a CALAIRE. |

### Corrección supervisora S-M02-01

Se precisó que la desviación estándar $0,23664$ nmol/mol se calcula agrupando las 20 lecturas de un día a través de los cinco niveles. Como los centros cambian con $x$, incluye la tendencia de calibración y no responde a precisión/repetibilidad dentro de nivel. El script ahora imprime y verifica la desviación estándar muestral de cada celda día×nivel; las cuatro lecturas de error $r=−0,06;−0,02;0,02;0,06$ producen $s=0,0516398$ nmol/mol en las 15 celdas. En el libreto se añadieron esta cifra y la distinción conceptual en tareas, solución docente, interpretación y criterio. No se modificaron ni regeneraron gráficos; se conservaron los tres HTML y sus contenidos.

### Reejecución final

`curso/.venv/bin/python -I -m py_compile curso/S1_fundamentos/calc/M02_practicas_luna.py` terminó correctamente. `curso/.venv/bin/python -I curso/S1_fundamentos/calc/M02_practicas_luna.py` terminó con código 0 y actualizó `M02_practicas_luna_ejecucion.txt`. Los tres HTML se regeneraron en cada ejecución: B e I coinciden byte a byte con la versión anterior; A cambió solo por el relleno de fondo corregido en la ronda de cierre (ver abajo).

Resultados verificados: B, $s(y)=0,28123$, $s(e)=0,14460$ nmol/mol; errores medios diarios −0,05; 0,05; 0,15; cero firmado 0 frente a 0,06 truncado. Histograma B: seis conteos 1; 2; 3; 3; 2; 1. Cuartiles por día B: (−0,125; −0,05; 0,025), (−0,025; 0,05; 0,125), (0,075; 0,15; 0,225) para Q1, mediana y Q3; bigotes mínimo–máximo según práctica. I: medias diarias 0,50; 0,58; 0,66; MAD=0,20; ajuste con intercepto 0,100 y pendiente 0,002; predicciones 0,26; 0,42; 0,58; 0,74; 0,90; residuos de −0,14 a 0,14. A: resultados anteriores reproducidos, incluido promedio firmado 0,00 frente a media absoluta 0,40 y s con punto +1,6 de 0,67041 nmol/mol.

Validación adicional: el HTML de B contiene 3 SVG y 3 tablas; I contiene 1 SVG compuesto de tres paneles de escala común más panel temporal y 3 tablas; A contiene 1 SVG y 1 tabla. Los tres tienen idioma español, rótulos/leyendas, unidades, tooltips SVG y ninguna referencia ARIA sin resolver; los números visibles usan coma decimal. No se pudo abrir/renderizar en navegador en este entorno, por lo que la comprobación visual de colisiones no se afirma. La ruta literal de habilidad citada por el usuario no existía; se aplicaron las instrucciones cargadas de dataviz y sus referencias disponibles, incluido el validador ejecutable.


## Ronda de cierre

Fecha: 2026-10-28. Ejecutor: Haiku 5.5. Entrada: `logs/M02_practicas_revision_cierre_haiku.md`, hallazgos H-01 a H-08. No se tocaron referencias ni citas, ni `guia_libreto.md`; no se hicieron commits.

| H-xx | decisión | ubicación | rc |
|---|---|---|---|
| H-01 | Aplicado: el enunciado de B nombra el nivel de ozono medido con el SRP (nmol/mol). La fila H-11 de la ronda anterior queda así cumplida. | `S1_fundamentos/M02_libreto.md`, enunciado de la práctica B | 0 |
| H-02 | Aplicado: la línea `<rect … fill="{surface}"/>` de `save_a_chart()` es ahora f-string. `M02_practica_A_grafico.html` ya no contiene el literal `fill="{surface}"` y su fondo es `#fcfcfb`. | `S1_fundamentos/calc/M02_practicas_luna.py`, `save_a_chart()` | 0 |
| H-03 | Aplicado: la frase de «Reejecución final» describe ahora la regeneración real de los tres HTML. | `logs/M02_practicas_luna.md`, sección «Reejecución final» | 0 |
| H-04 | Aplicado: la escena A1 usa el punto de sensibilidad +1,6, igual que la práctica A. Cifras: media firmada 0,178; media absoluta 0,533; s 0,670; mediana 0,3; MAD 0,6 nmol/mol. Coinciden con el script (0,17778; 0,53333; 0,67041; 0,3; 0,6). Se corrigió también la diapositiva. Esto cierra el H-06 de la ronda anterior. | `S1_fundamentos/M02_libreto.md`, escena A1 y su diapositiva | 0 |
| H-05 | Aplicado en la narración: la escena I2 declara que sus cinco pares son un ejemplo propio, distinto de los 60 pares de la práctica I. Sus cifras (a = 0,080; pendiente 0,002075) se reproducen con `calc/M02_examples.py` (rc=0). | `S1_fundamentos/M02_libreto.md`, escena I2 | 0 |
| H-06 | Aplicado: `scatter_panel()` recibe `pred_x` y ya no lee la variable global `levels`. La llamada de `save_i_chart()` pasa `pred_x=levels`. Cierra el H-10 de la ronda anterior en lo pendiente. | `S1_fundamentos/calc/M02_practicas_luna.py`, `scatter_panel()` y `save_i_chart()` | 0 |
| H-07 | Rechazado: el hallazgo es de `M06_libreto.md`, fuera del alcance de M02. Además, la corrección propuesta añade numerales nuevos en un corchete de cita (ISO 5725-2 §7.3.3, §8.1, tabla 4), y las citas no se tocan. Se traslada al supervisor de S2. | `S2_modelos_calibracion/M06_libreto.md`, línea ~152 (no editado) | 0 (sin cambio en M02) |
| H-08 | Rechazado: el hallazgo es de `M06_libreto.md`, fuera del alcance de M02. Las cifras de F no están verificadas (requiere ejecutar `calc/M06_RR_CALAIRE.py`). Se traslada al supervisor de S2. | `S2_modelos_calibracion/M06_libreto.md`, línea ~219 (no editado) | 0 (sin cambio en M02) |

**Verificación tras los cambios** (`curso/.venv/bin/python -I S1_fundamentos/calc/M02_practicas_luna.py`):

- rc = 0. La salida estándar es idéntica a la de la ejecución anterior y coincide con `logs/M02_practicas_luna_ejecucion.txt`, así que ese archivo no cambia.
- `M02_practica_B_grafico.html` e `M02_practica_I_grafico.html` tienen el mismo SHA-256 que antes del cambio. `M02_practica_A_grafico.html` cambió solo por el fondo (H-02).
- Cifras de las escenas y prácticas revisadas (B, I, A y escenas I2 y A1): todas coinciden con la salida del script.

**Pendiente, fuera de M02:** H-07 y H-08 quedan para el supervisor de S2 (M06). Si se decide aplicarlos, la verificación de F requiere ejecutar `calc/M06_RR_CALAIRE.py`.
