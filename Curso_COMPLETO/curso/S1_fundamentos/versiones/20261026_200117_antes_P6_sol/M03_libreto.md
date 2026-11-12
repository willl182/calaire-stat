# M03. Probabilidad, distribuciones y dependencia

## Ficha del capítulo

| Elemento | Descripción |
|---|---|
| Competencia estadística | Asignar distribuciones a entradas, convertir especificaciones en incertidumbres estándar y saber cuándo promediar reduce la incertidumbre. |
| Prerrequisitos | M1: modelo de medición, entradas y lecturas del SRP. M2: centro, dispersión, diferencia entre una lectura y un resumen. |
| Nivel B | Variable aleatoria; distribuciones normal, rectangular y triangular; semiamplitud frente a resolución; conversión de incertidumbre expandida; desviación de lectura y de promedio; distribución t, cuantiles y grados de libertad; límite de la reducción por promedio cuando hay componente común o deriva. |
| Nivel I añade | Covarianza y correlación; varianza de combinaciones lineales; distribuciones chi-cuadrado y F; gráficos de probabilidad; dependencia temporal y separación de variación de corto plazo y entre días. |
| Nivel A añade | Covarianzas comunes entre canales y puntos; autocorrelación; manejo operativo de matrices y bloques de covarianza: unidades, simetría y admisibilidad. |
| Datos | Ejemplos sintéticos con magnitudes declaradas: **simulados**, solo para enseñar cálculos; no describen resultados de CALAIRE. Resolución de 0,1 nmol/mol: entrada hipotética **simulada**, no una especificación del 49C ni del SRP. |
| Anexos | AX.2: varianza de combinaciones lineales y propagación con covarianza. AX.3: varianzas de rectangular y triangular. |
| Referencias clave | Hahs-Vaughn; MMU; Crowder 2020; GUM; GUM-S2; NIST/SEMATECH. Ubicaciones con numeral se incluyen solo cuando se pudieron comprobar en `docs/`. |

## Nivel B — lo que necesitan para interpretar una lectura

En este nivel vamos a añadir una idea sencilla pero poderosa: una lectura no es siempre un número fijo que se repite exactamente. Si repetimos una medición bajo condiciones que consideramos comparables, el resultado puede variar. La probabilidad nos ayuda a describir esa variación antes de saber qué valor aparecerá en la siguiente lectura. No sustituye el modelo de medición de M1 ni la descripción de M2. Nos permite hablar de posibles resultados y de sus patrones. [Hahs-Vaughn §5.1; MMU §3.2.1]

### Escena B1. De una repetición a un modelo de probabilidad

> **[DIAPOSITIVA]** Una secuencia de lecturas hipotéticas de un nivel del Level 2. Rotular: «datos simulados para enseñanza; no son resultados de CALAIRE».

«Imaginen que, con el mismo procedimiento, la misma concentración y el mismo patrón, observamos una lectura tras otra. Antes de la próxima lectura no sabemos el número exacto. Sí sabemos qué resultados son posibles y qué tan plausibles son según el modelo que usemos. A ese proceso de asignar probabilidades a resultados lo llamamos modelar la variabilidad.»

«La probabilidad de un evento está entre cero y uno. Un evento imposible tiene probabilidad cero, pero la recíproca no vale en general: un punto exacto de una variable continua puede tener probabilidad cero sin ser un valor imposible. Probabilidad uno significa casi seguro bajo el modelo. Para resultados discretos exhaustivos y mutuamente excluyentes, la suma de sus probabilidades es uno; para una densidad continua, el área total es uno. La palabra importante es “dentro del modelo”. Una probabilidad pequeña no demuestra que algo sea imposible ni identifica por sí sola una causa física.» [MMU §3.2.1]

«Una medición anómala puede ser señal de un cambio, de una condición no registrada o de una limitación del modelo; no es una invitación automática a borrar el dato. Hoy no vamos a probar hipótesis ni a declarar atípicos: eso se trata después y requiere un procedimiento apropiado.»

> **[EJEMPLO]** Modelo hipotético simulado de un ciclo: $X=0$ si la lectura queda dentro de banda y $X=1$ si queda fuera. Se suministran $P(X=0)=0,9$ y $P(X=1)=0,1$.

«La variable asigna un número a cada uno de los dos resultados definidos. Sumamos 0,9 y 0,1 y obtenemos uno: hemos incluido todos los resultados de este modelo discreto. No estamos estimando frecuencias del laboratorio ni introduciendo aquí otra familia de distribuciones.» [MMU §3.2.1; comprobación: `calc/M03_ejemplos.py`]


«Ahora introduzco variable aleatoria. Es una regla que asigna un número a cada resultado posible del proceso aleatorio que hemos definido. Si contamos cuántas veces ocurre una alarma en una secuencia fija, el resultado es discreto: puede ser cero, uno, dos y así sucesivamente. Si observamos una magnitud como una indicación, la modelamos normalmente como continua dentro de la resolución pertinente, aunque el instrumento guarde números redondeados o cuantizados. La decisión de modelarla como continua o discreta depende de la pregunta y de la escala de los datos.» [MMU §3.2.1]

«Para una variable discreta, describimos la probabilidad asociada a cada valor. Para una variable continua usamos una densidad. La densidad no es la probabilidad de un punto exacto; la probabilidad corresponde al área bajo la densidad en un intervalo. La función de distribución acumulada responde otra pregunta: cuál es la probabilidad de obtener un resultado menor o igual que un límite. En el trabajo diario, un intervalo o una cola de distribución suele ser más útil que la densidad en un punto.» [MMU §3.2.3]

> **[PIZARRA]** $F(x)=P(X\leq x)$; para variable continua, $P(a<X\leq b)=\int_a^b f(x)\,dx$.

«Lo leo en voz alta: efe de equis es la probabilidad de que la variable X sea menor o igual que equis. Para una variable continua, la probabilidad de quedar entre a y b es el área de la densidad entre esos límites. El área total de una densidad sobre todos los resultados posibles es uno.»

«El valor esperado es el centro de largo plazo que describe la distribución. La varianza mide la dispersión cuadrática alrededor de ese valor esperado; su raíz cuadrada vuelve a las unidades originales y se llama desviación estándar. No confundan estos parámetros del modelo con los estadísticos que calculamos de una muestra. La media y la desviación estándar de una muestra estiman características de una población o proceso, con limitaciones que veremos en inferencia.» [MMU §3.2.4]

