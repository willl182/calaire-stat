# M13. Métodos numéricos para calibración y análisis (solo nivel A)

## Ficha del capítulo

| Campo | Contenido |
|---|---|
| Competencia estadística | Contrastar la propagación lineal con métodos numéricos y decidir cuál usar. |
| Prerrequisitos | M3: distribuciones y dependencia; M7: ajuste lineal y calibración inversa; M8: propagación de incertidumbre. |
| Alcance por nivel | Solo A. Prop_e asigna M13 al nivel A; no hay contenidos ni secciones de nivel B o I. |
| Contenido A | Monte Carlo frente a propagación lineal en una calibración inversa; salidas múltiples y covarianza; bootstrap con unidad de remuestreo definida por el diseño; regresión de Huber frente a OLS ante una observación influyente, con supuestos y límites. |
| Datos de los ejemplos | Simulados y producidos de forma reproducible con semilla fija por `calc/M13_ejemplos.py`; no proceden del certificado F-PSMT-01 y no describen resultados de CALAIRE. El ejemplo de regresión robusta contiene una alteración simulada, declarada expresamente. |
| Anexos | AX.2, para la propagación lineal general; AX.5, para las ecuaciones normales y la covarianza de los parámetros; AX.9, cuando se interpreten diferencias con entradas compartidas; AX.13, para el fundamento de Monte Carlo y el control del número de ensayos. |
| Referencias clave | GUM; GUM-S1; GUM-S2; ISO/TS 28037; Efron y Tibshirani (bootstrap, referencia externa sin numeral); Huber (regresión robusta, referencia externa sin numeral). |

## Nivel A — métodos numéricos y elección del método

En este módulo no hay una sección B ni una sección I: la propuesta curricular asigna M13 solamente al nivel avanzado. Ustedes llegan con las bases de distribuciones, regresión y propagación que trabajamos antes. Aquí no repetiremos esos módulos. Vamos a concentrarnos en una pregunta de responsable técnico: cuando una fórmula de calibración transforma varias entradas inciertas, ¿basta con propagar linealmente sus incertidumbres o conviene propagar sus distribuciones con un método numérico? Y, cuando el cálculo produce más de una salida, ¿cómo evitamos perder la covarianza entre ellas? Después conectaremos esa pregunta con la estructura de los datos y con la sensibilidad a una observación influyente.

> **[DIAPOSITIVA]** Mapa de decisión: modelo y entradas → dependencias → resultado de interés → método → validación y límites.
>
> **[PAUSA]** Señalar que el método numérico no corrige un modelo mal planteado ni convierte datos deficientes en evidencia suficiente.

Hay cuatro escenas. Primero compararemos la propagación lineal con Monte Carlo para una calibración inversa. Después trataremos pendiente, intercepto y correcciones como salidas conjuntas. En la tercera escena, el bootstrap respetará los bloques del diseño, en vez de fingir que cada fila es independiente. En la última, compararemos OLS con una regresión robusta de Huber en un conjunto docente donde declaramos una observación influyente. En todas las escenas usaremos conjuntos simulados, con fines de enseñanza. No son resultados oficiales ni observaciones del laboratorio.

### Escena A1. Propagación lineal y Monte Carlo en una calibración inversa

Empecemos por la calibración inversa. En una calibración expresada como $y=a+b x$, la indicación $y$ se convierte en una estimación de referencia mediante $\hat{x}=(y-a)/b$. La respuesta no es una función lineal de las entradas: el intercepto se resta y el resultado se divide por la pendiente. Si las incertidumbres son pequeñas y el modelo se comporta de manera suficientemente regular en la región relevante, la propagación lineal aproxima la función alrededor de las estimaciones de las entradas. Cuando queremos representar de manera más completa la distribución del resultado, podemos propagar las distribuciones de entrada por el modelo, que es el enfoque de Monte Carlo descrito por GUM-S1 [GUM-S1 5.4, 5.10–5.11].

> **[PIZARRA]** $$\hat{x}=g(y,a,b)=\dfrac{y-a}{b}$$
>
> **[PIZARRA]** $$u^2(\hat{x})\approx \nabla g^{\mathsf T}\,\mathbf{V}\,\nabla g$$ [GUM 5.2.2]
>
> **[NOTA AL INSTRUCTOR]** Leer la segunda expresión como «la incertidumbre al cuadrado de la estimación se aproxima mediante el gradiente transpuesto, por la matriz de covarianza de las entradas, por el gradiente». Remitir la deducción general de propagación al anexo AX.2, y aquí limitarse al contraste de métodos del M13. La ley de propagación con covarianzas se formula en la GUM [GUM 5.2.2].

La matriz $\mathbf{V}$ no es una lista de varianzas desconectadas. Incluye las covarianzas conocidas o justificadas entre entradas. Por eso, antes de simular, definimos las distribuciones y la dependencia: qué entrada cambia, con qué distribución, qué magnitudes comparten una fuente y cómo se representa esa relación. El Suplemento 1 de la GUM trata la propagación de distribuciones y el muestreo de las entradas; el procedimiento numérico no autoriza a reemplazar una dependencia real por independencia cómoda [GUM-S1 5.3–5.6, 6.4.8.4, 7.3].

