# S1. Fundamentos — índice de entrega

Fecha de entrega revisada: 26 de octubre de 2026. Alcance: contenido narrado de M00–M04, niveles acumulativos B, I y A. Esta entrega no incluye ejercicios, soluciones de prácticas, rúbricas ni autorización para impartir. Los ejemplos numéricos resueltos pertenecen a la explicación docente; no son paquetes de prácticas.

Orden: M00 organiza las observaciones; M01 define el resultado y sus entradas; M02 elige y describe la respuesta; M03 introduce distribuciones y dependencia; M04 desarrolla estimación y contraste. I presupone B; A presupone B e I. Entrada directa a I/A requiere el diagnóstico curricular, todavía perteneciente a la fase de ejercicios.

## M00. Estructura de los datos y cálculo reproducible

[Libreto](M00_libreto.md) · [Bitácora de desarrollo](M00_bitacora_luna.md) · [Revisión Haiku](M00_revision_haiku.md).

- **B:** introducción de tabla larga e identificadores; B1, identificar la pareja antes de restar; B2, dato original, valor calculado y corrección trazable. Incluye faltantes, negativos del cero y señales de escalamiento.
- **I:** I1, conservar factores al agrupar con clave campaña × analista × día; I2, de ancho a largo sin inventar observaciones. Incluye campañas, analistas, días, conteos y exclusiones documentadas.
- **A:** A1, contrato de entradas, salidas y comprobaciones; A2, contraste de dos herramientas y tolerancia numérica.

Marcadores pendientes, uno por práctica curricular:

> **[PRÁCTICA — fase de ejercicios]** B: organizar un conjunto corto del Level 2, calcular e, detectar pareja desplazada y faltante y documentar corrección sin borrar el original.
>
> **[PRÁCTICA — fase de ejercicios]** I: reconstruir resúmenes diarios desde las parejas originales.
>
> **[PRÁCTICA — fase de ejercicios]** A: reproducir un resultado con segunda herramienta y explicar discrepancias.

**Datos y rótulo:** simulados, construidos explícitamente: cinco referencias/cuatro indicaciones; dieciséis combinaciones campaña–analista–día–ciclo; tabla ancha de cuatro celdas con tres valores y un faltante; tres parejas para Python/LibreOffice Calc. No son resultados del laboratorio. **Cálculo:** [M00_ejemplos.py](calc/M00_ejemplos.py); contraste independiente [verificar_M00_sol.py](calc/verificar_M00_sol.py). **AX:** sin remisión necesaria.

## M01. Modelo de medición y variables de análisis

[Libreto](M01_libreto.md) · [Bitácora de desarrollo](M01_bitacora_luna.md) · [Revisión Haiku](M01_revision_haiku.md).

- **B:** B1, qué resultado se compara; B2, modelo de medición como función; B3, sensibilidad numérica con plantilla. Mensurando, error, sesgo y corrección; conversión explícita a nmol/mol.
- **I:** I1, cambiar parámetro de escala no corrige automáticamente el instrumento. Cocientes declarados, signo y denominador del error relativo.
- **A:** A1, una entrada compartida puede desaparecer de la diferencia, solo con el modelo y las sensibilidades apropiados.

> **[PRÁCTICA — fase de ejercicios]** B: recalcular tres concentraciones con dos secciones eficaces declaradas e indicar signo y cambio relativo.
>
> **[PRÁCTICA — fase de ejercicios]** I: comparar escalas con cociente de valores realmente implementados y par declarado.
>
> **[PRÁCTICA — fase de ejercicios]** A: identificar contribuciones que se cancelan en una diferencia y las que permanecen en el resultado absoluto.

**Datos y rótulo:** entradas y resultados simulados para indicaciones, trayecto óptico hipotético y contribuciones comunes; coeficientes publicados cuando su fuente técnica está identificada. Los cocientes curriculares no equivalen a una certificación de qué coeficiente implementa el laboratorio. **Cálculo:** [M01_modelo_variables.py](calc/M01_modelo_variables.py). **AX:** AX.2, propagación y combinaciones con covarianza; la deducción no se imparte aquí. **Pendiente de aplicación real:** documentar coeficientes, unidad y escala efectivamente implementados; no inferirlos de valores redondeados del ejemplo.

## M02. Estadística descriptiva y elección de la respuesta

[Libreto](M02_libreto.md) · [Bitácora de desarrollo](M02_bitacora_luna.md) · [Revisión Haiku](M02_revision_haiku.md).

