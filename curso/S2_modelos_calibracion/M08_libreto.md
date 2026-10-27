# M08. Propagación de incertidumbre

## Ficha del capítulo

| Elemento | Contenido |
|---|---|
| Competencia estadística | Construir un presupuesto coherente con el resultado de interés y propagar varianzas y covarianzas. |
| Prerrequisitos | M1: modelo y entradas de medición; M3: incertidumbre estándar, distribuciones y dependencia; M4: estimación y grados de libertad; M6: componentes de precisión; M7: función de calibración y predicción inversa. Los niveles son acumulativos: I comprende B y A comprende B e I. |
| Nivel B | Modelo de medición; evaluaciones tipo A y tipo B; conversión $u=U/k$, resolución y tolerancias; elección entre $s_r$ y $s_r/\sqrt{n}$; presupuesto tabular con sensibilidades numéricas (Kragten) para entradas independientes; incertidumbre combinada y expandida; uso condicional de $k\approx 2$. |
| Nivel I añade | Sensibilidades analíticas; covarianzas; grados de libertad efectivos y cobertura; incertidumbre de una observación individual, promedio de calibración y resultado futuro; evitar doble conteo entre residuo de regresión y precisión; propagar por la cadena SRP 55 → Level 2 → cliente; límites de Student y Welch–Satterthwaite según el modelo. |
| Nivel A añade | Componentes comunes en resultados absolutos y diferencias; límites de la linealización; función de incertidumbre a lo largo de un intervalo y su comparación con una capacidad de medición y calibración (CMC) disponible a clientes bajo condiciones normales [CIPM MRA-G-13], de igual magnitud, unidades y cobertura. |
| Datos de ejemplo | Todos los ejemplos numéricos de presupuesto, sensibilidad, cobertura, cadena y CMC son **simulados** y están fijados en `calc/M08_ejemplos.py`; las prácticas simuladas también se reproducen con `calc/M08_practicas_luna.py`. No representan resultados del laboratorio. El certificado F-PSMT-01 y la cadena del laboratorio son contexto **propio**, sin derivar de ellos cifras de desempeño. |
| Anexos | AX.2: combinaciones lineales y covarianza; AX.3: distribuciones rectangulares y triangulares; AX.4: cuadrados medios esperados y $u^2_{\mathrm{prec}}$ del promedio; AX.7: Welch–Satterthwaite y condiciones. |
| Referencias clave | GUM (JCGM 100); GUM-6; *Introduction to Statistics in Metrology*, caps. 6–7; *Metrology and Measurement Uncertainty*, caps. 5–6. Los numerales externos citados se verificaron con `pdftotext`; ver bitácora. |

## Nivel B — formar un presupuesto para el resultado que se informa

En el nivel básico damos por vistos el modelo de medición, la diferencia entre una lectura y un promedio, y las distribuciones sencillas de M3. Aquí vamos a organizar esas piezas para responder una pregunta práctica: ¿qué incertidumbre corresponde al número que queremos informar? No empezamos por una lista genérica de contribuciones. Empezamos por nombrar el resultado y escribir cómo se obtiene. En la GUM, el modelo expresa la relación entre la magnitud de salida y las magnitudes de entrada; GUM-6 dedica sus apartados sobre ecuaciones de observación y modelos de calibración a formular esa relación [GUM 4.1; GUM-6 11.2–11.4].

### Escena B1. Primero se define el resultado

> **[DIAPOSITIVA]** Un esquema con una casilla «entradas», una función $f(\ldots)$ y una casilla «resultado de interés»; debajo, tres etiquetas: lectura individual, promedio de calibración y uso futuro.

Miren esta diapositiva. La incertidumbre no pertenece a una columna aislada por naturaleza; pertenece al resultado que definimos con un modelo. Si reportamos un valor corregido, el modelo puede ser una función de la indicación y de la corrección. Si usamos una recta de calibración, el valor de uso se obtiene con la predicción inversa. Si informamos el promedio de un conjunto, entran tanto la dispersión de las observaciones como las demás fuentes pertinentes. Por eso, antes de sumar incertidumbres, digan en voz alta: cuál es la respuesta, cuál es la magnitud de interés, en qué unidad se expresa y qué observaciones o periodo representa [GUM 4.1; GUM-6 11.2–11.4].

En la pizarra escribo el modelo general. La salida $Y$ es una función de las entradas $X_1$ hasta $X_n$. Dicho en palabras: el resultado se calcula aplicando una regla definida a los valores de entrada. En el ejemplo, el valor de uso $\hat{x}$ se obtiene restando el intercepto $a$ de la indicación media $y$ y dividiendo por la pendiente $b$. Es la inversión de la recta de calibración; mantenemos la convención de M7: referencia $x$, indicación $y$ y recta $y=a+b\cdot x$ [ISO 28037 §§11.1.1–11.1.3].

> **[PIZARRA]** $$\hat{x}=f(y,a,b)=\frac{y-a}{b}$$
>
> **[NOTA AL INSTRUCTOR]** Leer: «equis sombrero es igual a y menos a, todo dividido por b». Aclarar que la fórmula sirve aquí para mostrar el presupuesto; no se está presentando como certificado ni como cálculo real de CALAIRE.

Ahora separamos dos maneras de evaluar contribuciones. Una evaluación tipo A usa análisis estadístico de observaciones, por ejemplo, la dispersión de lecturas repetidas bajo un diseño definido. Una evaluación tipo B usa otra información disponible: una especificación, un certificado, una resolución, experiencia documentada o una distribución asignada a un límite. Los nombres tipo A y tipo B describen el método de evaluación, no una jerarquía de calidad ni dos clases de efectos físicos. Una fuente de incertidumbre no deja de existir porque la evaluemos por una u otra vía [GUM 3.3.4–3.3.5; Crowder 2020 §6.2.2–6.2.3].

> **[PREGUNTA AL GRUPO]** Si repetimos ocho veces una lectura y además tenemos una tolerancia del certificado, ¿las dos incertidumbres salen del mismo cálculo? — *Respuesta esperada:* no; la dispersión de repeticiones se evalúa con los datos, mientras la tolerancia se transforma según la información y distribución que declara el certificado.

Veamos un ejemplo con números. Es un conjunto **simulado**, preparado para esta clase. Ocho lecturas de un mismo día dan una media de $100{,}60\ \mathrm{nmol/mol}$. La ficha del ejemplo entrega además una repetibilidad $s_r=0{,}24\ \mathrm{nmol/mol}$, evaluada por separado con mayor resolución a partir de ocho observaciones independientes de un proceso normal y estable. Se suministran siete grados de libertad para esa estimación; no es la desviación de estas mismas lecturas redondeadas. La resolución digital total es $\delta=0{,}10\ \mathrm{nmol/mol}$. Para la media de ocho observaciones independientes, la parte tipo A es $s_r/\sqrt{8}=0{,}0849\ \mathrm{nmol/mol}$. Suponemos que el error de cuantización es rectangular, independiente entre lecturas e independiente de esa repetibilidad. Con esos supuestos, su incertidumbre estándar es $\delta/\sqrt{12}=0{,}0289\ \mathrm{nmol/mol}$. Para el promedio de ocho errores de cuantización independientes, esa parte baja a $0{,}0102\ \mathrm{nmol/mol}$. Si $s_r$ se hubiera calculado con las mismas lecturas redondeadas, la cuantización ya estaría en parte dentro de ella y no se sumaría otra vez sin justificarlo. En este modelo las dos fuentes están separadas, y la combinación de ambas partes de la entrada $y$ es $0{,}0855\ \mathrm{nmol/mol}$. Las cifras se reproducen en el script del capítulo. El divisor $\sqrt{8}$ corresponde a la media de ocho lecturas independientes, no a cualquier resultado con ocho cifras [GUM 4.2; Crowder 2020 §6.2.2–6.2.4; MMU §5.3.1; AX.3].

Para completar el modelo simulado, supongamos que el intercepto estimado vale $a=0{,}40\ \mathrm{nmol/mol}$ con incertidumbre estándar $u(a)=0{,}15\ \mathrm{nmol/mol}$, y que la pendiente vale $b=1{,}002$ con incertidumbre estándar $u(b)=0{,}002$. En esta primera escena supongo explícitamente que las tres entradas $y$, $a$ y $b$ son independientes. Los parámetros $a$ y $b$ se suministran con distribuciones aproximadamente normales y grados de libertad grandes; no proceden del ajuste OLS de M07, cuyos parámetros sí están correlacionados. La aproximación normal de cobertura de B3 se apoya en la linealidad local y en los grados de libertad grandes de $a$ y $b$; no depende solo de los grados de libertad. La sustitución da $\hat{x}=(100{,}60-0{,}40)/1{,}002=100{,}000\ \mathrm{nmol/mol}$. El cero redondo es intencional: hace más fácil seguir el cálculo, pero no cambia el hecho de que sus entradas inciertas producen una incertidumbre distinta de cero.

> **[EJEMPLO]** Datos **simulados**: ocho lecturas; $\bar{y}=100{,}60\ \mathrm{nmol/mol}$, $s_r=0{,}24\ \mathrm{nmol/mol}$, resolución total $\delta=0{,}10\ \mathrm{nmol/mol}$; $a=0{,}40\ \mathrm{nmol/mol}$, $u(a)=0{,}15\ \mathrm{nmol/mol}$; $b=1{,}002$, $u(b)=0{,}002$. Valor de uso $\hat{x}=100{,}000\ \mathrm{nmol/mol}$. 
>
> **[NOTA AL INSTRUCTOR]** Dejar visible el rótulo «simulado». No decir «CALAIRE obtuvo 100,000» ni insinuar que los parámetros provienen del certificado.