Hagamos un ejemplo ilustrativo. El conjunto se ha simulado y el script de cálculo fija una semilla para poder reproducir el resultado. La indicación tiene media de $420,00$ nmol/mol y desviación estándar de $0,80$ nmol/mol. El intercepto tiene media de $0,40$ nmol/mol y desviación estándar de $0,50$ nmol/mol. La pendiente tiene media de $1,002$ y desviación estándar de $0,002$. Suponemos una distribución normal conjunta para las tres entradas, con esas medias, desviaciones y correlaciones; la indicación y el intercepto son independientes, y la correlación entre intercepto y pendiente es $-0,60$ [GUM-S1 6.4.8.4]. El rótulo importa: estos valores no se extrajeron de una calibración del Level 2.

> **[EJEMPLO]** En la pizarra, anotar el modelo inverso, las tres medias, sus desviaciones estándar y la correlación entre intercepto y pendiente. Indicar: «Datos simulados; cálculo reproducible en `calc/M13_ejemplos.py`, bloque A1».

La primera comprobación es aritmética. Si sustituimos las medias en la función inversa, obtenemos $418,762475$ nmol/mol. Esa sustitución no es todavía la incertidumbre y tampoco es necesariamente la media exacta de la distribución transformada. La fórmula de primer orden usa las derivadas evaluadas en las entradas centrales: la derivada respecto a la indicación es $1/b$; respecto al intercepto es $-1/b$; y respecto a la pendiente es $-(y-a)/b^2$ [GUM 5.1.2]. Como la matriz contiene una covarianza negativa entre $a$ y $b$, la varianza de salida incluye el término cruzado correspondiente. No se debe borrar ese término por conveniencia.

En el cálculo lineal, la incertidumbre estándar resultante es $1,041437$ nmol/mol. Ahora hacemos Monte Carlo. En cada ensayo se toma una realización conjunta de las entradas conforme a la distribución normal conjunta declarada, se conservan la correlación y las unidades, y se calcula la misma expresión inversa. Repetimos ese proceso $400\,000$ veces en el ejemplo reproducible. La media simulada de la salida es $418,763825$ nmol/mol, la desviación estándar simulada es $1,040327$ nmol/mol y el intervalo central del $95\,\%$ va de $416,733012$ a $420,803052$ nmol/mol [GUM-S1 5.5, 7.5]. La semilla fija hace que estos valores se puedan volver a generar con el mismo entorno y script.

> **[PIZARRA]** $$\text{cada ensayo: }(y^{(r)},a^{(r)},b^{(r)})\longrightarrow \hat{x}^{(r)}=(y^{(r)}-a^{(r)})/b^{(r)}$$
>
> **[DIAPOSITIVA]** Cuadro comparativo: estimación al sustituir las medias, incertidumbre lineal, media Monte Carlo, desviación estándar Monte Carlo e intervalo central Monte Carlo. Rótulo visible: **datos simulados**.

En este caso, las dos incertidumbres estándar difieren en $0,001110$ nmol/mol, algo más de una milésima: la aproximación lineal da $1,041437$ nmol/mol y Monte Carlo da $1,040327$ nmol/mol. La proximidad aquí no demuestra que siempre sean intercambiables. Es evidencia para este modelo y esta escala de incertidumbre.

Además, la media simulada y el valor calculado al sustituir las medias no coinciden exactamente: la transformación no lineal puede desplazar la media de la salida. En otras aplicaciones puede importar la asimetría de la distribución, un límite físico, una entrada con distribución no normal o una incertidumbre suficientemente grande como para que la curvatura del modelo sea relevante.

GUM-S1 presenta Monte Carlo como un método de propagación de distribuciones y especifica condiciones para resumir sus resultados; no lo describe como una mejora automática en cualquier cálculo [GUM-S1 5.10–5.11, 7.5–7.8].

La decisión no consiste en decir «Monte Carlo es más avanzado, por tanto es mejor». Primero definimos el mensurando, el modelo, las distribuciones y las dependencias. Luego evaluamos si las condiciones y precisión de la aproximación lineal son adecuadas para el propósito. Si la linealización es suficiente, está validada y entrega la información requerida, su menor costo puede ser una ventaja. Si la forma de la distribución de salida o la no linealidad resulta importante, Monte Carlo permite propagar las distribuciones, pero exige más entradas bien caracterizadas y una implementación comprobada. El resumen de la simulación también debe ser apropiado: una media y una desviación no bastan para describir una distribución marcadamente asimétrica.

Fíjense en la dependencia. Si en el ejemplo hubiéramos generado por separado el intercepto y la pendiente, habríamos usado una matriz distinta de la declarada. El resultado sería reproducible, pero respondería a otro modelo estadístico. Preservar dependencia significa simular conjuntamente de una forma que tenga la covarianza que justifica el modelo; no significa añadir una correlación solo porque el software lo permite. Si la estructura de dependencia no se conoce, la limitación debe quedar explícita y, si cambia la conclusión, corresponde solicitar información o análisis técnico antes de reportar una cifra definitiva.

