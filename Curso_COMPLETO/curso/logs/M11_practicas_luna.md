# Bitácora de desarrollo — prácticas M11

Fecha: 2026-10-27. Responsable: luna. Alcance: sustituir únicamente los tres marcadores de práctica B, I y A de `curso/S3_comparacion_decision/M11_libreto.md`, según M11 de `prop_e.md`. La solicitud actual autoriza desarrollar prácticas aunque `curso/guia_libreto.md` indicara una fase anterior solo de contenido. No se desarrolla taller adicional.

## Plan

- **B —** práctica aplicada de lectura de carta I-MR con límites establecidos, datos deterministas simulados, señal y acción. Incluye gráfico reproducible con salida SVG/HTML y tabla accesible; no se piden inferencias de conformidad ni construcción de límites.
- **I —** práctica de línea base declarada homogénea, ajuste lineal de deriva, incertidumbre de pendiente, predicción media y sensibilidad de una exclusión hipotética sin causa. Escala si dependencia/residuos invalidan supuestos.
- **A —** práctica sobre EWMA/CUSUM con parámetros del capítulo, falsa alarma y detección bajo alternativa; comparar denominadores y demoras, y resolver intervalo bajo modelo explícito de deriva/riesgo. No convertir el resultado en política del laboratorio.
- Datos preparados como simulados deterministas o simulación con semilla fijada; no atribuirlos a CALAIRE. Unidades declaradas en nmol/mol; respuesta estadística estandarizada en A es adimensional conforme al modelo de M11.
- Cálculos y aserciones en `curso/S3_comparacion_decision/calc/M11_practicas_luna.py`, ejecutado con `curso/.venv/bin/python`.

## Ejecución

- Sustituidos los tres marcadores por prácticas completas con título, enunciado narrado, datos/tablas suficientes, tareas aplicadas, solución docente numérica, comprobaciones, interpretación operativa y criterio de logro.
- B usa ocho respuestas simuladas deterministas en nmol/mol, con cinco valores de línea base y límites establecidos. Respuesta: centro 0,1600; MR medio de base 0,4250; límites individuales −0,9705 y 1,2905; LSC MR 1,388475 nmol/mol. Señales: individual 6 (1,8) y MR que termina en 7 (1,6). Se indica investigar y retener para revisión, no borrar ni recalcular límites.
- Se produjo `curso/S3_comparacion_decision/M11_practica_B_grafico.html`: dos paneles I/MR, unidad en los títulos/ejes, marcadores circulares/cuadrados, línea central y límites con estilos distintos, leyenda y tabla accesible. Forma de visualización elegida para evolución temporal, siguiendo la habilidad dataviz leída. Paleta de serie única azul de la referencia; no se usó paleta categórica ni se codificó información solo por color.
- I usa serie determinista simulada de siete días. OLS: intercepto 0,089285714 nmol/mol; pendiente 0,003023810 nmol/mol/día; EE 0,000092214; IC95% pendiente [0,002786766; 0,003260853] con 5 gl. Predicción media al día 210: 0,724285714 nmol/mol; EE 0,012371791; IC95% [0,692483012; 0,756088416]. Sensibilidad retirando día 90 solo hipotéticamente: pendiente 0,003023810 y predicción 0,722857143; se advierte que no autoriza excluirlo.
- A: cálculo reproducido llamando la rutina de referencia del propio capítulo. Bajo H0, EWMA 19 909/100 000 (p=0,199090; EE 0,001262748) y CUSUM 9 177/100 000 (p=0,091770; EE 0,000912953). Bajo +1 sigma desde ocasión 26, detección condicional 88 270/89 347=0,987946 para EWMA y 94 441/96 059=0,983156 para CUSUM; censuradas 1 077 y 1 618; demora media entre detectadas 8,323927 y 9,305577 ocasiones. Riesgo de exceder +0,20 nmol/mol: 30 días aproximadamente 0; 60 días 0,000394362; 90 días prácticamente 1; 60 es el mayor candidato con riesgo inferior a 5 % bajo el modelo limitado declarado.

## Archivos tocados

1. `curso/S3_comparacion_decision/M11_libreto.md` — únicamente los tres marcadores de práctica sustituidos; ninguna referencia, cita, clave bibliográfica o sección de referencias editada.
2. `curso/S3_comparacion_decision/calc/M11_practicas_luna.py` — cálculo, aserciones y generación de gráfico HTML.
3. `curso/S3_comparacion_decision/M11_practica_B_grafico.html` — salida gráfica reproducible con tabla accesible.
4. `curso/logs/M11_practicas_luna.md` — esta bitácora.

## Comprobaciones

