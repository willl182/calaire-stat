# M03. Probabilidad, distribuciones y dependencia

## Sesión 2 (120 min)

| Bloque | Minutos |
|---|---:|
| Revisión de la tarea de la sesión anterior | 15 |
| Narración B + I (≈32 min a 130 palabras/min) | 32 |
| Ejemplos en pizarra, lectura de gráficos y discusión guiada | 17 |
| Práctica B — en clase | 25 |
| Práctica I — en clase | 15 |
| Preguntas y cierre | 16 |
| **Total** | **120** |

La narración medida de B e I suma unas **4 175 palabras** (≈32 min a 130 palabras/min); los 17 min de ejemplos y discusión guiada completan el bloque de 49 min del plan.

## Revisión de la tarea de la sesión anterior (15 min)

**Guion de revisión de la práctica I de M02.** Retomen los 60 pares simulados de referencia e indicación: tres días, cinco niveles y cuatro lecturas por celda. Pidan que expliquen qué resumen calcularon por día y nivel —media, mediana y MAD— y qué mide la desviación estándar dentro de cada celda. Lean la recta de error ya ajustada en los gráficos, sin volver a estimar sus coeficientes, y distingan la dispersión dentro de una celda de la dispersión agrupada que mezcla niveles. Cierren con la tendencia observada y con qué patrón no explicado justificaría escalar; no eliminen datos para mejorar el ajuste.

## Ficha del capítulo

| Elemento | Descripción |
|---|---|
| Competencia estadística | Asignar distribuciones a entradas, convertir especificaciones en incertidumbres estándar y saber cuándo promediar reduce la incertidumbre. |
| Prerrequisitos | M02: centro, dispersión y diferencia entre una lectura y un resumen; modelo de medición y entradas del SRP según el punto de partida de M02. |
| Nivel B | Variable aleatoria; distribuciones normal, rectangular y triangular; semiamplitud frente a resolución; conversión de incertidumbre expandida; desviación de lectura y de promedio; distribución t, cuantiles y grados de libertad; límite de la reducción por promedio cuando hay componente común o deriva. |
| Nivel I añade | Covarianza y correlación; varianza de combinaciones lineales; distribuciones chi-cuadrado y F; gráficos de probabilidad; dependencia temporal y separación de variación de corto plazo y entre días. |
| Datos | Ejemplos sintéticos con magnitudes declaradas: **simulados**, solo para enseñar cálculos; no describen resultados de CALAIRE. Resolución de 0,1 nmol/mol: entrada hipotética **simulada**, no una especificación del 49C ni del SRP. |
| Anexos | Las deducciones de varianza de combinaciones lineales y de las varianzas rectangular y triangular quedan fuera del alcance de este curso. |
| Referencias clave | Hahs-Vaughn; MMU; Crowder 2020; GUM; GUM-S2; NIST/SEMATECH. Ubicaciones con numeral se incluyen solo cuando se pudieron comprobar en `docs/`. |

## Nivel B — lo que necesitan para interpretar una lectura

En este nivel vamos a añadir una idea sencilla pero poderosa: una lectura no es siempre un número fijo que se repite exactamente. Si repetimos una medición bajo condiciones que consideramos comparables, el resultado puede variar. La probabilidad nos ayuda a describir esa variación antes de saber qué valor aparecerá en la siguiente lectura. No sustituye el punto de partida sobre referencia, indicación y ecuación del SRP presentado en M02, ni la descripción estadística que allí iniciamos. Nos permite hablar de posibles resultados y de sus patrones. [Hahs-Vaughn §5.1; MMU §3.2.1]

### Escena B1. De una repetición a un modelo de probabilidad

> **[DIAPOSITIVA]** Una secuencia de lecturas hipotéticas de un nivel del Level 2. Rotular: datos simulados para enseñanza; no son resultados de CALAIRE.

Imaginen que, con el mismo procedimiento, la misma concentración y el mismo patrón, observamos una lectura tras otra. Antes de la próxima lectura no sabemos el número exacto. Sí sabemos qué resultados son posibles y qué tan plausibles son según el modelo que usemos. A ese proceso de asignar probabilidades a resultados lo llamamos modelar la variabilidad.

La probabilidad de un evento está entre cero y uno. Un evento imposible tiene probabilidad cero, pero la recíproca no vale en general: un punto exacto de una variable continua puede tener probabilidad cero sin ser un valor imposible. Probabilidad uno significa casi seguro bajo el modelo. Para resultados discretos exhaustivos y mutuamente excluyentes, la suma de sus probabilidades es uno; para una densidad continua, el área total es uno. La palabra importante es “dentro del modelo”. Una probabilidad pequeña no demuestra que algo sea imposible ni identifica por sí sola una causa física. [MMU §3.2.1]

Una medición anómala puede ser señal de un cambio, de una condición no registrada o de una limitación del modelo; no es una invitación automática a borrar el dato. Hoy no vamos a probar hipótesis ni a declarar atípicos: eso se trata después y requiere un procedimiento apropiado.

Ahora introduzco variable aleatoria. Es una regla que asigna un número a cada resultado posible del proceso aleatorio que hemos definido. Si contamos cuántas veces ocurre una alarma en una secuencia fija, el resultado es discreto: puede ser cero, uno, dos y así sucesivamente. Si observamos una magnitud como una indicación, la modelamos normalmente como continua dentro de la resolución pertinente, aunque el instrumento guarde números redondeados o cuantizados. La decisión de modelarla como continua o discreta depende de la pregunta y de la escala de los datos. [MMU §3.2.1]

> **[EJEMPLO]** Modelo hipotético simulado de un ciclo: $X=0$ si la lectura queda dentro de banda y $X=1$ si queda fuera. Se suministran $P(X=0)=0,9$ y $P(X=1)=0,1$.

La variable asigna un número a cada uno de los dos resultados definidos. Sumamos 0,9 y 0,1 y obtenemos uno: hemos incluido todos los resultados de este modelo discreto. No estamos estimando frecuencias del laboratorio ni introduciendo aquí otra familia de distribuciones. [MMU §3.2.1; comprobación: `calc/M03_ejemplos.py`]

