# Evaluación Comparativa Integral de las Tres Auditorías del Curso (`audit_a.md`, `audit_b.md`, `audit_c.md`)

**Fecha:** 23 de octubre de 2026  
**Documentos evaluados:**
- **Auditoría A:** [`audit_a.md`](file:///home/w421/w421/calaire-stat/audit_a.md) (*Auditoría del curso de estadística aplicada a la fotometría de ozono con el SRP*)
- **Auditoría B:** [`audit_b.md`](file:///home/w421/w421/calaire-stat/audit_b.md) (*Auditoría del curso: vacíos, errores, contradicciones y adaptación a tres niveles*)
- **Auditoría C:** [`audit_c.md`](file:///home/w421/w421/calaire-stat/audit_c.md) (*Auditoría Integral del Curso: Estadística aplicada a la fotometría de ozono con el SRP*)

**Material de contraste:** [`temario_curso.md`](file:///home/w421/w421/calaire-stat/temario_curso.md), [`temario_build.py`](file:///home/w421/w421/calaire-stat/temario_build.py), [`casos_taller/caso_B_comparacion_clave.md`](file:///home/w421/w421/calaire-stat/casos_taller/caso_B_comparacion_clave.md), [`casos_taller/caso_C_historial_level2.md`](file:///home/w421/w421/calaire-stat/casos_taller/caso_C_historial_level2.md), [`casos_taller/calc_casos.py`](file:///home/w421/w421/calaire-stat/casos_taller/calc_casos.py), [`docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm`](file:///home/w421/w421/calaire-stat/docs/F-PSMT-01%20Certificado%20de%20Calibracion_G1-sn59756-324_TBH.xlsm) y [`docs/Resultados R&r_2022 2023 (1).xlsx`](file:///home/w421/w421/calaire-stat/docs/Resultados%20R&r_2022%202023%20(1).xlsx).

---

## 1. Resumen Ejecutivo y Matriz de Evaluación Global

Las tres auditorías coinciden en cuatro diagnósticos fundamentales sobre [`temario_curso.md`](file:///home/w421/w421/calaire-stat/temario_curso.md):
1. **El curso actual no resuelve la división en tres niveles (Básico, Intermedio, Avanzado):** etiquetar M1–M2 como Básico y M4–M12 como Intermedio deja al nivel Básico truncado en estadística descriptiva, pero pretender enseñar todo M1–M12 en nivel Básico desnaturaliza métodos que exigen madurez estadística (ANOVA mixto, GGMR, diseño experimental).
2. **Existen contradicciones técnicas y normativas internas:** la mezcla de la nueva sección eficaz CCQM.O3.2019 (`u_rel = 0,309 %`) en M1 con el presupuesto histórico de Hearn 1961 (`u_rel = 1,06 %`) en M8; la contradicción sobre la aplicabilidad de los criterios EPA TAD 2023 frente al diseño QAPP `6×6` entre M10, M11 y el Caso C; el mal uso de pruebas *t* pareadas o pruebas inferenciales antes de sus prerrequisitos; y la discrepancia numérica en el apartado 5 de [`caso_B_comparacion_clave.md`](file:///home/w421/w421/calaire-stat/casos_taller/caso_B_comparacion_clave.md).
3. **Sobran demostraciones matemáticas en las prácticas:** las deducciones algebraicas de M2, M3, M6, M7 y M8 deben salir del aula, pasar a anexos de consulta y sustituirse por ejercicios de aplicación con datos reales del laboratorio.
4. **Faltan puentes operativos en el flujo de datos del certificado:** desde el tratamiento de lecturas consecutivas (pseudorréplicas/autocorrelación) hasta el paso de la recta de calibración a la predicción inversa `x̂ = (y − a)/b`, su incertidumbre en uso y las reglas de decisión.

Sin embargo, **las tres auditorías difieren sustancialmente en su profundidad de verificación de los archivos reales del laboratorio, en la viabilidad de la arquitectura de niveles propuesta y en la calidad ejecutable de su plan de reforma**.

### Matriz Comparativa de Calificación por Criterio

| Criterio de evaluación | [`audit_a.md`](file:///home/w421/w421/calaire-stat/audit_a.md) | [`audit_b.md`](file:///home/w421/w421/calaire-stat/audit_b.md) | [`audit_c.md`](file:///home/w421/w421/calaire-stat/audit_c.md) |
|---|:---:|:---:|:---:|
| **1. Rigor metrológico, estadístico y normativo** | **9,2 / 10** | **8,3 / 10** | **9,6 / 10** |
| **2. Auditoría profunda de datos y libros Excel reales (`F-PSMT-01` y `R&R`)** | **5,5 / 10** | **4,0 / 10** | **10,0 / 10** |
| **3. Viabilidad y realismo de la arquitectura de 3 niveles y horas** | **6,5 / 10** *(48 / 80 / +32 h = 112–160 h)* | **6,8 / 10** *(Sin horas; mete M5, M6 y M9 en B)* | **9,5 / 10** *(30 / 50 / 66 h escalonadas)* |
| **4. Coherencia interna y pedagógica** | **8,8 / 10** | **7,4 / 10** *(Contradicciones en M6-B y M9-B)* | **9,5 / 10** |
| **5. Calidad de la sustitución de demostraciones por prácticas aplicadas** | **8,8 / 10** | **9,0 / 10** | **9,4 / 10** |
| **6. Calidad del plan de implementación y trazabilidad al repositorio** | **8,0 / 10** | **7,0 / 10** | **9,6 / 10** |
| **PROMEDIO PONDERADO GLOBAL** | **7,8 / 10** | **7,1 / 10** | **9,6 / 10** |

---

## 2. Evaluación Detallada de la Auditoría A ([`audit_a.md`](file:///home/w421/w421/calaire-stat/audit_a.md))

### 2.1 Tesis y estructura propuesta
La Auditoría A plantea que *interpretar una salida preparada con una plantilla no equivale a dominar ni saber elegir el método estadístico*. Por ello, rechaza tres versiones simétricas del temario y divide la oferta en tres programas diferenciados:
- **Curso básico operativo (48 h):** reorganizado en códigos propios (`B0` a `B8` + `TB`), enfocado en higiene de datos, uso de funciones y presupuestos ya aprobados, lectura de certificados y ejecución de acciones prescritas ante alarmas.
- **Curso principal intermedio (80 h):** módulos `M0` a `M12` + `TI` (11 h), concebido como el nivel mínimo para ejecutar y justificar calibraciones habituales (OLS/WLS, ANOVA sencillo de un factor, presupuesto GUM, reglas de decisión y cartas propias).
- **Extensión avanzada (32 h adicionales tras las 80 h intermedias = 112 h técnicas):** bloques `A1` a `A4` + `TA`, dedicados a modelos mixtos/anidados complejos (Caso D completo), GGMR con covarianzas generales (Caso B completo), Monte Carlo/Bootstrap agrupado y dependencia temporal.

### 2.2 Ventajas (Fortalezas)
1. **Excelente rigor institucional, regulatorio y de gobernanza metrológica:**
   - En **H03**, **H09**, **H10** y **H16** establece una distinción impecable entre *literatura de referencia externa* (EPA TAD, QAPP, NISTIR 6963) y *procedimientos formalmente adoptados por CALAIRE ante el INM/ONAC*. Advierte con total acierto que calcular un estadístico de la EPA sobre 6 días no convierte ese límite en criterio oficial del laboratorio si no está en su procedimiento vigente.
   - En **H16** separa con precisión quirúrgica tres productos que el temario original mezcla: (a) el resultado de calibración con su incertidumbre, (b) la función o corrección para el uso posterior, y (c) la declaración de conformidad (recordando que ISO/IEC 17025 §7.8.6 solo exige regla de decisión cuando se declara conformidad con una especificación).
2. **Detección de matices estadísticos finos en módulos aplicados:**
   - **En M12 (H17):** Es la única auditoría que señala que el ejemplo numérico de `d_i` del temario (`[1; 2; 0,5; 3; 1,5; 2,5] %`) usa exclusivamente valores positivos, lo que impide al alumno notar que en `40 CFR 58 Apéndice A` los estimadores `AB = media(|d_i|)` y `AS = s(|d_i|)` operan sobre **valores absolutos individuales**, no sobre el valor absoluto de la media con signo. También advierte que no deben mezclarse controles QC de un punto con auditorías anuales o NPAP.
   - **En M1 y M12 (H05):** Explicita el cambio de signo de la diferencia relativa `(meas − audit)/audit` según qué instrumento haya actualizado la sección eficaz `σ` y cuál permanezca en la escala antigua (`+1,245 %` frente a `−1,229 %`), e incluye el caso en que ambos comparten la escala antigua (donde el sesgo común pasa inadvertido en la comparación relativa).
   - **En M6 y Caso D (H11):** Aun confirmando los valores `F` del ANOVA del estudio R&R, advierte acertadamente sobre el problema de **multiplicidad** al ejecutar 10 pruebas `F` independientes (una por nivel de concentración) al 5 % nominal, y subraya que con un error medio por día el residual captura la variación de errores medios diarios dentro de `analista × campaña`, sin poder separar ruido de lectura, ciclo y efecto día.
   - **En M6 (H12):** Corrige la afirmación del temario de que la ISO 5725-4 es solo interlaboratorio (la cláusula 5 de ISO 5725-4:1994 cubre el sesgo de un solo laboratorio respecto a un valor de referencia) y corrige la imprecisión de igualar desviaciones estándar con sumas de varianzas sin raíz cuadrada (`σ²_R&R` vs. `s_R&R`).
3. **Incorporación de trazabilidad de datos (`M0` / Sección 4.1) y sistema formal de evaluación (Sección 7):**
   - Propone un módulo corto `M0` (2 h) sobre estructura de tablas de datos, diccionarios de variables y registro auditable de exclusiones/versiones.
   - Diseña rúbricas ponderadas para Básico, Intermedio y Avanzado, junto con una lista explícita de **errores críticos invalidantes** (confundir `U` con `u`, invertir el signo de una corrección, mezclar escalas de `σ`, extrapolar sin soporte, borrar datos para forzar cumplimiento).

### 2.3 Desventajas (Debilidades y omisiones)
1. **Inflación severa de horas y rigidez curricular (112 h a 160 h totales):**
   - El temario original tiene **62 h (66 h con M13)**. La Auditoría A lo expande a **48 h (Básico) + 80 h (Intermedio) + 32 h (Avanzado) = 160 h** de docencia distinta (o **112 h** para quien curse Intermedio + Avanzado). Además, declara que las 48 h del Básico *no se descuentan* de las 80 h del Intermedio (`48 + 80 = 128 h` para un operador que ascienda de Básico a Intermedio). En un laboratorio nacional con personal operativo limitado como CALAIRE, un programa de 112 a 160 horas sincrónicas es operativamente inviable.
2. **Desproporción entre duración (48 h) y alcance real del Curso Básico:**
   - Dedica **48 horas** al curso Básico, pero le prohíbe al estudiante ajustar siquiera una recta de mínimos cuadrados ordinarios (OLS), calcular una prueba *t* en un nivel o armar una tabla sencilla de presupuesto GUM en cuadratura: el alumno básico pasa 48 horas únicamente leyendo salidas ya calculadas y aplicando ecuaciones preaprobadas.
3. **Omisión de los errores metodológicos graves ocultos en los dos libros Excel reales de CALAIRE:**
   - Aunque la Auditoría A declara haber inspeccionado el XML de los libros y recalculado el ANOVA desde `B6:C23` de las 10 hojas del estudio R&R, **pasó por alto los dos hallazgos más graves en los datos reales del laboratorio**:
     - En [`Resultados R&r_2022 2023 (1).xlsx`](file:///home/w421/w421/calaire-stat/docs/Resultados%20R&r_2022%202023%20(1).xlsx), no advirtió que las celdas `B6:C23` de las 10 hojas contienen **valores absolutos de los errores (`|y − x|`)**, rotulados explícitamente como `VALORES ABSOLUTOS` en `BASE DE DATOS!B70`, lo que destruye la normalidad e invalida el ANOVA al ocultar sesgos de signo contrario entre analistas. Tampoco vio los `#REF!` de la fila 137 ni el promedio desplazado de la fila 138 en `BASE DE DATOS`.
     - En [`F-PSMT-01`](file:///home/w421/w421/calaire-stat/docs/F-PSMT-01%20Certificado%20de%20Calibracion_G1-sn59756-324_TBH.xlsm), no advirtió que en los niveles con ozono la concentración generada por el SRP cambia de un día a otro (por lo que agrupar las 48 lecturas brutas `y_jk` mezcla 6 niveles físicos distintos), ni detectó que `BD_DIAS!E8:E10` calcula `STDEV.P` sobre las 576 diferencias absolutas de todos los niveles y divide entre `√576 = 24` (`0,0105 nmol/mol`), ni vio el error `Y − Xprom` en `Uexp!G8`, ni analizó el desplazamiento cúbico de `EcuOffset` (limitándose a mirar `Uexp!Q8`).
4. **Ruptura de la nomenclatura del generador `temario_build.py`:**
   - Al renombrar los módulos en Básico (`B0–B8`) y en Avanzado (`A1–A4`) en lugar de mantener una matriz clara sobre `M1–M13`, dificulta la actualización directa del generador [`temario_build.py`](file:///home/w421/w421/calaire-stat/temario_build.py).

### 2.4 Calidad del plan y coherencia
- **Coherencia interna:** Muy alta (8,8/10). Sus criterios epistemológicos (distinguir usar una plantilla, elegir un método y validar un modelo) se respetan rigurosamente en todo el texto.
- **Calidad del plan:** Muy buena como marco de aseguramiento de calidad docente y criterios de evaluación (Sección 9), pero **poco realista en carga horaria** y con una laguna importante en la auditoría de las fórmulas internas de los libros Excel de CALAIRE.

---

## 3. Evaluación Detallada de la Auditoría B ([`audit_b.md`](file:///home/w421/w421/calaire-stat/audit_b.md))

### 3.1 Tesis y estructura propuesta
La Auditoría B propone organizar el curso en **tres perfiles acumulativos (B, I, A)** asociados a la función real dentro de CALAIRE:
- **Básico (B):** Operador que ejecuta calibraciones y controles diarios con plantillas de hoja de cálculo, interpreta resultados sobre **un nivel y un día** del certificado, y **detecta señales de alerta para escalar el caso a nivel I o A**.
- **Intermedio (I):** Analista que firma presupuestos de incertidumbre y certificados con CMC, trabajando con el certificado completo (`12 × 8 × 6`) y sus propias hojas de cálculo.
- **Avanzado (A):** Responsable técnico de la comparación con el BIPM, de los estudios R&R y de la validación de software en Python/R.
Mantiene los módulos `M1–M12` en los tres niveles mediante una tabla de tres columnas (`B | I | A`), dejando `M13` para el Avanzado, pero **declina asignar horas** (*"esta auditoría no propone horas"*).

### 3.2 Ventajas (Fortalezas)
1. **Gran claridad pedagógica y definición del perfil funcional:**
   - La tabla de la Sección 2 (función en el laboratorio, qué puede hacer al terminar, herramienta, fórmulas y subconjunto de datos) es sumamente clara y sintética.
   - Define una **competencia transversal de gran valor práctico para el Nivel Básico**: reconocer cuándo un caso se sale de la plantilla (datos correlacionados, pocos días con `ν_eff` pequeño, resultado cercano al límite, atípico sin causa, deriva en carta de control o cambio de `σ`) y escalarlo a nivel I o A, dedicándole incluso un bloque específico del taller.
2. **Aportes metodológicos y didácticos sumamente acertados:**
   - **Método de Kragten en M8 (Nivel Básico):** Proponer el método numérico de Kragten en hoja de cálculo para propagar incertidumbre en Nivel Básico (y como control numérico de las derivadas analíticas en Nivel Intermedio/Avanzado) es una excelente idea práctica que evita derivar analíticamente sin convertir la propagación en una caja negra.
   - **Nuevos conceptos operativos pertinentes (Sección 5.1):** Identifica vacíos muy útiles como enseñar explícitamente `u = U/k` al leer el certificado de un patrón, el **límite de detección/cuantificación (`LOD ≈ 3·s_0`)** aprovechando las lecturas de aire cero de M2/M3, la **incertidumbre relativa de una desviación estándar muestral con pocos datos (`u_rel(s) ≈ 1/√(2(n−1))`)** (que explica de forma intuitiva por qué con `n = 6` días `s` tiene ~32 % de incertidumbre), la **desviación de Allan** para series temporales en Nivel Avanzado (M3), y la incorporación formal del **sesgo no corregido** y de la **deriva interanual** al presupuesto de incertidumbre (M8/M11).
   - **Propuesta de reordenamiento en el Bloque III (`M10 → M11 → M9 → M12`):** Señala con razón que M10 (certificado y conformidad) y M11 (cartas de control) son parte del flujo general de todas las calibraciones del laboratorio, mientras que M9 (comparación clave BIPM con GLS/GGMR) es un caso especial del patrón primario que pedagógicamente encaja mejor después de M10–M11.
3. **Detección puntual de detalles en los textos de `docs/`:**
   - Detecta la discrepancia entre `0,31 nmol/mol` (NISTIR 6963, usado en M3) y `0,28 nmol/mol` (SRP 6008 / BIPM, usado en M8) para la contribución de `D` (**E5**).
   - Precisa el sentido físico de la dependencia térmica de `σ` en Malicet 1995 §3.1 (**E12**: `σ` *disminuye* ~1 % al *aumentar* `T` de 218 a 295 K).
   - Detecta la ambigüedad gramatical en M7: `"ejemplo B.2.1 de la ISO 6143 (NO medido por absorción UV)"` donde `"NO"` es óxido nítrico (`NO`), pero en español se lee como negación (**E14**).
   - Señala que en [`caso_C_historial_level2.md`](file:///home/w421/w421/calaire-stat/casos_taller/caso_C_historial_level2.md) se descartó la cita a `"Brereton apéndice A"`, mientras que [`temario_curso.md`](file:///home/w421/w421/calaire-stat/temario_curso.md) la mantuvo en M3/M4 (**E15**).

### 3.3 Desventajas (Debilidades y omisiones)
1. **Ausencia total de planificación horaria:**
   - Al negarse a proponer horas por módulo y por nivel, deja sin resolver uno de los problemas centrales del temario (la sobrecarga de M6 en 7 h, M7 en 5 h, M8 en 6 h y el taller en 8 h, y cuánto dura cada modalidad B, I y A). Un plan curricular sin asignación de horas no es directamente ejecutable.
2. **Contradicciones internas sobre qué entra en el Nivel Básico (M5, M6 y M9):**
   - En la Sección 1 y 2 establece como regla que *"si un tema no se puede aplicar a un nivel, no se da en ese nivel: entra en el siguiente"*. Sin embargo, al forzar que todos los módulos M1–M12 tengan celda en `B`:
     - **Contradicción en M6 (ANOVA):** En la tabla de la Sección 3 (fila M6, columna B) y en la Sección 7 (Caso A y D, columna B) exige en Nivel Básico *"ANOVA de un factor (días) con plantilla, `s_r`, precisión intermedia, límite `r`"*. Pero cinco líneas más abajo, bajo el título **"Temas que entran en I (no se dan en B)"**, escribe textualmente: *"componentes de varianza y modelos anidados o cruzados"*. Calcular la precisión intermedia interdía a partir de un ANOVA de días requiere, por definición, descomponer varianzas y estimar la componente de varianza entre días (`σ̂²_día = (MS_entre − MS_dentro)/n`). Además, en la Sección 2 había definido que el Nivel Básico trabaja solo con *"un nivel y un día del certificado"*, con lo cual es imposible hacer un ANOVA entre días con datos de un solo día.
     - **Error de diseño y de disponibilidad de datos en M9 y Caso B (Nivel Básico):** En M9 (columna B) y Caso B (columna B) pide que el Nivel Básico use *"los datos de la comparación propia de CALAIRE"* para calcular `D = x_NS − x_SRP27` y `u(D)` en cuadratura a 80 y 420 nmol/mol con las ecuaciones directas [2]–[3] del Protocolo A del BIPM. Esto tiene dos fallos: (a) **esos datos de la comparación propia CALAIRE–BIPM no existen en el repositorio** (`docs/` ni `casos_taller/`), y (b) en la comparación BIPM.QM-K1 los puntos medidos siguen la secuencia nominal (`0, 220, 80, 420...`), pero las concentraciones reales generadas (`x_SRP27`) nunca son exactamente `80,000` ni `420,000 nmol/mol`, y el grado de equivalencia oficial de un SRP se obtiene de la relación lineal ajustada por GLS, no de restar dos lecturas aisladas sin ajuste.
3. **Omisión completa de los errores en los libros Excel reales (`F-PSMT-01` y `Resultados R&r`):**
   - No inspeccionó las fórmulas ni los datos internos de los libros Excel del laboratorio:
     - Afirma en el preámbulo y en la Sección 9 que el tratamiento del estudio R&R está bien, **sin notar que las 10 hojas del libro R&R contienen valores absolutos (`|y − x|`)** ni ver los `#REF!` y rangos desplazados de `BASE DE DATOS`.
     - En **E1** diagnostica que el problema de analizar las 48 lecturas de un nivel en `F-PSMT-01` es únicamente la *pseudorreplicación* de las 8 lecturas intradía, **sin darse cuenta de que en `F-PSMT-01` el generador de ozono del SRP produjo concentraciones distintas cada uno de los 6 días** (ej. de `127,2` a `131,2 nmol/mol` en el Nivel 4), por lo que ni siquiera las 6 medias diarias brutas `ȳ_j` pueden promediarse ni meterse en un ANOVA sin antes restar la referencia del SRP (`d_jk = y_jk − x_jk`).
     - Tampoco detectó el `STDEV.P(ABS(...))/√576` de `BD_DIAS`, ni el error `Y − Xprom` de `Uexp!G8`, ni el polinomio cúbico con desplazamiento de `EcuOffset`.

### 3.4 Calidad del plan y coherencia
- **Coherencia interna:** Media-baja (7,4/10) debido a las contradicciones entre el alcance de datos de B ("un día") y las tareas de B ("ANOVA de días y precisión intermedia"), así como entre la tabla de M6-B y la lista de exclusiones de B, y el uso de datos inexistentes para M9-B.
- **Calidad del plan:** Es un excelente documento de **aportes conceptuales y pedagógicos puntuales** (Kragten, señales de escalamiento, reordenamiento del Bloque III, micro-correcciones textuales), pero **insuficiente como plan maestro** por carecer de horas, no auditar los libros Excel y presentar inconsistencias en el diseño del nivel Básico.

---

## 4. Evaluación Detallada de la Auditoría C ([`audit_c.md`](file:///home/w421/w421/calaire-stat/audit_c.md))

### 4.1 Tesis y estructura propuesta
La Auditoría C resuelve el problema de los tres niveles combinando dos decisiones: (1) **el Nivel Básico debe cerrar el ciclo operativo completo del laboratorio de principio a fin** (incluyendo regresión OLS en M7, presupuesto GUM tabular en M8, certificado en M10 y lectura de cartas `X–MR` en M11), y (2) **los módulos y temas que por su naturaleza matemática o estadística no son básicos suben íntegramente a Intermedio o Avanzado**. Así, diseña tres modalidades escalonadas y acumulativas que respetan el techo de 66 h del curso original:
- **Nivel Básico (Operativo — 30 h):** Cubre `M1` (4 h), `M2` (3 h), `M3 base` (2 h), `M4 base` (2 h), `M7 OLS` (4 h), `M8 tabla k=2` (4 h), `M10 base` (2 h), `M11 lectura X–MR` (2 h), `M12 base` (2 h) y `Taller A y C operativos` (5 h). **No incluye M5, M6, M9 ni M13**, que suben de nivel.
- **Nivel Intermedio (Metrológico y Analítico — 50 h totales, o +20 h sobre el Básico):** Incorpora los módulos que suben a Intermedio: `M5` (4 h, diseño experimental y pseudorréplicas), `M6` (5 h, ANOVA de 1 y 2 vías sobre diferencias pareadas `d_jk` e ISO 5725-3), `M9 conceptual/aplicado` (2 h, matriz `U_x` del SRP27 y grado de equivalencia), más las extensiones intermedias de `M2–M4` (Grubbs/Dixon, `F`, `χ²`, potencia), `M7` (LOF, WLS, GDR/ISO 6143, `cov(a,b)`), `M8` (`c_i`, covarianzas `u_b`, `ν_eff`, auditoría de `F-PSMT-01`), `M10–M12` (`E_n`, banda de guarda, TUR, regresión de deriva) y `Taller A, B, C, D` (6 h).
- **Nivel Avanzado (Especialista / Custodio Primario — 66 h totales, o +16 h sobre el Intermedio):** Incorpora `M13` (5 h: Monte Carlo GUM-S1/S2, Bootstrap por bloques de días, robustos ISO 5725-5) y las extensiones avanzadas de `M3` (autocorrelación `r_1` y `n_eff`), `M5` (anidados escalonados), `M6` (modelo mixto cruzado-anidado `Analista × Campaña + Día(AC)` y Satterthwaite), `M7/M9` (algoritmo matricial GGMR ISO/TS 28037 cl. 10 completo), `M8/M10/M11` (función continua `U(x)` para CMC, integrales de riesgo PFA/PFR, cartas EWMA/CUSUM) y `Taller A–D completo` (8 h).

### 4.2 Ventajas (Fortalezas)
1. **Única auditoría que descubrió y documentó los errores críticos en los libros Excel reales de CALAIRE (Sección 2.3):**
   - **En [`Resultados R&r_2022 2023 (1).xlsx`](file:///home/w421/w421/calaire-stat/docs/Resultados%20R&r_2022%202023%20(1).xlsx) (M6 y Caso D):**
     - Descubrió que en `BASE DE DATOS` (celda `B70: VALORES ABSOLUTOS`) todas las diferencias entre el Level 2 y el SRP 55 fueron pasadas por **valor absoluto (`|y − x|`)**, verificándolo al cruzar la campaña `171-Interno-15-Level2-TBH` con el archivo `F-PSMT-01` (donde los errores reales de `Dia1` son negativos, `−0,2528; −0,3964...`, y en el libro R&R aparecen positivos `+0,2528; +0,3964...`). Explica con rigor que aplicar `|e|` pliega la distribución normal (*folded normal*), mezcla sesgo con varianza y hace que dos analistas con sesgos opuestos (`−0,30` y `+0,30 ppb`) parezcan idénticos (`0,30 ppb`).
     - Localizó además los errores `#REF!` de la fila 137 y el rango desplazado `=AVERAGE(D118:D123)` en la fila 138 de `BASE DE DATOS`.
   - **En [`F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm`](file:///home/w421/w421/calaire-stat/docs/F-PSMT-01%20Certificado%20de%20Calibracion_G1-sn59756-324_TBH.xlsm) (M2–M8 y Caso A):**
     - **Mezcla de concentraciones entre días (E-04):** Demostró con los datos reales de `BD_DIAS` que en cualquier nivel distinto de cero la concentración generada por el SRP varía de un día a otro (ej. en el Nivel 4 las medias del SRP en los 6 días van de `127,22` a `131,23 nmol/mol`). Por ello, las 48 lecturas brutas del Level 2 (`y_jk`) tienen `s = 1,602 nmol/mol` (dominada por el cambio del generador entre días), mientras que las 48 **diferencias pareadas con signo (`d_jk = y_jk − x_jk`)** tienen `s = 0,402 nmol/mol`. Esto corrige un error transversal en las prácticas de M2, M3, M4, M6 y Caso A que ninguna otra auditoría vio.
     - **Error de `Urepetibilidad` en `BD_DIAS!E8:E10`:** Descubrió que la plantilla aplica `STDEV.P` sobre las **576 diferencias en valor absoluto mezclando los 12 niveles (de 0 a 455 nmol/mol) y los 6 días**, y luego divide entre `√576 = 24` (`0,0105 nmol/mol`), subestimando en más de un orden de magnitud la incertidumbre por repetibilidad/precisión intermedia.
     - **Error de regresión `Uo` en `Uexp!G8:H19`:** Descubrió que la celda `G8` resta el promedio del patrón `X` a la indicación del instrumento `Y` (`= E8 − $D$20`).
     - **Error de `Upatron` en `Uexp!J8:J19`:** Descubrió que usa la ecuación interna del BIPM-SRP27 (`√(0,28² + (0,00292·x)²)`) omitiendo la trazabilidad y deriva del propio SRP 55 respecto al BIPM-SRP27.
     - **Realidad de `EcuOffset` frente a M8:** Mostró que la plantilla no reporta simplemente `max(U_i, CMC_i)`, sino que ajusta un polinomio cúbico a `U_eval(x)` y desplaza hacia arriba toda la curva polinómica de la CMC sumándole al intercepto el exceso máximo (`0,62 → 0,64 nmol/mol`).
2. **Explicación física y matemática exacta de todas las discrepancias del temario (Sección 2.1):**
   - Explica por qué el cambio de `σ` en M1 da `1,29 %` con `308,32 / 304,39 atm⁻¹ cm⁻¹` (`1,1476 / 1,1329×10⁻¹⁷ cm²/molécula = +1,298 %`) y por qué el `1,25 %` proviene únicamente de truncar el valor antiguo a 4 cifras (`1,147`).
   - Calcula el nuevo coeficiente proporcional del presupuesto del SRP cuando se incluye la incertidumbre de la nueva `σ` CCQM.O3.2019 (`u_rel = 0,309 %`): baja de `0,011·x` a `√(0,00292² + 0,00309²)·x = 0,00425·x`.
   - Señala que en M3 la fórmula `u(x)/x = u(D)/|D·ln D|` no sale de la regla lineal `Var(aX + bY)`, sino de una derivada de primer orden de `ln D` (M8).
   - Desglosa en M10 una tabla completa y sin ambigüedad con los **4 regímenes de aceptación** (SRP QAPP Level 1 vs. Level 1; SRP SOP calificación vs. reverificación; SRP QAPP / TAD 2013 verificación `6×6`; y EPA TAD 2023 verificación de 3 ciclos con divisor `N = 3`).
3. **Arquitectura en 3 niveles coherente, realista y lista para implementar en [`temario_build.py`](file:///home/w421/w421/calaire-stat/temario_build.py):**
   - La progresión **30 h (Básico) → 50 h (Intermedio, +20 h) → 66 h (Avanzado, +16 h)** es sumamente equilibrada: un curso Básico de 30 h es dictable en una semana (o dos semanas de medio tiempo) y entrega a un operador todas las competencias de su trabajo diario; el Intermedio (50 h) forma al analista metrológico completo; y el Avanzado (66 h) coincide exactamente con la duración total prevista en el proyecto original.
   - La decisión de **subir M5, M6, M9 y M13 a Intermedio/Avanzado** elimina de raíz las contradicciones en que cae la Auditoría B al intentar meter ANOVA de días, precisión intermedia y comparaciones BIPM en el Nivel Básico.
   - El **apartado 5.3** detalla módulo por módulo (M1 a M13 y Taller) qué entra en Básico, qué sube a Intermedio, qué sube a Avanzado y cuál es la práctica aplicada de cada nivel, facilitando su vuelco directo a [`temario_build.py`](file:///home/w421/w421/calaire-stat/temario_build.py).

### 4.3 Desventajas (Debilidades y aspectos mejorables)
1. **No incluye un módulo inicial corto (`M0`) de preparación de datos/herramientas ni rúbricas formales de evaluación:**
   - A diferencia de la Auditoría A (que incluye `M0` para higiene de datos/CSV y rúbricas de calificación con errores críticos) y de la Auditoría B (que propone una sesión inicial de herramientas y ejercicios de escalamiento para el nivel B), la Auditoría C entra directamente en M1 sin explicitar el sistema de evaluación ni la lista de plantillas que deben prepararse para el Nivel Básico.
2. ** Compresión horaria en las extensiones intermedias de M7 y M8 (`+1 h` sobre el Básico):**
   - En la tabla 5.2 de la Auditoría C, M7 pasa de `4 h` en Básico a `5 h` en Intermedio (`+1 h`), y M8 pasa de `4 h` en Básico a `5 h` en Intermedio (`+1 h`). Si el curso se dicta de forma modular acumulativa, cubrir en solo 1 hora adicional de M7 la prueba de falta de ajuste, WLS, GDR/ISO 6143, la incertidumbre de predicción inversa y la corrección de la columna `Uo` de `Uexp` es muy apretado (aunque en un curso Intermedio directo de 50 h se dispone de las 5 h completas gracias a que los alumnos ya traen base operativa).
3. **Oportunidad de incorporar el método de Kragten en M8 Básico y matices de `AB`/`AS` en M12:**
   - En M8 Básico (4 h), la Auditoría C propone el presupuesto GUM tabular combinando componentes en cuadratura con `k = 2`. Incorporar aquí el **método numérico de Kragten en hoja de cálculo** (propuesto por la Auditoría B) daría una herramienta aún más sólida al Nivel Básico para cuando las entradas no están expresadas en la misma unidad del mensurando.
   - En M12, aunque explica las ecuaciones de `40 CFR 58 Apéndice A` con `χ²` y `t`, no añade un segundo conjunto de `d_i` con signos mezclados (positivos y negativos) como sugiere acertadamente la Auditoría A (H17) para mostrar cómo actúan `AB = media(|d_i|)` y los percentiles 25 y 75.

### 4.4 Calidad del plan y coherencia
- **Coherencia interna:** Sobresaliente (9,5/10). No presenta contradicciones entre los datos asignados a cada nivel, las herramientas estadísticas requeridas y los módulos cursados.
- **Calidad del plan:** Es, con diferencia, **el plan más completo, riguroso y accionable de los tres (9,6/10)**, con trazabilidad directa a las líneas de código y celdas de [`temario_curso.md`](file:///home/w421/w421/calaire-stat/temario_curso.md), [`temario_build.py`](file:///home/w421/w421/calaire-stat/temario_build.py), [`caso_B_comparacion_clave.md`](file:///home/w421/w421/calaire-stat/casos_taller/caso_B_comparacion_clave.md), [`F-PSMT-01`](file:///home/w421/w421/calaire-stat/docs/F-PSMT-01%20Certificado%20de%20Calibracion_G1-sn59756-324_TBH.xlsm) y [`Resultados R&r_2022 2023 (1).xlsx`](file:///home/w421/w421/calaire-stat/docs/Resultados%20R&r_2022%202023%20(1).xlsx).

---

## 5. Comparación Cruzada por Dimensiones Clave

### 5.1 Comparación de la Arquitectura de Niveles y Horas

| Característica | [`audit_a.md`](file:///home/w421/w421/calaire-stat/audit_a.md) | [`audit_b.md`](file:///home/w421/w421/calaire-stat/audit_b.md) | [`audit_c.md`](file:///home/w421/w421/calaire-stat/audit_c.md) |
|---|---|---|---|
| **Duración propuesta por nivel** | **Básico:** 48 h<br>**Intermedio:** 80 h<br>**Extensión A:** +32 h (112 h I+A; 160 h suma total) | **No propone horas** *(lo deja pendiente)* | **Básico:** 30 h<br>**Intermedio:** 50 h (+20 h)<br>**Avanzado:** 66 h (+16 h) |
| **¿El Básico es acumulativo hacia el Intermedio?** | **No.** Las 48 h básicas no sustituyen ni descuentan de las 80 h del núcleo intermedio. | **Sí.** Perfiles acumulativos (`B ⊂ I ⊂ A`). | **Sí.** Modalidades escalonadas y acumulativas (`30 h → +20 h → +16 h`). |
| **¿Qué módulos se excluyen del Nivel Básico y suben a I / A?** | Suben a I: M4, M5, M6, selección en M7 y construcción en M8.<br>Suben a A: modelos mixtos (Caso D), GGMR (M9/Caso B) y M13. | Solo excluye M13 en B; **mantiene M1 a M12 en Básico** (incluyendo M5, ANOVA de días en M6 y comparación BIPM en M9). | **Suben íntegramente a I/A:** **M5** (Diseño exp.), **M6** (ANOVA / ISO 5725), **M9** (GGMR / BIPM) y **M13** (Monte Carlo / Robustos). |
| **¿El operador de Nivel Básico aprende a ajustar una recta OLS (M7) y armar un presupuesto tabular `k=2` (M8)?** | **No ajusta OLS ni arma presupuesto desde cero;** solo aplica una ecuación ya aprobada y actualiza celdas permitidas. | **Sí:** recta en hoja de cálculo y presupuesto en plantilla con método de Kragten. | **Sí:** regresión OLS completa, residuos, predicción inversa `x̂ = (y−a)/b` y presupuesto GUM tabular con `k = 2`. |
| **Alineación con [`temario_build.py`](file:///home/w421/w421/calaire-stat/temario_build.py)** | Baja (crea códigos `B0–B8` y `A1–A4` separados de `M1–M13`). | Media (tabla resumida por celda, sin horas ni textos detallados por sección). | **Muy alta** (conserva la estructura `M1–M13` + `T` + `Anexos A1–A5` con desglose completo por módulo y nivel). |

### 5.2 Cobertura de Hallazgos Técnicos, Estadísticos y en Libros Excel

La siguiente tabla verifica cuáles de los **22 hallazgos técnicos reales** del proyecto fueron detectados por cada auditoría:

| # | Hallazgo técnico / metodológico verificado | [`audit_a.md`](file:///home/w421/w421/calaire-stat/audit_a.md) | [`audit_b.md`](file:///home/w421/w421/calaire-stat/audit_b.md) | [`audit_c.md`](file:///home/w421/w421/calaire-stat/audit_c.md) |
|---:|---|:---:|:---:|:---:|
| 1 | **Libro `Resultados R&r`:** Las 10 hojas usan **valores absolutos (`\|y − x\|`)** (`BASE DE DATOS!B70: VALORES ABSOLUTOS`), plegando la normal y ocultando sesgos opuestos | ❌ No | ❌ No | ✅ **Sí** |
| 2 | **Libro `Resultados R&r`:** Errores `#REF!` en fila 137 y rango de promedio desplazado en fila 138 de `BASE DE DATOS` | ❌ No | ❌ No | ✅ **Sí** |
| 3 | **Libro `F-PSMT-01`:** En niveles `> 0`, el SRP genera concentraciones distintas cada día (`127,2` a `131,2 ppb` en Nivel 4); agrupar las 48 lecturas brutas `y_jk` es inválido (debe usarse `d_jk = y_jk − x_jk`) | ❌ No | ❌ No *(solo ve pseudorréplicas)* | ✅ **Sí** |
| 4 | **Libro `F-PSMT-01` (`BD_DIAS`):** `Urepetibilidad` calcula `STDEV.P` sobre las 576 diferencias absolutas de los 12 niveles juntos y divide por `√576 = 24` (`0,0105 nmol/mol`) | ❌ No | ❌ No | ✅ **Sí** |
| 5 | **Libro `F-PSMT-01` (`Uexp`):** La incertidumbre de regresión `Uo` (`G8:H19`) mezcla ejes calculando `Y − Xprom` | ❌ No | ❌ No | ✅ **Sí** |
| 6 | **Libro `F-PSMT-01` (`Uexp`):** `Upatron` usa la ecuación interna del BIPM-SRP27 omitiendo la incertidumbre de trazabilidad/deriva del SRP 55 | ⚠️ Parcial | ❌ No | ✅ **Sí** |
| 7 | **Libro `F-PSMT-01` (`EcuOffset`):** Ajusta un polinomio cúbico y desplaza toda la curva CMC hacia arriba en vez de modelar `U(x) = √(U_0² + (U_1·x)²)` | ❌ No *(solo miró `Uexp!Q8`)* | ❌ No | ✅ **Sí** |
| 8 | **M1 vs. M8:** Contradicción entre la nueva `σ` CCQM 2025 (`u_rel = 0,309 %`) en M1 y el presupuesto NIST 2017 con Hearn 1961 (`u_rel = 1,06 %` → `0,011·x`) en M8 | ✅ Sí (H04) | ✅ Sí (E4) | ✅ **Sí (E-01, calcula `0,00425·x`)** |
| 9 | **M1:** Explicación de por qué `308,32 / 304,39` da `+1,29 %` (`1,1476 → 1,1329`) y por qué `+1,25 %` se debe al truncamiento a 4 cifras (`1,147`) | ⚠️ Parcial (H05) | ❌ No | ✅ **Sí (E-02)** |
| 10 | **M1 y M12:** Signo del sesgo relativo `(meas − audit)/audit` según cuál equipo tenga la sección eficaz antigua o nueva | ✅ **Sí (H05)** | ❌ No | ⚠️ Parcial |
| 11 | **M1:** Ecuación del SRP sin factor `10⁹` para `nmol/mol` ni definición de los 4 conteos `f_ij` de las dos celdas | ✅ Sí (H14) | ⚠️ Parcial (E16) | ✅ **Sí (E-03)** |
| 12 | **M2:** Pruebas inferenciales e interlaboratorio (Grubbs, Dixon, Cochran, Mandel *h/k*) ubicadas antes de probabilidad (M3), pruebas de hipótesis (M4) y ANOVA (M6) | ✅ Sí (H15) | ✅ Sí (E10) | ✅ **Sí (§3.1.1)** |
| 13 | **M3:** Presentar `u(x)/x = u(D)/\|D·ln D\|` como aplicación de `Var(aX + bY)` cuando es una derivada de primer orden (M8), e indefinición en `x = 0` | ✅ Sí (H14) | ✅ Sí (§5.3.2) | ✅ **Sí (E-05)** |
| 14 | **M3 vs. M8:** Distinción explícita entre semiamplitud `a` (`a/√3`) y resolución total `δ = 2a` (`δ/√12`), y entre `0,31 nmol/mol` (NISTIR 6963) y `0,28 nmol/mol` (SRP 6008) | ⚠️ Parcial | ✅ **Sí (E5)** | ✅ **Sí (E-06)** |
| 15 | **M4:** Regla `n ≈ 15·(S/D)²` es para dos muestras independientes, mientras que para una media o datos pareados es `≈ 8·(S/D)² + 2` | ✅ Sí (H15) | ✅ **Sí (E8)** | ✅ **Sí (E-07)** |
| 16 | **M4:** La prueba *t* pareada SRP vs. Level 2 debe hacerse **dentro de un nivel** (`n = 8` o `n = 6` días), nunca mezclando los 12 niveles de concentración | ✅ Sí (H06) | ✅ Sí (E9) | ✅ **Sí (E-07)** |
| 17 | **M6 y Caso D:** Problemas de multiplicidad en 10 niveles de ANOVA e imprecisión de ISO 5725-4 cl. 5 | ✅ **Sí (H11, H12)** | ❌ No | ⚠️ Parcial |
| 18 | **M10 vs. M11 vs. Caso C:** Contradicción entre criterios QAPP Level 1 (`±0,01`), QAPP `6×6` Level 2 (`±0,03`, `RSD ≤ 3,7 %`) y EPA TAD 2023 (`3 ciclos`, divisor `N = 3`) | ✅ Sí (H03) | ✅ Sí (E2, E3) | ✅ **Sí (E-08, tabla completa)** |
| 19 | **M10:** Confusión entre la fórmula de ajuste cero-span de dos puntos `c = (y − y_0)·c_c/(y_c − y_0)` (EN 14625) y la predicción inversa de la recta `x̂ = (y − a)/b` o la corrección VIM | ✅ Sí (H16) | ✅ Sí (E13) | ✅ **Sí (E-09)** |
| 20 | **M12:** Falta definir `AB = media(\|d_i\|)` y `AS = s(\|d_i\|)` e incluir un ejemplo con signos mixtos (positivos y negativos) en `40 CFR 58` | ✅ **Sí (H17)** | ❌ No | ⚠️ Parcial |
| 21 | **Caso B (`caso_B_comparacion_clave.md`):** Discrepancia numérica en §5 (`b = 0,998340767`, `a = −0,179540362`) frente a la tabla §2–3 y `calc_casos.py` (`b = 0,998350748`, `a = −0,184237121`) | ✅ Sí (H08) | ✅ Sí (E6) | ✅ **Sí (§2.2)** |
| 22 | **M3, M6, M7 y M8:** Eliminación de las deducciones matemáticas de las prácticas y creación de Anexos Matemáticos | ✅ Sí (H02, §6, §8) | ✅ Sí (§6) | ✅ **Sí (§4 y §6)** |

---

## 6. Dictamen Final y Recomendación de Síntesis

### 6.1 ¿Cuál de las tres auditorías tiene el mejor plan y mayor coherencia?

1. **Primer lugar — Auditoría C ([`audit_c.md`](file:///home/w421/w421/calaire-stat/audit_c.md)):**
   - Es la auditoría **más completa, técnicamente profunda y coherente**.
   - Su aporte diferencial decisivo es haber auditado a fondo los datos y fórmulas XML de [`F-PSMT-01`](file:///home/w421/w421/calaire-stat/docs/F-PSMT-01%20Certificado%20de%20Calibracion_G1-sn59756-324_TBH.xlsm) y [`Resultados R&r_2022 2023 (1).xlsx`](file:///home/w421/w421/calaire-stat/docs/Resultados%20R&r_2022%202023%20(1).xlsx), descubriendo errores críticos que el curso debe enseñar a detectar (el uso de valores absolutos `|y − x|` en el R&R, la variación entre días del generador del SRP que invalida agrupar las 48 lecturas brutas en niveles `> 0`, el `STDEV.P(ABS(...))/√576` en `BD_DIAS`, el `Y − Xprom` en `Uexp` y el polinomio cúbico desplazado en `EcuOffset`).
   - Su arquitectura de tres niveles (**Básico 30 h · Intermedio 50 h · Avanzado 66 h**), en la que **M5, M6, M9 y M13 suben a Intermedio/Avanzado** mientras el Básico conserva un ciclo operativo completo de principio a fin, es realista en horas, pedagógicamente sólida y directamente volcable a [`temario_build.py`](file:///home/w421/w421/calaire-stat/temario_build.py).

2. **Segundo lugar — Auditoría A ([`audit_a.md`](file:///home/w421/w421/calaire-stat/audit_a.md)):**
   - Destaca por su **rigor conceptual, regulatorio y de evaluación** (fronteras entre interpretación operativa y modelado, alcance jurídico de normas EPA frente a procedimientos aprobados por CALAIRE/INM, matices de `AB`/`AS` con signos mixtos en M12, signo del sesgo relativo por `σ`, multiplicidad en ANOVA, higiene de datos en `M0` y rúbricas de evaluación con errores críticos).
   - Su principal debilidad es **no haber detectado los errores internos de los dos libros Excel** y proponer una estructura de **48 h + 80 h + 32 h (112–160 h)** excesivamente larga y con un Nivel Básico de 48 h demasiado pasivo.

3. **Tercer lugar — Auditoría B ([`audit_b.md`](file:///home/w421/w421/calaire-stat/audit_b.md)):**
   - Destaca por su **concisión y excelentes ideas didácticas puntuales** (el método numérico de Kragten para M8 en nivel Básico, la competencia explícita de detectar señales para escalar un caso de B a I/A, el límite de detección `3·s_0` con las lecturas de cero, la incertidumbre de `s` con `n` pequeño `1/√(2(n−1))`, la desviación de Allan en M3-A y las micro-correcciones de Malicet 1995, NISTIR 6963 vs. SRP 6008 e ISO 6143 `"NO"`).
   - Queda en tercer lugar porque **no propone horas**, **no auditó las fórmulas internas de los libros Excel**, e incurre en **contradicciones internas en su Nivel Básico** (incluye M5, ANOVA entre días en M6 y comparación BIPM en M9 dentro del Básico pese a limitar los datos de B a un solo día y a declarar los componentes de varianza como exclusivos de I).

---

### 6.2 Hoja de Ruta Recomendada: Usar la Auditoría C como Base e Integrar 8 Aportes de A y B

Para actualizar [`temario_build.py`](file:///home/w421/w421/calaire-stat/temario_build.py), [`temario_curso.md`](file:///home/w421/w421/calaire-stat/temario_curso.md) y [`casos_taller/caso_B_comparacion_clave.md`](file:///home/w421/w421/calaire-stat/casos_taller/caso_B_comparacion_clave.md) con la máxima calidad posible, se recomienda **ejecutar el plan de la Auditoría C (`30 / 50 / 66 h`)** incorporándole los siguientes **8 elementos puntuales de las Auditorías A y B**:

1. **De la Auditoría B → Método de Kragten en M8 (Nivel Básico e Intermedio):** Incluir en M8 Básico la propagación numérica en hoja de cálculo (método de Kragten) junto al presupuesto tabular, y usarla en Intermedio para verificar numéricamente las derivadas analíticas del SRP.
2. **De la Auditoría B → Competencia explícita de escalamiento en Nivel Básico:** Añadir en el cierre/taller del Nivel Básico (30 h) la lista de **6 señales de alerta** (autocorrelación, `ν_eff` pequeño, resultado en zona de incertidumbre cerca del límite, atípico sin causa física, deriva en carta `X–MR`, cambio de `σ`) ante las cuales el operador debe escalar el análisis al nivel Intermedio/Avanzado.
3. **De la Auditoría B → Micro-precisiones en M1, M3, M4 y M7:**
   - En M1: especificar que `σ` *disminuye* ~1 % al *aumentar* `T` de 218 a 295 K (Malicet 1995 §3.1) y declarar explícitamente la equivalencia práctica `ppb = nmol/mol`.
   - En M3/M8: aclarar el origen de `0,31 nmol/mol` (NISTIR 6963, 2003) frente a `0,28 nmol/mol` (SRP 6008 / BIPM.QM-K1) para el término constante de `D`, e incluir el límite de detección `LOD ≈ 3·s_0` en el análisis del cero.
   - En M4/M8 (Intermedio): incluir la incertidumbre relativa de `s` con muestras pequeñas `u_rel(s) ≈ 1/√(2(n − 1))` (~32 % para `n = 6` días).
   - En M7: corregir la redacción ambigua `"NO medido por absorción UV"` por `"mezclas de monóxido de nitrógeno (NO) en nitrógeno (ISO 6143 Ejemplo B.2.1)"`.
4. **De la Auditoría A → Signo del cambio de escala de `σ` y distinción de presupuestos (H04, H05):** Explicitar en M1 y M12 cómo cambia el signo de `(meas − audit)/audit` según qué instrumento esté en la escala antigua o nueva, y rotular claramente el presupuesto del SRP 6008 como *presupuesto histórico (Hearn 1961)* frente al *presupuesto actualizado (CCQM.O3.2019)*.
5. **De la Auditoría A → Definición de `AB` y `AS` y ejemplo con signos mixtos en M12 (H17):** Explicitar `AB = media(|d_i|)` y `AS = s(|d_i|)` en `40 CFR 58 Apéndice A` y añadir un segundo ejercicio corto con `d_i` positivos y negativos para mostrar que `AB` no cancela signos.
6. **De la Auditoría A → Advertencia de aplicabilidad institucional y separación de productos en M10 (H03, H16):** Indicar en M10/M11 que los criterios EPA/QAPP/TAD son referencias técnicas cuyo uso oficial en CALAIRE depende del procedimiento aprobado vigente ante el INM/ONAC, y separar claramente en M10 (a) resultado de calibración, (b) ecuación de uso/corrección y (c) declaración de conformidad (cuando aplique).
7. **De la Auditoría A → Multiplicidad y cláusula 5 de ISO 5725-4 en M6 (H11, H12):** Mencionar en M6-A el efecto de multiplicidad al evaluar 10 niveles de ANOVA simultáneamente y precisar que la cláusula 5 de ISO 5725-4:1994 sí contempla la evaluación del sesgo de un laboratorio individual frente a una referencia.
8. **De la Auditoría A → Criterios de evaluación y errores críticos invalidantes (Sección 7 de Audit A):** Incorporar al final del temario la lista de errores críticos que un participante no puede cometer para aprobar cada nivel (confundir `U` con `u`, invertir el signo de una corrección, agrupar lecturas brutas de días con distinta concentración sin restar la referencia, dividir por `√576` mezclando niveles, o borrar atípicos sin causa documentada).