La primera conclusión docente es que el modelo y la definición del resultado determinan qué entradas intervienen. En esta ilustración el resultado es el valor inverso asociado a una media de ocho lecturas. Si la pregunta fuera la incertidumbre de una lectura futura, no bastaría con cambiar el título del presupuesto: habría que incorporar las fuentes que afectan a esa observación futura. Volveremos a esa distinción en el nivel intermedio.

### Escena B2. Convertir la información a incertidumbre estándar

> **[DIAPOSITIVA]** Mostrar tres tarjetas: «certificado: `U` y `k`», «resolución: intervalo de cuantización» y «tolerancia: límites y distribución». En un borde, «llevar todas las contribuciones a incertidumbre estándar `u`».

Ahora hagamos comparables las entradas. El presupuesto se expresa con incertidumbres estándar $u$, es decir, magnitudes equivalentes a desviaciones estándar bajo el modelo adoptado. Si el certificado informa una incertidumbre expandida $U$ y un factor de cobertura $k$, la conversión es $u=U/k$. Si informa solo una tolerancia, necesitamos entender cómo se interpreta: con límites simétricos $\pm h$ y distribución rectangular, la incertidumbre estándar es $h/\sqrt{3}$; si $\delta$ es la resolución total de un instrumento digital, su contribución rectangular es $\delta/\sqrt{12}$. No intercambien $h$ y $\delta$: la primera notación es semiamplitud desde el centro hasta un límite; la segunda es el ancho completo entre límites [GUM 4.3; Crowder 2020 §6.2.1–6.2.3; MMU §§5.2.2–5.3.1; AX.3].

> **[PIZARRA]** $u=U/k$; si el intervalo es rectangular $[-h,h]$, entonces $u=h/\sqrt{3}$; si la resolución total es $\delta$, entonces $u=\delta/\sqrt{12}$. 
>
> **[NOTA AL INSTRUCTOR]** Leer cada símbolo y la condición de distribución. No presentar la distribución rectangular como regla automática para toda tolerancia.

Con los datos didácticos de la escena anterior, $\delta=0{,}10\ \mathrm{nmol/mol}$ significa un ancho total de $0{,}10\ \mathrm{nmol/mol}$; la incertidumbre de una lectura es $0{,}10/\sqrt{12}=0{,}0289\ \mathrm{nmol/mol}$. Un certificado hipotético que declarara $U=0{,}30\ \mathrm{nmol/mol}$ con $k=2$ aportaría $u=0{,}15\ \mathrm{nmol/mol}$. Si, en cambio, una tolerancia acotara un error entre $-0{,}30$ y $+0{,}30\ \mathrm{nmol/mol}$ y justificáramos una distribución rectangular, su $u$ sería $0{,}30/\sqrt{3}=0{,}1732\ \mathrm{nmol/mol}$. Fíjense: los mismos números de límite no autorizan a intercambiar las dos interpretaciones. En el primer caso se convierte una incertidumbre expandida ya evaluada; en el segundo, se modela un intervalo de tolerancia como rectangular [Crowder 2020 §6.2.3–6.2.5; MMU §§5.2.2–5.3.1; AX.3].

La dispersión también depende de qué queremos reportar. $s_r$ estima la desviación de lectura dentro del día. Para la media de $n$ observaciones independientes, $s_r/\sqrt{n}$ estima la incertidumbre estándar de esa media. En nuestro ejemplo, $s_r=0{,}24$ y $n=8$, por eso $s_r/\sqrt{8}=0{,}0849\ \mathrm{nmol/mol}$. No digan que la dispersión del instrumento pasó a ser $0{,}0849$: cada lectura conserva su dispersión. El cociente se refiere a la media bajo los supuestos del diseño. Una deriva o un componente común no se elimina al tomar más lecturas y no recibe un divisor automático por raíz de $n$ [GUM 4.2; Crowder 2020 §6.2.2 y §6.2.4].

> **[PIZARRA]** $u(\bar{y})=s_r/\sqrt{n}$ solo para la media de observaciones independientes; para una observación individual, la dispersión de lectura se representa por $s_r$.
>
> **[ERROR CRÍTICO]** No dividir por $\sqrt{n}$ una incertidumbre común, una deriva, una tolerancia del equipo o la incertidumbre de un patrón compartido solo porque se hayan tomado $n$ lecturas. El divisor depende del resultado y del modelo de dependencia.

> **[PREGUNTA AL GRUPO]** ¿Qué es menor en el ejemplo, la dispersión de una lectura o la incertidumbre de la media de ocho? — *Respuesta esperada:* la incertidumbre estándar de la media es menor si las lecturas son independientes; la dispersión de lectura sigue siendo $s_r=0{,}24\ \mathrm{nmol/mol}$. 

### Escena B3. Presupuesto tabular y combinación de entradas independientes

> **[DIAPOSITIVA]** Una tabla con columnas: entrada, estimación, $u(x_i)$, cambio de salida al perturbar, contribución al cuadrado. La fila final muestra $u_c$ y $U$.

Ya tenemos las entradas en unidades compatibles. Para un presupuesto básico con entradas independientes, podemos usar una tabla de sensibilidades numéricas: alteramos una entrada en una incertidumbre estándar, volvemos a calcular la salida y registramos cuánto cambió. Este procedimiento numérico, emparentado con el de Kragten que se cita en la nota 3 del Anexo F.2 de GUM-6, permite seguir la sensibilidad sin pedir todavía que deriven una fórmula. La ecuación (47) de esa guía usa diferencias centrales; nuestra tabla usa una perturbación hacia arriba. La contribución aproximada de cada entrada es el cambio de salida producido por esa perturbación; elevamos cada cambio al cuadrado, sumamos y tomamos la raíz cuadrada. La suma es admisible aquí porque el ejemplo declara independencia. La ley completa y el tratamiento de covarianzas se desarrollan en el nivel I [GUM-6 F.2, ecuación (47) y nota 3; AX.2].

> **[PIZARRA]** Para entradas independientes, $u_c(\hat{x})\approx\sqrt{\sum_i [f(x_i+u(x_i))-f(x_i)]^2}$.
>
> **[NOTA AL INSTRUCTOR]** Decir «aproximamos la sensibilidad con un cambio numérico de una entrada». No llamarlo exacto: el procedimiento usa una perturbación finita y es razonable cuando el modelo se comporta localmente de forma casi lineal.

Volvamos al conjunto **simulado**. El valor de uso nominal es $\hat{x}=100{,}000\ \mathrm{nmol/mol}$. Si aumentamos solo $y$ en $u(y)=0{,}0855\ \mathrm{nmol/mol}$, la salida cambia aproximadamente $+0{,}0853\ \mathrm{nmol/mol}$. Si aumentamos solo $a$ en $0{,}15\ \mathrm{nmol/mol}$, cambia $-0{,}1497\ \mathrm{nmol/mol}$. Si aumentamos solo $b$ en $0{,}002$, cambia $-0{,}1992\ \mathrm{nmol/mol}$. El signo indica la dirección del cambio; para la combinación de incertidumbres independientes importa el cuadrado de cada contribución. Al sumar esos cuadrados y extraer la raíz, resulta $u_c\approx0{,}2634\ \mathrm{nmol/mol}$. El script `calc/M08_ejemplos.py` calcula cada salida perturbada, y conserva más cifras que las que necesitamos leer en voz alta.

> **[EJEMPLO]** Tabla numérica del conjunto **simulado**:
>
> | Entrada perturbada | $u(x_i)$ | $\hat{x}$ tras aumentar esa entrada | Cambio en $\hat{x}$ |
> |---|---:|---:|---:|
> | `y` (media) | 0,0855 nmol/mol | 100,0853 nmol/mol | +0,0853 nmol/mol |
> | $a$ | 0,1500 nmol/mol | 99,8503 nmol/mol | −0,1497 nmol/mol |
> | $b$ | 0,0020 (adimensional) | 99,8008 nmol/mol | −0,1992 nmol/mol |
> | **Combinada** |  |  | **$u_c\approx0{,}2634\ \mathrm{nmol/mol}$** |

Para pasar de incertidumbre combinada a expandida, escribimos $U=k\cdot u_c$. El factor `k` y el nivel de cobertura deben acompañar al resultado. En una situación donde las contribuciones relevantes tienen grados de libertad suficientemente grandes, el modelo de distribución justifica aproximadamente una cobertura normal central del 95 %, y puede usarse $k\approx 2$. No lo conviertan en una constante universal: si hay pocas observaciones, componentes con pocos grados de libertad o una forma de distribución que no respalda esa aproximación, hay que revisar la cobertura. En el ejemplo, la ficha declara que las contribuciones dominantes, intercepto y pendiente, tienen grados de libertad grandes; la parte tipo A, con siete, es pequeña. Con esa justificación declarada, $k=2$ representa aproximadamente el 95 %, no exactamente, y $U\approx 0{,}527\ \mathrm{nmol/mol}$; la selección justificada de cobertura y grados de libertad se verá en I [GUM 6.2–6.3; Crowder 2020 §6.2.5].

> **[PIZARRA]** $U=k\,u_c$; ejemplo ilustrativo: $U\approx 2\times 0{,}2634\approx 0{,}527\ \mathrm{nmol/mol}$ si el modelo respalda $k\approx 2$.
>
> **[ERROR CRÍTICO]** No confundir `u_c` con `U`. Si se reporta una incertidumbre expandida, declarar $k$, la cobertura que representa y las unidades; no rotular una incertidumbre estándar como si fuera expandida.