Para una variable discreta, describimos la probabilidad asociada a cada valor. Para una variable continua usamos una densidad. La densidad no es la probabilidad de un punto exacto; la probabilidad corresponde al área bajo la densidad en un intervalo. La función de distribución acumulada responde otra pregunta: cuál es la probabilidad de obtener un resultado menor o igual que un límite. En el trabajo diario, un intervalo o una cola de distribución suele ser más útil que la densidad en un punto. [MMU §3.2.3]

> **[PIZARRA]** $F(x)=P(X\leq x)$; para variable continua, $P(a<X\leq b)=\int_a^b f(x)\,dx$.

Lo leo en voz alta: efe de equis es la probabilidad de que la variable X sea menor o igual que equis. Para una variable continua, la probabilidad de quedar entre a y b es el área de la densidad entre esos límites. El área total de una densidad sobre todos los resultados posibles es uno.

El valor esperado es el centro de largo plazo que describe la distribución. La varianza mide la dispersión cuadrática alrededor de ese valor esperado; su raíz cuadrada vuelve a las unidades originales y se llama desviación estándar. No confundan estos parámetros del modelo con los estadísticos que calculamos de una muestra. La media y la desviación estándar de una muestra estiman características de una población o proceso, con limitaciones que veremos en inferencia. [MMU §3.2.4]

> **[PREGUNTA AL GRUPO]** Si la indicación esperada es 420 nmol/mol y la desviación estándar de lectura es 0,8 nmol/mol, ¿significa eso que cada lectura queda exactamente entre 419,2 y 420,8? — *Respuesta esperada:* no; la desviación estándar describe escala de dispersión, no un límite absoluto ni una garantía para cada lectura.

Exacto. Una desviación estándar no es un máximo ni un intervalo con cobertura garantizada. Para asignar probabilidades a intervalos necesitamos también un modelo de distribución y sus parámetros. Eso nos lleva a las distribuciones que usaremos.

### Escena B2. Distribuciones que aparecen en la fotometría

Empezamos con la distribución normal. Su forma es simétrica y con un solo máximo, centrado en su media. En la normal, la media, la mediana y el valor más frecuente coinciden. La normal estándar tiene media cero y desviación estándar uno; al estandarizar una variable normal, expresamos su distancia al centro en unidades de desviación estándar. Es útil para representar errores agregados de muchas pequeñas contribuciones y para aproximar ciertos resultados, pero no se declara normal una serie solo porque el histograma parezca una campana. [Hahs-Vaughn §4.1]

> **[PIZARRA]** $Z=(X-\mu)/\sigma$.

Leo: Z es X menos su media, dividido por su desviación estándar. Si X es normal, Z sigue la normal estándar. La operación cambia la escala, no elimina las causas de variación ni arregla una dependencia.

> **[EJEMPLO]** Distribución normal simulada con media 420,0 nmol/mol y desviación estándar 0,8 nmol/mol.

Una lectura de 421,6 está dos desviaciones estándar por encima de la media de este ejemplo, porque la diferencia de 1,6 se divide por 0,8. Eso permite ubicarla en la escala normal estándar. No vamos a convertir aquí esa distancia en una probabilidad tabulada: basta distinguir que el cálculo describe la posición respecto del modelo y que el ejemplo es simulado.

La distribución rectangular es adecuada cuando, por la información disponible, todos los valores dentro de un intervalo se tratan como igualmente plausibles. Si el intervalo va desde el centro menos h hasta el centro más h, h es la semiamplitud. La desviación estándar de esa distribución es h dividido por la raíz de tres. Si el fabricante declara resolución total δ entre pasos, y el error de redondeo se representa entre menos δ/2 y más δ/2, la semiamplitud es δ/2 y la incertidumbre estándar resulta δ dividido por la raíz de doce. No son dos fórmulas intercambiables con la misma entrada: una usa semiamplitud y otra usa resolución total. La deducción de estas expresiones queda fuera del alcance de este curso; aquí las aplicamos. [MMU §§3.2.5.1–3.2.5.2]

> **[PIZARRA]** Rectangular con semiamplitud $h$: $u=h/\sqrt{3}$. Cuantización con resolución total $\delta$: $u=\delta/\sqrt{12}$.

Leo: u igual a h sobre raíz de tres; o, para un intervalo de cuantización cuya anchura completa es delta, delta sobre raíz de doce. Escribir qué representa cada símbolo es parte del cálculo.

> **[EJEMPLO]** Ejemplo simulado de tolerancia uniforme: la entrada se conoce dentro de ±0,3 nmol/mol. Segundo ejemplo simulado: se supone una resolución total de 0,1 nmol/mol, sin atribuirla a un instrumento real.

Para el primer caso h vale 0,3. Al dividirlo por raíz de tres obtenemos una incertidumbre estándar de aproximadamente 0,173 nmol/mol. En el segundo caso δ vale 0,1. Al dividirlo por raíz de doce obtenemos aproximadamente 0,0289 nmol/mol. Los valores se calcularon con `calc/M03_ejemplos.py`. Noten cómo cambia el resultado si se confunde la resolución completa con su semiamplitud. Ambas entradas son hipotéticas y simuladas: no son lecturas ni especificaciones confirmadas de CALAIRE. Una aplicación real necesitaría la resolución documentada del equipo. [MMU §§3.2.5.1–3.2.5.2; `calc/M03_ejemplos.py`]

La distribución triangular también describe una entrada limitada a un intervalo, pero asigna mayor plausibilidad a valores cercanos al centro y menor a valores próximos a los extremos. Si la semiamplitud es h y la forma es triangular simétrica, su incertidumbre estándar es h dividido por raíz de seis. La forma de la distribución expresa información adicional: no se selecciona solo porque produzca una incertidumbre menor. [MMU §3.2.5.2]

> **[PIZARRA]** Triangular simétrica con semiamplitud $h$: $u=h/\sqrt{6}$.