> **[ERROR CRÍTICO]**

No traten las entradas correlacionadas como independientes sin justificación. Tampoco interpreten que una nube grande de simulaciones compensa una matriz de covarianza equivocada, una distribución asignada sin fundamento o un modelo de medición incompleto.

> **[PREGUNTA AL GRUPO]** Si el intervalo Monte Carlo es asimétrico, ¿sería prudente reportar automáticamente «estimación más o menos dos veces la desviación estándar»? — *Respuesta esperada:* no; se debe comprobar si ese resumen representa la distribución y la cobertura requeridas.

Una última cautela sobre el número de ensayos. Un número alto reduce el ruido numérico de los resúmenes, pero no garantiza por sí solo que un cuantil esté estabilizado ni que la simulación sea correcta. Como punto de partida, la GUM-S1 recomienda un número de ensayos de al menos $10^4/(1-p)$. Para un intervalo del $95\,\%$, esto corresponde a $200\,000$ ensayos; aquí usamos $400\,000$ [GUM-S1 7.2.2]. El responsable debe revisar además la estabilidad de los resultados en relación con la tolerancia numérica que necesita [GUM-S1 7.9.2–7.9.4]. La deducción del fundamento del método y el control del número de ensayos se desarrollan en el Anexo AX.13; aquí nos quedamos con la lectura operativa.

### Escena A2. Pendiente, intercepto y correcciones como salidas conjuntas

Pasemos de una salida a varias. Cuando ajustamos una recta, solemos presentar el intercepto y la pendiente juntos. En uso inverso calculamos también estimaciones corregidas en varios niveles de indicación. Esas cifras comparten los mismos datos y los mismos parámetros: no son resultados independientes. Si informamos cada incertidumbre estándar por separado y omitimos la covarianza, perdemos una parte de la información necesaria para calcular contrastes o diferencias posteriores. GUM-S2 extiende el tratamiento a vectores de salidas y describe la matriz de covarianza conjunta [GUM-S2 5.2–5.3, 6.2, 7.6]. Para los parámetros de una recta, la ISO/TS 28037 trata las incertidumbres y covarianzas asociadas con los valores y los parámetros de calibración [ISO 28037 10.1–10.2].

> **[PIZARRA]** $$\boldsymbol{q}=(a,b,\hat{x}_{80}-80,\hat{x}_{250}-250,\hat{x}_{420}-420)^{\mathsf T}$$
>
> **[PIZARRA]** $$\mathbf{V}_{q}=\left[\operatorname{cov}(q_i,q_j)\right]$$
>
> **[NOTA AL INSTRUCTOR]** Decir en voz alta «la salida conjunta es un vector, y su incertidumbre conjunta es una matriz». No desarrollar aquí las ecuaciones normales ni la propagación matricial; remitir a AX.5 cuando se necesite la deducción de los parámetros.

Vamos a construir un ejemplo con seis niveles de referencia: $40$, $100$, $180$, $260$, $340$ y $440$ nmol/mol. Se simularon seis días completos. Cada día contiene una lectura en cada nivel, de modo que tenemos $36$ observaciones en total. Los datos se generaron alrededor de una recta con un desplazamiento común a cada día, fijado en el script, y pequeñas variaciones de punto, también fijadas en el script. El diseño está hecho para enseñar cómo se presentan varias salidas; no describe la estructura ni el desempeño de una campaña real de CALAIRE.

> **[EJEMPLO]** Mostrar seis filas, una por día, y seis columnas, una por nivel. Rotular los datos como simulados; señalar que cada fila completa es un bloque diario.

El ajuste OLS del conjunto entrega un intercepto estimado de $0,65184834$ nmol/mol y una pendiente estimada de $1,00151145$. Para representar la agrupación por día, el script calcula una matriz de covarianza agrupada por conglomerado, no la covarianza OLS clásica. Con esa estimación, la covarianza entre intercepto y pendiente es $-0,0000000261$ y su correlación es aproximadamente $-0,0051$. En este cálculo casi no hay asociación estimada entre los dos parámetros. Esta matriz agrupada es solo una ilustración: con seis días, su estimación es poco estable y no debe tratarse como una caracterización precisa de la variabilidad entre días.

La matriz agrupada estimada tiene varianza de intercepto $0,01183676$ y términos cruzados de aproximadamente $-0,00000003$ al redondear. La varianza de la pendiente es muy pequeña: $0,000000002191$. No la interpretemos como exactamente nula ni omitamos su escala al presentar la matriz. La simetría no es un adorno: una matriz de covarianza debe cumplirla. Las unidades tampoco son idénticas en todos sus elementos. La varianza del intercepto se expresa en $(\mathrm{nmol/mol})^2$; la varianza de la pendiente es adimensional al cuadrado; la covarianza combina una unidad de intercepto con una pendiente adimensional. No mezclen sus magnitudes ni comparen celdas como si fueran la misma unidad.

> **[DIAPOSITIVA]** Matriz $\mathbf V_{(a,b)}$ calculada por el script. Destacar diagonal, simetría y término fuera de la diagonal. Añadir debajo: «estimaciones del ejemplo simulado; cifras redondeadas solo para exposición».

