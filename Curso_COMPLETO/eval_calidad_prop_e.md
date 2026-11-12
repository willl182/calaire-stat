# Evaluación de calidad de la propuesta E

**Documento evaluado:** `prop_e.md`, versión del 24 de octubre de 2026.  
**Público:** operadores del SRP de CALAIRE, laboratorio designado del INM.  
**Alcance:** calidad curricular, corrección estadística y metrológica, progresión y viabilidad de las prácticas. **No se evalúan las horas.**

Se contrastaron la propuesta, `sup_obs.md`, `obs1.md`, `obs2.md`, `ajustes_obs_prop_e.md`, `correcciones_redaccion_prop_e.md`, `prop_a.md`, `prop_d,md`, los materiales de `casos_taller/` y los datos fuente pertinentes. Para las cuestiones técnicas se consultaron las referencias locales GUM, ISO/TS 28037:2010 y el protocolo BIPM.QM-K1, versión 2.1 de 2025. La comprobación de datos se limitó a establecer qué prácticas son posibles y a verificar resultados relevantes para esta evaluación; no constituye una auditoría integral de los libros ni una validación de resultados oficiales del laboratorio.

## 1. Veredicto global y notas

**Veredicto: buena propuesta curricular de estadística aplicada a A, aprobable con correcciones, pero todavía no lista para impartirse con los paquetes disponibles. Nota global orientativa: 3,8/5.**

No necesita convertirse en otro curso ni cambiar su enfoque. La estadística organiza realmente los módulos y el dominio aporta preguntas, datos y consecuencias de uso. Las principales debilidades son el cierre incompleto de las evidencias por tema, algunas definiciones técnicas insuficientemente precisas y la distancia entre los casos prometidos y los materiales preparados.

La falta de ciertos datos reales **no hace inviable el curso**: la propuesta permite conjuntos simulados rotulados. Sí impide afirmar que todas las prácticas están listas o que sus resultados describirán el comportamiento real del SRP 55 o del Level 2.

Escala: **1** inadecuado; **2** insuficiente; **3** aceptable con carencias importantes; **4** sólido con ajustes; **5** plenamente satisfactorio. La nota global es la media simple, redondeada, de los seis criterios.

| Criterio | Nota /5 | Fundamento |
|---|---:|---|
| **1. Fidelidad a «estadística aplicada a A»** | **5** | Títulos, competencias y conclusiones son estadísticos. Fotometría, patrones, certificado y comparación sirven como casos, no como programa de formación sobre A. |
| **2. Corrección estadística y metrológica** | **4** | El núcleo es correcto: signo, inversión, dependencia, falta de ajuste, propagación y alcance de las comparaciones. Hay que precisar la componente entre días, `E_n`, cobertura y alcance de validación GGMR. |
| **3. Progresión B → I → A y prerrequisitos** | **4** | Autonomías bien diferenciadas; ANOVA exigible en I y métodos generales en A. Falta adelantar explícitamente el manejo operativo de matrices necesario para M7-A y concretar algunos límites de escalamiento. |
| **4. Viabilidad de prácticas con los datos disponibles** | **3** | Existen datos reales valiosos y suficientes para muchas actividades de B e I. Faltan paquetes A/D, escenarios completos de control y decisiones, y soporte para determinadas extensiones avanzadas. Allan no tiene todavía una serie adecuada identificada. |
| **5. Coherencia y cumplimiento de sup_obs/obs** | **3** | Se incorporan los acuerdos centrales. No se demuestra aún, tema por tema, la cobertura práctica y evaluativa que exige el usuario; quedan correcciones de materiales reconocidas pero no cerradas. |
| **6. Claridad** | **4** | Estructura legible, convenciones útiles y objetivos claros. Persisten una igualdad sin residual, una justificación de prerrequisitos demasiado general y cierta confusión entre características generales del KCRV y el caso BIPM concreto. |

**Severidad de los hallazgos:** no se identificó un hallazgo crítico demostrado en el texto curricular. Se presentan **7 mayores y 5 menores**. Algunos mayores son bloqueos de implementación que la propuesta ya reconoce, no métodos incorrectos ni incumplimientos ocultos.

## 2. Hallazgos mayores

### H01. Mayor — La evaluación por módulo no acredita todavía la práctica y evaluación de cada tema

