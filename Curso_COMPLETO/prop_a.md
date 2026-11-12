# Propuesta de ajuste del contenido del curso

**Curso:** Estadística aplicada a la fotometría de ozono con el SRP.  
**Fecha:** 23 de octubre de 2026.  
**Estado:** propuesta curricular para revisar antes de estimar la duración.  
**Base documental:** [temario actual](temario_curso.md), auditorías [A](audit_a.md), [B](audit_b.md) y [C](audit_c.md), y sus revisiones [A](rev_audits_a.md), [B](rev_audits_b.md), [C](rev_audits_c.md) y [D](rev_audits_d.md).

## 1. Orientación de la propuesta

Se propone conservar el recorrido completo del trabajo de CALAIRE —medir, tratar datos, calibrar, evaluar incertidumbre, comparar, reportar y vigilar los patrones— y reorganizarlo en tres niveles acumulativos. El contenido se decide por la competencia que necesita el participante y por la validez de su aplicación. Las horas se calcularán después de fijar las actividades, las herramientas y la evaluación de cada nivel.

La mejora principal consiste en conectar las partes que hoy pueden aprenderse como procedimientos aislados: qué resultado se quiere obtener, qué datos lo representan, qué variación se estima, qué modelo de calibración se utiliza y qué incertidumbre corresponde a su uso posterior. Esa conexión debe aparecer desde el básico y profundizarse en los niveles siguientes.

El curso mantendrá una orientación práctica. Cada tema incluido en un nivel tendrá explicación, ejercicio y evidencia de aprendizaje en clase. Las deducciones algebraicas se trasladarán a anexos de apoyo; las prácticas exigirán calcular, interpretar y tomar decisiones. Los defectos encontrados en los archivos servirán para construir ejemplos conceptuales preparados, sin hacer depender el aprendizaje de localizar celdas o reparar libros durante la clase.

### Cómo se resuelven las diferencias entre las revisiones

Las revisiones no recomiendan una misma auditoría como base. Se adopta una síntesis por decisiones de contenido:

- De B se toma la organización acumulativa por temas y la capacidad de reconocer cuándo un procedimiento deja de ser aplicable.
- De A se toman las condiciones de validez de los métodos, la distinción entre resultados y escalas temporales, y la evaluación mediante tareas concretas.
- De C se toman los hallazgos sobre pérdida de signo, variación de la referencia entre días y mezcla indebida de observaciones en la estimación de incertidumbre.
- De las revisiones A y D se incorporan las rectificaciones a las soluciones de C: existe un máximo puntual entre incertidumbre calculada y CMC en la plantilla; el cambio de escala requiere identificar el par numérico implementado; una función de incertidumbre o un presupuesto actualizado necesita justificación propia.
- De la revisión B se conserva el criterio de cubrir el recorrido del curso en los tres niveles, con práctica real y sin sustituir contenidos por menciones. Su recomendación de usar siempre el día como réplica se reemplaza por una definición dependiente de la pregunta y del diseño.
- De la revisión C se recuperan la continuidad entre módulos y la riqueza de los ejemplos. Se descartan sus conclusiones sobre suficiencia de las duraciones y su aprobación de correcciones que otras revisiones contradicen con evidencia localizada.

El resultado es un programa acumulativo con fronteras explícitas: el básico ejecuta análisis acotados con herramientas revisadas; el intermedio selecciona y justifica los métodos habituales; el avanzado desarrolla y valida los análisis complejos. La aprobación del curso aporta evidencia de aprendizaje; la autorización para firmar o asumir una función técnica corresponde al laboratorio.

## 2. Competencias y progresión

### Básico — ejecutar e interpretar un procedimiento definido

Al finalizar, el participante podrá preparar datos pareados, calcular errores con signo, describir variación, efectuar inferencias sencillas bajo condiciones dadas, ejecutar un ANOVA de un factor configurado, ajustar una recta OLS en un caso adecuado, construir un presupuesto sencillo en plantilla, aplicar una función de uso y una regla de decisión, y actuar ante señales de control.

También deberá reconocer las condiciones que obligan a detener el procedimiento y solicitar revisión: dependencia no contemplada, cambios de escala, atípicos sin explicación, residuos estructurados, incertidumbre relevante en ambos ejes, cobertura insuficientemente sustentada o resultados próximos a un límite. Reconocer estas situaciones se evaluará con casos; no se utilizará como sustituto del contenido básico.

### Intermedio — seleccionar y justificar el análisis habitual

Incluye las competencias básicas y añade selección de pruebas y unidades de repetición, diseño de estudios rutinarios, componentes de varianza, OLS/WLS, incertidumbre de la predicción inversa, covarianzas sencillas, cobertura, propagación al cliente, evaluación de deriva y justificación de decisiones y certificados.

### Avanzado — desarrollar, contrastar y validar modelos complejos

