# Bitácora de desarrollo — M12

## Plan

### Alcance por nivel (tomado literalmente de `prop_e.md`, §5, M12)

- **Competencia estadística:** «calcular indicadores agregados de precisión y sesgo con sus límites de confianza y distinguirlos de la incertidumbre de una calibración. (Contexto: verificaciones de los clientes en redes de monitoreo.)»
- **B:** «diferencia relativa con referencia y signo definidos; `media(|d_i|)` frente a `|media(d_i)|`; porcentajes cerca de cero y métrica absoluta.»
- **Práctica B fijada por prop_e:** «calcular indicadores con errores de ambos signos en un escenario docente.»
- **I añade:** «límites de confianza con chi-cuadrado y t; unilateral frente a bilateral; efecto de un cambio de escala; dispersión del cero y umbral bajo hipótesis expresas (sin convertir `3·s₀` en definición universal de límite de detección).»
- **Práctica I fijada por prop_e:** «calcular indicadores y límites; repetir con un cambio de escala en un equipo e interpretar signo y denominador.»
- **A añade:** «dependencia y mezcla de periodos en una serie de verificaciones; efectos comunes de trazabilidad en resultados agregados.»
- **Práctica evaluable A fijada por prop_e:** «analizar una discrepancia entre la conformidad de un instrumento y el desempeño agregado y proponer la evidencia necesaria. El escenario define muestra, referencia, periodos, métrica agregada, cobertura y criterio; se separan expresamente la tolerancia, el límite de control y el umbral del indicador.»

### Escenas previstas

1. Ficha del capítulo: competencia, prerrequisitos M4, M8 y M10, contenido acumulativo, datos rotulados, referencias y remisión a AX.11 para límites de confianza.
2. B1: población de verificaciones agregadas frente a calibración individual; definir pareja, referencia, signo y diferencia relativa. Ejemplo numérico con errores positivos y negativos.
3. B2: contraste entre `media(|d_i|)` y `|media(d_i)|`; qué responde cada indicador y qué cancelación oculta el sesgo firmado; porcentajes con denominador próximo a cero y alternativa absoluta en unidades. Marcador de práctica B.
4. Señales de escalamiento de B: cero o denominador inadecuado, referencia incierta/compartida, dependencia, cambio de escala, periodos no comparables, resultado próximo a criterio; parar y consultar, sin ampliar contenido.
5. I1: dispersión y CV de diferencias; límite de confianza chi-cuadrado, unilateral y bilateral; ejemplo numérico con resultado reproducible. Marcador de práctica I después del resto del contenido I.
6. I2: sesgo firmado/absoluto y límite con t, distinción unilateral/bilateral y signo; ejemplo resuelto con intervalos y criterio de interpretación, bajo supuestos explícitos.
7. I3: cambio de escala y efecto sobre error relativo y denominador; dispersión del cero y umbral calculado bajo hipótesis declaradas, advirtiendo que `3·s₀` no define universalmente el límite de detección.
8. A1: dependencia entre verificaciones, autocorrelación o agrupación por periodo; por qué el cálculo independiente altera la incertidumbre agregada, ejemplo simulado.
9. A2: periodos mezclados y trazabilidad común; distinguir componente común que no desaparece al agregar y variación propia; ejemplo simulado sin convertir resultados en estimación real de CALAIRE. Marcador de práctica A.
10. Cierre: síntesis por nivel, separación explícita entre desempeño agregado de red e incertidumbre de calibración, transición a cierre/sección siguiente.

### Datos y rótulo de origen

- Ejemplos aritméticos de B e I y escenarios de dependencia/periodos de A: **simulados**, generados determinísticamente por `calc/M12_indicadores.py`; serán identificados como docentes y no atribuidos a CALAIRE.
- No se usarán archivos propios de CALAIRE ni datos de redes como si fueran resultados locales o publicados. Las cifras normativas que se reproduzcan se identificarán como publicadas y se verificarán en el documento fuente.
- Cada ejemplo declarará qué constituye una verificación, referencia, periodo, métrica, muestra y escala; no se mezclarán métricas relativas y absolutas sin nombrar el denominador y la unidad.

