# Estadística aplicada a la fotometría de ozono con el SRP

**Propuesta de temario**, 22-10-2026. Versión web: `temario_curso.html`.

- **Público:** los operadores del SRP de CALAIRE, laboratorio designado por el INM. Este laboratorio compara su SRP contra el BIPM-SRP27 (BIPM.QM-K1), calibra los fotómetros y analizadores de ozono del país (certificados con CMC) y mantiene un patrón Level 2 para uso diario.
- **Duración:** 62 h de núcleo (12 módulos y taller final) más 4 h optativas.
- **Caso integrador:** calibración del Level 2 de CALAIRE (Thermo 49C, S/N 59756-324) contra el SRP 55, certificado F-PSMT-01: 12 puntos × 8 repeticiones × 6 días.
- **Niveles:** B básico · I intermedio · A avanzado.

## Cadena de trazabilidad y módulos que la cubren

| Eslabón | Papel | Módulos |
|---|---|---|
| BIPM-SRP27 | Referencia común de la comparación clave BIPM.QM-K1 | M9 |
| SRP 55 (NIST) | Patrón Nivel 1 de CALAIRE, laboratorio designado | M1 · M3 · M8 · M11 |
| Level 2: Thermo 49C | Patrón de uso diario; caso integrador del curso | M2–M8 · M11 |
| Fotómetros del país | Clientes calibrados con certificado y CMC | M7 · M8 · M10 |
| Redes de monitoreo | Uso del certificado en verificaciones y auditorías | M12 |

## Mapa del curso

El curso avanza con el trabajo del laboratorio y cada concepto estadístico aparece cuando la tarea lo necesita, apoyado en los anteriores. Primero se ve qué mide el SRP y cómo; con sus lecturas se aprende a describir datos, a modelar su variación con probabilidad y distribuciones (lo que explica el ruido del SRP) y a sacar conclusiones con pocas lecturas. Esa inferencia permite planear la comparación (diseño experimental), separar sus fuentes de variación (ANOVA), ajustar la recta (regresión) y expresar el resultado con su incertidumbre. Al final, todo se aplica a lo que solo hace el laboratorio designado: la comparación con el BIPM, la decisión y el certificado, el control diario de sus patrones y la relación con las redes. Cada módulo indica en qué módulos anteriores se apoya.

| Módulo | Tema | Nivel | Horas |
|---|---|---|---:|
| **I · Medición y tratamiento estadístico de las lecturas** | | | |
| M1 | Fundamentos de la fotometría UV de ozono y trazabilidad metrológica | B | 4 |
| M2 | Estadística descriptiva y análisis exploratorio de datos | B | 4 |
| M3 | Probabilidad, variables aleatorias y distribuciones | B–I | 5 |
| M4 | Inferencia estadística: estimación y contraste de hipótesis | I | 5 |
| **II · La calibración por comparación** | | | |
| M5 | Diseño de experimentos aplicado a la calibración por comparación | I | 5 |
| M6 | Análisis de varianza y evaluación de la precisión | I–A | 7 |
| M7 | Análisis de regresión y funciones de calibración | I | 5 |
| M8 | Evaluación de la incertidumbre de medida y capacidad de medición y calibración | I | 6 |
| **III · Diseminación de la trazabilidad** | | | |
| M9 | Comparaciones clave: mínimos cuadrados generalizados y grado de equivalencia | I–A | 4 |
| M10 | Evaluación de la conformidad y certificado de calibración | I | 3 |
| M11 | Control estadístico de procesos y aseguramiento de la validez de los patrones | I | 3 |
| M12 | Indicadores de precisión y sesgo en las redes de monitoreo | I | 3 |
| **Cierre** | | | |
| T | Taller integrador: casos reales del laboratorio | I–A | 8 |
| M13 | Temas avanzados (optativo) | A | 4 |
| | **Núcleo / con optativo** | | **62 / 66** |

---

# Bloque I · Medición y tratamiento estadístico de las lecturas

Qué mide el SRP y cómo, y la estadística que hace falta para entender sus lecturas: describirlas, modelar su variación como variable aleatoria y saber qué se puede concluir de unas pocas.

## M1. Fundamentos de la fotometría UV de ozono y trazabilidad metrológica (B, 4 h)

**Objetivo:** comprender el principio de medida del SRP, su ecuación de medida y la posición del laboratorio en la cadena de trazabilidad del ozono.

**Medición y trazabilidad**
- Mensurando: la fracción molar de O₃ en nmol/mol.
- Error, sesgo, corrección, exactitud, veracidad y precisión: el vocabulario que el resto del curso cuantifica.
- Calibración, verificación y ajuste: tres actos distintos.
- Trazabilidad metrológica: cadena documentada e ininterrumpida, con incertidumbre en cada eslabón.
- CIPM MRA, laboratorio designado y CMC publicadas en la KCDB.

**Cómo mide el SRP**
- Ley de Beer-Lambert; absorbancia natural frente a decimal.
- Ecuación de medida: `x = −R·T / (2·σ·L·N_A·P) · ln D`.
- Medida diferencial con dos celdas: `D = (f_11·f_22)/(f_21·f_12)` cancela la deriva común de la lámpara.
- Correcciones de temperatura y presión.
- La sección eficaz σ es parte del modelo y depende de la temperatura y de la longitud de onda.

**En el SRP**
- Cadena propia: BIPM-SRP27 → SRP 55 → Level 2 → fotómetros y analizadores del país; contraste con NIST → SRP de la EPA → Level 2/3 → estaciones.
- Línea de Hg de 253,7 nm, celdas de unos 89,5 cm, semiciclos de 5 s, rango 0–1000 nmol/mol.
- Sección eficaz: de 1,147 a 1,1329(35)×10⁻¹⁷ cm²/molécula (304,39 atm⁻¹ cm⁻¹) desde 2025. Los resultados suben un 1,25 %; con el par 308,32/304,39 sale 1,29 %. Siempre hay que declarar el valor y sus unidades.
- Cerca de 253,6 nm, σ baja alrededor de 1 % entre 218 y 295 K.

**Práctica**
- Dibujar la cadena del laboratorio con fechas, criterios e incertidumbre de cada eslabón.
- Recalcular 80, 420 y 500 nmol/mol con la sección eficaz antigua y la nueva.
- Comparar la dependencia térmica de σ en 210 nm, 253,6 nm y la banda de Huggins.

**Referencias:** Metrology and Measurement Uncertainty §§4.3–4.4 (error, sesgo, exactitud, precisión) · Intro. Statistics in Metrology caps. 2–3 · Metrology and Measurement Uncertainty §2.3.6 y cap. 7 · JCGM GUM-1 · NISTIR 6963 §§4–8 · NIST SRP 6008 pp. 1–2 · BIPM.QM-K1 §§1–1.1; Apéndice 1, ec. 8 · 40 CFR 50, Apéndice D §§2.2 y 4.1 · ISO 13964 §7.1 · Daumont et al. 1992 §§2–3, Tabla II · Malicet et al. 1995 §3, Tablas III–IV · Mark y Workman cap. 29 (ley de Beer) · SRP QAPP Elementos 4–6 y 10 · SRP SOP §§1.2–1.3 · EPA TAD §§2.1–2.9 · ISO/IEC 17025 §§6.4–6.5

## M2. Estadística descriptiva y análisis exploratorio de datos (B, 4 h)

**Objetivo:** resumir y representar un conjunto de lecturas con las medidas y gráficos adecuados, e identificar y tratar con criterio los valores atípicos.

**Se apoya en:** M1

**Teoría**
- Población y muestra; parámetro y estadístico.
- Tipos de variables y escalas de medida (nominal, ordinal, de intervalo y de razón).
- Notación de sumatoria.
- Distribución de frecuencias, histograma, percentiles, cuartiles y diagrama de caja.
- Tendencia central: media, mediana y moda, y cuándo usar cada una.
- Dispersión: rango, rango intercuartílico, varianza y desviación estándar muestral (por qué se divide por n − 1), coeficiente de variación, error estándar `s/√n`.
- Puntuación z, asimetría y curtosis.
- Cifras significativas y reglas de redondeo; redondear una sola vez, al final.
- Valores atípicos: un dato es atípico respecto de un modelo. Con n observaciones, `P = 1 − (1 − P_i)^n`. Pruebas de Grubbs (simple y doble), Dixon y Cochran; estadísticos h y k de Mandel. Ningún dato se elimina sin una causa documentada.

**En el SRP**
- BIPM: 10 lecturas por punto; el conjunto se acepta si s_SRP27 < 1 nmol/mol.
- Calibración del Level 2 (certificado F-PSMT-01): 8 réplicas por punto y por día, 48 lecturas por nivel.
- Las lecturas de cero negativas son ruido, no ozono físico: por qué no se truncan a cero.

**Práctica**
- Con las 48 lecturas de un nivel del certificado: tabla de frecuencias, histograma, diagrama de caja, media, mediana, s y CV.
- Con un día: media y s por punto, serie de lecturas y decisión sobre un extremo con una lista de verificación (cero, purga, estabilización, celda).

