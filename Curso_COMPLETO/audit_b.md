# Auditoría del curso: vacíos, errores, contradicciones y adaptación a tres niveles

**Objeto:** `temario_curso.md` (22-10-2026) y los casos del taller `casos_taller/caso_B_comparacion_clave.md` y `caso_C_historial_level2.md`.
**Fecha:** 23-10-2026.

**Criterios del encargo:**
- El curso debe poder darse en nivel básico (B), intermedio (I) o avanzado (A).
- Nada de demostraciones matemáticas en clase; si hacen falta, van en anexos.
- Las prácticas son de aplicación, no demostraciones.
- No se filosofa sobre los conceptos.

**Horas:** esta auditoría no propone horas. El temario deberá revisarlas después, con el alcance por nivel ya fijado.

**Cifras verificadas contra las fuentes de `docs/`.** Las que no se mencionan abajo cuadran.
- Presupuestos del SRP 6008 y del SRP27, incluida la combinación 0,00292 (2,89×10⁻³, 3,37×10⁻⁴ y 2,29×10⁻⁴).
- Criterio s_SRP27 < 1 nmol/mol del BIPM.
- Tabla D → U(x) del NISTIR 6963: 0,31 nmol/mol; 17 % a 1,8 nmol/mol; 0,057 % a 553 nmol/mol.
- Dependencia térmica de σ (Malicet 1995 §3.1).
- Criterios de la Tabla 7-1 del QAPP.
- Cuadrados medios esperados y F críticos del estudio R&R: F₀,₀₅;₁,₂ = 18,5 y F₀,₀₅;₂,₃₀ = 3,32.
- Ejemplo de la red de M12: CV = 1,65 %, |sesgo| = 2,52 %.
- Covarianza implícita del Caso B.

---

## 1. Resumen

1. **El curso no puede ser idéntico en los tres niveles.** Algunos temas no se pueden enseñar en B sin convertirlos en una receta que el operador no sabría cuándo falla. Se propone organizar el curso en **tres perfiles acumulativos**, ligados a la función de cada persona en el laboratorio (sección 2). Regla: en cada nivel, todo tema que se da se **enseña y se practica en clase** con datos de CALAIRE. Si un tema no se puede aplicar a un nivel, no se da en ese nivel: entra en el siguiente. No hay temas solo para mostrar ni lecturas. Hoy el temario asigna un nivel por módulo, lo que describe un curso que sube de dificultad, no tres versiones del mismo curso.
2. **Hay contradicciones internas que confundirían al operador:**
   - las lecturas consecutivas son pseudorréplicas en M5 y M6, pero se usan como réplicas independientes en M4 y M7;
   - el criterio de aceptación del Level 2 es distinto según el documento (QAPP 6×6 o EPA TAD);
   - la incertidumbre de σ es 1,06 % en M8 y 0,31 % en M1;
   - el Caso B da dos juegos de cifras para la misma variante.

   Detalle en la sección 4.
3. **Faltan conceptos de uso diario:** U/k de un certificado, s o s/√n en la tipo A, E_n, sesgo no corregido, deriva como contribución a U, límite de detección con los ceros, autocorrelación, incertidumbre de s con pocos datos, IC de una varianza (que M12 usa y M4 no enseña) y el método de Kragten para el nivel B. Detalle en la sección 5.
4. **Hay pruebas formales antes de su prerrequisito.** M2 presenta Grubbs, Dixon, Cochran y h/k de Mandel antes de que el curso enseñe pruebas de hipótesis (M4) y ANOVA (M6).
5. **Unas diez prácticas o puntos de teoría son demostraciones.** Se reescriben como aplicación en la sección 6.
6. **Faltan referencias base:** VIM (JCGM 200), JCGM 106 o ILAC G8 (reglas de decisión), ILAC P14 (CMC) e ISO 13528 (E_n, z, ζ). El *A Practical Handbook on Measurement Uncertainty* está en `docs/` sin usar y sirve para el nivel B de M8.

---

## 2. Criterio de niveles: tres perfiles acumulativos

