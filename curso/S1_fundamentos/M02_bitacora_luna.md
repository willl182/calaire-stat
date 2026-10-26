# Bitácora M02 — claude-luna

## Plan

### Alcance curricular por nivel (transcripción de prop_e §5, M2)

**Competencia estadística:** elegir la variable que responde a la pregunta y describir su centro, dispersión y estructura sin perder información.

- **B:** media, mediana, varianza, desviación estándar, rango, cuantiles; histograma, caja y serie temporal; dispersión de lecturas frente a error estándar; coeficiente de variación (CV) y su límite cerca de cero; detección gráfica de valores inusuales sin eliminación automática; redondeo al final.
  - *Práctica:* comparar la dispersión de indicaciones brutas y de errores `e` en un nivel medido durante varios días; explicar cuánto de la variación proviene del cambio de la referencia. Conservar los negativos del cero.
- **I añade:** resúmenes dentro y entre grupos; mediana y desviación absoluta mediana (MAD); modelo `eᵢ = a + (b − 1)·xᵢ + εᵢ`; el error predicho `ê(x) = â + (b̂ − 1)·x` muestra tendencia con `x` si hay sesgo proporcional.
  - *Práctica:* elegir la respuesta para una pregunta de precisión y otra de calibración con gráficos frente a referencia y tiempo.
- **A añade:** sensibilidad de las conclusiones a transformaciones, agregaciones y observaciones influyentes.
  - *Práctica:* en un ejemplo con sesgos opuestos (caso R&R: repetibilidad y reproducibilidad), evaluar cómo cambian las conclusiones del análisis al usar `e` o `|e|` y qué información pierde cada resumen. El cálculo básico `media(|e|)` frente a `|media(e)|` corresponde a M12-B y al caso D-B.

### Escenas previstas

- Apertura/ficha: pregunta estadística, elección previa de respuesta, niveles acumulativos y rótulos de origen.
- B1: elección entre indicación, error y promedio; conservación del emparejamiento y de la estructura de los datos.
- B2: distribución de frecuencias, histograma, cuantiles y caja; ejemplo numérico de ocho lecturas.
- B3: media/mediana, varianza/desviación estándar/rango y error estándar; ejemplo de un día y recordatorio de AX.1 sin deducción.
- B4: lecturas brutas frente a errores con signo y referencias que varían entre días; cero negativo, CV y límite cerca de cero.
- B5: serie temporal, detección visual de valores inusuales, conservación, cifras y redondeo.
- Marcador de práctica B, sin enunciado ni desarrollo; señales de escalamiento de B.
- I1: resúmenes dentro/entre grupos con emparejamiento por día; mediana y MAD; gráficos contra referencia y tiempo.
- I2: modelo lineal del error `eᵢ = a +(b−1)xᵢ+εᵢ` y ejemplo de sesgo proporcional con predicción narrada.
- Marcador de práctica I, sin desarrollo.
- A1: sensibilidad de conclusiones a `e` frente a `|e|`, agregación por grupos y observación influyente; ejemplo didáctico rotulado y límites de interpretación.
- Marcador de práctica A, sin desarrollo.
- Cierre y referencias del capítulo.

### Datos y rótulo de origen

Los ejemplos ilustrativos se diseñarán como conjuntos pequeños expresamente **simulados** para docencia, no extraídos de datos de CALAIRE: (1) ocho indicaciones y errores emparejados de un día en un nivel; (2) seis pares distribuidos en tres días con referencias ligeramente distintas y un punto de cero con lectura negativa; (3) niveles de referencia y errores para mostrar tendencia proporcional; (4) errores con signo de varios grupos y un valor influyente para el análisis A. En cada escena se declarará el rótulo y que los números no describen el desempeño del laboratorio. No se usarán valores de los Excel como si fueran simulados ni se atribuirán los ejemplos a CALAIRE.

### Cálculos previstos

Todos los resultados numéricos que aparezcan en el libreto se generarán o comprobarán con `curso/.venv/bin/python` y scripts guardados en `curso/S1_fundamentos/calc/M02_*.py`. Se prevén cálculos reproducibles para media, mediana, varianza muestral, desviación estándar, rango, cuantiles, MAD, CV cuando sea interpretable, error estándar, media de errores por día, descomposición descriptiva de la variación bruta y error, parámetros/predicciones del modelo descriptivo del error, y comparaciones de `media(e)` con `media(|e|)` ante agregación y observación influyente. Se citará el nombre del script junto al resultado en esta bitácora.