**Referencias:** Statistical Concepts §§1.3–1.5 (definiciones, variables, escalas) · Statistical Concepts §§2.1–2.3 (distribuciones, histograma, percentiles) · Statistical Concepts §§3.1–3.3 (sumatoria, tendencia central, dispersión) · Statistical Concepts §§4.2–4.3 (puntuación z, asimetría, curtosis) · Intro. Statistics in Metrology §4.3 (análisis exploratorio) · Metrology and Measurement Uncertainty §3.1 (cifras significativas, redondeo); §3.2.2 · Otto §2.2, Tablas 2.10–2.11 (Dixon, Grubbs) · ISO 5725 Parte 2: Cochran, Grubbs, Mandel y tablas · Mark y Workman caps. 119–121 (valores atípicos) · BIPM.QM-K1 §5 · NISTIR 6963 Tabla 2

## M3. Probabilidad, variables aleatorias y distribuciones (B–I, 5 h)

**Objetivo:** modelar la variabilidad de una medida mediante variables aleatorias y distribuciones de probabilidad, y aplicar las propiedades de la esperanza y la varianza al ruido del SRP.

**Se apoya en:** M1 · M2

**Teoría**
- Probabilidad: definición y reglas básicas.
- Variable aleatoria discreta y continua; función de densidad y función de distribución acumulada.
- Esperanza y varianza de una variable aleatoria.
- Reglas para combinaciones lineales: `E[aX + bY] = a·E[X] + b·E[Y]` y `Var(aX + bY) = a²·Var X + b²·Var Y + 2ab·Cov(X,Y)`. Es la base de la ley de propagación de M8.
- Covarianza y coeficiente de correlación.
- Distribuciones y su uso: normal y normal estándar; rectangular (`u = a/√3`; resolución `δ/√12`); triangular (`u = a/√6`); t de Student; chi-cuadrado; F.
- Estimar los parámetros de una distribución y evaluar el ajuste: histograma y gráfico de probabilidad normal.

**En el SRP**
- ¿Son normales las lecturas de un nivel? ¿Y las del cero?
- La resolución del analizador (0,1 nmol/mol) como variable rectangular.
- Ruido de conteo: la cuantización de ±0,5 cuentas es una variable rectangular, `0,5/√3` cuentas.
- Primera propagación con las reglas de la varianza: `u(x)/x = u(D)/|D·ln D|`. Con U(D) = 0,000017, U(x) ≈ 0,31 nmol/mol en todo el rango: 17 % a 1,8 nmol/mol y 0,06 % a 553 nmol/mol. El cero está limitado por la fotometría.
- Varianza de un promedio: promediar n lecturas reduce el ruido como 1/√n solo si son independientes; no reduce deriva ni sesgos.
- Covarianza en acción: la razón real entre canales tiene s = 0,000012, frente a 0,000089 si se supone independencia.
- Dos puntos medidos con el mismo patrón tienen covarianza: anticipo del término `u_b` del SRP27.

**Práctica**
- NISTIR 6963, Tabla 5: de D a x y U(x) en cinco niveles.
- NISTIR 6963, Tabla 2: nueve lecturas de cero con valores negativos. ¿Hay ozono negativo?
- Con las 48 lecturas de un nivel: histograma y gráfico de probabilidad normal.
- Deducir la desviación estándar de una distribución rectangular y comprobarla con números aleatorios.
- Verificar con datos simulados la regla de la varianza de una suma, con y sin covarianza.

**Referencias:** Statistical Concepts §4.1 (normal) · Statistical Concepts §5.1 (probabilidad) · Statistical Concepts §8.2 (chi-cuadrado) · Statistical Concepts §9.1.1 (distribución F) · Metrology and Measurement Uncertainty §§3.2.1–3.2.5 (variable aleatoria, densidad, media y s de una distribución, rectangular, triangular, normal, t) · Intro. Statistics in Metrology §4.4 (distribuciones, estimación de parámetros, ajuste) · Intro. Statistics in Metrology §7.2 y §7.4.1 (base matemática, covarianza y correlación) · Brereton apéndice A (distribuciones y tablas) · NISTIR 6963 §§8–11, Tablas 2, 3 y 5 · BIPM.QM-K1 Apéndice 1, ec. 11

## M4. Inferencia estadística: estimación y contraste de hipótesis (I, 5 h)

**Objetivo:** estimar parámetros y contrastar hipótesis sobre un instrumento a partir de una muestra de lecturas, cuantificando el riesgo de cada decisión.

**Se apoya en:** M2 · M3

**Teoría**
- Muestreo aleatorio; estimador y estadístico; sesgo y varianza de un estimador; grados de libertad.
- Distribución muestral de la media y teorema central del límite; error estándar.
- Intervalo de confianza para una media (normal y t) y su interpretación.
- Prueba de hipótesis: H_0 y H_1, estadístico de prueba, región crítica, nivel α y valor p.
- Errores tipo I y II, potencia y tamaño del efecto; tamaño de muestra (`n ≈ 15·(S/D)²` como regla rápida).
- Prueba t para una media; para dos medias independientes (incluida la versión de Welch) y para datos pareados.
- Pruebas sobre varianzas: una varianza (chi-cuadrado) y dos varianzas (F).
- Prueba chi-cuadrado de bondad de ajuste.
- Supuestos (independencia, normalidad) y cómo verificarlos.
- Significación estadística frente a relevancia metrológica; comparaciones múltiples.

**En el SRP**
- ¿El sesgo de un fotómetro en un nivel es distinto de cero?
- SRP y fotómetro midiendo el mismo gas: el caso natural de la prueba t pareada.
- ¿Cambió la dispersión del Level 2 de un año a otro? Prueba F.
- ¿Cuántas réplicas hacen falta para detectar 1 nmol/mol?

**Práctica**
- Intervalo de confianza al 95 % de la media de un nivel, con t.
- Prueba t pareada SRP frente a Level 2 en un día del certificado.
- Prueba F entre las varianzas de dos días; cálculo de potencia para un sesgo de 1 nmol/mol.

**Referencias:** Statistical Concepts §5.2 (muestreo, estimación, distribuciones muestrales) · Statistical Concepts §§6.1, 6.4 (una media: potencia, tamaño del efecto, supuestos) · Statistical Concepts §§7.1–7.2 (dos medias independientes y dependientes) · Statistical Concepts §§8.2–8.3 (chi-cuadrado) · Statistical Concepts §§9.1–9.3 (varianzas) · Metrology and Measurement Uncertainty §§3.2.5.5–3.2.5.9 (t de Student, efecto de N) · Intro. Statistics in Metrology §4.4.2 · Brereton apéndice A.3 (tablas t y F) · Mark y Workman cap. 15 (tamaño de muestra) · ASQ Metrology Handbook cap. 27

---

# Bloque II · La calibración por comparación

Con esa base se planea la comparación, se separan las fuentes de variación, se ajusta la recta y se expresa el resultado con su incertidumbre.

## M5. Diseño de experimentos aplicado a la calibración por comparación (I, 5 h)

**Objetivo:** planificar experimentos que permitan estimar los efectos de interés y separar las fuentes de variación, y aplicarlos a las comparaciones del laboratorio.

**Se apoya en:** M4

**Teoría**
- Respuesta, factores, niveles y unidad experimental.
- Aleatorización y bloques; el día como bloque.
- Replicación verdadera frente a pseudorreplicación: diez lecturas seguidas no son diez réplicas independientes.
- Diseños anidados (lecturas dentro de corridas, corridas dentro de días) y anidados escalonados para la precisión intermedia.
- Factorial completo (`N = ∏ n_i`; 2^k con k factores a dos niveles): efectos principales e interacciones.
- Un factor a la vez frente a un factorial; estudios de robustez.
- Potencia aplicada al diseño (M4): cuántas corridas para detectar un efecto dado.

**En el SRP**
- Robustez del SRP y del Level 2: flujo, tiempo de acondicionamiento, temperatura del laboratorio y calentamiento. Hoy esos efectos se suponen o se toman de la literatura.
- Los ensayos de sensibilidad de la EN 14625 son diseños de un factor a la vez: presión a 80 y 110 kPa, gas a 0 y 30 °C, tres mediciones por condición.
- Validación del Level 2 como método del laboratorio (ISO/IEC 17025 §7.2.2).
- ¿Cuántas corridas hacen falta para detectar un cambio de pendiente de 0,005 en el Level 2?

**Diseños reales de comparación que conviene contrastar**

