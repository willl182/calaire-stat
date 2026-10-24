# Propuesta de ajuste del curso

**Fecha:** 23-10-2026.
**Objeto:** `temario_curso.md` (22-10-2026) y los casos del taller.
**Base:** las auditorías `audit_a.md`, `audit_b.md` y `audit_c.md`, y sus cuatro revisiones `rev_audits_a.md` a `rev_audits_d.md`.
**Alcance:** solo contenido. Las horas se calculan después, con este alcance ya fijado. La sección 13 reúne lo que afecta a ese cálculo.

---

## 1. Criterios de la propuesta

1. **Tres perfiles acumulativos.** El curso completo se puede dar en B, I y A. I incluye todo B; A incluye todo I.
2. **Cada tema se enseña y se practica en clase en su nivel**, o no se da en ese nivel y entra en el siguiente. No hay temas de "lectura", "para mostrar" ni "optativos" dentro de un nivel.
3. **Las prácticas son de aplicación:** calcular, interpretar y decidir con datos del laboratorio. Las demostraciones van a anexos.
4. **El curso enseña conceptos, no audita archivos.** Los defectos de los libros de Excel de CALAIRE se usan como ejemplos de un concepto (por ejemplo, "¿s o s/√n?"), no como revisión del sistema de calidad.
5. **Solo se adopta lo técnicamente comprobado.** Las cuatro revisiones confirmaron varios hallazgos y refutaron otros. Esta propuesta usa los confirmados y deja fuera los refutados (sección 10).

### Cómo se combinan las auditorías

| Auditoría | Qué aporta a la propuesta |
|---|---|
| B | La arquitectura: tres perfiles acumulativos, una celda B/I/A por módulo, la competencia de escalar, los vacíos de uso diario (U/k, s o s/√n, E_n, Kragten, límite de detección, incertidumbre de s) |
| C | Los hallazgos de datos: diferencias con signo frente a lecturas brutas, valor absoluto en el R&R, `STDEV.P(ABS(...))/√576`, contenido detallado por módulo y anexos |
| A | La corrección conceptual: unidades de réplica (H07), signo del cambio de escala (H05), resultado / función de uso / conformidad (H16), lectura, promedio y resultado futuro (§4.2), supuestos de la regresión (H13), evaluación con errores críticos |

**Lo que distingue a cada nivel.** Las revisiones coinciden en que un nivel no se define por el nombre de la técnica sino por lo que hace el participante con ella. Se adoptan cuatro verbos:

| Verbo | B | I | A |
|---|---|---|---|
| Interpretar un resultado | Sí | Sí | Sí |
| Ejecutar un método con herramienta preparada | Sí | Sí | Sí |
| Elegir el método y justificarlo | — | Sí | Sí |
| Formular el modelo y validar la herramienta | — | — | Sí |

Así se resuelven las contradicciones del mapa de la auditoría B: B puede hacer un ANOVA de un factor con plantilla (ejecutar) sin elegir entre modelos (seleccionar), y el intermedio puede correr un GLS con software validado (ejecutar) sin formularlo ni validarlo (A).

---

## 2. Perfiles

| | Básico (B) | Intermedio (I) | Avanzado (A) |
|---|---|---|---|
| Función en el laboratorio | Ejecuta calibraciones y el control diario de los patrones | Prepara presupuestos de incertidumbre y certificados con CMC | Responsable técnico de la comparación con el BIPM, de los estudios R&R y de la validación de cálculos |
| Al terminar puede | Calcular con plantilla, interpretar, decidir con un criterio dado y **reconocer cuándo un caso necesita a alguien de nivel I o A** | Elegir el método, calcular con hoja propia y justificar la elección | Formular el modelo, tratar casos no estándar y validar software |
| Herramienta | Hoja de cálculo con plantilla preparada | Hoja de cálculo propia | Python o R, validación contra ejemplos normativos |
| Fórmulas | Se dan y se usan | Se dan, con su condición de uso | Se dan en forma general; las demostraciones están en los anexos |
| Datos | Subconjuntos preparados del certificado F-PSMT-01 (sección 3.4) | Certificado completo (12 × 8 × 6) | Certificado, estudio R&R y comparación BIPM |

Aprobar un nivel acredita la competencia enseñada. La autorización para firmar la da el laboratorio con sus propias reglas.

**Competencia transversal de B: escalar.** El operador reconoce las señales de que un caso se sale de la plantilla:
- lecturas consecutivas tratadas como réplicas independientes;
- pocos días de datos (ν_eff pequeño);
- resultado cerca del límite de aceptación;
- atípico sin causa identificada;
- señal o deriva en la carta de control;
- cambio de σ, de método o de software;
- variable de análisis transformada (valor absoluto, lecturas brutas de días con distinta concentración).

Se practica en cada módulo de B y se evalúa en el taller.

---

## 3. Convenciones del curso

Se fijan una sola vez, en M0, y se usan igual en todos los módulos, casos y soluciones.

### 3.1 Símbolos y signos

- **Unidades:** en este curso ppb = nmol/mol (fracción molar, gas ideal). Los certificados usan nmol/mol.
- **Error y corrección:** error = indicación − referencia; corrección = −error.
- **Función de calibración:** `y = a + b·x`, con y la indicación del instrumento y x el valor de referencia. Uso: `x̂ = (y − a)/b`. No se ajusta otra regresión intercambiando los ejes.
- **Incertidumbre:** u estándar, U expandida, k factor de cobertura. Siempre se declara k.
- **Cuantiles:** para un intervalo bilateral del 95 %, `t_0,975;ν`. Para un límite unilateral del 95 %, `t_0,95;ν`. No se escribe `t_0,95` para un intervalo bilateral.
- **Sección eficaz:** cada cálculo declara qué valor de σ usa cada instrumento.

### 3.2 Unidades de la medición

Se definen lectura, semiciclo, ciclo, corrida, día y resultado de calibración. Cada análisis declara:
1. la pregunta;
2. la variable de respuesta;
3. la unidad de réplica;
4. a qué se generaliza el resultado.

No hay una unidad de réplica universal. Las lecturas de un ciclo caracterizan la variación dentro de ese ciclo (repetibilidad de corto plazo). No sustituyen a ciclos independientes para la variación entre ciclos ni a días distintos para la precisión intermedia.