**Ubicación:** `prop_e.md:17`, M4-I en `prop_e.md:106–107`, M13 en `prop_e.md:219–223` y evaluación en `prop_e.md:248`.

**Evidencia:** la regla exige enseñar, practicar y evaluar **cada tema**. Sin embargo, M4-I reúne t pareada, Welch, intervalos y pruebas sobre varianzas, potencia, tamaño muestral, incertidumbre de una desviación, Grubbs y Dixon; su práctica solo explicita elegir contrastes en dos situaciones y planificar repeticiones. M13 enumera Monte Carlo, salidas múltiples, bootstrap y un método robusto no identificado, pero propone únicamente resolver un problema por dos vías. Esa tarea podría cubrir parte del bloque sin cubrir los demás métodos.

**Consecuencia:** hay una declaración de cumplimiento, pero no una trazabilidad que permita comprobarlo. No se demuestra que los temas restantes vayan a quedar como menciones, aunque el diseño actual tampoco lo impide.

**Corrección concreta propuesta:** incorporar una matriz **tema/método → nivel → prerrequisito → explicación → tarea o apartado → evidencia evaluable → datos y solución**. No hace falta un ejercicio separado por término: una práctica integrada puede acreditar varios aprendizajes si sus preguntas y rúbrica los hacen observables. En M13, identificar el método robusto y asignar evidencias a las cuatro aplicaciones; retirar del nivel cualquier tema que no se vaya a enseñar y evaluar. Las deducciones pueden seguir en anexos, pero la utilización de las ecuaciones y matrices necesarias debe practicarse en clase.

### H02. Mayor — La componente entre días y el alcance de la fórmula del promedio necesitan una definición inequívoca

**Ubicación:** convenciones en `prop_e.md:40`; M6-B en `prop_e.md:128–133`.

**Evidencia:** se define `s_entre` solamente como «desviación entre días» y se utiliza:

`u²(x̄) = s²_entre/d + s²_r/(d·n)`.

La expresión es correcta para un modelo equilibrado de efectos aleatorios si `s²_entre` estima la varianza del efecto de día, **excluida la repetibilidad**. No es correcta si se introduce como `s_entre` la desviación de los promedios diarios: estos ya contienen variación de repetibilidad. Es el pendiente 2 del informe de redacción, todavía vigente.

**Consecuencia:** puede producir doble conteo. Además, la fórmula describe una contribución de precisión bajo ese modelo, no necesariamente toda la incertidumbre de calibración. El símbolo `x̄` también resulta poco informativo cuando el ANOVA se hace sobre errores `e`, mientras `x` se reservó para la referencia.

**Corrección concreta propuesta:** declarar, por ejemplo, `e_dj = μ + D_d + ε_dj`, con efectos de día independientes de varianza `τ²`, errores de lectura de varianza `σ²`, independencia pertinente y `n` lecturas por cada uno de `d` días. Definir `s²_entre = τ̂²` y `s²_r = σ̂²`, y escribir:

`u²_prec(ē) = τ̂²/d + σ̂²/(d·n)`.

Si se suministra la desviación de medias diarias, identificarla con otro símbolo y explicar que, bajo el modelo correspondiente, la varianza del promedio se estima como `s²_medias/d`, sin añadir otra vez la repetibilidad. Aclarar las limitaciones por dependencia, desequilibrio y confusión entre día y ciclo; las demás contribuciones del presupuesto se incorporan en M8.

### H03. Mayor — El alcance general de covarianza prometido excede el alcance comprobado de la herramienta disponible

**Ubicación:** autonomía de A en `prop_e.md:29`; M7-A en `prop_e.md:147–148`; M9-A en `prop_e.md:173–174`.

**Evidencia:** la definición de GGMR y su atribución a ISO/TS 28037 son correctas. Sin embargo, el calculador disponible fija los bloques cruzados entre ejes a cero (`casos_taller/calc_casos.py:91–94`). El ejemplo de validación utilizado también tiene covarianzas cruzadas nulas: `casos_taller/caso_B_comparacion_clave.md:107–109`; ISO/TS 28037:2010, tablas 25–26, páginas impresas 35–36. El método general sí admite esos bloques: cláusula 10.1, páginas impresas 31–32.

**Consecuencia:** reproducir ese ejemplo no acredita una implementación para covarianzas cruzadas no nulas. La propuesta A y la D ya establecían esta frontera (`prop_a.md:238`; `prop_d,md:167` y `prop_d,md:229`), que E no conserva explícitamente.