| Documento | Diseño |
|---|---|
| BIPM.QM-K1 | 12 niveles: 0, 220, 80, 420, 120, 320, 30, 370, 170, 500, 270, 0 nmol/mol. 10 lecturas por punto. Estabilización ≥ 8 h; acondicionar ≥ 2 h con más de 500 nmol/mol. |
| SRP QAPP | 12 concentraciones con ceros, 10 lecturas, ≥ 3 ciclos. |
| SRP SOP | Igual, pero ≥ 6 ciclos. La diferencia con el QAPP se enseña tal cual. |
| EPA TAD (Level 2/3) | 3 ciclos, cada uno con cero y ≥ 6 concentraciones. |
| EN 14625 (linealidad) | ≥ 6 niveles, ≥ 5 lecturas, secuencia 80-40-0-60-20-95 %. |
| ISO 13964 | Cero y ≥ 5 concentraciones. |
| Calibración del Level 2 de CALAIRE (certificado F-PSMT-01) | 12 puntos × 8 repeticiones × 6 días. |

**Práctica**
- Diseñar un factorial 2³ de robustez del Level 2 (flujo, acondicionamiento, temperatura) con el día como bloque, y decir qué efectos e interacciones se podrán estimar.
- Identificar qué fuentes de variación puede separar cada diseño de la tabla y cuáles quedan confundidas.
- Analizar el diseño que usa hoy la calibración del Level 2 (12 × 8 × 6): qué fuentes separa, cuáles confunde y si los 6 días bastan para estimar la componente entre días.

**Referencias:** Intro. Statistics in Metrology §9.2 (experimentos factoriales en metrología) · Brereton cap. 2 (diseño experimental, factoriales) · Mark y Workman caps. 8–16 · ISO 5725 Parte 3: diseños anidados escalonados · EN 14625 §§8.4.6–8.4.8 · ISO/IEC 17025 §7.2.2 · BIPM.QM-K1 protocolo A §§3–7; protocolo B §§5–8 · SRP QAPP Elementos 6.2.1 y 7.1, Tabla 7-1 · SRP SOP §§9.7.19–9.7.20 · EPA TAD Tabla 4-1 · ISO 13964 §6.2 · NISTIR 6963 §§8–10 (independencia de los ciclos)

## M6. Análisis de varianza y evaluación de la precisión (I–A, 7 h)

**Objetivo:** descomponer la variabilidad mediante el análisis de varianza, estimar la repetibilidad, la precisión intermedia y sus componentes, y diseñar e interpretar estudios de repetibilidad y reproducibilidad.

**Se apoya en:** M4 · M5

**Teoría 1 · Modelo y descomposición de la variación**
- Modelo de un factor `y_ij = μ + τ_i + ε_ij`; supuestos: errores independientes, normales y de varianza común.
- Descomposición de sumas de cuadrados: `SS_total = SS_entre + SS_dentro`, con `a − 1` y `N − a` grados de libertad.
- Cuadrados medios y prueba `F = MS_entre/MS_dentro`: por qué el cociente sigue una distribución F cuando no hay efecto.
- Modelo de dos factores cruzados con interacción: `y_ijk = μ + A_i + D_j + (AD)_ij + ε_ijk`. Qué significa la interacción y cuándo hace falta réplica para estimarla.
- Diseño cruzado (todos los niveles de un factor con todos los del otro) frente a anidado (cada nivel de un factor aparece dentro de uno solo del otro, como lecturas dentro de ciclos y ciclos dentro de días).
- Revisión de supuestos con residuos; heterocedasticidad entre niveles de concentración y por qué obliga a analizar cada nivel por separado o a modelar la varianza.

**Teoría 2 · Efectos aleatorios y componentes de varianza**
- Efecto fijo (interesan esos niveles concretos) frente a efecto aleatorio (los niveles son una muestra de una población: días, analistas). Modelo mixto.
- Cuadrados medios esperados del modelo cruzado de efectos aleatorios con r réplicas: `E[MS_e] = σ_e²`; `E[MS_AD] = σ_e² + r·σ_AD²`; `E[MS_D] = σ_e² + r·σ_AD² + a·r·σ_D²`; `E[MS_A] = σ_e² + r·σ_AD² + d·r·σ_A²`.
- Estimadores por el método de los momentos: `σ̂_A² = (MS_A − MS_AD)/(d·r)` y análogos. Estimaciones negativas: qué significan y cómo se informan.
- La prueba correcta de un efecto aleatorio usa como denominador el cuadrado medio cuyo valor esperado coincide salvo por ese efecto: el analista se contrasta contra MS_AD, no contra MS_e.
- Cuadrados medios esperados en un diseño anidado; diseño anidado escalonado para estimar varias componentes con pocos ensayos.
- Grados de libertad de cada componente y de su combinación (Welch-Satterthwaite): una componente estimada con 1 o 2 grados de libertad es muy imprecisa, y solo mejora aumentando el número de niveles de ese factor.
- Réplica verdadera frente a pseudorréplica: las lecturas consecutivas de un mismo ciclo subestiman la repetibilidad.

**Teoría 3 · Precisión y estudios R&R**
- Modelo de la ISO 5725 `y = m + B + e`; repetibilidad s_r, reproducibilidad s_R y precisión intermedia con M factores (tiempo, operador, equipo, calibración): `s_I(T,O) = √(σ_e² + σ_T² + σ_O² + …)`.
- Límites `r = 2,8·s_r` y `R = 2,8·s_R`; veracidad frente a un valor de referencia.
- Estudio R&R como ANOVA de efectos aleatorios: repetibilidad = σ_e², reproducibilidad = σ_operador² + σ_interacción², R&R = suma de ambas.
- El %R&R y el número de categorías distintas comparan el R&R con la variación entre piezas. Cuando las "piezas" son niveles de concentración fijados por diseño, esa variación no es del proceso y esos índices pierden sentido: en calibración se usa el marco de la ISO 5725-3.
- Una prueba t entre dos operadores contrasta medias; no estima componentes de varianza. Un resultado no significativo con pocos operadores no demuestra que la reproducibilidad sea despreciable.
- Las componentes estimadas por ANOVA son evaluaciones tipo A que entran al presupuesto de incertidumbre (GUM, Anexo H.5); s_R solo cubre las fuentes que variaron en el estudio.

**En el SRP**
- Estudio R&R de CALAIRE 2022–2023: para cada nivel, el libro apila tres campañas de calibración del Level 2 (116/118 de enero de 2022, 142/143 de agosto de 2022 y 171/173 de febrero de 2023), cada una de 6 días, con un error medio por día. Cada analista hizo su propia calibración: los días están anidados en analista × campaña, y el "día 1" de un analista no es el del otro. Identificar esta estructura es el primer paso; una prueba t sobre las 18 cifras de cada analista la ignora.
- Analizado con el modelo analista × campaña con días anidados: no hay efecto medio del analista (F ≤ 1,24 frente a F_0,05; 1, 2 = 18,5, una prueba de muy poca potencia), pero la interacción analista × campaña es significativa en 135, 360, 405 y 455 ppb (F de 4,3 a 6,6 frente a F_0,05; 2, 30 = 3,32): la diferencia entre analistas cambia de una campaña a otra, y esa interacción forma parte de la reproducibilidad.
- La variación entre días dentro de una campaña es de 0,11 a 0,21 ppb; la componente entre campañas crece con la concentración y domina en 405 y 455 ppb, donde destaca la campaña de agosto de 2022 del analista 2 (errores medios de 0,73 y 0,83 ppb frente a unos 0,2 en las demás).
- Diseño que permite estimar repetibilidad, día y analista: varios analistas × varios días × al menos 2 ciclos independientes por analista y día, con orden sorteado. Para la componente entre analistas, los grados de libertad dependen del número de analistas, no del número de lecturas.
- Para un solo laboratorio sirve la Parte 3 de la ISO 5725; las Partes 2 y 4 son para estudios interlaboratorio.

**Práctica**
- Identificar la estructura de un diseño antes de analizarlo: a partir de la descripción de un estudio (quién midió, cuándo, cuántas veces), reconocer los factores, decidir si están cruzados o anidados, identificar la unidad de réplica y escribir el modelo con sus cuadrados medios esperados. Ejemplo: el estudio R&R de CALAIRE, cuyos días están anidados en analista × campaña; analizarlo como si los días fueran comunes a los dos analistas cambia la conclusión.
- Construir a mano la tabla ANOVA de un nivel del certificado (SS, g.l., MS, F) y revisar los supuestos con los residuos.
- Deducir los cuadrados medios esperados de un modelo cruzado de dos factores con réplicas y de un modelo con un factor anidado, y a partir de ellos los estimadores de cada componente y la prueba correcta de cada efecto.
- Reanalizar el estudio R&R de CALAIRE con el modelo analista × campaña con días anidados y comparar la conclusión con la prueba t del libro.
- Calcular los grados de libertad de cada componente para un diseño de 2, 3 y 4 analistas y decidir cuál justifica el esfuerzo.
- Analizar el factorial de robustez diseñado en M5 con un ANOVA de dos o tres factores.