### 3.3 Variable de análisis del certificado F-PSMT-01

En los niveles con ozono, la concentración que genera el SRP cambia de un día a otro. En el nivel 4 las medias diarias del SRP van de 127,22 a 131,23 nmol/mol. Por eso, en el mismo nivel:

| Variable | s (48 datos) |
|---|---:|
| Indicaciones brutas del Level 2 | 1,60 nmol/mol |
| Diferencias con signo `d = y − x` | 0,40 nmol/mol |
| Desviación intradía agrupada de las indicaciones | 0,34 nmol/mol |

La dispersión de las indicaciones brutas mide sobre todo el generador, no el Level 2. Regla del curso: **para estudiar el comportamiento del Level 2 dentro de un nivel se usa la diferencia con signo `d = y − x`.** Para varios niveles se usa la regresión de y contra x (M7).

Límites de la regla:
- Restar la referencia no garantiza independencia ni varianza constante. Con sesgo proporcional, `d` sigue dependiendo de la concentración.
- No se usa el valor absoluto `|y − x|`: pierde el signo y oculta sesgos opuestos.
- En I y A se enseña también el modelo de y en función de x con efecto día, como alternativa a `d`.

### 3.4 Subconjuntos de datos

Cada práctica dice qué subconjunto usa. Se preparan en CSV con trazabilidad a las celdas del libro:

| Código | Contenido | Uso |
|---|---|---|
| S1 | Un nivel: 6 días × 8 lecturas, con referencia, indicación y `d` con signo | Descriptiva, normalidad, IC, t, ANOVA de días |
| S2 | Un día: 12 niveles con la media de referencia e indicación de cada uno | Recta, residuos, función de uso |
| S3 | Ceros de los 6 días | Ceros negativos, límite de detección |
| S4 | Certificado completo 12 × 8 × 6 | Nivel I y A |
| S5 | R&R con errores con signo, en las campañas que se puedan reconstruir | M6 y caso D |

---

## 4. Estructura del curso

| Bloque | Módulo | Tema | Cambio respecto del temario actual |
|---|---|---|---|
| Inicio | **M0** | Datos, herramientas y convenciones | **Nuevo** |
| I | M1 | Fotometría UV y trazabilidad | Correcciones |
| I | M2 | Descriptiva y análisis exploratorio | Pruebas de atípicos salen a M4 y M6 |
| I | M3 | Probabilidad y distribuciones | Dependencia temporal; la propagación D → x pasa a M8 |
| I | M4 | Inferencia | Recibe Grubbs y Dixon, IC de una varianza, incertidumbre de s |
| II | M5 | Diseño de experimentos | Unidades de la medición |
| II | M6 | ANOVA y precisión | Variable `d` con signo; R&R con errores con signo |
| II | M7 | Regresión y función de calibración | Predicción inversa completa; supuestos |
| II | M8 | Incertidumbre y CMC | Kragten; lectura, promedio y resultado futuro; presupuestos rotulados |
| III | M10 | Conformidad y certificado | Antes que M9; tres productos; E_n; tabla de criterios completa |
| III | M11 | Control estadístico y deriva | Carta X-MR; límites propios |
| III | M9 | Comparación clave | Después de M10 y M11 |
| III | M12 | Redes de monitoreo | AB y AS; signos mezclados; signo del cambio de escala |
| Cierre | M13 | Métodos numéricos: Monte Carlo y remuestreo | **Deja de ser optativo**; tiene celda en los tres niveles |
| Cierre | T | Taller integrador | Versión por nivel y competencia de escalar |

**Orden del bloque III.** M10 y M11 son parte del trabajo de todas las calibraciones; M9 es el caso especial del patrón nacional. M10 solo necesitaba a M9 para la fila del BIPM en la tabla de criterios, y esa fila se completa en M9. Se conserva la numeración de los módulos para no romper las referencias cruzadas; solo cambia el orden de impartición.

**M13 en el núcleo.** El temario actual lo deja como optativo, lo que contradice el criterio 2. Se convierte en un módulo con práctica en los tres niveles. La calibración multivariada (PCR, PLS) se quita del curso porque no aplica a un fotómetro de una sola longitud de onda. El uso de herramientas de IA pasa a M0.

---

## 5. Contenido por módulo

Formato: **Corregir** lista lo que hoy está mal o ambiguo. **B / I / A** dice qué se enseña y se practica en cada nivel; cada nivel incluye todo el anterior.

### M0. Datos, herramientas y convenciones (nuevo)

**Por qué:** las tres auditorías encontraron errores que nacen de datos mal preparados (concentraciones distintas mezcladas, valores absolutos, rangos incompletos). Hace falta enseñar a preparar la tabla antes de analizarla.

- **B:** importar un CSV del certificado; separador decimal, unidades, fechas e identificadores; dato faltante frente a cero; conservar el original y registrar cada exclusión o conversión; convenciones de la sección 3. Práctica: armar S1 desde el CSV del certificado y comprobar los conteos por día y nivel.
- **I:** diccionario de variables (instrumento, fecha, campaña, analista, día, corrida, paso, réplica, referencia, indicación, unidad, σ usada); hoja propia con funciones estadísticas. Práctica: armar S4 y verificar los emparejamientos referencia–indicación.
- **A:** Python o R; entorno reproducible; uso responsable de herramientas de IA (verificar datos, unidades y supuestos de cualquier resultado). Práctica: script que lee S4 y reproduce un resultado de la plantilla.

### M1. Fotometría UV y trazabilidad

**Corregir:**
- La ecuación de medida debe llevar el factor 10⁹ para dar nmol/mol, unidades coherentes para R, T, P, L y σ, y la definición de cada `f_ij` (celda y estado de gas).
- Sentido de la dependencia térmica: σ **disminuye** alrededor de 1 % **al aumentar** T de 218 a 295 K (Malicet 1995 §3.1).
- Cambio de escala de σ. Cada par de valores da un factor distinto, y hay que declarar cuál se usa:

  | Par | Cambio del resultado con las mismas señales |
  |---|---:|
  | 1,147 / 1,1329 ×10⁻¹⁷ cm² | +1,245 % |
  | 308,32 / 304,39 atm⁻¹ cm⁻¹ | +1,291 % |
  | 1,1476 / 1,1329 ×10⁻¹⁷ cm² | +1,298 % |

  No se atribuye la diferencia a una sola causa. Se enseña a identificar qué par implementó cada instrumento.