> **[PREGUNTA AL GRUPO]** Si la indicación esperada es 420 nmol/mol y la desviación estándar de lectura es 0,8 nmol/mol, ¿significa eso que cada lectura queda exactamente entre 419,2 y 420,8? — *Respuesta esperada:* no; la desviación estándar describe escala de dispersión, no un límite absoluto ni una garantía para cada lectura.

«Exacto. Una desviación estándar no es un máximo ni un intervalo con cobertura garantizada. Para asignar probabilidades a intervalos necesitamos también un modelo de distribución y sus parámetros. Eso nos lleva a las distribuciones que usaremos.»

### Escena B2. Distribuciones que aparecen en la fotometría

«Empezamos con la distribución normal. Su forma es simétrica y con un solo máximo, centrado en su media. En la normal, la media, la mediana y el valor más frecuente coinciden. La normal estándar tiene media cero y desviación estándar uno; al estandarizar una variable normal, expresamos su distancia al centro en unidades de desviación estándar. Es útil para representar errores agregados de muchas pequeñas contribuciones y para aproximar ciertos resultados, pero no se declara normal una serie solo porque el histograma parezca una campana.» [Hahs-Vaughn §4.1]

> **[PIZARRA]** $Z=(X-\mu)/\sigma$.

«Leo: Z es X menos su media, dividido por su desviación estándar. Si X es normal, Z sigue la normal estándar. La operación cambia la escala, no elimina las causas de variación ni arregla una dependencia.»

> **[EJEMPLO]** Distribución normal simulada con media 420,0 nmol/mol y desviación estándar 0,8 nmol/mol.

«Una lectura de 421,6 está dos desviaciones estándar por encima de la media de este ejemplo, porque la diferencia de 1,6 se divide por 0,8. Eso permite ubicarla en la escala normal estándar. No vamos a convertir aquí esa distancia en una probabilidad tabulada: basta distinguir que el cálculo describe la posición respecto del modelo y que el ejemplo es simulado.»

«La distribución rectangular es adecuada cuando, por la información disponible, todos los valores dentro de un intervalo se tratan como igualmente plausibles. Si el intervalo va desde el centro menos h hasta el centro más h, h es la semiamplitud. La desviación estándar de esa distribución es h dividido por la raíz de tres. Si el fabricante declara resolución total δ entre pasos, y el error de redondeo se representa entre menos δ/2 y más δ/2, la semiamplitud es δ/2 y la incertidumbre estándar resulta δ dividido por la raíz de doce. No son dos fórmulas intercambiables con la misma entrada: una usa semiamplitud y otra usa resolución total. La deducción de estas expresiones está en el Anexo AX.3; aquí las aplicamos.» [MMU §§3.2.5.1–3.2.5.2]

> **[PIZARRA]** Rectangular con semiamplitud $h$: $u=h/\sqrt{3}$. Cuantización con resolución total $\delta$: $u=\delta/\sqrt{12}$.

«Leo: u igual a h sobre raíz de tres; o, para un intervalo de cuantización cuya anchura completa es delta, delta sobre raíz de doce. Escribir qué representa cada símbolo es parte del cálculo.»

> **[EJEMPLO]** Ejemplo simulado de tolerancia uniforme: la entrada se conoce dentro de ±0,3 nmol/mol. Segundo ejemplo simulado: se supone una resolución total de 0,1 nmol/mol, sin atribuirla a un instrumento real.

«Para el primer caso h vale 0,3. Al dividirlo por raíz de tres obtenemos una incertidumbre estándar de aproximadamente 0,173 nmol/mol. En el segundo caso δ vale 0,1. Al dividirlo por raíz de doce obtenemos aproximadamente 0,0289 nmol/mol. Los valores se calcularon con el script M03. Noten cómo cambia el resultado si se confunde la resolución completa con su semiamplitud. Ambas entradas son hipotéticas y simuladas: no son lecturas ni especificaciones confirmadas de CALAIRE. Una aplicación real necesitaría la resolución documentada del equipo.» [MMU §§3.2.5.1–3.2.5.2; `calc/M03_ejemplos.py`]

«La distribución triangular también describe una entrada limitada a un intervalo, pero asigna mayor plausibilidad a valores cercanos al centro y menor a valores próximos a los extremos. Si la semiamplitud es h y la forma es triangular simétrica, su incertidumbre estándar es h dividido por raíz de seis. La forma de la distribución expresa información adicional: no se selecciona solo porque produzca una incertidumbre menor.» [MMU §3.2.5.2]

> **[PIZARRA]** Triangular simétrica con semiamplitud $h$: $u=h/\sqrt{6}$.

«Para h igual a 0,3 nmol/mol, la desviación estándar es aproximadamente 0,122 nmol/mol. La amplitud del intervalo no cambió respecto del ejemplo rectangular; lo que cambió fue la distribución asignada dentro de él. Esa elección necesita una justificación sobre la información disponible, no una preferencia por un número más pequeño.» [Cálculo: `calc/M03_ejemplos.py`]

«En el certificado puede aparecer una incertidumbre expandida U. Para volver a la incertidumbre estándar u, usamos u igual a U dividido por k, siempre que el factor k corresponda a la declaración que estamos interpretando. U es la incertidumbre expandida reportada, no una segunda desviación estándar. El factor no se inventa ni se toma automáticamente como dos: se declara y se justifica en el contexto del resultado.» [GUM §4.3.3; §6.2.1]

> **[ERROR CRÍTICO]** «No confundan U con u. U es la incertidumbre expandida y u la estándar. Cambiar entre ambas sin declarar k da un resultado mal reportado.»

> **[PIZARRA]** $u=U/k$.

«Con U igual a 0,60 nmol/mol y k igual a 2, como ejemplo explícitamente supuesto, u es 0,30 nmol/mol. Este ejemplo sirve solo para practicar la conversión. No concluyan que k es siempre dos ni que una cobertura determinada queda demostrada sin revisar el modelo, la distribución y los grados de libertad.» [Cálculo: `calc/M03_ejemplos.py`]

### Escena B3. Una lectura, un promedio y la distribución t