- **B:** B1, variable antes del resumen; B2, frecuencias, histograma, cuantiles y caja; B3, centro y dispersión, lecturas frente a promedios; B4, indicación, error y CV, con descomposición descriptiva de varianzas; B5, orden temporal, valores inusuales y comunicación.
- **I:** I1, resúmenes dentro y entre grupos, mediana y MAD; I2, error que cambia con referencia, modelo de sesgo proporcional.
- **A:** A1, signo, magnitud, agregación e influencia. Sensibilidad de conclusiones a transformaciones y observaciones, sin trasladar aquí el cálculo básico de indicadores de M12-B.

> **[PRÁCTICA — fase de ejercicios]** B: comparar dispersión de indicaciones y errores en un nivel durante varios días; interpretar cambio de referencia y conservar negativos del cero.
>
> **[PRÁCTICA — fase de ejercicios]** I: elegir respuesta para precisión y calibración con gráficos frente a referencia y tiempo.
>
> **[PRÁCTICA — fase de ejercicios]** A: analizar, con sesgos opuestos del caso R&R, cambios de conclusión al usar e o su valor absoluto y pérdida de información.

**Datos y rótulo:** todos simulados determinísticamente: indicaciones alrededor de 100 nmol/mol; parejas de tres días en un único nivel nominal de 200 nmol/mol; negativos del cero; grupos, tendencia y sesgos opuestos para agregación e influencia. Ningún resultado procede del libro R&R. **Cálculo:** [M02_examples.py](calc/M02_examples.py). **AX:** AX.1, divisor n−1 y grados de libertad. Los gráficos se explican como parte del libreto; el índice no añade visualizaciones ni actividades.

## M03. Probabilidad, distribuciones y dependencia

[Libreto](M03_libreto.md) · [Bitácora de desarrollo](M03_bitacora_luna.md) · [Revisión Haiku](M03_revision_haiku.md).

- **B:** B1, repetición y modelo de probabilidad; B2, distribuciones normal, rectangular y triangular y conversiones; B3, lectura, promedio y t. Incluye cuantiles, grados de libertad y límite de reducción por componente común/deriva.
- **I:** I1, covarianza y correlación; I2, chi-cuadrado, F y gráficos de probabilidad; I3, dependencia temporal y escalas de variación.
- **A:** A1, causas comunes entre canales y puntos; A2, autocorrelación, estrategias de promedio global, por bloques y con tendencia declarada, y operación con matrices de covarianza: unidades, simetría y admisibilidad.

> **[PRÁCTICA — fase de ejercicios]** B: convertir especificaciones a incertidumbre estándar y comparar promedio independiente con serie con deriva.
>
> **[PRÁCTICA — fase de ejercicios]** I: calcular incertidumbre de diferencia con y sin covarianza.
>
> **[PRÁCTICA — fase de ejercicios]** A: construir y comprobar matriz pequeña de covarianza y comparar promediado en serie con ruido y deriva.

**Datos y rótulo:** simulados, con modelos y magnitudes explícitos; resolución hipotética de 0,1 nmol/mol, no especificación del 49C ni del SRP; modelos de distribución, componente común, diferencia, grupos temporales y matrices. **Cálculo:** [M03_ejemplos.py](calc/M03_ejemplos.py). **AX:** AX.2, combinaciones y propagación; AX.3, rectangular y triangular. No se imparte varianza de Allan ni formulación GGMR fuera del alcance curricular.

## M04. Inferencia: estimación y contraste

[Libreto](M04_libreto.md) · [Bitácora de desarrollo](M04_bitacora_luna.md) · [Revisión Haiku](M04_revision_haiku.md).

- **B:** B1, muestra y estimador; B2, distribución muestral de media e intervalo t; B3, contraste de una media, valor p y errores de decisión. Unidad de repetición independiente declarada en un nivel.
- **I:** I1, pareadas y Welch; I2, inferencia sobre varianzas con chi-cuadrado y F; I3, potencia y tamaño según diseño de media, pares o dos grupos, aproximación normal y cálculo t no central con statsmodels; I4, incertidumbre de desviación estimada; I5, condiciones de Grubbs y Dixon.
- **A:** A1, multiplicidad; A2, equivalencia con márgenes predefinidos; A3, consistencia conjunta por chi-cuadrado.

> **[PRÁCTICA — fase de ejercicios]** B: intervalo del error medio del Level 2 en un nivel; contraste con cero y magnitud relevante.
>
> **[PRÁCTICA — fase de ejercicios]** I: apartados distintos para t pareada, Welch, varianzas, potencia/tamaño por diseño, incertidumbre de s y condiciones/conclusión de Grubbs y Dixon.
>
> **[PRÁCTICA — fase de ejercicios]** A: distinguir no rechazar cero de demostrar equivalencia con márgenes definidos.