### Cálculos previstos

`calc/M12_indicadores.py`, ejecutado con `curso/.venv/bin/python`, reproducirá cada cifra calculada del capítulo: diferencias relativas y absolutas de ambos signos; medias de valores absolutos y valor absoluto de la media; CV, límite chi-cuadrado; media/sesgo con límite t; efecto del cambio de escala sobre signo y denominador; dispersión del cero y umbral bajo hipótesis explícitas; y contraste ilustrativo de agregación independiente frente a verificaciones dependientes y componente común. Se registrarán fórmulas, supuestos, semilla si se simula, y salida. Ninguna cifra calculada se incluirá sin correspondencia con el script.

### Referencias a verificar en `docs/` con `pdftotext`

- 40 CFR Part 58, Appendix A: subsecciones que respaldan indicadores agregados de precisión/sesgo, métricas y criterios; confirmar numerales directamente en el PDF.
- 40 CFR Part 53 y 40 CFR Part 50, apéndices pertinentes, únicamente si el texto necesita respaldar una distinción de pruebas de desempeño; no incorporar valores o requisitos regulatorios ajenos al alcance de prop_e M12.
- BS EN 14625:2012: criterio técnico de precisión/deriva solo si se usa como contraste necesario y se verifica numeral/tabla.
- Fuente estadística para intervalos chi-cuadrado/t y dependencia: localizar una referencia disponible en `docs/` y verificar los numerales por `pdftotext`; si no se confirma el numeral, citar la obra sin numeral y anotarlo pendiente.
- Las referencias del mapa de `temario_curso.md` son candidatas, no evidencia técnica ni confirmación de numerales.

### Anexos previstos

- **AX.11:** remisión a límites de confianza de indicadores de precisión y sesgo (chi-cuadrado y t); aquí se aplican, no se deducen.
- **AX.2:** remisión a la varianza de combinaciones lineales para explicar el término de covarianza en el promedio de verificaciones dependientes; no se desarrolla la deducción.

## Ejecución

### Libreto y prácticas

Se escribió `M12_libreto.md` en diez escenas más ficha, señales de escalamiento B, cierre y referencias. B cubre definición de diferencia relativa, signo, `media(|dᵢ|)` frente a `|media(dᵢ)|`, referencia cerca de cero y métrica absoluta. I desarrolla límites con chi-cuadrado y t, unilateral frente a bilateral, cambio de escala y dispersión/umbral del cero bajo hipótesis. A trata dependencia, periodos mezclados y trazabilidad común. Se dejaron solo los tres marcadores, en su nivel correspondiente, sin enunciados ni soluciones:

- B: «Indicadores con diferencias de ambos signos».
- I: «Indicadores, límites y cambio de escala».
- A: «Discrepancia entre conformidad individual y desempeño agregado».

La ficha y la escena A1 remiten a AX.11 para límites de confianza y AX.2 para varianza de combinaciones lineales. Las cifras de ejemplos están rotuladas como simuladas y no atribuidas a CALAIRE. Los valores regulatorios y de EN citados se distinguen como publicados.

### Scripts y resultados

Script ejecutado con `curso/.venv/bin/python`:

- `calc/M12_indicadores.py` — reproduce todos los resultados calculados en el libreto. Datos deterministas y simulados; no requiere semilla aleatoria.

