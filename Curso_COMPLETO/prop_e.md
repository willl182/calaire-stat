# Propuesta E: curso de estadística aplicada a la fotometría de ozono

**Curso:** Estadística aplicada a la fotometría de ozono y a los patrones del laboratorio (SRP 55 y Level 2).  
**Fecha:** 24 de octubre de 2026.  
**Estado:** propuesta curricular nueva. No sustituye ni modifica las propuestas [A](prop_a.md), [B](prop_b.md), [C](prop_c.md) ni [D](prop_d,md).  
**Base:** [propuesta A](prop_a.md), con el alcance acotado de la [propuesta D](prop_d,md), las observaciones [obs1](obs1.md) y [obs2](obs2.md) y la supraobservación [sup_obs](sup_obs.md).

## 1. Enfoque

Es un **curso de estadística**. La fotometría de ozono, el SRP 55, el Level 2, la comparación BIPM.QM-K1 y el certificado F-PSMT-01 aportan los **datos y los casos**; no son el objeto del curso. La estadística define el temario, y el dominio del laboratorio define los ejemplos.

Reglas que siguen de ese enfoque:

1. **Cada objetivo se redacta como «competencia estadística + caso».** Ejemplo: «Estimar la incertidumbre de una diferencia entre resultados correlacionados (caso: Level 2 frente al SRP 55)».
2. **Los títulos de los módulos son estadísticos.** La física, los protocolos y los formatos entran solo en la medida en que el ejercicio los necesita para plantear los datos.
3. **Las conclusiones del curso son conclusiones estadísticas**: qué contrasta un estadístico, qué supuesto exige, qué se puede afirmar con los datos disponibles. Las conclusiones sobre el instrumento son la interpretación del caso, no el objetivo.
4. **Cada tema incluido en un nivel se enseña, se practica y se evalúa en clase en ese nivel.** Si un tema no se puede enseñar bien en un nivel, pasa al siguiente; no se deja como mención ni como ilustración.
5. **Prácticas de aplicación.** Calcular, decidir e interpretar con datos. Las deducciones van a anexos y no se evalúan.
6. **Los defectos de los archivos reales se usan para construir ejemplos preparados.** Localizar o reparar celdas no es una actividad de clase.

## 2. Niveles

Los niveles son acumulativos: I comprende B; A comprende B e I. Para entrar directamente en I o A se hace un ejercicio diagnóstico.

| Nivel | Perfil | Autonomía estadística |
|---|---|---|
| **Básico (B)** | Ejecuta la calibración con plantilla | Aplica un método definido, interpreta el resultado y reconoce cuándo un supuesto no se cumple |
| **Intermedio (I)** | Prepara y firma presupuestos y certificados | Elige el método, estima sus parámetros y justifica el modelo |
| **Avanzado (A)** | Responsable técnico (comparación BIPM, R&R, validación) | Formula modelos con covarianza general, los contrasta y valida las herramientas |

Aprobar el curso aporta evidencia de aprendizaje. La autorización para firmar o asumir una función técnica corresponde al laboratorio.

**Señales de escalamiento del básico.** El participante de B debe reconocer, con casos evaluados, cuándo detener el procedimiento: dependencia no contemplada, cambio de escala, atípico sin causa, residuos con estructura, incertidumbre relevante en ambos ejes, pocos grados de libertad o resultado próximo a un límite. Reconocer estas señales complementa el contenido básico; no lo sustituye.

## 3. Convenciones comunes

- `x`: valor de referencia; `y`: indicación; `e = y − x`: error con signo.
- Recta `y = a + b·x`; uso inverso `x̂ = (y − a)/b`; corrección aditiva `x̂ − y`.
- `u`: incertidumbre estándar; `U = k·u`: expandida. Para un intervalo bilateral central del 95 % con Student: `k = t(0,975; ν_eff)`.
- `s_r`: estimación de la desviación de lectura dentro del día (`σ`); `s_entre`: estimación de la desviación del efecto aleatorio de día, excluida la repetibilidad (`τ`); `n`: lecturas por día; `d`: días. No se usa `s_entre` para designar la desviación de los promedios diarios.
- Unidades: nmol/mol (equivalente a ppb en esta aplicación).
- Antes de calcular, cada ejercicio declara: respuesta, resultado de interés (lectura, promedio o uso futuro), unidad de repetición y escala temporal. Al cerrar, se entrega el resultado con unidades, interpretación estadística y acción.
- Cada conjunto de datos se rotula como propio, publicado, adaptado o simulado.

