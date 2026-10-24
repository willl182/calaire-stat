# Evaluación comparativa de las auditorías A, B y C

**Fecha:** 23 de octubre de 2026.  
**Documentos evaluados:** [audit_a.md](audit_a.md), [audit_b.md](audit_b.md) y [audit_c.md](audit_c.md).  
**Objeto:** valorar sus ventajas, desventajas, rigor, coherencia interna y calidad de sus planes para revisar el curso de estadística aplicada a la fotometría de ozono con el SRP.

## 1. Dictamen

**A ofrece la mejor estructura para dirigir la revisión del curso; C aporta el diagnóstico más valioso de los datos y de varias fórmulas de Excel; B presenta la síntesis pedagógica más compacta, pero deja más decisiones abiertas y contiene contradicciones en su clasificación por niveles.**

No conviene adoptar íntegramente ninguna de las tres. La opción más sólida es usar la arquitectura y los criterios de cierre de A, incorporar los hallazgos de C que se reproducen en los libros y conservar de B sus recursos operativos y su competencia explícita de reconocer cuándo escalar una revisión.

La salvedad principal afecta a A: **reproducir las cifras del ANOVA del estudio R&R no basta para respaldar su interpretación metrológica**, porque los datos analizados son magnitudes absolutas de errores, al menos en la campaña que se pudo cruzar con el certificado. C identifica este problema y el contraste independiente lo confirma. Esta omisión impide considerar A una auditoría técnica cerrada, aunque su plan global sea el mejor.

La salvedad principal de C es distinta: sus hallazgos de Excel son útiles, pero algunas correcciones convierten un diagnóstico válido en una conclusión demasiado general. Su plan de 30/50/66 horas está bien sumado, aunque no demuestra que las competencias prometidas puedan alcanzarse en esos tiempos. B evita inventar horas, pero por ello tampoco entrega un plan listo para programar.

**Recomendación de adopción:** A como documento rector sujeto a correcciones; C como anexo técnico contrastado; B como lista de mejoras pedagógicas seleccionadas. La integración debe resolver los desacuerdos, no acumular todos los contenidos propuestos.

## 2. Método, alcance y fuerza de la evidencia

### 2.1 Qué se revisó

Se leyeron las tres auditorías completas y se contrastaron sus afirmaciones más decisivas con el temario, los casos, el código y los libros del proyecto. Se realizaron estas comprobaciones:

1. Ejecución de `python3 casos_taller/calc_casos.py`: terminó correctamente y reprodujo las cifras centrales de los casos B y C y el ejemplo de referencia ISO incluido en el script.
2. Inspección de `ggmr_fit`: construcción de la matriz conjunta, bloques cruzados, criterio de parada y resultados devueltos.
3. Lectura de fórmulas y valores almacenados en el XML de los dos libros Excel, sin ejecutar macros ni recalcularlos con Excel.
4. Reconstrucción de diferencias diarias con signo desde `BD_DIAS` y contraste con la campaña correspondiente del libro R&R.
5. Recálculo de las dispersiones de las 48 lecturas del nivel cercano a 130 nmol/mol y de sus diferencias pareadas.
6. Comprobación aritmética de las duraciones propuestas y de los factores de cambio de escala citados.
7. Contraste entre objetivos, tablas de nivel, prácticas, talleres y condiciones de cierre dentro de cada auditoría.

Se evalúan las versiones Markdown presentes en el proyecto. No se presupone que los HTML aporten evidencia técnica adicional ni que sean una revisión independiente.

### 2.2 Qué significa cada juicio

- **Confirmado:** reproducido en datos, fórmulas o código del proyecto.
- **Sustentado en el documento:** el argumento tiene respaldo identificable en la auditoría, pero no se repitió toda su investigación de fuentes.
- **Condicionado:** sería válido bajo supuestos o documentos que deben explicitarse.
- **No establecido:** la evidencia revisada no permite la conclusión formulada.
- **Juicio de diseño:** valoración razonada sobre enseñanza, carga o implementación; no es un resultado experimental.

Esta evaluación no acredita la vigencia de procedimientos, CMC ni autorizaciones institucionales. Tampoco constituye una nueva validación integral de las normas citadas. Cuando se objeta una afirmación normativa, se distingue entre una contradicción local verificable y una exigencia cuya referencia precisa falta en la auditoría.

### 2.3 Criterios de comparación

Se valoran seis dimensiones: exactitud y prudencia técnica; profundidad del contraste de datos; diseño por competencias y niveles; coherencia interna; factibilidad del plan; y trazabilidad de entregables y condiciones de aceptación.

Las tres coinciden en varios hallazgos porque revisan las mismas fuentes. **La coincidencia entre documentos no equivale a tres verificaciones independientes.** La reproducción en el material fuente tiene más peso que el número de auditorías que repiten una afirmación.

## 3. Comparación general