Incluye los niveles anteriores y añade modelos mixtos y anidados del R&R, regresión con incertidumbre en ambos ejes y covarianzas generales, reproducción de comparaciones bajo un protocolo definido, validación de herramientas, Monte Carlo y evaluación de alternativas cuando los supuestos habituales no son adecuados.

**Acumulación:** I comprende B más los contenidos nuevos de I; A comprende B e I más los contenidos nuevos de A. El acceso directo a I o A requiere comprobar las competencias previas mediante un ejercicio diagnóstico. El contenido ya acreditado se reconoce; cualquier refuerzo responde a una carencia identificada.

## 3. Organización y reglas comunes

Se conservan los identificadores M1–M12 para facilitar la revisión del temario. Se incorpora M0 como preparación transversal y M13 como bloque definido de métodos avanzados. Cada nivel recorre M0–M12; M13 entra en A. Las ampliaciones de nivel se especifican en cada módulo.

La secuencia será:

1. **M0–M4:** preparar datos, entender la medición, describir variación y obtener conclusiones acotadas.
2. **M5–M8:** diseñar la comparación, estimar precisión, ajustar la calibración y evaluar incertidumbre.
3. **M9–M12:** comparar patrones, reportar resultados, vigilar estabilidad y aplicar los resultados en redes.
4. **M13 en A y taller por nivel:** contrastar métodos y resolver el recorrido completo.

Antes de calcular, cada ejercicio identificará el mensurando o respuesta, el resultado de interés, la unidad de repetición y la escala temporal. Al cerrar, el participante entregará resultado con unidades, interpretación y acción que se desprende del análisis.

Se usará una convención común: `x` es el valor de referencia, `y` la indicación del instrumento y `e = y − x` el error con signo. Para la recta `y = a + b·x`, `a` es el intercepto y `b` la pendiente; su aplicación inversa es `x̂ = (y − a)/b`. Cuando una fuente use otra notación, se hará la correspondencia antes del ejercicio. El símbolo `D` se definirá localmente para evitar confundir la razón fotométrica con una diferencia de equivalencia.

## 4. Contenido y práctica por módulo

### M0. Preparación de datos y herramientas

**Resultado esperado:** producir una tabla utilizable y conservar la relación entre cada lectura, su referencia y las condiciones de adquisición.

**B:** tabla de datos con identificadores de nivel, lectura, ciclo, día e instrumento; emparejamiento referencia–indicación; unidades; fechas; ceros negativos; datos faltantes; conservación del signo; separación entre dato original y dato calculado. Uso de hoja de cálculo, gráficos y plantillas del curso.

**Práctica B:** organizar un conjunto corto, calcular `e`, detectar una pareja desplazada y un dato faltante, y documentar la corrección sin borrar el original.

**I añade:** preparación de datos de varios días, analistas y campañas; comprobación de conteos y agrupaciones; transformación de tablas anchas a una estructura de análisis; registro de exclusiones justificadas.

**Práctica I:** preparar la tabla de una campaña y comprobar que los resúmenes diarios se reconstruyen desde las parejas originales.

**A añade:** especificación de entradas, salidas y comprobaciones de un proceso reproducible de cálculo; contraste entre herramientas y trazabilidad de transformaciones.

**Práctica A:** reproducir un resultado desde datos originales con una segunda herramienta y explicar las discrepancias relevantes.

### M1. Fotometría UV, ecuación de medida y trazabilidad

**Resultado esperado:** relacionar la señal del SRP, el valor de ozono y la escala declarada.

**B:** mensurando y unidades; equivalencia de ppb como fracción molar con nmol/mol en esta aplicación; error, sesgo, corrección, calibración, verificación y ajuste; cadena de trazabilidad del caso de CALAIRE. Ley de Beer–Lambert y evaluación de la ecuación del SRP mediante plantilla, con magnitudes y unidades definidas. Conversión explícita a nmol/mol cuando la ecuación produce mol/mol.

**Práctica B:** calcular una concentración a partir de entradas suministradas y recalcular tres valores con dos valores de sección eficaz declarados; indicar el signo del cambio.

**I añade:** razón de señales de las dos celdas, definición de los cuatro conteos, compensación de deriva común, correcciones de presión y temperatura y comprobación de unidades. Diferencia entre cambiar la escala y corregir un instrumento.

**Práctica I:** comparar dos mediciones en escalas distintas, calcular el efecto sobre `e` y sobre un error relativo con denominador definido, y detectar una corrección de temperatura aplicada dos veces.

**A añade:** dependencia espectral y térmica de la sección eficaz y tratamiento de sus contribuciones comunes en comparaciones y resultados absolutos.

**Práctica A:** contrastar dos escenarios de presupuesto y explicar qué contribuciones se cancelan en la diferencia y cuáles permanecen en el resultado declarado.