**Referencias:** Intro. Statistics in Metrology §§9.3.1–9.3.6 (efectos aleatorios y mixtos, Tablas 9.9–9.10, supuestos, estudio R&R) · Otto §2.3 (ANOVA de uno y varios factores) · Mark y Workman cap. 115 (ANOVA) · Brereton cap. 2 (ANOVA y error puro) · Statistical Concepts cap. 9 (distribución F) · ISO 5725 Parte 3 §§5–6 (factores y modelo), §8 (estudio dentro del laboratorio), §§9.3–9.5 (diseños anidados) · ISO 5725 Partes 2 y 6, con sus corrigenda · GUM (JCGM 100) Anexo H.5 (análisis de varianza); G.4 (Welch-Satterthwaite) · Metrology and Measurement Uncertainty §4.4 (repetibilidad y reproducibilidad) · Deldossi y Zappa 2009 ISO 5725 frente a GUM · EN 14625 §8.2 · Estudio R&R CALAIRE 2022–2023 hojas 45ppb a 455ppb

## M7. Análisis de regresión y funciones de calibración (I, 5 h)

**Objetivo:** estimar y validar una función de calibración, eligiendo el método de ajuste según la estructura de incertidumbre de los datos.

**Se apoya en:** M3 · M4 · M6

**Teoría**
- Correlación de Pearson y su inferencia; por qué la correlación no valida una calibración.
- Mínimos cuadrados: criterio, ecuaciones normales y solución `b = S_xy/S_xx`, `a = ȳ − b·x̄`; forma matricial `β = (XᵀX)⁻¹Xᵀy`.
- Supuestos del modelo; residuos y s_e.
- Incertidumbre de los parámetros: u(a), u(b) y `cov(a,b) = −x̄·s²/S_xx`.
- Bandas de confianza y de predicción; predicción inversa con incertidumbre.
- Prueba de la pendiente; R² y sus límites.
- Falta de ajuste con réplicas: `F = [SS_LOF/(m−2)] / [SS_PE/(N−m)]`; residuo relativo por nivel.
- Recta con intercepto frente a recta forzada por el origen.
- Mínimos cuadrados ponderados y regresión con incertidumbre en x e y (ver tabla).
- Validación de un ajuste ponderado: χ²_obs frente a χ²_0,95; n−2 (ν = 10 con 12 puntos); en la ISO 6143, |residuo ponderado| ≤ 2.
- Función de análisis frente a función de calibración; prueba de compatibilidad.

**Qué regresión usar según la incertidumbre (ISO/TS 28037)**

| Incertidumbre en | Método |
|---|---|
| Solo y | WLS; con incertidumbres iguales, OLS |
| x e y, sin correlación | GDR (distancia generalizada) |
| x e y, covarianza dentro de cada par | GDR correlacionada (cercana a York) |
| Covarianzas entre valores de y | GMR (Gauss-Markov) |
| Covarianzas generales en ambos ejes | GGMR: la comparación con el BIPM (M9) |

> Ejemplo real del QAPP (SRP36 contra SRP7): pendiente 1,00169 ± 0,00012, intercepto 0,152 ± 0,050 ppb, R² = 0,99999985. Un R² casi perfecto no dice si la recta cumple los criterios de aceptación.

**Práctica**
- Deducir las ecuaciones normales y comprobarlas con los promedios del certificado.
- Regresión del Level 2 contra el SRP, falta de ajuste con las 8 réplicas y gráfico de residuos.
- Los mismos 12 pares por OLS y por WLS/GDR, reportando a, b, u(a), u(b), cov(a,b) y χ²_obs.
- Reproducir un ejemplo resuelto de la ISO/TS 28037 y el ejemplo B.2.1 de la ISO 6143 (NO medido por absorción UV).

**Referencias:** Intro. Statistics in Metrology §§10.1–10.4 (mínimos cuadrados, WLS, incertidumbre de parámetros, bandas, residuos, prueba de pendiente) · Statistical Concepts §§10.1, 10.4 (correlación, linealidad) · Otto §6.1 (Tabla 6.1) y §6.2 · Brereton §2.2 y cap. 6 · Mark y Workman cap. 21 (forma matricial); caps. 117–118 · GUM (JCGM 100) Anexo H.3 · ISO/TS 28037 cláusulas 6–10 y ejemplos · ISO 6143 §§4–7 y Anexo B · SRP QAPP Elemento 14.2

## M8. Evaluación de la incertidumbre de medida y capacidad de medición y calibración (I, 6 h)

**Objetivo:** evaluar la incertidumbre de medida conforme a la GUM, construir el presupuesto del SRP nacional y el de una calibración, y relacionarlos con la CMC.

**Se apoya en:** M1 · M3 · M4 · M6 · M7

**Teoría**
- Modelo de medición (GUM-6): medición directa e indirecta.
- Incertidumbre estándar; evaluación tipo A (de M2 y M4) y tipo B (de las distribuciones de M3).
- Ley de propagación: desarrollo de Taylor de primer orden y coeficientes de sensibilidad `c_i = ∂f/∂x_i`.
- Entradas correlacionadas: `u_c² = Σ c_i²u_i² + 2·Σ c_ic_j·u(x_i,x_j)`.
- Términos de orden superior, varias magnitudes de salida y límites del método analítico.
- Grados de libertad efectivos (Welch-Satterthwaite) y `k = t(ν_eff)` en lugar de k = 2 fijo.
- Incertidumbre expandida `U = k·u_c`, nivel de cobertura, presentación y redondeo.
- De la U de una calibración a la CMC; la plantilla aplica la regla `max(U, CMC)`.
- Propagación por la cadena: la incertidumbre del Level 2 (de su calibración contra el SRP) entra en el presupuesto de cada calibración de cliente.

**En el SRP: presupuestos reales**
- NIST SRP 6008: `u = √(0,28² + (0,011·x)²)` nmol/mol.
- BIPM-SRP27: `u = √(0,28² + (0,00292·x)²)`. El 0,00292 combina longitud óptica (2,89×10⁻³), presión (3,37×10⁻⁴) y temperatura (2,29×10⁻⁴); el 0,28 es la razón de intensidades D.
- La diferencia es la sección eficaz: el NIST incluye su incertidumbre (1,06×10⁻²·x) y el BIPM no, porque se cancela entre fotómetros UV con el mismo σ. ¿Cuándo debe entrar σ en un certificado?
- Componente común: `u(x_i,x_j) = x_i·x_j·u_b²`, con u_b = 2,92×10⁻³.
- Pérdidas de ozono, pureza del aire cero y lámpara no tienen cifra en la literatura: son sesgos que el operador vigila y cuantifica con datos propios.
- Las EN convierten cada característica de desempeño en una contribución y comparan con el objetivo de calidad (15 % en mediciones fijas).

**Práctica**
- Derivar los coeficientes de sensibilidad de la ecuación del SRP respecto de L, P, T, σ y D.
- Presupuesto completo de un punto de la calibración del Level 2: fuentes, sensibilidades, ν_eff, k y U.
- Llevar esa U al presupuesto de la calibración de un fotómetro de cliente hecha con el Level 2.
- Presupuesto del SRP nacional a 80 y 420 nmol/mol.

**Referencias:** Metrology and Measurement Uncertainty §§5.1–5.9 (tipo A y B, combinada, ν_eff, k, expandida, presentación) · Metrology and Measurement Uncertainty §§6.1–6.2 (ley de propagación, variables dependientes) · Intro. Statistics in Metrology §§6.2–6.4 (marco de incertidumbre, modelos directo e indirecto) · Intro. Statistics in Metrology §§7.2–7.7 (base matemática, correlación, orden superior, salidas múltiples, límites) · GUM (JCGM 100) §§4–7 y Anexo H · JCGM GUM-1 · JCGM GUM-6 §§11–12 · NIST SRP 6008 p. 2 · BIPM.QM-K1 Apéndice 1 · NISTIR 6963 §§10–11, Tabla 6 · EN 14625 anexos E–G · ASQ Metrology Handbook cap. 29

---

# Bloque III · Diseminación de la trazabilidad

Lo que solo hace este laboratorio: su comparación con el BIPM, la decisión sobre los fotómetros del país, el control de sus propios patrones y su relación con las redes.

## M9. Comparaciones clave: mínimos cuadrados generalizados y grado de equivalencia (I–A, 4 h; módulo central)

**Objetivo:** comprender, reproducir y sustentar el resultado del laboratorio en la comparación clave BIPM.QM-K1.

**Se apoya en:** M7 · M8

**Teoría**
- Protocolo A (comparación directa) y protocolo B (con patrón de transferencia).
- Ajuste GLS: estima a la vez la recta y los valores "verdaderos" de x, con la matriz de covarianza completa de x e y; se resuelve por Gauss-Newton, da cov(a,b) y se valida con χ² y residuos.
- OLS, WLS, Deming y la ISO 6143 son casos particulares; ninguno admite la covarianza entre puntos que impone el SRP27.
- La covarianza se construye desde causas comunes: `u_b²·x·xᵀ` viene de la temperatura, la presión y la longitud óptica compartidas.
- Grado de equivalencia `D = x_NS − x_SRP27` a 80 y 420 nmol/mol, con u(D) y sus covarianzas.

