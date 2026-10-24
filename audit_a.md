# Auditoría del curso de estadística aplicada a la fotometría de ozono con el SRP

Fecha: 23 de octubre de 2026. Documento auditado: `temario_curso.md`, propuesta del 22-10-2026, junto con su generador, los casos B y C, sus CSV y código, y fuentes técnicas seleccionadas de `docs/`.

## 1. Dictamen y decisión sobre el nivel del curso

**El curso técnico completo requiere un núcleo de nivel intermedio y una extensión avanzada. El básico debe tener un alcance operativo propio.** Puede recorrer las etapas del trabajo del laboratorio, desde las lecturas hasta el uso del certificado y el control de los patrones, pero no permite ejecutar y justificar todos los métodos del temario actual.

No corresponde prometer tres versiones técnicamente equivalentes de todo el temario: interpretar una salida preparada de ANOVA o GGMR no equivale a aprender a seleccionar, aplicar y justificar esos métodos. Las plantillas facilitan el trabajo, pero no cambian el nivel de la competencia exigida. La dificultad depende de los supuestos, decisiones y modelos que debe manejar el participante, incluso cuando no hay demostraciones matemáticas.

Se recomienda organizar la oferta en:

- **Curso básico operativo — 48 h:** preparación y descripción de datos, aplicación de funciones suministradas, interpretación de incertidumbre y certificados, controles y acciones prescritas. Tiene resultados de salida acotados; no se presenta como cobertura técnica completa del temario.
- **Curso principal intermedio — 80 h:** planificación y análisis de calibraciones habituales, inferencia aplicada, precisión intermedia, regresión, presupuesto de incertidumbre y decisiones documentadas. Es el nivel mínimo para ejecutar y justificar el núcleo analítico.
- **Extensión avanzada — 32 h después del intermedio o de acreditar competencias equivalentes:** modelos complejos, incertidumbre en ambos ejes y covarianzas generales, validación de ajustes/herramientas y propagación avanzada. El itinerario intermedio más extensión suma **112 h**.

El curso básico no es un prerrequisito obligatorio adicional para quien ya tenga sus competencias. No debe sumarse automáticamente 48+80+32 h. Las horas propuestas requieren un piloto y pueden ajustarse; reducir demostraciones no elimina la necesidad de tiempo para practicar selección, diagnóstico e interpretación.

Hay errores y contradicciones que deben corregirse antes de impartirlo: aplicación automática de criterios estadounidenses a CALAIRE, interpretación de la repetibilidad, uso de pruebas pareadas, presupuesto histórico de incertidumbre junto a una sección eficaz actualizada, y resultados incompatibles dentro de la solución del caso B. También hay vacíos en la conexión entre datos, modelo de calibración, corrección, incertidumbre y decisiones de uso. Los hallazgos técnicos y las verificaciones de la auditoría se conservan.

**Regla común:** las prácticas y los ejercicios serán de aplicación en todas las rutas. El participante trabaja con datos, resultados y decisiones acordes con su nivel. Las demostraciones, deducciones algebraicas y desarrollos matriciales quedan en anexos opcionales y no forman parte de la evaluación práctica. Las explicaciones conceptuales deben resolver una tarea concreta del laboratorio; no se añaden discusiones abstractas como objetivo docente.

## 2. Alcance y evidencia

Se revisaron íntegramente el temario y los enunciados/soluciones B y C; se inspeccionó el código de cálculo y se ejecutó `python3 casos_taller/calc_casos.py`. Se consultaron apartados concretos del protocolo BIPM.QM-K1 v2.1, SRP 6008, QAPP, SOP, TAD 2023, ISO/TS 28037, ISO 5725-4 y 40 CFR 58, Apéndice A. Se inspeccionaron fórmulas y valores almacenados en los libros Excel mediante su XML; no se ejecutaron macros ni se recalcularon los libros en Excel.

Se recalculó, desde B6:C23 de las diez hojas de concentración del estudio R&R, el ANOVA equilibrado analista × campaña con seis observaciones diarias por celda. Se contrastó además en fuentes oficiales en línea la transición de sección eficaz y la procedencia de las referencias históricas.

Esta es una auditoría del diseño y de la coherencia técnica del curso, con verificaciones selectivas. No es una validación integral de todas las fórmulas del certificado, del software, de la acreditación o de la CMC vigente. Las afirmaciones institucionales del temario no sustituyen certificados, alcance reconocido ni procedimientos aprobados.

Clasificación utilizada:

- **P1:** corregir antes de impartir; puede enseñar una decisión o un resultado técnicamente incorrecto.
- **P2:** completar antes de publicar la versión docente; afecta la aplicación o la progresión.
- **P3:** mejorar la eficiencia y presentación.
- **Error comprobado:** contradicción interna o resultado verificado.
- **Omisión/ambigüedad:** faltan condiciones para aplicar correctamente una afirmación.
- **Pendiente documental:** requiere evidencia propia del laboratorio que no queda establecida en el material revisado.

## 3. Hallazgos que requieren corrección

### H01 · Se confunde cobertura operativa con dominio técnico del curso — P1, diseño

**Ubicación:** mapa del curso, objetivos M1–M13 y taller.

M1 y M2 son predominantemente básicos; M3 requiere distinguir fundamentos accesibles de propagación con dependencia. Inferencia, diseño, ANOVA, selección de regresión y construcción de presupuestos llevan el curso a intermedio. Los modelos mixtos complejos y GGMR con covarianzas generales requieren avanzado. El taller actual mezcla esas exigencias y no define un nivel mínimo coherente.

El defecto no es que todos los métodos carezcan de una versión básica. Es que se pretende prometer cobertura completa sin distinguir interpretar un resultado, aplicar un procedimiento y justificar el modelo que lo produce.

**Cambio:** separar un básico operativo, un núcleo intermedio y una extensión avanzada con prerrequisitos explícitos. En básico, comparaciones clave y estudios de precisión aparecen como contexto de los resultados que usa el operador; sus análisis técnicos se reservan a niveles superiores. Definir qué puede hacer el egresado y qué tareas requieren revisión especializada. No utilizar una plantilla como evidencia de que un método avanzado se ha vuelto básico.

### H02 · Hay ejercicios de demostración dentro del núcleo — P1, contradicción con el enfoque solicitado

**Ubicación:** M3, «Deducir la desviación estándar de una distribución rectangular»; M6, «Deducir los cuadrados medios esperados»; M7, «Deducir las ecuaciones normales»; M8, «Derivar los coeficientes de sensibilidad».

Estas actividades consumen tiempo sin producir directamente una competencia operativa. Construir toda la tabla ANOVA a mano tampoco debe ser el centro de la práctica.

**Cambio:** trasladar las deducciones a anexos. Entregar fórmulas, factores y herramientas verificados, y pedir elegir entradas, comprobar unidades, ejecutar cálculos, interpretar salidas y decidir. En avanzado se puede validar una implementación frente a ejemplos de referencia sin demostrar el algoritmo.