## 4. Secuencia

1. **M0–M4 — Fundamentos:** datos, modelo de medición, descripción, probabilidad e inferencia.
2. **M5–M8 — Modelos de la calibración:** diseño, componentes de varianza, regresión e incertidumbre.
3. **M9–M12 — Comparación, decisión y seguimiento:** compatibilidad, reglas de decisión, control estadístico e indicadores.
4. **M13 (solo A) y taller integrador por nivel.**

El orden M9 → M10 → M11 → M12 se mantiene por sus dependencias reales: M9 prepara el tratamiento de resultados correlacionados que se aplica a decisiones con dependencia en M10; M11 se apoya en la dependencia temporal de M3 y en regresión y propagación de M7–M8. M11 no presupone el cálculo de covarianza entre resultados de M9.

## 5. Módulos

### M0. Estructura de los datos y cálculo reproducible

**Competencia estadística:** organizar observaciones en una estructura de análisis que conserve el emparejamiento, el signo y los factores del diseño.

- **B:** tabla larga con identificadores de nivel, lectura, ciclo, día e instrumento; emparejamiento referencia–indicación; unidades; datos faltantes; lecturas negativas del cero; separación entre dato original y calculado.
  - *Práctica:* organizar un conjunto corto del Level 2, calcular `e`, detectar una pareja desplazada y un faltante, y documentar la corrección sin borrar el original.
- **I añade:** datos de varios días, analistas y campañas; comprobación de conteos y agrupaciones; paso de tablas anchas a largas; registro de exclusiones justificadas.
  - *Práctica:* reconstruir los resúmenes diarios de una campaña desde las parejas originales.
- **A añade:** especificación de entradas, salidas y comprobaciones de un cálculo reproducible; contraste entre dos herramientas.
  - *Práctica:* reproducir un resultado con una segunda herramienta y explicar las discrepancias.

### M1. Modelo de medición y variables de análisis

**Competencia estadística:** expresar un resultado como función de sus entradas, identificar la variable de análisis y evaluar numéricamente cómo cambia el resultado cuando cambia una entrada (sensibilidad).

- **B:** mensurando, error, sesgo, corrección; modelo de medición como función `Y = f(X₁, …, X_N)`; sensibilidad numérica en plantilla. Caso: ecuación del SRP con entradas suministradas y conversión explícita a nmol/mol.
  - *Práctica:* recalcular tres concentraciones con dos valores de sección eficaz declarados e indicar el signo y la magnitud relativa del cambio.
- **I añade:** cambio de escala como cambio de un parámetro del modelo: efecto sobre `e` y sobre un error relativo con denominador definido; diferencia entre cambiar la escala y corregir un instrumento.
  - *Práctica:* comparar dos mediciones en escalas distintas usando el cociente de los valores realmente implementados (los pares 1,147/1,1329 y 308,32/304,39 dan incrementos distintos; el ejercicio declara cuál usa).
- **A añade:** entradas comunes a dos resultados y su efecto en una diferencia frente a un resultado absoluto (prepara la covarianza de M8 y M9).
  - *Práctica:* identificar qué contribuciones se cancelan en una diferencia entre dos fotómetros y cuáles permanecen en el resultado declarado.

### M2. Estadística descriptiva y elección de la respuesta

**Competencia estadística:** elegir la variable que responde a la pregunta y describir su centro, dispersión y estructura sin perder información.

- **B:** media, mediana, varianza, desviación estándar, rango, cuantiles; histograma, caja y serie temporal; dispersión de lecturas frente a error estándar; coeficiente de variación (CV) y su límite cerca de cero; detección gráfica de valores inusuales sin eliminación automática; redondeo al final.
  - *Práctica:* comparar la dispersión de indicaciones brutas y de errores `e` en un nivel medido durante varios días; explicar cuánto de la variación proviene del cambio de la referencia. Conservar los negativos del cero.
- **I añade:** resúmenes dentro y entre grupos; mediana y desviación absoluta mediana (MAD); modelo `eᵢ = a + (b − 1)·xᵢ + εᵢ`; el error predicho `ê(x) = â + (b̂ − 1)·x` muestra tendencia con `x` si hay sesgo proporcional.
  - *Práctica:* elegir la respuesta para una pregunta de precisión y otra de calibración con gráficos frente a referencia y tiempo.