Para h igual a 0,3 nmol/mol, la desviación estándar es aproximadamente 0,122 nmol/mol. La amplitud del intervalo no cambió respecto del ejemplo rectangular; lo que cambió fue la distribución asignada dentro de él. Esa elección necesita una justificación sobre la información disponible, no una preferencia por un número más pequeño. [Cálculo: `calc/M03_ejemplos.py`]

En el certificado puede aparecer una incertidumbre expandida U. Para volver a la incertidumbre estándar u, usamos u igual a U dividido por k, siempre que el factor k corresponda a la declaración que estamos interpretando. U es la incertidumbre expandida reportada, no una segunda desviación estándar. El factor no se inventa ni se toma automáticamente como dos: se declara y se justifica en el contexto del resultado. [GUM §4.3.3; §6.2.1]

> **[ERROR CRÍTICO]** No confundan U con u. U es la incertidumbre expandida y u la estándar. Cambiar entre ambas sin declarar k da un resultado mal reportado.

> **[PIZARRA]** $u=U/k$.

Con U igual a 0,60 nmol/mol y k igual a 2, como ejemplo explícitamente supuesto, u es 0,30 nmol/mol. Este ejemplo sirve solo para practicar la conversión. No concluyan que k es siempre dos ni que una cobertura determinada queda demostrada sin revisar el modelo, la distribución y los grados de libertad. [Cálculo: `calc/M03_ejemplos.py`]

### Escena B3. Una lectura, un promedio y la distribución t

Ahora vamos a separar tres objetos que con frecuencia se mezclan. Primero, la dispersión de lecturas individuales. Segundo, la variación del promedio de varias lecturas. Tercero, un componente que todas esas lecturas comparten, como una referencia común o una deriva persistente. Promediar puede reducir la parte independiente de lectura; no borra automáticamente lo común. [GUM §4.2.3; §5.2]

Supongan que cada lectura independiente tiene desviación estándar σ. Para el promedio de n lecturas independientes, la desviación estándar del promedio es σ sobre raíz de n. La división no cambia la dispersión de cada lectura: cambia la dispersión de los promedios que se obtendrían al repetir grupos de n observaciones. La independencia es la condición importante. Ocho lecturas consecutivas no son ocho réplicas independientes por el mero hecho de estar en ocho filas.

> **[PIZARRA]** $u(\bar X)=\sigma/\sqrt{n}$ si las lecturas son independientes; para una desviación muestral estimada $s$, el error estándar estimado es $s/\sqrt{n}$.

Leo: u de la media es sigma sobre raíz de n; si la desviación se estima con s, el error estándar estimado es s sobre raíz de n. Esta última no significa que la incertidumbre de cualquier resultado de promedio sea s sobre raíz de n: antes debemos precisar cuál es el resultado, qué se repite y a qué horizonte temporal queremos generalizar. [GUM §4.2.3, ecuación (5), y §4.2.7]

> **[EJEMPLO]** Lecturas simuladas con desviación estándar de 0,8 nmol/mol; promedio de 16 lecturas independientes.

La desviación de una lectura sigue siendo 0,8 nmol/mol. La desviación estándar del promedio, bajo independencia, es 0,8 dividido por raíz de 16, es decir, 0,20 nmol/mol. No hemos reducido la variabilidad de una lectura individual. Hemos reducido la variabilidad que se esperaría entre promedios de dieciséis lecturas independientes. [Cálculo: `calc/M03_ejemplos.py`]

Añadamos ahora un efecto común a las dieciséis lecturas, con desviación estándar 0,3 nmol/mol, independiente del ruido individual de 0,8. Suponemos ruido independiente entre lecturas y componentes centradas. La varianza del promedio es la varianza del componente común más la varianza del ruido individual dividida por dieciséis. La incertidumbre estándar del promedio queda en aproximadamente 0,361 nmol/mol. Sin componente común era 0,20; con él no puede bajar por debajo de 0,30 al aumentar el número de lecturas. A medida que el ruido de lectura se promedia, queda el piso común. [Cálculo: `calc/M03_ejemplos.py`; fórmula de la varianza con dependencia]

> **[ERROR CRÍTICO]** No dividan por raíz de n la incertidumbre completa sin separar qué componentes son independientes y cuáles comparten todas las lecturas. Un componente común, una deriva o un sesgo no desaparecen por promediar.

La deriva temporal es un caso especialmente importante. Si las lecturas sucesivas se desplazan lentamente, leer muchas veces en una secuencia puede añadir menos información que tomar observaciones separadas en el tiempo. La cantidad de filas no define por sí sola cuántas observaciones independientes tenemos. En nivel B, si sospechan dependencia no contemplada o deriva, deténganse y consulten; en nivel I estudiaremos cómo reconocer y modelar esa estructura.

> **[EJEMPLO]** Serie **simulada**, construida determinísticamente para aislar la deriva: 16 lecturas equiespaciadas, una por minuto, con tiempos $t=0,1,\ldots,15$ min. Se define $y_t=420,0+0,05t+r_t$ nmol/mol, con pendiente 0,05 nmol/mol por minuto y residuos $r_t$ que repiten cuatro veces $[-0,8;\ 0,8;\ 0,8;\ -0,8]$ nmol/mol. El patrón de residuos es didáctico; no es una muestra aleatoria ni demuestra independencia.

Leo el modelo: indicación igual a 420 más 0,05 veces el tiempo en minutos más un residuo declarado. La ventana es el intervalo de tiempos que decidimos resumir. En la ventana de los minutos cero a siete, la media es 420,175 nmol/mol. En la de ocho a quince es 420,575 nmol/mol. Ambas tienen ocho lecturas y el mismo residuo medio, cero, pero sus medias difieren en 0,400 nmol/mol por el desplazamiento temporal. Para toda la ventana de cero a quince, la media es 420,375 nmol/mol: representa el centro temporal de esa ventana, no la indicación inicial de 420,000. Comparar mitades sirve para investigar efectos que cambian durante las observaciones; aquí mostramos el efecto impuesto, sin hacer una prueba estadística. [GUM F.1.1.3; cálculo: `calc/M03_ejemplos.py`]