El presupuesto no es una lista donde cada renglón entra por costumbre. Pregunten si la fuente afecta el mensurando, si ya está incluida en otra entrada, cuál es el resultado de interés y si las entradas comparten información o una causa. La tabla numérica de este nivel solo trata entradas independientes; si existe una dependencia no contemplada, no fuercen una cuadratura simple: es una señal para detenerse y escalar el análisis.

El certificado F-PSMT-01 documenta un diseño propio de calibración del Level 2 contra el SRP 55: doce puntos (diez de concentración y dos de cero), ocho lecturas por punto y día, y seis días. Eso da 576 observaciones, pero no 576 réplicas intercambiables. Los puntos corresponden a concentraciones diferentes y las lecturas están agrupadas por día. Por eso, dividir una dispersión que mezcla niveles y días por $\sqrt{576}=24$ no estima automáticamente la incertidumbre del punto calibrado, de una media ni de una lectura futura. El divisor depende del resultado y del diseño de muestreo; primero se separan las fuentes de variación pertinentes [GUM 4.2.3; GUM H.5; F-PSMT-01, fuente propia del diseño].

> **[PIZARRA]** $12\times 8\times 6=576$ observaciones; $\sqrt{576}=24$, pero no es un divisor válido sin un modelo de réplicas independientes del resultado de interés.

### [PRÁCTICA] Presupuesto sencillo de un punto de calibración y por qué √576 no es el divisor

**Enunciado narrado.** Supongan que el resultado de interés es el error medio de calibración en un punto, promediado sobre seis días y ocho lecturas por día. Para practicar, recibimos un conjunto **simulado** mediante valores didácticos fijados en `calc/M08_practicas_luna.py`: $s_r=0{,}24\ \mathrm{nmol/mol}$, $s_{\mathrm{entre}}=0{,}30\ \mathrm{nmol/mol}$, $u_{\mathrm{ref}}=0{,}20\ \mathrm{nmol/mol}$ y una tolerancia rectangular de corrección con semiamplitud $h=0{,}30\ \mathrm{nmol/mol}$, de modo que $u_{\mathrm{corr}}=h/\sqrt{3}$.  El modelo equilibrado supone días independientes, lecturas independientes dentro de cada día, y las dos últimas contribuciones independientes de la precisión. No son datos ni incertidumbres de CALAIRE.

Calculen la incertidumbre estándar de precisión del promedio, el presupuesto combinado y $U$ con el factor didáctico declarado $k=2$. Conviertan esa tolerancia a incertidumbre estándar y úsenla como perturbación de una entrada en la función de presupuesto; registren el cambio de salida que aporta a la tabla numérica de sensibilidades. Repitan el presupuesto suprimiendo solo el efecto entre días y expliquen el cambio. Finalmente, evalúen por qué ni $s_r/\sqrt{576}$ ni dividir por 24 responde automáticamente a esta pregunta, dado que el diseño propio F-PSMT-01 contiene 12 puntos × 8 lecturas × 6 días y las observaciones están agrupadas.

**Solución docente.** La tolerancia rectangular produce $u_h=0{,}30/\sqrt{3}=0{,}1732\ \mathrm{nmol/mol}$. En el modelo aditivo $e=e_{\mathrm{prec}}+r+c$, con $r$ la entrada rectangular y sensibilidad unitaria, perturbar $r$ en $u_h$ cambia la salida en $+0{,}1732\ \mathrm{nmol/mol}$; su contribución al cuadrado es $0{,}0300\ (\mathrm{nmol/mol})^2$. La varianza de precisión del promedio es $0{,}30^2/6+0{,}24^2/(6\cdot8)=0{,}015+0{,}0012=0{,}0162\ (\mathrm{nmol/mol})^2$. Su raíz es $u_{\mathrm{prec}}=0{,}1273\ \mathrm{nmol/mol}$. Al añadir las dos entradas independientes, $u_c=\sqrt{0{,}0162+0{,}20^2+(0{,}30/\sqrt{3})^2}=0{,}2936\ \mathrm{nmol/mol}$; con el $k=2$ supuesto para el ejercicio, $U=0{,}5872\ \mathrm{nmol/mol}$. Es una incertidumbre expandida didáctica y no se afirma cobertura exacta del 95 %.

Sin el componente entre días, $u_c=\sqrt{0{,}24^2/48+0{,}20^2+(0{,}30/\sqrt{3})^2}=0{,}2668\ \mathrm{nmol/mol}$: la cifra baja porque se omitió una fuente que el modelo declara relevante, no porque los datos la hayan refutado. El cálculo ingenuo $s_r/\sqrt{576}=0{,}0100\ \mathrm{nmol/mol}$ tampoco corresponde: mezcla doce concentraciones y trata como intercambiables observaciones que comparten día. La comprobación reproducible confirma $12\cdot8\cdot6=576$, pero ese conteo no define la unidad de réplica del promedio de un punto.

**Interpretación y acción.** Para el resultado especificado, mantener el efecto entre días y la repetibilidad con sus divisores de diseño; incorporar las fuentes tipo B sin dividirlas por el número de lecturas. No emitir una incertidumbre oficial desde este ejemplo simulado.

**Criterio de logro.** Presenta $u_{\mathrm{prec}}$, $u_c$ y $U$ con unidades, distingue el promedio de una lectura individual y rechaza la división automática por $\sqrt{576}$.

**Agrupación de evidencias.** La conversión de tolerancia rectangular se evalúa directamente en la práctica al obtener $u_{\mathrm{corr}}=h/\sqrt{3}$. La sensibilidad numérica de Kragten se verifica al perturbar esa entrada en el modelo aditivo, con sensibilidad unitaria; el mismo cálculo alimenta el presupuesto de este resultado. Por eso la conversión y la sensibilidad se agrupan en una única evidencia trazable.

### Señales de escalamiento

Antes de cerrar el nivel B, nombremos las señales que exigen detener el procedimiento y consultar. Si dos entradas dependen de un patrón compartido y el presupuesto no tiene término para esa dependencia, no se asume independencia. Si el comportamiento sugiere un cambio de escala, un atípico sin causa identificada o residuos con estructura, el presupuesto no debe ocultar el problema dentro de una cifra combinada. También se escala cuando la incertidumbre es relevante en ambos ejes de una regresión, hay pocos grados de libertad para la cobertura disponible o el resultado queda próximo a un límite de decisión. Estas señales no sustituyen el contenido básico: indican que la plantilla o el modelo definido no alcanza para sostener el resultado [prop_e §2].

> **[DIAPOSITIVA]** Semáforo de escalamiento: dependencia no modelada; cambio de escala; atípico sin causa; estructura en residuos; incertidumbre relevante en ambos ejes; pocos grados de libertad; resultado cercano a un límite.
>
> **[PREGUNTA AL GRUPO]** Si el resultado de la plantilla sale con muchas cifras, ¿eso resuelve una de estas señales? — *Respuesta esperada:* no; la precisión de impresión no compensa un supuesto incumplido.

## Nivel I — añadir el modelo analítico, la dependencia y la cobertura

En el nivel intermedio damos por visto el presupuesto básico y agregamos lo necesario para prepararlo y justificarlo: derivadas de la función, covarianzas cuando las entradas dependen, cobertura según grados de libertad, y la diferencia entre un resultado de calibración y uno que se usará después. No vamos a repetir cada regla de B como si empezara un capítulo nuevo; vamos a ampliar el modelo para que el presupuesto responda a la decisión técnica que ustedes deben sostener [prop_e §5, M8].

### Escena I1. Sensibilidades analíticas y covarianza

> **[DIAPOSITIVA]** Reemplazar la tabla numérica de B por la forma general de la ley de propagación; resaltar las derivadas parciales y los términos de covarianza.

En B, perturbamos una entrada y observamos el cambio numérico. Ahora escribimos la sensibilidad como una derivada parcial: $c_i=\partial f/\partial x_i$. La sensibilidad indica cuánto cambia localmente la salida cuando cambia esa entrada, manteniendo fijas las demás. Si el modelo es suficientemente suave y la incertidumbre es pequeña alrededor del valor de entrada, una aproximación lineal lleva a la ley de propagación. La deducción por expansión de Taylor no la hacemos aquí; está en el Anexo AX.2. Aquí la usamos y verificamos que sus condiciones sean razonables [GUM 5.1–5.2; MMU §6.1; Crowder 2020 §7.2–7.3; AX.2].

> **[PIZARRA]** $$u_c^2(Y)=\sum_i c_i^2u^2(x_i)+2\sum_{i<j}c_ic_j\,u(x_i,x_j)$$
>
> **[NOTA AL INSTRUCTOR]** Leer: «la varianza combinada es la suma de los cuadrados de cada sensibilidad por su varianza, más dos veces cada producto de sensibilidades por la covarianza de ese par».

Si las entradas son independientes, sus covarianzas son cero y queda la suma de términos diagonales. Si comparten una causa o fueron estimadas conjuntamente, la covarianza puede ser positiva o negativa; el signo del término depende tanto de esa covarianza como de las sensibilidades. Por eso una correlación positiva no siempre aumenta la incertidumbre de salida: si una sensibilidad tiene signo contrario a la otra, su producto es negativo. La independencia no se concluye porque los nombres de las columnas sean distintos; se justifica con el modelo y el origen de las entradas [GUM 5.1–5.2; Crowder 2020 §7.4.1].