| Dimensión | Auditoría A | Auditoría B | Auditoría C |
|---|---|---|---|
| Aporte principal | Arquitectura por competencias, límites de interpretación y criterios de cierre | Síntesis pedagógica y mapa B/I/A fácil de consultar | Inspección de Excel y conexión entre variable analizada y objetivo metrológico |
| Rigor de las conclusiones | Alto en delimitación del alcance; incompleto en la naturaleza de los datos R&R | Variable: mezcla buenas advertencias con reglas demasiado universales | Alto en varios hallazgos de celdas; menos sólido en algunas generalizaciones y remedios |
| Evidencia reproducible | Declara cálculos y límites; falta un paquete de reproducción del ANOVA | Lista verificaciones sin suficiente detalle de reproducción | Celdas y ejemplos concretos; falta adjuntar extracción y validación completa |
| Nivel básico | Operación con procedimientos aprobados y límites explícitos | Incluye inferencia, ANOVA, presupuestos y comparaciones | Incluye OLS, prueba t y presupuesto tabular, excluye ANOVA |
| Coherencia de niveles | La más consistente | Varias incompatibilidades entre mapa, listas y talleres | Mejor separación que B, con excepciones técnicas y sobrecarga |
| Horas | 48 h básico; 80 h núcleo intermedio; extensión de 32 h | Sin propuesta de horas | 30/50/66 h acumuladas |
| Calidad del plan | Alta como marco de implementación, pendiente de piloto y recursos | Media como orientación; baja como programación ejecutable | Alta en detalle de contenidos; media-baja en factibilidad de las promesas |
| Riesgo principal | Dar por interpretado un ANOVA de datos transformados | Confundir uso de plantilla con competencia básica suficiente | Prometer demasiada autonomía y aplicar correcciones no completamente justificadas |
| Uso recomendado | Base de la revisión | Complemento pedagógico | Anexo de hallazgos técnicos que deben depurarse |

No se asigna una nota numérica global: dar decimales sugeriría una precisión que no existe y podría ocultar un defecto crítico detrás de un buen promedio. A lidera el plan general; C lidera el diagnóstico específico de los libros; B lidera la concisión.

## 4. Evaluación detallada de A

### 4.1 Ventajas

**Separa tareas y autonomía, en lugar de clasificar solamente nombres de métodos.** La sección 5 distingue aplicar una función aprobada, elegir una regresión y validar un ajuste con covarianzas generales. Esta separación es más útil que afirmar que «regresión» pertenece por entero a un nivel. Permite redactar objetivos observables y evaluar lo que realmente hace el participante.

**Define un básico con identidad propia.** Su básico completa un flujo operativo: datos, correcciones, uso de incertidumbre, certificado y control. No necesita prometer selección de modelos o construcción independiente de presupuestos para resultar útil. Sus exclusiones explícitas reducen la ambigüedad de la oferta docente.

**Diferencia reproducción numérica, validez del modelo y aplicabilidad institucional.** H03, H09, H10 y H16 evitan pasar de un ejemplo EPA o BIPM a una decisión de CALAIRE sin justificar el procedimiento, la población y el alcance. También distingue ejecutar una herramienta preparada de validar su método general.

**Conecta conceptos que suelen enseñarse aislados.** La secuencia datos → modelo → corrección → incertidumbre → decisión → uso futuro es uno de sus mejores aportes. Las secciones 4.2–4.7 incorporan el resultado futuro, el doble conteo, la diferencia entre compatibilidad y conformidad y las acciones ante una alarma.

**Ofrece condiciones verificables para cerrar la revisión.** Incluye productos por práctica, paquetes de casos, rúbricas, errores críticos y una lista de comprobaciones objetivas. Es la única que desarrolla de manera suficiente cómo decidir que la nueva versión está preparada.

**Las horas se presentan como hipótesis que requieren piloto.** Explicita prerrequisitos, preparación de datos y herramientas, actividades incluidas y exclusiones. La extensión avanzada no promete enseñar desde cero programación y todos los modelos posibles.

### 4.2 Desventajas y omisiones

**La omisión del valor absoluto en R&R es material.** H11 y el registro final confirman las F del modelo aplicado a B6:C23, pero no identifican que la respuesta del libro representa magnitudes absolutas. Un modelo puede reproducir exactamente las cifras de una transformación y responder a una pregunta distinta de la que se pretende enseñar.

Esto afecta expresiones como «dispersión de errores medios diarios» y cualquier interpretación como precisión de errores con signo. La corrección necesaria es rotular la respuesta realmente disponible, limitar las conclusiones y recuperar las diferencias originales antes de usar ese análisis como referencia del caso D. Las cautelas sobre multiplicidad y pocos analistas son buenas, pero no resuelven esta cuestión previa.

**La inspección del certificado no alcanza la profundidad de C.** A reconoce que no reconstruyó todas sus fórmulas, lo cual es honesto. Sin embargo, habría sido más útil identificar expresamente `BD_DIAS!E8/E10` y el paso de `ABS()` al término usado como repetibilidad. Son puntos de alto impacto docente y accesibles en el mismo material inspeccionado.

**La duración es más defendible que la de C, pero no está validada.** Las 48/80/+32 h son una estimación de diseño. Falta evidencia de desempeño de participantes, tiempo real de resolución, relación docente/grupo y recursos de apoyo. Aumentar horas ayuda, pero no demuestra por sí solo suficiencia.