**Ajuste del temario:** sustituir un porcentaje universal de cambio de escala por el cociente de los valores realmente implementados. Los pares 1,147/1,1329 y 308,32/304,39 producen incrementos distintos; el ejercicio declarará cuál usa. Los presupuestos históricos se identificarán como tales.

### M2. Estadística descriptiva y elección de la respuesta

**Resultado esperado:** describir los datos que responden a la pregunta planteada.

**B:** media, mediana, varianza, desviación estándar, rango y cuantiles; histogramas, cajas y series temporales; diferencias entre dispersión de lecturas y error estándar; CV y sus limitaciones cerca de cero. Detección gráfica de observaciones inusuales y revisión de causas físicas. Redondeo al final.

**Práctica B:** comparar la dispersión de indicaciones brutas y de diferencias pareadas en un nivel medido varios días; explicar cuánto de la variación observada puede proceder del cambio de la referencia. Conservar los valores negativos del cero.

**I añade:** resúmenes dentro y entre grupos, mediana y MAD como descripción robusta, y comparación de errores entre concentraciones. La diferencia `e` puede conservar una tendencia con `x` si existe sesgo proporcional.

**Práctica I:** comparar `y`, `e` y medias diarias; elegir la respuesta para una pregunta de precisión y otra de calibración, apoyándose en gráficos frente a referencia y tiempo.

**A añade:** evaluación de la sensibilidad de los resultados a transformaciones, agregaciones y observaciones influyentes.

**Práctica A:** comparar el análisis de `e` y `|e|` en un ejemplo con sesgos opuestos y mostrar qué información pierde cada resumen.

**Ajuste del temario:** las pruebas de atípicos pasan a M4/M6 después de sus prerrequisitos. Se permite describir indicaciones brutas; su dispersión agrupada solo se interpreta como precisión cuando el diseño y el modelo lo justifican.

### M3. Probabilidad, distribuciones y dependencia

**Resultado esperado:** elegir distribuciones sencillas y comprender cuándo promediar reduce la incertidumbre.

**B:** variable aleatoria, normal, rectangular y triangular; esperanza y varianza mediante ejemplos; semiamplitud `h` frente a resolución total `δ`; `h/√3` y `δ/√12`; desviación de lecturas frente a desviación de un promedio. Dependencia temporal reconocible en una serie y límites de `1/√n`. Uso de t y F con tablas o funciones suministradas, y papel de sus grados de libertad, como preparación para los cálculos guiados de M4 y M6.

**Práctica B:** convertir especificaciones en incertidumbres estándar y comparar promedios de datos independientes con una serie que presenta deriva. Explicar por qué aumentar lecturas no elimina un componente común.

**I añade:** covarianza y correlación; varianza de combinaciones lineales; propiedades y selección de las distribuciones t, chi-cuadrado y F; gráficos de probabilidad y diagnóstico de dependencia. Separación entre variación de corto plazo y entre días.

**Práctica I:** calcular la incertidumbre de una diferencia con y sin covarianza y examinar una serie antes de decidir cómo formar promedios para M4.

**A añade:** covarianzas comunes entre canales y puntos; modelos de dependencia y elección del tiempo de promedio, incluida desviación de Allan cuando haya series adecuadas.

**Práctica A:** comparar estrategias de promediado con ruido y deriva en datos preparados, y justificar una estrategia de adquisición.

**Ajuste del temario:** la propagación no lineal de la razón fotométrica a concentración se desarrolla en M8. Cerca de cero se trabaja con incertidumbre absoluta; la expresión relativa no se evalúa en cero. No se empleará una fórmula de tamaño efectivo como remedio universal a la dependencia.

### M4. Inferencia y relevancia metrológica

**Resultado esperado:** estimar un efecto y valorar la evidencia sin confundir significación con aptitud para el uso.

**B:** muestra, grados de libertad, intervalo de confianza con t, hipótesis, valor p y errores de decisión. Estimación y prueba de un error medio en un nivel, usando diferencias y unidades de repetición previamente justificadas.

**Práctica B:** calcular un intervalo para un error medio y contrastarlo con cero y con una magnitud metrológicamente relevante. El conjunto didáctico incluirá información suficiente para justificar la inferencia.

**I añade:** t pareada, Welch, pruebas e intervalos sobre varianzas, potencia y tamaño de muestra ligados a una diferencia de interés; incertidumbre de una desviación estimada; Grubbs y Dixon dentro de su campo de aplicación.

**Práctica I:** elegir el contraste en dos situaciones de laboratorio y planear la repetición necesaria para detectar un cambio definido. Comparar la precisión con que se estima una desviación usando pocos o muchos grupos.

**A añade:** multiplicidad, pruebas de equivalencia con márgenes definidos y diagnóstico de consistencia mediante chi-cuadrado.