- **Signo.** Si el monitor sigue en la escala antigua y la auditoría usa la nueva, `(meas − audit)/audit ≈ −1,23 %` (con el primer par). Si ambos comparten la escala antigua, la diferencia relativa no revela el cambio.
- Quitar la práctica "dependencia térmica de σ en 210 nm, 253,6 nm y banda de Huggins": es espectroscopía, no estadística.
- Calibración, verificación y ajuste se distinguen con un ejercicio, no con una definición.

**B:** vocabulario (error, sesgo, corrección, exactitud, veracidad, precisión); cadena de trazabilidad; ecuación del SRP evaluada con plantilla. Prácticas:
- recalcular 80, 420 y 500 nmol/mol con σ antigua y nueva, declarando el par usado;
- clasificar cinco registros reales del laboratorio como calibración, verificación o ajuste.

**I:** por qué la medida con dos celdas cancela la deriva de la lámpara; correcciones de T y P. Práctica: efecto sobre la lectura del SRP de un sesgo no corregido de +1,5 °C en la sonda de temperatura o de −2 hPa en el barómetro, a 80 y 420 nmol/mol.

**A:** dependencia de σ con T y λ y su efecto en la CMC; cómo distinguir la temperatura de la ecuación, la corrección de densidad y la dependencia térmica de σ para no corregir dos veces. Práctica: signo y magnitud del error de una red cuando monitor y auditoría usan escalas distintas, en los cuatro casos posibles.

### M2. Descriptiva y análisis exploratorio

**Corregir:**
- Grubbs y Dixon pasan a M4 (necesitan pruebas de hipótesis). Cochran pasa a M6 (compara varianzas entre grupos). h y k de Mandel pasan a M10, con los ensayos de aptitud (necesitan varios participantes).
- `P = 1 − (1 − P_i)^n` pasa a M4, con su condición: eventos independientes con la misma probabilidad.
- Práctica con "las 48 lecturas de un nivel": se reemplaza (ver B).

**B:** población y muestra; escalas; histograma, cuartiles, diagrama de caja; media, mediana; s, CV; dispersión de las lecturas (s) frente a dispersión de la media (s/√n); redondeo al final. Atípicos: cercas del diagrama de caja, z robusto con mediana y MAD, lista de verificación (cero, purga, estabilización, celda); ningún dato se elimina sin causa documentada. Prácticas con S1:
- comparar s de las 48 indicaciones brutas, s de las 48 diferencias `d` y s intradía (sección 3.3) y decidir cuál describe al Level 2;
- serie de un día, decisión sobre un extremo con la lista de verificación y resultado con y sin el dato.

**I:** lo mismo con S4: descriptiva de `d` por nivel en los 12 niveles. El CV no se usa cerca de cero.

**A:** asimetría y curtosis de `d` por nivel; resumen robusto del certificado completo y contraste con el resumen clásico.

### M3. Probabilidad y distribuciones

**Corregir:**
- `u(x)/x = u(D)/|D·ln D|` no sale de la regla `Var(aX + bY)`: es una derivada. Pasa a M8. Además no está definida en x = 0: allí se usa la incertidumbre absoluta.
- Origen de las cifras del término de D: 0,31 nmol/mol viene del NISTIR 6963 (2003) y 0,28 nmol/mol del SRP 6008 / BIPM. Hay que decir si cada una es u o U y elegir una como valor de trabajo del curso.
- "Deducir la desviación estándar de la rectangular" pasa al anexo A2.
- "Promediar reduce el ruido como 1/√n solo si son independientes" queda sin herramienta para comprobarlo: se agrega la dependencia temporal (ver abajo).

**B:** normal, rectangular (`a/√3`; resolución `δ/√12`), triangular (`a/√6`); varianza de un promedio y su condición de independencia; gráfico de la serie de lecturas; ceros negativos. Límite de detección con los ceros, con la convención que fije el curso (por ejemplo, 3·s₀ con ceros de días distintos). Prácticas:
- incertidumbre por resolución del Level 2 (0,1 nmol/mol) y del SRP, y comprobación del factor con números aleatorios en la hoja;
- nueve ceros del NISTIR 6963, Tabla 2, y los ceros de S3: ¿hay ozono negativo?, límite de detección;
- gráfico de la serie de S1: ¿las 8 lecturas de un día suben o bajan juntas?

**I:** reglas de la esperanza y la varianza con covarianza; gráfico de probabilidad normal de `d` por nivel; autocorrelación de lecturas consecutivas y qué cambia en `s/√n`; definiciones del límite de detección y por qué 3·s₀ es solo una convención. Práctica: autocorrelación de las 8 lecturas de cada día y decisión sobre cuántas promediar.

**A:** covarianza entre canales (0,000012 frente a 0,000089) y entre puntos (`u_b`); desviación de Allan; tamaño efectivo de muestra con sus condiciones (modelo de dependencia, serie suficientemente larga, sin concatenar días). Práctica: desviación de Allan de una serie larga del SRP y elección del tiempo de promediado.

### M4. Inferencia

**Corregir:**
- `n ≈ 15·(S/D)²` sin contexto. Se dan dos reglas, con α = 0,05 bilateral y potencia 0,80: una media o datos pareados ≈ 8·(σ/δ)²; dos grupos independientes ≈ 16·(σ/δ)² por grupo.
- La t pareada SRP–Level 2 sobre los 12 niveles supone un sesgo constante. Se hace **dentro de un nivel**, con las 6 diferencias diarias. Para varios niveles se usa la regresión (M7).
- IC "de la media de un nivel" con las 48 lecturas: usa pseudorréplicas. Se hace con las 6 medias diarias de `d`.
- La F es sensible a la no normalidad: no es la puerta automática para combinar días.

**B:** IC de una media con t; prueba t de un sesgo; valor p; errores tipo I y II; significación estadística frente a relevancia metrológica; un resultado no significativo no demuestra que no haya efecto. Práctica con S1: IC al 95 % del sesgo del Level 2 en un nivel con las 6 medias diarias de `d`, y decisión.