- **A añade:** sensibilidad de las conclusiones a transformaciones, agregaciones y observaciones influyentes.
  - *Práctica:* en un ejemplo con sesgos opuestos (caso R&R: repetibilidad y reproducibilidad), evaluar cómo cambian las conclusiones del análisis al usar `e` o `|e|` y qué información pierde cada resumen. El cálculo básico `media(|e|)` frente a `|media(e)|` corresponde a M12-B y al caso D-B.

### M3. Probabilidad, distribuciones y dependencia

**Competencia estadística:** asignar distribuciones a entradas, convertir especificaciones en incertidumbres estándar y saber cuándo promediar reduce la incertidumbre.

- **B:** variable aleatoria; normal, rectangular y triangular; semiamplitud `h` frente a resolución total `δ` (`h/√3`, `δ/√12`); `u = U/k`; desviación de lecturas frente a desviación de un promedio; distribución t, cuantiles y grados de libertad (prerrequisito de M4-B). La reducción con `1/√n` tiene límite cuando hay un componente común o deriva.
  - *Práctica:* convertir especificaciones del certificado en incertidumbres estándar y comparar el promedio de datos independientes con el de una serie con deriva.
- **I añade:** covarianza y correlación; varianza de combinaciones lineales; distribuciones chi-cuadrado y F (prerrequisito de M4-I y M6-I); gráficos de probabilidad; dependencia temporal; separación entre variación de corto plazo y entre días.
  - *Práctica:* calcular la incertidumbre de una diferencia con y sin covarianza.
- **A añade:** covarianzas comunes entre canales y puntos; autocorrelación; manejo operativo de matrices y bloques de covarianza (unidades, simetría y admisibilidad), como prerrequisito para M7-A y M9-A.
  - *Práctica evaluable:* construir y comprobar una matriz pequeña de covarianza, verificar unidades, simetría y admisibilidad, y comparar estrategias de promediado en una serie con ruido y deriva.

### M4. Inferencia: estimación y contraste

**Competencia estadística:** estimar un efecto con su intervalo y contrastar hipótesis, distinguiendo significación estadística de relevancia metrológica.

- **B:** grados de libertad; intervalo de confianza con t; hipótesis, valor p y errores de decisión; prueba t de un error medio en un nivel, con la unidad de repetición justificada en el enunciado.
  - *Práctica:* calcular el intervalo del error medio del Level 2 en un nivel y contrastarlo con cero y con una magnitud relevante.
- **I añade:** t pareada y Welch; intervalos y pruebas sobre varianzas (chi-cuadrado, F); potencia y tamaño de muestra según el diseño (media, pareadas, dos grupos); incertidumbre de una desviación estimada; pruebas de Grubbs y Dixon solo bajo sus condiciones de aplicación.
  - *Práctica evaluable:* resolver un apartado distinto para cada familia: selección, cálculo e interpretación de t pareada y Welch; intervalo y contraste de varianzas con chi-cuadrado/F; cálculo de potencia o tamaño muestral para media, pares y dos grupos; incertidumbre de una desviación estimada; evaluación de los supuestos y conclusión de Grubbs y Dixon. La rúbrica registra método, supuestos, resultado e interpretación por apartado.
- **A añade:** multiplicidad; pruebas de equivalencia con márgenes definidos; consistencia por chi-cuadrado.
  - *Práctica:* un caso donde «no rechazar cero» y «demostrar equivalencia» llevan a conclusiones distintas.

Ocho lecturas consecutivas no son ocho réplicas independientes sin justificación; no se mezclan concentraciones en una única prueba t pareada.

### M5. Diseño de experimentos

**Competencia estadística:** relacionar lo que se quiere estimar con lo que varía en el experimento: factores, réplicas, bloques, estructuras cruzadas y anidadas.

- **B:** factor, nivel, bloque, réplica; lectura, ciclo, día; observación dependiente frente a repetición independiente.
  - *Práctica:* representar el diseño 12 puntos × 8 lecturas × 6 días de la calibración del Level 2 e identificar qué variación se observa, qué queda confundido y qué datos harían falta para separarla.
- **I añade:** aleatorización, bloqueo, factoriales y robustez; distribución del esfuerzo entre niveles, ciclos y días; relación con potencia.
  - *Práctica:* diseñar un factorial de robustez con respuesta, factores, orden y criterio definidos.