**Datos y rótulo:** simulados para medias, pares, dos grupos, varianzas, potencia, observaciones inusuales, equivalencia y consistencia; F-PSMT-01/Level 2 frente a SRP 55 aporta contexto, no observaciones usadas. En B, ocho jornadas independientes, una pareja por jornada y un nivel nominal; no ocho lecturas consecutivas asumidas independientes. **Cálculo:** [M04_ejemplos.py](calc/M04_ejemplos.py). **AX:** AX.1 y AX.7. El cierre enlaza con M05, diseño de experimentos.

## Anexos y convenciones comunes

Remisiones principales: [AX_libreto.md](../S4_numericos_integracion/AX_libreto.md), AX.1 (M02/M04), AX.2 (M01/M03), AX.3 (M03), AX.7 (M04). La existencia del destino no acredita la revisión técnica de S4. Otros identificadores AX citados como contexto no cambian el temario ni trasladan deducciones al aula.

Convenciones: x referencia; y indicación; e=y−x; u estándar; U expandida; nmol/mol; d número de días; s_r repetibilidad y s_entre efecto de día excluida repetibilidad. El índice no redefine estimadores ni métodos; prevalece el detalle técnico de los libretos y sus fuentes externas.

## Estado y pendientes

Entrega documental de contenido para revisión de sección, no curso habilitado para impartirse. Decisiones sobre C01–C27, los 37 bloques D2-01–D2-37, los 16 bloques R3-01–R3-16 y correcciones adicionales (hasta S-115): [S1_revision_sol.md](S1_revision_sol.md). Las tres auditorías preservadas: [primera interrupción](auditoria_interrupcion_sol/LEEME.md), [segunda interrupción](auditoria_interrupcion_sol_2/LEEME.md) y [tercera interrupción](auditoria_respaldo_20261026_053907/LEEME.md). Bitácoras y revisiones Haiku son antecedentes, no dictámenes técnicos de esta reanudación. Estado: corregido tras [revisión Opus](S1_revision_opus.md), fase de contenido (claude-sol, gpt-6.1-sol, 2026-10-26). Decisiones O-01–O-14 y registro retrospectivo de scripts en «Correcciones tras la revisión Opus» de la revisión Sol; cuatro mayores resueltos, ningún hallazgo rechazado. El [respaldo posterior a Opus](auditoria_respaldo_20261026_200841/LEEME.md) se revisó bloque por bloque: P6-01–P6-23 tienen decisión y asociación O-… en esa misma sección; los cambios parciales no se aceptaron automáticamente. Cierre verificado: cinco salidas idénticas, 33 comprobaciones M03/M04, contraste Decimal y control de las 23 candidatas. El [segundo respaldo posterior a Opus](auditoria_respaldo_20261026_201402/LEEME.md) (P7-01–P7-03) se decidió en la misma sección: P7-01 y P7-03 conservados; P7-02 revertido (en M04 I2, $d$ sigue siendo número de días y $d_C$ el efecto de Cohen). Cierre P7 por Opus 5.5, esfuerzo bajo.

Pendientes: desarrollar los quince paquetes de prácticas con datos, diccionario, enunciado, plantilla, solución revisada y rúbrica; preparar diagnóstico de entrada; resolver evidencia operativa de coeficientes y escalas; completar preparación curricular de prop_e §§9–10 y expedientes por tema; obtener revisión final del curso. Revisión Opus de S1 recibida y correcciones documentadas; pendientes bibliográficos explícitos: construcción chi-cuadrado (O-06) y fuente específica del límite del CV (O-08, justificado aritméticamente). Las referencias externas ausentes de docs/ se identifican en cada capítulo y en la revisión; no se certifica una consulta inexistente.

Reproducibilidad: scripts, contrastes y salidas bajo [calc/](calc/); entorno en [entorno_sol.txt](calc/entorno_sol.txt); control estructural en [verificar_entrega_sol.py](calc/verificar_entrega_sol.py). Pruebas tras Opus: [pruebas_opus_sol.txt](calc/pruebas_opus_sol.txt); contraste Decimal: [verificar_opus_sol.py](calc/verificar_opus_sol.py). Control ampliado a R3-01–R3-16 y O-01–O-14. Ninguna cifra simulada se presenta como desempeño oficial de CALAIRE.