> **[PREGUNTA AL GRUPO]** Si dos entradas suben juntas, ¿siempre sube la incertidumbre de la salida? — *Respuesta esperada:* no; también importan los signos de las sensibilidades. Una covarianza positiva puede aumentar o reducir la varianza de salida según esos signos.

Tomemos ahora el ejemplo simulado de B y derivemos sus sensibilidades. Para $\hat{x}=(y-a)/b$, la derivada respecto de $y$ es $1/b$; respecto de $a$, $-1/b$; respecto de $b$, $-(y-a)/b^2$. Con $y=100{,}60$, $a=0{,}40$ y $b=1{,}002$, obtenemos aproximadamente $c_y=0{,}9980$, $c_a=-0{,}9980$ y $c_b=-99{,}8004$. Las dos primeras son adimensionales, porque $b$ lo es y $y$ y $a$ comparten la unidad nmol/mol; la tercera expresa el cambio de $\hat{x}$ por unidad de pendiente. Una pendiente cercana a uno no significa que su sensibilidad sea irrelevante: el tamaño de la contribución también depende de $u(b)$ [GUM 5.1; Crowder 2020 §7.2–7.3; AX.2].

En el presupuesto ilustrativo, cada término de varianza se calcula como sensibilidad al cuadrado por incertidumbre estándar al cuadrado. Para la media de `y` entran por separado la parte tipo A y la cuantización declaradas en el ejemplo; para `a` y `b` usamos las incertidumbres estándar proporcionadas. Bajo la suposición explícita de independencia, la raíz de la suma da la aproximación lineal $u_c\approx 0{,}2637\ \mathrm{nmol/mol}$ (el script entrega las cifras completas). La diferencia pequeña frente al valor calculado por perturbación finita en B se debe a que la tabla de Kragten perturba entradas por cantidades finitas; la derivada analítica describe la aproximación local de primer orden. No escondemos esa diferencia ni mezclamos los dos métodos como si fueran idénticos [MMU §6.1; Crowder 2020 §7.2–7.3].

> **[EJEMPLO]** Datos **simulados** de B, tratados analíticamente: $c_y\approx 0,9980$; $c_a\approx -0,9980$; $c_b\approx -99,8004$; $u_c$ lineal aproximada $0{,}2637\ \mathrm{nmol/mol}$ para entradas independientes.
>
> **[NOTA AL INSTRUCTOR]** Presentar la cifra como aproximación lineal. No sustituir la salida tabular de Kragten por esta cifra sin señalar que son aproximaciones distintas.

Para mostrar una covarianza numérica, consideremos otra ilustración **simulada**: dos resultados contienen una contribución relativa común $u_b=0,003$, aplicada a valores de `100` y `102 nmol/mol`. La covarianza inducida por esa fuente común es $x_1x_2u_b^2=0{,}0918\ (\mathrm{nmol/mol})^2$. En la diferencia entre resultados, esa covarianza entra con signo negativo: la parte común se cancela en parte. El parámetro `u_b` y ambos valores se fijaron para este ejemplo; no describen una característica medida de CALAIRE [Crowder 2020 §7.4.1; AX.2].

> **[ERROR CRÍTICO]** Si dos resultados comparten patrón o componente de trazabilidad, no presentar la cuadratura bajo independencia sin justificarla. La covarianza puede reducir o aumentar la incertidumbre de una diferencia; omitirla no es automáticamente conservador.

### Escena I2. Grados de libertad, Student y cobertura

> **[DIAPOSITIVA]** Diagrama: `u_c` → grados de libertad efectivos $\nu_{\mathrm{eff}}$ → cuantil de Student $t(0,975;\nu_{\mathrm{eff}})$ → intervalo bilateral del 95 %.

Ahora que sabemos combinar contribuciones, preguntamos cuánta información sostiene cada una. Una desviación estándar estimada con pocos datos tiene incertidumbre apreciable; una contribución basada en un límite o en conocimiento suficientemente amplio puede modelarse con grados de libertad grandes, de acuerdo con la información disponible. Para un intervalo bilateral central del 95 % con una aproximación de Student, el factor es $k=t(0,975;\nu_{\mathrm{eff}})$. Cuando los grados de libertad crecen, el cuantil se acerca al de la normal; con pocos grados de libertad, puede ser mayor. La GUM explica los grados de libertad efectivos y el uso de la t en sus anexos G.3–G.4 [GUM 6.2–6.3, G.3–G.4; Crowder 2020 §6.2.5; Crowder 2020 §7.3].

La aproximación de Welch–Satterthwaite estima $\nu_{\mathrm{eff}}$ a partir de las contribuciones independientes a la varianza combinada y de los grados de libertad asignados a cada contribución. En la versión elemental que usamos en I, todos los términos del presupuesto que entran en esa aproximación se tratan como independientes, según el modelo declarado. Si el presupuesto relevante contiene covarianzas, no aplicamos la fórmula diagonal mecánicamente ni fingimos que esas covarianzas son términos independientes. Esto no impide la reducción local justificada de M07-I: la combinación escalar de intercepto y pendiente conserva su covarianza dentro de un único bloque, con una sola escala residual y sus grados de libertad, independiente de la nueva indicación. Solo después de esa reducción se aplica la aproximación entre bloques independientes; no es una regla general para presupuestos correlacionados. Remitimos la deducción y condiciones al Anexo AX.7; si el caso necesita una cobertura numérica que este tratamiento no permite, se escala a A o a la persona responsable del método [GUM G.4; Crowder 2020 §7.3; AX.7; prop_e §5, M8].

> **[PIZARRA]** Para componentes independientes: $$\nu_{\mathrm{eff}}\approx\frac{u_c^4}{\sum_i c_i^4\,u^4(x_i)/\nu_i}$$ y $k=t(0{,}975;\nu_{\mathrm{eff}})$ para cobertura bilateral central del 95 %. Aquí $c_i u(x_i)$ es la contribución de la entrada $i$ a $u_c$.
>
> **[NOTA AL INSTRUCTOR]** Decir que la expresión es una aproximación con condiciones, no una identidad universal para cualquier matriz de covarianza.

En el ejemplo simulado de $\hat{x}$, el script conserva los siete grados de libertad suministrados para la evaluación independiente de $s_r$: ocho observaciones de aquella evaluación menos uno. No los deduce de las ocho lecturas actuales ni aumenta la información de $s_r$ al cambiar el número de lecturas que promediamos. Las demás componentes del ejemplo didáctico se tratan como si tuvieran grados de libertad grandes. Con la linealización y los componentes mostrados, resulta $\nu_{\mathrm{eff}}\approx658$. El cuantil bilateral de Student del 95 % es aproximadamente $1{,}964$, por tanto $U\approx0{,}518\ \mathrm{nmol/mol}$. En B usamos $k=2$ solo como ilustración condicionada y combinamos perturbaciones finitas; aquí usamos derivadas y grados de libertad. Por eso, $U\approx0{,}527$ y $U\approx0{,}518$ no son cifras contradictorias: son aproximaciones distintas bajo las hipótesis declaradas. Todos estos valores son **simulados**, no una cobertura del Level 2 [GUM G.4; Crowder 2020 §6.2.5; AX.7].

> **[EJEMPLO]** Para el presupuesto **simulado** lineal: $\nu_{\mathrm{eff}}\approx 658$; $k=t(0{,}975;658)\approx1{,}964$; con $u_c\approx0{,}2637\ \mathrm{nmol/mol}$, $U\approx0{,}518\ \mathrm{nmol/mol}$.
>
> **[NOTA AL INSTRUCTOR]** Confirmar las cifras directamente con `calc/M08_ejemplos.py` antes de impartir. La diferencia entre B e I muestra cambio de aproximación y tratamiento, no un dato de laboratorio.

La aproximación de Student también requiere que la distribución de salida sea aproximadamente normal y que la incertidumbre estimada admita ese tratamiento. Muchos grados de libertad no corrigen una forma de distribución inadecuada. Si domina una componente rectangular de límites conocidos, un intervalo construido con t puede incluso salir de los límites posibles; no garantiza entonces la cobertura pretendida. Revisamos la distribución o escalamos al tratamiento numérico de M13 [GUM G.6.5].

> **[PREGUNTA AL GRUPO]** Si domina una componente rectangular de límites exactos, ¿bastan grados de libertad grandes para usar t? — *Respuesta esperada:* no; también debe ser adecuada la forma de la distribución de salida.

Un número pequeño de grados de libertad es una señal para revisar la cobertura, no una prohibición automática de usar una prueba t sobre una media. Si el modelo de la prueba t y la unidad de repetición están justificados, la prueba puede seguir siendo pertinente; se debe interpretar su cobertura o potencia con la información disponible. Tampoco se resuelve un número pequeño de grados de libertad sumando lecturas que no son réplicas independientes del factor que domina la incertidumbre [GUM G.3–G.4].

> **[ERROR CRÍTICO]** No reportar $k=2$ como cobertura exacta del 95 % cuando los grados de libertad o la distribución no lo respaldan. No aplicar Welch–Satterthwaite a un presupuesto correlacionado mediante la fórmula de componentes independientes.

### Escena I3. Individual, promedio de calibración y resultado futuro

> **[DIAPOSITIVA]** Tres renglones con mismo instrumento y distinto resultado: «una lectura», «media estimada en la calibración», «próxima lectura o uso futuro».

Aclaramos ahora una confusión frecuente. El presupuesto de una observación individual no es necesariamente el de la media de calibración. Y ninguno representa automáticamente una observación futura. Para la media, una componente de repetibilidad independiente puede reducirse según el número de observaciones y el diseño. Para una lectura individual, esa reducción no corresponde. En el uso futuro puede entrar, además de la incertidumbre de los parámetros o del promedio calibrado, la dispersión del proceso futuro o la variación entre días. La selección depende del mensurando y del modelo de salida [GUM 4.1–4.2; GUM-6 11.4; Crowder 2020 §6.2.2–6.2.4].

