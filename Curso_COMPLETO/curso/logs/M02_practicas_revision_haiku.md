# Revisión de las prácticas M02 (B, I, A)

Revisor: Haiku 5.5. Fecha: 2026-10-27. Alcance: `curso/S1_fundamentos/M02_libreto.md` (bloques `[PRÁCTICA]` B, I y A), `curso/S1_fundamentos/calc/M02_practicas_luna.py`, `curso/logs/M02_practicas_luna.md`, y los gráficos generados. No se editó ningún libreto ni script; no se auditaron referencias.

## Verificación ejecutada

- Script reproducido en una copia temporal (`/tmp/m02rev.0Lbs/`, fuera del repositorio) con `curso/.venv/bin/python -I`. Código de salida 0. La salida numérica coincide con `curso/logs/M02_practicas_luna_ejecucion.txt` salvo las rutas absolutas. Los tres HTML generados son idénticos byte a byte a los del curso.
- Cifras de las soluciones docentes comprobadas una a una contra la salida: B (medias, medianas, s, rango, cuartiles lineales, medias diarias de error, media del cero firmado 0 y truncada 0,06); I (medias y medianas diarias y por nivel, MAD 0,20 y 0,06, s agrupada 0,23664, â = 0,100, pendiente 0,002, b̂ = 1,002, predicciones 0,26 a 0,90, residuos ±0,14); A (medias firmadas y absolutas, s = 0,08165 y 0,43425, MAD, media de centros 0,025 frente a media de seis lecturas 0,150, punto +1,6 con 0,17778; 0,53333; 0,30; 0,60; 0,67041). **Todas coinciden.**
- Tres marcadores `[PRÁCTICA]` en M02 (correcto). Sin caracteres de control en el libreto (correcto).
- Origen de datos: las tres prácticas declaran simulación, no atribuyen a CALAIRE y dan la regla de generación. Correcto.
- Alcance según `prop_e.md` (§M2, B/I/A): cumplido en la parte de contenido estadístico (sin ANOVA, sin bandas, sin R&R completo, sin M12-B). Hay incumplimiento en gráficos (H-01 a H-03).

## Hallazgos

### H-01 — Faltan histograma y diagrama de caja por día (B)
- **Severidad:** alta.
- **Ubicación:** `M02_libreto.md`, bloque B, «Tareas» (enunciado de gráficos); `prop_e.md` §M2-B («histograma, caja y serie temporal»). `calc/M02_practicas_luna.py`: solo genera la serie temporal de B (`M02_practica_B_grafico.html`).
- **Problema:** la tarea exige «un histograma de $e$ con intervalos declarados y un diagrama de caja por día», además de la serie temporal. No existen en el script ni en la carpeta de salida. Es un gráfico obligatorio omitido. La bitácora (`M02_practicas_luna.md`, Plan) lo menciona como previsto, pero la sección de ejecución lo da por completo sin declarar la omisión.
- **Corrección propuesta:** añadir al script (a) histograma de los doce errores con intervalos declarados (por ejemplo, ancho 0,1 nmol/mol, bordes de −0,25 a 0,35) y (b) diagrama de caja por día con cuartiles lineales, calculados en el script y con la salida numérica. Generar salida HTML/SVG accesible con leyenda, unidades y tabla de intervalos o de cuartiles. Añadir a la solución docente los intervalos y los cuartiles resultantes. Actualizar la bitácora.

### H-02 — La figura de I no tiene tres paneles por día
- **Severidad:** alta.
- **Ubicación:** `M02_libreto.md`, bloque I, «Tareas» («Tracen una figura de tres paneles con $e$ frente a $x$, uno por día… escala común»). `calc/M02_practicas_luna.py`, llamada `save_scatter(... "M02_practica_I_grafico.html" ...)`.
- **Problema:** el script dibuja un único panel con los tres días superpuestos. La tarea pide tres paneles con escala común. La superposición también oculta la agrupación por día, que es el objetivo de la escena (precisión frente a calibración).
- **Corrección propuesta:** generar tres paneles (uno por día), con los mismos `xlim` e `ylim`, de modo que el lector compare días con escala común. Conservar la tabla accesible.