**Corrección concreta propuesta:** restituir la condición de alcance: la herramienta actual se emplea dentro del caso `V_xy = 0`. Si A mantiene la aplicación general, aportar una herramienta que admita el bloque cruzado y un resultado de referencia no nulo, con tolerancias y comprobaciones de la matriz conjunta. No dejar esa aplicación como demostración ni como ampliación opcional. Precisar la definición de GGMR como ajuste con errores en ambos ejes que estima parámetros y abscisas ajustadas mediante una suma cuadrática generalizada; no confundirlo con WLS ordinario con `x` fijo.

### H04. Mayor — `E_n` se exige, pero no se fija su denominador, cobertura y criterio

**Ubicación:** M9-B/I en `prop_e.md:169–172`.

**Evidencia:** se pide calcular `Δ`, `u(Δ)` y `E_n`, sin definir este último. La advertencia sobre dependencia es correcta, pero no evita confundir una normalización por incertidumbre estándar con la normalización convencional por incertidumbre expandida. La referencia local *The ASQ Metrology Handbook*, capítulo 23, apartado “En number”, página impresa 233, utiliza incertidumbres expandidas.

**Consecuencia:** una confusión entre `u` y `U` puede cambiar la clasificación de compatibilidad aunque la propagación de la diferencia sea correcta.

**Corrección concreta propuesta:** para B, entregar un escenario independiente con un mismo factor de cobertura `k` y definir:

`E_n = Δ / √(U₁² + U₂²)`, con criterio declarado `|E_n| ≤ 1`.

Para I, calcular primero `u²(Δ) = u₁² + u₂² − 2·cov(1,2)` y después `U(Δ) = k_Δ·u(Δ)`. Si se utiliza `Δ/U(Δ)`, identificar expresamente la extensión adoptada y su interpretación. Con un mismo `k`, el término de covarianza en la expresión expandida es `2·k²·cov(1,2)`, no `2·cov(1,2)` sin conversión. Mantener la distinción entre compatibilidad, conformidad y verificación independiente. No es necesario introducir ensayos de aptitud ni ISO 13528 para enseñar esta comparación.

### H05. Mayor — La solución del caso B conserva dos juegos incompatibles de coeficientes

**Ubicación:** caso B en `prop_e.md:174–176` y `prop_e.md:240`; corrección pendiente en `prop_e.md:256`.

**Evidencia:** la tabla del caso B, `casos_taller/caso_B_comparacion_clave.md:93–100`, y el recálculo independiente de la variante (i) dan:

- `a = −0,184237121 nmol/mol`;
- `b = 0,998350748`;
- `χ² = 6,318259554`.

La discusión de `casos_taller/caso_B_comparacion_clave.md:126` mantiene `a = −0,179540362` y `b = 0,998340767` para esa misma variante. La propuesta reconoce que debe corregirse, pero el material de referencia aún no está unificado.

**Consecuencia:** no hay una solución única utilizable para evaluar al alumnado, aunque ambas cifras conduzcan al mismo cumplimiento numérico del criterio citado.

**Corrección concreta propuesta:** adoptar los coeficientes reproducidos de la tabla y revisar los resultados derivados y el texto de discusión de la variante (i). Completar también la solución WLS prometida en M7, que el calculador actual no implementa. Comparar OLS/WLS/GGMR con la **misma orientación de ejes**; la comparación con el OLS publicado en la orientación inversa debe quedar como una tarea distinta y explícita. Esta preparación corresponde al equipo docente, no a una búsqueda de errores durante la clase.

### H06. Mayor — El R&R disponible no permite el análisis completo con signo que se promete para D-A

**Ubicación:** M6-A en `prop_e.md:136–137`, caso D en `prop_e.md:242` y correcciones en `prop_e.md:256`.

**Evidencia:** el libro `docs/Resultados R&r_2022 2023 (1).xlsx`, hoja `BASE DE DATOS`, bloque `D100:W129`, contiene 600 resúmenes diarios en cinco bloques de campaña, dos analistas, seis días y diez concentraciones. Los valores conservados son magnitudes absolutas de diferencias diarias, no los errores con signo ni sus lecturas originales. El certificado Level 2 disponible permite recuperar un bloque de 60 errores diarios con signo, pero no el estudio entero. Los resúmenes tampoco separan repetibilidad de lectura y variación diaria.