Ahora convertimos tres indicaciones en estimaciones inversas y correcciones aditivas, usando la convención del curso: $\hat{x}=(y-a)/b$ y corrección $\hat{x}-y$. Para una indicación de $80$ nmol/mol, la estimación inversa es $79,228402$ nmol/mol y la corrección es $-0,771598$ nmol/mol. Para una indicación de $250$ nmol/mol, la estimación inversa es $248,971842$ nmol/mol y la corrección es $-1,028158$ nmol/mol. Para una indicación de $420$ nmol/mol, la estimación es $418,715283$ nmol/mol y la corrección es $-1,284717$ nmol/mol. Cada una de estas correcciones proviene de la misma recta ajustada.

> **[PIZARRA]** $$c(y)=\hat{x}-y=\dfrac{y-a}{b}-y$$
>
> **[PREGUNTA AL GRUPO]** ¿Por qué no podemos tratar las correcciones calculadas en los distintos niveles como si vinieran de tres rectas independientes? — *Respuesta esperada:* comparten los parámetros estimados y, por tanto, parte de su variación y covarianza.

El script propaga conjuntamente la covarianza de $a$ y $b$ hacia el vector de salidas, usando las sensibilidades locales de las correcciones respecto a esos dos parámetros. Con la matriz agrupada por día, las incertidumbres estándar de las correcciones son $0,108677$ nmol/mol a $80$ nmol/mol, $0,109195$ nmol/mol a $250$ nmol/mol y $0,110283$ nmol/mol a $420$ nmol/mol. Son estimaciones basadas en solo seis bloques y, por tanto, deben leerse con cautela. Además de esas incertidumbres individuales, obtenemos una matriz completa para intercepto, pendiente y las tres correcciones. El Suplemento 2 de la GUM pide justamente conservar la estimación conjunta y su matriz de covarianza para un vector de salidas [GUM-S2 7.6].

Leamos dos términos de esa matriz. La covarianza entre las correcciones a $80$ y $250$ nmol/mol es $0,01183560$ $(\mathrm{nmol/mol})^2$. Entre las correcciones a $250$ y $420$ nmol/mol es $0,01201140$ $(\mathrm{nmol/mol})^2$, y entre las correcciones a $80$ y $420$ nmol/mol es $0,01186056$ $(\mathrm{nmol/mol})^2$. Las tres son positivas en este ejemplo. Cuando una corrección se desplaza hacia arriba, las otras tienden a hacerlo también. Las correlaciones entre las parejas $80$–$250$, $250$–$420$ y $80$–$420$ son, respectivamente, aproximadamente $0,9974$, $0,9974$ y $0,9896$. La dirección y el tamaño dependen de la geometría de la recta y del rango de uso; no hay una regla universal según la cual todas las salidas deban moverse juntas.

La matriz de correlaciones ayuda a comparar esas dependencias sin mezclar unidades. La correlación entre intercepto y pendiente es aproximadamente $-0,0051$. Las correlaciones entre las correcciones a $80$ y $250$ nmol/mol, y entre $250$ y $420$ nmol/mol, son ambas aproximadamente $0,9974$. Estos valores también son resultados del ejemplo simulado y se reproducen en el bloque A2 del script. No los trasladen a otra calibración: dependen de sus niveles, su dispersión, el modelo y la covarianza estimada.

> **[ERROR CRÍTICO]**

No entreguen una tabla de salidas múltiples como si cada renglón fuese independiente cuando se usarán después para calcular una diferencia, una combinación o una comparación. No sustituyan la matriz por una colección de incertidumbres marginales si el análisis posterior necesita covarianza.

También observamos que las incertidumbres de las correcciones cambian con el nivel de indicación: son distintas en los tres niveles. No es una anomalía. La incertidumbre de una función inversa puede depender del punto de uso, porque cambian las sensibilidades respecto a los parámetros. Si el problema posterior consiste en comparar dos resultados derivados de entradas compartidas, la covarianza de la diferencia puede modificar la incertidumbre combinada; ese tratamiento ya está en el alcance de M9 y remite a AX.9. En M13 nuestra tarea es asegurar que una herramienta que produce varias salidas no borre esa información.

¿Qué validamos? Comprobamos que la vectorización y el orden de las salidas coinciden con la definición del problema; verificamos que las unidades de las covarianzas sean coherentes; comprobamos la simetría de la matriz y que sea admisible como matriz de covarianza; y contrastamos valores seleccionados con una implementación independiente o con una comprobación analítica cuando corresponda. Aquí el script calcula las salidas desde el mismo ajuste y deriva la matriz con la covarianza de los parámetros. Para un uso técnico, esa reproducción es un mínimo, no una validación independiente completa del software de producción.

### Escena A3. Bootstrap que respeta los bloques del diseño