**En el SRP**
- El BIPM ajusta con el software OzonE; Milton 2006 describe XGENLINE.
- Una rutina ODR que solo acepta errores independientes por punto no reproduce el ajuste del BIPM.
- Para reproducir la comparación propia: los 12 pares medidos, las incertidumbres en ambos ejes y las matrices U_x, U_y y U_xy (justificando si U_xy = 0).
- Los ceros inicial y final se tratan con su posible deriva, no como datos independientes duplicados.
- El resultado de la comparación respalda las CMC del laboratorio.

**Práctica**
- Armar U_x para la secuencia BIPM con u_b = 0,00292 y compararla con la matriz diagonal que supone el OLS.
- Con los datos de una comparación real del laboratorio: contrastar OLS, ISO 6143 y GLS, y calcular los grados de equivalencia.

**Referencias:** Milton et al. 2006 §§2–5, 7 y Apéndice A · ISO/TS 28037 cláusula 10 (GGMR) · BIPM.QM-K1 §§7–9; protocolo B §§9–11; Apéndices 1 y 3 · ISO 6143 §§4–7

## M10. Evaluación de la conformidad y certificado de calibración (I, 3 h)

**Objetivo:** aplicar reglas de decisión que incorporen la incertidumbre y emitir certificados de calibración técnicamente sustentados.

**Se apoya en:** M4 · M8 · M9

**Teoría**
- Conformidad con una especificación; regla de decisión, banda de guarda y riesgo de falsa aceptación o rechazo.
- TUR (relación de incertidumbre de ensayo).
- Compatibilidad entre un valor medido y uno de referencia.
- Corrección de lecturas: `c = (y − y_0)·c_c/(y_c − y_0)`.
- Contenido del certificado: mensurando, intervalo, método, resultados, U con k, trazabilidad, sección eficaz usada y regla de decisión.

**Criterios reales (cada uno vale solo en su documento)**

| Documento | Criterio |
|---|---|
| SRP QAPP | Pendiente 1,00 ± 0,01; intercepto 0 ± 1 ppb |
| SRP SOP | 1 ± 0,04 y 0 ± 4 ppb al calificar; 1 ± 0,03 y 0 ± 3 ppb al reverificar |
| EPA TAD | Pendiente 1,00 ± 0,03; intercepto 0 ± 3 ppb; s de pendientes < 0,0075 |
| BIPM.QM-K1 | Grado de equivalencia a 80 y 420 nmol/mol |

**Práctica**
- Decidir si un patrón de transferencia pasa, primero sin la incertidumbre y luego con ella, y redactar la declaración de conformidad.

**Referencias:** Intro. Statistics in Metrology cap. 5 (incertidumbre y riesgo en la decisión) · Metrology and Measurement Uncertainty caps. 8–9 · ASQ Metrology Handbook cap. 30 (riesgo, TUR) · ISO/IEC 17025 §§7.6 y 7.8.6 · SRP QAPP Tabla 7-1 · SRP SOP §9.1 · EPA TAD §4 · EN 14625 §9.5.3

## M11. Control estadístico de procesos y aseguramiento de la validez de los patrones (I, 3 h)

**Objetivo:** vigilar la estabilidad del SRP y del Level 2 mediante control estadístico, modelar su deriva y fundamentar el intervalo de recalibración.

**Se apoya en:** M2 · M4 · M7

**Teoría**
- Control estadístico de procesos: variación por causas comunes y especiales.
- Cartas de control de Shewhart: línea central, límites de control y reglas de alarma.
- Deriva y predicción de valores futuros con su incertidumbre.
- Análisis del intervalo de calibración.
- Aseguramiento de la validez de los resultados.

**En el SRP**
- SOP: controles tan seguido como sea posible; temperatura y presión pueden derivar en 2–3 días.
- QAPP: aire cero 0 ± 0,2 ppb; presión ± 0,2 mbar.
- EPA TAD: Level 2 contra Level 1 cada año; 3 ciclos; s de pendientes < 0,0075; s de interceptos < 1,00 ppb. Son criterios directamente aplicables a la calibración del Level 2 de CALAIRE.
- NIST: con humedad por encima de 50 % se ha visto deriva del detector.

**Práctica**
- Carta de control de la pendiente con las diez comparaciones SRP-0 contra SRP-2 del NISTIR 6963 (pendiente media 1,00003, s = 0,00056; intercepto −0,131 ppb, s = 0,142), o con el historial propio del Level 2.
- Ajustar la deriva de la pendiente en el tiempo y decidir si hay que recalibrar antes de lo previsto.

**Referencias:** Intro. Statistics in Metrology §11.2 (control estadístico de procesos) · Intro. Statistics in Metrology §§10.8–10.9 (deriva, valores futuros, intervalo de calibración) · Otto cap. 9, Tablas 9.1–9.2 (cartas de control) · SRP SOP §§9–11 · SRP QAPP Tabla 7-1 · EPA TAD §4 y Tabla 4-1 · NISTIR 6963 Tabla 4 · NIST SRP 6008 pp. 2–3 · ISO/IEC 17025 §7.7

## M12. Indicadores de precisión y sesgo en las redes de monitoreo (I, 3 h)

**Objetivo:** conocer los indicadores estadísticos con que las redes de monitoreo evalúan sus datos y su relación con los valores que certifica el laboratorio.

**Se apoya en:** M4 · M8 · M10

**Estadística oficial de la red (40 CFR 58, Apéndice A)**
- Diferencia de cada verificación: `d_i = (meas − audit)/audit · 100`.
- CV con límite superior al 90 %: `CV = s(d_i)·√[(n−1)/χ²_0,1; n−1]` (intervalo para una varianza, M4).
- Sesgo absoluto con límite superior al 95 %: `|sesgo| = AB + t_0,95; n−1·AS/√n`, con el signo según los percentiles 25 y 75.
- Objetivo para O₃: CV ≤ 7 % y |sesgo| ≤ 7 %.
- Datos de origen: control de un punto, auditoría anual con patrones independientes y NPAP. Las concentraciones de ensayo vienen de un patrón de transferencia trazable: ahí entra el laboratorio.

**Contexto de los analizadores**
- El CV y el sesgo resumen un año de verificaciones de un monitor; la U de un certificado describe una sola calibración. No se sustituyen.
- Desempeño del analizador (40 CFR 53): ruido, límite detectable inferior, deriva de cero y span, precisión al 20 % y 80 % del rango.
- EN 14625: repetibilidad ≤ 1 nmol/mol en cero y ≤ 3 en el nivel de ensayo; deriva de cero ≤ 2 nmol/mol en 12 h. Las EN 14211, 14212 y 14626 sirven de contraste con otros gases.
- Datos regulatorios: promedio móvil de 8 h, cuarto máximo anual, valor de diseño comparado con 0,070 ppm, completitud.

**Práctica**
- Con d_i = 1; 2; 0,5; 3; 1,5; 2,5 %: CV = 1,65 % y |sesgo| = 2,52 %, positivo.
- ¿Cómo aparece en los d_i de una red un sesgo de +1,25 % por usar la sección eficaz antigua?
- Ejemplo de la EPA 2014–2016 sobre el valor de diseño.

**Referencias:** 40 CFR 58, Apéndice A §§2.3, 2.6, 3.1, 4.1 y 5.1 · EPA QA Handbook Vol. II · 40 CFR 53 · 40 CFR 50 Apéndices A-1, C y P/U · Plantilla de validación EPA · EN 14625 §8 y Tabla E.1 · EN 14211, 14212 y 14626

---

# Cierre

El taller junta todo el curso sobre un caso real; el optativo abre los temas que superan el nivel del curso.

## T. Taller integrador: casos reales del laboratorio (I–A, 8 h)

**Objetivo:** integrar los métodos del curso en cuatro casos que corresponden a las funciones del laboratorio: calibrar el Level 2, compararse con el BIPM, vigilar sus patrones y evaluar su sistema de medición.

**Se apoya en:** M2–M12

**Caso A · Calibración del Level 2 contra el SRP 55**
- Datos reales de CALAIRE: certificado F-PSMT-01, Thermo 49C contra SRP 55, 12 puntos × 8 repeticiones × 6 días.
- Descripción y atípicos (M2), normalidad (M3), ANOVA por días (M6), regresión y falta de ajuste (M7), presupuesto GUM con ν_eff y k (M8), decisión (M10).
- Comparar con lo que reporta la plantilla actual y discutir las diferencias.

**Caso B · Comparación clave con ajuste GLS**
- Datos publicados: comparación SRP36 contra SRP7 (QAPP, Fig. 14.2), tratada con el método del BIPM.
- OLS frente a GGMR con la covarianza común `u_b`, en dos variantes de incertidumbre; validación del código con un ejemplo de la ISO/TS 28037; χ² y su interpretación (M7, M9).
- Grados de equivalencia a 80 y 420 nmol/mol por interpolación con la recta, y por qué difiere de la ecuación del protocolo para mediciones directas (M9).
- Inconsistencias internas del propio QAPP (covarianza y desviación residual) como ejercicio de lectura crítica.