### Referencias a verificar con `pdftotext`

- `Statistical Concepts` c02–c03 y `Introduction to Statistics in Metrology` c04: frecuencias, histogramas, cuantiles, centro, dispersión, caja y análisis exploratorio.
- `Statistical Concepts` c05: error estándar de la media.
- `Metrology and Measurement Uncertainty` c03: redondeo, solo si se emplea numeral en el capítulo.
- Ubicación documental de CV y MAD: comprobar; si no aparece numeral verificable, citar la fuente sin numeral y registrar el pendiente.
- Certificado F-PSMT-01 solo si se alude a su diseño de 8 lecturas por punto y día; el capítulo priorizará los ejemplos simulados y evitará adjudicarle estadísticos calculados.

Cada numeral se mantendrá únicamente después de localizarlo en el PDF convertido a texto y anotar el archivo y la página física del PDF. Si no se puede comprobar numeral/página, se citará la referencia sin numeral y se registrará como pendiente. Los anexos que se anticipan son **AX.1** para la razón del divisor `n−1` en la varianza muestral; no se desarrollará ninguna deducción en el libreto.

## Ejecución

### Contenido escrito

Se escribió `M02_libreto.md` con ficha; escenas B1–B5; práctica B en marcador; señales de escalamiento; escenas I1–I2; práctica I en marcador; escena A1; práctica A en marcador; cierre y referencias. Las prácticas se dejaron exclusivamente como marcadores, sin enunciado, datos, soluciones, evidencias ni rúbricas. El libreto explica el alcance M2 de B, I y A, sin incluir temas del mapa inicial que prop_e no asigna a M2 (por ejemplo, población/muestra, escalas de medida, moda, puntuación z, asimetría/curtosis ni pruebas formales de atípicos). Se omitió el uso de datos del certificado y del R&R para no atribuir resultados didácticos a CALAIRE; todos los conjuntos didácticos se rotulan **simulados** y se construyen determinísticamente en el script, sin generador aleatorio.

### Scripts y resultados reproducibles

- `calc/M02_examples.py`, ejecutado con `curso/.venv/bin/python curso/S1_fundamentos/calc/M02_examples.py` (ejecución completada correctamente).
- Ocho lecturas simuladas: media y mediana 100,15 nmol/mol; varianza muestral 0,060000; desviación estándar 0,244949 nmol/mol; rango 0,700000 nmol/mol; cuartiles lineales 99,975 y 100,325; error estándar 0,086603 nmol/mol; frecuencias histogramáticas 2, 3, 3 y relativas 0,25, 0,375, 0,375; CV 0,244582 %.
- Seis pares simulados en tres días: $s(y)=154,266493$ nmol/mol y $s(e)=0,132916$ nmol/mol; errores 0,2; 0,1; −0,1; 0,1; 0,3; 0,1. Medias de error por día: 0,15; 0,00; 0,20; desviaciones estándar muestrales: 0,070711; 0,141421; 0,141421 nmol/mol. Lectura simulada del cero: −0,2 nmol/mol.
- Ejemplo MAD simulado: mediana 0,2; MAD 0,1 nmol/mol.
- Modelo descriptivo del error: intercepto 0,080000 nmol/mol, pendiente del error 0,002075, pendiente $b=1,002075$ y errores predichos 0,246; 0,412; 0,578; 0,744; 0,910 nmol/mol.
- Sesgos opuestos y sensibilidad: cada grupo tiene media firmada ±0,4 y media absoluta 0,4; al combinar, media firmada 0,0 frente a media absoluta 0,4. Al añadir el valor influyente simulado +1,8, media firmada 0,2; media absoluta 0,555556; desviación estándar muestral 0,724569; mediana 0,3; MAD 0,6 nmol/mol. Sin ese valor, desviación estándar 0,434248, mediana 0,0 y MAD 0,4.

### Referencias verificadas con `pdftotext`

