# Evaluación comparativa de las tres auditorías del curso

**Fecha:** 23 de octubre de 2026.  
**Documentos evaluados:** [audit_a.md](audit_a.md), [audit_b.md](audit_b.md) y [audit_c.md](audit_c.md).  
**Objeto:** valorar sus ventajas, desventajas, rigor, coherencia interna y calidad de los planes propuestos, para decidir qué adoptar al revisar el curso.

## 1. Dictamen

**A es la mejor base para dirigir la revisión del curso; B aporta el mejor complemento para definir perfiles y competencias operativas; C aporta la inspección más valiosa de los libros Excel. Ninguna debe adoptarse íntegramente.**

La preferencia por A responde a su mejor separación entre evidencia, interpretación, aplicabilidad y competencia del alumno. Además, convierte el diagnóstico en una propuesta con prerrequisitos, horas, talleres, evaluación y condiciones de cierre. Su principal debilidad técnica es importante: reproduce e interpreta el ANOVA del R&R sin advertir que la respuesta analizada es el valor absoluto del error. Esa omisión afecta la interpretación metrológica del estudio y debe corregirse antes de usar A como documento rector.

B es más breve y fácil de convertir en una lista de trabajo docente. Su definición de la capacidad de reconocer un caso que exige revisión especializada es especialmente útil. Sin embargo, mantiene un básico muy exigente, contiene contradicciones en su reparto de contenidos y sustituye algunos problemas por reglas demasiado generales. No proponer horas es una decisión prudente mientras no se fijen competencias, pero deja incompleto el plan de ejecución.

C hace la aportación técnica más concreta al examinar los datos y las fórmulas de los Excel. Confirmé varias de sus cifras y localizaciones. Su propuesta curricular, en cambio, promete demasiado en 30/50/66 horas, y algunas correcciones introducen errores o afirmaciones no justificadas: el factor de cobertura de Student, la explicación del cambio de escala, la negación del máximo puntual de incertidumbres y la elección de una forma funcional de CMC, entre otras.

**Recomendación:** conservar la arquitectura y las condiciones de cierre de A, incorporar la competencia de escalamiento y los materiales operativos de B, e incorporar los hallazgos comprobados de Excel de C después de corregir sus interpretaciones. La síntesis debe sustituir afirmaciones incompatibles; concatenar los tres documentos conservaría sus contradicciones.

## 2. Criterios y alcance de esta evaluación

### 2.1 Qué se está juzgando

Se distinguen tres productos que no tienen la misma calidad en cada documento:

1. **Diagnóstico:** identificar un problema real, localizarlo y explicar su efecto.
2. **Solución:** proponer un cambio que resuelva el problema sin introducir otro.
3. **Plan:** establecer una secuencia ejecutable, con recursos, dependencias y evidencia de terminación.

Un diagnóstico correcto no valida automáticamente la solución. Una tabla de horas que suma bien tampoco demuestra que la formación quepa en ese tiempo.

Los criterios de comparación son: exactitud técnica; trazabilidad de las afirmaciones; control del alcance normativo e institucional; coherencia entre objetivos, ejercicios y niveles; realismo de la carga; preparación de materiales; evaluación del aprendizaje; y facilidad para implementar y mantener la revisión.

Las auditorías reconstruyen como requisitos un curso adaptable a básico/intermedio/avanzado, práctico y sin demostraciones obligatorias. Se evalúa su consistencia con esos requisitos declarados. Esta revisión no dispone del encargo original completo que produjo las auditorías: no presupone que el usuario hubiera autorizado una duración determinada ni que hubiera exigido tres cursos equivalentes o un itinerario acumulativo específico.

### 2.2 Trabajo de contraste realizado

- Lectura completa de las tres auditorías y contraste dirigido con el temario, el generador y los casos B/C.
- Ejecución de `python3 casos_taller/calc_casos.py`; revisión de la construcción de matrices y del contraste con el ejemplo ISO.
- Lectura del XML de ambos libros Excel, conservando fórmulas y resultados almacenados. No se ejecutaron macros ni se recalcularon los libros en Excel.
- Extracción de las 576 parejas referencia–indicación de `BD_DIAS`; reproducción de las cifras del nivel nominal cercano a 130 nmol/mol y de los errores diarios citados por C.
- Reproducción selectiva del ANOVA de las hojas `45ppb`, `135ppb`, `360ppb`, `405ppb` y `455ppb`, usando B6:C23 y la estructura analista × campaña con seis días por celda.
- Comprobación de las sumas de horas y de los incrementos curriculares.
- Consulta dirigida de fuentes oficiales BIPM/VIM e ILAC para resolver discrepancias específicas. Estas consultas no constituyen una revisión exhaustiva de la vigencia de todas las normas.

En lo que sigue, **confirmado** significa verificado en el material o por recálculo; **condicionado** significa plausible, pero dependiente de supuestos o documentación; y **juicio de diseño** significa una valoración pedagógica argumentada, no un resultado experimental.

## 3. Comparación general

| Dimensión | A | B | C |
|---|---|---|---|
| Diagnóstico técnico general | El más equilibrado; explicita supuestos y límites | Amplio y claro, con generalizaciones excesivas | Muy concreto en Excel; desigual al interpretar y corregir |
| Inspección de los datos originales | Buena, pero omite la transformación absoluta del R&R | Insuficiente para respaldar su aprobación global de cifras | La aportación diferencial más fuerte |
| Trazabilidad | Fuentes, alcance y pendientes bien distinguidos | Localizaciones útiles, registro de verificación escaso | Celdas y cifras precisas; varias referencias de línea desfasadas |
| Aplicabilidad a CALAIRE | La mejor delimitación | Reconoce la necesidad de elegir régimen | Separa regímenes, pero sigue presuponiendo usos locales |
| Frontera entre niveles | La más consistente y explícita | Buenos perfiles, mapa básico sobrecargado | Mejor que el temario original, con fronteras móviles |
| Realismo temporal | La hipótesis más defendible; requiere piloto | No evaluable: no asigna horas | Sumas correctas, suficiencia poco defendible |
| Evaluación del aprendizaje | Rúbricas y errores críticos definidos | Pide evaluación, sin desarrollarla | Describe prácticas; no fija un sistema de aprobación |
| Preparación de materiales | Paquetes, resultados y límites de uso | Lista operativa especialmente útil | Mucha descripción del futuro curso; preparación incompleta |
| Plan de implementación | El más completo, aún sin responsables ni estimación de producción | Buen inventario, falta secuencia de cierre | Archivos concretos, pero hoja de ruta corta para el alcance |
| Utilidad principal | Documento rector de la revisión | Diseño de competencias y material docente | Auditoría de datos y fórmulas de los libros |