**La articulación básico–intermedio necesita una política de reconocimiento.** A aclara que no se suman automáticamente 48+80+32 h y que pueden acreditarse competencias. No define cuántas horas de una ruta puente necesitaría quien termina el básico, qué unidades puede reconocer ni cómo evitar repeticiones de M0–M3. El itinerario técnico es de 112 h para quien ya reúne los requisitos de entrada; quien deba cursar previamente el básico podría acumular 160 h si no se reconocen aprendizajes.

**El plan todavía no es un cronograma de producción.** Falta asignar responsables, estimar esfuerzo de preparar casos y herramientas, ordenar dependencias y fijar quién aprueba cada entregable. Sus condiciones de cierre permiten construir ese cronograma, pero no lo sustituyen.

**Hay detalles editoriales de priorización.** H16 figura como P1 y H17 como P2, pero el primer paso de implementación agrupa H03–H16. No queda tan visible cuándo se cierran H01–H02 ni qué contenidos P2 se aceptan provisionalmente. Conviene convertir los hallazgos en un registro único de acciones.

### 4.3 Calidad y coherencia del plan

**Valoración: alta, con una corrección técnica previa indispensable.** Objetivos, exclusiones y talleres concuerdan mejor que en B y C. Las rúbricas refuerzan las fronteras de competencia y el avanzado se presenta como una extensión acotada.

A puede adoptarse como base si se integra el diagnóstico de los libros, se resuelve la respuesta del caso D y se define la entrada al intermedio. Su mayor virtud es que permite reducir alcance sin ocultarlo; su mayor debilidad es que una parte de la evidencia reproducida se interpreta sin revisar suficientemente qué variable representa.

## 5. Evaluación detallada de B

### 5.1 Ventajas

**Es la más fácil de consultar y transformar en una lista de revisión.** Las tablas de errores, vacíos y contenidos por nivel reducen el esfuerzo de localizar una corrección. Es útil para una reunión de diseño o para revisar módulos concretos.

**Introduce una competencia operativa esencial: reconocer cuándo escalar.** Las señales de datos correlacionados, pocos días, cercanía al límite, deriva y cambio de escala hacen que el básico no se limite a ejecutar fórmulas. Este aporte merece conservarse y evaluarse mediante situaciones prácticas.

**Aporta recursos concretos de hoja de cálculo.** La conversión U/k, la distinción s frente a s/√n, las sensibilidades numéricas de Kragten, los gráficos de secuencia y los cierres por módulo responden a necesidades reales. No todos requieren un módulo adicional; muchos pueden integrarse en una práctica existente.

**No presenta una duración sin haber fijado el alcance.** Posponer las horas es una limitación operativa, pero también una muestra de prudencia. Evita el problema de C de presentar el ahorro horario como si demostrara factibilidad.

**Señala problemas de secuencia y notación útiles.** Reubicar pruebas de atípicos, declarar la convención error/corrección y aclarar el uso de distintos divisores mejora la consistencia del curso sin necesidad de ampliar mucho el programa.

### 5.2 Desventajas y contradicciones internas

**El básico queda sobrecargado respecto a su perfil operativo.** Incluye IC, prueba t, ANOVA de un factor, componentes de precisión, Kragten, comparación directa y banda de guarda. Puede diseñarse un curso introductorio aplicado con algunas de esas tareas, pero B no demuestra qué prerrequisitos y horas permitirían practicarlas todas con criterio.

La plantilla es un apoyo, no evidencia suficiente de que se comprendan la unidad experimental, los supuestos o los límites de aplicación. La competencia de escalar ayuda, pero debe definirse qué situaciones puede resolver realmente el participante antes de escalar.

**El mapa contradice la lista de temas que entran en intermedio.** M6 básico exige `s_r` y precisión intermedia mediante ANOVA, mientras la lista posterior reserva a I las componentes de varianza. M5 básico incluye anidamiento, aunque la misma lista desplaza modelos anidados/cruzados a I. Hace falta distinguir reconocimiento de estructura, ejecución guiada y estimación autónoma.

**La frontera de GLS y covarianza entre puntos es inestable.** M9 intermedio pide construir U_x y ejecutar GLS; después se declaran exclusivos de A «GLS/GGMR, matrices de covarianza y covarianza común entre puntos». Podría resolverse separando ejecución con configuración fija de formulación y validación, pero B no lo establece con la claridad de A.

**Contradice el requisito que adopta sobre derivaciones.** En la sección 6 elimina derivar sensibilidades como tarea general, pero autoriza en I/A «derivar los de esta ecuación» por considerarlo aplicación. El propio encargo recogido por B excluye demostraciones matemáticas de clase. Para cumplirlo sin ambigüedad, conviene suministrar sensibilidades y comprobarlas numéricamente.

**La regla «la unidad de réplica es el día, n=6» es demasiado universal.** Puede ser apropiada para estimar determinada variación entre días, pero no define por sí sola toda inferencia posible. Una lectura, un ciclo y un promedio diario responden a preguntas distintas. Además, el día no garantiza independencia frente a una deriva o contribución común.