**I:** t pareada dentro de un nivel; Welch; prueba F; IC de una varianza (χ²), que M12 usa; incertidumbre de s con pocos datos, `u_rel(s) ≈ 1/√(2(n − 1))` (≈ 32 % con 6 días); potencia y tamaño de muestra con las dos reglas; Grubbs y Dixon con su condición; `P = 1 − (1 − α)^n`. Prácticas:
- t pareada en tres niveles de S4 y comparación con la recta de M7;
- ¿cuántos días hacen falta para detectar un sesgo de 1 nmol/mol?;
- IC de la desviación entre días con 6 días.

**A:** comparaciones múltiples; prueba de equivalencia (TOST) con un margen fijado de antemano; χ² de bondad de ajuste. Práctica: ¿son equivalentes dos analistas dentro de ±0,3 nmol/mol?

### M5. Diseño de experimentos

**Corregir:** definir las unidades de la medición (sección 3.2) y aplicarlas a cada diseño de la tabla de comparaciones.

**B:** respuesta, factores, niveles, unidad experimental; réplica frente a pseudorréplica; bloque; anidado y cruzado (reconocerlos). Práctica: en el diseño 12 × 8 × 6 del certificado, qué fuentes de variación separa, cuáles confunde y cuál es la unidad de réplica para cada pregunta.

**I:** factorial 2^k; robustez; potencia aplicada al diseño. Prácticas:
- factorial 2³ de robustez del Level 2 (flujo, acondicionamiento, temperatura) con el día como bloque;
- qué separa y qué confunde cada diseño de la tabla (BIPM, QAPP, SOP, TAD, EN 14625, ISO 13964).

**A:** anidado escalonado; diseño de un estudio R&R. Práctica: diseñar un R&R de CALAIRE que estime repetibilidad, día y analista, con sus grados de libertad.

### M6. ANOVA y precisión

**Corregir:**
- "Las lecturas consecutivas de un mismo ciclo subestiman la repetibilidad" es incorrecto. Se reemplaza por: "Las lecturas de un ciclo caracterizan la variación dentro de ese ciclo; no sustituyen a ciclos independientes para estimar la variación entre ciclos ni a días para la precisión intermedia."
- "Las Partes 2 y 4 de la ISO 5725 son para estudios interlaboratorio" es demasiado restrictivo: la Parte 4, cláusula 5, trata el sesgo de un laboratorio.
- Varianzas y desviaciones: `σ²_R&R = σ²_e + σ²_operador + σ²_interacción`; `s_R&R = √σ̂²_R&R`.
- `r = 2,8·s_r` y `R = 2,8·s_R` son límites aproximados de la diferencia entre dos resultados; no son tolerancias ni incertidumbres expandidas.
- El ANOVA del certificado se hace sobre `d` con signo, no sobre lecturas brutas.
- **Estudio R&R.** El libro analiza valores absolutos de los errores ("VALORES ABSOLUTOS", `BASE DE DATOS!B70`). Las F que hoy cita el temario (interacción significativa en 135, 360, 405 y 455 ppb) corresponden a esa respuesta y no se pueden enseñar como conclusiones sobre errores con signo. Se retiran hasta rehacer el análisis con signo; los niveles significativos pueden cambiar.
- Diez ANOVA, uno por nivel, al 5 % cada uno: hay multiplicidad.
- "Construir a mano la tabla ANOVA" y "deducir los cuadrados medios esperados" pasan a plantilla y al anexo A3.

**B:** ANOVA de un factor (día) con plantilla sobre `d` de un nivel; repetibilidad `s_r` dentro del día, desviación entre días y precisión intermedia con las fórmulas de la plantilla; límite r. Práctica con S1: ANOVA de días de `d` en el nivel 0 y en un nivel alto, y comparación con el mismo ANOVA sobre las lecturas brutas.

**I:** efectos fijos y aleatorios; dos factores cruzados y anidados con la tabla de cuadrados medios esperados **dada**; elección del denominador; residuos y heterocedasticidad entre niveles; Cochran; por qué el valor absoluto oculta sesgos de signo contrario (dos analistas con −0,30 y +0,30 dan la misma magnitud media); %R&R y número de categorías: por qué no sirven cuando las "piezas" son niveles fijados por diseño. Prácticas:
- identificar la estructura del R&R de CALAIRE (días anidados en analista × campaña) y escribir el modelo;
- ANOVA anidado sobre errores con signo en 2–3 niveles de S5;
- con un nivel, mismo análisis sobre `|e|` y sobre `e`: qué cambia en la conclusión.

**A:** modelo completo del R&R en todos los niveles; estimaciones negativas; grados de libertad por componente y Welch-Satterthwaite; multiplicidad; ISO 5725-3 frente a GUM; uso de las componentes como evaluaciones tipo A (GUM H.5) y qué fuentes cubren. Práctica: reanalizar el R&R completo con errores con signo y redactar qué se puede y qué no se puede concluir con 2 analistas y 3 campañas.

### M7. Regresión y función de calibración

**Corregir:**
- Fijar la convención `y = a + b·x` (sección 3.1).
- `cov(a,b) = −x̄·s²/S_xx` vale solo para OLS; no se reutiliza en WLS ni GGMR.
- Falta de ajuste con réplicas: exige réplicas del mismo valor de entrada. En el certificado el valor de referencia cambia entre días dentro de un nivel, y el cero inicial y el final son dos pasos, no dos niveles distintos. Se usa un ejemplo que cumpla los supuestos, o se revisa la agrupación antes de aplicar la F.
- χ² con n − 2 exige una matriz de incertidumbre adecuada; `|residuo ponderado| ≤ 2` es regla de la ISO 6143, no universal.
- Para "¿la recta es la identidad?" interesan a la vez intercepto 0 y pendiente 1, no la prueba de pendiente distinta de cero.
- "Ejemplo B.2.1 de la ISO 6143 (NO medido por absorción UV)": reescribir como "mezclas de monóxido de nitrógeno (NO) en nitrógeno; el método no es absorción UV".
- "Deducir las ecuaciones normales" pasa al anexo A4.