| | Básico (B) | Intermedio (I) | Avanzado (A) |
|---|---|---|---|
| **Función en el laboratorio** | Ejecuta calibraciones y el control diario de los patrones | Firma presupuestos de incertidumbre y certificados con CMC | Responsable técnico de la comparación con el BIPM, de los estudios R&R y de la validación de cálculos |
| **Al terminar puede…** | Calcular con plantilla, interpretar resultados, decidir con criterios dados y **reconocer cuándo un caso necesita a alguien de nivel I o A** | Calcular con herramientas propias, elegir el método y justificar la elección | Formular el modelo, tratar casos no estándar y validar software |
| **Herramienta** | Hoja de cálculo con plantilla preparada | Hoja de cálculo propia con funciones estadísticas | Python o R, matrices, validación contra ejemplos normativos |
| **Fórmulas** | Se dan y se usan | Se dan, con una frase sobre su origen | Se dan en forma general; las demostraciones están en anexos |
| **Datos** | Un nivel y un día del certificado F-PSMT-01 | Certificado completo (12 × 8 × 6) | Certificado, estudio R&R y comparación BIPM propia |

**Se enseña:** el participante lo calcula, lo aplica a datos de CALAIRE y decide con el resultado.

**No se da en ese nivel:** el tema entra en el nivel siguiente. No se muestra a medias ni se deja como lectura.

Los perfiles son acumulativos: I incluye todo B, y A incluye todo I.

**Competencia transversal del nivel B:** detectar cuándo un caso se sale de la plantilla. Las señales son:
- datos correlacionados o lecturas consecutivas tratadas como réplicas;
- pocos días de datos (ν_eff pequeño);
- resultado cerca del límite de aceptación;
- atípicos sin causa;
- deriva en la carta de control;
- cambio de σ o de método.

Esta competencia se practica explícitamente en el taller.

---

## 3. Mapa del curso por nivel

Cada celda dice qué se enseña y se practica en ese nivel. Lo que no aparece en la celda B entra en I; lo que no aparece en la celda I entra en A.

| Módulo | Tema | B | I | A |
|---|---|---|---|---|
| M1 | Fotometría UV y trazabilidad | Vocabulario, cadena, ecuación del SRP evaluada con plantilla, recalcular 80, 420 y 500 nmol/mol con los dos σ | Más las dos celdas (por qué D cancela la deriva de la lámpara) y las correcciones de T y P | Más la dependencia de σ con T y λ y su efecto en la CMC |
| M2 | Descriptiva | Completo (atípicos con diagrama de caja, z robusto y lista de verificación) | Igual que B, con el certificado completo | Repaso en clase con datos propios |
| M3 | Probabilidad y distribuciones | Normal, rectangular, triangular, resolución, 1/√n, gráfico de la serie, ceros negativos | Más reglas de la varianza con covarianza, gráfico de probabilidad normal, autocorrelación, propagación D → x | Más covarianza entre canales y entre puntos (u_b), desviación de Allan |
| M4 | Inferencia | IC con t, prueba t de un sesgo, valor p, errores I y II | Más t pareada, Welch, F, IC de una varianza, potencia y tamaño de muestra, Grubbs y Dixon, incertidumbre de s | Más comparaciones múltiples, TOST, chi-cuadrado de ajuste |
| M5 | Diseño de experimentos | Réplica frente a pseudorréplica, bloque, anidado, identificar qué fuentes separa el diseño 12 × 8 × 6 y cuáles confunde | Más factorial 2^k, robustez, potencia del diseño | Más anidado escalonado y diseño de un estudio R&R |
| M6 | ANOVA y precisión | ANOVA de un factor (días) con plantilla, s_r, precisión intermedia, límite r | Más efectos aleatorios con tabla de CME dada, dos factores, residuos, Cochran, R&R en 1–2 niveles | Más modelo completo del R&R, elección del denominador, estimaciones negativas, ν por componente, ISO 5725-3 frente a GUM |
| M7 | Regresión | Recta con hoja de cálculo, residuos, R² no valida, comparar con criterios | Más u(a), u(b), cov(a,b), falta de ajuste con medias diarias, predicción inversa, origen sí o no, WLS | Más forma matricial, GDR, GMR, GGMR, χ²_obs |
| M8 | Incertidumbre y CMC | Modelo, tipo A (s o s/√n), tipo B (U/k, resolución), presupuesto con plantilla y Kragten, U = 2u, redondeo, de U a CMC | Más sensibilidades analíticas, correlación, ν_eff y k = t, deriva y sesgo no corregido, propagación al cliente | Más covarianza u_b, σ dentro o fuera del presupuesto, límites del método lineal |
| M9 | Comparación clave | Con los datos de la comparación propia, calcular D = x_NS − x_SRP27 y u(D) en cuadratura a 80 y 420 nmol/mol (protocolo A, ecs. [2]–[3]), E_n y contraste con la CMC | Más protocolo B, por qué no basta el OLS, armar U_x con u_b, ajuste GLS con software ya validado, D por interpolación con cov(a,b) | GLS completo con software validado, reproducir la comparación propia |
| M10 | Conformidad y certificado | Regla de decisión simple y con banda de guarda, E_n, qué criterio corresponde a cada cosa, contenido del certificado | Más riesgo de falsa aceptación y falso rechazo, TUR, corrección de lecturas | Más riesgo específico y global (JCGM 106), decisión con covarianza |
| M11 | Control y deriva | Carta X-MR, reglas de alarma, acción ante una señal | Más regresión de la deriva, predicción, aporte de la deriva a U | Más intervalo de recalibración, límites con base propia, CUSUM y EWMA |
| M12 | Redes | d_i, CV y sesgo con plantilla; diferencia entre esos indicadores y la U del certificado | Más el origen de los límites con χ² y t, efecto del σ antiguo en los d_i, límite de detección | Más valor de diseño, EN 14625 frente a 40 CFR 53 |
| M13 | Temas avanzados | — | Optativo | Monte Carlo, salidas múltiples, bootstrap por días, robustos de la ISO 5725-5 |
| T | Taller | Casos en versión B (sección 7) | Versión I | Versión A |