«Ahora vamos a separar tres objetos que con frecuencia se mezclan. Primero, la dispersión de lecturas individuales. Segundo, la variación del promedio de varias lecturas. Tercero, un componente que todas esas lecturas comparten, como una referencia común o una deriva persistente. Promediar puede reducir la parte independiente de lectura; no borra automáticamente lo común.» [GUM §4.2.3; §5.2]

«Supongan que cada lectura independiente tiene desviación estándar σ. Para el promedio de n lecturas independientes, la desviación estándar del promedio es σ sobre raíz de n. La división no cambia la dispersión de cada lectura: cambia la dispersión de los promedios que se obtendrían al repetir grupos de n observaciones. La independencia es la condición importante. Ocho lecturas consecutivas no son ocho réplicas independientes por el mero hecho de estar en ocho filas.»

> **[PIZARRA]** $u(\bar X)=\sigma/\sqrt{n}$ si las lecturas son independientes; para una desviación muestral estimada $s$, el error estándar estimado es $s/\sqrt{n}$.

«Leo: u de la media es sigma sobre raíz de n; si la desviación se estima con s, el error estándar estimado es s sobre raíz de n. Esta última no significa que la incertidumbre de cualquier resultado de promedio sea s sobre raíz de n: antes debemos precisar cuál es el resultado, qué se repite y a qué horizonte temporal queremos generalizar.» [GUM §4.2.3, ecuación (5), y §4.2.7]

> **[EJEMPLO]** Lecturas simuladas con desviación estándar de 0,8 nmol/mol; promedio de 16 lecturas independientes.

«La desviación de una lectura sigue siendo 0,8 nmol/mol. La desviación estándar del promedio, bajo independencia, es 0,8 dividido por raíz de 16, es decir, 0,20 nmol/mol. No hemos reducido la variabilidad de una lectura individual. Hemos reducido la variabilidad que se esperaría entre promedios de dieciséis lecturas independientes.» [Cálculo: `calc/M03_ejemplos.py`]

«Añadamos ahora un efecto común a las dieciséis lecturas, con desviación estándar 0,3 nmol/mol, independiente del ruido individual de 0,8. Suponemos ruido independiente entre lecturas y componentes centradas. La varianza del promedio es la varianza del componente común más la varianza del ruido individual dividida por dieciséis. La incertidumbre estándar del promedio queda en aproximadamente 0,361 nmol/mol. Sin componente común era 0,20; con él no puede bajar por debajo de 0,30 al aumentar el número de lecturas. A medida que el ruido de lectura se promedia, queda el piso común.» [Cálculo: `calc/M03_ejemplos.py`; fórmula de la varianza con dependencia, ver AX.2]

> **[ERROR CRÍTICO]** «No dividan por raíz de n la incertidumbre completa sin separar qué componentes son independientes y cuáles comparten todas las lecturas. Un componente común, una deriva o un sesgo no desaparecen por promediar.»

«La deriva temporal es un caso especialmente importante. Si las lecturas sucesivas se desplazan lentamente, leer muchas veces en una secuencia puede añadir menos información que tomar observaciones separadas en el tiempo. La cantidad de filas no define por sí sola cuántas observaciones independientes tenemos. En nivel B, si sospechan dependencia no contemplada o deriva, deténganse y consulten; en nivel I estudiaremos cómo reconocer y modelar esa estructura.»

«Por último, necesitamos la distribución t de Student. La usamos como referencia para inferir sobre una media cuando la desviación poblacional es desconocida y se estima a partir de una muestra, bajo supuestos que revisaremos en M4. La t tiene forma simétrica y colas más pesadas que la normal estándar para pocos grados de libertad. A medida que aumentan los grados de libertad, sus cuantiles se acercan a los de la normal. Los grados de libertad describen cuánta información independiente contribuye a estimar una variabilidad; no son simplemente el número de lecturas copiadas de una tabla.» [GUM §§G.3.2–G.3.4; Hahs-Vaughn §6.1]

> **[PIZARRA]** $t=(\bar{x}-\mu_0)/(s/\sqrt{n})$; $\nu=n-1$ para una muestra independiente de una misma población normal con varianza desconocida; la referencia t central corresponde a una media poblacional igual a $\mu_0$.

«Leo: t es la diferencia entre la media observada y el valor de referencia, dividida por el error estándar estimado. En el ejemplo elemental de n observaciones independientes, los grados de libertad son n menos uno. En diseños agrupados, temporales o con componentes de varianza, esa cuenta directa puede ser incorrecta. M4 enseña los intervalos y pruebas; aquí nos basta entender por qué aparecen t, sus cuantiles y los grados de libertad.»

> **[EJEMPLO]** En una muestra simulada de cinco lecturas independientes, los grados de libertad del modelo elemental de una media son cuatro.

«No calculamos un intervalo de confianza en esta escena. Solo observamos que, si la desviación estándar del proceso no se conoce y se estima con cinco observaciones independientes, la referencia t tiene cuatro grados de libertad. Para un cuantil bilateral central del 95 %, el cuantil t con cuatro grados de libertad es aproximadamente 2,776, mientras que el cuantil normal correspondiente es aproximadamente 1,960. Con pocos grados de libertad el cuantil de t es mayor, reflejando la incertidumbre adicional de estimar la dispersión. El intervalo concreto y su interpretación corresponden a M4-B.» [Cálculo de cuantiles: `calc/M03_ejemplos.py`]

> **[PREGUNTA AL GRUPO]** Si se duplica el número de lecturas pero persiste una deriva común, ¿se reduce a la mitad la incertidumbre total del promedio? — *Respuesta esperada:* no; solo disminuye la parte que el modelo considera independiente, y una componente común puede permanecer.

«Exactamente. La reducción ideal es con la raíz cuadrada, no con el número de lecturas, y solo aplica a la parte independiente.»

> **[PRÁCTICA — fase de ejercicios]** Convertir especificaciones del certificado en incertidumbres estándar y comparar el promedio de datos independientes con el de una serie con deriva.

### Señales de escalamiento del nivel B

