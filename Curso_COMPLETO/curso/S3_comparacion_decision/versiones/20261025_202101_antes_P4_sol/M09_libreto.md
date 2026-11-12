# M09. Comparación de resultados: diferencias, covarianza y consistencia

## Ficha del capítulo

| Elemento | Contenido |
|---|---|
| Competencia estadística | Estimar la incertidumbre de una diferencia entre resultados, con la covarianza que corresponda, y decidir qué hipótesis contrasta el indicador de compatibilidad. |
| Prerrequisitos | M3: incertidumbre y dependencia; M4: estimación e interpretación de contrastes; M7: recta de calibración y covarianza de sus parámetros; M8: propagación de incertidumbre. Los niveles son acumulativos: I comprende B y A comprende B e I. |
| Nivel B | Diferencia, incertidumbre de la diferencia bajo independencia justificada y $E_n$ en un escenario que cumpla las condiciones de su fórmula. $E_n=Δ/√(U_{1}^{2}+U_{2}^{2})$, con el mismo factor $k$ para ambas incertidumbres expandidas, y criterio $|E_n|≤1$. Reconocer que un patrón compartido no invalida $E_n$ en general, pero impide suponer independencia sin justificación. |
| Nivel I añade | Varianza de una diferencia con covarianza; covarianza por patrón compartido; interpolación con recta y covarianza de parámetros; compatibilidad frente a conformidad. Calcular $U(Δ)=k_Δu(Δ)$ y declarar cobertura. $Δ/U(Δ)$ es una extensión de $E_n$, no la definición B. |
| Nivel A añade | Matrices de covarianza y GGMR para comparación dentro de $V_{xy}=0$; consistencia por chi-cuadrado; grado de equivalencia frente a referencia común. Caso SRP 36/SRP 7 como adaptación didáctica para interpolación; no se cubren protocolo, organización de la comparación ni base de datos de comparaciones clave (KCDB). |
| Datos de los ejemplos | B e I: datos **simulados**, fijados en `calc/M09_ejemplos.py`; no son resultados de CALAIRE. A: pares **publicados** en US EPA SRP QAPP, Element 14.2, Figura 14.2; incertidumbres y covarianzas **adaptadas** del modelo BIPM-SRP27, con $V_{xy}=0$ por hipótesis didáctica. No son datos de CALAIRE ni resultado oficial. |
| Anexos | AX.2: varianza de combinaciones lineales y covarianza. AX.8: GGMR con $V_{xy}=0$ y chi-cuadrado de consistencia. AX.9: diferencia con patrón compartido y grado de equivalencia frente a referencia común. |
| Referencias clave | GUM 5.2.2; ISO/TS 28037:2010, cláusula 10 y Tablas 25–26; BIPM.QM-K1, Protocolo A §§7–8 y Apéndice 1 §3, ec. 21; US EPA SRP QAPP, Element 14.2, Figura 14.2. Los numerales se verificaron en los PDF de `docs/`; detalle en la bitácora. |

## Nivel B — comparar cuando la independencia está justificada

En este nivel damos por vistos la incertidumbre estándar y expandida, el uso de una recta de calibración y la diferencia entre una medición y un resultado de referencia. Vamos a añadir una pregunta precisa: ¿qué diferencia observamos entre dos resultados y qué tan grande es esa diferencia frente a sus incertidumbres? En B usaremos una condición estricta: la independencia de los resultados debe estar justificada. No basta con que los resultados estén en dos columnas distintas. La guía GUM establece que, si las entradas están correlacionadas, la incertidumbre combinada debe incluir los términos de covarianza [GUM 5.2.2].

### Escena B1. La diferencia tiene signo y una pregunta definida

> **[DIAPOSITIVA]** Dos resultados de concentración, $y_{1}$ y $y_{2}$, con sus incertidumbres. En un segundo paso, marcar la diferencia $Δ=y_{2}−y_{1}$ y una flecha que señale «comparar bajo un modelo».

Miren los dos resultados de la diapositiva. Antes de hablar de compatibilidad, fijamos cuál se resta de cuál. Voy a definir delta como el resultado dos menos el resultado uno. Así el signo nos dice la dirección: delta positivo significa que el segundo resultado supera al primero; delta negativo significa que queda por debajo. El signo no mide por sí solo la importancia de la diferencia. Para eso necesitamos su incertidumbre y la pregunta que pretendemos contestar.

> **[PIZARRA]** $\Delta=y_2-y_1$.
>
> **[NOTA AL INSTRUCTOR]** Leer: «delta es igual a ye dos menos ye uno». Mantener las unidades de ambos resultados iguales antes de restar.

El concepto estadístico no depende de que las dos columnas sean dos fotómetros, dos patrones o dos resultados de calibración. El caso de hoy usa concentraciones de ozono y, por tanto, expresaremos las cifras en nmol/mol. Pero lo primero sigue siendo estadístico: definimos una diferencia entre dos estimaciones. En la GUM, cuando se propaga una función de varias entradas correlacionadas, la covarianza forma parte de la incertidumbre de salida [GUM 5.2.2]. La forma más simple de la diferencia bajo independencia sale de ese marco cuando no hay covarianza entre resultados. La deducción completa queda en AX.2; aquí usaremos la regla y revisaremos el supuesto.

Construyamos una ilustración **simulada** para el nivel B. Supongamos que dos resultados independientes son cien coma cero cero y cien coma treinta y cinco nmol/mol. La incertidumbre estándar del primero es cero coma veinte nmol/mol, y la del segundo cero coma quince nmol/mol. Para esta ilustración declaramos que no comparten patrón, corrección, dato de calibración ni otra contribución correlacionada. No estamos afirmando que esos valores provengan de CALAIRE; son datos inventados para enseñar el cálculo.

> **[EJEMPLO]** Datos **simulados**: $y_{1}=100,00 nmol/mol$, $y_{2}=100,35 nmol/mol$, $u_{1}=0,20 nmol/mol$, $u_{2}=0,15 nmol/mol$; se supone independencia justificada.