**Caso C · Historial y control estadístico del Level 2**
- Datos reales de CALAIRE (pendientes e interceptos de los 6 días) y diez comparaciones publicadas (NISTIR 6963, Tabla 4).
- Evaluación de los 6 días contra la verificación 6x6 del QAPP, que es el criterio directamente aplicable, y contraste con la EPA TAD 2023 (M10).
- Cartas de individuales y rango móvil a 3σ, prueba de deriva y prueba F (M4, M11).

**Caso D · Estudio R&R de CALAIRE 2022–2023**
- Datos reales: errores medios diarios del Level 2 frente al SRP 55 de dos analistas en 10 niveles, en tres campañas de 6 días cada una.
- Lectura crítica: reconstruir la estructura real (campañas, días anidados en analista × campaña), ver qué responde una prueba t entre analistas y qué no, y localizar los errores de fórmula del libro (varianzas con 12 de 18 datos, α distinto en un nivel).
- Reanálisis con el modelo analista × campaña con días anidados (M6): efecto del analista, interacción, componente entre campañas y entre días; los datos no están pareados por día. Qué diseño haría falta para estimar bien la reproducibilidad.

**Práctica**
- Los casos B y C tienen enunciado paso a paso, datos con su fuente y solución de referencia reproducible en la carpeta casos_taller/ (datos en CSV y el script calc_casos.py). Los casos A y D se trabajan directamente sobre los libros de Excel de CALAIRE.

**Referencias:** Certificado F-PSMT-01 plantilla .xlsm · SRP QAPP Elemento 14.2, Fig. 14.2; §6.2.3 y Tabla 7-1 · BIPM.QM-K1 protocolo A §8; Apéndices 1 y 3 · Milton et al. 2006 · ISO/TS 28037 cláusula 10, Tablas 25–26 · NISTIR 6963 Tabla 4 · EPA TAD Tabla 4-1, §4.4 · Intro. Statistics in Metrology §11.2 · Otto cap. 9 · Estudio R&R CALAIRE 2022–2023 hojas 45ppb a 455ppb

## M13. Temas avanzados (optativo) (A, 4 h)

**Objetivo:** introducir métodos que superan la propagación lineal y la regresión de una sola respuesta.

**Se apoya en:** M3 · M7 · M8

**Temas**
- Monte Carlo frente a propagación lineal; Monte Carlo en ajuste de curvas.
- Pendiente e intercepto como salidas conjuntas.
- Regresión no lineal y regresión de distancia ortogonal.
- Implementación propia del ajuste GGMR/GLS y su validación.
- Bootstrap remuestreando días completos; regresión robusta y métodos robustos de la ISO 5725-5.
- Calibración multivariada (PCR, PLS): por qué no aporta en un fotómetro de una sola longitud de onda.
- Uso responsable de herramientas de IA para análisis, siempre verificando datos, unidades y supuestos.

**Referencias:** GUM Suplemento 1 y corrigendum · GUM Suplemento 2 · Intro. Statistics in Metrology cap. 8; §§10.5–10.6 · ISO/TS 28037 cláusula 10 · Milton et al. 2006 · ISO 5725 Parte 5 · Brereton cap. 6 · Mark y Workman caps. 21–27 · Handbook of Uncertainty Quantification §§1–2 · AI-Assisted Statistics caps. 1, 4, 10 y 11

---

# Conceptos estadísticos del curso

Cada concepto con lo que se enseña de su teoría, el módulo donde se trata y la fuente teórica con sección.

## Datos y estadística descriptiva

| Concepto | Qué se enseña | Módulo | Fuente teórica |
|---|---|---|---|
| Población, muestra, parámetro y estadístico | Distinguir lo que se quiere conocer de lo que se mide; notación. | M2 | Statistical Concepts §1.3 |
| Tipos de variables y escalas de medida | Discretas y continuas; escalas nominal, ordinal, de intervalo y de razón. | M2 | Statistical Concepts §§1.4–1.5; Intro. Statistics in Metrology §4.2 |
| Distribución de frecuencias e histograma | Tablas de frecuencia absoluta, relativa y acumulada; formas de una distribución. | M2 | Statistical Concepts §§2.1–2.2; Intro. Statistics in Metrology §4.3.2 |
| Percentiles, cuartiles y diagrama de caja | Posición relativa de un dato; rango intercuartílico; lectura de la caja. | M2 | Statistical Concepts §2.3; Intro. Statistics in Metrology §4.3.2 |
| Tendencia central | Media, mediana y moda; propiedades y cuándo usar cada una. | M2 | Statistical Concepts §3.2; Intro. Statistics in Metrology §4.3.1 |
| Dispersión | Rango, varianza, desviación estándar muestral (n − 1), coeficiente de variación. | M2 | Statistical Concepts §3.3; Metrology and Measurement Uncertainty §3.2.2 |
| Error estándar de la media | `s/√n`: dispersión de la media, no de las lecturas. | M2, M4 | Intro. Statistics in Metrology §4.3.1; Statistical Concepts §5.2 |
| Puntuación z, asimetría y curtosis | Estandarización; medidas de forma de la distribución. | M2 | Statistical Concepts §§4.2–4.3 |
| Cifras significativas y redondeo | Reglas de redondeo y de operación; redondear al final. | M2, M8 | Metrology and Measurement Uncertainty §3.1 |
| Valor atípico | Definición respecto de un modelo; Grubbs, Dixon, Cochran, h y k de Mandel; criterios de exclusión. | M2 | Otto §2.2; ISO 5725 Parte 2; Mark y Workman caps. 119–121 |

## Probabilidad y distribuciones

| Concepto | Qué se enseña | Módulo | Fuente teórica |
|---|---|---|---|
| Probabilidad | Definición y reglas básicas; intuición frente a probabilidad. | M3 | Statistical Concepts §5.1 |
| Variable aleatoria | Discreta y continua; experimento aleatorio y muestra. | M3 | Metrology and Measurement Uncertainty §3.2.1 |
| Función de densidad y de distribución | Densidad de probabilidad discreta y continua; distribución acumulada. | M3 | Metrology and Measurement Uncertainty §3.2.3 |
| Esperanza y varianza | Media y desviación estándar de una distribución. | M3 | Metrology and Measurement Uncertainty §3.2.4 |
| Reglas de la esperanza y la varianza | Combinaciones lineales; varianza de una suma con covarianza. Base de la propagación. | M3, M8 | Intro. Statistics in Metrology §7.2 |
| Covarianza y correlación | Definición, signo, rango de r y efecto sobre la varianza combinada. | M3, M8 | Intro. Statistics in Metrology §7.4.1; Statistical Concepts §10.1 |
| Distribución normal | Propiedades, normal estándar y uso de tablas. | M3 | Statistical Concepts §4.1; Metrology and Measurement Uncertainty §3.2.5.4 |
| Distribuciones rectangular y triangular | Cuándo se usan y su desviación estándar (`a/√3`, `a/√6`). | M3, M8 | Metrology and Measurement Uncertainty §§3.2.5.1–3.2.5.3; Metrology and Measurement Uncertainty §5.3 |
| Distribución t de Student | Origen, grados de libertad y convergencia a la normal. | M3, M4 | Metrology and Measurement Uncertainty §3.2.5.5; Statistical Concepts §6.1 |
| Distribuciones chi-cuadrado y F | Origen y uso en pruebas sobre varianzas y en el ANOVA. | M3, M4 | Statistical Concepts §8.2; Statistical Concepts §9.1.1 |
| Ajuste a una distribución | Estimar parámetros; gráfico de probabilidad normal; pruebas de normalidad. | M3 | Intro. Statistics in Metrology §§4.4.1–4.4.3; Statistical Concepts §6.4 |

## Inferencia

| Concepto | Qué se enseña | Módulo | Fuente teórica |
|---|---|---|---|
| Muestreo aleatorio y estimación | Estimador, sesgo y varianza de un estimador; grados de libertad. | M4 | Statistical Concepts §5.2 |
| Distribución muestral y teorema central del límite | Comportamiento de la media de n lecturas. | M4 | Statistical Concepts §5.2.2; Metrology and Measurement Uncertainty §§3.2.5.6–3.2.5.9 |
| Intervalo de confianza | Construcción con normal y con t; interpretación correcta. | M4 | Statistical Concepts §6.1; Intro. Statistics in Metrology §4.4.2 |
| Prueba de hipótesis | H₀, H₁, estadístico, región crítica, α y valor p. | M4 | Statistical Concepts §§6.1, 7.1.2 |
| Errores tipo I y II, potencia, tamaño del efecto | Riesgos de una prueba y tamaño de muestra. | M4, M5 | Statistical Concepts §§6.1.2–6.1.4; Mark y Workman cap. 15 |
| Prueba t | Una media, dos medias independientes (Welch) y datos pareados. | M4 | Statistical Concepts §6.1; Statistical Concepts §§7.1–7.2 |
| Pruebas sobre varianzas | Una varianza (chi-cuadrado) y dos varianzas (F). | M4 | Statistical Concepts §§9.1–9.3 |
| Prueba chi-cuadrado de bondad de ajuste | Comparar frecuencias observadas y esperadas. | M4 | Statistical Concepts §8.3.1 |
| Supuestos de las pruebas | Independencia y normalidad; cómo verificarlos. | M4, M6 | Statistical Concepts §§6.1.5, 6.4; Intro. Statistics in Metrology §9.3.3 |
| Significación frente a relevancia | Un efecto detectable puede no importar metrológicamente, y al revés. | M4 | Statistical Concepts §6.1.4; Mark y Workman cap. 15 |