Si aplicamos mecánicamente s sobre raíz de dieciséis a la serie completa obtenemos 0,215 nmol/mol. Es un resumen aritmético, no una incertidumbre validada para una serie con media cambiante. No cuantifica el desplazamiento de 0,375 respecto del instante inicial ni la diferencia de 0,400 entre ventanas. En el modelo de ruido independiente de antes, sigma sobre raíz de dieciséis era 0,200; ese resultado describe fluctuación aleatoria de un promedio, no el cambio sistemático al mover la ventana. En B registren la ventana y escalen la deriva; en I compararemos estrategias sobre esta misma serie. [GUM §4.2.3 y F.1.1.3]

Por último, necesitamos la distribución t de Student. La usamos como referencia para inferir sobre una media cuando la desviación poblacional es desconocida y se estima a partir de una muestra, bajo supuestos que revisaremos en M4. La t tiene forma simétrica y colas más pesadas que la normal estándar para pocos grados de libertad. A medida que aumentan los grados de libertad, sus cuantiles se acercan a los de la normal. Los grados de libertad describen cuánta información independiente contribuye a estimar una variabilidad; no son simplemente el número de lecturas copiadas de una tabla. [GUM §§G.3.2–G.3.4; Hahs-Vaughn §6.1]

> **[PIZARRA]** $t=(\bar{x}-\mu_0)/(s/\sqrt{n})$; $\nu=n-1$ para una muestra independiente de una misma población normal con varianza desconocida; la referencia t central corresponde a una media poblacional igual a $\mu_0$.

Leo: t es la diferencia entre la media observada y el valor de referencia, dividida por el error estándar estimado. En el ejemplo elemental de n observaciones independientes, los grados de libertad son n menos uno. En diseños agrupados, temporales o con componentes de varianza, esa cuenta directa puede ser incorrecta. M4 enseña los intervalos y pruebas; aquí nos basta entender por qué aparecen t, sus cuantiles y los grados de libertad.

> **[EJEMPLO]** En una muestra simulada de cinco lecturas independientes, los grados de libertad del modelo elemental de una media son cuatro.

No calculamos un intervalo de confianza en esta escena. Solo observamos que, si la desviación estándar del proceso no se conoce y se estima con cinco observaciones independientes, la referencia t tiene cuatro grados de libertad. Para un cuantil bilateral central del 95 %, el cuantil t con cuatro grados de libertad es aproximadamente 2,776, mientras que el cuantil normal correspondiente es aproximadamente 1,960. Con pocos grados de libertad el cuantil de t es mayor, reflejando la incertidumbre adicional de estimar la dispersión. El intervalo concreto y su interpretación corresponden a M4-B. [Cálculo de cuantiles: `calc/M03_ejemplos.py`]

> **[PREGUNTA AL GRUPO]** Si se duplica el número de lecturas pero persiste una deriva común, ¿se reduce a la mitad la incertidumbre total del promedio? — *Respuesta esperada:* no; solo disminuye la parte que el modelo considera independiente, y una componente común puede permanecer.

Exactamente. La reducción ideal es con la raíz cuadrada, no con el número de lecturas, y solo aplica a la parte independiente.

### Práctica B. Convertir especificaciones del certificado en incertidumbres estándar y comparar promedios (en clase, 25 min)

**Enunciado narrado.** Ustedes reciben una ficha docente con tres entradas hipotéticas para una calibración de ozono: una tolerancia simétrica de ±0,30 nmol/mol que se modelará rectangular; una cuantización con resolución total δ = 0,10 nmol/mol; y una incertidumbre expandida U = 0,60 nmol/mol declarada con k = 2,0; y una entrada triangular simétrica con semiamplitud 0,30 nmol/mol. Son datos **simulados**, definidos aquí para el ejercicio; no son especificaciones del certificado de un SRP ni de un Level 2. El resultado de interés es la incertidumbre estándar de cada entrada individual, en nmol/mol. Después compararán promedios de 16 lecturas: primero, lecturas independientes con desviación estándar 0,80 nmol/mol; segundo, ruido independiente igual más una contribución común con desviación estándar 0,30 nmol/mol. Finalmente examinarán una serie simulada de 16 lecturas, una por minuto, definida exactamente por $y_t=420,0+0,05t+r_t$ nmol/mol, con $t=0,\ldots,15$ minutos y $r_t$ igual a cuatro repeticiones de $[-0,8;0,8;0,8;-0,8]$. La deriva de 0,05 nmol/mol por minuto se impone para enseñar el efecto de la ventana; no se presenta como ruido aleatorio observado.

Calculen las cuatro incertidumbres estándar de entrada, incluida la triangular. Para una media de 16 lecturas independientes con s=0,80 nmol/mol, calculen el semiancho de referencia central del 95 % usando $t(0,975;15)$; indiquen por qué no se usa directamente el cuantil normal. Calculen también la incertidumbre estándar de los dos promedios bajo los modelos declarados, la media global de la serie y las medias de cuatro bloques consecutivos de cuatro minutos. Comparen las dos mitades de ocho lecturas. Indiquen qué promedio representa el modelo de lecturas independientes y por qué no basta con aplicar $s/\sqrt n$ a la serie con deriva. Cierren con la decisión operativa y una señal de escalamiento.

**Solución docente.** Para la rectangular, la semiamplitud es $h=0,30$ nmol/mol, así que $u=h/\sqrt3=0,1732$ nmol/mol. Para la resolución, la entrada uniforme cubre la anchura total δ; por tanto $u=\delta/\sqrt{12}=0,02887$ nmol/mol. Para la incertidumbre expandida, $u=U/k=0,60/2,0=0,300$ nmol/mol. Para la triangular simétrica, $u=h/\sqrt6=0,1225$ nmol/mol. Las cuatro cantidades son incertidumbres estándar, no límites absolutos.