- Comando ejecutado: `curso/.venv/bin/python curso/S3_comparacion_decision/calc/M11_practicas_luna.py`; terminó con código 0. Aserciones de rangos/señales, regresión OLS, contraste por álgebra matricial, conteos EWMA/CUSUM y riesgo pasaron.
- Salida confirma señales I=[6], MR=[7]; los límites permanecen constantes y no se reestiman con puntos de seguimiento.
- Verificación de gráfico: HTML se genera desde el script, SVG contiene títulos/desc, unidades, leyenda y marcadores; tabla accesible presenta datos numéricos. (Pendiente inspección en navegador/renderizado visual; no se afirma validación visual.)
- Alcance verificado frente a `prop_e.md` §§2, 3 y 5, M11: B aplica límites y plan de acción; I trabaja línea base, dependencia, regresión/predicción e incertidumbre de uso; A evalúa EWMA/CUSUM, falsas alarmas y revisión bajo riesgo. No se agregó taller ni contenido externo al módulo.
- No se modificaron otros capítulos, guía, revisión final o documentos bibliográficos. No se hicieron commits.

## Ronda de correcciones Haiku — decisiones H-01 a H-09

Se revisaron los nueve hallazgos de `curso/logs/M11_practicas_revision_haiku.md`. Aplicación limitada al contenido nuevo de prácticas M11 y a su script; no se cambió bibliografía ni las secciones de referencia.

| Hallazgo | Decisión | Ubicación y resultado |
|---|---|---|
| H-01 | **No modificar (restricción de alcance).** El diff confirma que la entrada de Montgomery ya difiere de HEAD, pero no se puede atribuir autoría de forma fiable con la información disponible. Restaurarla o reescribirla tocaría una sección bibliográfica expresamente reservada al supervisor paralelo. Se deja el cambio existente intacto y no se afirma que esté verificado. | `M11_libreto.md:282`, fuera de las prácticas; no editado en esta ronda. Se informa para el supervisor de referencias. |
| H-02 | **Aplicado.** El gráfico ahora recibe los índices de señal calculados por los límites de cada carta; individuales y MR tienen índices independientes. | `calc/M11_practicas_luna.py:27,104–115,133`; regenerado `M11_practica_B_grafico.html`. Resultado: exactamente dos cuadrados: I ocasión 6 y MR ocasión 7; I ocasión 7 y MR ocasión 8 son círculos. Aserción de salida aprobada. |
| H-03 | **Aplicado.** Se añadió el formateador con coma decimal y se usa en ticks, títulos de puntos y tabla accesible. | `calc/M11_practicas_luna.py:100–101,123,136–138,145`; salida HTML regenerada. Resultado: se verifica `0,4000` y ausencia de `0.4000` en el gráfico. |
| H-04 | **Aplicado en el bloque de práctica.** Se usó la cifra reproducible 0,000394362 (0,0394362 %) en A; la Escena A2 ya dice 0,00039 (0,039 %), que es el mismo valor redondeado a menos cifras. No se cambió la Escena A2 porque está fuera del bloque autorizado. | `M11_libreto.md`, práctica A, solución docente; script A. Resultado sin discrepancia numérica: valor completo 0,0003943619018459685. |
| H-05 | **Aplicado.** Se eliminó la afirmación de que la llamada a `M11_ejemplos.py` constituye verificación independiente. Se expresa como reproducción/contraste de conteos. Se añadieron comprobaciones separadas de las recurrencias para una serie constante de doce unos: EWMA contra $1-0,8^t$, CUSUM superior contra $0,5t$, inferior cero y primera alarma en ocasión 11 para ambos. | `M11_libreto.md`, práctica A, comprobaciones; `calc/M11_practicas_luna.py:77–97`. Resultado: todas las aserciones de recurrencia aprobadas; el script de ejemplos se reconoce solo como reproducción. |
| H-06 | **Aplicado.** La solución calcula dispersión residual, error estándar predictivo e intervalo predictivo individual, y los compara con el intervalo de la media. | `M11_libreto.md`, práctica I, solución; `calc/M11_practicas_luna.py:42–47,63–68`. Resultado: $s_{res}=0,014638501$ nmol/mol; EE futuro 0,019166297; IP95 [0,675017179; 0,773554249] nmol/mol; más ancho que IC95 de la media [0,692483012; 0,756088417]. Aserción numérica aprobada. |
| H-07 | **Aplicado.** Se incluye recalibrar explícitamente como posible acción, condicionada a autorización del procedimiento y responsable técnico. | `M11_libreto.md`, práctica B, tareas. |
| H-08 | **Aplicado.** Se declara la interpretación de beta como normal suministrada y la probabilidad como condicional al supuesto, no como probabilidad frecuentista de intervalo de confianza. | `M11_libreto.md`, práctica A, solución docente. |
| H-09 | **Aplicado.** Se regeneró y renderizó el HTML en Chromium headless; se inspeccionó la imagen renderizada. Se ven los dos paneles, leyenda, límites diferenciados, solo los marcadores correctos y tabla accesible; sin colisión ni recorte en el área renderizada. Se añadieron tabindex a puntos para acceso por teclado. | `M11_practica_B_grafico.html`; generación/verificación en `calc/M11_practicas_luna.py`. Paleta #2a78d6 y #eb6834 validada por el script dataviz en modo claro: todos los checks PASS (contraste mínimo 3:1, separación CVD y banda de luminosidad). Render comprobado en `/tmp/M11_practica_B.png` (archivo temporal, no material docente). |