Usar medias diarias tampoco arregla automáticamente una prueba de falta de ajuste si los valores de referencia cambian entre días. Hay que definir el modelo de respuesta y las condiciones de réplica, como advierte A en H13.

**El taller A básico contiene una incompatibilidad de datos.** Propone «un nivel y la recta de un día» junto con ANOVA de días. Un solo nivel no permite una recta multipunto y un solo día no permite estimar variación entre días. Serían tres subconjuntos relacionados, que deben entregarse y nombrarse por separado.

**Supone disponible una comparación propia que el paquete no contiene.** B recomienda usarla incluso en básico. La idea es buena si existen datos utilizables y autorización para su uso docente, pero no es una práctica ejecutable con los archivos presentes. A reconoce expresamente este faltante.

**La declaración «las cifras que no se mencionan cuadran» excede el registro de verificación.** No incluye inventario completo, procedimiento o resultados para sostener una validación general. La coincidencia numérica de los CME y las F no detecta el problema del valor absoluto. Conviene sustituir esa frase por una lista cerrada de comprobaciones y límites.

### 5.3 Calidad y coherencia del plan

**Valoración: media como propuesta pedagógica y baja como plan listo para ejecutar.** El mapa es útil, pero necesita reconciliar sus propias fronteras de nivel, fijar horas, preparar datos y convertir recomendaciones en entregables con aceptación.

También conviene suavizar «no hay temas solo para mostrar». Un operador puede necesitar reconocer un informe de comparación o una alerta especializada sin aprender a producir su modelo. La lectura documental breve puede tener un resultado operativo evaluable; excluirla por principio empobrecería la comprensión de la trazabilidad.

## 6. Evaluación detallada de C

### 6.1 Ventajas

**Identifica el hallazgo de datos más importante de las tres auditorías.** La pérdida del signo en el estudio R&R cambia el objeto del análisis. C no se limita a señalar una etiqueta: proporciona ejemplos contrastables entre una campaña y el certificado. Esta observación obliga a revisar la interpretación de los resultados que A y B dan por reproducidos.

**Comprueba la heterogeneidad de las concentraciones entre días.** El ejemplo cercano a 130 nmol/mol muestra que una dispersión de indicaciones brutas mezcla variación del generador y comportamiento relativo del equipo. Es un argumento concreto para definir la respuesta antes de aplicar normalidad, IC o ANOVA.

**Hace visible una cadena de fórmulas problemática.** Localiza la agrupación de diferencias absolutas, `STDEV.P`, la división por √576 y la transferencia del resultado al presupuesto. Este seguimiento entre hojas es más informativo que una recomendación general de «revisar la repetibilidad».

**Conecta el uso del certificado con la incertidumbre de la inversión.** Su crítica a `Uo` obliga a mirar qué magnitud entra en el término de distancia y cómo se combinan lectura nueva, parámetros y covarianza. También hace visible que la incertidumbre del patrón no se justifica por copiar una expresión de otro SRP.

**Presenta una propuesta de módulos y horas fácil de convertir en edición.** El detalle de contenidos por nivel y la identificación de `temario_build.py` como punto de actualización son prácticos. La secuencia de producir Markdown y HTML desde el generador ayuda a evitar divergencias.

### 6.2 Desventajas y conclusiones que deben limitarse

**Confunde en un punto ausencia de máximo puntual con tratamiento posterior de la curva.** C afirma que la plantilla no aplica `max(U, CMC)` y lo contrapone al polinomio y al desplazamiento. El XML muestra que `Uexp!Q8` sí selecciona el mayor entre N8 y O8 mediante P8. A describe correctamente esa etapa.

C sí detecta una cuestión adicional: después existe una construcción de función continua con `Uexp!U22` y `EcuOffset`. Deben auditarse ambas etapas. La selección puntual no valida la curva final y la curva posterior no elimina la selección puntual existente. La crítica debe reescribirse con esa secuencia.

**El remedio funcional de U(x) se presenta como demasiado automático.** Una forma `√(U₀²+(U₁x)²)` puede tener sentido para ciertas componentes. No se demuestra que sea siempre la forma adecuada ni que reemplazar el cúbico por ella asegure cobertura, compatibilidad con la CMC o ausencia de subestimación. Falta justificar el modelo y comprobar la función en todo el intervalo. C tampoco aporta una cláusula precisa que obligue a una de esas dos formas concretas.

**La crítica a `Upatron` necesita evidencia propia antes de cuantificar una omisión.** La fórmula de `Uexp!J8` reproduce `√(0,28²+(0,00292·D8)²)`. Eso está confirmado. Que represente correctamente el SRP55 no queda establecido por la fórmula; tampoco queda establecida una corrección consistente en sumar sin más el grado de equivalencia y una deriva. Debe reconstruirse el presupuesto propio, con escala, trazabilidad y covarianzas, evitando doble conteo.

**La magnitud de la subestimación no está cerrada.** El valor de 0,0105 nmol/mol y su origen son verificables. Declarar una subestimación «en más de un orden de magnitud» exige definir la contribución correcta y el resultado al que se aplica. Compararlo directamente con la dispersión de una lectura o de diferencias agrupadas no equivale a comparar dos incertidumbres del mismo mensurando. El defecto metodológico es claro; el factor exacto requiere otro cálculo.