Retomemos el ejemplo **simulado** de M06-B: seis días con ocho lecturas por día, $s_{\mathrm{entre}}=0{,}30$ y $s_r=0{,}24\ \mathrm{nmol/mol}$. Para un punto, la contribución de precisión es $u^2_{\mathrm{prec}}(\bar e)=0{,}30^2/6+0{,}24^2/48=0{,}0162\ (\mathrm{nmol/mol})^2$: sumamos la varianza entre días dividida por seis y la varianza de lectura dividida por cuarenta y ocho. Su raíz es $0{,}1273\ \mathrm{nmol/mol}$. Ahora completamos el presupuesto prometido en M06: añadimos una referencia común de $0{,}30$ y una corrección de $0{,}10\ \mathrm{nmol/mol}$, independientes de la precisión y entre sí, con sensibilidades unitarias. No reducimos esas dos componentes al promediar [GUM H.5 y 5.1.2; AX.4].

> **[PIZARRA]** $u_c(\bar e)=\sqrt{0{,}30^2+0{,}10^2+0{,}30^2/6+0{,}24^2/48}=0{,}3409\ \mathrm{nmol/mol}$.

Leemos: raíz de la varianza de referencia más la de corrección más las dos contribuciones de precisión del promedio. Este presupuesto completo del modelo aditivo no describe CALAIRE ni se suma al presupuesto inverso de B. Para una lectura de un día elegido al azar, sin los divisores del promedio, obtenemos $u_c=\sqrt{0{,}30^2+0{,}10^2+0{,}30^2+0{,}24^2}=0{,}4976\ \mathrm{nmol/mol}$. Para el uso futuro de la corrección media estimada, supongamos una nueva indicación media con incertidumbre total $0{,}25$ y una estabilidad entre calibración y uso de $0{,}18\ \mathrm{nmol/mol}$, independientes de todo lo anterior y entre sí. La incertidumbre de esa nueva indicación ya contiene su precisión propia: no añadimos otra componente diaria. Resulta $u_c=\sqrt{0{,}3409^2+0{,}25^2+0{,}18^2}\approx0{,}4595\ \mathrm{nmol/mol}$. Las tres cifras responden a resultados diferentes [GUM 4.1–4.2 y 5.1.2; GUM-6 11.4].

Si se justificara $k=2$, las incertidumbres expandidas del promedio y del uso futuro serían $0{,}6818$ y $0{,}9189\ \mathrm{nmol/mol}$; sin información sobre grados de libertad y distribución de estas componentes, no afirmamos cobertura exacta del 95 %. Omitir el efecto entre días daría solo $s_r/\sqrt{48}=0{,}0346\ \mathrm{nmol/mol}$ de precisión. Dividir $s_r$ por $\sqrt{576}$ daría $0{,}0100$, también incorrecto: mezcla los doce puntos y además ignora la estructura diaria. La acción es conservar los divisores del modelo y completar cada punto por separado, no buscar el menor número [GUM H.5; M06-B; AX.4].

Hay también que evitar contar la misma variación dos veces. Usemos ahora la recta simulada de M07-I, no el modelo aditivo anterior. Para una **lectura futura individual**, distinta de la indicación media con $u(y)=0{,}20$ de aquel ejemplo, fijamos $u(y)=s_{\mathrm{res}}=0{,}3946\ \mathrm{nmol/mol}$: el residual estima aquí toda la dispersión de esa lectura. Con los mismos parámetros, su covarianza y $y=250{,}50$, la inversión da $\hat x=249{,}900$ y $u(\hat x)=0{,}4256\ \mathrm{nmol/mol}$. Añadir otra vez $s_r=s_{\mathrm{res}}$ como precisión independiente produce $0{,}5800\ \mathrm{nmol/mol}$. La segunda cifra cuenta dos veces la dispersión futura; la incertidumbre de los parámetros permanece en ambas porque representa la estimación de la recta, no otra realización de la lectura futura. Revisen qué representa cada término antes de sumar [GUM 4.3.10; ISO 28037 §11.1.3; M07-I1].

> **[ERROR CRÍTICO]** No sumar como si fueran independientes el residual de regresión y una componente de precisión que describe la misma variación. No retirar una de ellas por conveniencia: establezcan qué representa cada término en el modelo.

> **[PREGUNTA AL GRUPO]** Si el residuo ya contiene la dispersión de repetición del ajuste, ¿qué debemos comprobar antes de agregar una desviación de repetibilidad aparte? — *Respuesta esperada:* si representa una fuente distinta o si es la misma variación contada dos veces.

### Escena I4. Propagación en la cadena SRP 55 → Level 2 → cliente

> **[DIAPOSITIVA]** Diagrama de tres eslabones: SRP 55 → calibración del Level 2 → calibración del fotómetro cliente. Bajo cada flecha: salida de un modelo que pasa a ser entrada del siguiente.

La calibración del cliente no comienza estadísticamente desde cero. En la cadena del laboratorio, el SRP 55 sirve para calibrar el Level 2 y el Level 2 se usa después como referencia de trabajo para calibrar fotómetros del país. La incertidumbre pertinente del patrón que se transfiere entra como componente del presupuesto del siguiente eslabón. El modelo compuesto debe conservar qué magnitud se transfiere y qué correcciones o parámetros se aplican en cada etapa [GUM-6 8.4, 11.4; GUM 4.1; prop_e §5, M8].

Para verlo con números, usemos un ejemplo **simulado** con tres componentes independientes, todas expresadas como incertidumbres estándar equivalentes en el resultado final: $u(\mathrm{SRP\ 55})=0{,}28\ \mathrm{nmol/mol}$, contribución propia de la calibración SRP 55–Level 2 de `0,35`, y contribución propia del uso/calibración del cliente de `0,42`. La incertidumbre del Level 2, tras combinar sus dos primeras contribuciones, es $\sqrt{0{,}28^2+0{,}35^2}=0{,}4482\ \mathrm{nmol/mol}$. Al añadir la contribución del cliente, la incertidumbre total simulada es $\sqrt{0{,}28^2+0{,}35^2+0{,}42^2}=0{,}6142\ \mathrm{nmol/mol}$; con $k=2$ solo como cobertura asumida para este ejemplo, $U\approx 1{,}2285\ \mathrm{nmol/mol}$. No estamos declarando que estas son las incertidumbres certificadas del SRP 55, Level 2 o cliente; el ejemplo enseña el paso de componentes a través de la cadena bajo una independencia supuesta [GUM 5.1; GUM-6 8.4; AX.2].

Veamos además cómo una función transfiere la incertidumbre, sin esconder las sensibilidades en cifras ya equivalentes. Usamos como función del Level 2 los parámetros **simulados** de M07-I: $a=0{,}242857\ \mathrm{nmol/mol}$, $b=1{,}001429$, $u(a)=0{,}2856\ \mathrm{nmol/mol}$, $u(b)=0{,}0009433$ y $\operatorname{cov}(a,b)=-0{,}000222449\ \mathrm{nmol/mol}$. Este OLS no incluye incertidumbre de referencia; añadimos por separado una componente común del SRP de $0{,}28\ \mathrm{nmol/mol}$, representada como desplazamiento equivalente de la indicación del Level 2. Es independiente del ruido con que se estimaron los parámetros. Para $y=250{,}50$, la salida transferida es $z=(y-a)/b=249{,}900\ \mathrm{nmol/mol}$. Una comparación ideal de sensibilidad unitaria transfiere $z$ al cliente como $\hat x_{\mathrm{cliente}}=z+\delta_{\mathrm{cliente}}$, con corrección nominal cero. La incertidumbre propia del cliente se suministra en unidades de indicación del Level 2 como $0{,}42$; en la salida es $u(\delta_{\mathrm{cliente}})=0{,}42/b$. Este es otro modelo docente, no una ampliación de las cifras anteriores: en el modelo por función, la contribución de calibración SRP 55–Level 2 ya está representada por $u(a)$, $u(b)$ y $\operatorname{cov}(a,b)$; no se vuelve a sumar la contribución $0{,}35$ del modelo anterior. Por eso, los totales de ambos modelos no son comparables: contienen entradas distintas [GUM-6 8.4; ISO 28037 §11.1.3].

La sensibilidad al desplazamiento del SRP es $1/b=0{,}9986$, por lo que su contribución transferida es $0{,}28/b=0{,}2796\ \mathrm{nmol/mol}$. Conservamos el bloque de parámetros: $v_p=u^2(a)+z^2u^2(b)+2z\operatorname{cov}(a,b)=0{,}02595\ (\mathrm{nmol/mol})^2$. Leemos: varianza del intercepto más z al cuadrado por varianza de pendiente más dos z por covarianza. La incertidumbre de la salida del Level 2 es $\sqrt{0{,}28^2+v_p}/b=0{,}3226$ y la del cliente es $\sqrt{0{,}28^2+v_p+0{,}42^2}/b=0{,}5291\ \mathrm{nmol/mol}$. Así la salida del primer eslabón entra en el segundo con su incertidumbre; no se vuelve a sumar el SRP después de transferirla. Las cifras completas se reproducen en el script [GUM 5.1–5.2; AX.2; M07-I].