**Temas que entran en I (no se dan en B):**
- componentes de varianza y modelos anidados o cruzados;
- incertidumbre de parámetros de regresión y predicción inversa;
- entradas correlacionadas y ν_eff;
- potencia y tamaño de muestra;
- factoriales;
- riesgo probabilístico de decisión;
- deriva con predicción;
- origen de los límites estadísticos de la red (en B se calculan con plantilla);
- protocolo B y GLS de M9.

**Temas exclusivos de A:**
- GLS/GGMR, matrices de covarianza y covarianza común entre puntos;
- modelo completo del R&R;
- Monte Carlo, salidas múltiples y bootstrap;
- validación de software.

Con este criterio se corrige la etiqueta de nivel de los módulos del temario. Hoy M7 y M8 dicen "I" pero incluyen contenidos de A, y M9 dice "I–A" pero todo su contenido es de A. Lo que debe cambiar es la tabla de módulos, no los módulos: cada uno lleva su columna B/I/A.

---

## 4. Errores y contradicciones

Ordenados por gravedad.

| # | Dónde | Problema | Corrección |
|---|---|---|---|
| E1 | M4 práctica (IC con 48 lecturas), M3 (normalidad de las 48), M7 (falta de ajuste "con las 8 réplicas"), Caso A | **Contradicción con M5/M6.** Se enseña que las lecturas consecutivas son pseudorréplicas, pero después el IC, la normalidad y el error puro se calculan con las 48 lecturas (6 días × 8) o con las 8 seguidas como si fueran independientes. El IC sale demasiado estrecho, la F de falta de ajuste se infla y el histograma mezcla seis días. | Regla única para todo el curso: la unidad de réplica de la calibración es el **día**, n = 6. Las 8 lecturas de un día dan la repetibilidad dentro del día. La inferencia sobre un nivel usa las 6 medias diarias o el modelo anidado de M6. El error puro de M7 se calcula con las medias diarias. |
| E2 | M11 "En el SRP" frente a Caso C §2 | M11 dice que los criterios de la EPA TAD (3 ciclos, s de pendientes < 0,0075) "son directamente aplicables" al Level 2 de CALAIRE. El Caso C dice que el criterio aplicable es el 6×6 del QAPP y que la TAD es solo un contraste. Además, el Caso C reconoce que la TAD 2023 reemplaza al 6×6: el QAPP §6.2.3 remite a EPA-454/B-10-001, de 2010. | Decidir y escribir **una sola vez**, en M10, qué régimen sigue CALAIRE (procedimiento del INM, 6×6 heredado o TAD 2023) y por qué. M11 y el Caso C deben citar esa decisión. |
| E3 | Tabla de criterios de M10 | La fila del "SRP QAPP" (1,00 ± 0,01; 0 ± 1 ppb) es el criterio **SRP contra SRP**. Falta el criterio del QAPP para el Level 2 (Tabla 7-1: RSD de seis pendientes 3,7 %; s de seis interceptos 1,5; pendiente 1,00 ± 3 %; intercepto 0 ± 3 ppb), que es el que usa el Caso C. Tal como está, el operador aplicaría ±0,01 a su Level 2. | Agregar una columna "Qué se verifica" (SRP–SRP, Level 2–SRP, Level 3–Level 2) y la fila del 6×6. Hacer lo mismo con la fila del SOP. |
| E4 | M8 frente a M1 (incertidumbre de σ) | M1 da σ = 1,1329(35)×10⁻¹⁷ cm², o sea u_rel ≈ 0,31 %. M8 dice que el NIST incluye σ con 1,06×10⁻²·x. Ese 1,06 % viene del certificado SRP 6008 de 2017 (u(σ) = 1,22×10⁻¹⁹ sobre el valor convencional anterior) y no corresponde al valor de 2025. | Aclarar en M8 que 1,06 % es la incertidumbre del valor anterior y que con el valor CCQM 2025 sería ≈ 0,31 %. Práctica: recalcular u(x) a 420 nmol/mol con cada valor. |
| E5 | M3 frente a M8 (término de D) | M3 usa U(D) = 0,000017 → 0,31 nmol/mol (NISTIR 6963, 2003). M8 usa 0,28 nmol/mol (SRP 6008, u(D) = 1,4×10⁻⁵). Son dos cifras para la misma componente, con U en un caso y u en el otro, sin explicación. | Decir de qué documento y de qué época viene cada cifra. Elegir una como valor de trabajo del curso. Revisar si en el NISTIR U es expandida o estándar. |
| E6 | Caso B §5 frente a la tabla de §2–3 | Para la variante (i), la tabla da b = 0,998350748 y a = −0,184237121; el §5 dice b = 0,998340767 y a = −0,179540362. | Volver a correr `calc_casos.py` y dejar una sola cifra. |
| E7 | M8 teoría frente a la tabla de conceptos | M8 incluye "términos de orden superior, varias magnitudes de salida", y la tabla de conceptos asigna "varias magnitudes de salida" a M13. | En B e I solo se menciona que existen. Se tratan en M13 (A). |
| E8 | M4: "n ≈ 15·(S/D)²" | No se dice para qué prueba, α ni potencia. Para una media (α = 0,05 bilateral, potencia 0,80) el factor es ≈ 8. El 15–16 es **por grupo**, al comparar dos medias independientes. | Dar las dos reglas con su contexto: una media ≈ 8·(σ/δ)²; dos grupos ≈ 16·(σ/δ)² por grupo. |
| E9 | M4 práctica "t pareada SRP frente a Level 2 en un día" | Si los pares son los 12 niveles, la prueba supone un sesgo constante. Un sesgo proporcional (pendiente ≠ 1) hace que la media de las diferencias dependa de los niveles elegidos, y además la varianza cambia con el nivel. | Hacer la t pareada **dentro de un nivel**, con las diferencias de los 6 días. Para varios niveles, la herramienta es la regresión (M7). |
| E10 | M2 | Grubbs simple y doble, Dixon, Cochran y h/k de Mandel aparecen antes de las pruebas de hipótesis. Cochran supone un ANOVA. h/k de Mandel son para estudios interlaboratorio (ISO 5725-2), que M6 declara no aplicables a un solo laboratorio. | En M2: diagrama de caja, z robusto, lista de verificación y "no se elimina sin causa". Grubbs y Dixon pasan a M4. Cochran pasa a M6. Mandel se quita. |
| E11 | M8: "k = t(ν_eff) en lugar de k = 2 fijo" | "En lugar de" es demasiado fuerte. La práctica habitual (GUM G.6.6, EA-4/02) es k = 2 con ν_eff grande y t solo si ν_eff es pequeño. Con 6 días como tipo A dominante, ν_eff puede ser pequeño: ese es el mensaje útil. | "k = 2 si ν_eff es grande; con pocos días de datos, k = t₀,₉₇₅(ν_eff)." En B, reconocer la señal de "pocos días". |
| E12 | M1: "σ baja alrededor de 1 % entre 218 y 295 K" | No se indica el sentido. Según Malicet §3.1, σ disminuye 1,0 % **al subir** la temperatura de 218 a 295 K. | Escribir "disminuye ≈ 1 % al aumentar T de 218 a 295 K". La comparación entre 210 nm, 253,6 nm y la banda de Huggins se deja solo en A: es espectroscopía, no estadística. |
| E13 | M10: corrección `c = (y − y_0)·c_c/(y_c − y_0)` | Las variables no están definidas. Tampoco se relaciona con la función de calibración de M7 ni con la convención error/corrección de M1. | Definir y_0, y_c y c_c. Fijar una convención para todo el curso: error = indicación − referencia y corrección = −error, o bien la función inversa de M7. Mostrar cuál usa el certificado F-PSMT-01. |
| E14 | M7: "ejemplo B.2.1 de la ISO 6143 (NO medido por absorción UV)" | El paréntesis es ambiguo: "NO" puede leerse como óxido nítrico o como negación. | Reescribir, por ejemplo: "mezclas de NO; el método no es absorción UV". |
| E15 | Referencias de M3/M4 "Brereton apéndice A" frente a Caso C §5 | El Caso C dice que no pudo verificar esa cita contra la copia local, pero el temario la mantiene. | Verificar `chemometrics_a01.pdf` y citarlo en los dos lugares o en ninguno. |
| E16 | Unidades | El curso alterna nmol/mol (M1–M9) y ppb (R&R, QAPP, TAD) sin declararlo. | Nota en M1: "en este curso ppb = nmol/mol (fracción molar; gas ideal)". En los certificados se usa nmol/mol. |