**El problema de las lecturas brutas se formula con absolutos innecesarios.** Las diferencias con signo son una elección razonable para estudiar error relativo a la referencia bajo un modelo definido. No son la única respuesta posible: también puede modelarse la indicación en función de la referencia, con efectos diarios u otras estructuras. Tampoco el cero garantiza independencia o estabilidad. Hay que evitar sustituir «analizar y» por una nueva regla universal «analizar siempre y−x».

**La prueba t de ocho lecturas no resuelve la dependencia.** E-07 acota correctamente un único nivel, pero la práctica básica vuelve a tratar las ocho lecturas consecutivas como base de IC y t sin exigir evidencia suficiente de independencia. El problema no desaparece por dejar la autocorrelación para avanzado: el básico debe recibir datos y procedimiento para los que la inferencia sea válida, o limitarse a resultados ya revisados.

**Algunas fórmulas simplificadas quedan sin condiciones.** El tamaño efectivo `n(1−r₁)/(1+r₁)` no es una corrección universal para series cortas y cualquier patrón de dependencia. Asimismo, `P=1−(1−α)^n` requiere condiciones que no se explicitan al presentarlo como inflación de riesgo por comparaciones múltiples. A es más cuidadosa en este punto.

**La reconstrucción histórica del cambio de escala es demasiado concluyente.** C atribuye 1,25 % exclusivamente a truncar 1,1476 a 1,147 y llama 1,29 % al «cambio físico real». Los cocientes impresos no son idénticos: 1,147/1,1329 produce 1,24459 %; 308,32/304,39 produce 1,29111 %; 1,1476/1,1329 produce 1,29755 %. La explicación histórica debe documentar convenciones, conversión y precisión de cada par. A adopta una posición más defendible: identificar el par usado y calcular con él, fijando además el signo y el denominador.

**El plan promete demasiadas competencias nuevas con incrementos mínimos.** En M7 se pasa de OLS operativo a incertidumbre de parámetros, falta de ajuste, WLS y GDR con una hora adicional; avanzado añade formulación matricial manteniendo las mismas cinco horas. M10 y M11 incorporan riesgo probabilístico y cartas con memoria sin aumentar su duración frente al intermedio. M13 concentra varios métodos en cinco horas.

No es imposible impartir un panorama o reproducir ejemplos preparados en esos tiempos. Lo no demostrado es la promesa de implementar, validar y decidir con autonomía, además de resolver los casos completos. La auditoría no distingue con suficiente precisión exposición, ejecución guiada y dominio evaluado.

### 6.3 Calidad y coherencia del plan

**Valoración: alta como inventario de revisión técnica, media como especificación docente y media-baja en factibilidad horaria.** Sus sumas son correctas: 30, 50 y 66 h; los incrementos son 20 y 16 h. El problema está en el alcance asociado a esas horas.

También faltan un piloto, rúbricas suficientes, criterios de aprobación y preparación de herramientas para covarianzas cruzadas: el script actual fija `U_xy=0`, aunque el plan avanzado pide analizar `U_xy≠0`. Ese cambio requiere desarrollo y validación previos, no solamente una consigna docente.

La hoja de ruta final señala archivos y acciones, pero no organiza todos sus propios hallazgos en dependencias, responsables y condiciones de aceptación. C está más cerca de un temario alternativo que de un plan completo de aseguramiento de la revisión.

## 7. Resultados del contraste independiente

### 7.1 Caso B: error documental confirmado en las tres

El script produce para la variante (i):

- `a = −0,184237121`.
- `b = 0,998350748`.
- `χ²_obs = 6,318259554`, con 10 grados de libertad.

El apartado 5 del caso conserva otro par. Las tres identifican correctamente el desacuerdo. La corrección es documental; no hace falta modificar el algoritmo para resolver esa discrepancia.

Para la variante (ii), se reproduce `χ²_obs = 0,765027308` y una probabilidad acumulada cercana a `4,97×10⁻⁵`. Ese resultado merece diagnóstico del presupuesto y sus supuestos; por sí solo no prueba una causa concreta.

El ejemplo ISO incorporado coincide dentro de `atol=2×10⁻⁴`, tal como declara el programa. Es una comprobación útil para ese ejemplo. No acredita todas las configuraciones ni los bloques cruzados, que la función construye como cero. La función tampoco devuelve un estado explícito que distinga convergencia de agotamiento de iteraciones. A delimita mejor este alcance que las otras dos.

### 7.2 Estudio R&R: hallazgo de C confirmado y efecto sobre A/B

En `BASE DE DATOS!B70` aparece `VALORES ABSOLUTOS`. El cruce de la primera jornada de la campaña disponible ofrece, entre otros, estos resultados:

| Nivel nominal | Diferencia media con signo reconstruida desde el certificado | Valor del libro R&R, B18 |
|---|---:|---:|
| 45 nmol/mol | +0,101734125 | +0,101734125 |
| 90 nmol/mol | −0,252784125 | +0,252784125 |
| 135 nmol/mol | −0,396401625 | +0,396401625 |
| 315 nmol/mol | −0,446215500 | +0,446215500 |
| 360 nmol/mol | +0,041436000 | +0,041436000 |
| 455 nmol/mol | −0,051132250 | +0,051132250 |

El mismo patrón se reproduce en los diez niveles de esa jornada. Esto confirma pérdida de signo en la campaña cruzada; no reconstruye automáticamente los errores originales de todas las otras campañas.

**Consecuencia:** se puede analizar la magnitud del error si ese es el objetivo y se adopta un modelo adecuado. Lo que no debe hacerse es interpretar sin justificación sus componentes como las de los errores con signo o usar una ausencia de efecto para descartar sesgos opuestos entre analistas.

También se confirman `D137 = AVERAGE(#REF!)`, `D138 = AVERAGE(D118:D123)` y los rangos B6:B17/C6:C17 en `455ppb!N7/N8`, frente a los 18 datos disponibles hasta la fila 23. C da mayor visibilidad a estos defectos; A ya reconoce el rango incompleto.

### 7.3 Nivel cercano a 130 nmol/mol: diagnóstico de C reproducido

Desde `BD_DIAS`, las medias de referencia por día son aproximadamente 127,8464; 127,2152; 129,6152; 128,6263; 131,2302 y 131,2244 nmol/mol.

El recálculo da:

- Desviación muestral de las 48 indicaciones: **1,60225 nmol/mol**.
- Desviación muestral de las 48 diferencias pareadas con signo: **0,40157 nmol/mol**.
- Desviación intradía combinada de las indicaciones: **0,33576 nmol/mol**.

Las cifras respaldan el ejemplo de C y la necesidad de separar preguntas estadísticas. No demuestran independencia de las diferencias ni convierten su desviación agrupada en la incertidumbre del resultado futuro.

### 7.4 Repetibilidad del certificado: cadena de fórmulas confirmada

`BD_DIAS!E8` usa `STDEV.P` sobre F15:F110 y los otros cinco rangos diarios de diferencias absolutas. El valor almacenado es **0,252451532 nmol/mol**. `E10` lo divide por √576 y obtiene **0,010518814 nmol/mol**; `Uexp!I8` enlaza a ese valor.

La crítica más fuerte es la combinación de niveles y respuestas transformadas sin un modelo que justifique ese estimador para el resultado reportado. Elegir `STDEV.S` en lugar de `STDEV.P` manteniendo el resto no solucionaría el problema.

### 7.5 Regresión, patrón y CMC: separar fórmula de interpretación

| Punto | Evidencia observada | Conclusión admisible |
|---|---|---|
| `Uexp!G8` | `E8−$D$20` | C localiza correctamente un término que debe revisarse contra la ecuación de predicción inversa |
| `Uexp!H8` | Usa G8, residual, pendiente, n=12 y p=8 | No basta cambiar una letra: hay que reconstruir el modelo y sus posibles términos compartidos |
| `Uexp!J8` | `√(J6²+(0,00292·D8)²)`, J6=0,28 | Reproduce una expresión; no acredita por sí sola el presupuesto propio vigente del SRP55 |
| `Uexp!Q8` | Selecciona N8 u O8 mediante P8 | Sí hay selección puntual del máximo; la objeción literal de C es incorrecta |
| `Uexp!U22` | `Q6+T10+S6` | Hay una etapa posterior de modificación de la función que exige validación propia |

En la fila 8, N8≈0,58182 y O8≈0,61991; Q8 toma O8. Es un contraejemplo concreto a la afirmación de que no existe el máximo puntual. Sigue pendiente comprobar la curva final y su alcance; observar esa selección no valida todo el certificado.

## 8. Desacuerdos que deben resolverse antes de combinar los planes

### 8.1 Qué significa «básico»

A propone ejecutar procedimientos; B incorpora varios análisis y estimaciones; C se sitúa entre ambos, pero añade t, OLS y presupuesto en 30 h. Son ofertas de competencia distintas. No puede compararse su duración como si enseñaran lo mismo.

La decisión debe partir del trabajo esperado del egresado. Para un operador que aplica procedimientos aprobados, la frontera de A es la más clara. Si se quiere que construya presupuestos o seleccione pruebas, debe declararse esa autonomía, exigir prerrequisitos y asignar tiempo verificable.

### 8.2 Acumulación de horas y continuidad

| Ruta | Lectura correcta | Pendiente |
|---|---|---|
| A | Básico 48 h; intermedio 80 h con requisitos de entrada; avanzado como extensión de 32 h | Definir reconocimiento desde básico y posibles puentes |
| B | Perfiles acumulativos en contenidos, sin duración | Estimar cursos completos e incrementos, sin confundirlos |
| C | Cursos completos de 30/50/66 h y progresión nominal +20/+16 | Demostrar que los incrementos desarrollan las competencias nuevas |

No debe aprobarse una cifra final negociando un promedio entre A y C. Primero se fija la competencia; luego se estima y prueba la carga.