- **A añade:** diseños anidados escalonados; diseño de un estudio de repetibilidad y reproducibilidad (R&R); comparación de diseños por componentes identificables.
  - *Práctica evaluable:* proponer un estudio que separe lectura, ciclo, día y analista; identificar efectos fijos y aleatorios, unidad de réplica, interacciones y denominadores; explicar qué gana al añadir analistas frente a añadir lecturas.

### M6. ANOVA y componentes de varianza

**Competencia estadística:** separar fuentes de variación y usar cada componente según el resultado que se reporta.

- **B:** repetibilidad y precisión intermedia. Se entregan `s_r` y `s_entre` ya calculadas como estimaciones de `σ` y `τ` del modelo equilibrado `e_dj = μ + D_d + ε_dj`, donde los efectos de día `D_d` son independientes, de varianza `τ²`, y los errores de lectura `ε_dj` son independientes, de varianza `σ²`, e independientes de los efectos de día. Con `n` lecturas en cada uno de `d` días, el participante interpreta cada componente y calcula la contribución de precisión al promedio de errores:

  `u²_prec(ē) = s²_entre/d + s²_r/(d·n)`  (con `s_entre = τ̂` y `s_r = σ̂`)

  No ejecuta el ANOVA ni aplica un divisor automático. Si se entregan desviaciones de promedios diarios, se identifican como tales y, bajo el mismo modelo, se usa `s²_medias/d` sin volver a sumar repetibilidad. La fórmula requiere diseño equilibrado y los supuestos indicados; dependencia, desequilibrio o confusión entre día y ciclo exigen revisar el modelo. Las demás contribuciones del presupuesto se incorporan en M8.
  - *Práctica:* calcular la contribución expandida de precisión del promedio, `U_prec = k·u_prec(ē)` con el `k` que declara el ejercicio, con y sin la componente entre días; interpretar la diferencia y explicar por qué corresponde incluirla. Es una U parcial: el presupuesto completo del promedio se construye en M8.
- **I añade:** ANOVA de un factor aleatorio (sumas de cuadrados, grados de libertad, cuadrados medios, F); estimación de componentes y su incertidumbre; efectos fijos y aleatorios; dos factores e interacción; residuos y heterogeneidad (Cochran); ISO 5725 cuando el diseño corresponda.
  - *Práctica:* ejecutar el ANOVA de días en un nivel del Level 2 con errores con signo, estimar las componentes y justificar el modelo.
- **A añade:** analista × campaña con días anidados; elección de denominadores; componentes negativas y alternativas de estimación; aplicabilidad de ISO 5725, incluido el sesgo de un laboratorio.
  - *Práctica:* analizar el caso R&R con errores con signo; comparar modelos admisibles y justificar conclusiones considerando interacción y multiplicidad.

### M7. Regresión y calibración inversa

**Competencia estadística:** ajustar un modelo de calibración, diagnosticarlo y usarlo en sentido inverso con su incertidumbre.

- **B:** mínimos cuadrados ordinarios (OLS) con intercepto en un caso con condiciones adecuadas; pendiente, intercepto, residuos; límites de R²; intervalo de uso; `x̂ = (y − a)/b` frente a la corrección `x̂ − y`.
  - *Práctica:* ajustar la recta de un conjunto del Level 2, revisar residuos y comprobar el signo de la corrección.
- **I añade:** incertidumbres y covarianza de `a` y `b`; bandas de confianza y predicción; incertidumbre de la predicción inversa; origen forzado; mínimos cuadrados ponderados (WLS) y elección de pesos. La ficha de decisión indica cuándo la incertidumbre del eje de referencia es relevante: si lo es, I detiene el ajuste con `x` fijo y escala el caso a A. **Falta de ajuste:** la prueba convencional supone réplicas al mismo valor de referencia; si la referencia cambia entre repeticiones (caso: F-PSMT-01, donde cambia entre días) no se aplica tal cual; hacen falta réplicas reales o un modelo que trate la variación de la referencia.
  - *Práctica:* comparar OLS y WLS, calcular la incertidumbre de un valor de uso y decidir si los datos permiten una prueba de falta de ajuste.