---

## 5. Vacíos conceptuales

### 5.1 Conceptos que faltan

"Nivel mínimo" es el nivel desde el que se enseña. En los niveles anteriores no se da.

| Concepto | Por qué lo necesita el operador | Dónde | Nivel mínimo |
|---|---|---|---|
| Tipo B a partir de un certificado: u = U/k | Es la entrada más frecuente de un presupuesto (por ejemplo, la U del SRP 55 en la calibración del Level 2) | M8 | B |
| ¿s o s/√n en la tipo A? | Depende de si el cliente usa una lectura o un promedio. Es el error de presupuesto más común | M8, con base en M2 | B |
| Número E_n (y ζ) | Criterio estándar para comparar dos resultados con su U: Level 2 frente a SRP 55, ensayos de aptitud, clientes | M10 | B |
| Límite de detección y de cuantificación con los ceros (≈ 3·s₀) | M12 menciona el "límite detectable inferior" sin enseñarlo. M2 y M3 ya trabajan los ceros | M3 o M12 | B |
| Estadística robusta básica (mediana, MAD, z robusto) | Es la alternativa razonable a las pruebas de atípicos en B. Hoy solo está en M13 | M2 | B |
| Método de Kragten (sensibilidades numéricas en hoja de cálculo) | Permite hacer un presupuesto sin derivar. Es la vía para B y un control para I y A | M8 | B |
| Independencia de lecturas consecutivas: gráfico de la serie, autocorrelación, desviación de Allan | Justifica cuántas lecturas promediar. M3 afirma la regla 1/√n sin herramienta | M3 | B (gráfico), I (autocorrelación), A (Allan) |
| Deriva entre calibraciones como contribución a U | Une M11 con M8: la deriva de la carta entra en el presupuesto del Level 2 durante su intervalo de uso | M8 y M11 | I |
| Sesgo conocido no corregido | Pérdidas de O₃, aire cero, lámpara: M8 dice que son sesgos que "el operador vigila", pero no cómo entran en U si no se corrigen | M8 | I |
| Incertidumbre de s con n pequeño (u_rel(s) ≈ 1/√(2(n−1))) | Con 6 días, s tiene ≈ 30 % de incertidumbre. Explica el ν_eff pequeño y la poca potencia de la F | M4 y M8 | I |
| IC de una varianza (χ²) | M12 lo usa (límite del CV al 90 %); M4 solo enseña la prueba | M4 | I |
| Ensayos de aptitud y comparaciones nacionales (ISO 13528: z, E_n, valor asignado) | El laboratorio calibra los fotómetros del país y puede organizar comparaciones (ISO/IEC 17025 §7.7.2) | M10 o M12 | I |
| Coherencia entre la CMC y el resultado de la comparación clave | M9 afirma que la comparación "respalda las CMC", pero no dice cómo se verifica | M9 | I |
| Prueba de equivalencia (TOST) | Responde a "¿el analista no importa?". M6 ya advierte que un resultado no significativo no lo demuestra | M4 o M6 | A |