| Clave / numeral citado | Archivo comprobado | Página física del PDF y comprobación |
|---|---|---|
| Statistical Concepts §§2.1–2.2 (frecuencias e histograma) | `docs/statistical_concepts_c02.pdf` | PDF pp. 2–3: texto de frecuencias y subsecciones del histograma; pp. 1–2 incluyen el índice. |
| Statistical Concepts §2.3 (percentiles, cuartiles, caja) | `docs/statistical_concepts_c02.pdf` | PDF pp. 4–5: texto de percentiles y subsección de box-and-whisker; numeral visible también en el índice, p. 1. |
| Statistical Concepts §§3.2.2–3.2.3 (mediana, media); §3.3 (dispersión) | `docs/statistical_concepts_c03.pdf` | PDF pp. 3–5: apartados de centro, rango y medidas de dispersión; índice en p. 1. |
| Statistical Concepts §5.2 (error estándar de la media) | `docs/statistical_concepts_c05.pdf` | PDF pp. 2–3: apartado de muestreo/estimación y mención de standard error of the mean; índice, p. 1. |
| Introduction to Statistics in Metrology §4.3 (análisis exploratorio, tendencias y valores potencialmente atípicos) | `docs/intro_stats_metro_c04.pdf` | PDF pp. 2–5: encabezado §4.3, tendencias/valores inusuales, histogramas y boxplots; el propio libro señala las páginas impresas 60–63. |
| Metrology and Measurement Uncertainty §3.1.1 (redondeo) | `docs/metrology_measure_uncer_c03.pdf` | PDF p. 2: título §3.1.1 y reglas de redondeo; índice en p. 1. |

No se asignó numeral no comprobado. La definición de CV se cita a nivel de capítulo sin numeral porque la búsqueda en los PDFs consultados no confirmó ubicación específica. La MAD también se cita sin numeral y queda pendiente verificar ubicación teórica específica. El modelo del error y el alcance por nivel se citan a `prop_e §5, M2` como fuente curricular. No se necesitó citar ISO 5725 ni el certificado.

### Decisiones y pendientes

Se corrigió el plan de escenas para que B1 se limite a elegir variables, sin enseñar conceptos estadísticos que prop_e no asigna al módulo. El ejemplo del error contiene niveles de referencia distintos deliberadamente: sirve para enseñar que la dispersión de $y$ no es la dispersión de $e$, no para estimar precisión del instrumento. Los cuantiles se calcularon con interpolación lineal explícita en el script. La MAD se presenta sin factor de escala y no se convierte en desviación estándar. El modelo de error se presenta como descripción ilustrativa, no como validación de ajuste.

Pendiente para la siguiente revisión: verificar en una referencia disponible la ubicación precisa de CV y MAD; revisar el libreto contra los requisitos de redacción y cobertura curricular. No se desarrollaron prácticas por instrucción de fase actual.

## Correcciones (revisión Haiku)