- **A añade:** regresión con incertidumbre en ambos ejes y **GGMR** (regresión generalizada de Gauss-Markov, ISO/TS 28037: ajuste que estima los parámetros y las abscisas ajustadas mediante una suma cuadrática generalizada basada en la matriz conjunta de covarianza de `x` e `y`; no es WLS ordinario con `x` fijo); diagnóstico por residuos ponderados y chi-cuadrado (valores altos y anormalmente bajos). El curso trabaja en el alcance validado de la herramienta disponible: covarianza cruzada entre ejes nula (`V_xy = 0`).
  - *Práctica evaluable:* ajustar el mismo conjunto por OLS, WLS y GGMR con igual orientación de ejes; explicar el efecto de una componente común y verificar la implementación dentro del alcance validado con un ejemplo de ISO/TS 28037.

No se fija automáticamente `ν = n − 2`. Los ceros inicial y final comparten nivel nominal pero pueden revelar deriva.

### M8. Propagación de incertidumbre

**Competencia estadística:** construir un presupuesto coherente con el resultado de interés y propagar varianzas y covarianzas.

- **B:** modelo de medición; evaluación tipo A y tipo B; `u = U/k`, resolución y tolerancias; elección entre `s` y `s/√n` según el resultado; presupuesto tabular con sensibilidades numéricas (Kragten) para entradas independientes; combinada y expandida; `k ≈ 2` solo donde el ejercicio lo justifica.
  - *Práctica:* presupuesto sencillo de un punto de calibración; explicar por qué dividir una dispersión de varios niveles y días por √576 no estima la incertidumbre buscada.
- **I añade:** sensibilidades analíticas; covarianzas; `ν_eff` y cobertura; resultado individual, promedio de calibración y resultado futuro; doble conteo entre residual de regresión y precisión; propagación por la cadena SRP 55 → Level 2 → cliente. En una práctica se selecciona y justifica la cobertura y los grados de libertad, incluida la adecuación y las limitaciones de Student y Welch–Satterthwaite. Este último se aplica de forma elemental solo a componentes independientes conforme al modelo; no se extiende mecánicamente a presupuestos correlacionados. Si el caso exige cobertura numérica no disponible en I, se escala a A. Un número pequeño de grados de libertad exige revisar la cobertura, no descarta por sí mismo una prueba t de media cuyos supuestos sí se cumplen.
  - *Práctica evaluable:* construir presupuestos para los tres resultados y trasladar al uso de un fotómetro de cliente; justificar la cobertura elegida, sus grados de libertad y sus límites.
- **A añade:** componentes comunes en resultados absolutos y diferencias; límites de la linealización; función de incertidumbre sobre un intervalo y su relación con la capacidad de medición y calibración (CMC; misma magnitud, unidades y cobertura).
  - *Práctica:* verificar punto a punto y en el intervalo una función de incertidumbre propuesta, incluido el máximo puntual entre U y CMC.

El presupuesto del SRP 27 no se presenta como presupuesto del SRP 55. No se impone una forma funcional.

### M9. Comparación de resultados: diferencias, covarianza y consistencia

**Competencia estadística:** estimar la incertidumbre de una diferencia entre resultados, con la covarianza que corresponda, y decidir qué hipótesis contrasta el indicador de compatibilidad.

- **B:** diferencia, incertidumbre de la diferencia bajo independencia justificada y `E_n` en un escenario que cumpla las condiciones de su fórmula. Para el ejercicio se define `E_n = Δ/√(U₁² + U₂²)`, con incertidumbres expandidas `U₁` y `U₂` calculadas con el mismo factor de cobertura `k`, y criterio `|E_n| ≤ 1`. Reconoce que compartir un patrón **no invalida `E_n` en general**, pero impide suponer independencia: no debe usarse sin justificación la fórmula que la asume, y se identifica cuándo hay que tratar la covarianza.
  - *Práctica evaluable:* calcular `Δ`, `u(Δ)`, `U₁`, `U₂` y `E_n` en dos puntos de un caso preparado e independiente, declarar cobertura y criterio y clasificar el resultado; ante un segundo caso (Level 2 frente al SRP 55), explicar por qué la cuadratura simple no está justificada y qué información de covarianza hace falta, sin calcularla.