### 5.2 Contenido que sobra o pesa demasiado

| Contenido | Qué hacer |
|---|---|
| h/k de Mandel (M2) | Quitar o dejar en A |
| %R&R y número de categorías distintas (M6) | Una línea en B e I ("no se usan en calibración"); el detalle en A |
| Gauss-Newton e implementación del GLS (M9, M13) | Solo A |
| Calibración multivariada PCR/PLS (M13) | Una línea: no aplica a un fotómetro de una sola longitud de onda |
| Uso de herramientas de IA (M13) | Pasar a una sesión inicial de herramientas, como regla práctica: verificar datos, unidades y supuestos |

### 5.3 Secuencia y prerrequisitos

1. **De M2 a M4:** las pruebas de atípicos pasan a M4 (ver E10).
2. **M3:** la "primera propagación" (u(x)/x = u(D)/|D·ln D|) usa una derivada antes de M8. En B no se da; en I y A se aplica y se anuncia que M8 la generaliza.
3. **M10 antes que M9.** M10 solo depende de M9 para la fila del BIPM. Orden propuesto del bloque III: M10 → M11 → M9 → M12. En B, M9 se reduce al cálculo directo de D, u(D) y E_n, y puede ir al final.
4. **Welch-Satterthwaite** se define en M6 y otra vez en M8. Debe definirse en un solo lugar.
5. **Pseudorreplicación** aparece en M5 y M6. Está bien como refuerzo, siempre que después se aplique en M4, M7 y el Caso A (ver E1).
6. **Cartas X-MR:** el Caso C las usa, pero M11 solo dice "Shewhart". Hay que nombrarlas en M11.