«Antes de seguir, dejemos claras las señales para detenerse. Si dos entradas comparten una fuente de variación y la plantilla no contempla esa dependencia, no supongan independencia. Si la serie muestra cambio de escala, deriva o residuos con estructura, el promedio simple puede ocultar la estructura. Si ven un dato inusual sin causa documentada, no lo eliminen para acercar el resultado a lo esperado. Si la incertidumbre en ambos ejes resulta relevante, el ajuste básico con referencia fija no es suficiente: escalen el análisis. Si hay pocos grados de libertad, una cobertura o una decisión próxima a un límite, consulten a quien tenga la responsabilidad técnica. Si las observaciones son temporales y consecutivas, no las llamen independientes sin evidencia.»

> **[ESCALAMIENTO]** «Detener el cálculo básico y consultar cuando haya dependencia no contemplada, cambio de escala, atípico sin causa, residuos con estructura, incertidumbre relevante en ambos ejes, dependencia temporal, grados de libertad limitados o una decisión cercana a un límite. Registrar qué supuesto falla o qué información falta; no corregirlo borrando observaciones.»

«Estas señales no son un reemplazo de la formación de niveles I y A. Son el punto en que el operador de B reconoce el límite de la plantilla y protege la validez del resultado.»

## Nivel I — lo que se añade

En B hemos representado una entrada por su propia distribución y hemos visto que promediar no siempre elimina toda variación. En I añadimos la dependencia entre entradas y entre observaciones, porque en calibración dos valores pueden compartir el mismo patrón y dos lecturas próximas pueden arrastrar parte del mismo ruido. A partir de aquí, una suma o una diferencia ya no se calcula ignorando automáticamente cómo se relacionan sus términos.

### Escena I1. Covarianza y correlación: qué se cancela y qué se suma

«La covarianza mide cómo dos variables se mueven juntas respecto de sus medias. Si cuando X está por encima de su media Y suele estar también por encima, la covarianza tiende a ser positiva. Si una suele estar por encima mientras la otra queda por debajo, tiende a ser negativa. Una covarianza cercana a cero indica ausencia de asociación lineal en el modelo, pero no demuestra independencia en general.» [Crowder 2020 §7.4.1]

«La covarianza depende de las unidades de X y de Y. Para expresar la asociación en una escala sin unidades usamos la correlación: covarianza dividida por el producto de las desviaciones estándar. La correlación queda entre menos uno y uno. El signo indica la dirección lineal y la magnitud describe cuán fuerte es esa asociación lineal. Una correlación no identifica una causa y tampoco describe por sí sola relaciones no lineales.» [Crowder 2020 §7.4.1]

> **[PIZARRA]** $\operatorname{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])]$; $\rho_{XY}=\operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)$.

«Leo: la covarianza es la esperanza del producto de las desviaciones de X e Y respecto de sus medias. La correlación es esa covarianza dividida por ambas desviaciones estándar. Si una de las desviaciones es cero, la correlación no está definida porque no hay variación que normalizar.»

«La esperanza de una combinación lineal se obtiene combinando las esperanzas con los mismos coeficientes. Para la varianza necesitamos más cuidado: la varianza de una suma incluye la covarianza. Esa es la razón estadística de que una causa compartida pueda aumentar o disminuir la incertidumbre de un resultado. La demostración algebraica queda en el Anexo AX.2; aquí la usaremos.» [Crowder 2020 §7.2]

> **[PIZARRA]** $E[aX+bY]=aE[X]+bE[Y]$; $\operatorname{Var}(aX+bY)=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y)+2ab\operatorname{Cov}(X,Y)$.

«Leo la segunda expresión: la varianza de a X más b Y es a al cuadrado por la varianza de X, más b al cuadrado por la varianza de Y, más dos a b veces la covarianza. Si usamos una diferencia, el coeficiente de una de las variables es negativo. Por eso el término de covarianza cambia de signo.»

> **[EJEMPLO]** Dos entradas simuladas con desviaciones estándar 0,8 y 0,6 nmol/mol y correlación 0,75. La covarianza es 0,36 (nmol/mol)².

«Multiplicamos la correlación, 0,75, por las dos desviaciones, 0,8 y 0,6. Obtenemos una covarianza de 0,36. Si sumamos las entradas ignorando su relación, la desviación estándar de la suma resulta 1,00. Al incluir la covarianza positiva, la desviación estándar de la suma aumenta a aproximadamente 1,31. Para la diferencia de las mismas dos entradas, el término positivo se resta y la desviación estándar baja a aproximadamente 0,529. No significa que la diferencia siempre tenga menos incertidumbre. Significa que una fluctuación común se cancela parcialmente en esta diferencia, mientras que se suma en la suma.» [Cálculo: `calc/M03_ejemplos.py`; deducción en AX.2]

«Pensemos ahora en dos resultados de concentración que se apoyan en el mismo patrón. Una variación del patrón puede mover ambos resultados de forma parecida. Al estudiar la diferencia entre ellos, ese efecto común puede cancelarse en parte. Pero esa cancelación solo puede cuantificarse si conocemos la covarianza o un modelo que la produzca. La palabra “comparten” no nos da por sí sola el valor numérico.»

> **[ERROR CRÍTICO]** «No calculen la incertidumbre de una diferencia por suma cuadrática suponiendo independencia cuando los dos resultados comparten el SRP 55 u otra entrada. Primero identifiquen y justifiquen la dependencia.»

«Para el promedio de variables correlacionadas también cambia la regla. Si cada lectura tiene la misma varianza y todas las parejas tienen una correlación positiva, las observaciones redundan en parte: el promedio mejora menos que lo que predice la regla de independencia. Con correlación negativa puede ocurrir lo contrario dentro de los límites que admite una matriz válida. Por eso no aplicamos s sobre raíz de n de forma automática a una secuencia dependiente.»

> **[PIZARRA]** Para variables $X_i$: $\operatorname{Var}(\sum_i c_iX_i)=\sum_i c_i^2\operatorname{Var}(X_i)+2\sum_{i<j}c_ic_j\operatorname{Cov}(X_i,X_j)$.

«La regla de la varianza de una combinación lineal se generaliza sumando cada varianza con el cuadrado de su coeficiente y agregando dos veces cada covarianza de parejas distintas. El Anexo AX.2 contiene la derivación. En las hojas de cálculo, el signo de cada coeficiente importa: una diferencia y una suma no comparten el mismo término de covarianza.»

### Escena I2. Chi-cuadrado, F y gráficos de probabilidad