La diferencia vale cero coma treinta y cinco nmol/mol. Para resultados independientes, la incertidumbre estándar de la diferencia se obtiene sumando las varianzas, no los errores estándar en línea recta: raíz de cero coma veinte al cuadrado más cero coma quince al cuadrado. En números, eso da cero coma veinticinco nmol/mol. Lean la regla en voz alta conmigo: la incertidumbre estándar de delta es la raíz de la suma de los cuadrados de las dos incertidumbres estándar, cuando los resultados son independientes. Si no se cumple la independencia, esta no es la fórmula completa [GUM 5.2.2; AX.2].

> **[PIZARRA]** Para resultados independientes, $u(\Delta)=\sqrt{u_1^2+u_2^2}$.
>
> **[NOTA AL INSTRUCTOR]** Decir «esta expresión es una versión particular de la ley de propagación; su condición es covarianza nula». No presentar independencia como consecuencia automática de tener dos instrumentos.

Ahora debemos distinguir incertidumbre estándar de expandida. Supongamos que para los dos resultados la cobertura se expresa con el mismo factor $k=2$. Entonces $U_{1}=2×0,20=0,40 nmol/mol$ y $U_{2}=2×0,15=0,30 nmol/mol$. La definición operativa de este ejercicio básico es $E_n$ igual a delta dividido por la raíz de $U_{1}$ al cuadrado más $U_{2}$ al cuadrado. Sustituimos: cero coma treinta y cinco dividido por la raíz de cero coma cuarenta al cuadrado más cero coma treinta al cuadrado. El denominador vale cero coma cincuenta nmol/mol y $E_n$ vale cero coma setenta. El signo queda positivo porque conservamos el sentido de la diferencia. La GUM define la incertidumbre expandida mediante un factor de cobertura multiplicado por la incertidumbre estándar [GUM 6.2.1].

> **[PIZARRA]** $E_n=\dfrac{\Delta}{\sqrt{U_1^2+U_2^2}}$; en este caso $E_n=0,35/\sqrt{0,40^2+0,30^2}=0,70$.
>
> **[NOTA AL INSTRUCTOR]** Leer: «E sub ene es delta dividida por la raíz cuadrada de U uno al cuadrado más U dos al cuadrado». Aclarar que el $k$ es común para que la expresión sea comparable a la normalización de incertidumbre de delta con esa cobertura.
>
> **[ERROR CRÍTICO]** No poner $u(\Delta)=0,25$ en el denominador de $E_n$: el denominador usa $U_1$ y $U_2$, es decir, $\sqrt{0,40^2+0,30^2}=0,50$. No comparar $\Delta$ con $u(\Delta)$ y llamarlo expandido.

El criterio acordado para este ejercicio es que el valor absoluto de $E_n$ sea menor o igual que uno. Aquí vale cero coma setenta. Para este caso particular, con $k=2$ e independencia, el criterio tiene un paralelo en ISO 6143 §6.1, que indica que este criterio «puede usarse» para contenidos determinados y preasignados; no le asigna un nivel de significación exacto ni lo convierte en regla universal [ISO 6143 §6.1]. La hipótesis nula que contrastamos es que los dos resultados estiman el mismo valor verdadero, es decir, que la diferencia entre esos valores es cero. Un $|E_n|\leq1$ significa que el criterio práctico no señala incompatibilidad; no es una prueba de equivalencia ni confirma que la hipótesis nula sea verdadera. Tampoco prueba conformidad con una tolerancia externa. Informamos la diferencia, las incertidumbres expandidas, el factor de cobertura común y el supuesto de independencia.

> **[PREGUNTA AL GRUPO]** Si $E_n$ resulta cero coma setenta, ¿podemos decir que los dos fotómetros son conformes? — *Respuesta esperada:* no; solo clasificamos la diferencia con el criterio de compatibilidad declarado. La conformidad requiere especificación y regla de decisión propias.
>
> **[ERROR CRÍTICO]** No presentar $|E_n|≤1$ como prueba de conformidad, equivalencia exacta ni validación independiente del instrumento. Informar siempre la diferencia, las incertidumbres expandidas, el factor de cobertura común y el supuesto de independencia.

### Escena B2. La cuadratura necesita independencia justificada

> **[DIAPOSITIVA]** Tres esquemas de procedencia de resultados: dos patrones sin causa común conocida; dos resultados que comparten un patrón; y una pareja con estructura de dependencia no caracterizada. En cada esquema, resaltar que la apariencia de las columnas no determina la independencia.

La palabra importante de la escena anterior es «independientes». La suma en cuadratura —sumar las varianzas y luego tomar la raíz cuadrada— es correcta si la covarianza entre los resultados es cero, o si el diseño y el modelo justifican tratarla como despreciable para el propósito. No concluyan que dos resultados son independientes solo porque se midieron por separado. Pueden compartir un patrón de referencia, una corrección, una calibración, una constante, un gas, o incluso entradas comunes de un presupuesto. La forma general se verá en el nivel I. Por ahora, el operador básico debe preguntar de dónde vienen las dos incertidumbres y detenerse si la dependencia posible no está incluida.

Supongamos que el SRP 55 se utiliza para calibrar el Level 2 y luego ambos resultados se comparan. Si el Level 2 conserva información del patrón SRP 55 usado en la calibración, ambos resultados pueden compartir una fuente. En ese escenario, no se puede insertar automáticamente $u_{1}$ y $u_{2}$ en la fórmula de independencia. Esto no significa que $E_n$ deje de ser válido por definición en todo caso que tenga un patrón compartido. Significa que no debemos usar, sin justificación, la versión de $E_n$ que asume cuadratura simple. Hace falta conocer o estimar la covarianza, o seleccionar otro método que represente adecuadamente la dependencia. Para nivel B basta con reconocerlo, no calcular esa covarianza.

> **[PIZARRA]** «¿Comparten patrón o información?» → si sí o no se sabe: no aplicar la cuadratura independiente sin justificación; consultar por el modelo de covarianza.
>
> **[NOTA AL INSTRUCTOR]** Reforzar la distinción: $E_n$ como indicador puede seguir siendo útil si se construye con las incertidumbres y dependencias que correspondan; la fórmula $√(U_{1}^{2}+U_{2}^{2})$ no se justifica cuando existe covarianza ignorada.