---

## 6. Demostraciones y filosofía: qué va a anexo y cómo queda como aplicación

| Dónde | Hoy | En clase (aplicación) | Anexo |
|---|---|---|---|
| M2 | "por qué se divide por n − 1" | Una frase y una comprobación por simulación en la hoja de cálculo | Insesgamiento de s² |
| M3 práctica | "Deducir la desviación estándar de una distribución rectangular" | Usar a/√3 y a/√6 con la resolución del 49C y el redondeo del certificado; comprobar con números aleatorios | Varianza de la rectangular y la triangular |
| M6 teoría | "por qué el cociente sigue una distribución F" | Usar la F y decidir con el valor p | Distribución del cociente de cuadrados medios |
| M6 práctica | "Deducir los cuadrados medios esperados…" | Con la tabla de CME **dada**, elegir el denominador y estimar las componentes con los datos del R&R | Derivación de los CME cruzados y anidados |
| M7 teoría y práctica | "Deducir las ecuaciones normales y comprobarlas" | Calcular a, b, u(a) y u(b) con las fórmulas y verificar con ESTIMACION.LINEAL o software | Ecuaciones normales y forma matricial |
| M8 teoría | "Desarrollo de Taylor de primer orden" | Regla de propagación con coeficientes de sensibilidad y método de Kragten | Taylor y términos de orden superior |
| M8 práctica | "Derivar los coeficientes de sensibilidad respecto de L, P, T, σ y D" | B: tabla de coeficientes dada o Kragten. I y A: derivar los de esta ecuación, que son cocientes simples (es aplicación), y comprobarlos numéricamente | — |
| M9 teoría | GLS "por Gauss-Newton" | I: qué entra (U_x, U_y), qué sale (a, b, cov, χ²) y cómo se usa para decidir | Algoritmo (Milton 2006; ISO/TS 28037 cl. 10) |
| Caso B | Discusión sobre la orientación de los ejes, el divisor 10/11 del QAPP, la plausibilidad del redondeo y una covarianza cruzada sin datos | I: ajustar, calcular χ² y D a 80 y 420 nmol/mol y decidir, con dos preguntas de discusión como máximo | Reproducir las cifras del QAPP y explicar sus inconsistencias, solo en A |
| M1 | "Calibración, verificación y ajuste: tres actos distintos" | Ejercicio: clasificar cinco registros reales del laboratorio | — |