«En B usamos la forma de una distribución para representar una entrada. En I veremos dos distribuciones más que aparecen cuando describimos variabilidad estimada y comparamos escalas de variación: chi-cuadrado y F. La distribución chi-cuadrado se construye a partir de cuadrados de variables normales estándar independientes. Sus valores son no negativos y su forma depende de los grados de libertad. La distribución F es el cociente de dos cantidades chi-cuadrado independientes entre sí, cada una escalada por sus propios grados de libertad. También depende de esos grados de libertad y toma valores no negativos.» [Hahs-Vaughn §§8.2 y 9.1.1]

«No vamos a ejecutar aquí pruebas de hipótesis sobre varianzas; eso corresponde a M4-I. Para M3 necesitamos saber qué distribuciones son, por qué sus cuantiles dependen de grados de libertad y reconocer que tienen soporte positivo y normalmente una forma asimétrica, en especial con pocos grados de libertad. En ANOVA, la distribución F permitirá estudiar cocientes de cuadrados medios en M6. No anticipamos la prueba ni sus condiciones.»

> **[PIZARRA]** $\chi^2_\nu=\sum_{i=1}^{\nu} Z_i^2$ para $Z_i$ normales estándar independientes; $F_{\nu_1,\nu_2}=(\chi^2_{\nu_1}/\nu_1)/(\chi^2_{\nu_2}/\nu_2)$.

«Leo: chi cuadrado con nu grados de libertad es la suma de nu cuadrados de variables normales estándar independientes. F con ν₁ y ν₂ grados de libertad es el cociente de dos chi cuadrados, cada uno dividido por su grado de libertad. Para obtener la distribución F, las dos cantidades chi-cuadrado también deben ser independientes entre sí. Estas representaciones explican por qué se usan para cantidades de variación estimada y cocientes de variaciones.»

> **[EJEMPLO]** Ejemplo esquemático de chi-cuadrado con dos grados de libertad: si las dos variables normales estándar observadas son 1 y −1, la suma de cuadrados vale 2. Para F, si los valores de chi-cuadrado son 6 con 3 grados de libertad y 4 con 2 grados de libertad, el cociente de cuadrados medios vale 1.

«En el primer cálculo sumamos uno al cuadrado y menos uno al cuadrado: obtenemos dos. En el segundo, seis dividido por tres es dos y cuatro dividido por dos también es dos; el cociente es uno. Estos números ilustran la construcción de las distribuciones; no son pruebas de significación ni decisiones sobre los datos del laboratorio.» [Cálculo: `calc/M03_ejemplos.py`]

«¿Cómo comprobamos si una distribución normal es una aproximación razonable para las lecturas de un nivel o para el cero? Empezamos mirando los datos con un histograma y un gráfico de probabilidad normal. En este último ordenamos los valores observados y los comparamos con los cuantiles que corresponderían a una normal. Si los puntos siguen aproximadamente una recta, la normal puede ser plausible para ese conjunto. Curvatura, colas distintas o puntos alejados sugieren revisar el modelo, el proceso o la escala. El gráfico no certifica normalidad ni convierte un pequeño conjunto en evidencia concluyente.» [Crowder 2020 §4.4.3]

> **[EJEMPLO]** Cinco valores simulados ordenados: 418,8; 419,5; 420,0; 420,5; 421,2 nmol/mol. Para las posiciones $(i-0,5)/5$, los cuantiles normales estándar son aproximadamente −1,282; −0,524; 0,000; 0,524; 1,282.

«Comparamos cada lectura ordenada con su cuantil teórico: el menor valor con −1,282, el segundo con −0,524, el central con cero, el cuarto con 0,524 y el mayor con 1,282. Esa pareja de listas da los cinco puntos del gráfico. Son datos simulados para mostrar cómo se construye; no concluimos normalidad con solo cinco valores.» [Cálculo: `calc/M03_ejemplos.py`]

> **[DIAPOSITIVA]** Gráfico de probabilidad normal conceptual, sin datos de laboratorio. Marcar: «alineación aproximada no equivale a prueba ni demuestra independencia».

«Una serie puede parecer normal en su histograma y aun así tener dependencia temporal. Por ejemplo, lecturas que suben y bajan suavemente pueden tener una distribución marginal parecida a una campana, pero no ser independientes en el orden temporal. Por eso el histograma y el gráfico de probabilidad contestan sobre la forma de distribución, no sobre toda la estructura del proceso.»

> **[PRÁCTICA — fase de ejercicios]** Calcular la incertidumbre de una diferencia con y sin covarianza.

### Escena I3. Dependencia temporal y dos escalas de variación

«En una serie temporal, el orden es parte de la información. Si anotamos una lectura cada cierto intervalo, la lectura actual puede depender de la anterior por acondicionamiento, control del flujo, respuesta del fotómetro o deriva. La dependencia temporal se investiga mirando la serie en orden y preguntando si los residuos o desviaciones consecutivas tienden a parecerse. No basta con resumir todas las observaciones como una bolsa sin orden.» [NIST/SEMATECH, «Autocorrelation», no disponible en docs/]

«Distinguimos ahora variación de corto plazo y variación entre días. La primera describe cambios entre lecturas bajo condiciones de corto plazo comparables. La segunda refleja cambios del efecto de día cuando repetimos el procedimiento en jornadas distintas. Si combinamos ambos componentes sin indicar la escala temporal, no podremos responder cuánto varía una lectura dentro del día ni cuánto cambia el promedio de un día a otro.»

> **[PIZARRA]** Modelo didáctico: $X_{dj}=\mu+D_d+\varepsilon_{dj}$; $\operatorname{sd}(D_d)=\tau$; $\operatorname{sd}(\varepsilon_{dj})=\sigma$. $D_d$: efecto de día; $\varepsilon_{dj}$: variación de lectura dentro del día.

«Leo: la observación del día d y la lectura j es la media general más un efecto de ese día más un error de lectura. La desviación estándar del efecto diario es tau y la del error de lectura es sigma; sus estimadores se anotan s_entre y s_r, respectivamente. Para este cálculo suponemos efectos de día centrados, independientes entre días, y errores de lectura centrados, independientes entre sí e independientes de los efectos de día. Este modelo ilustra dos escalas, no introduce aquí el procedimiento ANOVA de M6. Si promediamos varias lecturas del mismo día, se reduce la parte de lectura independiente; el efecto de día no se reduce al repetir dentro de ese día. Para caracterizar la precisión de uso en días distintos necesitamos observaciones en varios días.»