**Práctica A:** resolver un caso donde no rechazar diferencia cero y demostrar equivalencia producen conclusiones distintas; evaluar el efecto de analizar varios niveles simultáneamente.

**Ajuste del temario:** eliminar la regla única de tamaño muestral. Una media, diferencias pareadas y dos grupos independientes requieren planteamientos distintos. Ni ocho lecturas ni seis días constituyen por sí solos un tamaño válido para cualquier pregunta. Las exclusiones requieren justificación técnica además del resultado de una prueba.

### M5. Diseño de la comparación y estudios de robustez

**Resultado esperado:** relacionar lo que se quiere estimar con lo que realmente varía en el experimento.

**B:** factores, niveles, bloques, lectura, ciclo, corrida y día; repetición independiente frente a observaciones dependientes; identificación práctica de estructuras cruzadas y anidadas.

**Práctica B:** representar el diseño 12 puntos × 8 lecturas × 6 días e identificar qué variación se observa, qué queda confundido y qué datos adicionales serían necesarios para separarla.

**I añade:** aleatorización, bloqueo, factoriales y robustez; distribución del esfuerzo entre niveles de concentración, ciclos y días; relación con potencia y precisión de estimación.

**Práctica I:** diseñar un factorial de robustez del Level 2 con respuesta, factores, orden, bloques y criterio de evaluación definidos.

**A añade:** diseños anidados escalonados y diseño de R&R; elección de analistas y campañas; comparación de diseños por componentes identificables y precisión esperada.

**Práctica A:** proponer un estudio que separe lectura, ciclo, día y analista y explicar qué mejora al añadir analistas frente a añadir lecturas.

**Ajuste del temario:** las secuencias BIPM, QAPP, SOP, TAD y EN se compararán como diseños con objetivos distintos. Su similitud numérica no establece que sean intercambiables ni que alguno sea el procedimiento adoptado por CALAIRE.

### M6. ANOVA, componentes de varianza y precisión

**Resultado esperado:** separar fuentes de variación y utilizar sus estimaciones de acuerdo con el resultado que se quiere reportar.

**B:** repetibilidad y precisión intermedia; ANOVA de un factor mediante plantilla, lectura de sumas de cuadrados, grados de libertad, cuadrados medios y F. Estimación guiada de componentes dentro y entre días para un caso equilibrado cuyo modelo ya está definido; suma de varianzas y raíz para obtener una desviación.

**Práctica B:** resolver un caso de errores con signo a un nivel, estimar ambas componentes y explicar por qué la variación de una lectura de corto plazo difiere de la de otro día. La plantilla incluirá reglas para detectar supuestos incumplidos y estimaciones problemáticas.

**I añade:** elección de efectos fijos y aleatorios, componentes con tablas de cuadrados medios esperados suministradas, modelos habituales de dos factores, interacción, residuos y heterogeneidad de varianzas. Uso de Cochran y de herramientas de ISO 5725 cuando el diseño corresponda. Enlace entre componentes e incertidumbre del resultado.

**Práctica I:** elegir y resolver un modelo de dos factores preparado; comparar incertidumbre de un promedio de calibración y dispersión de uso futuro; justificar qué componentes entran en cada caso.

**A añade:** estructura completa analista × campaña con días anidados, elección del denominador de los contrastes, precisión de componentes, estimaciones negativas y alternativas de estimación. Diferencias entre R&R industrial, precisión intralaboratorio e interlaboratorio; aplicabilidad de ISO 5725, incluida la evaluación del sesgo de un laboratorio.

**Práctica A:** analizar un conjunto con signo y estructura documentada; comparar modelos admisibles, cuantificar su incertidumbre y justificar conclusiones considerando interacción y multiplicidad.

**Ajuste del temario:** retirar la afirmación de que las lecturas consecutivas siempre subestiman la repetibilidad. Pueden caracterizar variación de corto plazo; la generalización depende de su dependencia y de las condiciones. El residual de medias diarias no se renombrará como ruido de lectura. Las conclusiones del R&R sobre `|e|` se conservarán únicamente como conclusiones de esa respuesta, hasta reconstruir y analizar los errores con signo.

### M7. Regresión, calibración inversa y función de uso

**Resultado esperado:** obtener una función de calibración defendible y aplicarla en el sentido correcto.

**B:** ajuste OLS con intercepto en un caso con condiciones adecuadas; pendiente, intercepto, residuos y límites de R²; intervalo de uso. Aplicación de `x̂ = (y − a)/b` y diferencia entre valor corregido y corrección aditiva `x̂ − y`.

**Práctica B:** ajustar una recta en hoja de cálculo, revisar residuos, calcular un valor corregido y comprobar el signo de la corrección con un ejemplo conocido.