Para la media de 16 lecturas, los grados de libertad elementales son 15. El cuantil bilateral central del 95 % es $t(0,975;15)=2,131$; el semiancho de referencia es $2,131(0,80/\sqrt{16})=0,4262$ nmol/mol. Se usa t porque la desviación poblacional se estima con s; no se está haciendo aquí una prueba ni un intervalo de confianza de M4.

Con 16 lecturas independientes, la desviación estándar del promedio es $0,80/\sqrt{16}=0,200$ nmol/mol. Si cada lectura además contiene el mismo componente común, la varianza del promedio es $0,30^2+0,80^2/16=0,1300$ (nmol/mol)²; su raíz es $0,3606$ nmol/mol. La contribución común permanece aunque se repitan más lecturas dentro de la misma condición.

La serie determinista arroja media global 420,375 nmol/mol. Las cuatro medias de bloque son 420,075; 420,275; 420,475 y 420,675 nmol/mol. La segunda mitad supera a la primera en 0,400 nmol/mol. Esta secuencia no es una muestra aleatoria independiente: aplicar un error estándar basado en $s/\sqrt{16}$ no cuantifica una media estable ni elimina la tendencia temporal. La media global solo describe el centro de toda la ventana declarada; los bloques muestran el desplazamiento. Comprobación: cada bloque está centrado en su tiempo y las medias de los cuatro bloques promedian 420,375 nmol/mol.

**Interpretación y decisión operativa.** Para una especificación o resolución documentada, conviertan primero a u con la distribución y el significado de amplitud correctos. Para promediar, declaren si informan una lectura, un promedio de corto plazo o una ventana temporal. No reduzcan una componente común por raíz de n. Si en datos reales aparece deriva o el intervalo de observación cambia la conclusión, detengan la plantilla de promedio independiente, conserven la secuencia temporal y escalen para evaluar el modelo; no borren lecturas ni atribuyan esta simulación a CALAIRE.

**Criterio de logro.** Calcula las cuatro conversiones, obtiene el semiancho de referencia con t y 15 grados de libertad, distingue ruido independiente de componente común y detecta que la serie con deriva no admite la reducción automática por $\sqrt n$.

### Señales de escalamiento del nivel B

Antes de seguir, dejemos claras las señales para detenerse. Si dos entradas comparten una fuente de variación y la plantilla no contempla esa dependencia, no supongan independencia. Si la serie muestra cambio de escala, deriva o residuos con estructura, el promedio simple puede ocultar la estructura. Si ven un dato inusual sin causa documentada, no lo eliminen para acercar el resultado a lo esperado. Si la incertidumbre en ambos ejes resulta relevante, el ajuste básico con referencia fija no es suficiente: escalen el análisis. Si hay pocos grados de libertad, una cobertura o una decisión próxima a un límite, consulten a quien tenga la responsabilidad técnica. Si las observaciones son temporales y consecutivas, no las llamen independientes sin evidencia.

> **[ESCALAMIENTO]** Detener el cálculo básico y consultar cuando haya dependencia no contemplada, cambio de escala, atípico sin causa, residuos con estructura, incertidumbre relevante en ambos ejes, dependencia temporal, grados de libertad limitados o una decisión cercana a un límite. Registrar qué supuesto falla o qué información falta; no corregirlo borrando observaciones.

Estas señales no son un reemplazo de la formación del nivel I. Son el punto en que el operador de B reconoce el límite de la plantilla y protege la validez del resultado.

## Nivel I — lo que se añade

En B hemos representado una entrada por su propia distribución y hemos visto que promediar no siempre elimina toda variación. En I añadimos la dependencia entre entradas y entre observaciones, porque en calibración dos valores pueden compartir el mismo patrón y dos lecturas próximas pueden arrastrar parte del mismo ruido. A partir de aquí, una suma o una diferencia ya no se calcula ignorando automáticamente cómo se relacionan sus términos. Reconocemos las familias chi-cuadrado y F, pero sus contrastes e intervalos pertenecen a M4-I.

### Escena I1. Covarianza y correlación: qué se cancela y qué se suma

La covarianza mide cómo dos variables se mueven juntas respecto de sus medias. Si cuando X está por encima de su media Y suele estar también por encima, la covarianza tiende a ser positiva. Si una suele estar por encima mientras la otra queda por debajo, tiende a ser negativa. Una covarianza cercana a cero indica ausencia de asociación lineal en el modelo, pero no demuestra independencia en general. [Crowder 2020 §7.4.1]

La covarianza depende de las unidades de X y de Y. Para expresar la asociación en una escala sin unidades usamos la correlación: covarianza dividida por el producto de las desviaciones estándar. La correlación queda entre menos uno y uno. El signo indica la dirección lineal y la magnitud describe cuán fuerte es esa asociación lineal. Una correlación no identifica una causa y tampoco describe por sí sola relaciones no lineales. [Crowder 2020 §7.4.1]

> **[PIZARRA]** $\operatorname{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])]$; $\rho_{XY}=\operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)$.

Leo: la covarianza es la esperanza del producto de las desviaciones de X e Y respecto de sus medias. La correlación es esa covarianza dividida por ambas desviaciones estándar. Si una de las desviaciones es cero, la correlación no está definida porque no hay variación que normalizar.

La esperanza de una combinación lineal se obtiene combinando las esperanzas con los mismos coeficientes. Para la varianza necesitamos más cuidado: la varianza de una suma incluye la covarianza. Esa es la razón estadística de que una causa compartida pueda aumentar o disminuir la incertidumbre de un resultado. La demostración algebraica queda fuera del alcance de este curso; aquí usaremos el resultado. [Crowder 2020 §7.2]

> **[PIZARRA]** $E[aX+bY]=aE[X]+bE[Y]$; $\operatorname{Var}(aX+bY)=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y)+2ab\operatorname{Cov}(X,Y)$.

Leo la segunda expresión: la varianza de a X más b Y es a al cuadrado por la varianza de X, más b al cuadrado por la varianza de Y, más dos a b veces la covarianza. Si usamos una diferencia, el coeficiente de una de las variables es negativo. Por eso el término de covarianza cambia de signo.