**B:** recta OLS con plantilla sobre S2; residuos; R² no valida una calibración; comparar a y b con el criterio fijado en M10; aplicar `x̂ = (y − a)/b` dentro del intervalo calibrado; no extrapolar. Prácticas:
- recta de un día del certificado, gráfico de residuos y decisión;
- corregir tres lecturas nuevas con la función obtenida.

**I:** u(a), u(b), cov(a,b); bandas de confianza y de predicción; **predicción inversa con su incertidumbre** (u(a), u(b), cov(a,b) y la repetibilidad de la nueva lectura, `s_y/√p`); intercepto frente a recta por el origen; falta de ajuste cuando aplica; WLS. Prácticas:
- recta con S4 (medias diarias por nivel), residuos por día;
- incertidumbre de una lectura corregida a 80 y 420 nmol/mol;
- los mismos 12 pares por OLS y WLS, con a, b, u(a), u(b), cov(a,b) y χ²_obs.

**A:** forma matricial; GDR, GMR, GGMR (tabla de la ISO/TS 28037); validación con χ²; condiciones de cada método. Práctica: reproducir un ejemplo resuelto de la ISO/TS 28037 y el ejemplo B.2.1 de la ISO 6143, y comparar con el resultado de la propia implementación.

### M8. Incertidumbre y CMC

**Corregir:**
- **Presupuestos rotulados.** Se trabajan tres, cada uno con su nombre:

  | Presupuesto | Expresión | Estatus |
  |---|---|---|
  | NIST SRP 6008 (2017) | `√(0,28² + (0,011·x)²)` | Histórico. Incluye u(σ) = 1,06 % del valor anterior de σ |
  | BIPM-SRP27 | `√(0,28² + (0,00292·x)²)` | Sin σ: se cancela entre fotómetros con el mismo σ |
  | Escenario didáctico | `√(0,28² + (0,00425·x)²)` | Suma u(σ)/σ = 0,309 % del valor de 2025 al de SRP27. Ejercicio de cálculo, no presupuesto vigente |

  El presupuesto vigente del SRP 55 sale de su propia documentación (pendiente, sección 11).
- "Desarrollo de Taylor" y "derivar los coeficientes de sensibilidad" pasan al anexo A5. Los coeficientes se dan y se comprueban numéricamente.
- `k = t(ν_eff) en lugar de k = 2` es demasiado fuerte: k = 2 si ν_eff es grande; con pocos días, `k = t_0,975;ν_eff`.
- Tipo A y tipo B son formas de evaluar, no sinónimos de aleatorio y sistemático.
- "La plantilla aplica `max(U, CMC)`": es cierto (`Uexp!Q8` toma el mayor entre la U calculada y la curva). Después hay una segunda etapa que modifica la curva (`EcuOffset`, `Uexp!U22`). Se enseñan como dos operaciones distintas.
- "Varias magnitudes de salida" pasa entero a M13.

**B:** modelo de medición; tipo A: **¿s o s/√n?** según el cliente use una lectura o un promedio; tipo B a partir de un certificado, `u = U/k`; resolución; presupuesto con plantilla y método de Kragten (sensibilidades numéricas); U = k·u_c; redondeo; U calculada frente a CMC y regla del máximo. Prácticas:
- presupuesto de un punto de la calibración del Level 2 con plantilla y Kragten;
- tomar la U del certificado del SRP 55 y convertirla a u;
- ante tres usos (una lectura, el promedio de un día, el promedio de seis días), decir qué término tipo A corresponde.

**I:** coeficientes de sensibilidad dados y comprobados con Kragten; entradas correlacionadas; ν_eff y k; **lectura, promedio y resultado futuro**: en un modelo simple, la incertidumbre estadística del promedio de m días con n lecturas es `σ²_día/m + σ²_e/(mn)`, y una lectura futura de otro día no se divide por esos tamaños; las contribuciones comunes del patrón no bajan con más lecturas; sesgo conocido no corregido; deriva entre calibraciones como contribución (con M11); evitar el doble conteo entre repetibilidad, residuo de la recta y precisión intermedia; la incertidumbre del patrón sale de su propio certificado; propagación al cliente. Prácticas:
- presupuesto completo de un punto del Level 2 con ν_eff y k;
- **el caso de la plantilla:** la componente de repetibilidad se calcula con `STDEV.P` de 576 diferencias en valor absoluto de los 12 niveles y se divide por √576. Identificar los tres problemas (valor absoluto, mezcla de niveles, dividir por √n un resultado que no es un promedio de 576 lecturas) y calcular la componente por nivel con el modelo correcto;
- U de una lectura, de un promedio y de un uso futuro: qué cambia;
- llevar la U del Level 2 al presupuesto de un fotómetro de cliente.

**A:** covarianza `u_b` entre puntos; σ dentro o fuera del presupuesto según el resultado que se declara; límites del método lineal; formas de expresar la CMC (valor, intervalo, función, tabla; ILAC-P14 §4.2). Prácticas:
- presupuesto del SRP nacional a 80 y 420 nmol/mol con cada uno de los tres presupuestos rotulados;
- ajustar una función a U(x) en todo el intervalo y comprobar que no queda por debajo de ningún punto calculado; comparar con la curva desplazada de la plantilla.

### M10. Conformidad y certificado (se imparte antes que M9)

**Corregir:**
- **Tres productos distintos:** el resultado de calibración con su U; la función o corrección para el uso posterior; la declaración de conformidad, que solo existe si se pide o aplica. La regla de decisión es obligatoria solo cuando se declara conformidad (ISO/IEC 17025 §7.8.6).
- **Corrección.** `c = (y − y_0)·c_c/(y_c − y_0)` es un modelo de dos puntos (cero y span) con alcance propio. Se definen y_0, y_c y c_c y se distingue de la función multipunto de M7. Según el VIM (2.53), una corrección puede ser un sumando, un factor o una tabla. "Ajuste del instrumento" se reserva para cambiar sus parámetros.
- **Tabla de criterios.** Se agrega la columna "qué se verifica" y las filas que faltan:

  | Documento | Qué se verifica | Diseño | Criterio |
  |---|---|---|---|
  | SRP QAPP | SRP contra SRP | — | Pendiente 1,00 ± 0,01; intercepto 0 ± 1 ppb |
  | SRP QAPP, Tabla 7-1 (6×6) | Level 2 contra SRP | 6 días | RSD de 6 pendientes ≤ 3,7 %; s de 6 interceptos ≤ 1,5 ppb; pendiente 1,00 ± 3 %; intercepto 0 ± 3 ppb |
  | SRP SOP | SRP contra SRP | ≥ 6 ciclos | 1 ± 0,04 y 0 ± 4 ppb al calificar; 1 ± 0,03 y 0 ± 3 ppb al reverificar |
  | EPA TAD 2023 | Level 2/3 contra nivel superior | 3 ciclos | Pendiente 1,00 ± 0,03; intercepto 0 ± 3 ppb; s de pendientes < 0,0075 |
  | BIPM.QM-K1 | SRP nacional contra SRP27 | Protocolo A o B | Grado de equivalencia a 80 y 420 nmol/mol (se completa en M9) |

  Las cifras se verifican contra cada documento al redactar. El régimen que sigue CALAIRE para su Level 2 se escribe aquí una sola vez; M11 y el caso C lo citan (decisión pendiente, sección 11).