### H03 · Criterios EPA «directamente aplicables» a CALAIRE — P1, contradicción y pendiente documental

**Ubicación:** M11 afirma que los criterios TAD son directamente aplicables; taller C afirma lo mismo del QAPP 6×6. El caso C reconoce que la periodicidad y los requisitos del laboratorio deben confirmarse con sus documentos y el INM.

No se establece qué procedimiento aprobado adoptó CALAIRE, en qué fecha, para qué equipo y con qué modificaciones. Tener seis días de resultados no acredita por sí solo una verificación formal QAPP 6×6; tener más de tres regresiones tampoco acredita automáticamente el diseño TAD.

**Cambio:** sustituir «directamente aplicable» por «referencia técnica que debe contrastarse con el procedimiento aprobado de CALAIRE». Adjuntar una ficha de aplicabilidad: documento, versión, instrumento, etapa —calificación, verificación, reverificación o calibración—, diseño, estadístico, divisor, límite y autoridad de adopción. Las diferencias SOP/QAPP/TAD deben resolverse para el caso de uso, no solo enumerarse.

**Evidencia:** TAD 2023, Tabla 4-1 y §4.4.1; QAPP §6.2.3 y Tabla 7-1; limitaciones del propio caso C. El [TAD publicado por EPA](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1016Y93.TXT) describe requisitos dentro de su esquema de patrones de transferencia; no prueba la adopción por CALAIRE.

### H04 · Se mezcla una sección eficaz nueva con un presupuesto histórico — P1, omisión de alcance

**Ubicación:** M1 y M8.

M1 introduce σ = 1,1329(35)×10⁻¹⁷ cm²/molécula, mientras M8 presenta `u = √(0,28² + (0,011x)²)` del SRP 6008 y su contribución histórica de sección eficaz `0,0106x`. La fórmula sí corresponde al documento histórico consultado; no es un presupuesto actualizado del SRP55 ni una consecuencia de la nueva σ.

La incertidumbre estándar relativa de la nueva σ es `0,0035/1,1329 = 0,003089`, aproximadamente 0,309 %. Su exclusión en una comparación entre fotómetros que comparten σ es una convención/estructura de incertidumbre que debe declararse. No equivale a que σ carezca de incertidumbre en cualquier resultado absoluto o certificado.

**Cambio:** trabajar con dos presupuestos rotulados: histórico, para reproducir la fuente; y vigente del laboratorio, para decisiones actuales. Explicar qué resultado es convencional y cuál incluye la incertidumbre completa del método. No sustituir una cifra en un presupuesto ajeno y presentarlo como validación del SRP55.