Volvamos a los números simulados. La clasificación $E_n=0,70$ solo se sostiene porque declaramos resultados independientes. Si descubrimos que comparten una fuente, el cálculo no se vuelve verdadero por haber sido reproducible: su supuesto quedó invalidado. La reproducibilidad del cálculo confirma la aritmética, no la adecuación del modelo. Esto es fundamental en el trabajo con patrones. La salida de una plantilla puede contener muchos decimales y aun así no responder a la pregunta correcta.

> **[PREGUNTA AL GRUPO]** ¿Compartir un patrón vuelve inválido todo indicador $E_n$? — *Respuesta esperada:* no. Lo que invalida sin más es asumir independencia y usar la cuadratura simple sin modelar o justificar la dependencia.

Por lo tanto, al comunicar una comparación básica, digan: «La diferencia se evaluó con la fórmula independiente porque las fuentes relevantes se modelaron como independientes». Si no podemos sostener esa frase, no afirmamos independencia. Anotamos qué información falta y escalamos. Este capítulo no convierte una correlación desconocida en cero ni asigna un número por intuición.

> **[ERROR CRÍTICO]** No llamar independiente a una pareja de resultados solo porque sus incertidumbres se reporten en certificados distintos. No ocultar una fuente compartida dentro de la incertidumbre de cada resultado y luego sumar en cuadratura como si la información fuera independiente.

> **[PRÁCTICA — fase de ejercicios]** Diferencia y $E_n$ en una comparación independiente

### Señales de escalamiento

Antes de terminar el nivel B, repasemos las señales para detenerse. Si los resultados comparten un patrón y la plantilla no tiene término de covarianza, se escala. Si no sabemos si el patrón es común o qué contribuciones están incluidas en los certificados, se escala. Si las unidades, el sentido de la diferencia, o los factores de cobertura no coinciden, primero hay que resolver esa inconsistencia; no se arregla con una etiqueta de compatibilidad. Si las incertidumbres se estimaron con pocas réplicas, o una sola fuente domina $U_1$ o $U_2$, también nos detenemos y revisamos los grados de libertad y la cobertura. Si el resultado está cerca de un límite de decisión, recordemos que la decisión corresponde a M10 y no al indicador de M09.

> **[ESCALAMIENTO]** El operador B detiene la cuadratura simple y consulta cuando hay indicios de patrón compartido o dependencia no documentada, cobertura no comparable, o modelo de incertidumbre no identificable. En el caso Level 2 frente al SRP 55, se identifica la información de covarianza necesaria y no se calcula una covarianza inexistente.
>
> **[TRANSICIÓN]** En I conservaremos la diferencia y añadiremos el término que faltaba cuando los resultados comparten una causa: la covarianza.

## Nivel I — modelar la dependencia antes de comparar

En I damos por visto todo B: la definición con signo de la diferencia, el uso de $E_n$ bajo las condiciones fijadas y la necesidad de justificar independencia. Ahora añadimos dos herramientas que permiten construir la incertidumbre de una comparación realista. Primero, la covarianza entre resultados, que puede aparecer por un patrón compartido. Segundo, la covarianza de los parámetros cuando usamos una recta para interpolar una diferencia. También vamos a separar una pregunta de compatibilidad estadística de una pregunta de conformidad. No repetiremos los fundamentos de incertidumbre de M8; los aplicaremos a la diferencia que estamos evaluando.

### Escena I1. La covarianza puede reducir o aumentar la incertidumbre de la diferencia

> **[DIAPOSITIVA]** Dos resultados conectados al mismo patrón común. Debajo, tres versiones de la correlación: positiva, nula y negativa. Resaltar que importa la covarianza, no solo el nombre de la fuente compartida.

La diferencia de dos resultados no se calcula cambiando la fórmula de resta. Seguimos definiendo delta como resultado dos menos resultado uno. Lo que cambia es su varianza. Para dos resultados cualesquiera, esta varianza contiene las dos varianzas individuales y resta dos veces la covarianza. La GUM presenta el tratamiento de entradas correlacionadas en su ley de propagación [GUM 5.2.2]. La deducción y la forma general de combinación lineal están en el Anexo AX.2; aquí nos concentramos en interpretar y usar la expresión.

> **[PIZARRA]** $u^2(\Delta)=u_1^2+u_2^2-2\,\operatorname{cov}(1,2)$.
>
> **[NOTA AL INSTRUCTOR]** Leer: «la varianza de delta es la varianza del resultado uno más la varianza del resultado dos menos dos veces la covarianza entre ambos». La covarianza tiene unidades al cuadrado, igual que las varianzas.

Si los resultados tienden a subir y bajar juntos, la covarianza es positiva y el término que se resta reduce la varianza de la diferencia. Tiene sentido: cuando una fluctuación común mueve ambos resultados en la misma dirección, una parte se cancela al restarlos. Si tienden a moverse en sentidos opuestos, la covarianza es negativa y restar dos veces un número negativo aumenta la varianza. Si no hay covarianza, recuperamos la regla independiente del nivel B. No digamos que toda fuente común se cancela por completo: la cancelación depende de su magnitud y de cómo afecte a cada resultado.

Veamos una ilustración **simulada**, distinta de cualquier resultado del laboratorio. Mantenemos incertidumbres estándar de cero coma veinte y cero coma quince nmol/mol. Para representar una causa compartida, supongamos una covarianza positiva de cero coma cero uno ocho (nmol/mol) al cuadrado. Las dos varianzas suman $0,0400+0,0225=0,0625$; el término que se resta es $2×0,018=0,0360$; por tanto, la varianza de la diferencia es $0,0265 (nmol/mol)^{2}$. Su raíz da $u(Δ)=0,1628 nmol/mol$, aproximadamente. Si hubiéramos supuesto independencia, habríamos obtenido cero coma veinticinco. El componente común positivo redujo la incertidumbre de la diferencia en esta ilustración.