No se asigna una nota decimal global: daría una precisión artificial y permitiría que una buena presentación compensara un error técnico crítico. Para elegir una base de implementación, el orden es **A, B, C**. Para recuperar hallazgos específicos de Excel, **C tiene prioridad sobre A y B**.

## 4. Hallazgos del contraste independiente

### 4.1 Coeficientes incompatibles del caso B: las tres aciertan

**Estado: confirmado.** El script produce para GGMR variante (i):

```text
a = -0.184237121 nmol/mol
b =  0.998350748
```

La sección 5 del caso conserva otro par. A/H08, B/E6 y C/§2.2 detectan correctamente la discrepancia. Es una corrección documental inmediata y verificable. No demuestra que todo el procedimiento GGMR esté validado.

El contraste incluido en el script reproduce el ejemplo ISO/TS 28037 dentro de la tolerancia declarada de `2e-4`. No obstante, `ggmr_fit` construye explícitamente los bloques cruzados con ceros. A/H09 y §4.8 delimitan bien esa capacidad; B y C hablan de validación con menos precisión. C propone posteriormente estudiar `U_xy ≠ 0`, tarea que requiere ampliar o sustituir la herramienta disponible.

**Decisión:** adoptar la corrección común y la delimitación de A. Toda actividad con covarianza cruzada debe tener herramienta y resultados de referencia propios.

### 4.2 El R&R analiza magnitudes de error: C detecta una omisión decisiva de A y B

**Estado: confirmado en la rotulación y en una correspondencia concreta de datos.** `BASE DE DATOS!B70` contiene `VALORES ABSOLUTOS`. En la campaña de febrero de 2023 se pueden contrastar los errores diarios con signo del certificado con sus magnitudes positivas en R&R. Por ejemplo, un error aproximado de `−0,396402` aparece como `+0,396402`.

C/§2.3.A identifica correctamente el problema. Analizar `|e|` puede ser útil si la pregunta es sobre la magnitud del error; no permite interpretar sin más sus componentes como precisión del error con signo. Dos analistas con sesgos de −0,30 y +0,30 tendrían igual magnitud media y una diferencia con signo de 0,60. La transformación puede ocultar esa diferencia.

A/H11 reproduce correctamente varias F bajo el modelo numérico aplicado. B/§9 también aprueba los cuadrados medios y F. Pero **reproducibilidad aritmética y validez del mensurando analizado son comprobaciones distintas**. Ambas auditorías debieron advertir la transformación antes de respaldar la interpretación metrológica.

El recálculo selectivo reproduce las F de interacción de aproximadamente 6,6115; 4,3087; 6,4735 y 5,0654 en 135, 360, 405 y 455 ppb. Esas cifras corresponden a la respuesta almacenada. No pueden trasladarse como resultados del error con signo sin reconstruirlo y repetir el análisis.

C también debe corregirse: en su nueva práctica M6-A vuelve a pedir «cuantificar la interacción significativa» en los mismos cuatro niveles. **Después de cambiar la respuesta a errores con signo, los niveles significativos pueden cambiar.** El ejercicio debe pedir estimar e interpretar el resultado obtenido, sin imponer la conclusión antigua.

**Decisión:** incorporar el hallazgo de C como requisito previo al uso del caso D y retirar cualquier conclusión sobre precisión con signo hasta disponer de los datos adecuados.

### 4.3 Las 48 lecturas brutas no representan necesariamente un mismo valor de entrada

**Estado: confirmado para el nivel examinado.** Al extraer el cuarto escalón de `BD_DIAS`, las medias de referencia por día son aproximadamente:

```text
127.8464; 127.2152; 129.6152; 128.6263; 131.2302; 131.2244 nmol/mol
```

Se reproducen las cifras de C/E-04:

| Estadístico | Valor reproducido |
|---|---:|
| Desviación estándar de las 48 indicaciones brutas | 1,602254 nmol/mol |
| Desviación estándar de las 48 diferencias con signo | 0,401569 nmol/mol |
| Desviación intradía agrupada de las indicaciones | 0,335765 nmol/mol |

C aporta aquí evidencia más fuerte que A y B. Para estudiar el comportamiento del instrumento, la variación de entrada debe separarse o modelarse.

Pero C exagera al afirmar que «solo» las diferencias son comparables, o que «nunca» pueden analizarse indicaciones brutas: un modelo que incluya la referencia medida también puede ser apropiado. Además, restar la referencia no garantiza independencia, homocedasticidad ni eliminación de un sesgo proporcional. Si `y = a + b·x`, la diferencia esperada es `a + (b−1)·x`; puede seguir variando con la concentración real.

El cero tampoco queda exento de revisar efectos diarios y dependencia. Puede emplearse para una descripción agrupada, pero no se justifica por ello una inferencia con 48 observaciones independientes.

**Decisión:** adoptar el diagnóstico de C y enseñar diferencias con signo como respuesta inicial para el caso, conservando la comprobación del modelo y de la estructura temporal que pide A.

### 4.4 Repetibilidad y unidad de réplica: A formula la corrección más precisa

Las tres reconocen un problema de dependencia y agrupación. La divergencia está en la solución:

- **A/H07:** distingue variación dentro de ciclo, entre ciclos y entre días; no presume el tamaño ni el signo de la autocorrelación.
- **B/E1:** fija como regla única que la unidad de réplica es el día, `n = 6`.
- **C/E-07 y nueva M4:** propone una t sobre las ocho lecturas de un nivel y un día, mientras M5 advierte que no son ocho réplicas independientes del proceso de calibración.