> **[EJEMPLO]** Dos entradas simuladas con desviaciones estándar 0,8 y 0,6 nmol/mol y correlación 0,75. La covarianza es 0,36 (nmol/mol)².

Multiplicamos la correlación, 0,75, por las dos desviaciones, 0,8 y 0,6. Obtenemos una covarianza de 0,36. Si sumamos las entradas ignorando su relación, la desviación estándar de la suma resulta 1,00. Al incluir la covarianza positiva, la desviación estándar de la suma aumenta a aproximadamente 1,31. Para la diferencia de las mismas dos entradas, el término positivo se resta y la desviación estándar baja a aproximadamente 0,529. No significa que la diferencia siempre tenga menos incertidumbre. Significa que una fluctuación común se cancela parcialmente en esta diferencia, mientras que se suma en la suma. [Cálculo: `calc/M03_ejemplos.py`]

Pensemos ahora en dos resultados de concentración que se apoyan en el mismo patrón. Una variación del patrón puede mover ambos resultados de forma parecida. Al estudiar la diferencia entre ellos, ese efecto común puede cancelarse en parte. Pero esa cancelación solo puede cuantificarse si conocemos la covarianza o un modelo que la produzca. La palabra “comparten” no nos da por sí sola el valor numérico.

> **[ERROR CRÍTICO]** No calculen la incertidumbre de una diferencia por suma cuadrática suponiendo independencia cuando los dos resultados comparten el SRP 55 u otra entrada. Primero identifiquen y justifiquen la dependencia.

Para el promedio de variables correlacionadas también cambia la regla. Si cada lectura tiene la misma varianza y todas las parejas tienen una correlación positiva, las observaciones redundan en parte: el promedio mejora menos que lo que predice la regla de independencia. Con correlación negativa puede ocurrir lo contrario dentro de los límites que admite una matriz válida. Por eso no aplicamos s sobre raíz de n de forma automática a una secuencia dependiente.

> **[PIZARRA]** Para variables $X_i$: $\operatorname{Var}(\sum_i c_iX_i)=\sum_i c_i^2\operatorname{Var}(X_i)+2\sum_{i<j}c_ic_j\operatorname{Cov}(X_i,X_j)$.

La regla de la varianza de una combinación lineal se generaliza sumando cada varianza con el cuadrado de su coeficiente y agregando dos veces cada covarianza de parejas distintas. La derivación queda fuera del alcance de este curso. En las hojas de cálculo, el signo de cada coeficiente importa: una diferencia y una suma no comparten el mismo término de covarianza.

### Escena I2. Chi-cuadrado, F y gráficos de probabilidad

En B usamos la forma de una distribución para representar una entrada. En I veremos dos distribuciones más que aparecen cuando describimos variabilidad estimada y comparamos escalas de variación: chi-cuadrado y F. La distribución chi-cuadrado se construye a partir de cuadrados de variables normales estándar independientes. Sus valores son no negativos y su forma depende de los grados de libertad. La distribución F es el cociente de dos cantidades chi-cuadrado independientes entre sí, cada una escalada por sus propios grados de libertad. También depende de esos grados de libertad y toma valores no negativos. La representación de chi-cuadrado como suma de cuadrados se presenta aquí como definición; Hahs-Vaughn §9.1.1 se cita solo para características de la distribución F.

No vamos a ejecutar aquí pruebas de hipótesis sobre varianzas; eso corresponde a M4-I. Para M3 necesitamos saber qué distribuciones son, por qué sus cuantiles dependen de grados de libertad y reconocer que tienen soporte positivo y normalmente una forma asimétrica, en especial con pocos grados de libertad. En ANOVA, la distribución F permitirá estudiar cocientes de cuadrados medios en M6. No anticipamos la prueba ni sus condiciones.

> **[PIZARRA]** $\chi^2_\nu=\sum_{i=1}^{\nu} Z_i^2$ para $Z_i$ normales estándar independientes; $F_{\nu_1,\nu_2}=(\chi^2_{\nu_1}/\nu_1)/(\chi^2_{\nu_2}/\nu_2)$.

Leo: chi cuadrado con nu grados de libertad es la suma de nu cuadrados de variables normales estándar independientes. F con ν₁ y ν₂ grados de libertad es el cociente de dos chi cuadrados, cada uno dividido por su grado de libertad. Para obtener la distribución F, las dos cantidades chi-cuadrado también deben ser independientes entre sí. Estas representaciones explican por qué se usan para cantidades de variación estimada y cocientes de variaciones.

> **[EJEMPLO]** Ejemplo esquemático de chi-cuadrado con dos grados de libertad: si las dos variables normales estándar observadas son 1 y −1, la suma de cuadrados vale 2. Para F, si los valores de chi-cuadrado son 6 con 3 grados de libertad y 4 con 2 grados de libertad, el cociente de cuadrados medios vale 1.

En el primer cálculo sumamos uno al cuadrado y menos uno al cuadrado: obtenemos dos. En el segundo, seis dividido por tres es dos y cuatro dividido por dos también es dos; el cociente es uno. Estos números ilustran la construcción de las distribuciones; no son pruebas de significación ni decisiones sobre los datos del laboratorio. [Cálculo: `calc/M03_ejemplos.py`]

¿Cómo comprobamos si una distribución normal es una aproximación razonable para las lecturas de un nivel o para el cero? Empezamos mirando los datos con un histograma y un gráfico de probabilidad normal. En este último ordenamos los valores observados y los comparamos con los cuantiles que corresponderían a una normal. Si los puntos siguen aproximadamente una recta, la normal puede ser plausible para ese conjunto. Curvatura, colas distintas o puntos alejados sugieren revisar el modelo, el proceso o la escala. El gráfico no certifica normalidad ni convierte un pequeño conjunto en evidencia concluyente. [Crowder 2020 §4.4.3]