| Id del hallazgo | Decisión | Cambio hecho | Ubicación | Justificación |
|---|---|---|---|---|
| R01 | aplicado con cambios | Se cambió la afirmación general de numerales «comprobados» por una lista de numerales localizados; CV y MAD quedaron explícitamente sin numeral. | `M02_libreto.md`, ficha, línea «Referencias clave» | Evita atribuir verificación a CV/MAD y refleja los numerales realmente presentes en los PDF (guía del libreto §5; hallazgos R02–R07). |
| R02 | aplicado con cambios | Se quitó la nota de trabajo de la narración y se citó ASQ sin numeral; se añadió ficha bibliográfica del manual y quedó pendiente ubicar capítulo/numeral. | `M02_libreto.md`, B4, CV; referencias del capítulo | La búsqueda no localizó el término en *Statistical Concepts*; ASQ contiene la definición, pero la ubicación precisa no quedó comprobada, por lo que no se inventa un numeral. |
| R03 | aplicado | Se retiró la atribución a Crowder y la nota de pendiente de la narración; se citó NIST/SEMATECH sin numeral, marcado no disponible en `docs/`. | `M02_libreto.md`, I1, definición de MAD y referencias | Crowder no contiene MAD según la búsqueda de la revisión; la fuente externa se cita sin numeral, conforme a la guía §5. |
| R04 | aplicado con cambios | Se eliminó la cita a Crowder y se añadió un ejemplo numérico simulado: media de cinco indicaciones con signo ≈0 y media tras truncar dos negativos =0,06 nmol/mol. Se incorporó el cálculo al script. | `M02_libreto.md`, B4, lectura negativa; `calc/M02_examples.py` | Crowder §4.3 trata análisis exploratorio, no truncamiento. La comparación es aritmética reproducible y no se atribuye a una fuente que no la respalda. |
| R05 | aplicado | Se añadió GUM 4.2.3, ec. (5), para la varianza de la media, y se conservó Hahs-Vaughn §5.2 solo para muestreo/estimación. Se lee la fórmula en voz alta. | `M02_libreto.md`, B3, error estándar; referencias | La ecuación (5) de GUM da $s^2(\bar q)=s^2(q_k)/n$; §5.2 de Hahs-Vaughn no contiene la fórmula. |
| R06 | aplicado con cambios | Se quitó Crowder §4.3 de las cifras de influencia y se añadió una cita sin numeral a NIST/SEMATECH para la definición de influencia. | `M02_libreto.md`, A1, valor influyente y definición | La revisión confirmó que Crowder no define influencia; se usa una fuente externa sin numeral no verificado y las cifras se mantienen como aritmética del ejemplo. |
| R07 | aplicado | Se añadió ISO/TS 28037 §5 para la función de calibración lineal y §5.8 para OLS; `prop_e` se conserva solo como justificación curricular. | `M02_libreto.md`, I2, modelo y ajuste | Se verificó en el cuerpo del PDF la forma $Y=A+BX$ y la definición de OLS por minimización de suma de cuadrados en §5.8. |
| R08 | aplicado con cambios | Se citó VIM 2.16 para error de medida con signo y NIST/SEMATECH, sin numeral, para la magnitud/resúmenes absolutos; se quitó `prop_e` como respaldo técnico. | `M02_libreto.md`, A1, signo y magnitud | `prop_e` solo establece alcance curricular. VIM respalda el concepto metrológico de error; la transformación absoluta y sus resúmenes se atribuyen a fuente estadística externa sin numeral. |
| R09 | aplicado | Se agregó al libreto el ejemplo de promedio de los seis errores: 0,11667 nmol/mol sin redondeo intermedio frente a 0 tras redondear cada dato a enteros. Se agregó su cálculo al script. | `M02_libreto.md`, B5, redondeo; `calc/M02_examples.py` | Ejemplo reproducible que muestra numéricamente cómo el redondeo prematuro cambia el resultado; la salida del script coincide. |
| R10 | aplicado | Se corrigió la concordancia: «en uno los valores se concentran… y en el otro se distribuyen…». | `M02_libreto.md`, B3, ejemplo del rango | La construcción ahora mantiene sujeto y verbos concordantes. |
| R11 | aplicado | Se sustituyeron $z_i$ y $\bar z$ por $y_i$ y $\bar y$ y se nombró la varianza como $s_y^2$. | `M02_libreto.md`, B3, fórmula de varianza | La notación queda definida por la indicación $y$ usada en el capítulo. |
| R12 | aplicado | Se dividieron las frases largas sobre histograma/serie temporal y sensibilidad en frases más cortas. | `M02_libreto.md`, B5 y A1 | Mejora el ritmo oral requerido por la guía §1, sin cambiar el contenido. |
| R13 | aplicado | Se fusionaron las dos explicaciones del CV en un párrafo, manteniendo la pregunta sobre el denominador y la recomendación de reportar dispersión absoluta cerca de cero. | `M02_libreto.md`, B4, CV | Elimina la repetición de la inestabilidad del CV cerca de cero y conserva la regla operativa. |
| R14 | aplicado | Se normalizaron las citas narrativas a las claves de referencia: Hahs-Vaughn, Crowder 2020 y MMU. | `M02_libreto.md`, citas del capítulo | La guía §5 exige clave y ubicación; los nombres completos quedan en la lista bibliográfica. |
| R15 | aplicado | Se incorporó la lectura oral de $s/\sqrt n$ y de $\hat e(x)=\hat a+(\hat b-1)x$. | `M02_libreto.md`, B3 e I2 | La guía §4 requiere que las fórmulas se escriban y también se digan en palabras. |

### Correcciones adicionales por iniciativa propia

- Actualicé la bibliografía para quitar atribuciones pendientes incorrectas a *Statistical Concepts* (CV) y Crowder (MAD), y añadí las referencias completas usadas: ASQ, GUM, ISO 28037, VIM y NIST/SEMATECH. La ubicación exacta del CV dentro de ASQ queda pendiente; no se asignó un numeral no verificado.
- Recalculé `calc/M02_examples.py` con `curso/.venv/bin/python -I`. La comparación simulada de cero produce media ≈0 antes de truncar y 0,06 nmol/mol después; para los seis errores, las medias son 0,1166666667 y 0,0 nmol/mol, respectivamente. El resto de cifras revisadas no cambió.
- Retiré la cita de Crowder §4.3 de la aritmética del valor influyente; conservé esa cita en los párrafos de análisis exploratorio, tendencias y valores inusuales, que sí corresponden a §4.3.
- Verifiqué que las citas en la narración ya no usen títulos bibliográficos completos en lugar de claves y que no permanezcan notas de «ubicación específica pendiente» dentro de la exposición oral.