Ahora abordemos el remuestreo. Para distinguir los dos procedimientos, llamaremos «ensayos» a las realizaciones de Monte Carlo y «réplicas» a las muestras bootstrap. Bootstrap no significa «revolver todas las filas y volver a ajustar». Significa construir muestras de remuestreo que representen la unidad independiente que exige el diseño y la pregunta estadística [Efron y Tibshirani 1993, no disponible en docs/]. Si las mediciones están agrupadas por día, si varios niveles de una calibración comparten las condiciones de ese día, remuestrear filas sueltas rompe el bloque y trata como independientes datos que comparten una causa. La propuesta pide expresamente respetar bloques o agrupaciones; la elección de la unidad de remuestreo debe salir del diseño y del resultado que queremos caracterizar.

> **[PIZARRA]** Diseño docente: día → conjunto de niveles medidos ese día. Remuestreo: seleccionar días completos con reemplazo y conservar dentro de cada día el bloque completo.
>
> **[PREGUNTA AL GRUPO]** Si la pregunta es cuánto cambia la pendiente entre días, ¿qué unidad remuestreamos? — *Respuesta esperada:* los días completos, porque el día es la unidad de agrupación que introduce dependencia en este ejemplo.

Volvamos a los datos simulados de la escena anterior: seis días, seis niveles por día, con un resultado por combinación de día y nivel. Para cada réplica bootstrap seleccionamos seis días con reemplazo. Si un día aparece dos veces, se incorpora dos veces el bloque completo con sus seis niveles; si no aparece, ese bloque queda fuera de esa réplica. Reajustamos la recta y guardamos la pendiente y la corrección calculada para una indicación de $250$ nmol/mol. En el script hacemos $20\,000$ réplicas bootstrap de este tipo. El tamaño de la simulación se declara para que la salida sea auditable; no implica que cada réplica contenga observaciones independientes nuevas.

La estimación de pendiente para el conjunto original es $1,00151145$. El intervalo percentil bootstrap del $95\,\%$ para la pendiente va de $1,00143187$ a $1,00159362$. Para la corrección a $250$ nmol/mol, el intervalo percentil va de $-1,21228848$ a $-0,82985981$ nmol/mol. El script fija la semilla y el procedimiento, así que podemos reproducir los límites. Aquí los intervalos son ilustrativos: enseñan qué resume el bootstrap por bloques y no son intervalos certificados para el Level 2.

> **[DIAPOSITIVA]** Dos distribuciones bootstrap: pendiente y corrección en $250$ nmol/mol. Marcar sus límites percentiles, con la nota «bootstrap por días completos; conjunto simulado; no es resultado de CALAIRE».

¿Qué pasaría si, en lugar de seleccionar días, sorteáramos cada fila de manera aislada? El remuestreo crearía combinaciones artificiales: niveles que originalmente compartían el efecto del mismo día podrían terminar como si vinieran de días distintos. Eso cambia la estructura de dependencia y, en general, la incertidumbre estimada ya no responde al diseño declarado. No es posible corregirlo diciendo después que se hicieron muchas réplicas: cada réplica estaría basada en el mecanismo equivocado. En la práctica técnica, la agrupación se decide antes de correr el algoritmo, y se documenta junto con el método.

Hay otro límite importante en nuestro ejemplo: solo tenemos seis bloques diarios. Repetir el sorteo miles de veces no crea días observados adicionales ni aumenta la información real sobre variación entre días. El intervalo bootstrap puede ser inestable cuando el número de unidades independientes es pequeño, cuando la distribución del estimador es irregular o cuando el diseño no representa la población de interés. La precisión computacional del percentil y la solidez estadística del intervalo son preguntas distintas. En consecuencia, un bootstrap por bloques no repara un estudio insuficiente ni sustituye el diseño experimental.

> **[ERROR CRÍTICO]**

No remuestreen lecturas dentro de un bloque como si cada una fuese una réplica independiente cuando el efecto de interés opera entre bloques. No presenten el número de réplicas computacionales como si fuese el número de unidades experimentales.

Antes de usar un bootstrap, digan en voz alta cuál es el estimador que se remuestrea, cuál es la unidad independiente, cómo se mantienen las agrupaciones, qué intervalo se reporta y cuál población pretende representar el diseño. Si el estudio tiene estructura anidada o cruzada, una sola regla genérica de remuestreo puede no bastar: hay que reproducir el nivel de aleatorización que respalda la inferencia. Si no sabemos qué unidades son intercambiables, paramos y pedimos que el diseño se revise. El método numérico no debe presentarse como una rutina automática de software.

> **[ESCALAMIENTO]**

Escalen el análisis si las unidades de remuestreo no están justificadas, si hay muy pocos bloques para sostener la inferencia requerida, si faltan bloques o la estructura cambió durante la campaña, o si la conclusión depende de una agrupación que los datos no permiten reconstruir. Registren la limitación; no oculten la dependencia mediante remuestreo de filas.

Distingamos ahora bootstrap de Monte Carlo. Ambos generan muchas evaluaciones y pueden producir distribuciones numéricas, pero no responden a la misma pregunta ni usan la misma información. En Monte Carlo de la escena inicial, describimos las entradas mediante distribuciones justificadas y las propagamos por un modelo de medición.