> **[EJEMPLO]** Datos simulados: desviación estándar dentro de una jornada de 0,8 nmol/mol; efecto común de jornada de 0,3 nmol/mol; 16 lecturas por jornada.

«Ya vimos el cálculo: la contribución de lectura al promedio de la jornada baja a 0,20 nmol/mol, mientras que la variación entre jornadas permanece en 0,30. La desviación estándar total del promedio de jornada, al combinar ambas partes independientes del modelo, es aproximadamente 0,361 nmol/mol. Si reportamos solo la dispersión intradía, responderemos una pregunta distinta de la que responde la variabilidad de promedios diarios. Los valores son simulados y no describen el Level 2.» [Cálculo: `calc/M03_ejemplos.py`]

«En la práctica, usen el tiempo y el diseño como parte de la descripción del resultado. ¿Es una lectura, un promedio de ciclo, un promedio de jornada o una predicción para otra fecha? ¿Las observaciones se tomaron en el mismo día o en días distintos? En M6 se estimarán componentes para los diseños indicados; por ahora, el objetivo es no confundir esas variaciones.»

> **[ERROR CRÍTICO]** «No sumen un componente entre días y una desviación de promedios diarios si esta última ya contiene ese componente. Identifiquen qué resume cada desviación antes de combinarla.»

«La dependencia temporal también altera los grados de libertad efectivos. Una serie larga no siempre contiene tanta información independiente como indica el número de filas. En este nivel no corregimos mecánicamente una cuenta: reconocemos la estructura, documentamos el orden y escalamos el análisis cuando la dependencia afecta la conclusión.»

### Señales de escalamiento del nivel I

«Si el gráfico temporal muestra dependencia aparente, como rachas, tendencia o ciclos, no supongan que las lecturas son independientes. Si una incertidumbre de diferencia depende de una fuente común, soliciten el modelo o los datos de covarianza. Si el gráfico de probabilidad muestra una estructura que el modelo normal no describe, no oculten esa discrepancia con una prueba elegida por costumbre. Si una estimación combina variación intradía y entre días, asegúrense de que cada componente responde al resultado que se reporta.»

> **[ESCALAMIENTO]** «Pasar a revisión técnica cuando haya dependencia temporal aparente, deriva, estructura por día, dependencia por patrón compartido o una matriz de covarianza necesaria que no esté disponible. No sustituir la información ausente por independencia supuesta.»

## Nivel A — lo que se añade

En B e I ya aprendimos a describir distribuciones, a propagar la varianza con covarianzas y a reconocer dependencia temporal. En A vamos a operar con varias covarianzas al mismo tiempo. Esto es necesario cuando una causa común conecta canales o puntos de concentración, como sucede en modelos de comparación de patrones. No vamos a desarrollar aquí GGMR ni una comparación completa: M7-A y M9-A usarán estas herramientas dentro del alcance establecido.

### Escena A1. Causas comunes entre canales y puntos

«Una covarianza puede aparecer entre dos canales porque comparten una causa: la misma lámpara, el mismo patrón de tiempo, temperatura o presión, o una referencia común. En una razón entre dos canales, una fluctuación común puede cancelarse parcialmente. Si tratamos los canales como independientes, podemos sobreestimar o subestimar la incertidumbre de esa razón. La dirección depende de cómo la entrada se propaga y de los signos de sus sensibilidades.»

«En la fotometría diferencial, la razón entre dos canales incorpora covarianza. Para que el ejemplo numérico sea reproducible y transparente, mostraré un cálculo sintético con canales A y B, incertidumbres y correlación declaradas.»

> **[EJEMPLO]** Ejemplo **simulado** para enseñar propagación de una razón: $A=1,0000$, $B=0,8000$, $u(A)=0,00005$, $u(B)=0,00004$ y correlación entre canales $\rho=0,90$.

«Para una razón R igual a A sobre B, la aproximación de primer orden usa la sensibilidad respecto de A y la sensibilidad respecto de B. La varianza incorpora la covarianza entre ambos canales.»

> **[PIZARRA]** $u^2(A/B)\approx u^2(A)/B^2 + A^2u^2(B)/B^4 - 2A\,\operatorname{Cov}(A,B)/B^3$.

«Leo: la varianza de A sobre B. El primer término es la varianza de A dividida por B al cuadrado. Sumamos A al cuadrado por la varianza de B dividida por B a la cuarta. Después restamos dos A por la covarianza de A y B, dividido por B al cubo. El signo negativo aparece porque en el cociente la sensibilidad respecto de B es negativa. Con los datos simulados, la incertidumbre estándar de la razón con correlación es aproximadamente 0,00002795. Si ignoramos la correlación, obtenemos aproximadamente 0,00008839. La diferencia grande en este ejemplo aparece porque ambos canales tienen correlación positiva alta y la razón resta sus fluctuaciones comunes. Estos resultados son una ilustración del cálculo diferencial, no valores observados ni incertidumbres del SRP 55.» [Cálculo: `calc/M03_ejemplos.py`; aplicación general de la varianza con covarianza, AX.2]

«En sistemas con varios puntos, un componente común puede generar covarianza entre todas las concentraciones, no solo entre canales. Si el mismo factor multiplicativo afecta los puntos, los términos fuera de la diagonal pueden tener una estructura relacionada con el producto de las concentraciones. Esa estructura no se representa con una lista de incertidumbres individuales solamente. Para preservar la información se necesita una matriz de covarianza.»

> **[EJEMPLO]** Dos puntos simulados, 100 y 400 nmol/mol, comparten un factor multiplicativo cuya desviación estándar relativa es 1 %. La matriz de covarianza resultante es $\mathbf V=\begin{bmatrix}1&4\\4&16\end{bmatrix}$ (nmol/mol)².

«La incertidumbre estándar de los dos puntos es 1,0 y 4,0 nmol/mol, y su covarianza es 4,0 (nmol/mol)²; en este modelo la correlación es uno. Al restar el punto de 100 del de 400, la incertidumbre estándar es 3,0 nmol/mol porque el factor común se cancela parcialmente. Si ignoráramos la covarianza, calcularíamos aproximadamente 4,1 nmol/mol. Todo es simulado: ilustra una causa común, no una estructura medida en CALAIRE.» [Cálculo: `calc/M03_ejemplos.py`; AX.2]