### H-03 — Faltan la gráfica de medias diarias frente al orden temporal y la superposición de la recta (I)
- **Severidad:** alta.
- **Ubicación:** `M02_libreto.md`, bloque I, «Tareas» («tracen además las medias diarias contra orden temporal» y «superpongan predicciones sobre el gráfico frente a referencia»); `prop_e.md` §M2-I («gráficos frente a referencia y tiempo»). Verificado: `M02_practica_I_grafico.html` tiene 0 elementos `polyline` y no contiene la recta ni el gráfico temporal.
- **Problema:** dos gráficos y una superposición exigidos no se generan. Los números de la solución sí están calculados, pero el lector no puede verificar la tendencia en la figura.
- **Corrección propuesta:** (a) añadir la recta $\hat e(x)=0,100+0,002\,x$ como línea continua sobre el gráfico frente a referencia, con los cinco puntos predichos (0,26; 0,42; 0,58; 0,74; 0,90) marcados y rotulados como «ajuste descriptivo; datos simulados»; (b) añadir gráfico de las medias diarias (0,50; 0,58; 0,66 nmol/mol) contra el día 1–3, con etiqueta de unidades. Ambos con leyenda y tabla accesible.

### H-04 — Separador decimal con punto en gráficos y tablas
- **Severidad:** media.
- **Ubicación:** los tres HTML (`M02_practica_B_grafico.html`, `M02_practica_I_grafico.html`, `M02_practica_A_grafico.html`): celdas de tabla (`<td>99.8</td>`), etiquetas de ejes (`{tick:.1f}`) y tooltips. Texto de descripción del SVG de B: «de menos 0,05 a 0,05 y 0,15», que además usa «menos» en lugar del signo.
- **Problema:** la instrucción de estilo del curso pide coma decimal. Los textos del libreto usan coma, pero los entregables gráficos usan punto. La descripción del SVG de B es ambigua («de menos 0,05»).
- **Corrección propuesta:** formatear todos los números visibles con coma (`f"{v:.1f}".replace(".", ",")`), también en ejes, tablas y tooltips. Reescribir la descripción como «de −0,05 a 0,05 y 0,15 nmol/mol».

### H-05 — El verde de la paleta no alcanza 3:1 sobre el fondo claro
- **Severidad:** media.
- **Ubicación:** `calc/M02_practicas_luna.py`, paleta `#1baf7a` (serie 3 de B; también en I y A). Bitácora: «En claro: contraste del aqua 2,74:1 quedó en WARN con alivio por etiquetas visibles/tabla».
- **Problema:** verificado por cálculo de contraste WCAG sobre `#fcfcfb`: `#2a78d6` 4,30:1; `#eb6834` 3,12:1; `#1baf7a` 2,74:1. Las marcas de datos necesitan 3:1 frente al fondo. Una advertencia no resuelta, mitigada con texto y tabla, no basta para una serie que distingue días. En modo oscuro los tres pasan.
- **Corrección propuesta:** oscurecer el verde (un tono con ≥3:1 sobre `#fcfcfb` y distinto de azul y naranja) y volver a validar con `dataviz/scripts/validate_palette.py` en claro y oscuro. Registrar el resultado final en la bitácora sin WARN.