En bootstrap, la fuente primaria es la muestra observada: recreamos muestras según un esquema de remuestreo para estudiar la variación de un estimador. Si las distribuciones de entrada se conocen por especificación o por un presupuesto de incertidumbre, Monte Carlo permite utilizar esa información. Si queremos evaluar la variabilidad de un estimador basada en datos y el diseño respalda un esquema de remuestreo, bootstrap puede ser pertinente.

No se elige uno por ser más sencillo de programar. Se elige por el origen de la incertidumbre y por el diseño que permite defender.

En este capítulo los bloques diarios son parte del conjunto simulado, y los días completos son las unidades que remuestreamos. En una aplicación real hay que revisar si todos los días son intercambiables para la pregunta, si la campaña tiene tendencias o cambios de protocolo y si existen agrupaciones de nivel superior. Si el proceso varía entre campañas y dentro de campaña, un esquema que solo remuestrea días puede omitir la variación entre campañas. La regla no es «si hay días, remuestree días»; la regla es identificar qué unidad de replicación sustenta la inferencia. La descripción del diseño debe preceder al código.

### Escena A4. Regresión robusta de Huber frente a OLS

La última escena nos lleva a la sensibilidad del ajuste frente a una observación influyente. OLS elige intercepto y pendiente minimizando la suma de los residuos al cuadrado [ISO 28037 5.8.1]. Por eso, un residuo grande puede pesar mucho en el ajuste. Una alternativa robusta definida es la regresión de Huber: utiliza una función de pérdida cuadrática para residuos pequeños y lineal para residuos grandes. Así limita el crecimiento de la influencia de residuos grandes, sin declarar automáticamente que una observación sea falsa o deba borrarse [Huber 1981, no disponible en docs/].

> **[PIZARRA]** $$\rho_c(r)=\begin{cases}\tfrac{1}{2}r^2,&|r|\le c\\c|r|-\tfrac{1}{2}c^2,&|r|>c\end{cases}$$
>
> **[PIZARRA]** OLS: minimizar $$\sum_i r_i^2$$; Huber: minimizar $$\sum_i\rho_c(r_i)$$, con una escala $$c$$ declarada.
>
> **[NOTA AL INSTRUCTOR]** Leer la expresión: «la pérdida de Huber es cuadrática mientras el residuo no supera la escala y lineal después; la escala determina dónde cambia el trato». La implementación del ejemplo usa `scipy.optimize.least_squares` con pérdida Huber y escala `0,35` nmol/mol; los resultados no deben separarse de esa especificación.

En la práctica, la pérdida de Huber se resuelve iterativamente. Una lectura operativa equivalente es que cada observación recibe un peso que se mantiene cuando el residuo es pequeño y disminuye cuando el residuo excede la escala definida. Los pesos dependen del ajuste actual; por eso se vuelve a estimar la recta hasta que el procedimiento converge. El resultado depende de la elección de escala, la inicialización y la implementación. Para este ejemplo se ha fijado la escala de $0,35$ nmol/mol en el script y se usa la implementación especificada allí. No presenten «Huber» como una única respuesta inequívoca si no registran cómo se calculó.

Construimos ocho niveles simulados, desde $20$ hasta $370$ nmol/mol. Los valores sin alteración se generaron alrededor de una recta de pendiente $1,002$, con pequeñas diferencias deterministas, documentadas en el código. Para que podamos estudiar influencia, alteramos intencionalmente la última respuesta: en ese nivel, el valor simulado inicial es $371,200000$ nmol/mol y la respuesta alterada para esta demostración es $379,200000$ nmol/mol. La alteración de $8,0$ nmol/mol es deliberadamente grande, no fue detectada ni excluida de un archivo de CALAIRE. Es una intervención de enseñanza.

> **[EJEMPLO]** Mostrar las observaciones simuladas, marcando el punto de $x=370$ nmol/mol como «respuesta alterada de forma deliberada para la demostración». Escribir junto al gráfico: «no es un dato de laboratorio ni un criterio de exclusión».

Ajustemos primero OLS a los datos no alterados: obtenemos intercepto $0,49971429$ nmol/mol y pendiente $1,00201429$. Ahora ajustamos OLS después de introducir la alteración: el intercepto pasa a $-1,10028571$ nmol/mol y la pendiente a $1,01534762$. La pendiente aumenta porque el punto de respuesta alta está en el extremo alto del rango y atrae la recta. Con Huber, en los datos alterados y la escala especificada, el intercepto es $0,36428571$ nmol/mol y la pendiente $1,00314286$. En este ejemplo concreto, la pendiente robusta se mantiene más cerca de la pendiente de la recta de datos no alterados que la pendiente OLS.

Comparar una salida dentro del intervalo también ayuda. A una referencia de $200$ nmol/mol, la predicción OLS del ajuste alterado es $201,969238$ nmol/mol, mientras que la predicción de Huber es $200,992857$ nmol/mol. El residuo en la observación influyente es $4,621667$ nmol/mol con el ajuste OLS y $7,672857$ nmol/mol con Huber.