## Diseño experimental y ANOVA

| Concepto | Qué se enseña | Módulo | Fuente teórica |
|---|---|---|---|
| Elementos de un experimento | Respuesta, factores, niveles y unidad experimental. | M5 | Intro. Statistics in Metrology §§9.2.1–9.2.3; Brereton cap. 2 |
| Aleatorización, bloques y replicación | Replicación verdadera frente a pseudorreplicación. | M5 | Brereton cap. 2; Mark y Workman caps. 8–12 |
| Diseño factorial | Efectos principales e interacciones; 2^k. | M5 | Intro. Statistics in Metrology §9.2; Brereton cap. 2; Mark y Workman caps. 8–16 |
| Diseño anidado | Lecturas dentro de corridas dentro de días; diseño escalonado. | M5, M6 | ISO 5725 Parte 3 |
| ANOVA de un factor | Descomposición de sumas de cuadrados, cuadrados medios y prueba F. | M6 | Otto §2.3; Mark y Workman cap. 115 |
| Efectos fijos y aleatorios; componentes de varianza | Cuadrados medios esperados y estimación de σ²_día. | M6 | Intro. Statistics in Metrology §§9.3.1–9.3.2 |
| ANOVA de dos factores, anidado y mixto | Interacción y factores anidados. | M6 | Otto §2.3; Intro. Statistics in Metrology §9.3.2 |
| Supuestos del ANOVA | Independencia, normalidad y varianza homogénea; residuos. | M6 | Intro. Statistics in Metrology §9.3.3 |
| Estudio R&R del sistema de medición | Modelo cruzado con efectos aleatorios, componentes de varianza y R&R total; diferencia con la ISO 5725 y con una prueba t entre operadores. | M6 | Intro. Statistics in Metrology §9.3.4 |
| Cuadrados medios esperados | Valor esperado de cada cuadrado medio en modelos cruzados y anidados; base de los estimadores y de la elección del denominador de F. | M6 | Intro. Statistics in Metrology §9.3.1, Tablas 9.9–9.10 |
| Diseño cruzado frente a anidado | Qué componentes permite estimar cada estructura; diseño anidado escalonado. | M5, M6 | ISO 5725 Parte 3 §§9.3–9.5 |
| Grados de libertad de una componente de varianza | Precisión de una componente según el número de niveles de su factor; Welch-Satterthwaite para combinaciones. | M6 | GUM (JCGM 100) G.4; Intro. Statistics in Metrology §9.3.4 |
| Repetibilidad, reproducibilidad y precisión intermedia | Definiciones, estimación y límites r y R. | M6 | Metrology and Measurement Uncertainty §4.4; ISO 5725 Partes 2, 3 y 6 |
| Veracidad y sesgo | Sesgo frente a un valor de referencia. | M6, M10 | ISO 5725 Partes 4 y 6; Metrology and Measurement Uncertainty §4.3.2 |

## Regresión y calibración

| Concepto | Qué se enseña | Módulo | Fuente teórica |
|---|---|---|---|
| Correlación de Pearson | Cálculo, inferencia y por qué no valida una calibración. | M7 | Statistical Concepts §10.1 |
| Mínimos cuadrados | Criterio, ecuaciones normales y forma matricial. | M7 | Intro. Statistics in Metrology §10.2.1; Mark y Workman cap. 21 |
| Incertidumbre de los parámetros | u(a), u(b) y su covarianza. | M7 | Intro. Statistics in Metrology §§10.2.2, 10.3.1 |
| Bandas de confianza y de predicción | Incertidumbre de la recta y de una nueva observación. | M7 | Intro. Statistics in Metrology §§10.3.2–10.3.3 |
| Análisis de residuos y prueba de pendiente | Diagnóstico gráfico y cuantitativo del modelo. | M7 | Intro. Statistics in Metrology §10.4 |
| Falta de ajuste | Error puro frente a falta de ajuste con réplicas. | M7 | Otto §6.1, Tabla 6.1; Brereton §2.2 |
| Calibración inversa | Predecir x a partir de una nueva y, con incertidumbre. | M7 | Otto §6.2; ISO/TS 28037 |
| Mínimos cuadrados ponderados | Pesos según u(y). | M7 | Intro. Statistics in Metrology §10.2.3; ISO/TS 28037 cláusula 6 |
| Incertidumbre en x e y | GDR, Deming y York como casos particulares. | M7 | Intro. Statistics in Metrology §10.2.4; ISO/TS 28037 cláusulas 7–8 |
| Mínimos cuadrados generalizados | Matriz de covarianza completa; GMR y GGMR. | M7, M9 | Milton et al. 2006; ISO/TS 28037 cláusulas 9–10 |
| Validación con chi-cuadrado | χ²_obs frente a sus grados de libertad; residuos ponderados. | M7, M9 | ISO/TS 28037; ISO 6143 |

## Incertidumbre de medición

| Concepto | Qué se enseña | Módulo | Fuente teórica |
|---|---|---|---|
| Modelo de medición | Mensurando, magnitudes de entrada y ecuación del modelo. | M8 | JCGM GUM-6; Intro. Statistics in Metrology §§6.3–6.4 |
| Evaluación tipo A y tipo B | De los datos y de otra información. | M8 | Metrology and Measurement Uncertainty §§5.2–5.3; Intro. Statistics in Metrology §§6.2.2–6.2.3 |
| Ley de propagación | Desarrollo de Taylor de primer orden y coeficientes de sensibilidad. | M8 | Metrology and Measurement Uncertainty §6.1; Intro. Statistics in Metrology §§7.2–7.3 |
| Entradas correlacionadas | Término de covarianza en la propagación. | M8 | Metrology and Measurement Uncertainty §6.2; Intro. Statistics in Metrology §7.4 |
| Incertidumbre combinada y expandida | u_c, k, U y nivel de cobertura. | M8 | Metrology and Measurement Uncertainty §§5.5, 5.7–5.8; Intro. Statistics in Metrology §§6.2.4–6.2.5 |
| Grados de libertad efectivos | Welch-Satterthwaite y k con t. | M8 | Metrology and Measurement Uncertainty §5.6 |
| Presentación del resultado | Resultado ± U con k y unidades; redondeo. | M8 | Metrology and Measurement Uncertainty §5.9; GUM (JCGM 100) §7 |
| Método de Monte Carlo | Propagación de distribuciones. | M13 | Intro. Statistics in Metrology cap. 8; GUM Suplemento 1 |
| Varias magnitudes de salida | Pendiente e intercepto como salida conjunta. | M13 | Intro. Statistics in Metrology §7.6; GUM Suplemento 2 |

## Decisión y control

| Concepto | Qué se enseña | Módulo | Fuente teórica |
|---|---|---|---|
| Regla de decisión y riesgo | Banda de guarda, falsa aceptación y falso rechazo. | M10 | Intro. Statistics in Metrology cap. 5; Metrology and Measurement Uncertainty cap. 8; ASQ Metrology Handbook cap. 30 |
| TUR | Relación de incertidumbre de ensayo. | M10 | ASQ Metrology Handbook cap. 30 |
| Grado de equivalencia | Diferencia con la referencia y su incertidumbre con covarianzas. | M9 | BIPM.QM-K1 §8 y Apéndice 1 |
| Cartas de control | Shewhart: línea central, límites y reglas. | M11 | Intro. Statistics in Metrology §11.2; Otto cap. 9 |
| Deriva e intervalo de calibración | Predicción de valores futuros y elección del intervalo. | M11 | Intro. Statistics in Metrology §§10.8–10.9 |
| Estadística de precisión y sesgo de la red | CV y sesgo con límites de confianza (chi-cuadrado y t). | M12 | 40 CFR 58, Apéndice A §4.1 |

---

# Bibliografía

Todas las fuentes están en `docs/`. Entre corchetes, los módulos donde se usa cada una.

## SRP y medición de ozono