- Distinguir cuatro preguntas: ¿hay diferencia significativa?, ¿son compatibles?, ¿cumple la especificación?, ¿son equivalentes dentro de un margen? Un p > 0,05 no demuestra equivalencia.

**B:** regla de decisión simple y con banda de guarda; **E_n** con su condición (las dos U independientes); qué criterio de la tabla corresponde a cada verificación; contenido del certificado (mensurando, intervalo, método, resultados, U con k, trazabilidad, σ usada). Prácticas:
- decidir si un patrón de transferencia pasa, sin y con la incertidumbre, y redactar la declaración;
- E_n del Level 2 frente al SRP 55 en tres niveles;
- clasificar cinco situaciones: ¿qué criterio de la tabla aplica?

**I:** riesgo de falsa aceptación y de falso rechazo; TUR; corrección de lecturas con el modelo de dos puntos y con la función multipunto; **ensayos de aptitud y comparaciones nacionales** (ISO 13528: valor asignado, z, ζ, E_n). Prácticas:
- el mismo resultado frente a una hipótesis de diferencia, un margen práctico y una especificación: tres respuestas distintas;
- puntajes z y E_n de una comparación nacional simulada de cinco fotómetros.

**A:** riesgo específico y global (JCGM 106); decisión con covarianza; h y k de Mandel en una comparación con varios participantes. Práctica: banda de guarda para un riesgo de falsa aceptación fijado, declarando la distribución supuesta.

### M11. Control estadístico y deriva

**Corregir:**
- Nombrar la carta de individuales y rango móvil (X-MR), que es la que usa el caso C.
- Quitar "son criterios directamente aplicables" (EPA TAD): se cita el régimen fijado en M10.
- Límites de control frente a tolerancias; fase de establecimiento frente a fase de seguimiento. Los límites calculados con otro proceso (diez comparaciones del NIST) no vigilan el Level 2 de CALAIRE.
- Seis días no son un historial. Una tendencia contra el orden de corrida no es deriva en el tiempo si los intervalos son desiguales.

**B:** carta X-MR, reglas de alarma, acción ante una señal. Prácticas:
- carta de la pendiente con las diez comparaciones del NISTIR 6963 (aprender el método);
- ficha de actuación ante una alarma: investigar, estado del patrón, trabajos afectados, retorno al servicio.

**I:** regresión de la deriva contra el tiempo; predicción con incertidumbre; aporte de la deriva a la U del Level 2 durante su intervalo de uso. Práctica: con el historial propio del Level 2 (si existe) o una serie simulada rotulada, ajustar la deriva y decidir si hay que recalibrar antes.

**A:** intervalo de recalibración; límites con base propia; CUSUM y EWMA. Práctica: comparar la detección de un cambio de pendiente de 0,005 con X-MR, CUSUM y EWMA.

### M9. Comparación clave (se imparte después de M10 y M11)

**Corregir:**
- El resultado del caso B no es un grado de equivalencia oficial de BIPM.QM-K1: se rotula como "diferencia interpolada bajo un modelo didáctico". Los datos son de otros instrumentos (QAPP, SRP36 contra SRP7) y el ajuste supone `U_xy = 0`.
- `ggmr_fit` fija en cero los bloques cruzados. Sirve para `U_xy = 0`; el caso `U_xy ≠ 0` no se enseña hasta tener una herramienta verificada.
- "Gauss-Newton" pasa al anexo B.
- Cómo se verifica que la comparación respalda la CMC: se agrega.

**B:** qué es una comparación clave y qué significa el grado de equivalencia; con la recta y su covarianza **entregadas**, calcular D y U(D) a 80 y 420 nmol/mol con la plantilla, E_n y contraste con la CMC. Práctica: con los datos de la comparación propia (si se consiguen) o del caso B rotulado, calcular D, U(D) y E_n y decidir.

**I:** protocolos A y B; por qué el OLS no basta; armar U_x con u_b para la secuencia BIPM y compararla con la diagonal del OLS; ajuste GLS con el software validado (`U_xy = 0` declarado); D por interpolación con cov(a,b); coherencia entre la CMC y el resultado de la comparación. Prácticas:
- U_x de la secuencia BIPM;
- caso B: OLS frente a GLS, χ² y D a 80 y 420 nmol/mol.

**A:** formular el GLS completo; validar el software contra la ISO/TS 28037; extender a `U_xy ≠ 0` solo con herramienta verificada; tratamiento de los ceros inicial y final. Práctica: reproducir la comparación completa y redactar el informe de validación del cálculo.

### M12. Redes de monitoreo

**Corregir:**
- Definir `AB = media(|d_i|)` y `AS = s(|d_i|)`. El límite del sesgo absoluto no es el valor absoluto de la media con signo.
- El ejemplo actual solo tiene d_i positivos. Se agrega un segundo con signos mezclados.
- Los estimadores de 40 CFR 58 §4.1 usan los controles de un punto; no se mezclan con auditorías anuales ni NPAP.
- El CV regulatorio no es `s/|media|`.
- "Sesgo de +1,25 % por usar la sección eficaz antigua": declarar qué σ usa el monitor y cuál la auditoría; con el monitor en la escala antigua, d_i ≈ −1,23 %.
- El valor de diseño necesita el periodo de varios años y sus reglas de validez.