### 8.3 Repetibilidad e independencia

A ofrece el criterio más defendible: declarar lectura, ciclo, corrida, día y resultado. B universaliza el día como réplica; C permite ocho lecturas como base inferencial sin resolver suficientemente la dependencia.

La solución común debe partir de la pregunta, no del número de filas: variación de corto plazo, precisión entre días, incertidumbre del promedio de calibración y uso futuro requieren tratamientos distintos.

### 8.4 Comparación clave y CMC

B presupone datos propios; C mantiene algunas formulaciones institucionales concluyentes; A distingue ejemplo didáctico, informe oficial y evidencia del laboratorio. Hasta disponer del paquete propio, debe usarse una adaptación rotulada y limitar las conclusiones a su modelo.

La misma cautela aplica a `E_n`. Incluirlo es útil; enseñar la cuadratura de dos U como fórmula universal sin revisar dependencia o usarlo como criterio general de conformidad introduciría un nuevo atajo. Debe ligarse a una comparación y un presupuesto definidos.

### 8.5 Aplicabilidad EPA y otras fuentes

Las tres reconocen el conflicto entre diseños y límites. A lo resuelve mejor porque exige evidencia de adopción por CALAIRE. La similitud entre seis días de datos y un esquema 6×6 permite un contraste didáctico, pero no sustituye la revisión del diseño completo y del procedimiento aplicable.

La tabla de criterios debe identificar documento, edición, instrumento, etapa, diseño, estadístico, divisor, unidad y autoridad de adopción. No basta elegir el conjunto de límites que el ejemplo supera.

### 8.6 Explicación conceptual y demostración matemática

Las tres apoyan retirar deducciones obligatorias. B conserva una excepción que contradice ese criterio. C y B llaman demostración a algunas explicaciones que podrían resolverse en minutos con un ejemplo.

Debe mantenerse una explicación breve de por qué una decisión es válida, conectada con el trabajo. Se pueden suministrar ecuaciones y comprobar sensibilidades o resultados numéricamente. No hace falta eliminar toda justificación para evitar demostraciones algebraicas.

## 9. Plan consolidado recomendado

Este plan reúne los aportes compatibles y ordena lo que falta. **No propone añadir todos los temas de las tres auditorías ni modificar los libros originales como parte de esta evaluación.** Los responsables son funciones sugeridas que deben asignarse a personas concretas.

### Fase 1. Fijar datos, variable de respuesta y alcance documental

**Responsables sugeridos:** custodio de datos y responsable técnico de metrología.

- Conservar originales y registrar versiones de auditorías, generador, casos y libros.
- Preparar extracción documentada del certificado con referencia e indicación emparejadas, signos, fechas, nivel, analista y campaña.
- Recuperar los errores con signo del R&R cuando sea posible; identificar las campañas que no pueden reconstruirse.
- Separar estudio de magnitud del error y estudio de precisión de errores con signo.
- Obtener procedimiento aplicable, escala de σ, certificado/presupuesto propio y alcance de CMC necesario para los ejercicios.

**Entregables:** diccionario de datos, CSV trazables a celdas y matriz de documentos aplicables.  
**Aceptación:** conteos y emparejamientos comprobados, transformaciones registradas, imposibilidades explícitas. Ningún resultado se presenta como oficial o vigente sin la evidencia correspondiente.

### Fase 2. Corregir y verificar los cálculos docentes

**Responsables sugeridos:** analista de cálculo y revisor técnico.

- Unificar el resultado del apartado 5 del caso B con el cálculo reproducido.
- Reconstruir los estimadores de precisión sobre la respuesta elegida y el diseño disponible.
- Revisar inversión de calibración, contribución del patrón, covarianzas, cobertura y doble conteo.
- Documentar selección puntual de U/CMC y construcción posterior de la función; verificar ambas etapas.
- Mantener GGMR dentro del alcance validado o preparar y contrastar la extensión necesaria antes de enseñar `U_xy≠0`.

**Entregables:** soluciones A–D, presupuestos comentados y registro de verificaciones.  
**Aceptación:** cada cifra tiene entradas, procedimiento, unidad, tolerancia numérica y límite de interpretación. Un segundo revisor puede reproducir los resultados. Las fórmulas heredadas no se consideran correctas solo porque el libro conserva un valor en caché.

### Fase 3. Congelar competencias y rutas

**Responsables sugeridos:** coordinación docente y responsable técnico.

- Adoptar como base la distinción de A entre operación, análisis habitual y validación avanzada.
- Incorporar de B la competencia de escalar y sus conversiones operativas U/k y s frente a s/√n.
- Precisar si se pretende que el básico solo aplique una función entregada o también ajuste OLS; si se incorpora esta última tarea, acotar datos, diagnóstico y autonomía.
- Definir para cada tarea si se reconoce, se ejecuta con configuración fija o se selecciona y justifica.
- Establecer requisitos de entrada y reconocimiento entre rutas; evitar asociar aprobación docente con autorización automática para firmar certificados.