**I añade:** incertidumbres de los parámetros y su covarianza, bandas de confianza y predicción, incertidumbre de uso inverso, origen forzado, WLS y elección de pesos. Falta de ajuste solo con una estimación válida del error puro y niveles efectivamente comparables.

**Práctica I:** comparar OLS y WLS, justificar el ajuste y calcular la incertidumbre de un valor de uso. Decidir si los datos permiten una prueba de falta de ajuste; cuando la referencia cambia entre repeticiones, emplear un modelo apropiado o un conjunto adicional preparado.

**A añade:** regresión con incertidumbre en ambos ejes, GDR, GMR y GGMR; representación matricial y diagnóstico por residuos y chi-cuadrado. Dependencia entre puntos y entre ejes.

**Práctica A:** contrastar métodos sobre el mismo conjunto y explicar qué cambia al introducir una componente común. Resolver además un ejemplo de referencia para verificar la herramienta.

**Ajuste del temario:** separar ajuste, inversión y aplicación posterior. No fijar automáticamente `ν = n − 2` ni aplicar una F de falta de ajuste sin revisar su modelo. Los ceros inicial y final comparten nivel nominal, pero pueden revelar deriva. La notación del protocolo BIPM se traducirá a la convención del curso.

### M8. Incertidumbre del resultado, uso posterior y CMC

**Resultado esperado:** construir un presupuesto coherente con el resultado y evitar reducciones o sumas de componentes sin justificación.

**B:** modelo de medición; evaluación tipo A y B; conversiones `u = U/k`, resolución y tolerancias; elección entre `s` y `s/√n` bajo un procedimiento definido; presupuesto tabular y sensibilidades numéricas por Kragten en un caso de entradas independientes y linealización adecuada. Incertidumbre combinada y expandida, cobertura, unidades y redondeo.

**Práctica B:** construir un presupuesto sencillo de calibración e identificar por qué dividir una dispersión de distintos niveles y días por √576 no estima automáticamente la incertidumbre buscada. Usar `k ≈ 2` solo en el ejemplo preparado que satisface esa aproximación; ante pocos grados de libertad, solicitar el tratamiento correspondiente.

**I añade:** sensibilidades analíticas, covarianzas, grados de libertad efectivos y cobertura con condiciones explícitas; separación entre resultado individual, promedio de calibración y resultado futuro. Tratamiento de corrección de sesgo y deriva; prevención del doble conteo entre residual de regresión, precisión y otras contribuciones. Propagación desde SRP a Level 2 y desde Level 2 a cliente.

**Práctica I:** construir presupuestos para esos tres resultados, comparar sus diferencias y llevar la incertidumbre de la función calibrada al uso de un fotómetro de cliente.

**A añade:** componentes comunes, sección eficaz en resultados absolutos y comparaciones, límites de la linealización y construcción de una función de incertidumbre sobre un intervalo. Relación entre incertidumbre evaluada, incertidumbre declarada y CMC aplicable, con la misma magnitud, unidades, cobertura y alcance.

**Práctica A:** contrastar presupuestos histórico y alternativo bajo supuestos declarados; verificar punto a punto y en el intervalo una función propuesta, incluidos el máximo puntual y cualquier ajuste posterior de la curva.

**Ajuste del temario:** no presentar el presupuesto interno del SRP27 como presupuesto propio del SRP55. No prescribir una función cuadrática o cúbica por preferencia. Para un intervalo bilateral central del 95 %, cuando proceda Student, se usará la convención acumulada `k = t_(0,975;ν_eff)`. La CMC se tratará como capacidad documentada, no como reemplazo del presupuesto ni como producto automático de una comparación favorable.

### M9. Comparaciones de patrones y equivalencia

**Resultado esperado:** calcular e interpretar una diferencia entre patrones con la incertidumbre que corresponde a su dependencia.

**B:** comparación directa en puntos definidos; diferencia, incertidumbre y compatibilidad; `E_n` en un ejemplo con condiciones y criterio previamente especificados. Se enseñará primero la incertidumbre de la diferencia: `u²(Δ) = u²₁ + u²₂ − 2·cov(1,2)`; la cuadratura simple se aplicará en el ejercicio de independencia justificada.

**Práctica B:** calcular diferencias y su incertidumbre en dos puntos de un caso didáctico preparado; interpretar el indicador normalizado y distinguir compatibilidad, conformidad y respaldo a una capacidad de medición.

**I añade:** comparación directa frente a transferencia; interpolación mediante una recta, covarianza de parámetros y efectos de contribuciones compartidas sencillas. Relación entre protocolo, presupuesto y resultado.

**Práctica I:** obtener diferencias interpoladas e incertidumbres a partir de parámetros y covarianzas suministrados y revisados; resolver también un escenario de diferencia con una contribución común explícita.