> **[PIZARRA]** Para entradas $\mathbf{x}$ y salida localmente lineal $y=f(\mathbf{x})$: $u^2(y)\approx\mathbf{c}^{T}\mathbf{V}\mathbf{c}$ (igualdad si el modelo es lineal), donde $\mathbf{V}$ contiene varianzas y covarianzas y $\mathbf{c}$ las sensibilidades.

«Leo: la varianza de y se aproxima por el vector de sensibilidades transpuesto, multiplicado por la matriz de covarianza y por el vector de sensibilidades. Para un modelo lineal la igualdad es exacta. La diagonal de V contiene varianzas; los elementos fuera de la diagonal son covarianzas. La forma matricial evita olvidar pares, pero no corrige una matriz mal construida. La derivación se reserva para AX.2.» [GUM §5.2.2; Crowder 2020 §§7.2 y 7.4]

«En M9-A, la covarianza de puntos y la referencia común del BIPM-SRP27 se tratarán con la información adecuada para el caso. Aquí no asumimos que una matriz diagonal sea suficiente, ni que exista una cancelación perfecta. Hay que documentar el origen de cada término.»

### Escena A2. Autocorrelación y operación segura con matrices

«La autocorrelación relaciona una serie con versiones desplazadas de sí misma. La correlación de retardo uno compara cada observación con la inmediatamente anterior; la de retardo dos compara observaciones separadas por dos pasos, y así sucesivamente. Una autocorrelación positiva de retardo uno significa que valores altos tienden a ir seguidos de valores altos, y valores bajos de valores bajos, dentro del modelo analizado. No prueba por sí sola una deriva ni identifica su causa. Es una señal para estudiar el proceso temporal y no reducir la incertidumbre como si cada lectura fuera nueva e independiente.» [NIST/SEMATECH, «Autocorrelation», no disponible en docs/]

> **[PIZARRA]** $\rho_k=\operatorname{Corr}(X_t,X_{t-k})$.

«Leo: rho con subíndice k es la correlación entre la lectura en el tiempo t y la lectura k pasos antes. La separación k debe tener significado en el registro: si el intervalo entre lecturas cambió, los retardos no representan necesariamente la misma distancia temporal.»

> **[EJEMPLO]** Secuencia **simulada**, construida de forma determinista en unidades normalizadas: $[1;\ 0,5;\ -0,5;\ -1;\ -0,5;\ 0,5;\ 1;\ 0,5;\ -0,5;\ -1;\ -0,5;\ 0,5;\ 1]$.

«Tomamos los primeros doce valores en una lista y los últimos doce en otra. Cada pareja queda separada por un paso temporal. Calculamos la correlación de Pearson entre esas dos listas y obtenemos 0,5. Es una asociación muestral positiva en esta secuencia construida, no un parámetro estimado del laboratorio ni una prueba de independencia. Declaramos el cálculo porque otros estimadores de autocorrelación, con una sola media y otra normalización, pueden dar un número distinto en muestras cortas. No ajustamos aquí un modelo temporal.» [Crowder 2020 §7.4.1, correlación; NIST/SEMATECH, no disponible en docs/; cálculo: `calc/M03_ejemplos.py`]

«Cuando manejamos una matriz de covarianza, empezamos con controles que parecen elementales, pero son esenciales. La matriz debe ser cuadrada para las mismas variables en filas y columnas. Debe ser simétrica: covarianza de X con Y igual a covarianza de Y con X. Sus unidades deben ser coherentes: una covarianza de dos magnitudes distintas tiene el producto de sus unidades. La diagonal contiene varianzas con unidades al cuadrado. No se pueden copiar correlaciones en una matriz y tratarlas como covarianzas si las desviaciones no son iguales a uno.»

«Además, la matriz debe ser admisible como matriz de covarianza: ninguna combinación lineal real de sus variables puede tener varianza negativa. En una matriz numérica, esto equivale a que sea semidefinida positiva. Para un bloque pequeño se puede verificar que sus autovalores sean no negativos, considerando tolerancias numéricas. También se deben revisar unidades, orden de variables y definición de cada bloque antes de entregar la matriz a un ajuste.» [GUM-S2 §3.20 y notas 3–5; §3.21, nota 4]

> **[PIZARRA]** $\mathbf{V}=\mathbf{V}^{T}$; $\mathbf{a}^{T}\mathbf{V}\mathbf{a}\geq0$ para todo vector $\mathbf{a}$.

«Leo: V es igual a su transpuesta y, para todo vector a, a transpuesta por V por a es mayor o igual que cero. La primera igualdad comprueba simetría. La segunda expresa que ninguna combinación lineal tiene varianza negativa. En una matriz de correlaciones la diagonal debe ser uno; en una matriz de covarianza, la diagonal son las varianzas.»

> **[EJEMPLO]** Matriz de correlaciones simulada de tres puntos: diagonal unitaria, correlaciones 0,50 entre puntos vecinos y 0,25 entre extremos. Es simétrica y sus autovalores calculados son aproximadamente 0,407; 0,750 y 1,843, todos positivos.

«La matriz es admisible para este ejemplo porque es simétrica y sus autovalores son positivos. El resultado se reproduce con el script de M03. En una aplicación real no bastaría con comprobar autovalores: verificaríamos qué datos y fuentes comunes produjeron esos términos, que el orden de puntos coincide entre matrices y que las unidades corresponden a la variable.» [Cálculo: `calc/M03_ejemplos.py`]

> **[EJEMPLO]** Para los tres puntos de la matriz de correlaciones anterior, asignamos incertidumbres estándar **simuladas** de $0,2$, $0,3$ y $0,4$ nmol/mol, en ese orden. Convertimos cada correlación mediante $V_{ij}=\rho_{ij}u_i u_j$ y obtenemos $\mathbf V=\begin{bmatrix}0,04&0,03&0,02\\0,03&0,09&0,06\\0,02&0,06&0,16\end{bmatrix}$ (nmol/mol)².