**Consecuencia:** ajustar un modelo multifactor a esas magnitudes es posible, pero sus componentes y contrastes no se convierten en los correspondientes a `e = y − x`. No pueden reconstruirse signos ni emparejamientos por el número de día. Tampoco se obtiene una componente de lectura a partir de medias diarias sin información adicional.

**Corrección concreta propuesta:** preparar D-I/D-A con errores firmados recuperados de fuentes suficientes o con un conjunto simulado rotulado. Documentar la estructura cruzada/anidada, efectos fijos y aleatorios, fechas, unidad de réplica, interacción y denominadores. Incluir lecturas dentro del día si se pretende separar esa componente. Mantener el archivo histórico únicamente para preguntas que su respuesta permita. D-B sí puede prepararse ya con un bloque recuperado para comparar `media(|e|)` y `|media(e)|`, sin introducir ANOVA avanzado.

### H07. Mayor — El caso C permite cálculos, pero todavía no cubre las decisiones de seguimiento prometidas

**Ubicación:** M11 en `prop_e.md:195–202`, caso C en `prop_e.md:241` y ficha común en `prop_e.md:189`.

**Evidencia:** C1 contiene seis regresiones diarias del Level 2; C2 contiene diez regresiones publicadas de otro contexto, con fechas de agosto sin año y algunas repetidas. La descriptiva y los cálculos X–MR disponibles son reproducibles, pero no constituyen una línea base propia homogénea de largo plazo. Las series actuales tampoco aportan señales por los límites especificados que permitan ejercitar toda la secuencia investigar/repetir/retener/recalibrar. Faltan soluciones EWMA/CUSUM y un modelo explícito para el riesgo del intervalo de revisión.

**Consecuencia:** el paquete actual no basta para evaluar detección de cambios pequeños, falsas alarmas, deriva de uso e intervalos de recalibración. E lo advierte correctamente respecto de NIST y de los seis días; el bloqueo está en completar la práctica, no en esa advertencia.

**Corrección concreta propuesta:** conservar C2 como ejercicio externo y preparar una serie docente homogénea, rotulada, con fase estable, cambios, deriva y eventos de mantenimiento identificados. Para I, justificar línea base y modelo temporal antes de estimar deriva y su incertidumbre. Para A, fijar parámetros de EWMA/CUSUM y una medida de desempeño —por ejemplo, falsa alarma en un horizonte o longitud media de corrida y detección de un cambio definido—. La propuesta de intervalo debe evaluarse bajo ese modelo, no presentarse como intervalo real del Level 2. Cerrar la ficha de criterios con equipo/proceso, etapa, diseño, estadístico, unidades y fuente; incluir también el escenario de los indicadores de M12, sin mezclarlo con tolerancias ni límites de control.

## 3. Hallazgos menores

### H08. Menor — Las matrices operativas aparecen después de su primera aplicación avanzada

**Ubicación:** M3-A en `prop_e.md:97–98`, M7-A en `prop_e.md:147–148` y M9-A en `prop_e.md:173`.

**Evidencia:** M7-A exige ajustar con la matriz conjunta completa; «matrices de covarianza» se explicita como contenido en M9-A. M3-A ya introduce covarianzas entre puntos, pero no dice que allí se enseña a construir y comprobar la matriz necesaria para el ajuste.

**Corrección concreta propuesta:** asignar a M3-A el manejo operativo de matrices y bloques, sus unidades, simetría y admisibilidad, con un ejercicio pequeño evaluado; aplicarlo después en M7 y M9. La deducción matricial puede continuar en anexos. No es necesario cambiar el orden M9 → M10 → M11 → M12. Especificar también en las fichas cuándo I debe escalar un ajuste que requiere incertidumbre relevante en ambos ejes; la capacidad de firmar no elimina esa frontera.

### H09. Menor — La igualdad del error frente a la referencia omite el residual

**Ubicación:** M2-I en `prop_e.md:84`.

**Evidencia:** `e = a + (b − 1)·x` es la relación de la recta, no la igualdad de todas las observaciones individuales cuando existe dispersión residual.

**Corrección concreta propuesta:** escribir `ê(x) = â + (b̂ − 1)·x` para el error predicho, o `e_i = a + (b − 1)·x_i + ε_i` para el modelo de observaciones. Así se conserva la conclusión correcta sobre sesgo proporcional sin borrar la variación que luego se analiza.