> **[EJEMPLO]** Cadena didáctica **simulada**: $u(\mathrm{Level\ 2})=0{,}4482\ \mathrm{nmol/mol}$; $u(\mathrm{cliente})=0{,}6142\ \mathrm{nmol/mol}$; ejemplo de expansión $U=1{,}2285\ \mathrm{nmol/mol}$ si se adopta $k=2$ para el caso ilustrativo.
>
> **[ERROR CRÍTICO]** No trasladar una incertidumbre expandida sin su factor de cobertura ni sumarla como si fuera una incertidumbre estándar. No sustituir el presupuesto del SRP 55 por el de otro SRP o por el de una fuente publicada distinta.

Para la cadena, trasladamos las componentes que el modelo del presupuesto haya definido; no inferimos una incertidumbre total solo del conteo de observaciones. La diferencia entre repetibilidad, efecto de día, pendiente e incertidumbre del patrón se estudia en los módulos anteriores. La precaución sobre las 576 observaciones del diseño propio F-PSMT-01 se explicó en B3.

### [PRÁCTICA] Presupuestos para los tres resultados y traslado al fotómetro cliente, con cobertura, grados de libertad y límites justificados

**Enunciado narrado.** Ahora ustedes preparan tres respuestas distintas con datos **simulados**, fijados en `calc/M08_practicas_luna.py`: una lectura en un día elegido al azar ($s_{\mathrm{entre}}=0{,}30$, $s_r=0{,}24$), el promedio de calibración de seis días con ocho lecturas por día, y un promedio futuro que añade una nueva indicación de incertidumbre estándar $0{,}25$ y una contribución de estabilidad $0{,}18\ \mathrm{nmol/mol}$. Para lectura y promedio incluimos además una referencia común de $0{,}30$ y una corrección de $0{,}10\ \mathrm{nmol/mol}$. Se declaran independientes entre sí y de la precisión. En el resultado futuro, la incertidumbre de la nueva indicación ya incluye su precisión. Para ilustrar la cadena, se suministran por separado $u(\mathrm{SRP\ 55})=0{,}28$, contribución propia SRP 55–Level 2 de $0{,}35$ y contribución propia Level 2–cliente de $0{,}42\ \mathrm{nmol/mol}$, independientes y expresadas en unidades equivalentes de salida.

Calculen los tres presupuestos sin intercambiar sus unidades de repetición. Para la media de calibración calculen $\nu_{\mathrm{eff}}$ y el cuantil bilateral central del 95 % de Student mediante Welch–Satterthwaite, considerando finitos los grados de libertad de los dos componentes de precisión y grandes los de las otras entradas. Luego calculen la cadena hasta cliente. Expliquen por qué no se añade otra vez repetibilidad a la indicación futura y por qué la cobertura numérica es condicional. Como comprobaciones del modelo, calculen $c_y$, $c_a$ y $c_b$ para la inversión $\hat{x}=(y-a)/b$ usando $y=100{,}60$, $a=0{,}40$, $b=1{,}002$; para dos resultados de 100 y 102 nmol/mol con componente relativa común 0,003 y componentes específicas 0,20 y 0,25 nmol/mol, comparen $u(\Delta)$ con covarianza y bajo independencia. Identifiquen además por qué no se suma otra vez el residual como repetibilidad en el ejemplo de lectura futura de I3.

**Solución docente.** Las sensibilidades de la inversión son $c_y=1/b=0{,}9980$, $c_a=-1/b=-0{,}9980$ y $c_b=-(y-a)/b^2=-99{,}8004$; con los valores de entrada indicados, la covarianza no se añade porque este ejemplo de B declara independencia. Para la comprobación de componente común, $u(x_1,x_2)=100\cdot102\cdot0{,}003^2=0{,}0918\ (\mathrm{nmol/mol})^2$; así, $u(\Delta)=\sqrt{(0{,}20^2+0{,}30^2)+(0{,}25^2+0{,}306^2)-2(0{,}0918)}=0{,}3202\ \mathrm{nmol/mol}$, frente a $0{,}5349\ \mathrm{nmol/mol}$ bajo independencia. El residual de la regresión en I3 representa la dispersión de la lectura futura; agregar de nuevo $s_r$ contaría esa misma variación dos veces. Para una lectura individual, $u=\sqrt{0{,}30^2+0{,}10^2+0{,}30^2+0{,}24^2}=0{,}4976\ \mathrm{nmol/mol}$. Para el promedio, la precisión aporta varianza $0{,}30^2/6+0{,}24^2/48=0{,}0162$; por tanto $u_{\mathrm{cal}}=\sqrt{0{,}30^2+0{,}10^2+0{,}0162}=0{,}3409\ \mathrm{nmol/mol}$. El futuro resulta $u_{\mathrm{fut}}=\sqrt{0{,}3409^2+0{,}25^2+0{,}18^2}=0{,}4595\ \mathrm{nmol/mol}$. No se agrega otro término diario: la nueva indicación ya lo representa según el enunciado.

Para cobertura de la media, los términos de varianza son $0{,}30^2/6$, $0{,}24^2/48$, $0{,}30^2$ y $0{,}10^2$. Se asignan $5$, $42$, $10^{12}$ y $10^{12}$ grados de libertad, respectivamente; el valor grande implementa numéricamente la hipótesis de grados de libertad prácticamente infinitos en los dos componentes suministrados. La fórmula da $\nu_{\mathrm{eff}}\approx299{,}83$, $k=t(0{,}975;\nu_{\mathrm{eff}})\approx1{,}9679$ y $U_{95}\approx0{,}6708\ \mathrm{nmol/mol}$. Esto supone componentes independientes y salida suficientemente compatible con Student; no autoriza aplicar Welch–Satterthwaite de forma mecánica a un presupuesto correlacionado ni demuestra por sí solo la adecuación de la distribución.

En la cadena, $u(\mathrm{Level\ 2})=\sqrt{0{,}28^2+0{,}35^2}=0{,}4482\ \mathrm{nmol/mol}$ y $u(\mathrm{cliente})=\sqrt{0{,}4482^2+0{,}42^2}=0{,}6142\ \mathrm{nmol/mol}$. Si se adopta $k=2$ solo para esta expansión didáctica, $U=1{,}2285\ \mathrm{nmol/mol}$. La incertidumbre del SRP ya forma parte de la del Level 2 y no se suma de nuevo al final.

**Interpretación y acción.** La lectura, el promedio de calibración y el uso futuro tienen distintas fuentes y divisores. La cifra del cliente hereda la del patrón de trabajo y añade la contribución propia del siguiente eslabón. En un presupuesto real se deben confirmar covarianzas, grados de libertad y distribución antes de declarar cobertura.

**Criterio de logro.** Calcula y distingue los tres resultados, justifica la cobertura dentro de sus supuestos y transfiere la incertidumbre por la cadena sin omisión ni doble conteo.

**Agrupación de evidencias.** La práctica evalúa en conjunto sensibilidades analíticas, covarianza y control del doble conteo dentro del presupuesto de la media: calcular cada término y comprobar qué significa es necesario para obtener y justificar la cobertura de ese mismo resultado. Los resultados individual, promedio y futuro hacen observable la selección de respuesta, mientras la cadena verifica el traslado sin repetir contribuciones.

### Señales de escalamiento en I

Deténganse y consulten si las entradas del presupuesto comparten una causa cuya covarianza no está declarada o no se puede justificar; no apliquen Welch–Satterthwaite en forma diagonal. Escalen a A o a la persona responsable del método si la distribución de salida no es compatible con Student —por ejemplo, una rectangular dominante cuyos límites contradicen el intervalo calculado— o si el caso requiere cobertura numérica que I no puede sostener. Si no está claro si el residual de regresión y la precisión representan la misma variación, no sumen ni retiren términos hasta definir el modelo. En la cadena, si se detecta una contribución de patrón compartido sin tratamiento de dependencia, suspendan el traslado y soliciten el presupuesto/covarianza del eslabón correspondiente.

## Nivel A — covarianza común, límites del modelo y función de incertidumbre

En el nivel avanzado damos por vistos los presupuestos de B e I. Añadimos tres tareas de mayor alcance: seguir componentes comunes cuando se informa un valor absoluto o una diferencia, reconocer hasta dónde sirve la aproximación lineal y analizar una función de incertidumbre a lo largo del intervalo para compararla con una capacidad de medición y calibración (CMC). Una CMC es la capacidad de medición y calibración que un instituto o laboratorio pone a disposición de sus clientes en condiciones normales, según su alcance publicado [CIPM MRA-G-13, sin numeral; no disponible en docs/]. La comparación exige que CMC y función de incertidumbre correspondan a la misma magnitud, unidades y cobertura. No vamos a convertir esta sección en un método de Monte Carlo: ese contenido corresponde a M13 y no se desarrolla aquí [prop_e §5, M8; prop_e §4].

### Escena A1. Lo común puede quedarse en el absoluto y cancelarse en la diferencia

> **[DIAPOSITIVA]** Dos mediciones $x_1$ y $x_2$, cada una dividida en componente propia y una flecha compartida que llega a ambas; debajo, escribir el contraste $\Delta=x_2-x_1$.

Al evaluar dos valores por separado, una causa común puede contribuir a la incertidumbre de cada uno. Si el resultado que interesa es su diferencia, esa misma contribución puede cancelarse total o parcialmente. Por eso no se obtiene la incertidumbre de la diferencia sumando las incertidumbres absolutas sin más. El modelo de salida es $\Delta=x_2-x_1$, con sensibilidades $-1$ y $+1$; la ley general añade el término de covarianza con signo negativo. La decisión depende de qué parte de la incertidumbre es común, de cuánto se comparte y de la relación entre ambas entradas [GUM 5.2; Crowder 2020 §7.4.1; AX.2].