- **I añade:** varianza de una diferencia con covarianza, `u²(Δ) = u²₁ + u²₂ − 2·cov(1,2)`; covarianza introducida por un patrón compartido; interpolación con una recta y la covarianza de sus parámetros; compatibilidad frente a conformidad. Para normalizar la diferencia se calcula `U(Δ) = k_Δ·u(Δ)` y se declara la cobertura; si se usa `Δ/U(Δ)` como extensión de `E_n`, se identifica expresamente y no se confunde con la definición de B. Con un mismo `k`, `U²(Δ) = k²[u₁² + u₂² − 2·cov(1,2)]`; el término de covarianza expandido es `−2·k²·cov(1,2)`.
  - *Práctica evaluable:* estimar `u(Δ)` incluyendo la covarianza del SRP 55 compartido, calcular `U(Δ)` con cobertura declarada y explicar que el resultado evalúa la compatibilidad estadística entre resultados bajo el modelo de dependencia adoptado; **no constituye una verificación independiente del instrumento**.
- **A añade:**
  - Matrices de covarianza y GGMR aplicado a una comparación, dentro del alcance `V_xy = 0` (ver M7-A); consistencia por chi-cuadrado.
  - **Grado de equivalencia** frente a una referencia común: diferencia `D` respecto al valor de referencia clave (KCRV) y su incertidumbre. Caso docente: BIPM.QM-K1, donde el BIPM-SRP27 es la referencia común.
  - El caso SRP 36/SRP 7 es una adaptación didáctica para interpolación. No se estudian el protocolo, la organización de la comparación ni la base de datos de comparaciones clave (KCDB).
  - *Práctica evaluable:* resolver la comparación con referencia común con herramienta contrastada e informar `D` y `u(D)` (o la incertidumbre expandida declarada), separados de cualquier indicador normalizado; analizar la sensibilidad a las hipótesis de covarianza.

El caso B (SRP 36/SRP 7) es una adaptación didáctica; no se presenta como resultado oficial de CALAIRE. Un resultado de comparación es evidencia para evaluar una CMC, no su aprobación.

### M10. Reglas de decisión y riesgo

**Competencia estadística:** aplicar y elegir reglas de decisión con incertidumbre y cuantificar el riesgo de falsa aceptación y falso rechazo.

- **B:** resultado, U, k, intervalo y función de uso; regla de decisión suministrada; banda de guarda; acción en la zona próxima al límite.
  - *Práctica:* completar un certificado docente y resolver resultados dentro, cerca y fuera del límite.
- **I añade:** selección y justificación de reglas; riesgo de falsa aceptación y rechazo; relación incertidumbre–tolerancia; coherencia entre presupuesto y declaración.
  - *Práctica:* resolver un resultado próximo al límite con dos reglas y explicar el riesgo que asume cada una.
- **A añade:** riesgo específico y global con modelos explícitos; requisitos bilaterales; decisiones con dependencia.
  - *Práctica:* cuantificar el riesgo de una decisión para una distribución y una especificación definidas.

Los criterios externos se reúnen en una ficha común que usan M10, M11, M12 y el caso C. La ficha identifica equipo o proceso, documento y edición, etapa, diseño, estadístico, divisor, unidades y fuente; distingue tolerancias, límites de control y criterios de indicadores.

### M11. Control estadístico y series temporales

**Competencia estadística:** detectar cambios en una serie, estimar deriva y decidir una acción con criterio de riesgo.

- **B:** causas comunes y especiales; carta de individuales y rango móvil con límites establecidos; límites de control frente a tolerancias; reglas de alarma y plan de acción.
  - *Práctica:* completar la carta de un historial preparado del Level 2 y decidir entre investigar, repetir, retener o recalibrar.
- **I añade:** construcción de línea base homogénea; dependencia; regresión de deriva; predicción e inclusión de la deriva en la incertidumbre de uso.
  - *Práctica evaluable:* con una serie docente homogénea, justificar inclusión/exclusión de observaciones en la línea base, estimar la deriva, evaluar su incertidumbre y predecir el efecto de prolongar el uso.
- **A añade:** EWMA y CUSUM; sensibilidad frente a falsas alarmas; intervalos de recalibración justificados.
  - *Práctica evaluable:* aplicar EWMA y CUSUM con parámetros declarados, comparar detección de un cambio definido y falsa alarma en un horizonte o longitud media de corrida, y proponer un intervalo de revisión bajo el modelo de riesgo especificado.

El historial publicado por el NIST sirve para aprender el método en su propia serie; no es la línea base del Level 2. Los seis días de una calibración no son un historial de largo plazo. El caso C requiere una serie docente homogénea rotulada, con fase estable, cambios, deriva y eventos de mantenimiento identificados; los datos disponibles no acreditan por sí solos las decisiones de seguimiento ni un intervalo real del Level 2.