**B:** d_i, CV y sesgo con plantilla; diferencia entre esos indicadores (un año de verificaciones de un monitor) y la U de un certificado (una calibración). Prácticas:
- d_i = 1; 2; 0,5; 3; 1,5; 2,5 %: CV = 1,65 %, |sesgo| = 2,52 %;
- el mismo cálculo con signos mezclados.

**I:** origen de los límites con χ² y t (conecta con M4); efecto del cambio de σ en los d_i con el signo correcto; límite detectable inferior de 40 CFR 53. Práctica: cómo aparece el cambio de escala en los d_i de una red en los cuatro casos de escalas.

**A:** valor de diseño; EN 14625 frente a 40 CFR 53; contraste con la regulación nacional adoptada, si aplica. Práctica: ejemplo de la EPA 2014–2016 del valor de diseño.

### M13. Métodos numéricos: Monte Carlo y remuestreo

**Corregir:** deja de ser optativo. Se quitan PCR/PLS. El uso de herramientas de IA pasa a M0.

**B:** Monte Carlo en hoja de cálculo para un punto de la ecuación del SRP. Práctica: comparar con el resultado de Kragten del mismo punto (M8).

**I:** Monte Carlo de la predicción inversa; bootstrap remuestreando días completos. Prácticas:
- incertidumbre de una lectura corregida por Monte Carlo y por la fórmula de M7;
- bootstrap por días de la desviación entre días de un nivel.

**A:** pendiente e intercepto como salidas conjuntas (GUM-S2); Monte Carlo en ajuste de curvas; regresión no lineal y de distancia ortogonal; métodos robustos de la ISO 5725-5. Práctica: validar la propia implementación del GGMR por Monte Carlo.

---

## 6. Taller integrador por nivel

| Caso | B | I | A |
|---|---|---|---|
| **A · Calibración del Level 2** (F-PSMT-01) | S1 y S2: descriptiva de `d`, ANOVA de días, recta de un día, presupuesto con Kragten, decisión con E_n | S4: ANOVA de `d` por nivel, recta con medias diarias, predicción inversa, presupuesto con ν_eff, decisión; contraste con lo que reporta la plantilla | Como I, más propagación al cliente, función U(x) y bootstrap por días |
| **B · Comparación clave** | D, U(D) y E_n con la recta entregada | OLS frente a GLS con U_x armada; D a 80 y 420 nmol/mol | Caso completo; reproducir las cifras del QAPP y explicar sus inconsistencias; validación del código |
| **C · Historial del Level 2** | Carta X-MR con las comparaciones del NIST; decisión con el criterio de M10 | Más la prueba de deriva | Más la prueba F, N frente a N − 1 e intervalo de recalibración |
| **D · Estudio R&R** | Factores y unidad de réplica; ANOVA de días de una campaña sobre `d` | ANOVA anidado sobre errores con signo en 2–3 niveles; efecto del valor absoluto | Modelo completo; diseño de un estudio nuevo |
| **Escalar** (B) | Ante seis situaciones reales, decidir si basta la plantilla o hay que escalar, y por qué | — | — |

**Cambios en los casos:**
- **Caso B:** unificar el §5 con el cálculo reproducido (variante i: a = −0,184237121; b = 0,998350748). Indicar que `0,28²·I` corresponde solo a la variante (ii). Rotular el resultado como didáctico. En I, como máximo dos preguntas de discusión sobre las fuentes.
- **Caso C:** las diez comparaciones del NIST (C2) sirven para aprender a construir la carta; los 6 días de CALAIRE (C1) describen una calibración. La superposición de C1 sobre la carta de C2 queda como ejercicio para reconocer una comparación inadecuada.
- **Casos A y D:** necesitan enunciado, datos en CSV (S1–S5) y solución de referencia por nivel, como B y C. No se trabajan sobre los libros de Excel en clase.

---

## 7. Evaluación

**Por módulo:** un ejercicio de cierre con respuesta numérica verificable. En B se agrega una situación de escalar.

**Taller:** rúbrica por caso y por nivel.

| Nivel | Pesos de la rúbrica |
|---|---|
| B | Datos y unidades 25 %; aplicación correcta del procedimiento 30 %; interpretación 25 %; escalar y registrar 20 % |
| I | Datos y unidades 20 %; elección y aplicación del método 25 %; diagnóstico e interpretación 25 %; presupuesto, decisión y documentación 30 % |
| A | Estructura del problema y supuestos 20 %; elección y comparación de modelos 30 %; validación y sensibilidad 30 %; consecuencias y límites de la decisión 20 % |

**Errores críticos** (no se aprueba si se cometen dentro del alcance del nivel):
- confundir U con u;
- invertir el signo de una corrección;
- mezclar escalas de σ sin declararlo;
- extrapolar la función de calibración;
- eliminar datos sin causa documentada;
- usar límites de control de otro proceso como propios;
- declarar conformidad sin criterio aplicable;
- tratar lecturas consecutivas como réplicas independientes para la variación entre días;
- describir el Level 2 con lecturas brutas de días con distinta concentración, o con el valor absoluto del error;
- dividir por √n una componente que no corresponde a un promedio de n lecturas independientes.

En I y A se agregan: justificar un método que no aplica a los datos y tomar un resultado no significativo como prueba de equivalencia.

El umbral de aprobación (A propone 75/100) se fija con el piloto.

---

## 8. Anexos

Material de consulta; no se usa en clase ni en las prácticas.

- **A1.** Por qué la varianza muestral divide por n − 1.
- **A2.** Desviación estándar de las distribuciones rectangular y triangular.
- **A3.** Cuadrados medios esperados de modelos cruzados y anidados; Welch-Satterthwaite.
- **A4.** Ecuaciones normales de OLS y WLS; forma matricial; función objetivo de la ISO/TS 28037.
- **A5.** Derivadas parciales de la ecuación del SRP; desarrollo de Taylor de la GUM.
- **B.** Algoritmo GLS/GGMR (Milton 2006; ISO/TS 28037 cláusula 10).
- **C.** Tablas t, χ² y F; factores de las cartas de control.
- **D.** Glosario único: términos del VIM en español, símbolos y convenciones de la sección 3.

---

## 9. Referencias