Salida relevante: `d=[−2, +1, −1, +2] %`; `media(d)=0,0000 %`; `media(|d|)=1,5000 %`; `|media(d)|=0,0000 %`; `s(d)=1,825742 %`; `SE(media)=0,912871 %`; `IC bilateral 95 %=[−2,905163 %, +2,905163 %]`; `χ²₀,₁₀;₃=0,584374`; límite superior unilateral 90 % de precisión `4,136704 %`; `AB=1,500000 %`; `AS=0,577350 %`; `t₀,₉₅;₃=2,353363`; límite superior unilateral 95 % del sesgo absoluto `2,179358 %`; cambio de escala `d: 1,000000 % → 2,010000 %`; `s₀=0,158114 nmol/mol`; `3s₀=0,474342 nmol/mol` bajo las hipótesis explicitadas; serie agrupada `[0,5; 1,5; 2,5; 3,5] %`, medias de periodo `[1,0; 3,0] %`, SE iid `0,645497 %` frente a SE entre dos medias `1,000000 %`; componente común `0,800000 %` permanece al promediar dos u ocho valores. Todos coinciden con las cifras redondeadas del libreto.

### Referencias verificadas con `pdftotext`

| Clave y numeral citado | Archivo en `docs/` | Página PDF comprobada | Comprobación |
|---|---|---:|---|
| 40 CFR 58, Appendix A §2.3.1.2 | `Appendix A to Part 58_ Title 40 (up to date as of 10-20-2026).pdf` | 4 de 26 | Meta de límite superior 90 % para CV de O₃ y 95 % para sesgo absoluto; ambas metas de 7 %. |
| 40 CFR 58, Appendix A §3.1.1 | mismo archivo | 7 de 26 | Procedimiento de comprobación QC de un punto para monitores gaseosos. |
| 40 CFR 58, Appendix A §4.1.1 | mismo archivo | 18 de 26 | Definición de `dᵢ` como `(meas−audit)/audit × 100` y significado de los campos. |
| 40 CFR 58, Appendix A §4.1.2 | mismo archivo | 18–19 de 26 | Estimador de precisión como límite superior, cuantil chi-cuadrado y grados de libertad; fórmula visible en p. 19. |
| 40 CFR 58, Appendix A §4.1.3 | mismo archivo | 19 de 26 | Límite unilateral superior del sesgo absoluto con el cuantil t y definiciones de AB y AS. |
| 40 CFR 58, Appendix A §§4.1.3.1–4.1.3.2 | mismo archivo | 20 de 26 | Asignación del signo mediante percentiles 25 y 75 de las diferencias firmadas. |
| GUM §§5.2.1–5.2.2 | `ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf` | 29 PDF (p. impresa 21) | Validez de expresiones sin covarianza solo con entradas independientes/no correlacionadas y expresión general con covarianzas. |
| EN 14625 §3.12 | `BS EN 14625_2012.pdf` | 10 de 98 | Definición del límite de detección y relación `3,3·sᵣ,₀/B`. |
| EN 14625 Tabla 1 | mismo archivo | 19 de 98 | Criterios de repetibilidad en cero y en concentración de ensayo. |
| EN 14625 §8.4.5 y fórmula 5 | mismo archivo | 25 de 98 | Diseño de repetibilidad en cero y fórmula del límite de detección con desviación en cero y pendiente. |

Los numerales incluidos en el libreto se confirmaron directamente por extracción de texto; las ecuaciones escaneadas de 40 CFR y EN también se cotejaron visualmente en las páginas correspondientes. No se usaron numerales de `temario_curso.md` como evidencia.

### Decisiones y pendientes

- Se limitó el uso de los porcentajes-meta de 40 CFR al contexto de O₃ descrito por el propio apéndice; no se presentan como tolerancias universales ni como criterios de CALAIRE.
- Se incluyó la fórmula estadística de varianza del promedio con covarianzas para explicar la dependencia; se remitió a AX.2, mientras que AX.11 queda para las deducciones de límites de confianza.
- La escena de `3s₀` se presenta únicamente como umbral didáctico condicionado; se contrasta con la definición específica de EN 14625 y no se llama definición universal de límite de detección.
- Pendiente documental: `NIST/SEMATECH e-Handbook of Statistical Methods` no está disponible en `docs/`; se cita sin numeral como contexto de dependencia y debe verificarse su ubicación antes de una versión que requiera referencia puntual. Las afirmaciones centrales y las fórmulas de covarianza se respaldan además con GUM verificada.
- No se desarrollaron ejercicios, soluciones, evidencias evaluables ni rúbricas, de acuerdo con la fase actual.