### H10. Menor — La explicación general del KCRV debe separarse del caso BIPM.QM-K1 concreto

**Ubicación:** M9-A en `prop_e.md:173–176`.

**Evidencia:** es correcto incluir la correlación cuando un participante contribuye al valor de referencia. Sin embargo, el protocolo local BIPM.QM-K1 identifica al **BIPM-SRP27 como referencia común**, no construye en ese caso una media de todos los participantes: introducción, página 2; protocolo A, §8, página 9; protocolo B, §§10.1–10.2, página 19. El conjunto SRP36/SRP7 disponible es una adaptación para interpolación, no un conjunto de contribuciones a un KCRV combinado.

**Corrección concreta propuesta:** distinguir dos situaciones: diferencia respecto de una referencia común en el caso docente BIPM y diferencia respecto de un valor combinado al que contribuye el participante en otro ejercicio preparado. Para la segunda, suministrar pesos y covarianzas. Mantener la primera si es el único caso que se va a enseñar. Distinguir siempre el par `D, u(D)` —o su incertidumbre expandida declarada— de un indicador normalizado `E_n`. Esto delimita el problema estadístico sin enseñar la organización ni el protocolo operativo de la comparación.

### H11. Menor — La cobertura de incertidumbre necesita condiciones más explícitas para la autonomía de I

**Ubicación:** convenciones en `prop_e.md:39`; M8 en `prop_e.md:156–159`; escalamiento en `prop_e.md:33`.

**Evidencia:** la notación `t(0,975; ν_eff)` es correcta y B limita `k ≈ 2` a ejercicios justificados. No obstante, M8-I solo enumera «ν_eff y cobertura»: no explicita cómo comprobar cuándo la aproximación de Student y Welch–Satterthwaite es adecuada, especialmente al introducir covarianzas. GUM, anexo G, §§G.4 y G.6, trata esa cobertura como aproximación con condiciones, no como regla universal.

**Corrección concreta propuesta:** añadir una tarea en I que seleccione y justifique cobertura, grados de libertad y límites del procedimiento. La aplicación elemental de Welch–Satterthwaite debe justificarse por las componentes independientes del modelo, no extenderse mecánicamente a cualquier presupuesto correlacionado. Los casos que requieran un tratamiento numérico no disponible en I se escalan a A. Aclarar que «pocos grados de libertad» obliga a revisar el procedimiento de cobertura, no a prohibir toda prueba t de una media con muestra pequeña que sí cumple sus supuestos.

### H12. Menor — La justificación de la secuencia atribuye a M11 un prerrequisito no concretado

**Ubicación:** `prop_e.md:52`, M10-A en `prop_e.md:186` y M11-I en `prop_e.md:197`.

**Evidencia:** se afirma que la covarianza de M9 se usa en M10 y M11. En M10-A hay decisiones con dependencia; en M11 se menciona dependencia temporal, pero no se identifica un cálculo que necesite específicamente lo enseñado en M9. Una carta B con límites suministrados no requiere por sí misma ese desarrollo.

**Corrección concreta propuesta:** conservar el orden acordado, pero explicar las dependencias reales: M9 prepara decisiones con resultados correlacionados de M10; M11 se apoya en dependencia temporal de M3 y en regresión e incertidumbre de M7–M8. Si se añade una tarea de control que utilice la covarianza de M9, identificarla expresamente y evaluarla. No hace falta incorporar contenido adicional solo para justificar la secuencia.

## 4. Viabilidad comprobada de los casos

### 4.1. Datos disponibles y alcance legítimo