> **[EJEMPLO]** Cinco valores simulados ordenados: 418,8; 419,5; 420,0; 420,5; 421,2 nmol/mol. Para las posiciones $(i-0,5)/5$, los cuantiles normales estándar son aproximadamente −1,282; −0,524; 0,000; 0,524; 1,282.

Comparamos cada lectura ordenada con su cuantil teórico: el menor valor con −1,282, el segundo con −0,524, el central con cero, el cuarto con 0,524 y el mayor con 1,282. Esa pareja de listas da los cinco puntos del gráfico. Son datos simulados para mostrar cómo se construye; no concluimos normalidad con solo cinco valores. [Cálculo: `calc/M03_ejemplos.py`]

> **[DIAPOSITIVA]** Gráfico de probabilidad normal conceptual, sin datos de laboratorio. Marcar: alineación aproximada no equivale a prueba ni demuestra independencia.

Una serie puede parecer normal en su histograma y aun así tener dependencia temporal. Por ejemplo, lecturas que suben y bajan suavemente pueden tener una distribución marginal parecida a una campana, pero no ser independientes en el orden temporal. Por eso el histograma y el gráfico de probabilidad contestan sobre la forma de distribución, no sobre toda la estructura del proceso.

### Práctica I — en clase (15 min). Calcular la diferencia con covarianza e iniciar el gráfico de probabilidad

**Enunciado narrado.** En una comparación docente simulada, dos resultados de ozono son $A=420,0$ y $B=419,4$ nmol/mol; $u(A)=0,80$ y $u(B)=0,60$ nmol/mol, con correlación declarada $\rho_{AB}=0,75$ por una contribución de referencia compartida. Calculen $\Delta=A-B$, la covarianza y $u(\Delta)$ suponiendo primero independencia y después usando esa correlación. Inicien el gráfico de probabilidad normal con los errores fijados $[-0,10;0;0,10;-0,10;0;0,10]$ nmol/mol: ordénenlos y calculen su varianza muestral descriptiva. Datos simulados; no proceden de CALAIRE.

### Práctica I — tarea. Completar el gráfico y la interpretación temporal

**Enunciado narrado.** Completen los seis puntos del gráfico normal usando posiciones de Blom $p_i=(i-0,375)/(6+0,25)$ y los cuantiles normales teóricos. Usen la secuencia en el orden entregado para señalar si hay patrón temporal; no hagan una prueba formal. Expliquen por qué los contrastes e intervalos chi-cuadrado y F se reservan para M4-I.

**Solución docente.** Los pares (cuantil teórico; error ordenado), redondeados, son $(-1,28;-0,10)$, $(-0,64;-0,10)$, $(-0,20;0,00)$, $(0,20;0,00)$, $(0,64;0,10)$ y $(1,28;0,10)$. La figura reproducible `calc/M03_practica_I_probabilidad.html` muestra los pares. La secuencia bajo–centro–alto se repite: es una señal descriptiva para revisar dependencia, no una prueba de normalidad ni una estimación concluyente de autocorrelación. La muestra pequeña no certifica normalidad. Chi-cuadrado y F se reconocen como distribuciones en M3; sus contrastes e intervalos corresponden a M4-I.

**Interpretación y decisión operativa.** Informen $u(\Delta)=0,529$ nmol/mol solo bajo el modelo de covarianza declarado. Si falta información del patrón compartido, no sustituyan la covarianza por cero. Si aparecen rachas o estructura gráfica, documenten y escalen; no eliminen puntos.

**Criterio de logro.** Incluye el término de covarianza con signo correcto, obtiene los pares de Blom verificables y distingue inspección gráfica y señal temporal de una prueba concluyente.

### Escena I3. Dependencia temporal y dos escalas de variación

En una serie temporal, el orden es parte de la información. Si anotamos una lectura cada cierto intervalo, la lectura actual puede depender de la anterior por acondicionamiento, control del flujo, respuesta del fotómetro o deriva. La dependencia temporal se investiga mirando la serie en orden y preguntando si los residuos o desviaciones consecutivas tienden a parecerse. No basta con resumir todas las observaciones como una bolsa sin orden. [NIST/SEMATECH, Autocorrelation, no disponible en docs/]

Distinguimos ahora variación de corto plazo y variación entre días. La primera describe cambios entre lecturas bajo condiciones de corto plazo comparables. La segunda refleja cambios del efecto de día cuando repetimos el procedimiento en jornadas distintas. Si combinamos ambos componentes sin indicar la escala temporal, no podremos responder cuánto varía una lectura dentro del día ni cuánto cambia el promedio de un día a otro.

> **[PIZARRA]** Modelo didáctico: $X_{dj}=\mu+D_d+\varepsilon_{dj}$; $\operatorname{sd}(D_d)=\tau$; $\operatorname{sd}(\varepsilon_{dj})=\sigma$. $D_d$: efecto de día; $\varepsilon_{dj}$: variación de lectura dentro del día.

Leo: la observación del día d y la lectura j es la media general más un efecto de ese día más un error de lectura. La desviación estándar del efecto diario es tau y la del error de lectura es sigma; sus estimadores se anotan s_entre y s_r, respectivamente. Para este cálculo suponemos efectos de día centrados, independientes entre días, y errores de lectura centrados, independientes entre sí e independientes de los efectos de día. Este modelo ilustra dos escalas, no introduce aquí el procedimiento ANOVA de M6. Si promediamos varias lecturas del mismo día, se reduce la parte de lectura independiente; el efecto de día no se reduce al repetir dentro de ese día. Para caracterizar la precisión de uso en días distintos necesitamos observaciones en varios días.

> **[EJEMPLO]** Datos simulados: desviación estándar dentro de una jornada de 0,8 nmol/mol; efecto común de jornada de 0,3 nmol/mol; 16 lecturas por jornada.

Ya vimos el cálculo: la contribución de lectura al promedio de la jornada baja a 0,20 nmol/mol, mientras que la variación entre jornadas permanece en 0,30. La desviación estándar total del promedio de jornada, al combinar ambas partes independientes del modelo, es aproximadamente 0,361 nmol/mol. Si reportamos solo la dispersión intradía, responderemos una pregunta distinta de la que responde la variabilidad de promedios diarios. Los valores son simulados y no describen el Level 2. [Cálculo: `calc/M03_ejemplos.py`]