> **[EJEMPLO]** Datos **simulados**: $u_{1}=0,20 nmol/mol$, $u_{2}=0,15 nmol/mol$, $cov(1,2)=0,018 (nmol/mol)^{2}$. Resultado: $u^{2}(Δ)=0,0265 (nmol/mol)^{2}$; $u(Δ)=0,1628 nmol/mol$.
>
> **[PIZARRA]** $0,20^2+0,15^2-2(0,018)=0,0265$; $u(\Delta)=\sqrt{0,0265}=0,1628\ \mathrm{nmol/mol}$.

La covarianza no se estima mirando la diferencia una vez. Debe provenir de un modelo de medición, de entradas comunes cuantificadas, de un diseño de datos o de una estimación respaldada por observaciones. En el caso Level 2 frente al SRP 55, la calibración del Level 2 transmite información del SRP 55 al resultado del fotómetro; al comparar después esos resultados, parte de esa trazabilidad puede ser común y producir covarianza. Para calcularla hacen falta las contribuciones y sensibilidades compartidas, además de la incertidumbre del resultado del SRP 55. Aquí no tenemos ese presupuesto desglosado, así que no asignamos un valor ni calculamos la covarianza. La dejamos como información necesaria para el análisis.

> **[PREGUNTA AL GRUPO]** ¿Una covarianza positiva grande puede hacer que la diferencia sea más precisa que cada resultado por separado? — *Respuesta esperada:* sí, porque parte de la variación común puede cancelarse en la resta; siempre que el modelo y la covarianza estén sustentados.
>
> **[NOTA AL INSTRUCTOR]** El ejemplo anterior muestra una mejora parcial: $u(\Delta)=0,1628$ nmol/mol, que todavía supera $u_2=0,15$ nmol/mol. En el límite de covarianza positiva admisible, $\operatorname{cov}(1,2)=u_1u_2=0,030\ (\mathrm{nmol/mol})^2$, resulta $u(\Delta)=0,05$ nmol/mol, menor que ambas incertidumbres individuales.
>
> **[ERROR CRÍTICO]** No reemplazar la covarianza por cero por conveniencia, no asignarle el signo por intuición y no sumar incertidumbres estándar en línea recta. Verificar además que la matriz de covarianza sea admisible; una varianza calculada negativa indica una incoherencia en entradas o modelo.

En una diferencia con dependencia, la incertidumbre expandida se calcula después de obtener la incertidumbre estándar. Declaramos la cobertura y el factor de cobertura de la diferencia: $U(\Delta)=k_\Delta u(\Delta)$. Si en esta ilustración suponemos $k_\Delta=2$, la incertidumbre expandida vale $0,3256\ \mathrm{nmol/mol}$. El factor dos es aquí un dato explícito, no una elección automática para toda comparación. Si además tomamos $k_\Delta=k$, al expandir la expresión de la varianza, el término de covarianza es $-2k^2\operatorname{cov}(1,2)$. Eso muestra cuánto aporta una causa común a la incertidumbre expandida de la diferencia [GUM 6.2.1].

> **[PIZARRA]** $U(\Delta)=k_\Delta u(\Delta)$; si $k_\Delta=k$, $U^2(\Delta)=k^2[u_1^2+u_2^2-2\,\operatorname{cov}(1,2)]$ y el término expandido es $-2k^2\operatorname{cov}(1,2)$.
>
> **[NOTA AL INSTRUCTOR]** Leer: «U de delta es k sub delta por u de delta. Si usamos el mismo factor k para delta y para los resultados, la covarianza aparece multiplicada por menos dos k al cuadrado».

Si decidimos normalizar la diferencia como $\Delta/U(\Delta)$, debemos decir que usamos una extensión del indicador $E_n$, no la definición del nivel B. La hipótesis nula sigue siendo que la diferencia entre los valores verdaderos es cero. La normalización y cualquier criterio de compatibilidad deben declararse con su cobertura y modelo de covarianza; un valor normalizado no demuestra equivalencia. En el ejemplo anterior solo propagamos la incertidumbre, sin clasificar compatibilidad con una tolerancia ni conformidad. La práctica del nivel I pedirá aplicar el modelo de covarianza del SRP 55 compartido y explicar el alcance de la conclusión, pero su desarrollo queda para la fase de ejercicios.

### Escena I2. Interpolar con una recta y propagar la covarianza de sus parámetros

> **[DIAPOSITIVA]** Una recta estimada $y=a+b·x$. Marcar una concentración de referencia $x_{0}$, el valor interpolado $a+b·x_{0}$, la línea identidad y la separación vertical $D(x_{0})$.

A veces no tenemos una pareja de lecturas directas exactamente en la concentración de interés. Usamos entonces una recta estimada en una comparación y calculamos la diferencia en un punto elegido. Supongamos que $x$ es el valor de referencia, $y$ la indicación, y la relación es $y=a+b·x$. La diferencia entre la indicación interpolada y el valor de referencia en $x_{0}$ es $D(x_{0})=a+b·x_{0}−x_{0}$, que también se escribe $a+(b−1)x_{0}$. Como $a$ y $b$ se estimaron conjuntamente, su covarianza interviene en la incertidumbre de esa diferencia. Este es un caso de propagación de una función de parámetros correlacionados [GUM 5.2.2; AX.2].

> **[PIZARRA]** $D(x_0)=a+(b-1)x_0$; $u^2[D(x_0)]=u^2(a)+x_0^2u^2(b)+2x_0\operatorname{cov}(a,b)$.
>
> **[NOTA AL INSTRUCTOR]** Leer: «D de equis cero es a más b menos uno por equis cero». Para la varianza, leer cada término y remarcar que el signo de la covarianza de parámetros se conserva.

Pongamos números **simulados**. Supongamos $a=0,12 nmol/mol$, $b=1,001$, y evaluamos en $x_{0}=200 nmol/mol$. La indicación interpolada sería $0,12+1,001×200=200,32 nmol/mol$; por lo tanto, la diferencia respecto a la referencia de 200 es $0,32 nmol/mol$. Supongamos además $u(a)=0,10 nmol/mol$, $u(b)=0,0005$ y $cov(a,b)=−0,000035 nmol/mol$. La covarianza negativa no se omite: su contribución a la varianza es $2×200×(−0,000035)=−0,014 (nmol/mol)^{2}$. La contribución de $u^{2}(a)$ es $0,0100$; la de $x_{0}^{2}u^{2}(b)$ es $0,0100$; al sumar el término cruzado queda $0,0060 (nmol/mol)^{2}$. La incertidumbre estándar de la diferencia es $0,07746 nmol/mol$.