**A añade:** construcción de matrices de covarianza, GGMR y reproducción completa de una comparación bajo supuestos definidos; contraste de variantes del presupuesto y diagnóstico del ajuste.

**Práctica A:** resolver el caso B completo con herramienta contrastada y emitir un informe de sensibilidad a las hipótesis de incertidumbre. La extensión a covarianzas cruzadas no nulas se realizará únicamente con una herramienta que las admita y ejemplos de referencia propios.

**Ajuste del temario:** utilizar el caso B disponible como adaptación didáctica; los datos propios de BIPM.QM-K1 serán una sustitución posterior si se dispone del paquete suficiente. El resultado docente no se presentará como grado de equivalencia oficial de CALAIRE. Un resultado de comparación es evidencia para evaluar una CMC, no su aprobación automática.

### M10. Resultado, certificado y conformidad

**Resultado esperado:** entregar información de calibración utilizable y aplicar el criterio correspondiente al servicio definido.

**B:** resultado de calibración, función de uso y declaración de conformidad; contenido técnico del certificado; criterio de aceptación y regla de decisión suministrados; banda de guarda y acción en la zona próxima al límite.

**Práctica B:** completar un certificado docente con resultado, unidades, U, k, intervalo, escala y función de uso; resolver ejemplos con y sin declaración de conformidad.

**I añade:** selección y justificación de reglas de decisión; riesgo de falsa aceptación y rechazo; relación de incertidumbre y tolerancia con convención definida; coherencia entre presupuesto, resultado y declaración.

**Práctica I:** resolver un resultado próximo al límite con dos reglas y explicar cómo cambia la decisión y qué riesgo se asume.

**A añade:** riesgo específico y global bajo modelos explícitos, requisitos bilaterales y decisiones con dependencia.

**Práctica A:** cuantificar el riesgo de una decisión para una distribución y especificación definidas y justificar la regla elegida.

**Ajuste del temario:** reunir los regímenes externos en una ficha común con documento y edición, equipo, etapa, diseño, estadístico, divisor y unidad. M11 y el caso C usarán esa misma ficha. Mientras falte la evidencia de adopción local, los ejercicios serán escenarios expresamente definidos. Aplicar una corrección calculada se distinguirá del cambio efectivo de parámetros del instrumento; una corrección puede ser aditiva o funcional.

### M11. Control de estabilidad, deriva y acciones

**Resultado esperado:** detectar cambios y decidir una acción técnica sustentada.

**B:** causas comunes y especiales; carta de individuales y rango móvil en un caso adecuado; límites de control frente a tolerancias; reglas de alarma y plan de acción. Línea base vinculada al instrumento y al proceso que se vigilan.

**Práctica B:** completar una carta de historial preparado, detectar señales y decidir entre investigar, repetir, retener un resultado o solicitar recalibración según el procedimiento del caso.

**I añade:** construcción de línea base, dependencia, regresión de deriva, predicción e inclusión de deriva en la incertidumbre de uso.

**Práctica I:** estimar deriva en un historial comparable y evaluar el impacto de prolongar su utilización.

**A añade:** intervalos de recalibración fundamentados, cartas EWMA y CUSUM y evaluación de sensibilidad frente a falsas alarmas.

**Práctica A:** comparar cartas ante cambios pequeños y proponer un intervalo de revisión con criterio y riesgo definidos.

**Ajuste del temario:** el historial NIST servirá para aprender con esos instrumentos; no será la línea base del Level 2 de CALAIRE. Los seis días de una calibración no se convertirán en historial de largo plazo. Si falta historial propio suficiente se empleará una serie didáctica rotulada.

### M12. Aplicación en redes de monitoreo

**Resultado esperado:** distinguir los indicadores de desempeño de la red de la incertidumbre de una calibración.

**B:** diferencia relativa con referencia y signo definidos, indicadores de precisión y sesgo de un escenario de red y cálculo con plantilla. Porcentajes cerca de cero y necesidad de una métrica absoluta. Relación entre certificado, verificación y medición ambiental.

**Práctica B:** calcular indicadores con errores de ambos signos y explicar la diferencia entre `media(|d_i|)` y `|media(d_i)|`.

**I añade:** límites de confianza con chi-cuadrado y t, distinción entre límites unilaterales y cobertura bilateral, efecto de la escala de sección eficaz y evaluación del cero. Estimación didáctica de un umbral de detección bajo hipótesis expresas.

**Práctica I:** calcular los indicadores y sus límites en un conjunto preparado; repetir con un cambio de escala en uno de los equipos e interpretar signo y denominador. Comparar un umbral obtenido del ruido del cero con lo necesario para validar un límite de detección.

**A añade:** contraste entre marcos de desempeño ambiental y de calibración, efectos comunes de trazabilidad sobre una red y consecuencias para resultados agregados.

**Práctica A:** analizar una discrepancia entre conformidad de un instrumento y desempeño de una red y proponer la evidencia necesaria para resolverla.