En la práctica, usen el tiempo y el diseño como parte de la descripción del resultado. ¿Es una lectura, un promedio de ciclo, un promedio de jornada o una predicción para otra fecha? ¿Las observaciones se tomaron en el mismo día o en días distintos? En M6 se estimarán componentes para los diseños indicados; por ahora, el objetivo es no confundir esas variaciones.

> **[ERROR CRÍTICO]** No sumen un componente entre días y una desviación de promedios diarios si esta última ya contiene ese componente. Identifiquen qué resume cada desviación antes de combinarla.

La dependencia temporal también altera los grados de libertad efectivos. Una serie larga no siempre contiene tanta información independiente como indica el número de filas. En este nivel no corregimos mecánicamente una cuenta: reconocemos la estructura, documentamos el orden y escalamos el análisis cuando la dependencia afecta la conclusión.

### Señales de escalamiento del nivel I

Si el gráfico temporal muestra dependencia aparente, como rachas, tendencia o ciclos, no supongan que las lecturas son independientes. Si una incertidumbre de diferencia depende de una fuente común, soliciten el modelo o los datos de covarianza. Si el gráfico de probabilidad muestra una estructura que el modelo normal no describe, no oculten esa discrepancia con una prueba elegida por costumbre. Si una estimación combina variación intradía y entre días, asegúrense de que cada componente responde al resultado que se reporta.

> **[ESCALAMIENTO]** Pasar a revisión técnica cuando haya dependencia temporal aparente, deriva, estructura por día, dependencia por patrón compartido o una matriz de covarianza necesaria que no esté disponible. No sustituir la información ausente por independencia supuesta.

## Cierre del capítulo

En B aprendimos que una lectura se modela como variable aleatoria, que una distribución expresa qué valores son plausibles y que la elección entre normal, rectangular o triangular depende de la información. Convertimos semiamplitudes, resolución e incertidumbre expandida en incertidumbres estándar, y distinguimos la variación de una lectura de la de un promedio. También vimos por qué la reducción por raíz de n depende de independencia y por qué t y sus grados de libertad son necesarios cuando la dispersión se estima.

En I añadimos covarianza y correlación para calcular sumas, diferencias y promedios dependientes. Reconocimos las distribuciones chi-cuadrado y F como modelos de variación estimada, y usamos gráficos de probabilidad con cautela. Diferenciamos fluctuación de corto plazo, variación entre días y dependencia temporal.

La regla práctica que quiero que se lleven es esta: antes de promediar o combinar incertidumbres, describan exactamente qué resultado quieren, qué entradas lo forman, qué escala temporal representa cada lectura y qué causas son compartidas. Si no pueden justificar independencia, no la supongan. En M4 usaremos distribuciones y modelos para estimar efectos y contrastar hipótesis. Ahí aprenderemos a interpretar intervalos y pruebas, no solo a reconocer sus distribuciones.

## Referencias del capítulo

- Clave Hahs-Vaughn: Hahs-Vaughn, D. L. y Lomax, R. G. *Statistical Concepts: A First Course*. 4.ª ed. Routledge, 2020. Capítulos 4–6 y 8–9. Archivos consultados: `../Curso_COMPLETO/docs/Statistical Concepts – A First Course.pdf` y extractos `../Curso_COMPLETO/docs/statistical_concepts_c04.pdf`, `c05.pdf`, `c06.pdf`, `c08.pdf`, `c09.pdf`.
- Clave MMU: Novellino do Rosario, P. P. y Mendes, A. *Metrology and Measurement Uncertainty: Concepts and Applications*. Springer Nature Switzerland AG, 2025. Capítulo 3. Archivos consultados: `../Curso_COMPLETO/docs/metrology_measure_uncer_c03.pdf`, `../Curso_COMPLETO/docs/Metrology and Measurement Uncertainty.pdf`.
- Clave Crowder 2020: Crowder, S., Delker, C., Forrest, E. y Martin, N. *Introduction to Statistics in Metrology*. Springer Nature Switzerland AG, 2020. Capítulos 4 y 7. Archivos consultados: `../Curso_COMPLETO/docs/intro_stats_metro_c04.pdf`, `../Curso_COMPLETO/docs/intro_stats_metro_c07.pdf`.
- **GUM.** JCGM 100:2008, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*, §§4.2.3, 4.2.7, 4.3.3, 5.2, 6.2.1, F.1.1.3 y G.3.2–G.3.4. §4.3.3 respalda u=U/k para certificados/especificaciones; G.3.2 trata la distribución t; F.1.1.3 ofrece apoyo cualitativo sobre influencias aleatorias. Las aplicaciones a datos simulados son propias. `../Curso_COMPLETO/docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf`.
- **GUM-S2.** JCGM 102:2011, *Evaluation of measurement data — Supplement 2 to the GUM — Extension to any number of output quantities*, §3.20, nota 4, y §3.21, nota 4 (PDF local; notas sobre admisibilidad de matrices de covarianza/correlación). `../Curso_COMPLETO/docs/ISO_IEC Guide 98-3_2008 Suppl.2_2011 - libgen.li.pdf`.
- NIST/SEMATECH. *e-Handbook of Statistical Methods*, «Autocorrelation». NIST, recurso web, https://www.itl.nist.gov/div898/handbook/eda/section3/eda35c.htm (consultada en línea el 2026-10-27; no está en `docs/`). Su estimador con media global no se confunde con la correlación de Pearson entre listas desplazadas del ejemplo.
- Prop_e, versión final del 24 de octubre de 2026, §3, §5 M3 y §6. Documento curricular local utilizado para fijar alcance, convenciones y exclusiones; no es referencia técnica externa.
- Las deducciones de varianza de combinaciones lineales y de las varianzas rectangular y triangular quedan fuera del alcance de este curso.