**Anexos propuestos:**
- **Anexo A (derivaciones):** n − 1, rectangular y triangular, CME, ecuaciones normales, u(a), u(b) y cov(a,b), Taylor.
- **Anexo B:** algoritmo GLS/GGMR.
- **Anexo C (tablas):** t, χ², F y factores de las cartas de control.

---

## 7. Taller por nivel

| Caso | B | I | A |
|---|---|---|---|
| A · Calibración del Level 2 | Un nivel y la recta de un día con plantilla: descriptiva, ANOVA de días, recta, presupuesto con Kragten, decisión con E_n | Certificado completo: ANOVA, falta de ajuste con medias diarias, presupuesto con ν_eff, decisión, contraste con la plantilla actual | Como I, más la propagación al cliente y bootstrap por días |
| B · Comparación clave | Con los datos de la comparación propia de CALAIRE: calcular D y u(D) a 80 y 420 nmol/mol con la ecuación directa del protocolo, E_n y contraste con la CMC | OLS frente a GLS con U_x armada; D a 80 y 420 nmol/mol | El caso actual completo, incluido reproducir las cifras del QAPP y explicar sus inconsistencias |
| C · Historial del Level 2 | Carta X-MR y decisión con el criterio que se fije en M10 (E2) | Más la prueba de deriva | Más la prueba F, N frente a N − 1 y la discusión del intervalo de recalibración |
| D · Estudio R&R | Identificar factores y unidad de réplica (quién, cuándo, cuántas veces); ANOVA de un factor (días) en una campaña | ANOVA anidado en 2–3 niveles | Modelo completo en todos los niveles; diseño de un estudio nuevo |
| Transversal (B) | Ante cinco situaciones reales, decidir si basta la plantilla o hay que escalar a I o A (competencia de la sección 2) | — | — |

**Sobre el Caso B actual.** Usa datos de EE. UU. redondeados y dedica gran parte del texto a advertencias. Es valioso en A, pero en I se vuelve una discusión de fuentes. Los datos de la comparación BIPM.QM-K1 propia del laboratorio deberían ser el caso principal en los tres niveles, como ya pide M9.

**Casos A y D:** no tienen enunciado ni solución de referencia. Hacen falta por nivel.

---

## 8. Otros faltantes para que el curso sea dictable

1. **Evaluación por nivel:**
   - en B e I, un ejercicio de cierre por módulo con respuesta numérica verificable;
   - en B, también la competencia de escalar casos;
   - en el taller, una rúbrica por caso.
2. **Plantillas de hoja de cálculo para B:** IC, prueba t, ANOVA de un factor, recta, presupuesto con Kragten, carta X-MR y E_n. Sin ellas, el nivel B no puede tratar M6–M8.
3. **Datos por nivel:** dejar en `casos_taller/` los CSV del certificado (un nivel, un día, completo) y del R&R, con la misma trazabilidad de celdas que ya tienen B y C.
4. **Glosario único del curso:**
   - términos del VIM en español;
   - símbolos: u, U, k, s, σ, D, x;
   - convención error/corrección.
5. **Sesión inicial de herramientas:** hoja de cálculo en B e I, Python o R en A.

---

## 9. Lo que está bien y conviene conservar

- Cada concepto se presenta con un dato del SRP o de CALAIRE. Es el mayor acierto del temario.
- La cadena de trazabilidad como hilo conductor, con su tabla de eslabones por módulo.
- El tratamiento del estudio R&R: estructura anidada, por qué una t no basta, interacción como parte de la reproducibilidad. Los CME y los F críticos cuadran.
- Las advertencias "cada criterio vale solo en su documento" y "QAPP frente a SOP se enseña tal cual".
- Los presupuestos del BIPM y del NIST, la tabla D → U(x) del NISTIR y el ejemplo de la red de M12 son correctos.
- La validación del GGMR contra la ISO/TS 28037 en el Caso B. Conviene mantenerla en A.