> **[PIZARRA]** $$u^2(\Delta)=u^2(x_1)+u^2(x_2)-2\,u(x_1,x_2)$$
>
> **[NOTA AL INSTRUCTOR]** Leer: «la varianza de la diferencia es la suma de las dos varianzas menos dos veces la covarianza».

Hagamos el cálculo con un conjunto **simulado**. Dos resultados absolutos son $x_1=100$ y $x_2=102\ \mathrm{nmol/mol}$. A cada uno se le asigna una componente común relativa $u_b=0,003$ y componentes específicas independientes `0,20` y `0,25 nmol/mol`. La covarianza de la parte común es $x_1x_2u_b^2=0{,}0918\ (\mathrm{nmol/mol})^2$. Al sumar toda la variación de cada resultado y luego restar dos veces esa covarianza, obtenemos $u(\Delta)\approx 0{,}320\ \mathrm{nmol/mol}$; si se ignorara la covarianza y se supusiera independencia, resultaría aproximadamente `0,535 nmol/mol`. Ambas cifras son simuladas y reproducibles en el script. En este ejemplo, la diferencia es menos incierta porque la causa común se cancela parcialmente; en otro modelo, con otra estructura, la covarianza y el signo de las sensibilidades pueden cambiar el efecto [Crowder 2020 §7.4.1; AX.2].

> **[EJEMPLO]** Valores **simulados**: $x_1=100$, $x_2=102\ \mathrm{nmol/mol}$; componente relativa compartida `0,003`; contribuciones específicas `0,20` y `0,25 nmol/mol`. Resultado: $u(\Delta)\approx 0{,}320\ \mathrm{nmol/mol}$ con el componente compartido; $u(\Delta)\approx 0{,}535\ \mathrm{nmol/mol}$ bajo independencia.
>
> **[ERROR CRÍTICO]** No suponer que compartir una referencia significa covarianza igual a cero. Tampoco suponer que toda covarianza común desaparece por completo: la cancelación depende del modelo, las sensibilidades y la proporción común que afecte a cada resultado.

En el ejemplo, para un valor absoluto como $x_1$, el componente común sigue dentro de su incertidumbre. La reducción aparece en el contraste porque la misma contribución entra a ambos lados con coeficientes opuestos. Esta diferencia entre incertidumbre absoluta y diferencial es importante: el presupuesto se construye para el mensurando declarado, no para el origen de datos considerado en abstracto. La matriz de covarianza conserva esas relaciones para más de dos resultados; cada covarianza debe tener unidades de producto de las unidades de sus dos variables [GUM 5.2; Crowder 2020 §7.4.1; AX.2].

> **[PREGUNTA AL GRUPO]** Si la fuente común cambia en el tiempo entre dos mediciones, ¿podemos asumir la cancelación perfecta? — *Respuesta esperada:* no; se debe describir si la fuente permanece común, qué variación tuvo y qué covarianza representa el modelo.

### Escena A2. La linealización tiene dominio y una función se revisa en todo el intervalo

Veamos primero un ejemplo **simulado** de curvatura. Para $\hat{x}=100/b$, con $b=1$ y $u(b)=0{,}20$, la sensibilidad local predice cambios de magnitud $20$. Sin embargo, sustituir $b+u(b)=1{,}20$ da $83{,}33$, un cambio de $-16{,}67$ respecto de cien; sustituir $b-u(b)=0{,}80$ da $125$, un cambio de $+25$. La asimetría muestra que una sola sensibilidad local no resume bien estos desplazamientos. No estamos calculando un intervalo de cobertura con esas dos sustituciones: estamos comprobando la adecuación local de la aproximación. Si la región de valores plausibles de la pendiente incluye valores próximos a cero, la inversión exige especial revisión; la propagación numérica de distribuciones corresponde a M13 [GUM-6 F.1–F.2; ISO 28037 §11.1.3, notas 1 y 3; script `calc/M08_ejemplos.py`].

> **[DIAPOSITIVA]** Tabla de $U(x)$, CMC hipotética y máximo puntual en cuatro concentraciones, con el punto de cruce y el intervalo de dominio señalados. No se requiere un gráfico para resolver esta práctica.

La propagación analítica que usamos en I se basa en sensibilidades locales y una aproximación de primer orden. Es útil si la función se comporta suavemente en la región de incertidumbre y la distribución de entradas no hace que la curvatura domine el resultado. Si hay no linealidad marcada, incertidumbres grandes respecto de la escala local, asimetría importante o límites que deforman la distribución de salida, una única aproximación lineal puede describir mal la incertidumbre. La primera respuesta no es forzar más decimales, sino revisar el modelo, su dominio y la adecuación de la aproximación. La validez de la aproximación lineal y de la ley de propagación se trata en GUM-6, Anexos F.1–F.2, y en Crowder 2020 §7.7. El análisis numérico por Monte Carlo queda fuera de este capítulo [GUM-6 F.1–F.2; Crowder 2020 §7.7; prop_e §5, M8; M13].

> **[ESCALAMIENTO]** Escalen el análisis cuando el modelo sea fuertemente no lineal en el intervalo relevante, cuando las entradas sean tan inciertas que la sensibilidad en el valor central no represente el intervalo, o cuando la distribución de salida no pueda describirse de modo adecuado con la propagación de primer orden.

No basta con verificar una sola concentración si la incertidumbre se declara como función sobre un intervalo. Para cada punto, se evalúa la función de incertidumbre de la calibración y se compara con la CMC pertinente, manteniendo constante el mensurando, las unidades y la cobertura. La CMC no se compara de manera válida si una curva está en incertidumbre estándar y la otra en expandida, si usan coberturas distintas o si representan magnitudes diferentes. El máximo puntual combina el presupuesto de la calibración con el piso de declaración de una CMC aplicable; no es una regla de decisión de la GUM ni aprueba una CMC; el contenido es comprobar la función frente al intervalo y reconocer el máximo puntual entre `U` y CMC [GUM 6.2–6.3; CIPM MRA-G-13].

Consideremos una función **simulada** para una magnitud de fracción molar de ozono: $u(x)=\sqrt{0{,}28^2+(0{,}006x)^2}\ \mathrm{nmol/mol}$, con `x` en nmol/mol. Supongamos $k=2$ para formar $U(x)=2u(x)$ y, solo con fines didácticos, una CMC propuesta `0,80+0,004x nmol/mol`, con el mismo mensurando y cobertura. La función de CMC no es un dato del laboratorio ni una CMC aprobada; la hemos fijado para aprender a hacer la comparación. En $x=0$, $U=0,56$ y la CMC simulada vale `0,80`; se toma el máximo, `0,80`. En $x=80$, $U\approx 1,111$ y la CMC `1,12`, el máximo es `1,12`. En $x=250$, $U\approx 3,052$ frente a CMC `1,80`; en $x=500$, $U\approx 6,026$ frente a `2,80`. El máximo puntual entre las dos funciones cambia a lo largo del dominio, por lo que la comprobación debe cubrir los puntos y el intervalo que justifican el uso [calc/M08_ejemplos.py, construcción simulada].

> **[EJEMPLO]** Funciones **simuladas**, `x` en nmol/mol, `U` y CMC en nmol/mol, ambas con $k=2$:
>
> | `x` | `U(x)` | CMC propuesta | `max(U, CMC)` |
> |---:|---:|---:|---:|
> | 0 | 0,560 | 0,800 | 0,800 |
> | 80 | 1,111 | 1,120 | 1,120 |
> | 250 | 3,052 | 1,800 | 3,052 |
> | 500 | 6,026 | 2,800 | 6,026 |
>
> **[NOTA AL INSTRUCTOR]** Decir explícitamente que la CMC propuesta y la función de incertidumbre son simuladas. El ejemplo no afirma ni propone la CMC vigente de CALAIRE.

Para verificar todo el intervalo de cero a quinientos no basta con cuatro puntos: buscamos dónde se cruzan las dos funciones. Como ambas son positivas, comparar sus cuadrados es equivalente. La diferencia $U^2-\mathrm{CMC}^2$ es $0{,}000128x^2-0{,}0064x-0{,}3264$. Se lee: cero coma cero cero cero uno dos ocho por equis al cuadrado, menos cero coma cero cero seis cuatro por equis, menos cero coma tres dos seis cuatro. Ese polinomio se anula dentro del intervalo solo en $x\approx81{,}35\ \mathrm{nmol/mol}$. Antes del cruce domina la CMC; después domina $U$, hasta quinientos. El script lo comprueba también en una malla de una décima. Esto verifica la envolvente en todo el intervalo para estas funciones simuladas; no impone una forma funcional a presupuestos reales [calc/M08_ejemplos.py, álgebra del ejemplo simulado].

Interpretemos el cruce. Para un servicio acreditado al que se aplica una CMC publicada, la incertidumbre informada al cliente no puede ser menor que esa CMC: por debajo de $81{,}35\ \mathrm{nmol/mol}$, el máximo obliga a declarar la CMC, aunque el presupuesto puntual dé menos. Por encima, $U(x)>\mathrm{CMC}(x)$: este presupuesto no respalda la CMC propuesta como incertidumbre alcanzable en esas condiciones. Hay que revisar la función propuesta o justificar una mejora real del presupuesto; no bajar $U$ por conveniencia. Mientras tanto, ese resultado requiere la incertidumbre mayor que sí sostiene el modelo. Como aquí la CMC solo es hipotética, el máximo es una ilustración y no autoriza declaración acreditada alguna [ILAC-P14, sin numeral, no disponible en docs/; CIPM MRA-G-13, sin numeral, no disponible en docs/].