La regla de B puede ser adecuada para una pregunta sobre medias diarias, pero no sirve universalmente para todo el curso. La propuesta de C puede ser válida para una pregunta de corto plazo si las diferencias cumplen los supuestos; el documento no demuestra esas condiciones. Tampoco está demostrado que todas las F de falta de ajuste deban aumentar al ignorar dependencia, como asegura B/E1.

**Decisión:** definir para cada actividad resultado, escala temporal, unidad de repetición y población a la que se generaliza. Una regla de calendario no sustituye al modelo.

### 4.5 `Urepetibilidad` del certificado: el hallazgo de C está sustentado

**Estado: confirmado.** En el libro:

```text
BD_DIAS!E8:
_xlfn.STDEV.P(F15:F110,L15:L110,R15:R110,X15:X110,AD15:AD110,AJ15:AJ110)

BD_DIAS!E10:
IFERROR(E8/SQRT(E4),"-")

Uexp!I8:
+BD_DIAS!$E$10
```

Las columnas de diferencias contienen `ABS(...)`. El valor almacenado de E8 es aproximadamente 0,252452 y el de E10, 0,0105188 nmol/mol. El cálculo combina 12 escalones y seis días y reutiliza una contribución única.

C acierta al cuestionar la transformación, la agrupación y la división por √576. Es una aportación que A no desarrolla y B no detecta con ese detalle. El defecto principal no se resuelve cambiando `STDEV.P` por `STDEV.S`: hay que definir qué resultado requiere incertidumbre y qué componentes lo afectan.

La expresión de C «subestimando ... en más de un orden de magnitud» no debe convertirse en factor de corrección universal. El cociente depende del nivel, del resultado —lectura, promedio o uso futuro— y de qué contribuciones ya estén incluidas en el presupuesto.

**Decisión:** reconstruir la componente bajo un modelo explícito por nivel o una función justificada; revisar doble conteo con regresión y precisión intermedia. Conservar las fórmulas originales como evidencia, no como solución docente.

### 4.6 C niega un máximo puntual que sí existe

**Estado: contradicción comprobada entre C y el libro.** C/§2.3.B.4 afirma que el libro no reporta punto a punto `max(U_i, CMC_i)`. Sin embargo:

```text
Uexp!P8 = +IF(O8<=N8,"OK","ERROR")
Uexp!Q8 = IF(P8="OK",N8,O8)
```

Q8 selecciona el mayor de N8 y O8. A/H16 lo describe correctamente. También existe un cálculo posterior en `Uexp!U22`, `Q6+T10+S6`, relacionado con el desplazamiento de la curva.

**Los dos mecanismos pueden coexistir.** Para determinar qué se declara finalmente hay que seguir las referencias hasta las tablas, ecuaciones y salida del certificado. La existencia de un ajuste posterior no permite negar el máximo intermedio, ni la existencia del máximo valida toda la salida.

**Decisión:** reformular el hallazgo de C como una auditoría pendiente de la cadena completa de reporte, conservando la constatación de A.

### 4.7 Incertidumbre histórica y nueva sección eficaz: acuerdo en el diagnóstico, cautela desigual

Las tres aciertan al pedir que el presupuesto histórico del SRP 6008 se distinga del uso de la nueva sección eficaz. Se confirma `0,0035/1,1329 ≈ 0,0030894`, es decir, 0,309 % de incertidumbre estándar relativa.

C calcula un término proporcional de aproximadamente `0,00425·x` al combinar 0,00292 y 0,00309 en cuadratura. La operación es correcta **como escenario condicionado a conservar las demás entradas y asumir la estructura correspondiente**. No demuestra que ese sea el presupuesto vigente del SRP55.

A/H04 evita mejor ese salto: pide presupuestos rotulados y documentación propia. B/E4 propone un recálculo didáctico válido, pero debe etiquetarlo como tal.

**Decisión:** conservar los presupuestos históricos para reproducción y usar documentación propia para decisiones actuales. Una sustitución de coeficiente no valida un presupuesto completo.

### 4.8 Cambio de escala: la explicación de C es demasiado categórica