## Correcciones (revisión Haiku)

| id del hallazgo | decisión | cambio hecho | ubicación | justificación |
|---|---|---|---|---|
| R01 | aplicado | Reescritas las expresiones de valor absoluto con `\lvert` y `\rvert` en LaTeX. | Libreto, ficha, fila Nivel B | Las barras quedan dentro del contenido de la celda y no pueden interpretarse como separadores de columnas Markdown. |
| R02 | aplicado con cambios | Pasadas variables, expresiones y resultados en prosa a notación matemática LaTeX; conservados en código solo los nombres de archivos/rutas. | Libreto completo | Cumple la convención de notación de la guía y hace consistente la escritura de subíndices y operaciones. |
| R03 | aplicado | Normalizada la clave a `CFR58-A` en las citas y en la bibliografía. | Libreto, narración y Referencias del capítulo | La clave coincide con la guía; el documento citado es el apéndice A de 40 CFR Part 58. |
| R04 | aplicado con cambios | Añadida cita a Crowder 2020 sin numeral para la estimación muestral y el intervalo t, más remisión a AX.1/AX.11; queda explícito en bibliografía que el numeral/datos editoriales requieren verificación. Para chi-cuadrado se conserva CFR58-A §4.1.2, que especifica el límite usado. | Libreto, escenas I1–I2 y Referencias | No se inventa un numeral. El PDF de Crowder no permitió extracción fiable en esta sesión (errores de XRef); por eso la referencia queda marcada como pendiente y no se afirma haber verificado un capítulo/página. |
| R05 | aplicado | Incorporadas señales explícitas sobre pocas verificaciones/grados de libertad, proximidad a criterio, cambio de escala/ganancia, dependencia temporal, atípicos sin causa, residuos estructurados e incertidumbre relevante en ambos ejes. | Libreto, Señales de escalamiento B | Cubre las señales indicadas en la revisión y ayuda a no trasladar supuestos de independencia o comparabilidad. |
| R06 | aplicado | Corregida la explicación de la fórmula y su lectura oral: la desviación muestral se multiplica por la raíz del cociente entre $n−1$ y el cuantil. | Libreto, escena I1 | Describe correctamente $s_d\sqrt{(n−1)/\chi^2}$; la raíz afecta al cociente completo. |
| R07 | aplicado | Añadidas remisiones a AX.1 para el divisor $n−1$ y a AX.11 para la deducción de límites. | Libreto, escena I1 | Los anexos contienen respectivamente el divisor/grados de libertad y los límites de confianza. |
| R08 | aplicado | Convertido $\mu_d$ a LaTeX y homogeneizado el signo menos de los datos del cero a `−`. | Libreto, escenas I2 e I4 | Distingue correctamente el signo matemático y mantiene la convención tipográfica del curso. |
| R09 | aplicado con cambios | Acortados y separados en ideas los párrafos de B2 y A1; aclarado el referente al distinguir el indicador agregado del certificado. | Libreto, escenas B2, B2 final y A1 | Mejora el ritmo oral y elimina la ambigüedad de «la primera». |
| R10 | aplicado | Sustituido «añadiremos incertidumbre a los indicadores» por «añadiremos límites de confianza a los indicadores». | Libreto, transición B→I | Evita equiparar la incertidumbre estadística del indicador con la incertidumbre de calibración. |

Correcciones adicionales por iniciativa propia:

- Corregida la remisión de la nota de A1 de AX.11 a AX.2: la fórmula de varianza con covarianzas se deduce en AX.2; AX.11 corresponde a límites de confianza.
- Reescrita la explicación larga del procedimiento de signo y sesgo absoluto en B2/I2 en frases más cortas, sin cambiar el contenido técnico.
- Normalizada la clave `CFR58-A` también en la ficha y la cita de la comparación de criterios.
- No se modificó el script: la revisión no detectó discrepancias numéricas y los cambios aplicados son de forma, referencias, explicación y cobertura de escalamiento.