| Caso o bloque | Evidencia disponible | Prácticas viables | Preparación o límite pendiente |
|---|---|---|---|
| **A. Level 2** | `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm`, hoja `BD_DIAS`: **576 parejas = 6 días × 12 puntos de secuencia × 8 lecturas**. Son diez niveles no nulos y dos ceros, inicial/final. Los registros examinados corresponden a un ciclo por día. | Tabla larga, descriptiva, signo, comparación indicación/error, regresiones diarias, ANOVA de días bajo modelo declarado, presupuestos docentes y aplicación inversa. | Extraer un paquete revisado y documentado. Los datos no separan ciclo de día ni suministran por sí solos todas las covarianzas. No hay documento de caso A completo en `casos_taller/`. |
| **B. Comparación** | `datos_caso_B.csv`: **12 parejas agregadas** SRP36/SRP7 con SD por eje. Caso y calculador disponibles. | OLS, GGMR dentro del alcance comprobado, diferencias interpoladas y sensibilidad a hipótesis suministradas. | Corregir coeficientes; añadir WLS y variantes graduadas. `SD/√12` es un supuesto docente declarado, no un hecho experimental recuperado. No hay KCRV combinado con pesos/covarianzas. |
| **C1. Campaña Level 2** | `datos_caso_C1.csv`: **seis resúmenes diarios**, del 2 al 9 de febrero de 2023. | Reconstruir y comparar regresiones; descriptiva y discusión de corto plazo. | El CSV solo no permite separar variación intra/interdía; para eso se necesita el libro original. No es historial de largo plazo. |
| **C2. Serie publicada** | `datos_caso_C2.csv`: **diez regresiones publicadas**, con SD de parámetros y desviación residual absoluta. | Descriptiva y cálculos de carta dentro del contexto externo declarado. | Sin parejas originales ni covarianza pendiente–intercepto. No es línea base del Level 2 ni serie suficiente para sustentar sus intervalos de recalibración. |
| **D. R&R** | Libro con **600 resúmenes diarios absolutos**; recuperación parcial de errores firmados desde el certificado Level 2. | Ejemplo real de pérdida del signo; análisis descriptivo de magnitudes; modelos para esa respuesta si se declaran sus límites. | Faltan errores firmados del estudio completo y lecturas intradía. Preparar D-I/D-A con datos recuperados suficientes o simulados. |
| **Allan** | Lecturas por punto y registros temporales de una corrida que cambia de concentración. | No se ha acreditado una serie adecuada para el objetivo de identificar regímenes y elegir `τ`. | Ocho lecturas por punto y marcas temporales de resolución/cadencia insuficientemente documentadas no sostienen ese objetivo. No incluirlo todavía con los datos examinados. |

**Resultado positivo importante:** no faltan los datos originales del caso A. Las regresiones recalculadas desde sus parejas reproducen los resúmenes diarios; para el primer día, `a = −0,096778639 nmol/mol` y `b = 0,999627356`. Por tanto, varias prácticas centrales son preparables con datos reales, sin inventar la estructura 12 × 8 × 6.

También puede prepararse un ejercicio de ANOVA a un nivel. Por ejemplo, en el punto nominal de 360 nmol/mol, el modelo condicional de seis días y ocho lecturas produce `s_r ≈ 0,367128`, componente entre días `≈ 0,195818` y contribución estándar al promedio `≈ 0,095910 nmol/mol`. **Estos números acreditan factibilidad de la práctica, no independencia de las lecturas ni incertidumbre oficial del instrumento.** La elección del modelo y las contribuciones adicionales siguen siendo necesarias.

### 4.2. Qué falta para declarar los paquetes listos

`casos_taller/` contiene dos documentos de caso, tres CSV y un calculador. No están completos los cuatro paquetes con datos, diccionario, enunciado, plantilla, solución revisada y rúbrica anunciados en `prop_e.md:235`.

Es factible completar el curso mediante preparación docente:

- **B:** conjuntos acotados con supuestos y componentes suministrados; escenarios independientes para `E_n`; carta con límites y acciones definidos. Los conjuntos pueden ser simulados sin exigir que B ejecute simulaciones.
- **I:** soluciones ANOVA y WLS revisadas, incertidumbre de inversión y uso futuro, componentes compartidas y presupuestos del cliente; ejercicios completos de contraste, diseño e indicadores.
- **A:** diseños firmados con estructura conocida, herramientas dentro de alcance validado, variantes de covarianza, métodos numéricos y comparación de cartas con riesgo definido.

La simulación rotulada resuelve carencias didácticas; **no convierte sus resultados en evidencia del desempeño real del laboratorio**. La condición de cierre de `prop_e.md:260` sigue pendiente, y el propio texto la formula como condición futura, no como logro ya obtenido.

## 5. Revisión de los ocho pendientes del informe de redacción