C/E-02 atribuye la diferencia entre 1,25 % y 1,29 % únicamente al truncamiento de `1,1476` a `1,147`, y presenta un cambio físico único. El [informe BIPM 2024/03, §§2.2 y 3.2](https://www.bipm.org/documents/d/guest/rapportbipm2024-03) reconoce el valor histórico 1,147 y variaciones de implementación; además identifica 1,1476 para equipos KRISS. No respalda reducir toda la diferencia a un error de redondeo del temario.

Los cocientes que aparecen en los documentos efectivamente producen resultados distintos:

| Par numérico | Incremento de concentración para iguales señales |
|---|---:|
| 1,147 / 1,1329 | +1,244594 % |
| 308,32 / 304,39 | +1,291107 % |
| 1,1476 / 1,1329 | +1,297555 % |

A/H05 es mejor: exige identificar el par aplicado, la escala de cada instrumento y el denominador del indicador. B también necesita esa precisión al trabajar el efecto sobre redes.

**Decisión:** retirar «únicamente por truncamiento» y resolver el ejercicio con los valores realmente implementados. El signo del error de red depende de cuál escala usa la medición y cuál la referencia.

### 4.9 C introduce una notación de cobertura incorrecta o ambigua

En la nueva M8, C escribe `k = t_{0,95}(ν_eff)`. Si el subíndice representa la probabilidad acumulada, un intervalo bilateral central del 95 % requiere `t_{0,975;ν_eff}`. B/E11 lo indica correctamente. C usa en M12 `t_{0,95}` para un límite unilateral; trasladarlo al presupuesto bilateral cambia el significado.

Es posible definir una notación de t indexada por cobertura bilateral, pero entonces debe declararse y no alternarse con cuantiles acumulados. La lectura ordinaria del texto de C es ambigua y no resulta aceptable como instrucción de cálculo.

A también debe concretar su escritura abreviada `k=t(ν_eff)` al convertirla en material docente. La aproximación de Welch–Satterthwaite y el uso de Student deben conservar sus condiciones; pocos días no justifican por sí solos cualquier aplicación mecánica.

**Decisión:** fijar una convención única para todos los cuantiles y comprobar las plantillas con un ejemplo de cobertura declarado.

### 4.10 Corrección VIM y cero–span: C detecta una ambigüedad, pero la explica mal

C/E-09 afirma que la fórmula de dos puntos no es una corrección metrológica porque esta sería `C = x_ref − y`. Esa definición es demasiado estrecha: el [VIM, entrada 2.53](https://jcgm.bipm.org/vim/en/2.53.html), admite compensación por suma, factor o tabla.

Sí es necesario distinguir una corrección aditiva, el valor corregido calculado mediante una función y una modificación de los ajustes del instrumento. Aplicar una fórmula a datos no prueba que se haya efectuado un ajuste físico o de software.

A/H16 y B/E13 son más cuidadosas al pedir convenciones, variables y alcance. C debe mantener la distinción entre modelos de dos puntos y multipunto sin presentar el modelo de dos puntos como incompatible por definición con el concepto de corrección.

**Decisión:** definir qué operación se realiza, sobre qué datos y con qué incertidumbre; reservar «ajuste del instrumento» para el cambio efectivo de sus parámetros.

### 4.11 Función de incertidumbre y CMC: C prescribe más de lo que prueba

C/§3.2.4 presenta una función continua particular como requisito CIPM/ILAC-P14 y propone sustituir el polinomio por `√(U₀²+(U₁x)²)`. [ILAC-P14:09/2020, §4.2](https://ilac.org/?ddownload=123348) admite distintas representaciones de incertidumbre: valor único, intervalo con interpolación adecuada, función, matriz o gráfico. No obliga a esa familia funcional.

Una expresión raíz de suma de cuadrados puede ser apropiada si corresponde a las componentes del presupuesto. No se valida por ser más simple. También hay que distinguir presupuesto calculado, incertidumbre declarada, representación funcional y capacidad reconocida. El ajuste propuesto debe comprobar su comportamiento en todo el intervalo pertinente.

**Decisión:** adoptar la exigencia de revisar la representación y su soporte; rechazar el reemplazo automático por una familia predeterminada. A/H16 ofrece una mejor delimitación institucional.

### 4.12 Control histórico, deriva y conformidad: A evita mejor conclusiones excesivas

A/H03 y H10 distingue comparación con límites publicados, cumplimiento de un diseño y adopción local de un procedimiento. También separa tendencia por orden de corrida de deriva por tiempo.

B/E2 pide elegir y justificar el régimen local, pero su taller conserva cartas y una comparación propia que no están preparadas. C distingue QAPP/TAD en teoría, mientras su taller básico pide evaluar cumplimiento QAPP y su M11 intermedia vuelve a superponer datos CALAIRE sobre una línea base NIST. La advertencia de construir límites propios no se traslada con suficiente fuerza al enunciado de la práctica.

**Decisión:** usar la serie NIST para aprender el método; usar una serie homogénea propia para control operativo; identificar expresamente cuándo solo se evalúan umbrales numéricos de referencia. Ninguna auditoría acredita por sí misma el procedimiento adoptado, el estado de acreditación o la CMC vigente de CALAIRE.

## 5. Evaluación individual de A

### 5.1 Ventajas

**Distingue niveles de autonomía.** Su mayor acierto es separar aplicar una función aprobada, seleccionar un ajuste y validar un modelo general. Esto permite que el básico complete tareas útiles sin atribuirle dominio analítico que no se ha enseñado.

**Controla la interpretación de resultados.** Sus advertencias sobre no significación, equivalencia, conformidad y límites de control son pertinentes. Evita presentar un resultado compatible con cero como garantía de desempeño.

**Explica mejor la incertidumbre del resultado que se usa.** La distinción entre una lectura, el promedio de una campaña y un uso futuro es más importante para el laboratorio que añadir otro catálogo de pruebas. También atiende contribuciones comunes y doble conteo.

**Declara límites de la auditoría.** Diferencia inspeccionar fórmulas y cachés de recalcular libros; reproducir un ejemplo de validar software; y citar normas de probar su adopción institucional. Esta disciplina mejora la confianza en lo que sí afirma.

**Incluye criterios de aceptación del rediseño.** Las rúbricas, los errores críticos y los productos de taller permiten comprobar aprendizaje y terminación del trabajo. Es la única propuesta que desarrolla ambos aspectos con suficiente detalle.

### 5.2 Desventajas y riesgos

**La omisión del valor absoluto en R&R debilita un bloque central.** Debe corregir H11, la aprobación numérica del estudio y las actividades avanzadas asociadas. Las cifras se reproducen, pero la interpretación original de precisión no queda validada.

**Las horas son una hipótesis de diseño.** A reconoce la necesidad de piloto, pero 48/80/32 no proceden de tiempos medidos ni de una caracterización del grupo. Es una propuesta más desarrollada que C, no una duración demostrada.

**El básico puede quedar demasiado restringido para operadores con experiencia.** Excluir la selección autónoma de modelos es sensato; impedir también cualquier ajuste OLS guiado puede desaprovechar competencias previas. Conviene diferenciar resolver un ejercicio bajo modelo fijado de decidir que OLS es válido en un caso nuevo. El primero puede caber en un básico de 48 h con buen diagnóstico de entrada.

**La frontera intermedio–avanzado necesita una regla de aplicación.** Si el caso real requiere incertidumbre en ambos ejes y covarianzas, el intermedio debe ejecutar una configuración aprobada o remitirlo. La promesa de «calibración habitual completa» solo se sostiene para los casos que cumplen el modelo enseñado.

**La categoría P1 mezcla consecuencias diferentes.** Un resultado numérico erróneo, una atribución normativa y una demostración incompatible con el enfoque práctico son problemas distintos. Todos pueden bloquear la publicación, pero necesitan responsables y revisiones diferentes.

**Hay repetición editorial.** Fronteras de nivel y exclusiones reaparecen en dictamen, tablas, talleres y cierre. Son consistentes, pero pueden mantenerse en una matriz maestra para reducir el riesgo de divergencia futura.

### 5.3 Calidad del plan de A

**Valoración: la más alta de las tres; implementable después de corregir evidencia y definir producción.**

Las horas cierran: básico 48 h, intermedio 80 h y extensión 32 h. También queda claro que no corresponde vender automáticamente 160 h como itinerario obligatorio: el básico no es un prerrequisito adicional para quien acredita su salida.

Los talleres encajan mejor con las competencias: TB aplica procedimientos; TI analiza casos habituales; TA compara y valida modelos complejos. La condición de entrada a avanzado reduce el riesgo de dedicar esa extensión a remediar conocimientos básicos.

Sus pendientes son de ejecución: responsables, esfuerzo de preparación, calendario, inventario de herramientas, trazabilidad entre cada hallazgo y su cambio, y criterio para resolver resultados del piloto. También debe justificar el umbral de 75/100 y concretar cómo se corrigen y reevaluan errores críticos.

No conviene dejar la verificación de supuestos relevantes para después de empezar a impartir. La separación «antes de impartir»/«antes de versión definitiva» debe revisarse: todo supuesto que determine la validez de un ejercicio evaluado debe resolverse antes de usarlo.

**Adopción recomendada:** base curricular y de control de calidad, con enmiendas obligatorias al R&R, al alcance del intermedio y a la documentación de las horas.

## 6. Evaluación individual de B

### 6.1 Ventajas

**Define perfiles por tareas.** Es útil describir al participante por lo que calcula, interpreta, decide y remite a otro nivel. La lista de señales para escalar una revisión convierte una limitación técnica en una competencia que puede evaluarse.

**Es fácil de trabajar en una reunión de diseño.** Las tablas de errores, vacíos, niveles y casos permiten repartir tareas. Presenta con claridad problemas frecuentes como `U/k`, `s` frente a `s/√n`, convenciones de corrección y prerrequisitos de pruebas de atípicos.

**Propone materiales necesarios.** CSV graduados, plantillas, glosario y rúbricas son entregables concretos. Su observación de que A y D no tienen paquetes equivalentes a B/C sigue siendo relevante.

**Evita fijar horas antes de cerrar alcance.** La falta de horas no debe tratarse como error técnico. Es una buena decisión de secuencia, aunque insuficiente para una programación final.

### 6.2 Desventajas y problemas de coherencia

**Su declaración de verificación es demasiado amplia.** «Las que no se mencionan abajo cuadran» no identifica el universo comprobado, los cálculos ni sus límites. No es equivalente al registro acotado de A. La omisión de los valores absolutos de R&R demuestra por qué esa garantía general es arriesgada.

**El básico conserva una carga analítica considerable.** Incluye t, ANOVA de días, componentes de precisión, Kragten, bandas de guarda y cálculo directo de resultados de comparación. Las plantillas ayudan a ejecutar; no eliminan la necesidad de entender qué modelo y criterio se está usando.

**La tabla contradice las exclusiones.** M6 básico incluye ANOVA y `s_r`, mientras después se afirma que los componentes de varianza entran en I. M9 intermedio pide armar `U_x`, pero luego se reservan matrices y covarianza común a A. Se puede distinguir matriz entregada de matriz construida y justificada, pero B no formaliza esa distinción.

**El taller A básico no define bien su subconjunto.** «Un nivel y la recta de un día» sirve para unas actividades; ANOVA de días requiere más de un día. Son subconjuntos distintos y deben entregarse como tales.

**Impone una unidad de réplica universal.** El día puede ser una unidad adecuada en un estudio concreto, no la respuesta automática a toda cuestión sobre calibración o repetibilidad. Su regla debe sustituirse por la definición del resultado y del diseño.

**Prohíbe demasiado al eliminar toda lectura o exposición breve.** Enseñar qué significa un informe de comparación puede ser útil al operador sin exigirle producirlo. La regla «si no lo calcula, no se enseña» reduce innecesariamente la comprensión del flujo de trabajo.

**Vincula niveles con funciones de autorización.** «Firma presupuestos ... y certificados» no debe aparecer como efecto directo de aprobar el intermedio. La autorización del personal depende de las reglas y evaluación de competencia del laboratorio.

**Depende de datos propios no identificados.** Sustituir el caso B por una comparación CALAIRE–BIPM es deseable si existe el paquete. La auditoría no lo localiza ni propone un recurso alternativo concreto.

**Introduce excepciones al enfoque sin demostraciones.** En §6 vuelve a pedir derivar sensibilidades en I/A porque serían cocientes simples. Si el requisito es excluir esa tarea obligatoria, su dificultad no constituye una excepción. Deben suministrarse y comprobarse numéricamente.

### 6.3 Calidad del plan de B

**Valoración: buen documento de diseño preliminar; plan de ejecución incompleto.**

Puede funcionar como inventario de necesidades y conversación sobre roles. Para programar el curso le faltan horas, diagnóstico de entrada, distribución de prácticas, umbrales de aprobación y secuencia de entregas.

Antes de estimar duración debe resolver el básico y la lógica acumulativa. También debe priorizar los nuevos temas: límite de detección, Allan, Kragten, TOST, ensayos de aptitud y otros no tienen igual necesidad. Agregarlos todos, además de conservar casi todo el núcleo, reproduce la sobrecarga que critica. Por ejemplo, `3·s₀` puede ser una ilustración, pero no una definición universal de límite de detección o cuantificación.

La propuesta de mover M10 antes de M9 puede favorecer al operador; debe comprobarse en una tabla de dependencias. No es una mejora demostrada por sí sola ni debe duplicar contenidos de incertidumbre y decisión.

**Adopción recomendada:** perfiles, competencia de escalamiento, inventario de plantillas y datos. Rehacer el reparto de contenidos y completar planificación antes de usarla como programa.

## 7. Evaluación individual de C

### 7.1 Ventajas

**Inspecciona los archivos que el alumno realmente usaría.** Es su mayor ventaja. Encontrar `ABS`, rangos incompletos, referencias rotas y fórmulas cruzadas cambia el diagnóstico desde «mejorar un temario» a «revisar la validez de los ejemplos y resultados».

**Aporta cifras reproducibles.** Las medias de referencia y dispersiones del nivel cercano a 130 nmol/mol, la mezcla de 576 diferencias absolutas y varias celdas cuestionadas se verifican en el libro.

**Convierte parte de los errores en ejercicios pertinentes.** Comparar indicaciones y diferencias, auditar una fórmula de incertidumbre o revisar una corrección son actividades de aplicación con utilidad inmediata.

**Presenta una propuesta de contenidos muy concreta.** Su tabla maestra facilita ver qué cambia por nivel y permite comprobar las horas. Los anexos propuestos identifican con claridad qué deducciones salen de la práctica obligatoria.

### 7.2 Desventajas técnicas

**Varias soluciones son menos rigurosas que sus diagnósticos.** Los casos documentados en §4 son sustantivos: niega un máximo que sí existe; reduce indebidamente la corrección VIM; impone una función de CMC; trata un cambio de escala como único; y escribe un cuantil de cobertura ambiguo o incorrecto.

**Confunde a veces evidencia de una contribución con obligación de sumarla.** El término `Upatron` basado en SRP27 no basta para acreditar el presupuesto del SRP55. Pero la solución tampoco es añadir sin más una magnitud denominada «grado de equivalencia»: debe explicarse si corresponde una corrección, su incertidumbre, una contribución adicional y posibles dependencias. Lo que se ha demostrado es la insuficiencia de la justificación, no un presupuesto sustituto completo.

**El diagnóstico de `Uo` necesita seguir el modelo completo.** Se confirma que G8 contiene `E8−D20`, con indicación y media de referencia. Para declarar la sustitución correcta deben fijarse orientación, transformación a la coordenada de referencia, número de observaciones, repetición futura y covarianzas. Corregir una resta no valida por sí solo H8:H19.

**Presenta aproximaciones temporales como soluciones generales.** `n_eff = n(1−r₁)/(1+r₁)` necesita condiciones de un modelo de dependencia y de la aproximación. No basta estimar un único retardo con ocho datos ni concatenar días con discontinuidades. Tampoco debe presuponerse la autocorrelación positiva de cada serie sin analizarla.

**No controla suficientemente requisitos de pruebas y decisiones.** La expresión `P = 1−(1−α)^n` necesita independencia de los eventos usados; una prueba de Cochran no «demuestra» heterocedasticidad en cualquier estructura; y una banda de guarda «óptima» requiere especificar distribución, riesgo y criterio de optimización.

**Sobreafirma lo omitido por el temario.** Los rangos incompletos en 405/455 ppb y problemas asociados ya están anunciados en la discusión del estudio. Debe distinguir hallazgos nuevos —como la interpretación del valor absoluto— de problemas conocidos que aún no cuentan con solución docente.

### 7.3 Calidad y realismo del plan de C

**Valoración: buen borrador de temario revisado; plan de formación insuficientemente sustentado.**

Las sumas 30/50/66 h son correctas. El problema está en lo que supone cada incremento:

- **De básico a intermedio, +20 h:** se agregan diseño experimental, ANOVA, incertidumbres de ajuste, WLS/GDR, correlación, cobertura, comparación y decisiones más complejas.
- **De intermedio a avanzado, +16 h:** se agregan modelos mixtos, GGMR general, validación numérica, propagación y remuestreo, métodos robustos, riesgos y control con memoria.

Hay ejemplos especialmente poco defendibles: M7 añade incertidumbre de parámetros, bandas, falta de ajuste, WLS/GDR y ejercicios de referencia con solo una hora adicional; M8 añade modelo, sensibilidades, correlaciones, cobertura, cadena de incertidumbre y auditoría del libro también en una hora. M10 y M11 mantienen las mismas horas en I y A pese a añadir riesgo probabilístico y cartas con memoria. M13 reúne varias familias computacionales en cinco horas.

Una mayor preparación previa podría permitir actividades guiadas en esos tiempos, pero C no establece esas competencias de entrada. No justifica prometer implementación y validación autónomas. Además, describe al avanzado como desarrollador, aumentando la exigencia respecto de A.

La acumulación de horas tampoco viene acompañada de un itinerario real de cursos puente: la tabla enumera versiones completas, pero no define qué se conserva, qué se reemplaza ni cómo se evalúa el ingreso directo. La resta 50−30 no prueba que exista un curso de actualización de 20 h.

La hoja de ruta §7 localiza el generador y el caso B, pero queda corta frente a su propia propuesta. No desarrolla la producción de A/D, el arreglo de las herramientas, las referencias nuevas, el piloto o las rúbricas. **Es más completa como reescritura del temario que como plan para producir y verificar el curso.**

**Adopción recomendada:** registro de hallazgos comprobados de los libros y actividades asociadas, con correcciones. No adoptar su duración ni su promesa de autonomía avanzada sin rediseño y piloto.

## 8. Comparación transversal de la coherencia

### 8.1 Coherencia entre diagnóstico y solución

A presenta la mejor correspondencia: diagnostica exceso de complejidad y reduce la autonomía básica; detecta falta de aplicabilidad y exige documentación; identifica falta de validación y acota la herramienta. Debe aplicar el mismo rigor al mensurando del R&R.

B identifica sobrecarga, pero conserva muchos análisis en básico y agrega nuevos métodos. C identifica el exceso técnico y lo redistribuye, pero mantiene una duración avanzada casi igual a la propuesta original a pesar de añadir auditoría de Excel, validación y métodos adicionales.

### 8.2 Coherencia entre competencias y evaluación

A es superior porque evalúa productos diferentes por ruta. B aporta una competencia transversal muy buena —escalar problemas—, pero no desarrolla sus criterios de aprobación. C describe muchas prácticas sin demostrar cómo distinguir ejecución guiada de dominio autónomo.

Las tres deben separar cuatro verbos: **interpretar, ejecutar, seleccionar y validar**. Un resultado preparado puede evaluar interpretación; una plantilla fija puede evaluar ejecución; elegir entre modelos y justificarlo requiere otra evidencia; validar una herramienta exige casos y tolerancias. El nivel no puede inferirse solo del nombre de la técnica.

### 8.3 Coherencia con el enfoque práctico

Las tres reconocen correctamente que las demostraciones deben salir de la práctica obligatoria. A lo sostiene con mayor consistencia. B reintroduce derivadas por una excepción propia. C elimina deducciones, pero acumula suficiente formulación y programación para consumir el tiempo liberado.

También debe evitarse identificar explicación conceptual con «filosofía»: reconocer por qué `s/√n` no siempre procede o por qué no se transfieren límites entre procesos es parte de aplicar correctamente. El criterio debería ser que la explicación sostenga una decisión verificable del alumno.

### 8.4 Coherencia de fuentes y mantenimiento

A identifica mejor versiones y límites; B es más fácil de consultar; C localiza celdas con detalle. Ninguna aporta un registro único que relacione hallazgo, fuente, cambio, responsable y aceptación.

Las referencias de C a números de línea del temario están desfasadas respecto de la copia actual; conviene citar encabezados y fragmentos, o asociar líneas a una versión identificada. Sus enlaces `file:///...#L...` tampoco garantizan navegación correcta en un visor Markdown.

El generador contiene una función `renum` y una correspondencia de numeración entre identificadores internos y módulos publicados. Por ello, los cambios deben hacerse siguiendo títulos y estructura, no sustituyendo a ciegas una clave como `m9`. Las salidas Markdown/HTML deben regenerarse y compararse. Ninguna auditoría convierte expresamente este detalle de mantenimiento en un criterio de verificación.

## 9. Qué conservar, corregir o posponer

| Decisión | Procedencia | Motivo y condición |
|---|---|---|
| Conservar la distinción operación / análisis habitual / validación compleja | A | Es la arquitectura más coherente; precisar autonomía por tarea |
| Conservar la competencia de escalar casos | B | Debe entrar en objetivos, ejercicios y rúbrica básica |
| Incorporar `ABS`, mezcla de niveles y defectos de rangos/referencias | C | Hallazgos comprobados; revisar su efecto antes de fijar soluciones |
| Corregir coeficientes del caso B | A/B/C | Cambio inmediato con referencia reproducible |
| Corregir el análisis e interpretación del R&R | C, con límites de A | Reconstruir errores con signo; no conservar conclusiones antiguas por obligación |
| Separar presupuesto histórico, escenario didáctico y presupuesto propio | A | Evita atribuir a SRP55 coeficientes ajenos |
| Preparar CSV, diccionarios, plantillas y soluciones A/D | A/B | Dependencia para impartir y pilotar |
| Sustituir la regla universal «la réplica es el día» | B | Definir unidad y resultado por actividad |
| Corregir cuantil de cobertura, VIM y explicación de escala | C | Evitar nuevos errores en la reescritura |
| Revisar salida completa `max` / curva / certificado | A/C | Ambas etapas pueden existir; falta seguir la cadena de reporte |
| Posponer elegir una familia definitiva para `U(x)` | C | Requiere presupuesto, alcance y validación en el intervalo |
| No adoptar 30/50/66 h como compromiso | C | No está sustentada la suficiencia de los incrementos |
| Usar 48/80/+32 h como hipótesis de trabajo | A | Confirmar perfil de ingreso, preparación y tiempos por piloto |
| Priorizar nuevos contenidos por necesidad real | B/C | Evitar crecer por acumulación de técnicas |

## 10. Plan consolidado recomendado

Este es un plan para producir la revisión. Los roles son propuestas de responsabilidad; no constituyen asignaciones institucionales ni autorización para modificar procedimientos del laboratorio. El esfuerzo de producción debe estimarse aparte de las horas de clase.

### Fase 1. Establecer la evidencia y resolver los errores que cambian resultados

**Responsabilidad propuesta:** responsable técnico con apoyo del responsable de datos/cálculo.

**Trabajo:** identificar versiones de archivos; registrar datos originales y transformaciones; corregir la discrepancia B; reconstruir el error con signo para R&R; definir el modelo del certificado; separar escenarios históricos y actuales; y localizar el procedimiento local realmente adoptado. Si faltan datos propios, preparar un ejemplo externo o simulado claramente identificado.

**Entregables:** registro de hallazgos resueltos/pendientes; extracción trazable; resultados reproducibles; ficha de aplicabilidad por criterio; lista de conclusiones que los datos permiten y que no permiten.

**Cierre:** cada resultado enseñado tiene fuente, datos, modelo, unidad y estatus; las discrepancias numéricas están resueltas; ningún ejemplo didáctico se presenta como certificación del desempeño de CALAIRE. El R&R absoluto deja de sostener conclusiones sobre precisión con signo.

### Fase 2. Fijar perfiles de ingreso y competencias de salida

**Responsabilidad propuesta:** coordinación docente y responsable técnico.

**Trabajo:** adoptar la estructura de A y la competencia de escalamiento de B; decidir qué ejercicios guiados caben en básico; definir la frontera del intermedio cuando el caso necesita ambos ejes inciertos; seleccionar un conjunto pequeño de métodos avanzados según el trabajo real.

**Entregable:** una matriz única tarea–nivel–autonomía–prerrequisito–evidencia de evaluación. Incluir expresamente lo que el participante debe remitir a revisión.

**Cierre:** objetivos, publicidad, actividades y rúbricas describen la misma competencia. La aprobación del curso no se confunde con autorización para firmar o con habilitación institucional.

### Fase 3. Producir los casos y herramientas antes de cerrar horas

**Responsabilidad propuesta:** equipo docente y responsable de cálculo.

**Trabajo:** preparar A–D por nivel, con CSV, diccionario, enunciado, solución y controles. Entregar herramientas con entorno reproducible. Para GGMR, declarar `U_xy=0` o implementar y verificar el caso cruzado antes de incluirlo. Preparar ejemplos de fallo y escalamiento, además de casos que cumplen.

**Entregables mínimos:** cada práctica identifica entrada, resultado, herramienta, supuestos, respuesta esperada, tolerancia y tiempo previsto. Las plantillas distinguen celdas editables, entradas fijadas y decisiones que requieren revisión.

**Cierre:** un docente distinto del autor puede ejecutar el caso sin reconstruir Excel ni suponer documentación ausente. Toda práctica evaluada tiene una solución comprobada.

### Fase 4. Revisar el generador y sincronizar las salidas

**Responsabilidad propuesta:** mantenedor del material, con revisión técnica y docente.

**Trabajo:** modificar `temario_build.py`, mantener una numeración coherente y regenerar Markdown/HTML. Incorporar las convenciones de unidades, símbolos y cuantiles, los anexos opcionales y referencias precisas. Revisar enunciados y soluciones en conjunto.

**Cierre:** las salidas contienen los mismos objetivos, horas y prácticas; los enlaces funcionan; las fórmulas no cambian de significado entre versiones; las búsquedas de coeficientes antiguos no dejan contradicciones en el material activo.

### Fase 5. Pilotar los bloques que determinan la duración

**Responsabilidad propuesta:** coordinación docente con participantes representativos.

**Trabajo:** usar como hipótesis inicial la distribución de A y medir M6–M8 y taller A; añadir un piloto avanzado de validación si se mantiene esa promesa. Registrar tiempo de preparación del alumno, ejecución, interpretación, corrección y apoyo del docente.

**Cierre:** ajustar alcance u horas con evidencia. Si el grupo no completa la práctica de forma suficientemente autónoma, reducir competencias o aumentar tiempo; no dar por cumplida la meta porque se mostró una solución preparada.

### Fase 6. Aprobar la versión docente

**Responsabilidad propuesta:** coordinación docente y responsable técnico.

**Trabajo:** revisar resultados de piloto, cerrar incidencias y aprobar rúbricas. El 75/100 propuesto por A puede servir como punto de partida; requiere acuerdo sobre evidencia mínima, errores críticos y reevaluación.

**Cierre:** no quedan errores que alteren cálculos o decisiones en ejercicios obligatorios; se explicitan pendientes documentales; todos los paquetes son reproducibles; las competencias declaradas se evalúan; y las duraciones corresponden al perfil de entrada publicado.

## 11. Condiciones que aún impiden considerar terminado el plan

Ninguna de las tres auditorías, por sí sola, acredita que el curso esté listo para impartirse. Faltan decisiones y materiales concretos:

1. Una respuesta documentada sobre procedimiento, escala y presupuesto propios aplicables al ejemplo actual.
2. Datos con signo y solución revisada de R&R, o una delimitación expresa del estudio de magnitud del error.
3. Seguimiento completo de las fórmulas hasta la salida declarada del certificado.
4. Paquetes A/D autónomos y versiones graduadas del resto de casos.
5. Herramientas preparadas y verificadas para todas las variantes realmente exigidas.
6. Diagnóstico de entrada, resultados de piloto y criterios de aprobación concretos.

Estos pendientes no justifican detener la producción del material: permiten definir ejercicios históricos o didácticos y avanzar en paralelo en contenidos que no dependan de documentación propia. Sí impiden atribuir conclusiones operativas al laboratorio sin su soporte.

## 12. Veredicto por documento

**A — adoptar como base, con enmiendas.** Es la más sólida para gobernar el rediseño porque articula competencias, materiales, evaluación y cierre. Debe incorporar el hallazgo de valores absolutos y revisar las conclusiones del R&R. Sus horas son una estimación razonada que debe pilotarse.

**B — incorporar como complemento docente.** Sus perfiles, señales de escalamiento e inventario de materiales son valiosos. Debe reducir el básico, resolver contradicciones de nivel y reemplazar reglas universales por condiciones de aplicación. No es todavía una programación ejecutable.

**C — incorporar como evidencia técnica revisada.** Sus hallazgos comprobados en Excel son indispensables y corrigen una omisión seria de A/B. Debe separar hechos de inferencias, enmendar las correcciones problemáticas y rediseñar el compromiso horario. No conviene usar su temario propuesto como versión final.

La decisión más defendible es una revisión dirigida por A, corregida con la evidencia de C y hecha operativa con las competencias y materiales de B. La calidad final dependerá de resolver esas discrepancias y verificar las soluciones, no del número de recomendaciones reunidas.

## 13. Referencias y límites de reproducibilidad

### Material local contrastado

- [Auditoría A](audit_a.md): H03–H16; §§4.2, 4.8, 5, 7, 9 y 10.
- [Auditoría B](audit_b.md): §§2–3; E1, E4, E6, E9 y E11; §§5–9.
- [Auditoría C](audit_c.md): E-01, E-02, E-04, E-07 y E-09; §§2.3, 3.2, 5 y 7.
- [Temario](temario_curso.md) y [generador](temario_build.py).
- [Cálculos B/C](casos_taller/calc_casos.py), [caso B](casos_taller/caso_B_comparacion_clave.md), [caso C](casos_taller/caso_C_historial_level2.md) y sus tres CSV.
- [Certificado de calibración](<docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm>): `BD_DIAS`, `Resumen`, `Uexp`, `EcuOffset` y datos diarios asociados.
- [Estudio R&R](<docs/Resultados R&r_2022 2023 (1).xlsx>): `BASE DE DATOS` y hojas de concentración indicadas.
- [Protocolo BIPM.QM-K1](docs/BIPM.QM-K1_2.protocol.pdf), §1.1, y [certificado SRP 6008](docs/SRP6008_spec_cert.pdf), utilizados para contraste histórico dirigido.

### Fuentes oficiales consultadas para resolver discrepancias

- [BIPM, informe 2024/03, revisión de septiembre de 2025](https://www.bipm.org/documents/d/guest/rapportbipm2024-03): §§2.2 y 3.2, valores e implementaciones de la sección eficaz.
- [VIM, entrada 2.53](https://jcgm.bipm.org/vim/en/2.53.html): alcance del concepto de corrección.
- [ILAC-P14:09/2020](https://ilac.org/?ddownload=123348): §4.2, formas de expresión de incertidumbre en el alcance de acreditación.

### Límites

Las cifras extraídas de Excel son valores almacenados y fórmulas inspeccionadas; no equivalen a una recalculación integral del libro. La reproducción del ANOVA fue selectiva y utilizó la respuesta existente. No se reconstruyó el error con signo de todas las campañas ni se estableció un presupuesto sustituto del SRP55. No se validaron integralmente el certificado, el software o la acreditación. Las valoraciones de suficiencia horaria son juicios de diseño pendientes de piloto, no tiempos medidos de aprendizaje.