Que el residuo de Huber sea mayor no significa que el método haya fallado: la recta robusta no se desplaza tanto hacia ese punto, así que deja una discrepancia mayor allí y protege más el patrón global del conjunto. Pero si la observación alta representa un cambio real del sistema, «proteger» el ajuste sería precisamente una respuesta equivocada. La interpretación depende del proceso de medición y de la pregunta.

> **[DIAPOSITIVA]** Una gráfica con datos simulados originales y alterados, rectas OLS antes y después de la alteración y recta Huber. Leyenda completa; no ocultar el punto ni llamarlo «error» sin investigación.

Esta comparación ilustra robustez frente a una observación influyente, no una licencia para retirar observaciones. Primero se investiga si hay una causa asignable y se documenta el resultado. Si no hay causa que justifique excluir el dato, se conserva y se informa el análisis acordado. OLS y Huber responden a criterios de ajuste distintos; sus diferencias pueden revelar sensibilidad, pero ninguna discrepancia por sí sola dicta cuál estimador es verdadero. Si la finalidad normativa o el procedimiento validado especifica un estimador, no lo cambiamos después de ver qué resultado nos conviene.

Tampoco confundamos resistencia a residuos grandes con resistencia a cualquier problema. Huber no corrige una recta inadecuada, una tendencia no modelada, heterocedasticidad severa, dependencia ignorada o un cambio de escala.

Tampoco es necesariamente resistente a puntos de alto apalancamiento en las abscisas: un punto extremo en $x$ puede influir en la geometría del ajuste aun cuando se limite el peso por su residuo. En nuestro ejemplo el punto de la respuesta alterada está en el extremo del intervalo de referencias; por ello, no generalicen el resultado a cualquier observación influyente.

El método, la escala, los supuestos, el diagnóstico y el rango de aplicación deben quedar documentados.

> **[ERROR CRÍTICO]**

No elijan Huber porque entregue una pendiente más conveniente. No eliminen el dato para que OLS y Huber coincidan. No informen una recta robusta sin declarar el estimador, la escala usada y qué observaciones entraron en el cálculo.

> **[ESCALAMIENTO]**

Detengan el reporte y pidan revisión técnica si una observación influyente puede ser un cambio real, si OLS y Huber llevan a decisiones distintas, si el patrón está fuera del rango de calibración, si hay varios puntos influyentes o si la conclusión depende de una escala de Huber no justificada. En esos casos se requiere revisar el modelo y el proceso, no escoger silenciosamente el resultado que parezca más estable.

Noten también que el ejemplo define a propósito una comparación pareada de métodos: mismas abscisas, mismas respuestas alteradas y mismo uso, con la única diferencia de la función objetivo. Eso hace interpretable el contraste de sensibilidad. Si cambiáramos simultáneamente los datos, el rango, el modelo o la escala robusta, no sabríamos qué produjo la diferencia. En una validación de software, documentar estas decisiones es tan importante como guardar el coeficiente final. La implementación debe tener comprobaciones sobre datos representativos, y la sensibilidad a la escala debe evaluarse según el uso previsto, no tras elegir la salida más favorable.

No confundan «observación influyente» con «valor atípico» como si fueran etiquetas equivalentes. La influencia habla de cuánto puede cambiar un ajuste al incluir una observación; la causa del valor y su compatibilidad con el proceso son preguntas distintas. Un punto puede ser influyente y correcto, por ejemplo si representa un nivel extremo que el diseño debe cubrir. Un residuo grande puede deberse a un error de registro, pero también a un cambio del proceso o a una relación no lineal que el modelo no describe. Huber reduce el efecto de residuos grandes dentro de la función objetivo; no determina cuál de esas explicaciones es verdadera. Esa separación protege el análisis contra la eliminación automática de datos y contra el uso mecánico de un método robusto.

Antes de cerrar, hagamos una verificación común para cualquier salida numérica. Pregunten si la entrada representa la magnitud que dice representar; si la unidad se conservó en cada operación; si los signos y la convención de corrección se mantienen; si la dependencia fue representada; si los supuestos del método coinciden con el diseño; si la implementación puede reproducirse; y si la incertidumbre reportada responde a la pregunta del usuario. Un resultado con muchas cifras decimales no es necesariamente preciso, y una corrida que termina sin error no demuestra que el modelo sea apropiado.

> **[PIZARRA]** Lista de cierre narrada: mensurando y modelo; datos y origen; dependencia; unidad de análisis; método y supuestos; comprobaciones; incertidumbre; interpretación y acción.
>
> **[PAUSA]** Dar tiempo para que el grupo compare esta lista con las decisiones tomadas en las escenas.

En Monte Carlo, una comprobación independiente puede ser comparar con la aproximación lineal en el régimen donde esperamos que funcione, y revisar la estabilidad de los resúmenes numéricos. En salidas múltiples, verificamos el orden del vector, las dimensiones y propiedades de la matriz, además de una salida individual recalculada. En bootstrap, verificamos que cada réplica conserve la unidad independiente y los bloques. En Huber, registramos la especificación exacta y comparamos con OLS como análisis de sensibilidad, sin transformar esa comparación en un criterio de selección posterior al resultado.