> **[EJEMPLO]** Datos **simulados**: $a=0,12 nmol/mol$, $b=1,001$, $x_{0}=200 nmol/mol$, $u(a)=0,10 nmol/mol$, $u(b)=0,0005$, $cov(a,b)=−0,000035 nmol/mol$. Resultado: $D=0,32 nmol/mol$, $u(D)=0,07746 nmol/mol$.
>
> **[NOTA AL INSTRUCTOR]** El signo negativo de la covarianza de parámetros disminuye la varianza a este $x_{0}$. La matriz de covarianza debe ser admisible; los números se eligieron para que la varianza resultante sea no negativa.

¿De dónde viene la covarianza entre intercepto y pendiente? Del ajuste conjunto: al cambiar la pendiente, el intercepto puede compensar parcialmente el cambio en la recta, según la distribución de puntos y el modelo. Por eso, usar solo $u(a)$ y $u(b)$ e ignorar $\operatorname{cov}(a,b)$ puede sobrestimar o subestimar la incertidumbre del valor interpolado. La contribución relativa también cambia con $x_{0}$: aparece el factor $x_{0}$ en el término cruzado y $x_{0}^{2}$ en el de la pendiente. Así que la incertidumbre de la diferencia no tiene por qué ser constante a lo largo del intervalo.

> **[ERROR CRÍTICO]** No reemplazar la covarianza de los parámetros por cero cuando el ajuste entrega una matriz de covarianza, ni invertir el sentido de la diferencia sin cambiar el signo de $D$. No extrapolar fuera del intervalo de calibración solo porque la fórmula se pueda evaluar.

Ahora separemos dos palabras que suelen mezclarse. La **compatibilidad** pregunta cómo se relaciona una diferencia observada con su incertidumbre bajo un modelo estadístico. La **conformidad** pregunta si una magnitud cumple requisitos o límites definidos, con una regla de decisión y consideración del riesgo. Una diferencia compatible no es automáticamente una prueba de conformidad. Y una diferencia que no pasa un umbral de compatibilidad no identifica, por sí sola, cuál instrumento está mal ni cuál especificación se incumple. M10 tomará la incertidumbre y la regla de decisión para tratar esa pregunta distinta.

> **[PREGUNTA AL GRUPO]** Si $D(x_{0})$ es pequeño frente a su $U(D)$, ¿eso demuestra que el instrumento cumple su tolerancia? — *Respuesta esperada:* no; compara la diferencia bajo el modelo estadístico. La conformidad requiere una tolerancia y una regla de decisión definidas.
>
> **[PRÁCTICA — fase de ejercicios]** Diferencia con covarianza del SRP 55 compartido

> **[TRANSICIÓN]** En A dejaremos de trabajar solo con una diferencia de parámetros ya estimados. Representaremos todos los puntos y sus incertidumbres en matrices, ajustaremos la relación generalizada y examinaremos su consistencia.

## Nivel A — modelar la comparación con matrices y referencia común

En este nivel damos por vistos B e I: la diferencia con signo, el término de covarianza entre resultados, la propagación de parámetros de una recta y la distinción entre compatibilidad y conformidad. Ahora añadimos la formulación matricial y el método generalizado de regresión para comparar valores con incertidumbre tanto en el eje de referencia como en el de indicación. El alcance didáctico está restringido a $V_{xy}=0$, es decir, no incluimos covarianza cruzada entre ejes. También examinaremos la consistencia del ajuste mediante chi-cuadrado y definiremos el grado de equivalencia frente a una referencia común; el cálculo numérico adaptado será una diferencia interpolada respecto al patrón de trabajo SRP 7. No vamos a estudiar el protocolo ni la organización de BIPM.QM-K1, la base de datos de comparaciones clave (KCDB, por sus siglas en inglés), ni GGMR con $V_{xy}\neq0$ [prop_e §6].

### Escena A1. De incertidumbres por punto a matrices de covarianza

> **[DIAPOSITIVA]** Doce puntos en un plano, con una línea ajustada. Al costado aparecen las matrices $U_x$, $U_y$ y $V_{xy}$; en esta lección se destaca $V_{xy}=0$ y dos bloques internos no diagonales.

En los niveles anteriores calculamos la incertidumbre de una diferencia a partir de dos resultados, o propagamos la covarianza de dos parámetros. En una comparación con muchos puntos, necesitamos organizar las incertidumbres y dependencias de todo el conjunto. Una matriz de covarianza contiene las varianzas en la diagonal y las covarianzas entre distintos puntos fuera de la diagonal. Separamos la matriz del eje de referencia, $U_x$, la del eje de indicación, $U_y$, y la covarianza cruzada entre ejes, $V_{xy}$. La especificación técnica ISO/TS 28037 presenta el modelo GGMR con incertidumbres y covarianzas asociadas a las mediciones de ambos ejes, junto con un procedimiento iterativo para ajustar la recta y estimar la covarianza de sus parámetros [ISO 28037 §10.1–10.2].

> **[PIZARRA]** $V=\begin{bmatrix}U_x&V_{xy}\\V_{xy}^{T}&U_y\end{bmatrix}$; alcance de este capítulo: $V_{xy}=0$.
>
> **[NOTA AL INSTRUCTOR]** Leer: «uve es la matriz de covarianza conjunta; sus bloques diagonales son U equis y U ye, y el bloque cruzado es V equis ye». Aclarar que $V_{xy}=0$ es una hipótesis del ejemplo, no un resultado general de independencia entre ejes.

¿Qué significa ajustar con incertidumbre en ambos ejes? En vez de tratar cada valor de referencia como exacto y mover solo las indicaciones hacia la recta, GGMR estima también valores latentes sobre el eje de referencia. La línea se determina teniendo en cuenta la distancia ponderada de los puntos observados y la matriz de incertidumbre. El §10 describe la suma generalizada de cuadrados, la iteración y la evaluación de la incertidumbre de los parámetros; su ejemplo incluye covarianzas internas de los ejes y fija $V_{xy}=0$ [ISO 28037 §10.1–10.3; Tablas 25–26]. La formulación detallada y las deducciones se dejan para AX.8. Aquí nos interesa entender qué información entra y qué controles salen.