### M12. Indicadores de precisión y sesgo a partir de diferencias relativas

**Competencia estadística:** calcular indicadores agregados de precisión y sesgo con sus límites de confianza y distinguirlos de la incertidumbre de una calibración. (Contexto: verificaciones de los clientes en redes de monitoreo.)

- **B:** diferencia relativa con referencia y signo definidos; `media(|d_i|)` frente a `|media(d_i)|`; porcentajes cerca de cero y métrica absoluta.
  - *Práctica:* calcular indicadores con errores de ambos signos en un escenario docente.
- **I añade:** límites de confianza con chi-cuadrado y t; unilateral frente a bilateral; efecto de un cambio de escala; dispersión del cero y umbral bajo hipótesis expresas (sin convertir `3·s₀` en definición universal de límite de detección).
  - *Práctica:* calcular indicadores y límites; repetir con un cambio de escala en un equipo e interpretar signo y denominador.
- **A añade:** dependencia y mezcla de periodos en una serie de verificaciones; efectos comunes de trazabilidad en resultados agregados.
  - *Práctica evaluable:* analizar una discrepancia entre la conformidad de un instrumento y el desempeño agregado y proponer la evidencia necesaria. El escenario define muestra, referencia, periodos, métrica agregada, cobertura y criterio; se separan expresamente la tolerancia, el límite de control y el umbral del indicador.

### M13. Métodos numéricos (solo A)

**Competencia estadística:** contrastar la propagación lineal con métodos numéricos y decidir cuál usar.

1. **Monte Carlo** (GUM S1): propagar distribuciones conservando dependencias y comparar con la linealización en una calibración inversa.
2. **Salidas múltiples** (GUM S2): obtener pendiente, intercepto y valores corregidos con su covarianza.
3. **Remuestreo:** bootstrap con la unidad de remuestreo que exige el diseño, respetando bloques o agrupaciones.
4. **Robustez:** regresión robusta de Huber como método definido, comparada con OLS ante una observación influyente; se explicitan sus supuestos y límites.

- *Práctica integradora evaluable:* resolver la propagación por linealización y Monte Carlo y comparar conclusiones; obtener parámetros y valores corregidos con matriz de covarianza; ejecutar bootstrap por la agrupación del diseño e interpretar el intervalo; comparar OLS y Huber y justificar qué estimación reportar. Cada apartado tiene resultado, supuestos y criterio en la rúbrica; si los datos o las soluciones de referencia no están preparados, el método no se imparte en este nivel.

## 6. Inclusiones y exclusiones

**Fuera del curso:** ensayos de aptitud, ISO 13528 e intercomparaciones entre laboratorios (z, ζ, Mandel); regresión por componentes principales (PCR) y mínimos cuadrados parciales (PLS), aprendizaje automático y quimiometría general; valores de diseño ambientales y promedios regulatorios; protocolo y organización de BIPM.QM-K1 y KCDB; varianza de Allan; GGMR con covarianza cruzada entre ejes no nula (`V_xy ≠ 0`); grado de equivalencia frente a un KCRV combinado al que contribuye el participante.

**Dentro:** comparaciones metrológicas entre patrones como problema estadístico de diferencias con covarianza: Level 2 frente al SRP 55 (I) y SRP 55 frente al BIPM, con grado de equivalencia frente a referencia común y GGMR con `V_xy = 0` (A).


## 7. Casos y taller integrador

Cuatro familias de casos con versiones por nivel. Para impartir cada práctica, su paquete debe incluir datos, diccionario, enunciado, plantilla, solución revisada y rúbrica. Los datos faltantes pueden suplirse con conjuntos simulados rotulados; esos resultados son didácticos y no describen el desempeño real del laboratorio. Los paquetes disponibles aún no acreditan que todas las prácticas estén listas.

| Caso | Competencias estadísticas | B | I | A |
|---|---|---|---|---|
| **A. Calibración del Level 2** | Descriptiva, componentes, regresión, propagación | Errores, U del promedio con componentes dadas, OLS, presupuesto | ANOVA, covarianza de parámetros, promedio frente a uso futuro, cliente | Modelos alternativos, función de incertidumbre |
| **B. Comparación de patrones** | Diferencias con covarianza, GGMR | Comparación directa con independencia justificada y `E_n` definido | Interpolación con covarianza; patrón compartido | GGMR dentro del alcance validado; grado de equivalencia y sensibilidad |
| **C. Seguimiento del patrón** | Control estadístico, deriva | Carta dada y acción con límites, señales y plan de acción definidos | Línea base homogénea y deriva en la incertidumbre | EWMA/CUSUM e intervalo de revisión bajo modelo de riesgo definido |
| **D. Precisión entre analistas** | Descriptiva con signo (B); ANOVA multifactor (I y A) | `media(|e|)` frente a `|media(e)|` en el bloque firmado disponible (concepto de M12-B) | Dos factores con datos firmados suficientes, recuperados o simulados | Analista × campaña con días anidados y lecturas intradía si se estima repetibilidad |