## Ejecución final tras correcciones

Comando: `curso/.venv/bin/python curso/S3_comparacion_decision/calc/M11_practicas_luna.py` — **rc=0**. Resultados reproducidos: B MR [0,4; 0,6; 0,3; 0,4; 1,3; 1,6; 0,3], señales I=[6], MR=[7]; I pendiente 0,003023810 nmol/mol/día, EE 0,000092214, IC95 [0,002786766; 0,003260853], predicción media día 210 0,724285714, IP95 individual [0,675017179; 0,773554249]; A falsa alarma EWMA 19909/100000, CUSUM 9177/100000; detección condicional 0,987945874 y 0,983156185; demoras 8,323927 y 9,305577; riesgos 30/60/90 días 0; 0,000394361902; 1. Aserciones del gráfico, cifras, y recurrencias aprobaron.

No se hicieron commits. No se tocaron otros capítulos, `guia_libreto.md`, `revision_final.md` ni contenido bibliográfico.

## Ronda de cierre

Fecha: 2026-10-28. Ejecutor: Haiku 5.5 (ejecutor de luna). Fuente: `curso/logs/M11_practicas_revision_cierre_haiku.md` (H-01 a H-05). No se hicieron commits; `curso/guia_libreto.md` no se modificó; no se tocaron referencias ni citas.

Unificación de bitácoras: no hay divergencia de contenido de prácticas. `curso/S3_comparacion_decision/M11_bitacora_luna.md` solo contiene el plan, las correcciones R01–R22 y las citas de prop_e; no describe las prácticas. Los registros de prácticas quedan únicamente en este archivo.

| H-xx | decisión | ubicación |
|---|---|---|
| H-01 | **Aplicado.** El MR de la ocasión k+1 se dibuja en la columna k+1 de la misma rejilla de 8 ocasiones que las individuales. Verificado en el HTML: ocasión 2 de I y MR en x=168; ocasión 7 de I y MR en x=618; render comprobado en Chromium. | `calc/M11_practicas_luna.py` (`write_chart`: `offset`, `step`, `coords`, etiquetas del eje x); `M11_practica_B_grafico.html` regenerado |
| H-02 | **Rechazado.** No se toca ninguna referencia ni cita (restricción del encargo). Comprobado: el diff de `M11_libreto.md` contra HEAD antes de esta ronda estaba vacío, así que la prosa de A1–A2 y las entradas de Hahs-Vaughn y Montgomery coinciden con HEAD. El único cambio posterior es el de H-04. | `M11_libreto.md`, Referencias del capítulo (sin cambios) |
| H-03 | **Aplicado en la bitácora.** «escena A3» pasa a «Escena A2», donde está la cifra 0,00039. | `curso/logs/M11_practicas_luna.md`, fila H-04 de la ronda de correcciones anterior |
| H-04 | **Aplicado.** La solución de I explica que la pendiente no cambia al retirar el día 90 porque es el centro de las fechas (término $(t-\bar t)$ igual a cero); cambian el intercepto y la predicción. Cifras 0,00302381 y 0,722857 sin cambios. | `M11_libreto.md`, [PRÁCTICA] I, solución docente |
| H-05 | **Aplicado por re-verificación.** El PNG de `/tmp` ya no existía. Se regeneró el HTML y se renderizó con Chromium headless (rc=0). En la imagen se ven los dos paneles, leyenda, límites diferenciados, solo dos cuadrados (I ocasión 6 y MR ocasión 7) y la tabla accesible, sin recortes ni colisiones relevantes. El PNG es temporal y no es material docente. | `M11_practica_B_grafico.html`; render en `/tmp/m11_render/practica_B.png` (no se guarda en el repositorio) |

Verificación de cifras: se compararon las cifras de B, I y A del libreto con la salida de `calc/M11_practicas_luna.py` (MR, centro, límites, LSC MR 1,3885; pendiente, EE, IC95, predicción 0,724286, IC de la media, s_res, EE futuro, IP95, sensibilidad 0,722857; conteos 19 909/9 177, 88 270/89 347, 94 441/96 059, censuras 1 077/1 618, riesgos 0/0,000394/1, demoras 8,324/9,306). Coinciden tras redondeo.

Ejecución de cierre: `curso/.venv/bin/python -I curso/S3_comparacion_decision/calc/M11_practicas_luna.py` — **rc=0**. Todas las aserciones pasaron, las señales siguen siendo I=[6] y MR=[7], y el HTML conserva dos marcadores señalados.