> **[PREGUNTA AL GRUPO]** En $250\ \mathrm{nmol/mol}$, ¿podemos informar $1{,}80$ porque es la CMC propuesta? — *Respuesta esperada:* no; el presupuesto exige $U\approx3{,}052\ \mathrm{nmol/mol}$ y obliga a revisar el respaldo de la función propuesta.

No confundamos una comparación puntual con una caracterización de todo el intervalo. El máximo de dos funciones no se obtiene comparando solo sus valores en un extremo, a menos que el comportamiento entre puntos esté justificado. Revisen que las funciones usan la misma magnitud, unidades, condiciones y cobertura, y que el intervalo de aplicación es el que se declara. Si la linealización es adecuada punto por punto en una región, puede resumirse la función; si deja de ser adecuada, no debe ocultarse esa limitación dentro de una curva aparentemente lisa [Crowder 2020 §7.5–7.7].

### [PRÁCTICA] Verificación de una función de incertidumbre frente a una CMC en el intervalo

**Enunciado narrado.** Como responsables técnicos, revisen estas funciones **simuladas** (no son una CMC ni un presupuesto de CALAIRE): para $0\leq x\leq500\ \mathrm{nmol/mol}$, $u(x)=\sqrt{0{,}28^2+(0{,}006x)^2}\ \mathrm{nmol/mol}$, $U(x)=2u(x)$, y una CMC hipotética $0{,}80+0{,}004x\ \mathrm{nmol/mol}$. El ejemplo fija la misma magnitud y cobertura para ambas. Evalúen los extremos y los puntos $x=80$ y $250\ \mathrm{nmol/mol}$, identifiquen qué función domina y encuentren todos los cruces en el intervalo. Verifiquen la conclusión con una malla de paso $0{,}1\ \mathrm{nmol/mol}$ y expliquen la acción donde $U$ supera la CMC propuesta. Como diagnóstico separado de linealización, para $\hat{x}=100/b$, $b=1$ y $u(b)=0{,}20$, comparen los cambios exactos al perturbar $b$ en $\pm u(b)$ con el cambio de magnitud 20 predicho localmente; expliquen qué advierte la asimetría, sin tratar esas perturbaciones como intervalo de cobertura. No comparen solo un punto ni interpreten la CMC didáctica como autorizada.

**Solución docente.** Para el diagnóstico, la linealización da cambios de magnitud 20; las perturbaciones exactas son $100/1{,}20=83{,}33$ (cambio $-16{,}67$) y $100/0{,}80=125$ (cambio $+25$). La asimetría advierte que la aproximación local puede no representar bien la región de incertidumbre; no define un intervalo de cobertura. En $x=0$, $U=0{,}560$ y CMC $=0{,}800$, por lo que domina la CMC. En $80$, $U=1{,}1114$ frente a $1{,}1200$; en $250$, $U=3{,}0518$ frente a $1{,}8000$; en $500$, $U=6{,}0261$ frente a $2{,}8000\ \mathrm{nmol/mol}$. Como ambas funciones son positivas, los cruces se hallan resolviendo $U^2-\mathrm{CMC}^2=0$: $0{,}000128x^2-0{,}0064x-0{,}3264=0$. La única raíz del intervalo es $x=81{,}3471\ \mathrm{nmol/mol}$; la malla confirma un único cambio de función dominante. Antes del cruce domina CMC y después domina $U$.

| $x$ (nmol/mol) | $U(x)$ (nmol/mol) | CMC hipotética (nmol/mol) | Máximo puntual (nmol/mol) |
|---:|---:|---:|---:|
| 0 | 0,5600 | 0,8000 | 0,8000 |
| 80 | 1,1114 | 1,1200 | 1,1200 |
| 250 | 3,0518 | 1,8000 | 3,0518 |
| 500 | 6,0261 | 2,8000 | 6,0261 |

**Interpretación y acción.** Bajo las condiciones hipotéticas, el máximo puntual describe la envolvente de las dos funciones. Donde $U$ supera CMC, este presupuesto no respalda la función propuesta como incertidumbre alcanzable; se revisa el modelo o la CMC aplicable y se informa solo lo respaldado por el presupuesto y los procedimientos autorizados. El ejercicio no establece una declaración acreditada.

**Criterio de logro.** Verifica unidades, magnitud y cobertura; encuentra el cruce dentro del intervalo y no extrapola una conclusión puntual a todo el dominio.

**Agrupación de evidencias.** Esta práctica reúne la evidencia sobre componentes comunes en resultados absolutos y diferencias (subtarea de A1), límites de la linealización (diagnóstico de A2) y verificación de la función frente a CMC a lo largo del intervalo (tabla y cruce). Se agrupan porque la decisión de comparar la función solo es válida tras definir la incertidumbre, evaluar el alcance local del modelo y comprobar la cobertura común; cada contenido tiene una respuesta observable en la solución.

### Señales de escalamiento

En A no escalamos porque la respuesta parezca incómoda; escalamos cuando el modelo y la información disponibles ya no respaldan la cobertura o la comparación. Consulten si la contribución común no está descrita por una covarianza defendible, si la diferencia cambia de interpretación bajo hipótesis plausibles de dependencia, si la linealización es inadecuada en una parte del dominio o si la función y la CMC no comparten magnitud, unidades y cobertura. Una función de incertidumbre no convierte por sí sola un valor de CMC en una declaración autorizada; la responsabilidad técnica del laboratorio permanece [prop_e §2; prop_e §5, M8].

> **[PREGUNTA AL GRUPO]** ¿Podemos afirmar que `U` está por debajo de CMC si solo se comparó el valor de cero? — *Respuesta esperada:* no; se debe comprobar el intervalo de uso y la coincidencia de magnitud, unidades y cobertura.

## Cierre del capítulo

En B aprendimos a empezar por el resultado, definir el modelo, convertir las entradas a incertidumbres estándar y combinar contribuciones independientes con una tabla numérica. La advertencia central fue elegir $s_r$ o $s_r/\sqrt{n}$ según la respuesta, no según el número de celdas. En I añadimos sensibilidades analíticas, covarianzas, grados de libertad y cobertura; distinguimos la calibración del uso futuro, evitamos el doble conteo y seguimos la incertidumbre a través de la cadena SRP 55 → Level 2 → cliente. En A comparamos resultados con componentes comunes, delimitamos la aproximación lineal y revisamos la función de incertidumbre a lo largo del intervalo frente a una CMC compatible.

El mensaje que quiero que se lleven es sencillo: una incertidumbre combinada no es una cifra que se pega al resultado al final. Se obtiene de un modelo, de entradas definidas, de una respuesta estadística concreta y de supuestos que deben poder explicarse. Si la independencia, la cobertura o la aproximación no están justificadas, la cifra puede estar calculada correctamente y aun así no responder la pregunta. En el módulo siguiente usaremos estas ideas al comparar resultados: la diferencia tiene su propio modelo y puede requerir la covarianza entre resultados [GUM 4.1–4.3, 5.1–5.2, 6.2–6.3; prop_e §4, secuencia M9].

> **[TRANSICIÓN]** En M9 pasamos del presupuesto de un resultado a la incertidumbre de una diferencia entre resultados, con especial atención a la covarianza y a la hipótesis de compatibilidad.

## Referencias del capítulo

- **GUM.** JCGM 100:2008 (ISO/IEC Guide 98-3:2008), *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*. `docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf`.
- **GUM-6.** GUM-6:2020, *Guide to the expression of uncertainty in measurement — Part 6: Developing and using measurement models*. `docs/JCGM_GUM_6_2020.pdf`.
- **Crowder 2020.** Crowder, S.; Delker, C.; Forrest, E.; Martin, N. *Introduction to Statistics in Metrology*. Springer Nature Switzerland AG, 2020, caps. 6–7. PDFs `docs/intro_stats_metro_c06.pdf` y `docs/intro_stats_metro_c07.pdf`.
- **MMU.** Novellino do Rosario, P. P.; Mendes, A. *Metrology and Measurement Uncertainty: Concepts and Applications*. Springer Nature Switzerland AG, 2025, caps. 5–6. PDFs `docs/metrology_measure_uncer_c05.pdf` y `docs/metrology_measure_uncer_c06.pdf`.
- **CIPM MRA-G-13.** CIPM, *Calibration and measurement capabilities in the context of the CIPM MRA*, documento de orientación (no disponible en `docs/`; se cita sin numeral para la definición y el respaldo de CMC; la base de datos KCDB queda fuera del curso).
- **ISO 28037.** ISO/TS 28037:2010, *Determination and use of straight-line calibration functions*. International Organization for Standardization, §11.1. `docs/ISO 28037.pdf`.
- **F-PSMT-01.** CALAIRE, certificado G1 S/N 59756-324. Archivo propio: `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm` (solo estructura del diseño).
- **Anexos AX.2, AX.3 y AX.7.** `curso/S4_numericos_integracion/AX_libreto.md`, secciones AX.2, AX.3 y AX.7 (contenido interno leído y comprobado; no disponible en `docs/`).
- **Referencias internas de alcance:** `prop_e.md` §§2–5; `curso/guia_libreto.md` §§1, 3–7. No se emplean como respaldo técnico externo.


- **ILAC-P14.** ILAC, *ILAC Policy for Measurement Uncertainty in Calibration*, ILAC-P14:09/2020 (no disponible en docs/; política de declaración de incertidumbre frente a CMC, sin numeral).