La matriz importa porque una causa compartida puede correlacionar varios puntos del mismo eje. Por ejemplo, un componente relativo común del patrón genera covarianzas entre concentraciones diferentes: al aumentar el nivel de concentración, la contribución común puede crecer en el mismo sentido para varios puntos. En el modelo publicado del BIPM-SRP27, el Apéndice 1 identifica variables comunes de medición —temperatura, presión y longitud óptica— para las mediciones realizadas con el SRP, y expresa su componente relativa común como $u_b=2,92×10^{-3}$ [BIPM-K1, Apéndice 1 §3, ec. 21]. El documento también presenta otro valor en un apartado previo.
>
> **[NOTA AL INSTRUCTOR]** El Apéndice 1 §1 escribe $2,89×10^{-3}$ y el §3, ecuación 21, escribe $2,92×10^{-3}$. Para esta adaptación usamos el valor de la ecuación 21. No asumimos que ese componente describa el SRP 36, el SRP 7 ni los patrones de CALAIRE.

Esa contribución compartida explica por qué puede haber elementos no nulos fuera de la diagonal de una matriz de covarianza.

> **[PREGUNTA AL GRUPO]** Si dos concentraciones del mismo eje comparten una contribución de escala, ¿dónde aparece esa dependencia? — *Respuesta esperada:* en las covarianzas fuera de la diagonal de la matriz del eje, no solo en sus varianzas individuales.

Vamos a fijar ahora el caso docente y sus límites. Los doce pares de la Figura 14.2 del SRP QAPP se publican como resultados de SRP 36 y SRP 7, con desviaciones estándar por punto [SRP-QAPP, Element 14.2, Figura 14.2]. Esos datos son **publicados**, y describen una verificación de esos instrumentos en el contexto del QAPP; no son registros de CALAIRE. Para el cálculo didáctico, orientamos la comparación como $x=SRP 7$ y $y=SRP 36$. Esta orientación permite definir el SRP 7 como referencia y el SRP 36 como resultado comparado. No es la orientación del ajuste impreso en la figura, así que no se deben copiar los coeficientes publicados como si pertenecieran a esta recta.

Las incertidumbres y covarianzas que usaremos para el ejemplo A son **adaptadas**. Por eje, tomamos una contribución aleatoria diagonal y añadimos una contribución común proporcional a los valores del eje, con el coeficiente relativo usado en el modelo SRP27 publicado. Para construir la parte diagonal, suponemos que cada desviación estándar de la figura describe doce lecturas y usamos su cociente por la raíz de doce como incertidumbre estándar de la media; la figura no especifica ese supuesto como tal. Este modelo se aplica por separado a cada eje; establecemos $V_{xy}=0$ para poder impartir el cálculo dentro del alcance del curso. Es una hipótesis fuerte y solo didáctica. No reconstruye la incertidumbre real del QAPP ni el presupuesto de los SRP 36 y 7. La separación es importante: los pares observados están publicados; las incertidumbres del ajuste son adaptadas; el resultado que vamos a calcular también es un resultado didáctico adaptado.

> **[EJEMPLO]** Origen: pares **publicados** de SRP QAPP, Figura 14.2; modelo de incertidumbre **adaptado** del SRP27, con $u_b=0,00292$ y $V_{xy}=0$. Orientación didáctica: referencia $x=SRP 7$; resultado $y=SRP 36$. No es un resultado oficial ni pertenece a CALAIRE.
>
> **[ERROR CRÍTICO]** No atribuir el ajuste GGMR, sus incertidumbres, su chi-cuadrado ni sus grados de equivalencia a CALAIRE o al resultado oficial del QAPP. No presentar $V_{xy}=0$ como hecho medido; es una hipótesis declarada del caso. No extender la conclusión a covarianza cruzada no nula.

Para ajustar, el método busca una recta $y=a+b·x$ y los valores latentes de $x$ que minimizan la suma de residuos ponderada por la matriz conjunta. En la salida aparecen el intercepto, la pendiente, sus incertidumbres estándar y su covarianza. La matriz de covarianza de $a$ y $b$ no es un detalle optativo: es la que usamos después para propagar una diferencia interpolada. En el ejemplo, el ajuste adaptado de los doce pares produce $a=−0,184237 nmol/mol$, $b=0,998350748$, $u(a)=0,031189 nmol/mol$, $u(b)=0,004125035$ y $cov(a,b)=−3,83046×10⁻⁶ nmol/mol$. Estos valores se reproducen en el script del capítulo. No son parámetros de una calibración oficial.

> **[PIZARRA]** GGMR estima conjuntamente la recta y las posiciones latentes; para el caso, $y=a+b x$ y $V_{xy}=0$. Resultado adaptado: $a=-0,184237$, $b=0,998350748$.
>
> **[NOTA AL INSTRUCTOR]** Leer: «ye es igual a a más b por equis; GGMR estima la recta y las posiciones de referencia latentes, con covarianza cruzada entre ejes nula en este caso». Leer después las cifras con unidades. El intercepto y su incertidumbre tienen unidades de nmol/mol; la pendiente es una razón y no lleva esas unidades.

Después del ajuste revisamos consistencia con chi-cuadrado. La cláusula 10 de ISO/TS 28037 define el estadístico observado a partir de los residuos transformados con la factorización de Cholesky y usa $ν=m−2$ grados de libertad para la recta; indica compararlo con el cuantil del 95 % de la distribución chi-cuadrado bajo las condiciones del modelo [ISO 28037 §10.3]. Para doce pares, $ν=10$. El ajuste adaptado da $χ^{2}_obs=6,3183$, y el cuantil 95 % es $18,3070$. Como $6,3183$ no excede $18,3070$, este control no señala una inconsistencia de la recta y datos bajo el modelo usado.