Hay señales que nos obligan a detenernos. Si no tenemos base para las distribuciones o covarianzas, no fingimos que la simulación las conoce. Si las salidas posteriores necesitan covarianza y la herramienta solo entrega incertidumbres individuales, no usamos la herramienta como si bastara. Si el diseño no permite identificar la unidad de remuestreo o deja muy pocas unidades independientes, no presentamos un intervalo bootstrap como solución automática. Si la estimación cambia materialmente entre OLS y Huber, investigamos la observación y el modelo antes de reportar. Y si la respuesta que necesitamos queda fuera del intervalo para el que se validó la calibración, no extrapolamos silenciosamente.

> **[ESCALAMIENTO]**

Escalen al responsable técnico cuando la conclusión dependa de una dependencia desconocida, de una distribución de entrada no sustentada, de un intervalo numérico inestable, de una matriz de covarianza inadmisible, de un diseño con pocos bloques, de un ajuste sensible a una observación sin causa aclarada o de una predicción fuera del rango validado. La señal de escalamiento no es una solución estadística; es la decisión correcta de no sobreinterpretar los datos.

> **[TRANSICIÓN]** M13 concluye el contenido de métodos numéricos. Las deducciones asociadas a la propagación, a la covarianza de parámetros y a Monte Carlo quedan remitidas a los anexos correspondientes.

> **[PRÁCTICA — fase de ejercicios]** Práctica integradora evaluable de métodos numéricos

## Cierre del capítulo

Cerremos con la competencia de este módulo. Ustedes deben poder contrastar la propagación lineal con Monte Carlo y decidir cuál es adecuado para el modelo inverso y el uso previsto; representar pendiente, intercepto y correcciones como salidas conjuntas, con su covarianza; remuestrear unidades que respetan los bloques del diseño; y comparar OLS con Huber ante una observación influyente, explicando los supuestos y los límites de esa comparación. Con esta base, pasaremos al taller integrador de nivel A, donde se articularán los contenidos del curso.

Ninguno de estos métodos elimina la obligación de entender los datos. Monte Carlo propaga distribuciones, pero no arregla entradas mal caracterizadas. La matriz de covarianza conserva dependencia, pero no identifica por sí sola su causa. Bootstrap refleja el diseño solo si se remuestrea la unidad correcta, y no genera información experimental nueva. La regresión robusta reduce la influencia de ciertos residuos grandes, pero no demuestra que un valor sea erróneo, no reemplaza el diagnóstico y no protege frente a toda forma de mala especificación. Esa es la decisión estadística que nos llevamos: elegir el cálculo por la pregunta, por la estructura de los datos y por los supuestos que podemos defender.

Cuando entreguen una salida de estos métodos, acompañen la cifra con la versión del modelo, la procedencia de las entradas, el método numérico, la unidad y la cobertura o el intervalo que corresponda. En un análisis con varias salidas, informen además qué orden sigue el vector y qué matriz se usó. En bootstrap, nombren la unidad de remuestreo y el tipo de intervalo; en Huber, registren la función y su escala. La reproducibilidad es parte de la interpretación estadística: otra persona debe poder entender qué se calculó, bajo qué hipótesis y por qué esa respuesta sirve para la decisión planteada.

Los ejemplos de este capítulo fueron simulados y todos sus valores están reproducidos por `calc/M13_ejemplos.py`. No constituyen evaluaciones del SRP 55, del Level 2 ni de una calibración real del laboratorio. Para usar estos métodos en resultados oficiales se requiere una implementación validada, entradas justificadas, revisión del alcance y la autorización técnica correspondiente.

## Referencias del capítulo

- **GUM.** JCGM 100:2008 (ISO/IEC Guide 98-3:2008), *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*. `docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ … (GUM_1995) - libgen.li.pdf`; numerales 5.1.2 y 5.2.2 verificados con `pdftotext`.
- **GUM-S1.** JCGM 101:2008, *Evaluation of measurement data — Supplement 1 to the Guide to the expression of uncertainty in measurement — Propagation of distributions using a Monte Carlo method*, con corrigendum 1:2009. `docs/ISO_IEC Guide 98-3_2008 Suppl.1_2008 - libgen.li.pdf`; numerales citados verificados con `pdftotext`.
- **GUM-S2.** JCGM 102:2011, *Evaluation of measurement data — Supplement 2 to the Guide to the expression of uncertainty in measurement — Extension to any number of output quantities*. `docs/ISO_IEC Guide 98-3_2008 Suppl.2_2011 - libgen.li.pdf`; numerales citados verificados con `pdftotext`.
- **ISO 28037.** ISO/TS 28037:2010, *Determination and use of straight-line calibration functions*. `docs/ISO 28037.pdf`; cláusula 10 verificada con `pdftotext`.
- **Efron y Tibshirani.** Efron, B. y Tibshirani, R. J. *An Introduction to the Bootstrap*. Chapman & Hall, 1993. No disponible en `docs/`; se cita sin numeral; referencia externa pendiente de verificación bibliográfica local.
- **Huber.** Huber, P. J. *Robust Statistics*. Wiley, 1981. No disponible en `docs/`; se cita sin numeral; referencia externa pendiente de verificación bibliográfica local.