### H-06 — La escena A1 y la práctica A usan datos distintos para el mismo ejemplo
- **Severidad:** media.
- **Ubicación:** `M02_libreto.md`, escena A1 (párrafo «Veamos la diferencia…» y «Ahora añadamos un valor influyente… +1,8») frente al bloque «[PRÁCTICA] A».
- **Problema:** la escena usa el grupo 2 reducido a (−0,4; −0,4) con media 0,133333 y el punto +1,8 (media firmada 0,2; media absoluta 0,556; s 0,725). La práctica usa (−0,3; −0,4) con media 0,150 y el punto +1,6 (0,17778; 0,53333; s 0,67041). Son dos ejemplos con el mismo nombre en un mismo capítulo, con cifras que no coinciden. El alumno puede comparar valores incompatibles. Las cifras de la escena son internamente correctas (verificado).
- **Corrección propuesta:** alinear la escena con la práctica (o la práctica con la escena). Como la escena no es bloque de práctica, la decisión corresponde al autor del capítulo; recomiendo usar los valores de la práctica, ya verificados por el script.

### H-07 — La escena I1 describe los datos de B con dos errores por día
- **Severidad:** media.
- **Ubicación:** `M02_libreto.md`, escena I1 («Retomemos los seis errores simulados de B, dos por día. Las medias por día son 0,15; 0,00 y 0,20…»).
- **Problema:** el bloque B tiene doce errores, cuatro por día, con medias −0,05; 0,05 y 0,15 nmol/mol. La escena contradice a la práctica que debe retomarla. No pertenece al bloque editado en esta intervención; conviene confirmar si es texto previo.
- **Corrección propuesta:** reescribir la escena con los datos de B (cuatro por día, medias −0,05; 0,05; 0,15) o indicar explícitamente que es un subconjunto.

### H-08 — Leyendas ambiguas en I y A
- **Severidad:** baja.
- **Ubicación:** `save_scatter` en `calc/M02_practicas_luna.py`; leyendas `str(group)` → «1», «2», «3» (I) y «1», «2» (A).
- **Problema:** la leyenda muestra solo números. Un lector no sabe si son días o grupos; el tooltip repite el número.
- **Corrección propuesta:** rotular «Día 1…3» en I y «Grupo 1…2» en A, en leyenda, tooltip y tabla.

### H-09 — La bitácora no declara la omisión de gráficos
- **Severidad:** baja.
- **Ubicación:** `curso/logs/M02_practicas_luna.md`, sección «Plan» (menciona histograma y cajas) frente a «Ejecución» («Se desarrollaron completamente los bloques B, I y A»).
- **Problema:** la bitácora afirma integridad sin declarar que faltan los gráficos de H-01 a H-03.
- **Corrección propuesta:** tras corregir, registrar qué gráficos se generaron y cuáles se añadieron; si no se corrigen, declarar la omisión.

### H-10 — Función de trazado con dependencia oculta
- **Severidad:** baja.
- **Ubicación:** `calc/M02_practicas_luna.py`, `save_scatter`: los bucles usan la variable global `groups_for_plot` en lugar del parámetro `groups`.
- **Problema:** funciona, pero depende de un orden de asignación global. Un cambio en el orden de llamadas produce gráficos incorrectos sin error.
- **Corrección propuesta:** pasar los identificadores de grupo como argumento y usar solo parámetros.

### H-11 — Aplicación a ozono/SRP débil en los enunciados
- **Severidad:** baja.
- **Ubicación:** enunciados de B y A («un nivel nominal», «dos condiciones de un estudio tipo R&R»); I menciona «Level 2».
- **Problema:** el caso de ozono/SRP aparece poco. B y A podrían ser cualquier medición. El alumno no ve la relación con SRP 55 → Level 2 → cliente que el capítulo describe.
- **Corrección propuesta:** en el enunciado de B, identificar el nivel nominal como nivel de ozono del SRP (con unidades nmol/mol) y en A indicar el origen del estudio (condiciones de un estudio tipo R&R del Level 2). Mantener el rótulo «simulado».

## Conclusión

Las cifras y las soluciones docentes son correctas y reproducibles. La revisión no aprueba la práctica por cobertura gráfica: H-01, H-02 y H-03 son gráficos obligatorios que faltan o no cumplen la tarea. Corregir H-01 a H-05 antes de dar por cerrado M02; H-06 y H-07 requieren decisión del autor del capítulo.