> **[PIZARRA]** $\nu=m-2=10$; $\chi^2_{obs}=6,3183$; $\chi^2_{0,95;10}=18,3070$.
>
> **[NOTA AL INSTRUCTOR]** Estos son resultados adaptados calculados por el script. No interpretar el cuantil como un límite de tolerancia ni el resultado como prueba de equivalencia.

La conclusión es deliberadamente acotada. No rechazar por este criterio la consistencia del modelo no prueba que el modelo sea verdadero, que las incertidumbres sean exactas, ni que la comparación demuestre conformidad. El chi-cuadrado bajo o moderado debe leerse en relación con las incertidumbres declaradas y el modelo, no como una puntuación de calidad. Los puntos del QAPP están redondeados y el modelo del SRP27 no sustituye los presupuestos reales de esos dos instrumentos. El chi-cuadrado tampoco resuelve una dependencia cruzada omitida. La hipótesis $V_{xy}=0$ debe mantenerse a la vista cada vez que se informe el resultado.

> **[PREGUNTA AL GRUPO]** ¿Basta con que $\chi^2_{obs}$ quede por debajo del cuantil para demostrar equivalencia entre los patrones? — *Respuesta esperada:* no; solo indica que esta prueba no señala falta de consistencia del modelo de recta bajo las incertidumbres y supuestos declarados.

### Escena A2. Grado de equivalencia y diferencia interpolada respecto a un patrón de trabajo

> **[DIAPOSITIVA]** Un recuadro central «referencia común: BIPM-SRP27» conectado a los puntos de la comparación; junto a él, $D(x_{0})$ y $u(D)$, seguidos por separado de un indicador normalizado opcional.

En una comparación clave se informa la diferencia de un participante respecto al valor de referencia clave, o KCRV, en una concentración especificada. El KCRV es el valor que el protocolo de esa comparación designa como referencia para evaluar las diferencias; aquí no lo tratamos como un promedio que vayamos a recalcular. En BIPM.QM-K1, el protocolo designa al BIPM-SRP27 como referencia y define respecto de él la diferencia del estándar nacional, $D$, con su incertidumbre [BIPM-K1, Protocolo A §8, ecs. 2–3]. Esta es la definición operacional que necesitamos; no derivaremos ni reconstruiremos el valor de referencia. No estudiaremos el protocolo, la organización ni la KCDB, la base de datos de comparaciones clave (por sus siglas en inglés).

La ecuación 3 del Protocolo A §8 combina las incertidumbres en cuadratura. Como vimos en B2, esa forma requiere justificar independencia o covarianza nula; no se aplica automáticamente cuando los resultados comparten información. El Protocolo A §7, ecuación 1, representa una contribución común mediante un término de covarianza. En este capítulo mantenemos esa dependencia en la matriz de covarianza adaptada y no añadimos de nuevo la incertidumbre del patrón como si fuera independiente [BIPM-K1, Protocolo A §7, ec. 1; §8, ecs. 2–3].

En una comparación con ajuste lineal, puede que el valor comparado se obtenga por interpolación en lugar de contar con mediciones directas exactamente en el punto nominal. El protocolo distingue el valor del estándar participante y el del SRP27 como referencia [BIPM-K1, Protocolo A §§7–8]. En nuestro caso didáctico usamos la recta adaptada $y=a+b·x$, donde $x$ es el patrón de trabajo SRP 7 e $y$ es el resultado comparado SRP 36. Por tanto, calculamos una diferencia interpolada respecto al SRP 7, $D_{36-7}(x_{0})=a+(b−1)x_{0}$. No la llamamos grado de equivalencia frente al KCRV: el KCRV de BIPM.QM-K1 es BIPM-SRP27, no SRP 7. Su varianza se calcula con la incertidumbre y covarianza de los parámetros: $u^2(D)=u^2(a)+x_0^2u^2(b)+2x_0\operatorname{cov}(a,b)$. La incertidumbre de la referencia queda representada en el ajuste y en las matrices usadas; no se añade otra vez como si fuera independiente, porque eso duplicaría información. Para comparar con un protocolo que evalúa mediciones directas, primero habría que respetar exactamente qué resultados y covarianzas contiene cada fórmula [GUM 5.2.2; AX.9].

> **[PIZARRA]** $D_{36-7}(x_0)=a+(b-1)x_0$; $u^2(D_{36-7})=u^2(a)+x_0^2u^2(b)+2x_0\operatorname{cov}(a,b)$.
>
> **[NOTA AL INSTRUCTOR]** Leer: «D sub treinta y seis menos siete, de equis cero, es la diferencia interpolada del SRP 36 respecto al SRP 7 en la concentración de referencia equis cero». Mantener explícita la orientación de los ejes y el signo: resultado comparado menos referencia.

Regresemos al ajuste adaptado y evaluemos en ochenta nmol/mol. Con $a=−0,184237121$ y $b=0,998350748$, la diferencia es aproximadamente $−0,316177 nmol/mol$. Su incertidumbre estándar, propagando la matriz de covarianza del intercepto y la pendiente, es $0,330548 nmol/mol$. A cuatrocientos veinte nmol/mol, $D$ es aproximadamente $−0,876923 nmol/mol$ y $u(D)=1,731867 nmol/mol$. Son cifras del script, que usa los pares publicados redondeados del QAPP con el modelo de incertidumbre adaptado. La diferencia negativa indica que, bajo nuestra orientación, el resultado SRP 36 interpolado queda por debajo del SRP 7. La incertidumbre mayor al punto alto refleja la contribución de pendiente y covarianza en la propagación; no la resumimos con una única incertidumbre para todo el intervalo.

> **[EJEMPLO]** Caso **adaptado** (datos de entrada **publicados** del QAPP; modelo de incertidumbre basado en SRP27 y $V_{xy}=0$): a $80\ \mathrm{nmol/mol}$, $D_{36-7}=−0,316177\ \mathrm{nmol/mol}$, $u(D)=0,330548 nmol/mol$; a $420\ \mathrm{nmol/mol}$, $D_{36-7}=−0,876923\ \mathrm{nmol/mol}$, $u(D)=1,731867 nmol/mol$.
>
> **[NOTA AL INSTRUCTOR]** Aclarar que la referencia común del marco curricular de BIPM.QM-K1 es BIPM-SRP27. SRP 7 se usa aquí como eje de referencia del caso didáctico SRP 36/SRP 7, no se identifica con SRP27. Los resultados no son oficiales ni de CALAIRE.