**Agregar:**
- VIM (JCGM 200), en particular 2.53 (corrección).
- JCGM 106 o ILAC G8 (reglas de decisión).
- ILAC-P14 §4.2 (expresión de la CMC).
- ISO 13528 (ensayos de aptitud: z, ζ, E_n).
- EA-4/02 o GUM G.6.6 (elección de k).
- Informe BIPM 2024/03, rev. 2025 (σ de 2025 y su incertidumbre).
- *A Practical Handbook on Measurement Uncertainty*, que ya está en `docs/` y no se usa: sirve para M8 en B.
- La fuente que fije la definición del límite de detección (M3).

**Corregir:**
- "Brereton apéndice A" en M3 y M4: verificar contra `chemometrics_a01.pdf` y citarlo igual en el temario y en el caso C.
- ISO 5725-4: citar la cláusula 5 en M6.

---

## 10. Lo que se descarta de las auditorías

| Propuesta | Origen | Motivo |
|---|---|---|
| Horas 48/80/32 y 30/50/66 | A, C | Las horas se calculan después; además, las revisiones mostraron que las de C no alcanzan para lo que promete |
| Rutas no acumulativas y básico sin estadística aplicada | A | Contradicen los perfiles acordados |
| Quitar M5, M6 y M9 de B | C | El criterio es por tema, no por módulo. B ejecuta esos temas con plantilla |
| "Lectura breve", "15 minutos", "una línea", "solo se menciona", "opcional", "repaso" | A, B, C | Contradicen el criterio 2. Cada caso se convirtió en una práctica o se movió de nivel |
| "La unidad de réplica es siempre el día, n = 6" | B | No es universal. Se reemplaza por la sección 3.2 |
| Derivar sensibilidades en I y A | B | Es una demostración. Se dan y se comprueban con Kragten |
| B trabaja con "un nivel y un día" | B | No permite un ANOVA de días ni una recta. Se reemplaza por los subconjuntos S1–S3 |
| IC y t sobre las 8 lecturas consecutivas de un día | C | Son pseudorréplicas. Se usan las 6 medias diarias de `d` |
| "La plantilla no aplica `max(U, CMC)`" | C | Falso: `Uexp!Q8` lo aplica. La curva desplazada es una etapa adicional |
| Sustituir la curva de CMC por `√(U₀² + (U₁x)²)` como requisito | C | ILAC-P14 admite varias formas. Queda como práctica de A con comprobación en todo el intervalo |
| `k = t_0,95(ν_eff)` para un intervalo bilateral | C | Es `t_0,975;ν` |
| El 1,25 % "se debe únicamente al truncamiento" | C | Hay tres pares con tres factores. Se enseña a identificar el par |
| La corrección "es solo `x_ref − y`" | C | El VIM admite sumando, factor o tabla |
| `n_eff = n(1 − r₁)/(1 + r₁)` como corrección general | C | Solo con sus condiciones, y en A |
| Cochran "para demostrar la heterocedasticidad" de 0 a 455 nmol/mol | C | Se espera por diseño; la prueba no aporta |
| Superponer los 6 días de CALAIRE sobre la carta del NIST como control | C | Esos límites no vigilan el Level 2 de CALAIRE |
| Factor de subestimación "de más de un orden de magnitud" para `√576` | C | Depende del nivel y del resultado. Se enseña el concepto, no un factor |
| Sumar el grado de equivalencia del SRP 55 a `Upatron` sin más | C | El presupuesto del patrón sale de su propia documentación |

---

## 11. Decisiones pendientes del usuario

1. **Régimen de criterios del Level 2:** QAPP 6×6, EPA TAD 2023 o procedimiento propio aprobado ante el INM. Se escribe una vez en M10.
2. **Datos de la comparación BIPM.QM-K1 propia de CALAIRE.** No están en `docs/`. Sin ellos, M9 y el caso B usan el caso actual rotulado como didáctico.
3. **Presupuesto vigente del SRP 55 y valor de σ que usa CALAIRE.** Sin ellos, M8 trabaja con los tres presupuestos rotulados.
4. **Errores con signo del R&R.** La campaña de febrero de 2023 se puede reconstruir desde el certificado. Hay que ver si existen los datos originales de las campañas de enero y agosto de 2022. Sin ellos, el caso D se limita a la campaña reconstruible o a datos simulados rotulados.
5. **Historial propio del Level 2** para la carta de M11 en I.
6. **Valor de trabajo del término de D:** 0,28 o 0,31 nmol/mol (M3).

---

## 12. Fuera del curso

Los hallazgos sobre la plantilla F-PSMT-01 afectan a un certificado real del Level 2. Son estos:
- `STDEV.P` de diferencias en valor absoluto de los 12 niveles, dividida por √576, como `Urepetibilidad`;
- `Uexp!G8`, que resta la media del patrón a la indicación;
- `Upatron`, que copia la ecuación del SRP27;
- la etapa de curva desplazada.

También afecta al R&R el uso de valores absolutos, `#REF!` en la fila 137 y rangos de 12 de 18 datos en 455 ppb.

Su efecto sobre la U reportada puede quedar tapado por la regla del máximo con la CMC, pero conviene llevarlos al responsable de la plantilla sin esperar a que el curso los use como ejemplo.

---

## 13. Insumos para el cálculo de horas

No se proponen cifras. Para calcularlas habrá que considerar:
- **Contenido que se agrega:** M0; M13 en los tres niveles; Kragten, E_n, límite de detección, `s` o `s/√n`, lectura / promedio / resultado futuro, ensayos de aptitud, dependencia temporal, competencia de escalar.
- **Contenido que sale de clase:** las demostraciones (a los anexos), PCR/PLS, la espectroscopía de la banda de Huggins, la construcción manual de tablas ANOVA, la discusión de fuentes del caso B en I.
- **Contenido que cambia de nivel:** pruebas de atípicos (M2 → M4/M6), propagación D → x (M3 → M8), Mandel (M2 → M10, A).
- **Bloques que más pesan y conviene medir en un piloto:** M6, M7, M8 y el caso A.
- **Tiempo de evaluación y devolución** dentro de cada nivel.
- **Preparación fuera de clase** (no son horas del curso): subconjuntos S1–S5, plantillas de B, soluciones de los casos A y D por nivel.