| Pendiente de `correcciones_redaccion_prop_e.md:32–41` | Dictamen | Acción propuesta |
|---|---|---|
| **1. Enlaces a `prop_d,md`** | **No es un enlace roto:** el archivo existe con ese nombre. | No renombrar ni cambiar enlaces por necesidad técnica. Puede normalizarse el nombre en otra tarea autorizada, actualizando sus referencias. |
| **2. Definición de `s_entre`** | **Confirmado.** La fórmula es condicionalmente correcta, pero la definición admite doble conteo. | Aplicar H02: componente pura entre días, modelo y respuesta explícitos; distinguirla de la SD de medias diarias. |
| **3. GGMR / ISO 28037** | **Atribución y núcleo de la descripción confirmados.** ISO/TS 28037:2010, cláusula 10, denomina GGMR al método y utiliza la matriz conjunta de ambos ejes. | Precisar la diferencia frente a WLS ordinario y cerrar el alcance de validación según H03. No clasificar la cita como error. |
| **4. «SRP 27»** | **No es una errata.** El protocolo BIPM contiene su presupuesto en el apéndice 1. La advertencia de no atribuirlo al SRP 55 es pertinente. | Conservarlo; mejorar a «presupuesto del BIPM-SRP27 utilizado como referencia didáctica». **No sustituir 27 por 55.** |
| **5. `E_n` y dependencia** | **La advertencia es correcta.** Compartir patrón impide asumir independencia sin justificación; no invalida por sí solo todo indicador de compatibilidad. | Cerrar fórmula, cobertura y criterio según H04, sin confundir incertidumbres estándar y expandidas. |
| **6. Covarianza M9 → M10/M11** | **Parcialmente sin justificar.** Se reconoce una aplicación en M10-A, pero no se concreta en M11. | Precisar la explicación de prerrequisitos, conservando el orden, según H12. |
| **7. Condición de Allan** | **No satisfecha por las series examinadas.** No se identificó una serie adecuada para el objetivo anunciado. | No incluirlo aún, salvo incorporar datos que acrediten cadencia, estabilidad, duración y resolución temporal suficientes. Su condición de entrada es válida; no es una ampliación opcional. |
| **8. Lista de correcciones previas a la clase** | **Es legítima en una propuesta de trabajo**, pero no acredita que las correcciones se hayan ejecutado. | Mantenerla como lista de pendientes con estado y criterio de cierre, o separarla en un anexo de implementación. No presentarla como material ya corregido. |

**Observación documental adicional:** `ajustes_obs_prop_e.md` recoge bien las decisiones, pero conserva referencias de sección desactualizadas: ubica módulos en §6, aunque en E están en §5, y ubica inclusiones/exclusiones en §7, aunque están en §6. Su registro de ajustes no debe tomarse como evidencia suficiente de cierre sin contrastarlo con el texto y las soluciones.

## 6. Cumplimiento de los criterios del usuario y de sup_obs/obs

| Exigencia | Evaluación |
|---|---|
| **Curso de estadística aplicado a A, no curso de A** | **Cumple.** La corrección del contexto BIPM de H10 no exige añadir formación sobre protocolos. |
| **Cada tema se enseña, practica y evalúa en su nivel** | **Declarado, pero todavía no demostrado tema por tema.** Es el cierre prioritario de H01. |
| **Prácticas de aplicación; demostraciones a anexos** | **Cumple en el diseño.** Hay cálculo, elección, interpretación y acción. Separar las deducciones de la utilización operativa, que sí debe evaluarse. |
| **Si un tema no puede enseñarse bien en B, pasa al siguiente** | **Bien resuelto en lo principal.** B no ejecuta ANOVA, no calcula covarianzas de la comparación correlacionada y trabaja con procedimientos suministrados. Su autonomía no se reduce a mirar ejemplos. |
| **ANOVA: componentes dadas en B; ejecución en I** | **Cumple**, sujeto a corregir la definición de la componente entre días. |
| **t en B; F en I** | **Cumple.** La ubicación corresponde a las aplicaciones previstas. |
| **Dependencia y `E_n`** | **Cumple conceptualmente.** Falta la especificación operativa de H04. |
| **Falta de ajuste y referencia variable** | **Cumple.** No trata los promedios de días con referencias distintas como réplicas automáticas del mismo `x`. |
| **Allan: entra con práctica si hay series adecuadas; de lo contrario, no entra** | **Cumple como regla de inclusión.** Con la evidencia revisada, no está habilitada su inclusión todavía. |
| **Fuera ISO 13528 y ensayos de aptitud** | **Cumple.** Las comparaciones entre patrones se mantienen justificadamente como problemas de diferencias y covarianza. Para mayor claridad, la exclusión genérica de «intercomparaciones entre laboratorios» puede acotarse a los esquemas e índices excluidos, sin contradecir la inclusión expresa de BIPM. |
| **Mantener M9 → M10 → M11 → M12** | **Cumple.** Debe afinarse su justificación, no cambiar el orden. |
| **No evaluar las horas** | **Respetado en esta evaluación.** Ninguna nota ni hallazgo se basa en duración, carga horaria o compresión de contenidos. |