La cifra de diferencia y su incertidumbre son los resultados principales que debemos comunicar. Para el grado de equivalencia frente al KCRV, la hipótesis nula es que la diferencia verdadera del participante respecto a esa referencia es cero. Si se calcula una incertidumbre expandida, se declara su factor de cobertura; cualquier indicador normalizado se identifica aparte y no se confunde con el grado de equivalencia. El cálculo numérico anterior es solo la diferencia interpolada SRP 36 menos SRP 7; no contrasta el grado de equivalencia frente al KCRV.

El caso curricular de comparación entre el SRP 55 y BIPM-SRP27 serviría para expresar el grado de equivalencia del SRP 55 respecto a esa referencia común. Aquí describimos la pregunta y la definición, pero no tenemos en este libreto un conjunto de datos y un presupuesto completo para calcularlo. Por eso no inventamos cifras ni presentamos el ajuste SRP 36/SRP 7 como si fuera esa comparación.

> **[PIZARRA]** Informe en columnas separadas: $D(x_{0})$; $u(D)$ o $U(D)$ con cobertura; indicador normalizado, si se utiliza, identificado aparte.
>
> **[NOTA AL INSTRUCTOR]** Leer: «informamos la diferencia respecto a la referencia, su incertidumbre y, si corresponde, el indicador normalizado en columnas distintas».

En el ejemplo A, la condición de referencia común es importante. No calculamos un KCRV combinado en el que participe el mismo laboratorio cuyo resultado se evalúa. Tampoco incluimos la variante de incertidumbre cruzada $V_{xy}\neq0$; esa posibilidad está excluida del alcance de este curso. El caso SRP 36/SRP 7 solo ilustra una diferencia interpolada respecto a un patrón de trabajo. El grado de equivalencia frente a BIPM-SRP27 se define conceptualmente a partir del Protocolo A §8, pero no calculamos aquí ese grado de equivalencia porque no hay datos y presupuestos apropiados para hacerlo.

> **[ERROR CRÍTICO]** No atribuir a CALAIRE el caso SRP 36/SRP 7 ni presentar el resultado adaptado como oficial. No confundir $D$ con $D/U(D)$; no combinar la referencia con la participación del mismo laboratorio; no ocultar los supuestos $V_{xy}=0$ y covarianzas intraje declaradas. Un resultado de comparación aporta evidencia para evaluar una CMC, pero no equivale a su aprobación.
>
> **[ESCALAMIENTO]** Si hay covarianza cruzada entre ejes, matriz no admisible, datos originales insuficientes, ajuste que no converge o discrepancia con una implementación validada, no se fuerza el GGMR de este capítulo. Se detiene la interpretación y se consulta por un modelo y una herramienta dentro del alcance técnico requerido.

La comparación produce una evidencia sobre la relación estadística entre un resultado y su referencia bajo un modelo. El hecho de que el ajuste sea consistente no prueba por sí solo que los instrumentos sean conformes ni que exista equivalencia absoluta. La conformidad requiere criterios y reglas de decisión; la evaluación de una CMC requiere un juicio técnico más amplio que un único indicador. Por eso mantenemos separados estos productos: los parámetros de la recta, la prueba de consistencia del ajuste, el grado de equivalencia y cualquier decisión posterior.

> **[PRÁCTICA — fase de ejercicios]** Comparación con referencia común y grado de equivalencia

## Cierre del capítulo

Hagamos una síntesis antes de pasar a M10. En B definimos la diferencia con signo, calculamos $E_n$ con incertidumbres expandidas y un factor común, y solo usamos la cuadratura simple cuando la independencia está justificada. En I añadimos la covarianza: una causa común puede reducir o aumentar la incertidumbre de la diferencia, y una recta interpolada requiere propagar también la covarianza entre sus parámetros. En A organizamos la dependencia en matrices, aplicamos GGMR dentro del alcance $V_{xy}=0$, examinamos la consistencia con chi-cuadrado y distinguimos el grado de equivalencia frente a una referencia común de la diferencia interpolada SRP 36 menos SRP 7 que calculamos en el ejemplo adaptado.

Quiero que se lleven tres separaciones claras. Primero, diferencia no es incertidumbre: reportamos ambas. Segundo, compatibilidad no es conformidad: un indicador de comparación no sustituye la especificación ni la regla de decisión. Tercero, un cálculo reproducible no valida por sí solo sus hipótesis: declaramos origen de datos, modelo de covarianza, cobertura y límites. En el siguiente módulo vamos a usar el resultado y su incertidumbre para formular reglas de decisión y estudiar el riesgo asociado a aceptar o rechazar.

> **[TRANSICIÓN]** M10 toma la incertidumbre y las diferencias aquí modeladas y pregunta cómo decidir frente a un requisito, sin confundir compatibilidad estadística con conformidad.

## Referencias del capítulo

- **GUM.** JCGM 100:2008 (ISO/IEC Guide 98-3:2008), *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*. JCGM, 2008. Archivo: `docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf`.
- **ISO 28037.** ISO/TS 28037:2010, *Determination and use of straight-line calibration functions*. International Organization for Standardization, 2010. Archivo: `docs/ISO 28037.pdf`.
- **BIPM-K1.** BIPM, *Protocol for BIPM.QM-K1, On-demand Key Comparison of Ozone at Ambient Level*, versión 2.1, 9 de octubre de 2025. Archivo: `docs/BIPM.QM-K1_2.protocol.pdf`.
- **ISO 6143.** ISO 6143:2001, *Gas analysis — Comparison methods for determining and checking the composition of calibration gas mixtures*. International Organization for Standardization, 2001. Archivo: `docs/ISO 6143 2001.pdf`.
- **SRP-QAPP.** U.S. Environmental Protection Agency, Office of Air Quality Planning and Standards, *Quality Assurance Project Plan for the Standard Reference Photometer Program*, febrero de 2017. Archivo: `docs/srp_qapp.pdf`.