**Entregable:** matriz competencia → actividad → herramienta → evidencia → nivel.  
**Aceptación:** ninguna tabla o taller exige una tarea excluida de su nivel. No hay derivaciones obligatorias. La descripción comercial coincide con la evaluación.

### Fase 4. Construir la versión docente y programar las horas

**Responsables sugeridos:** autor del material, instructor y mantenedor del generador.

- Preparar paquetes de casos por nivel con datos suficientes para cada pregunta.
- Distinguir material original defectuoso, copia de trabajo y solución de referencia revisada.
- Incorporar cambios en `temario_build.py` y regenerar Markdown/HTML mediante el flujo del proyecto.
- Incluir fichas de métodos, acciones ante alarmas, ejemplos con signos mezclados y alcance de los límites externos.
- Tomar 48/80/+32 h de A como estimación inicial condicionada, no como compromiso validado. Si se exige 30/50/66 h, reducir objetivos explícitamente antes del piloto.

**Entregables:** temario coherente, plantillas, soluciones, anexos y programación de sesiones.  
**Aceptación:** las horas incluyen práctica, evaluación y devolución; las actividades no dependen de datos ausentes ni de reconstruir libros durante la clase.

### Fase 5. Pilotar y aprobar

**Responsables sugeridos:** instructor piloto y revisor distinto de quien preparó los cálculos.

- Pilotar M6–M8 y el caso A, además de una actividad crítica de cada ruta.
- Registrar tiempo de preparación, resolución, errores, apoyos necesarios y recuperación.
- Aplicar rúbricas adaptadas de A, con la competencia de escalamiento de B.
- Ajustar horas o alcance según resultados, manteniendo los límites de autonomía declarados.

**Entregables:** informe del piloto, acciones cerradas y versión congelada.  
**Aceptación:** ejecución completa con participantes que cumplan los requisitos, resultados reproducibles y corrección de errores críticos. El tiempo del piloto y la preparación de material deben presupuestarse aparte de las horas impartidas.

## 10. Qué conservar, corregir y posponer

| Procedencia | Conservar | Corregir antes de adoptar | Posponer o condicionar |
|---|---|---|---|
| A | Fronteras de autonomía, cadena de aplicación, rúbricas y condiciones de cierre | Interpretación del R&R; diagnóstico de fórmulas del certificado; transición básico–intermedio | Duraciones definitivas hasta el piloto; aplicaciones institucionales sin evidencia |
| B | Síntesis, escalamiento, U/k, s frente a s/√n, recursos de hoja de cálculo y cierres por módulo | ANOVA/componentes en básico; GLS por nivel; derivaciones permitidas; regla universal n=6; taller A | Comparación propia hasta disponer de datos; nuevos temas sin prioridad ni tiempo |
| C | Pérdida de signo, heterogeneidad entre días, rastreo de E8/E10 e inspección de Uo | Negación del máximo puntual; factor de subestimación no cerrado; cambio de escala demasiado categórico; generalizaciones sobre respuesta e independencia | Sustitución de U(x), presupuesto del SRP55, riesgo avanzado y covarianzas cruzadas hasta justificar y validar |

## 11. Condiciones para considerar completa la revisión del curso

1. La variable analizada coincide con la pregunta y sus transformaciones están declaradas; el valor absoluto no sustituye silenciosamente al error con signo.
2. Las soluciones reproducen los datos y distinguen incertidumbre de una lectura, de un promedio y de un resultado futuro.
3. Las fórmulas del certificado se revisan como una cadena, incluida la construcción de la función final de incertidumbre.
4. Cada criterio numérico tiene fuente, diseño y alcance; la adopción por CALAIRE se documenta o la actividad se rotula como ejemplo externo.
5. El caso B deja de presentar dos pares de coeficientes para la misma variante y el software declara su alcance validado.
6. Los paquetes A y D permiten trabajar sin reconstrucción improvisada de Excel; el caso propio de comparación no se presupone disponible.
7. Los niveles tienen objetivos, prácticas y evaluación compatibles. El uso de una plantilla no amplía por sí solo la autonomía reconocida.
8. Las horas se verifican con actividades reales, incluyendo revisión y corrección, y las rutas aclaran prerrequisitos y reconocimiento.
9. Los documentos se actualizan desde el generador y no se contradicen con sus casos o soluciones.
10. Las cuestiones no resueltas quedan identificadas como pendientes y limitan las conclusiones correspondientes.

## 12. Conclusión de la evaluación

**A es la mejor base para gobernar el cambio, pero necesita el hallazgo de C sobre los datos R&R y una revisión más profunda del certificado. C es indispensable para corregir el material fuente, pero debe depurar sus conclusiones y reducir o justificar las promesas de su plan. B aporta claridad y buenos recursos de enseñanza, aunque requiere resolver contradicciones antes de funcionar como arquitectura del curso.**

La calidad final depende de resolver primero los datos y el modelo, después fijar competencias y finalmente ajustar las horas. Adoptar A sin C conservaría una interpretación problemática del estudio R&R; adoptar C sin A conservaría riesgos de sobrecarga y de conclusiones excesivas; adoptar B sin las otras dos dejaría insuficientemente cerrado el alcance técnico y operativo de la revisión.