**Ajuste del temario:** separar controles de un punto, auditorías y otras evaluaciones. Las fórmulas de AB, AS, CV y sus límites llevarán definiciones y ámbito. La regla `3·s₀` será un ejemplo condicionado del comportamiento del blanco; no se presentará como validación completa del límite de detección.

### M13. Contraste de métodos avanzados

**Ubicación:** A, después de M8 y M9. Se reemplaza el inventario abierto de temas por tres aplicaciones definidas.

1. **Monte Carlo:** propagar distribuciones de entrada, conservar dependencias y comparar con la linealización GUM en un caso de calibración inversa.
2. **Salidas múltiples:** obtener conjuntamente pendiente, intercepto y valores corregidos, conservando su covarianza.
3. **Remuestreo y robustez:** aplicar bootstrap con la agrupación que exige el diseño y contrastar un método robusto en un ejemplo pertinente.

**Práctica A:** resolver un caso donde el método alternativo cambia o confirma una conclusión, explicar la estabilidad numérica del resultado y justificar cuál se usa.

PCR/PLS, aprendizaje automático, uso de IA y otros temas de quimiometría no integran el contenido requerido de esta propuesta: no son necesarios para resolver las tareas definidas. Su incorporación futura requerirá una necesidad y una práctica propias. La validación de cálculos se integra en los casos de A.

## 5. Casos y taller integrador

Se utilizarán cuatro familias de casos, con versiones graduadas. Cada paquete incluirá datos suficientes, diccionario de variables, enunciado, plantilla cuando corresponda, solución revisada y criterios de evaluación. Los datos faltantes se suplirán con conjuntos didácticos identificados; no se inventarán registros atribuidos al laboratorio.

### Caso A — calibración y uso del Level 2

- **B:** preparar parejas, describir errores, estimar componentes en el caso sencillo, ajustar OLS, construir presupuesto y aplicar la función de uso.
- **I:** justificar agrupación y ajuste, incorporar covarianza de parámetros, distinguir promedio y uso futuro, y propagar al cliente.
- **A:** contrastar modelos y presupuestos, examinar dependencia y verificar una función de incertidumbre sobre el intervalo.

### Caso B — comparación de patrones

- **B:** comparación directa con incertidumbres y dependencia definidas en el enunciado.
- **I:** comparación interpolada a partir de una función y su covarianza revisadas.
- **A:** ajuste GGMR del conjunto disponible, contraste de variantes y validación dentro del alcance de la herramienta.

La versión B necesita un conjunto preparado para comparación directa; no se atribuirán mediciones directas a 80 y 420 nmol/mol a una tabla que solo permite interpolar. Las tres versiones se identificarán como ejercicios didácticos cuando no correspondan a la comparación propia.

### Caso C — estabilidad y decisión sobre el patrón

- **B:** carta preparada, criterio aplicable y acción ante señales.
- **I:** construcción de línea base y presupuesto de deriva con historial suficiente.
- **A:** comparación de métodos de vigilancia e intervalo de revisión.

### Caso D — precisión entre analistas y campañas

- **B:** ejemplo sencillo de un factor para separar variación dentro y entre días; comparación de sesgos con signo y magnitud.
- **I:** modelo de dos factores preparado con respuesta y estructura conocidas.
- **A:** análisis completo de analista × campaña con días anidados, cuando estén disponibles los datos con signo; de lo contrario, conjunto didáctico equivalente y limitaciones del archivo histórico explícitas.

**Producto final por nivel:** un informe con datos tratados, método, resultados, incertidumbre pertinente, interpretación y acción. La dificultad aumenta por las decisiones que toma el participante y por los modelos que debe justificar.

## 6. Correcciones que deben reflejarse en los materiales

Estas correcciones se prepararán antes de impartir las actividades; su investigación documental no será una tarea obligatoria del alumno.