**Evidencia:** SRP 6008, p. 2; BIPM.QM-K1 §1.1 y Apéndice 1. El [informe BIPM 2024/03, revisado en septiembre de 2025](https://www.bipm.org/documents/d/guest/rapportbipm2024-03), proporciona la nueva σ y su incertidumbre. La [página NIST del SRP 6008](https://www.nist.gov/sri/standard-reference-instruments/sri-6008-ozone-standard-reference-photometer) conserva información de la escala anterior: la actualidad de una página no actualiza automáticamente sus coeficientes.

### H05 · Falta fijar el signo y la referencia del cambio de escala — P1, ambigüedad

**Ubicación:** M1, ejercicio de recalcular concentraciones; M12, «sesgo de +1,25 % por usar la sección eficaz antigua».

Para las mismas señales, `x_nueva = x_antigua·σ_antigua/σ_nueva`. Con el par 1,147/1,1329 el factor es 1,01244594: el resultado nuevo sube aproximadamente 1,245 %. Si el monitor permanece en la escala antigua y la auditoría está en la nueva, `(meas−audit)/audit` es negativo, aproximadamente −1,229 %. El signo cambia si se intercambian las escalas.

El cociente 308,32/304,39 da otro factor, 1,01291107. Son pares históricos que deben identificarse; no son porcentajes intercambiables.

**Cambio:** indicar en cada ejercicio qué σ usa cada equipo, qué valor se toma como referencia, cuál es el denominador y si se modificó el software. Incluir el caso en que ambos instrumentos comparten la escala antigua y el acuerdo relativo no revela el cambio común. Las decisiones de reprocesar datos históricos deben seguir la política aplicable, no deducirse de este ejercicio.

### H06 · La prueba t pareada puede aplicarse indebidamente a varios niveles — P1, ambigüedad

**Ubicación:** M4, «Prueba t pareada SRP frente a Level 2 en un día del certificado».

Emparejar lecturas del mismo gas no convierte las diferencias de todos los niveles en una muestra de un único sesgo constante. Si existe error proporcional, la diferencia depende de la concentración; también puede haber heterocedasticidad y dependencia temporal. Una t global puede ocultar errores importantes por nivel.

**Cambio:** usar una t pareada para un nivel definido, con pares correctamente sincronizados y diferencias suficientemente independientes. Para el intervalo completo, analizar error frente a concentración y una función de calibración adecuada. La t describe el comportamiento de diferencias bajo sus supuestos; no incorpora automáticamente toda la incertidumbre del patrón ni demuestra conformidad o equivalencia.

### H07 · Lecturas consecutivas y repetibilidad: afirmación demasiado absoluta — P1, error conceptual

**Ubicación:** M6, «las lecturas consecutivas de un mismo ciclo subestiman la repetibilidad».

Las lecturas consecutivas pueden estimar repetibilidad de corto plazo si corresponden a condiciones de repetibilidad y el modelo de dependencia es adecuado. Lo que no estiman por sí solas es variación entre ciclos, días o recalibraciones. La autocorrelación también puede invalidar `s/√n`, pero no se presume su tamaño ni su signo sin revisar la secuencia.

**Cambio:** definir lectura, semiciclo, ciclo, corrida, día y resultado de calibración. Para cada componente, declarar qué unidad se repite y qué condiciones cambian. Reemplazar la frase por: «Las lecturas de un ciclo caracterizan la variación dentro de ese ciclo; no sustituyen ciclos independientes para estimar variación entre ciclos ni días para precisión intermedia».

### H08 · La solución B contiene coeficientes incompatibles — P1, error numérico comprobado

**Ubicación:** `casos_taller/caso_B_comparacion_clave.md`, tabla de ajustes y apartado «5. Criterios y discusión OLS/GLS».

El script y la tabla del ajuste (i) producen `a = −0,184237121` y `b = 0,998350748`. El apartado 5 conserva `a = −0,179540362` y `b = 0,998340767`, que no reproducen esa variante. Los grados de equivalencia de la solución sí corresponden al primer par.

**Cambio:** unificar el apartado 5 con el cálculo reproducido y registrar la versión de datos y modelo utilizada. La conclusión sobre límites numéricos QAPP no cambia, pero una solución de referencia no debe ofrecer dos resultados para el mismo análisis.

Además, el enunciado de la matriz genérica debe indicar expresamente que `0,28²I` corresponde solo a la variante (ii); en (i) la diagonal aleatoria es `diag((s_i/√12)²)`.

### H09 · Los «grados de equivalencia» del taller B son una adaptación — P1, ambigüedad de estatus

**Ubicación:** M9 y taller B, frente a las limitaciones del caso B.

Las parejas QAPP son de otros instrumentos; sus incertidumbres completas y covarianzas no están disponibles. El ejercicio añade un modelo inspirado en SRP27 a ambos ejes y supone `U_xy=0`. El resultado interpolado no es un resultado oficial de BIPM.QM-K1 ni evidencia del desempeño de CALAIRE.

**Cambio:** denominarlo «diferencia interpolada e incertidumbre bajo un modelo didáctico». Reservar «grado de equivalencia de la comparación» para el resultado definido y evaluado conforme al protocolo aplicable. Distinguir medición directa, predicción en una coordenada nominal exacta y predicción para una entrada medida con incertidumbre: no tienen necesariamente el mismo presupuesto.

La función `ggmr_fit` admite covarianzas entre puntos dentro de cada eje, pero fija los bloques cruzados a cero. Sirve para el ejemplo actual; no basta para anunciar una implementación validada del caso general con `U_xy≠0`.

### H10 · Límites de control externos no vigilan el Level 2 de CALAIRE — P1, riesgo de aplicación

**Ubicación:** taller C y su solución; M11.

El caso C ya advierte correctamente que los límites derivados de diez comparaciones NIST no son límites operativos de CALAIRE. Esa advertencia debe incorporarse al objetivo y al enunciado, para que la superposición de C1 no parezca demostrar estabilidad.

**Cambio:** construir una carta propia con una serie homogénea de CALAIRE cuando exista. Mientras tanto, usar C2 para aprender el cálculo de cartas y C1 para describir una calibración. La superposición y la F entre C1/C2 pueden conservarse como ejercicio para identificar una comparación inadecuada, no como prueba de que un sistema es más estable.

Los seis días de C1 no constituyen un historial de meses/años. Una tendencia contra orden de corrida tampoco es una deriva por día si los intervalos temporales son desiguales.

### H11 · ANOVA correcto bajo un modelo, pero falta declarar sus límites — P1, omisión

**Ubicación:** M6 y caso D.

El recálculo reproduce las cifras principales del temario: `F_analista ≤ 1,2382`; interacciones nominalmente significativas en 135, 360, 405 y 455 nmol/mol, con F de 4,31 a 6,61 y grados de libertad (2,30). Es una fortaleza del material: reconoce días anidados en analista × campaña.

Sin embargo, esos resultados dependen de tratar los factores y el residual conforme al modelo declarado. Dos analistas y tres campañas dan muy poca información para generalizar componentes aleatorias. Analizar diez niveles por separado introduce multiplicidad; las cuatro significaciones son al nivel nominal por prueba, no una conclusión simultánea al 5 % para todo el intervalo. Campaña puede recoger tiempo, estado del instrumento, ajustes y otros cambios: no identifica una causa física única.

Con un error medio por día, el residual representa dispersión de errores medios diarios dentro de analista × campaña. No separa ruido de lectura, ciclos y efecto diario. Tampoco estima directamente repetibilidad de lecturas individuales.

**Cambio:** declarar efectos fijos/aleatorios, unidad de respuesta, hipótesis y alcance de cada componente. Informar magnitud e incertidumbre o limitación de la estimación. Tratar la multiplicidad de forma explícita, al menos como análisis exploratorio. No convertir «no significativo» en «analistas equivalentes».

### H12 · Terminología ISO 5725 y R&R imprecisa — P2, error y ambigüedad

**Ubicación:** M6.

«Las Partes 2 y 4 son para estudios interlaboratorio» es demasiado restrictivo: ISO 5725-4:1994 incluye en su cláusula 5 la determinación del sesgo de un laboratorio mediante un método normalizado. La Parte 3 es pertinente para precisión intermedia dentro del laboratorio, pero no excluye todo uso de la Parte 4.

Además, «repetibilidad = σ_e²» y «R&R = suma» describen varianzas. Si se informa una desviación estándar, corresponde la raíz de la suma de componentes de varianza. El significado de reproducibilidad en R&R industrial debe distinguirse del de ISO 5725 y de las condiciones de precisión intermedia del laboratorio.

**Cambio:** escribir `σ²_R&R = σ²_e + σ²_operador + σ²_interacción` para el modelo correspondiente, y `s_R&R = √(σ̂²_R&R)` para la desviación. Explicar los límites `r≈2,8s_r` y `R≈2,8s_R` como límites aproximados de diferencia entre dos resultados independientes bajo las condiciones indicadas; no son tolerancias ni incertidumbres expandidas.

### H13 · La regresión requiere condiciones que hoy quedan implícitas — P1, omisión

**Ubicación:** M7.

La fórmula OLS de `cov(a,b)` presupone el modelo OLS correspondiente; no debe reutilizarse automáticamente para WLS/GGMR. El χ² con `n−2` requiere una matriz de incertidumbre adecuada y condiciones del modelo; no se justifica solo por tener doce filas. Tampoco un residuo ponderado ≤2 debe enseñarse como regla universal fuera de su procedimiento concreto.

La falta de ajuste con réplicas presupone grupos comparables de una misma entrada, error puro identificable y un modelo apropiado de varianza/dependencia. El cero inicial y final son dos pasos de secuencia, no necesariamente dos niveles físicos distintos. Los valores medidos del patrón tampoco son idénticos dentro de un nivel nominal.

**Cambio:** definir por separado número de observaciones, pasos, niveles distintos y réplicas independientes. Usar la F clásica de falta de ajuste únicamente en un ejemplo que cumpla sus supuestos; en datos reales, revisar agrupación por nivel, deriva y variación de la referencia. Para probar cercanía a identidad interesan intercepto 0, pendiente 1 y comportamiento del error en el intervalo, no solo pendiente distinta de cero.

### H14 · Ecuación de medida y propagación cerca de cero incompletas para su uso — P2, omisión

**Ubicación:** M1 y M3.

La ecuación del SRP no define cada `f_ij`, sus estados de gas y la orientación de D. Tampoco explicita el factor de conversión entre fracción molar en mol/mol y nmol/mol ni el conjunto coherente de unidades para σ, L, R, T y P. Mezclar cm con unidades SI produce errores grandes.

`u(x)/x` no está definida en x=0. Debe usarse la forma absoluta o su límite; `U(D)` y `U(x)` necesitan el factor de cobertura declarado para compararse con `u`.

**Cambio:** entregar una ficha con esquema de estados, símbolos, unidades, signo y ejemplo resuelto. En cero usar incertidumbre absoluta; evitar CV o error relativo cuando la media sea cero o muy pequeña. Distinguir temperatura termodinámica en la ecuación, corrección de densidad y dependencia térmica de σ, para evitar corregir dos veces el mismo efecto.

### H15 · Reglas estadísticas presentadas sin su dominio de aplicación — P2, omisión

**Ubicación:** M2–M4 y M8.

- `P = 1−(1−P_i)^n` requiere eventos independientes y probabilidad individual común. No es una fórmula universal para el riesgo de cualquier procedimiento de detección de atípicos.
- Grubbs, Dixon y Cochran tienen propósitos, tamaños de muestra y supuestos diferentes. Cochran se refiere a dispersión entre grupos; h/k de Mandel requieren estructura agrupada. No son alternativas intercambiables para borrar una lectura extrema.
- `n≈15(S/D)²` necesita especificar diseño, α, potencia, unilateralidad/bilateralidad y significado de S y D. No vale como regla general para medias pareadas, pendientes y factores aleatorios.
- Una prueba F es sensible a desviaciones de normalidad. No debe ser la puerta automática para decidir si dos días se pueden combinar.
- Welch–Satterthwaite y `k=t(ν_eff)` requieren condiciones de aplicación y probabilidad de cobertura. Las correlaciones y componentes de varianza estimadas no admiten cualquier sustitución mecánica en la fórmula habitual.

**Cambio:** dar una tarjeta de selección por método: pregunta, unidad de análisis, supuestos, resultado y acción. Priorizar gráficos, tamaños de efecto e intervalos. Reservar pruebas especializadas para el nivel en que sean útiles. Ante una anomalía, investigar y documentar; comparar el análisis con y sin el dato cuando proceda.

### H16 · Certificado, CMC y conformidad deben separarse mejor — P1, omisión

**Ubicación:** M8 y M10.

La plantilla efectivamente selecciona el mayor entre la U calculada y una curva usada como CMC: `Uexp!Q8` selecciona N8/O8 según P8. Esto comprueba la mecánica del libro; no acredita la vigencia ni la aplicabilidad de esa curva. El máximo tampoco corrige un presupuesto incompleto.

Una CMC no se obtiene sin más a partir de una calibración aislada. Deben identificarse alcance, intervalo, unidad, cobertura y condiciones. También debe distinguirse CMC publicada en KCDB y capacidad incluida en un alcance de acreditación, cuando corresponda; no se debe trasladar automáticamente una regla institucional entre ambos contextos.

La calibración produce una relación entre valores e indicaciones con incertidumbre; una declaración de conformidad requiere especificación y regla acordadas cuando sea solicitada o aplicable. La regla de decisión no es un campo obligatorio de toda calibración sin declaración de conformidad.

**Cambio:** separar tres productos: resultado de calibración, función/correcciones para el uso y eventual declaración de conformidad. La corrección de dos puntos `c=(y−y_0)c_c/(y_c−y_0)` debe rotularse como modelo específico, con su alcance e incertidumbre; no reemplaza automáticamente la función multipunto del taller.

### H17 · Las estadísticas de redes necesitan completar definiciones y alcance — P2, omisión

**Ubicación:** M12.

Las fórmulas son reconocibles y el ejemplo positivo es coherente, pero faltan las definiciones operativas de `AB=media(|d_i|)` y `AS=s(|d_i|)`. Al usar solo diferencias positivas no se revela que el límite de sesgo absoluto no es el valor absoluto de la media de diferencias con signo. Agregar un ejemplo con signos mezclados.

40 CFR 58 §4.1.2–4.1.3 utiliza verificaciones QC de un punto para esos estimadores; no corresponde agrupar automáticamente controles de un punto, auditorías anuales y NPAP. Tampoco el periodo debe fijarse siempre en «un año» sin indicar el objetivo de agregación.

**Cambio:** especificar población, monitor/sitio, periodo, controles admisibles, datos faltantes y cálculo de percentiles. Distinguir el CV regulatorio de `s/|media|`. Los criterios EPA y EN se enseñan como marcos con jurisdicción y alcance definidos; añadir el documento colombiano adoptado si se pretende decidir sobre redes nacionales. El valor de diseño estadounidense requiere el periodo plurianual y las reglas de validez aplicables; no es solo un cuarto máximo aislado.

## 4. Vacíos conceptuales que deben resolverse con aplicación

No hace falta añadir más teoría general. Hace falta conectar los conceptos que ya aparecen para que el alumno complete el trabajo sin saltos. Los productos analíticos de esta sección corresponden al núcleo intermedio o a la extensión según la clasificación de la sección 5. En básico se seleccionan únicamente las tareas operativas; no se exigen todos estos productos.

### 4.1 Preparación y trazabilidad de los datos — M0, M2 y todos los talleres

Añadir un bloque inicial corto: importar CSV/Excel, separador decimal, unidades, fechas, identificadores, valores faltantes y diferencia entre cero y dato ausente. Conservar datos originales y registrar exclusiones, conversiones, redondeo y versiones.

El archivo de trabajo debería contener, como mínimo: instrumento, fecha/hora, campaña, analista, día, corrida, paso de concentración, réplica, referencia, indicación, unidad, escala de σ y estado de estabilización. El certificado ya contiene datos de lectura en `BD_DIAS` y hojas diarias; se debe documentar su extracción y emparejamiento, no pedir al estudiante que reconstruya el libro durante la clase.

**Producto:** base de análisis y registro de cambios con conteos comprobados por grupo.

### 4.2 Diferencia entre resultado individual, promedio y resultado futuro — M3, M6 y M8

El presupuesto debe corresponder al resultado que se entrega. Para un modelo simple con m días independientes y n lecturas independientes por día, la incertidumbre estadística del promedio puede incluir `σ²_día/m + σ²_e/(mn)`. Para una lectura futura de otro día no se dividen esas mismas componentes por los mismos tamaños de muestra. Las contribuciones comunes del patrón no desaparecen al aumentar lecturas.

La fórmula se usa como ejemplo de aplicación bajo ese modelo, no como regla para cualquier certificado. Si el resultado futuro se corrige con parámetros ajustados, debe considerarse también su incertidumbre y las covarianzas pertinentes.

**Producto intermedio:** comparar la U de una lectura, un promedio y un uso futuro, explicando qué cambia. En básico se interpretan resultados ya calculados y se identifica cuál corresponde al uso previsto.

### 4.3 Dependencia temporal y datos agrupados — M2, M3, M5–M7 y M11

Independencia aparece como requisito, pero faltan herramientas para examinarla. Añadir secuencia temporal, residuos por día/ciclo y una autocorrelación ilustrativa cuando sea útil. El diagnóstico debe decidir si se cambia el promediado, el diseño o el modelo. No necesita un curso completo de series temporales.

**Producto:** identificar qué observaciones aportan replicación independiente y qué componentes siguen sin estimarse.

### 4.4 Función de calibración → corrección → uso — M7, M8 y M10

Fijar una convención común, por ejemplo `y=a+b·x`, con y indicación y x referencia. Usar `x̂=(y−a)/b` solo bajo el modelo aplicable y propagar incertidumbre con parámetros, covarianza y nueva lectura. Distinguir esa operación de ajustar otra regresión intercambiando ejes.

Añadir interpolación, prohibición de extrapolar sin validación y entrega de correcciones por puntos cuando no se justifique una función continua.

**Producto:** corregir una lectura nueva, calcular su incertidumbre y declarar el intervalo de uso válido.

### 4.5 Corregir sesgos y evitar doble conteo — M6–M8

Falta una práctica que obligue a decidir qué error se corrige y qué incertidumbre queda después. No identificar tipo A con «aleatorio» ni tipo B con «sistemático»: describen formas de evaluación. Separar resolución, repetibilidad, variación diaria, falta de ajuste, deriva y referencia; comprobar si dos términos describen la misma variación.

**Producto:** presupuesto comentado que justifique cada inclusión y exclusión. Ninguna contribución sin datos debe convertirse en cero por ausencia de información.

### 4.6 Equivalencia, compatibilidad, conformidad y ausencia de evidencia — M4, M9 y M10

Los cuatro conceptos deben llevar a salidas distintas. Un p>0,05 no demuestra equivalencia. Un error compatible con cero dentro de una incertidumbre amplia no garantiza que el instrumento cumpla una tolerancia pequeña. Si se requiere equivalencia, fijar previamente el margen y usar un procedimiento adecuado; en básico basta interpretar un intervalo frente a ese margen.

**Producto intermedio/avanzado:** resolver un mismo resultado frente a una hipótesis de diferencia, un margen práctico y una especificación. En básico se aplica únicamente el criterio ya establecido y se explica cuándo remitir la revisión.

### 4.7 Cartas y acciones — M11

Distinguir fase de establecimiento de límites y seguimiento con límites fijados; elegir carta de individuales o de subgrupos según el dato disponible. Separar límites de control de tolerancias. No recalcular límites tras cada alarma sin investigar.

**Producto:** ficha de actuación ante alarma, incluyendo investigación, estado del patrón, revisión del trabajo afectado y criterio de retorno al servicio.

### 4.8 Validación de herramientas — transversal

El script B/C pasó su contraste con el ejemplo ISO; eso es evidencia útil, no validación de todas sus posibilidades. Faltan instrucciones de entorno y dependencias, criterios de convergencia explícitos, alcance de `U_xy=0` y respuestas ante datos inválidos. El avanzado debe verificar resultados frente a referencias y evaluar sensibilidad; no se le exige programar desde cero.

**Producto:** informe breve de verificación con entradas, resultados esperados, tolerancias y limitaciones.

## 5. Arquitectura propuesta: básico operativo, núcleo intermedio y extensión avanzada

### 5.1 Fronteras de contenido y autonomía

La clasificación se aplica a tareas, no solo a nombres de módulos. «Regresión», por ejemplo, incluye aplicar una ecuación entregada y también elegir un ajuste con covarianzas generales: son competencias distintas.

| Contenido o tarea | Nivel mínimo de aplicación autónoma dentro del curso | Tratamiento en básico |
|---|---|---|
| Unidades, trazabilidad, error, corrección y escala de σ | Básico | Aplicación con procedimiento definido. |
| Descriptiva por nivel, gráficos y detección inicial de anomalías | Básico | Calcular, representar, documentar e investigar según guía. |
| Diferenciar s, incertidumbre del promedio y U; leer cobertura | Básico | Interpretar y usar valores con su significado correcto. |
| Aplicar una función de calibración ya aprobada | Básico | Corregir lecturas y respetar el intervalo de uso. |
| Seguir una carta y una regla de decisión predefinidas | Básico | Actualizar controles y ejecutar acciones prescritas. |
| Seleccionar contrastes, interpretar supuestos y planear potencia | Intermedio | Sin selección autónoma de pruebas; contexto breve cuando haga falta. |
| Diseñar bloques/réplicas y estimar precisión intermedia con un modelo sencillo | Intermedio | Reconocer lecturas, ciclos y días; no ajustar ANOVA. |
| Seleccionar OLS/WLS, diagnosticar ajuste y evaluar falta de ajuste cuando proceda | Intermedio | Leer gráficos preparados y reconocer cuándo escalar la revisión. |
| Construir un presupuesto y justificar fuentes/cobertura | Intermedio | Interpretar un presupuesto aprobado y actualizar entradas permitidas. |
| Seleccionar/documentar reglas de decisión y establecer límites de control | Intermedio | Aplicar reglas y límites previamente establecidos. |
| Interpretar un informe de comparación clave y comprobar su documentación | Intermedio para revisión técnica; básico para lectura operativa | Reconocer diferencia, incertidumbre, escala y consecuencias de uso. |
| Ejecutar una comparación con protocolo, matrices y configuración fijados | Intermedio, con herramienta validada y revisión especializada de cambios | Fuera de la práctica analítica básica. |
| Elegir/validar modelos mixtos complejos o diseños anidados con varias componentes | Avanzado | No se enseña como competencia de salida. |
| Elegir/validar regresión con incertidumbre en ambos ejes y covarianzas generales | Avanzado | Solo se explica por qué algunos resultados requieren análisis especializado. |
| Construir/verificar matrices conjuntas y justificar `U_xy` en GGMR | Avanzado | Fuera de alcance. |
| Evaluar Monte Carlo, remuestreo agrupado y validación numérica | Avanzado | Fuera de alcance. |

El intermedio debe reconocer cuándo OLS/WLS deja de ser adecuado y remitir el análisis; no necesita dominar todos los métodos alternativos para tomar esa decisión. Ejecutar un GGMR preconfigurado no habilita a modificar sus matrices o validar una nueva situación experimental.

### 5.2 Curso básico operativo — 48 h

**Entrada:** aritmética, porcentajes y manejo elemental de hoja de cálculo. **Salida:** preparar y resumir datos, aplicar una calibración suministrada, usar correctamente incertidumbres reportadas, reconocer problemas y seguir procedimientos de control. Las decisiones de modelo, presupuesto y aceptación no previstas se remiten a revisión técnica.

Se reorganiza con bloques propios, evitando reproducir todos los títulos M1–M13 como si se impartieran íntegramente.

| Bloque básico | Referencia al temario | Horas |
|---|---|---:|
| B0 · Datos, unidades y herramientas | M0 | 2 |
| B1 · Medición UV, trazabilidad y cambio de escala | M1 | 5 |
| B2 · Resumen de lecturas y calidad de datos | M2 | 6 |
| B3 · Variación, promedios y lectura de incertidumbre | Fundamentos de M3/M8 | 5 |
| B4 · Aplicación de funciones y correcciones aprobadas | Uso operativo de M7 | 6 |
| B5 · Uso de presupuestos y resultados con incertidumbre | Uso operativo de M8 | 6 |
| B6 · Certificado y decisiones previstas en un procedimiento | Uso operativo de M9/M10 | 4 |
| B7 · Seguimiento de controles y acciones ante alarmas | Uso operativo de M11 | 4 |
| B8 · Indicadores básicos de redes y uso del certificado | Selección de M12 | 2 |
| TB · Taller de operación y evaluación | Datos adaptados de A/C | 8 |
| **Total básico** | | **48** |

B3 explica por qué más lecturas no eliminan un sesgo común y por qué importa el día de medición; no incorpora matrices de covarianza. B5 permite convertir U a u cuando corresponde y actualizar entradas identificadas en una plantilla aprobada; no exige desarrollar el modelo ni decidir correlaciones. B6 incluye una lectura breve de un informe BIPM como documento de la cadena, sin cálculo de GGMR.

Quedan fuera de los objetivos básicos: selección de pruebas t/F, cálculo de potencia, diseño factorial, estimación ANOVA de componentes, selección/validación del modelo de regresión, construcción independiente de presupuestos, formulación de reglas de decisión y establecimiento de intervalos de recalibración. Su exclusión es deliberada y debe figurar en la oferta.

### 5.3 Curso principal intermedio — 80 h

**Entrada:** competencias básicas de datos, unidades, descriptiva, uso de certificados y hoja de cálculo; pueden acreditarse sin cursar el básico. **Salida:** planear y analizar calibraciones habituales, justificar supuestos y modelos sencillos, construir presupuestos, documentar resultados y reconocer situaciones que requieren análisis avanzado.

| Módulo del núcleo intermedio | Horas | Alcance que se evalúa |
|---|---:|---|
| M0 · Datos, herramientas y diagnóstico | 2 | Base trazable, importación y comprobaciones. |
| M1 · Medición y trazabilidad | 4 | Entradas del modelo, escala y documentación. |
| M2 · Descriptiva y calidad de datos | 4 | Análisis por grupos y tratamiento documentado de anomalías. |
| M3 · Variación y distribuciones | 5 | Promedios, distribuciones de entrada y contribuciones comunes. |
| M4 · Inferencia aplicada | 6 | Intervalos, selección de pruebas, relevancia y potencia en casos definidos. |
| M5 · Diseño de estudios | 5 | Unidad experimental, bloques, replicación y diseño sencillo de robustez. |
| M6 · Precisión intermedia y ANOVA sencillo | 8 | Modelo de un factor aleatorio/día, componentes y límites de interpretación. |
| M7 · Regresión y uso de calibraciones | 9 | OLS/WLS, diagnóstico, corrección y detección de necesidad de otro método. |
| M8 · Presupuesto de incertidumbre | 9 | Modelo habitual, fuentes, doble conteo, cobertura y cadena. |
| M9 · Comparaciones clave | 5 | Lectura técnica, protocolo y ejecución con configuración fijada. |
| M10 · Certificado y conformidad | 4 | Resultado, corrección, especificación y regla documentada. |
| M11 · Control y deriva | 5 | Límites propios, tendencia y evidencia necesaria para recalibración. |
| M12 · Indicadores de redes | 3 | Selección de controles, cálculo e interpretación con alcance definido. |
| TI · Taller integrador y evaluación | 11 | Calibración habitual completa y revisión de sus limitaciones. |
| **Total intermedio** | **80** | |

En M6, el estudio D completo se usa para reconocer una estructura compleja y las limitaciones de su resumen; el ajuste analista × campaña con días anidados se desarrolla en la extensión. En M9, la matriz y el modelo se entregan justificados y fijados: el alumno comprueba su uso y entiende el informe; la construcción/validación del caso general se reserva al avanzado. Monte Carlo se traslada a la extensión, liberando tiempo para consolidar los presupuestos habituales.

El núcleo intermedio cubre la cadena analítica ordinaria del laboratorio. Su aprobación no implica dominio de todos los métodos incluidos en el temario original; los contenidos avanzados quedan identificados y tienen su propia evaluación.

### 5.4 Extensión avanzada — 32 h

**Entrada obligatoria:** dominio equivalente a la salida intermedia, comprobado mediante un análisis de calibración y presupuesto. **Salida:** seleccionar, contrastar y validar modelos y herramientas para situaciones complejas, justificando estructuras de dependencia y límites de sus conclusiones.

| Bloque de extensión | Referencia al temario | Horas |
|---|---|---:|
| A1 · Diseños complejos, interacción y modelos mixtos/anidados | Profundización M5/M6; caso D | 8 |
| A2 · Regresión con errores en ambos ejes y covarianzas generales; GGMR | Profundización M7/M9; caso B | 8 |
| A3 · Propagación avanzada, Monte Carlo y remuestreo por grupos | Profundización M8/M13 | 6 |
| A4 · Dependencia temporal, cambios de régimen y predicción | Profundización M11 | 3 |
| TA · Taller de validación y evaluación | Casos A/B/D complejos | 7 |
| **Total extensión** | | **32** |

La validación de herramientas se practica dentro de A1–A3 con ejemplos de referencia; TA integra esas competencias. Las 32 h presuponen datos depurados y herramientas preparadas, y acotan el trabajo a los modelos necesarios para los casos del laboratorio. No alcanzan para enseñar desde cero programación, toda la teoría de modelos mixtos y cualquier variante de regresión.

**Carga total del itinerario técnico: 80 h intermedias + 32 h de extensión = 112 h.** Una persona que ya domine el núcleo puede cursar solo la extensión. Una persona que llegue desde básico debe acreditar los requisitos del intermedio; las 48 h básicas no sustituyen las 80 h del núcleo.

### 5.5 Secuencia y condiciones de las horas

Las horas incluyen explicación aplicada, ejercicios, realimentación y evaluación supervisada. Excluyen pausas, estudio personal y operación prolongada de los instrumentos. Usar datos ya adquiridos cuando la estabilización o una campaña de varios días exceda la sesión; la duración estadística del estudio no equivale a horas de clase.

En el intermedio se conserva M0–M12, con anticipaciones breves: incertidumbre desde M1, agrupación e independencia desde M2 y un presupuesto simple en M3 antes de seleccionar pesos en M7. M10 no exige dominar un algoritmo GGMR. Los casos complejos se anuncian como frontera del núcleo y se resuelven en la extensión.

Las 62 h actuales están bien sumadas. El problema es de carga: M6 reúne demasiados modelos en 7 h, M7 demasiados métodos en 5 h y M8 varios presupuestos en 6 h. El taller actual tampoco alcanza para reconstruir los Excel y resolver cuatro estudios extensos. La reorganización distribuye esas tareas por su nivel real y aumenta el tiempo de aplicación.

Antes de admitir participantes, aplicar un diagnóstico de entrada. Ofrecer refuerzo cuando falten competencias; no compensarlas aumentando la velocidad. Confirmar las duraciones mediante un piloto de M6–M8 y los talleres. La misma rúbrica de dificultad debe usarse en la publicidad, los objetivos, los ejercicios y la certificación de aprovechamiento.

## 6. Sustitución de ejercicios por actividades de aplicación

Cada actividad debe incluir datos, tarea, herramienta autorizada, resultado esperado y criterio de aceptación. Las justificaciones deben ser breves y vinculadas con la decisión. Esta tabla es un banco de sustituciones, no un programa obligatorio para todas las rutas: selección de modelos ANOVA, validación GGMR y construcción de presupuestos se asignan al nivel indicado en la sección 5. El básico utiliza las actividades de operación e interpretación acotadas en TB.

| Actividad actual o insuficiente | Sustitución de aplicación | Evidencia que entrega el alumno |
|---|---|---|
| Deducir desviación de una rectangular | Convertir especificación, resolución y certificado a incertidumbre estándar. | Tabla con distribución, semiancho, divisor y unidad. |
| Deducir cuadrados medios esperados | Elegir entre dos modelos para datos con días compartidos o anidados. | Modelo seleccionado, componentes estimables y conclusión. |
| Construir toda la ANOVA a mano | Revisar una salida preparada y detectar un denominador incorrecto o una unidad mal definida. | Diagnóstico y resultado corregido con herramienta. |
| Deducir ecuaciones normales | Ajustar calibración, inspeccionar residuos y corregir una lectura nueva. | Parámetros, gráfico, corrección e intervalo válido. |
| Derivar sensibilidades del SRP | Utilizar sensibilidades suministradas y verificar su signo/unidad mediante cambios pequeños de entrada. | Presupuesto y comprobación numérica. |
| Comparar σ a 210 nm y en Huggins como práctica central | Resolver un cambio de escala entre SRP, Level 2 y cliente. | Factor, signo, metadatos y resultado actualizado. |
| Enumerar muchas pruebas de atípicos | Investigar una lectura extrema y documentar su tratamiento. | Decisión con evidencia y sensibilidad del resultado. |
| Decidir con R² o solo con pendiente | Evaluar errores y residuos en niveles bajos/altos y contra una especificación. | Decisión trazable a criterios definidos. |
| Calcular cartas externas y trasladarlas a CALAIRE | Construir una carta del proceso de origen y explicar por qué no permite decidir sobre otro. | Carta y límites explícitos de su uso. |
| Implementar GGMR desde cero | Reproducir un ejemplo de referencia y evaluar cambios al omitir correlaciones. | Comparación numérica, tolerancias y limitaciones. |

## 7. Talleres y evaluación según el alcance de cada ruta

### Material que debe prepararse

Los casos A y D no cuentan con el mismo paquete autónomo de datos, enunciado y solución que B/C. Preparar extracción documentada a CSV, diccionario de variables, unidad de análisis, solución revisada y resultados esperados. Mantener los Excel como fuente y objeto de revisión; su reconstrucción no debe consumir el tiempo de análisis.

No existe en el material revisado una comparación propia CALAIRE–BIPM lista para reproducir M9. Usar un ejemplo oficial o una adaptación expresamente identificada hasta disponer de ella. Los datos simulados deben rotularse y no presentarse como evidencia del laboratorio.

Los cuatro casos no se exigen completos en todas las rutas. Cada taller tiene productos distintos y conserva las fronteras de competencia definidas en la sección 5.

### TB · Básico operativo — 8 h

- **Aplicación de una calibración, 5 h:** preparar un subconjunto de A, resumir lecturas por nivel, aplicar una función entregada, usar la incertidumbre suministrada y completar los campos operativos de un certificado bajo procedimiento.
- **Seguimiento y comunicación, 3 h:** actualizar una carta del mismo proceso, identificar una alarma y ejecutar la ficha de acciones. Leer un resultado de comparación como antecedente de trazabilidad y decidir qué información falta o debe remitirse a revisión.

No se pide ajustar ANOVA, elegir la regresión, construir un presupuesto desde cero ni interpretar p-valores como objetivo de aprobación. Puede explicarse por qué estas tareas requieren otro nivel si surge la necesidad durante el caso.

### TI · Núcleo intermedio — 11 h

- **Caso A, 6 h:** datos, OLS/WLS y diagnóstico, precisión diaria con modelo sencillo, presupuesto, corrección y certificado. Los datos deben permitir completar un caso coherente sin introducir a mitad del taller un modelo avanzado no enseñado.
- **Caso B, 2 h:** ejecutar el análisis con herramienta/configuración entregadas, comprobar resultados e interpretar el informe. Identificar qué cambios exigirían revisar el modelo avanzado.
- **Caso C, 2 h:** separar requisitos de verificación y control propio; establecer límites preliminares con datos homogéneos y evaluar evidencia de deriva.
- **Caso D, 1 h:** reconocer diseño, confusión de factores y falta de replicación; formular la pregunta que debe resolver un análisis especializado. No se evalúa el ajuste completo del modelo mixto.

### TA · Extensión avanzada — 7 h

- **Casos A/B, 4 h:** contrastar modelos de ajuste y propagación, verificar matrices, evaluar escenarios justificados de dependencia y cuantificar el efecto en resultados y decisiones.
- **Caso D, 3 h:** comparar modelos plausibles, reproducir el análisis con días anidados, valorar la información disponible para cada componente y proponer un diseño mejor.

A1–A4 contienen prácticas previas con los mismos tipos de datos; el taller final integra y evalúa, sin ser el primer contacto con el método. La profundización de control/deriva se evalúa dentro de A4.

### Evaluación y fronteras de aprobación

Propuesta de rúbrica por ruta:

- **Básico:** datos/unidades 25 %; aplicación correcta del procedimiento 30 %; interpretación 25 %; registro y comunicación de incidencias 20 %.
- **Intermedio:** datos/unidades 20 %; selección/aplicación de métodos habituales 25 %; diagnóstico e interpretación 25 %; presupuesto, decisión y documentación 30 %.
- **Extensión avanzada:** estructura del problema y supuestos 20 %; selección/comparación de modelos 30 %; validación y sensibilidad 30 %; consecuencias y limitaciones de la decisión 20 %.

Aprobación propuesta: 75/100 y corrección de errores críticos dentro del alcance evaluado. Entre ellos: confundir U con u; invertir una corrección; mezclar escalas sin advertirlo; extrapolar sin soporte; excluir datos para lograr aprobación; usar límites ajenos como control propio; declarar conformidad sin criterio aplicable. En intermedio/avanzado se añade justificar un método inapropiado o confundir ausencia de significación con equivalencia.

Los resultados preparados permiten evaluar interpretación, pero no cuentan como evidencia de que el alumno sabe construir el modelo. La constancia de aprovechamiento debe expresar el alcance logrado. Ninguna ruta exige demostraciones ni programación desde cero. Reservar tiempo de realimentación y corrección dentro de las horas propuestas.

## 8. Contenido que conviene reducir o trasladar

- **Anexos opcionales:** ecuaciones normales, formas matriciales, cuadrados medios esperados, demostraciones de distribuciones/varianzas y derivación analítica de sensibilidades. Consultables, sin ejercicios obligatorios de deducción.
- **Menor prioridad en básico:** moda, curtosis, taxonomía extensa de escalas y catálogo de pruebas de atípicos. Enseñar solo lo necesario para interpretar los datos del curso.
- **Núcleo intermedio:** diseños sencillos, un factor aleatorio, OLS/WLS y presupuesto habitual. **Extensión avanzada:** interacción, modelos mixtos/anidados complejos y regresión con incertidumbre en ambos ejes/covarianzas generales. Las herramientas preparadas no borran esta frontera.
- **A3/M13 avanzado:** concentrarse en Monte Carlo, remuestreo por días/campañas cuando el número de grupos lo permita y validación de herramientas. Remuestrear seis días no crea evidencia de largo plazo.
- **Fuera del núcleo:** PCR/PLS para un fotómetro de una longitud de onda, recorridos espectroscópicos extensos y comparación detallada de otros contaminantes. Podrán incluirse como consulta si existe una necesidad real.
- **IA:** instrucción transversal breve para comprobar datos, fórmulas y fuentes. No reemplaza una competencia estadística ni necesita desplazar una práctica de calibración.

## 9. Orden de implementación y condiciones de cierre

### Antes de impartir

1. Corregir H03–H16 donde afectan decisiones o resultados; unificar los coeficientes de B y el estatus de los ejemplos externos.
2. Aprobar el alcance acotado del básico, el núcleo intermedio y la extensión avanzada de 32 h, con prerrequisitos, horas y competencias de salida. Identificar expresamente los contenidos que no se evalúan en cada ruta.
3. Sustituir las prácticas de demostración por las actividades de aplicación propuestas.
4. Identificar el procedimiento vigente de CALAIRE, la escala de σ, el presupuesto del SRP55 y la CMC/alcance aplicable. Si falta documentación, marcar el ejercicio como histórico o didáctico y limitar su conclusión.
5. Publicar paquetes A–D con datos y soluciones reproducibles; seleccionar actividades distintas para TB, TI y TA. Entregar una plantilla de certificado coherente con el modelo enseñado.

### Antes de publicar la versión definitiva

6. Revisar supuestos de las pruebas, condiciones de χ²/falta de ajuste, incertidumbre del promedio frente al uso futuro y doble conteo.
7. Completar actividades de control propio, acciones y métricas de red con su alcance.
8. Hacer un piloto del bloque más cargado —M6–M8 y taller A— y ajustar las horas según resultados reales de alumnos del nivel correspondiente.

### Comprobaciones objetivas para aceptar la revisión

- El básico completa un flujo operativo y declara sus exclusiones; no promete dominio analítico de todo el temario.
- El núcleo intermedio evalúa una calibración habitual completa y la detección de situaciones que requieren análisis avanzado.
- La extensión evalúa los modelos complejos y su validación con prerrequisitos intermedios acreditados.
- Interpretar una salida preparada y construir/justificar su modelo tienen objetivos y evidencias de evaluación distintos.
- No hay ejercicios obligatorios de demostración ni deducción en el núcleo o taller.
- Cada límite numérico tiene fuente, versión, estadístico, unidad, diseño y justificación de aplicabilidad.
- Cada resultado de referencia coincide con el cálculo reproducible dentro del redondeo declarado.
- Cada presupuesto identifica mensurando, resultado al que aplica, entradas, correlaciones, cobertura y fuentes de datos.
- Los ejemplos históricos, externos, simulados y propios están identificados desde el enunciado.
- El material por módulo puede ejecutarse en las horas asignadas con los datos y herramientas entregados.

## 10. Registro de verificaciones y límites de la auditoría

**Comprobado:** las horas actuales suman 62/66; el script B/C ejecuta correctamente; reproduce los coeficientes OLS y las tablas GGMR principales, el ejemplo de validación ISO/TS 28037, la descriptiva C1/C2 y los contrastes publicados. La discrepancia del apartado 5 de B es de documentación. La validación ISO es de un ejemplo y con bloques cruzados nulos; no valida cualquier matriz o dataset.

**Comprobado en libros:** existen datos por lectura en `BD_DIAS` y hojas diarias; `Resumen!D6:F11` distingue pendiente libre, intercepto y pendiente forzada; `Uexp!Q8` realiza la selección del máximo descrita. En el libro R&R, por ejemplo, `455ppb!N7:N8` usa B6:B17/C6:C17, mientras las medias emplean hasta la fila 23. Este defecto de rango del libro ya está anunciado en el temario y es útil como revisión práctica; debe estar corregido en una solución de referencia.

**Comprobado por recálculo:** el modelo ANOVA equilibrado descrito reproduce las F y rangos de dispersión diarios principales. Esa coincidencia valida la reproducción numérica bajo el modelo, no demuestra por sí sola su alcance causal ni la precisión de sus componentes.

**Pendiente:** reconstrucción/recálculo completo del certificado, exactitud de todas sus fórmulas, vigencia del procedimiento de CALAIRE, presupuesto actual propio, CMC reconocida y evidencia suficiente para fijar intervalos. Tampoco se verificó exhaustivamente cada página/cita de todos los libros de la bibliografía ni todas las ediciones vigentes de las normas. La versión docente debe congelar y declarar sus referencias; el curso puede reproducir una edición histórica sin presentarla como vigente.

**Fuentes de contraste principales:** protocolo local `docs/BIPM.QM-K1_2.protocol.pdf`, especialmente §1.1, protocolo A §§7–8 y Apéndice 1; `docs/SRP6008_spec_cert.pdf`, p. 2; `docs/srp_qapp.pdf`, §§6.2.3, 14.2 y Tabla 7-1; `docs/o3_tad_508_20230906_final.pdf`, Tabla 4-1, §4.4 y apéndice de ecuaciones; `docs/ISO 5725-4_1994.pdf`, cláusula 5; `docs/ISO 28037.pdf`, cláusula 10, Tablas 25–26; y 40 CFR 58, Apéndice A local, §§4.1.2–4.1.3. Contraste externo: [orientación BIPM sobre la nueva sección eficaz](https://www.bipm.org/en/ozone/new-absorption-cross-section), [informe de implementación BIPM](https://www.bipm.org/documents/d/guest/rapportbipm2024-03), [documento TAD EPA](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1016Y93.TXT) y [ficha NIST SRP 6008](https://www.nist.gov/sri/standard-reference-instruments/sri-6008-ozone-standard-reference-photometer). Consulta realizada el 23-10-2026.