## 7. Lo que está bien y conviene conservar

1. **Identidad estadística real.** Los catorce módulos se formulan alrededor de competencias estadísticas; M1 usa la ecuación del instrumento para enseñar modelos y sensibilidad, no para desarrollar un curso de espectroscopia.
2. **Niveles definidos por autonomía.** Ejecutar un procedimiento en B, seleccionar y justificar en I, formular y validar en A es una progresión adecuada para los perfiles solicitados. La autorización institucional para firmar se distingue de aprobar el curso.
3. **B conserva trabajo estadístico completo.** Calcula, interpreta y decide; recibe componentes ya calculadas cuando su estimación pertenece a I. Reconocer un supuesto incumplido se evalúa y no reemplaza la enseñanza.
4. **Convenciones útiles.** `e = y − x`, `x̂ = (y − a)/b` y corrección `x̂ − y` evitan confundir signo, resultado corregido y ajuste instrumental. Son correctas las conversiones `u = U/k`, `h/√3`, `δ/√12` y la convención de Student bilateral central del 95 % cuando corresponde.
5. **Atención al resultado de interés.** Distinguir lectura, promedio y uso futuro, y declarar unidad de repetición y escala temporal, conecta descriptiva, inferencia, componentes, regresión y presupuesto.
6. **Regresión bien orientada.** No se valida con R², no se fuerza el origen por costumbre, no se impone `ν = n − 2` a cualquier ajuste y se exige una base válida de error puro para falta de ajuste.
7. **Dependencia correctamente interpretada.** La fórmula de varianza de la diferencia es correcta. Es especialmente valioso no llamar «verificación independiente» a comparar resultados ligados al mismo patrón.
8. **Metrología con límites claros.** No se convierte un presupuesto del SRP 27 en presupuesto del SRP 55, una comparación favorable en aprobación de CMC, ni una adaptación SRP36/SRP7 en resultado oficial de CALAIRE.
9. **Seguimiento sin extrapolaciones indebidas.** Se distinguen límites de control y tolerancias; la historia NIST no se atribuye al Level 2 y seis días no se presentan como historial de largo plazo.
10. **Indicadores sin confundir respuestas.** Se preserva la diferencia entre `media(|d_i|)` y `|media(d_i)|`, se evitan porcentajes cerca de cero y no se convierte `3·s₀` en definición universal de detección.
11. **Errores de archivos fuera del objetivo docente.** Es correcta la decisión de preparar los ejemplos antes de clase y no evaluar la capacidad de localizar celdas rotas.
12. **Condición de cierre honesta.** La propuesta no afirma que ya estén resueltos Allan, las soluciones y todos los paquetes. Esa condición debe mantenerse y hacerse verificable.

## 8. Recomendación de cierre

**Conservar la estructura y el enfoque de E.** Antes de aprobarla como programa ejecutable:

1. Cerrar las definiciones y soluciones que pueden alterar cálculos o interpretación: **H02, H03, H04 y H05**.
2. Completar los paquetes por nivel, especialmente datos firmados/modelos de D y escenarios de C, sin atribuir simulaciones al laboratorio: **H06 y H07**. El caso A tiene una base real suficiente para avanzar.
3. Verificar la matriz de enseñanza, práctica y evaluación **por tema**, no solo por módulo: **H01**.
4. Resolver prerrequisitos y precisiones menores; no incluir Allan mientras no se acredite su conjunto adecuado.

**Conclusión:** la debilidad de E no es ser un curso de A disfrazado de estadística. Es una propuesta estadística pertinente cuyo cierre técnico y didáctico aún debe demostrarse con definiciones inequívocas, herramientas de alcance comprobado y prácticas evaluables completas.