1. **Variable y signo:** conservar `e = y − x` en las estimaciones de sesgo y precisión. Usar `|e|` solo cuando el indicador de interés lo requiera.
2. **Referencia variable:** acompañar la comparación de indicaciones brutas y diferencias con la referencia real de cada pareja. Restar la referencia no garantiza independencia ni elimina un sesgo proporcional.
3. **Repetición y promedio:** retirar el divisor √576 como solución general; elegir los componentes y divisores según el resultado de interés y el modelo. Revisar solapamientos entre precisión, regresión y otras fuentes.
4. **R&R:** separar resultados del error absoluto y del error con signo; no trasladar los niveles de interacción significativa del primero al segundo sin recalcular.
5. **Regresión inversa:** reconstruir la expresión de incertidumbre desde el modelo y sus entradas. Corregir una referencia de celda sin revisar la ecuación completa resulta insuficiente.
6. **Presupuesto del patrón:** identificar qué evidencia respalda el SRP55 y qué expresiones pertenecen a ejemplos o presupuestos históricos. El término `0,00425·x` citado por las revisiones puede ilustrar un escenario condicionado; no sustituye un presupuesto propio verificado.
7. **CMC y función final:** reconocer la selección puntual del máximo presente en la plantilla y revisar por separado la función posterior. No prescribir una forma funcional ni inferir su validez de los valores seleccionados.
8. **Caso B:** unificar, tras reproducir el cálculo, los coeficientes de la variante (i). Las revisiones A y D reportan `a = −0,184237121 nmol/mol` y `b = 0,998350748`. Declarar las configuraciones comprobadas y que el script descrito fija `U_xy = 0`.
9. **Cobertura y escala:** utilizar una convención única de cuantiles, distinguir u de U y documentar los valores de sección eficaz usados en cada conjunto.
10. **Criterios de aceptación:** resolver una sola ficha de escenarios y fuentes para M10, M11 y caso C; evitar que un mismo ejercicio cambie de régimen entre módulos.

Las localizaciones y cifras anteriores proceden de las revisiones del proyecto. Esta propuesta no constituye una nueva validación de los libros ni modifica certificados o resultados del laboratorio.

## 7. Evaluación del aprendizaje

Cada módulo se cerrará con una tarea de aplicación y una explicación breve de la decisión. El taller reunirá las competencias en un mismo recorrido. Se evaluará:

- **Datos y respuesta:** emparejamiento, signo, unidades, agrupación y conservación del original.
- **Método:** condiciones de aplicación, unidad de repetición y alcance de la conclusión.
- **Cálculo:** ejecución reproducible y coherencia entre resultado e incertidumbre.
- **Interpretación y acción:** efecto metrológico, criterio aplicable y decisión sustentada.
- **Autonomía del nivel:** ejecutar el caso definido en B, seleccionar y justificar en I, contrastar y validar en A.

En B se incluirá un caso válido y otro con una condición que impida aplicar la plantilla. En I se exigirá elegir entre métodos plausibles. En A se exigirá contrastar al menos un resultado con un ejemplo de referencia o una segunda implementación.

Requerirán corrección y nueva resolución los errores que invalidan el resultado: confundir U y u; invertir el signo de una corrección; mezclar escalas; tratar observaciones dependientes como independientes sin modelo; extrapolar sin sustento; eliminar datos para forzar cumplimiento; aplicar límites de otro escenario; o reportar un resultado didáctico como oficial. La aprobación exigirá resolver las tareas del nivel y subsanar estos errores; una nota global no compensará una conclusión técnicamente inválida.

## 8. Material docente y anexos

Se prepararán fichas breves para elegir respuesta y unidad de repetición, convertir U/k y resolución, distinguir lectura/promedio/uso futuro, aplicar e invertir la recta, elegir regresión, interpretar una carta y decidir ante señales de inaplicabilidad. Estas fichas acompañarán cálculos realizados por el participante.

Los anexos reunirán deducciones de estimadores descriptivos, esperanza y varianza, cuadrados medios esperados, ecuaciones normales, propagación y formulaciones matriciales. El alumno utilizará las ecuaciones en clase y comprobará sus consecuencias con números; las demostraciones no serán requisito de aprobación.

Las fuentes se asignarán por concepto y ejercicio, con versión y secciones concretas. Se priorizarán los documentos ya reunidos sobre estadística en metrología, GUM, calibración lineal, ISO 5725 y fotometría de ozono. Los documentos ambientales se incorporarán donde el problema requiera su ámbito. La bibliografía se depurará para que cada referencia tenga una función docente identificable.

## 9. Condiciones para cerrar el contenido y calcular después las horas

El contenido estará listo para estimar su duración cuando:

1. Cada tema tenga nivel de entrada, prerrequisito, práctica y resultado observable.
2. Cada práctica disponga de datos, herramienta, solución y condiciones de validez suficientes.
3. Los casos con datos ausentes tengan una alternativa docente preparada y rotulada.
4. Las correcciones críticas estén incorporadas en las soluciones que se usarán en clase.
5. El recorrido B → I → A sea acumulativo y cada ampliación tenga una tarea nueva identificable.
6. Los criterios de evaluación correspondan a la autonomía que se promete en cada nivel.

Después se calcularán por separado los tiempos de explicación, práctica, discusión, evaluación y recuperación, y se comprobarán con participantes del perfil de entrada. Si una duración objetivo resulta incompatible con esos aprendizajes, se revisará explícitamente el alcance antes de comprimir las actividades.

Esta propuesta deja definidos el contenido, su progresión y las evidencias de aprendizaje. La reescritura del temario y de su generador, la preparación de los paquetes docentes y la estimación de horas son los pasos siguientes a la revisión de esta propuesta.