- **BIPM.QM-K1.** BIPM. *Protocol for BIPM.QM-K1, On-demand Key Comparison of Ozone at Ambient Level*, v2.1, 9-10-2025. `BIPM.QM-K1_2.protocol.pdf` [M1, M2, M3, M5, M8, M9, T]
- **NISTIR 6963.** Paur, R. J.; Bass, A. M.; Norris, J. E.; Buckley, T. J. *Standard Reference Photometer for the Assay of Ozone in Calibration Atmospheres*. NIST, 2003. `nistir6963.pdf` [M1, M2, M3, M5, M8, M11, T]
- **NIST SRP 6008.** NIST. *Standard Reference Instrument Series 6008: Ozone Standard Reference Photometer*, especificación y certificado, 2017. `SRP6008_spec_cert.pdf` [M1, M8, M11]
- **SRP SOP.** US EPA. *SOP for the Verification and Re-Verification of EPA's Ozone Standard Reference Photometers*, SRP/SOP-1, rev. 1, 2015. `srp_sop.pdf` [M1, M5, M10, M11]
- **SRP QAPP.** US EPA. *Quality Assurance Project Plan for the Standard Reference Photometer Program*, 2017. `srp_qapp.pdf` [M1, M5, M7, M10, M11, T]
- **EPA TAD.** US EPA. *Transfer Standards for Calibration of Air Monitoring Analyzers for Ozone*, EPA-454/B-22-003, 2023. `o3_tad_508_20230906_final.pdf` [M1, M5, M10, M11, T]
- **Daumont et al. 1992.** Daumont, D.; Brion, J.; Charbonnier, J.; Malicet, J. *Ozone UV spectroscopy I: Absorption cross-sections at room temperature*. J. Atmos. Chem. 15, 145–155. `Ozone UV spectroscopy I_ Absorption cross-sections at room.pdf` [M1]
- **Malicet et al. 1995.** Malicet, J. et al. *Ozone UV spectroscopy II: Absorption cross-sections and temperature dependence*. J. Atmos. Chem. 21, 263–273. `Ozone UV spectroscopy_ II_ Absorption cross-sections .pdf` [M1]
- **ISO 13964.** BS ISO 13964:1998. *Air quality — Determination of ozone in ambient air — Ultraviolet photometric method*. `Air quality_ Determination of ozone in ambient air_ ISO 13964.pdf` [M1, M5]
- **EN 14625.** BS EN 14625:2012. *Ambient air — Standard method for the measurement of the concentration of ozone by ultraviolet photometry*. `BS EN 14625_2012.pdf` [M5, M6, M8, M10, M12]

## Regulación y aseguramiento de la calidad (EE. UU.)

- **40 CFR 50, Apéndice D.** eCFR vigente al 16-10-2026; incluye la nueva sección eficaz (304,39 atm⁻¹ cm⁻¹). `Appendix D to Part 50_ Title 40 (up to date as of 10-16-2026).pdf` [M1]
- **40 CFR 50.** Texto completo y Apéndices A-1 y C (eCFR, 19-10-2026). `USEPA - 40 CFR Part 50.pdf`, `Appendix A-1 to Part 50_ ….pdf`, `Appendix C to Part 50_ ….pdf` [M12]
- **40 CFR 53.** Métodos de referencia y equivalentes: pruebas de desempeño de analizadores. `USEPA - 40 CFR Part 53.pdf` [M12]
- **40 CFR 58, Apéndice A.** Requisitos de aseguramiento de calidad de las redes, eCFR vigente al 20-10-2026. `Appendix A to Part 58_ Title 40 (up to date as of 10-20-2026).pdf` [M12]
- **EPA QA Handbook Vol. II.** US EPA. *Quality Assurance Handbook for Air Pollution Measurement Systems, Volume II*. `USEPA - Quality Handbook.pdf` [M12]
- **Plantilla de validación EPA.** US EPA. Apéndice D, plantilla de validación (v. 03/2017); idéntica a `USEPA - Appendix D Air Quality Handbook.pdf`. `app_d_validation_template_version_03_2017_for_amtic_rev_1.pdf` [M12]

## Incertidumbre, calibración y precisión (GUM e ISO)

- **GUM (JCGM 100).** ISO/IEC Guide 98-3:2008. *Guide to the expression of uncertainty in measurement*. `ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ ….pdf` [M6, M7, M8]
- **GUM Suplemento 1.** ISO/IEC Guide 98-3/Suppl. 1:2008, método de Monte Carlo, con su corrigendum 1:2009. `ISO_IEC Guide 98-3_2008 Suppl.1_2008 ….pdf`, `… Suppl.1_2008_Cor 1_2009 ….pdf` [M13]
- **GUM Suplemento 2.** ISO/IEC Guide 98-3/Suppl. 2:2011, cualquier número de magnitudes de salida. `ISO_IEC Guide 98-3_2008 Suppl.2_2011 ….pdf` [M13]
- **JCGM GUM-1.** Introducción a la expresión de la incertidumbre de medida. `JCGM_GUM-1.pdf` [M1, M8]
- **JCGM GUM-6.** JCGM GUM-6:2020. Desarrollo y uso de modelos de medición. `JCGM_GUM_6_2020.pdf` [M8]
- **ISO/IEC 17025.** BS EN ISO/IEC 17025:2017. Requisitos generales para la competencia de los laboratorios de ensayo y calibración. `BS EN ISO_IEC 17025_2017.pdf` [M1, M5, M10, M11]
- **ISO 6143.** ISO 6143:2001. *Gas analysis — Comparison methods for determining and checking the composition of calibration gas mixtures*. `ISO 6143 2001.pdf` [M7, M9]
- **ISO/TS 28037.** ISO/TS 28037:2010. *Determination and use of straight-line calibration functions*. `ISO 28037.pdf` [M7, M9, T, M13]
- **ISO 5725.** ISO 5725-2, -3, -4 y -6:1994 y 5725-5:1998. Exactitud (veracidad y precisión) de métodos y resultados de medición, con los corrigenda de las Partes 1, 2, 3, 5 y 6. `ISO 5725-*.pdf` [M2, M5, M6, M13]
- **Deldossi y Zappa 2009.** Deldossi, L.; Zappa, D. Comparación entre ISO 5725 y GUM, 2009. `2009 - Deldossi - ISO 5725 vs GUM comparison.pdf` [M6]
- **Milton et al. 2006.** Milton, M. J. T. et al. *Implementation of a generalized least-squares method for determining calibration curves from data with general uncertainty structures*. Metrologia, 2006. `milton2006.pdf` [M9, T, M13]
- **EN 14211, 14212 y 14626.** BS EN 14211:2012 (NO/NO₂), BS EN 14212:2012 (SO₂) y BS EN 14626:2012 (CO). `BS EN 14211_2012.pdf`, `BS EN 14212_2012 .pdf`, `BS EN 14626_2012 .pdf` [M12]

## Libros de estadística, metrología y quimiometría

- **Statistical Concepts.** *Statistical Concepts – A First Course*, por capítulos. `statistical_concepts_c01–c10.pdf` [M2, M3, M4, M6, M7]
- **Intro. Statistics in Metrology.** *Introduction to Statistics in Metrology*, por capítulos. `intro_stats_metro_c01–c11.pdf`, `a01–a05.pdf` [M1, M2, M3, M4, M5, M6, M7, M8, M10, M11, T, M13]
- **Metrology and Measurement Uncertainty.** *Metrology and Measurement Uncertainty*, por capítulos. `metrology_measure_uncer_c01–c10.pdf` [M1, M2, M3, M4, M6, M8, M10]
- **ASQ Metrology Handbook.** *The ASQ Metrology Handbook*, caps. 27, 29 y 30. `asq_metrological_handbook_c*.pdf` [M4, M8, M10]
- **Otto.** Otto, M. *Chemometrics: Statistics and Computer Application in Analytical Chemistry*, 3.ª ed. Wiley-VCH, 2017. `Chemometrics Statistics and Computer Application.pdf` [M2, M6, M7, M11, T]
- **Brereton.** Brereton, R. G. *Chemometrics: Data Driven Extraction for Science*, 2.ª ed. Wiley, 2018. `chemometrics_c01–c07.pdf`, `chemometrics_a01.pdf` [M3, M4, M5, M6, M7, M13]
- **Mark y Workman.** Mark, H.; Workman, J. *Chemometrics in Spectroscopy*, 2.ª ed. Elsevier, 2018, secciones. `chemometrics_spectroscopy_s03, s05, s06, s020, s021.pdf` [M1, M2, M4, M5, M6, M7, M13]
- **Handbook of Uncertainty Quantification.** Consulta de apoyo. `Handbook of Uncertainty Quantification.pdf` [M13]
- **AI-Assisted Statistics.** *AI-Assisted Statistics for Data Scientists*, material de apoyo. `AI-Assisted Statistics for Data Scientists_.epub` [M13]

## Caso del proyecto

- **Estudio R&R CALAIRE 2022–2023.** Resultados del estudio de repetibilidad y reproducibilidad del Level 2 contra el SRP 55: dos analistas, 10 niveles, tres campañas de 6 días (hoja BASE DE DATOS). `Resultados R&r_2022 2023 (1).xlsx` [M6, T]
- **Certificado F-PSMT-01.** Plantilla del certificado de calibración del patrón Level 2 de CALAIRE (Thermo 49C, S/N 59756-324) contra el SRP 55. `F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm` [T]