**Producto final por nivel:** informe con datos tratados, método, resultado, incertidumbre, interpretación estadística y acción.

## 8. Evaluación

Cada módulo cierra con una práctica de aplicación en clase y una evidencia evaluable. El expediente de cada tema registra: tema o método, nivel, prerrequisito, explicación docente, apartado de práctica, evidencia observable, datos rotulados, solución revisada y criterio de rúbrica. Una práctica integrada puede cubrir varios temas solo si cada uno tiene una pregunta y evidencia identificables; una mención o deducción en anexo no acredita enseñanza ni evaluación. La rúbrica evalúa datos y respuesta, método y supuestos, cálculo reproducible, interpretación y acción, y autonomía del nivel.

La cobertura mínima por nivel queda vinculada a las prácticas indicadas en cada módulo: M0 estructura y trazabilidad; M1 modelo y sensibilidad; M2 descripción y elección de respuesta; M3 distribuciones, conversión y dependencia; M4 estimación y contrastes; M5 diseño; M6 componentes; M7 ajuste y diagnóstico; M8 presupuesto y cobertura; M9 diferencia y compatibilidad; M10 decisión y riesgo; M11 seguimiento; M12 indicadores; M13, en A, Monte Carlo, salidas múltiples, bootstrap y robustez. Para cada contenido separado por punto y coma en un módulo, la solución docente y la rúbrica incluirán al menos una evidencia observable o justificarán explícitamente su agrupación con otro contenido. Los métodos que no cuenten con datos, solución revisada y criterio de evaluación antes del cierre no se incluyen en ese nivel; pasan al siguiente si corresponden o quedan fuera del curso. No se convierten en lecturas, demostraciones ni extensiones opcionales.

En B se evalúa un caso válido y otro con un supuesto incumplido; en I se elige entre métodos plausibles y se justifican límites; en A se contrasta el resultado con una referencia o segunda implementación dentro del alcance validado. Cada ejercicio declara el origen de los datos y no atribuye resultados simulados al laboratorio.

**Errores críticos** (exigen corrección y nueva resolución): confundir u y U; invertir el signo de una corrección; mezclar escalas; tratar observaciones dependientes como independientes sin modelo; suponer independencia entre resultados que comparten patrón; aplicar falta de ajuste sin réplicas válidas; extrapolar; eliminar datos para cumplir; usar límites de otro escenario; reportar un resultado didáctico como oficial.

## 9. Material y anexos

- **Fichas de método:** pregunta, entradas, supuestos, cálculo, ejemplo y señales de escalamiento.
- **Anexos:** deducciones de estimadores, cuadrados medios esperados, ecuaciones normales, propagación y formulación matricial (GGMR). No se evalúan.
- **Preparación pendiente antes de impartir:** unificar coeficientes y soluciones del caso B; preparar el paquete D-I/D-A con datos firmados y estructura documentada; completar escenarios de control y decisión de C; cerrar soluciones, datos y rúbricas tema por tema; completar la ficha común de criterios externos. Criterios verificables: una única solución reproducible por variante B; conjunto D con signos, fechas, unidad de réplica e intradía suficientes para lo que se evalúa; serie C homogénea con fase estable, deriva, cambios y mantenimiento identificados, además de parámetros y medida de riesgo para A; expediente de evaluación completo según §8. El paquete B no usa √576 como divisor automático: cada incertidumbre corresponde al resultado y modelo declarado.

## 10. Cierre del contenido

El contenido no se declara listo para impartirse mientras queden tareas de preparación de §9. Antes de cerrar el programa se verifica, con el expediente de §8, que cada tema incluido tiene nivel, prerrequisito, explicación, práctica, datos, solución revisada y evidencia evaluable y que los casos cuentan con paquetes viables. Las horas quedan fuera del alcance de esta propuesta.