«Multiplicamos cada correlación por las dos incertidumbres estándar correspondientes. Para la diferencia entre el tercer punto y el primero, el vector de coeficientes es menos uno, cero y uno. La varianza es 0,16 más 0,04 menos dos veces 0,02: queda 0,16 (nmol/mol)² y su raíz es 0,40 nmol/mol. Si dividimos la matriz en el bloque de los puntos uno y dos y el bloque del tercero, las covarianzas de enlace son 0,02 y 0,06; no podemos borrarlas. Como contraste, una matriz de correlaciones de dos puntos con diagonal uno y correlación 1,2 tendría autovalores −0,2 y 2,2: se rechaza, no se usa para propagar.» [Crowder 2020 §7.4.1; cálculo matricial: `calc/M03_ejemplos.py`]

«Las matrices pueden organizarse en bloques cuando hay grupos naturales de variables, canales, días o puntos. Los bloques ayudan a ver qué dependencias son comunes y cuáles son locales. Pero el formato de bloques es una manera de ordenar la información, no una licencia para omitir covarianzas entre bloques si el modelo dice que existen. Etiquetamos filas y columnas, anotamos unidades y fuente de cada bloque, y comprobamos simetría y admisibilidad de la matriz completa.»

«Para GGMR trabajaremos solo con covarianza cero entre ejes, $V_{xy}=0$. El caso con $V_{xy}\ne0$ queda fuera del curso. Tampoco estudiaremos PCR o PLS ni quimiometría general: no son necesarios para la competencia estadística de este módulo. Estas exclusiones no afectan el uso de matrices de covarianza entre canales y puntos dentro del alcance definido.» [prop_e §6]

> **[ERROR CRÍTICO]** «No entreguen una matriz de correlaciones donde el método espera covarianzas; no cambien unidades dentro de un bloque; no supongan covarianza cero por falta de dato; no acepten una matriz asimétrica o que implique varianzas negativas.»

> **[PRÁCTICA — fase de ejercicios]** Construir y comprobar una matriz pequeña de covarianza, verificar unidades, simetría y admisibilidad, y comparar estrategias de promediado en una serie con ruido y deriva.

### Señales de escalamiento del nivel A

«Escalen el trabajo cuando no se conozca el origen de una covarianza común, cuando las unidades o el orden de variables sean inconsistentes, cuando la matriz no sea admisible o cuando el análisis temporal dependa de un modelo de autocorrelación que no se haya validado. Si una herramienta produce resultados incompatibles con una segunda implementación, la diferencia debe resolverse antes de informar la comparación. Para GGMR trabajaremos solo con covarianza cero entre ejes, $V_{xy}=0$. El caso con $V_{xy}$ distinto de cero queda fuera del curso.»

> **[ESCALAMIENTO]** «Solicitar revisión técnica y detener la propagación o el ajuste si falta la justificación de covarianzas comunes, la matriz incumple simetría o admisibilidad, o el resultado depende de una estructura temporal no modelada.»

## Cierre del capítulo

«En B aprendimos que una lectura se modela como variable aleatoria, que una distribución expresa qué valores son plausibles y que la elección entre normal, rectangular o triangular depende de la información. Convertimos semiamplitudes, resolución e incertidumbre expandida en incertidumbres estándar, y distinguimos la variación de una lectura de la de un promedio. También vimos por qué la reducción por raíz de n depende de independencia y por qué t y sus grados de libertad son necesarios cuando la dispersión se estima.»

«En I añadimos covarianza y correlación para calcular sumas, diferencias y promedios dependientes. Reconocimos las distribuciones chi-cuadrado y F como modelos de variación estimada, y usamos gráficos de probabilidad con cautela. Diferenciamos fluctuación de corto plazo, variación entre días y dependencia temporal. En A organizamos covarianzas comunes en matrices, vigilamos unidades, simetría y admisibilidad, y distinguimos autocorrelación de independencia.»

«La regla práctica que quiero que se lleven es esta: antes de promediar o combinar incertidumbres, describan exactamente qué resultado quieren, qué entradas lo forman, qué escala temporal representa cada lectura y qué causas son compartidas. Si no pueden justificar independencia, no la supongan. En el próximo módulo usaremos distribuciones y modelos para estimar efectos y contrastar hipótesis. Ahí aprenderemos a interpretar intervalos y pruebas, no solo a reconocer sus distribuciones.»

## Referencias del capítulo

- Clave Hahs-Vaughn: Hahs-Vaughn, D. L. y Lomax, R. G. *Statistical Concepts: A First Course*. 4.ª ed. Routledge, 2020. Capítulos 4–6 y 8–9. Archivos consultados: `docs/Statistical Concepts – A First Course.pdf` y extractos `docs/statistical_concepts_c04.pdf`, `c05.pdf`, `c06.pdf`, `c08.pdf`, `c09.pdf`.
- Clave MMU: Novellino do Rosario, P. P. y Mendes, A. *Metrology and Measurement Uncertainty: Concepts and Applications*. Springer Nature Switzerland AG, 2025. Capítulo 3. Archivos consultados: `docs/metrology_measure_uncer_c03.pdf`, `docs/Metrology and Measurement Uncertainty.pdf`.
- Clave Crowder 2020: Crowder, S., Delker, C., Forrest, E. y Martin, N. *Introduction to Statistics in Metrology*. Springer Nature Switzerland AG, 2020. Capítulos 4 y 7. Archivos consultados: `docs/intro_stats_metro_c04.pdf`, `docs/intro_stats_metro_c07.pdf`.
- **GUM.** JCGM 100:2008, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*, §§4.2.3, 4.2.7, 4.3.3, 5.2, 6.2.1 y G.3.2–G.3.4. `docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf`.
- **GUM-S2.** JCGM 102:2011, *Evaluation of measurement data — Supplement 2 to the GUM — Extension to any number of output quantities*, §§3.20–3.21. `docs/ISO_IEC Guide 98-3_2008 Suppl.2_2011 - libgen.li.pdf`.
- NIST/SEMATECH. *e-Handbook of Statistical Methods*, «Autocorrelation». NIST, recurso web, https://www.itl.nist.gov/div898/handbook/eda/section3/eda35c.htm (recurso web externo no disponible en `docs/`; contenido no cotejado con pdftotext en esta revisión). Su estimador con media global no se confunde con la correlación de Pearson entre listas desplazadas del ejemplo.
- Prop_e, versión final del 24 de octubre de 2026, §3, §5 M3 y §6. Documento curricular local utilizado para fijar alcance, convenciones y exclusiones; no es referencia técnica externa.
