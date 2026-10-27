# M12. Indicadores de precisión y sesgo a partir de diferencias relativas

## Ficha del capítulo

| Elemento | Contenido |
|---|---|
| Competencia estadística | Calcular indicadores agregados de precisión y sesgo con sus límites de confianza y distinguirlos de la incertidumbre de una calibración. Contexto: verificaciones de los clientes en redes de monitoreo. |
| Prerrequisitos | M4: estimación, intervalos e interpretación de contrastes; M8: incertidumbre de una calibración y de resultados; M10: límites, tolerancias y reglas de decisión. Para A: M3-I (covarianza y dependencia), M9-I (diferencias con covarianza) y M11-I (fases homogéneas). I comprende B; A comprende B e I. |
| Nivel B | Diferencia relativa con referencia y signo definidos; $\operatorname{media}(\lvert d_i\rvert)$ frente a $\lvert\operatorname{media}(d_i)\rvert$; porcentajes cerca de cero y métrica absoluta. |
| Nivel I añade | Límites de confianza con chi-cuadrado y t; unilateral frente a bilateral; efecto de un cambio de escala; dispersión del cero y umbral bajo hipótesis expresas. $3·s₀$ no es una definición universal de límite de detección. |
| Nivel A añade | Dependencia y mezcla de periodos en una serie de verificaciones; efectos comunes de trazabilidad en resultados agregados. |
| Datos de los ejemplos | Todos los datos numéricos didácticos son **simulados**, generados de forma determinista en `calc/M12_indicadores.py`. No son datos ni resultados de CALAIRE. Las fórmulas y criterios regulatorios citados son **publicados**; se distingue su aplicación original de los ejemplos simulados. |
| Anexos | AX.1: divisor y grados de libertad de la desviación muestral. AX.2: varianza de combinaciones lineales para el término de covarianza en un promedio dependiente. AX.11: límites de confianza de indicadores de precisión y sesgo (chi-cuadrado y t). Las deducciones se remiten a los anexos; aquí se interpretan y aplican las expresiones. |
| Referencias clave | CFR58-A, §§2.3.1.2 y 4.1.1–4.1.3.2; GUM 5.2.1–5.2.2; BS EN 14625:2012, §3.12, §8.4.5, fórmula 5 y Tabla 1. Numerales comprobados en los PDF de `docs/`; el detalle de páginas está en la bitácora. |

## Nivel B — definir la diferencia antes de resumirla

En el nivel B damos por vistos los resúmenes y la lectura de intervalos de M4, la diferencia entre un resultado de calibración y una verificación, y el uso de tolerancias y reglas de decisión de M10. Aquí añadimos una operación concreta: traducir cada verificación a una diferencia relativa con referencia, denominador y signo definidos; después resumir la dispersión y la dirección sin confundirlas. En I añadiremos los límites de confianza y sus condiciones. Por ahora, nuestra tarea es dejar inequívoco qué números entran al resumen.

### Escena B1. La diferencia relativa necesita una referencia explícita

> **[DIAPOSITIVA]** Dos columnas, «valor indicado por el monitor» y «valor de auditoría». Una flecha señala la resta y otra, el denominador de la diferencia relativa. Mantener visible la etiqueta «ejemplo simulado».

Miren estas dos columnas. Cada fila es una verificación: tenemos una indicación del monitor y el valor de referencia usado para esa verificación. Para la estadística de calidad del aire de la EPA, la diferencia porcentual de una verificación de un punto se define como la indicación menos el valor de auditoría, dividida por el valor de auditoría y multiplicada por cien. El documento especifica qué representa $\mathrm{meas}$ y qué representa $\mathrm{audit}$; por eso la referencia no es un detalle intercambiable. [CFR58-A §4.1.1]

> **[PIZARRA]** $$d_i=\frac{\mathrm{meas}_i-\mathrm{audit}_i}{\mathrm{audit}_i}\times100\%$$
>
> **[NOTA AL INSTRUCTOR]** Leer: «de sub i es igual a la indicación menos la auditoría, dividido por la auditoría, por cien por ciento». Identificar $\mathrm{audit}$ como denominador y no invertir la resta.

La fórmula produce un valor firmado. Si el monitor indica más que la referencia, $d_i$ es positivo; si indica menos, es negativo. El cero significa coincidencia aritmética en esa pareja, no ausencia de incertidumbre. La definición mantiene la dirección de la desviación y expresa su magnitud relativa respecto de la auditoría. En la fuente regulatoria la diferencia se aplica a controles de calidad de un punto de analizadores de SO₂, NO₂, O₃ y CO; el contexto y el diseño de esa aplicación importan. No vamos a trasladar automáticamente cualquier criterio regulatorio a una verificación distinta o a un patrón de CALAIRE. [CFR58-A §§3.1.1 y 4.1.1]

Ahora resolvamos un ejemplo **simulado**. En cuatro verificaciones, imaginemos que el valor de auditoría es cien nmol/mol en cada caso, y que las indicaciones son noventa y ocho, ciento uno, noventa y nueve y ciento dos nmol/mol. No son datos del laboratorio ni de una red real. Para la primera, indicación menos auditoría es menos dos; dividimos por cien y multiplicamos por cien por ciento: menos dos por ciento. Para la segunda obtenemos más uno por ciento, para la tercera menos uno, y para la cuarta más dos. Como el denominador se mantiene en cien nmol/mol, los errores absolutos corresponden aquí a menos dos, más uno, menos uno y más dos nmol/mol.

> **[EJEMPLO]** Datos **simulados**: $\mathrm{audit} = [100, 100, 100, 100] nmol/mol$; $\mathrm{meas} = [98, 101, 99, 102] nmol/mol$. Resultado: $d = [-2, +1, -1, +2] \%$ y errores absolutos $e = [-2, +1, -1, +2] nmol/mol$.
>
> **[PIZARRA]** Para la primera pareja: $d_1=(98-100)/100\times100\%=-2\%$.

Detengámonos en las palabras «referencia» y «signo». Si cambiamos qué valor ponemos abajo, cambiamos la pregunta. Si invertimos la resta, el signo se invierte. Ningún formato de hoja de cálculo puede decidir por nosotros si queríamos monitor menos auditoría o auditoría menos monitor. Por eso, antes de calcular una serie, definimos qué instrumento entrega $\mathrm{meas}$, qué resultado es $\mathrm{audit}$, qué unidad comparten y cuál es el denominador de cada diferencia. Esta especificación es parte del indicador, no un comentario posterior.

> **[PREGUNTA AL GRUPO]** Si la indicación queda por debajo del valor de auditoría, ¿qué signo tiene $d_i$ con la convención escrita? — *Respuesta esperada:* negativo, porque $\mathrm{\mathrm{meas}}_i - \mathrm{\mathrm{audit}}_i$ es negativo y el denominador es positivo.
>
> **[ERROR CRÍTICO]** No intercambiar la indicación y la referencia sin declarar una nueva convención. No borrar el signo antes de haber definido qué pregunta responde el indicador. No tratar una diferencia porcentual como si fuera una concentración: $\%$ y nmol/mol son unidades distintas.

### Escena B2. La magnitud media y el sesgo firmado no responden lo mismo

> **[DIAPOSITIVA]** Los cuatro valores firmados de la escena anterior aparecen sobre una recta: −2, +1, −1, +2. Debajo, dos operaciones: «promedio de magnitudes» y «magnitud del promedio».

Tenemos cuatro diferencias con dos signos. Si tomamos primero el valor absoluto de cada una, obtenemos dos, uno, uno y dos por ciento. El promedio de esas magnitudes es uno coma cinco por ciento. Esta cantidad responde: en promedio, ¿qué tamaño tuvo la diferencia, sin conservar la dirección? En cambio, si promediamos los valores firmados primero, el resultado es cero por ciento; su valor absoluto también es cero. Esa segunda cantidad responde: ¿qué tamaño tiene el promedio firmado? Aquí los errores positivos y negativos se cancelan exactamente.

> **[PIZARRA]** $$\operatorname{media}(|d_i|)=1,50\%;\qquad |\operatorname{media}(d_i)|=0,00\%$$
>
> **[NOTA AL INSTRUCTOR]** Leer en voz alta las dos operaciones con su orden: «promedio de los valores absolutos» y «valor absoluto del promedio firmado». No decir que son dos formas equivalentes de calcular un mismo número.

El primer resumen no informa la dirección neta del error. Sí impide que errores de signos opuestos se anulen. El segundo conserva la dirección durante el promedio. Informa el tamaño del desplazamiento medio firmado, pero puede ser pequeño aunque cada verificación esté lejos de cero. El caso simulado produce una media de magnitudes de uno coma cinco por ciento y un valor absoluto de la media firmada igual a cero. Los dos resultados son correctos; contestan preguntas diferentes. En el procedimiento publicado para verificaciones de un punto, el sesgo absoluto también se estima con los valores absolutos. Después se asigna un signo mediante los percentiles de las diferencias originales. Esa operación no convierte la media firmada en media absoluta. [CFR58-A §§4.1.3–4.1.3.2]

> **[PREGUNTA AL GRUPO]** ¿El cero de $\lvert\operatorname{media}(d_i)\rvert $ demuestra que todas las verificaciones coincidieron con la referencia? — *Respuesta esperada:* no. Los cuatro valores no son cero; los positivos y negativos se compensaron en el promedio.

Para conectar los porcentajes con una escala absoluta, en este ejemplo cada auditoría vale cien nmol/mol. Por eso una diferencia de uno por ciento corresponde a uno nmol/mol. La media de las magnitudes absolutas es uno coma cinco nmol/mol, mientras que el error firmado medio es cero nmol/mol. Esta igualdad numérica entre porcentaje y nmol/mol solo aparece por la elección particular de una referencia igual a cien; no la generalicen. Para otra referencia, el mismo porcentaje corresponde a otra diferencia absoluta.

En una comprobación cerca de cero, el porcentaje puede ser inestable o ni siquiera estar definido. Si $\mathrm{audit}$ vale cero, no podemos dividir por ese denominador. Si la auditoría vale cero coma dos nmol/mol y la indicación es cero coma cinco, la diferencia absoluta es cero coma tres nmol/mol, pero el cociente es ciento cincuenta por ciento. Ese porcentaje grande puede provenir de un denominador diminuto; por sí solo no describe una separación absoluta grande. Al acercarnos a cero, debemos conservar y reportar una métrica absoluta apropiada al mensurando, con su unidad, en vez de forzar un porcentaje cuyo denominador hace que la escala se dispare. Esta es una advertencia de interpretación, no una nueva fórmula universal para elegir un umbral.

> **[EJEMPLO]** Datos **simulados**: $\mathrm{audit} = 0,20 nmol/mol$; $\mathrm{meas} = 0,50 nmol/mol$. Diferencia absoluta: $+0,30 nmol/mol$. Diferencia relativa definida en esta convención: $+150 \%$; si la auditoría fuera cero, la diferencia relativa quedaría indefinida.
>
> **[PIZARRA]** Cerca de cero: informar la diferencia absoluta en nmol/mol y explicar por qué el porcentaje puede ser inestable; con denominador cero, no calcular $d_i$.

En este nivel no decidimos si un monitor cumple una especificación. Primero identificamos la referencia, formamos los valores firmados y elegimos el resumen que corresponde a la pregunta. El indicador agregado de una serie de verificaciones tampoco es la incertidumbre de un certificado de calibración. El indicador agregado describe verificaciones bajo una población, un diseño y un periodo definidos. El certificado describe un resultado individual de calibración bajo su propio modelo. Una cosa no sustituye a la otra. [CFR58-A §§2.3.1.2 y 4.1.1–4.1.3]

> **[ERROR CRÍTICO]** No presentar $\operatorname{media}(\lvert d_i\rvert )$ como sesgo firmado ni $\lvert\operatorname{media}(d_i)\rvert $ como dispersión. No reportar un porcentaje sin identificar la referencia y el denominador. No interpretar un porcentaje enorme cerca de cero como evidencia automática de una desviación absoluta grande.

### [PRÁCTICA] Indicadores con diferencias de ambos signos

**Enunciado narrado.** «La hoja de verificaciones simuladas de un analizador de ozono de una red, contrastado frente al SRP, presenta seis parejas de indicación y auditoría de referencia, todas de 100 nmol/mol. Son datos didácticos, generados determinísticamente al sumar los errores de la tabla a la referencia; no son mediciones de CALAIRE. Antes de resumir, confirmemos la convención: indicación menos auditoría, dividido por auditoría. Entreguen las seis diferencias $d_i$ y los tres resúmenes pedidos abajo; el orden de filas no representa una escala temporal ni afirma independencia entre verificaciones».

| Verificación | Auditoría (nmol/mol) | Indicación (nmol/mol) | $d_i$ (%) |
|---:|---:|---:|---:|
| 1 | 100,0 | 98,0 | −2,0 |
| 2 | 100,0 | 101,0 | +1,0 |
| 3 | 100,0 | 99,0 | −1,0 |
| 4 | 100,0 | 102,0 | +2,0 |
| 5 | 100,0 | 97,0 | −3,0 |
| 6 | 100,0 | 103,0 | +3,0 |

> **[MATERIAL]** Entregar la tabla y pedir que conserven tanto las diferencias firmadas como las magnitudes absolutas. Los datos son simulados de forma determinista: auditoría fija de 100 nmol/mol e indicaciones construidas sumando los errores enumerados.

«Calculen los seis $d_i$ con la convención escrita; luego obtengan la media firmada, la media de valores absolutos y el valor absoluto de la media. Expresen además las diferencias absolutas en nmol/mol. Expliquen qué resume cada indicador, si el porcentaje es interpretable cerca de cero y por qué esto no es la incertidumbre de calibración de un certificado».

**Solución docente verificable.** Los errores absolutos con signo son −2, +1, −1, +2, −3 y +3 nmol/mol. Como el denominador es 100, los valores numéricos de las diferencias porcentuales coinciden con esos errores: $d=[−2;+1;−1;+2;−3;+3]\%$. Su suma es cero, por lo que $\bar d=0,00\%$ y $|\bar d|=0,00\%$. La suma de magnitudes es 12 puntos porcentuales, así que $\operatorname{media}(|d_i|)=2,00\%$. La desviación estándar muestral es $s_d=2,3664\%$ (divisor 5). En escala absoluta, la media de magnitudes es 2,00 nmol/mol y el error firmado medio es 0,00 nmol/mol, solo porque cada auditoría vale exactamente 100.

Comprobación: ninguna de las seis diferencias es cero, aunque su media firmada sea cero; los signos se cancelan. Si la auditoría fuese cero, el porcentaje no estaría definido; cerca de cero reportarían la diferencia absoluta con su unidad y escalarían la elección del indicador. La media de magnitudes describe tamaño observado sin dirección; la media firmada describe dirección neta. Ninguna calcula la incertidumbre de una calibración: para eso haría falta el modelo y presupuesto de esa calibración.

**Decisión operativa.** Registrar ambos resúmenes con referencia, denominador, convención de signo, muestra y periodo. No declarar conformidad: no se ha suministrado criterio para esta serie. Consultar si el denominador no está definido o si la interpretación depende de porcentaje frente a diferencia absoluta.

**Criterio de logro.** Calcula correctamente los seis signos y ambos indicadores, conserva las unidades y explica por qué cero firmado no equivale a coincidencia individual.

### Señales de escalamiento

Antes de cerrar el nivel B, repasemos cuándo detener la plantilla y consultar. Si la referencia vale cero o está tan cerca de cero que el porcentaje no responde a la pregunta, no fabriquen un denominador; escalen la elección de una métrica absoluta. Si el archivo no deja claro cuál columna es el valor de auditoría, cuál es la indicación o qué signo se acordó, detengan el resumen hasta resolverlo. Si las diferencias positivas y negativas parecen cancelarse, informen qué resumen se está calculando y no eliminen el otro sin justificación. Si el indicador se compara con un límite y la muestra, periodo o procedimiento no coincide con el criterio que define ese límite, no clasifiquen la conformidad por analogía. Si hay pocas verificaciones, como las cuatro de este ejemplo, no presenten un límite como estable. Si el resultado queda cerca del criterio, detengan y consulten. Si el monitor cambió de escala o de ganancia, no comparen el antes y el después sin declararlo. Si las verificaciones están agrupadas en el tiempo, no las traten como independientes. Si aparece un valor atípico sin causa identificada, residuos con estructura o incertidumbre relevante tanto en la indicación como en la referencia, detengan el análisis y consulten antes de interpretar el agregado. Estas señales complementan el contenido básico y no lo sustituyen.

> **[ESCALAMIENTO]** El operador B se detiene y consulta cuando no puede identificar la referencia o el signo; cuando el denominador es nulo o inadecuado; cuando una conclusión depende de escoger entre una métrica relativa y otra absoluta; o cuando el criterio externo pertenece a otro diseño, equipo o periodo. Registrar la duda; no corregirla cambiando silenciosamente los datos.
>
> **[TRANSICIÓN]** En I añadiremos límites de confianza a los indicadores: veremos qué límite se está calculando, si es unilateral o bilateral y bajo qué hipótesis se puede interpretar.

## Nivel I — cuantificar límites y hacer explícita la escala

En I damos por visto todo B: la definición de la diferencia relativa con su denominador, el signo, la diferencia entre magnitud media y media firmada, y el cuidado con porcentajes cerca de cero. Ahora añadiremos límites de confianza con chi-cuadrado y t, distinguiremos límites unilaterales de intervalos bilaterales, estudiaremos qué cambia si se modifica la escala del monitor y usaremos la dispersión del cero para construir un umbral solo bajo hipótesis expresas. Un límite de confianza describe incertidumbre estadística de un indicador bajo un modelo; no transforma por sí mismo ese indicador en tolerancia, límite de control ni límite de detección.

### Escena I1. Un límite superior de precisión con chi-cuadrado

> **[DIAPOSITIVA]** Repetir las cuatro diferencias firmadas simuladas: −2 %, +1 %, −1 %, +2 %. Al lado, mostrar el número de observaciones $n=4$, la desviación estándar muestral y el cuantil inferior de chi-cuadrado.

Partamos de la medida de dispersión de M4: la desviación estándar muestral de las diferencias relativas, calculada con divisor $n−1$; la razón de ese divisor está en el Anexo AX.1 y su definición, en GUM 4.2.2. Para interpretar el límite chi-cuadrado como un límite exacto para la desviación poblacional, suponemos verificaciones independientes, de una misma población normal y con varianza constante. Nuestros cuatro números son una construcción determinista para ilustrar la cuenta; no prueban esas hipótesis ni acreditan cobertura empírica. [NIST/SEMATECH, intervalo de confianza para la desviación estándar; no disponible en docs/] En el procedimiento de evaluación de controles de un punto de la EPA, el indicador de precisión se construye como un límite superior de confianza del 90 por ciento para la dispersión, mediante la distribución chi-cuadrado con $n−1$ grados de libertad. La expresión utiliza la desviación estándar muestral de los $d_i$ multiplicada por la raíz del cociente entre $n−1$ y el cuantil del diez por ciento de chi-cuadrado. El cuantil es inferior porque buscamos un límite superior para una desviación desconocida. [CFR58-A §4.1.2]

> **[PIZARRA]** $$L_{90}(s_d)=s_d\sqrt{\frac{n-1}{\chi^2_{0,10;n-1}}},\qquad s_d=\sqrt{\frac{\sum_i(d_i-\bar d)^2}{n-1}}$$
>
> **[NOTA AL INSTRUCTOR]** La deducción de esta expresión está en el Anexo AX.11; aquí la usamos. Leer: «ele ese noventa de la desviación es la desviación muestral multiplicada por la raíz del cociente entre ene menos uno y el cuantil diez por ciento de chi-cuadrado, con ene menos uno grados de libertad». Aclarar que la EPA denomina CV al estimador de precisión de esta aplicación; no sustituirlo por otra definición de CV sin revisar la convención.

Con nuestro ejemplo **simulado**, la media firmada es cero por ciento y la desviación estándar muestral es uno coma ocho dos seis por ciento. Hay cuatro observaciones, así que tenemos tres grados de libertad. El cuantil diez por ciento de chi-cuadrado con tres grados de libertad es cero coma cinco ocho cuatro. Sustituyendo en la fórmula, el límite superior unilateral del 90 por ciento es aproximadamente cuatro coma uno cuatro por ciento. El script conserva cifras completas; redondeamos aquí para leerlo. No hemos calculado una incertidumbre de calibración: calculamos el límite superior de un indicador agregado de dispersión para el conjunto simulado.

> **[EJEMPLO]** Datos **simulados**: $d=[-2, +1, -1, +2] \%$, $n=4$, $s_d=1,8257 \%$, $χ²₀,₁₀;₃=0,5844$. Resultado: $L₉₀(s_d)=4,1367 \%$.
>
> **[PIZARRA]** $1,8257\sqrt{3/0,5844}=4,1367\%$.

La fuente regulatoria establece para analizadores automáticos de ozono una meta de límite superior de confianza del 90 por ciento para el CV de siete por ciento, y una meta distinta de límite superior del 95 por ciento para el sesgo absoluto de siete por ciento. Son metas de ese marco de aseguramiento; no son límites universales que podamos aplicar a cualquier cliente, calibración o población. Si solo quisiéramos comparar la cifra didáctica con esa meta para aprender la lectura, cuatro coma uno cuatro es menor que siete, pero esa comparación numérica no califica un equipo real ni reemplaza la comprobación de que el muestreo y el procedimiento sean los especificados. [CFR58-A §2.3.1.2]

> **[ERROR CRÍTICO]** No reemplazar el cuantil chi-cuadrado por el de otra cola. No confundir el límite superior unilateral del 90 por ciento para la dispersión con un intervalo bilateral del 90 por ciento, una tolerancia o una incertidumbre expandida. No aplicar la meta del CFR a otro diseño como si el documento la declarara universal.

### Escena I2. El límite de sesgo absoluto no conserva el signo por sí solo

> **[DIAPOSITIVA]** Dos filas: arriba, diferencias originales con signo; abajo, sus valores absolutos. Dibujar una flecha «límite superior unilateral» y otra «signo asignado por los percentiles originales».

Ahora pasemos al indicador de sesgo absoluto que define la EPA para sus verificaciones de un punto. Primero se calcula $AB$, el promedio de los valores absolutos de las diferencias. Después se añade un término con la desviación estándar de esos valores absolutos, el cuantil 95 de Student y la raíz de $n$. El procedimiento lo denomina límite superior unilateral del 95 por ciento para el sesgo absoluto. Para interpretarlo como límite inferencial de la media de las magnitudes, necesitamos independencia y una aproximación t adecuada. Tomar valores absolutos de diferencias normales no produce una muestra normal. Con solo cuatro valores, la cobertura nominal no está garantizada: reproducimos la fórmula regulatoria, no demostramos un límite exacto del 95 por ciento para esta muestra determinista. La fórmula usa una cola: estamos acotando por arriba, no construyendo un intervalo simétrico alrededor de una media firmada. [GUM G.3.2] [CFR58-A §4.1.3]

> **[PIZARRA]** $$L_{95}(\mathrm{AB})=\mathrm{AB}+t_{0,95;n-1}\frac{\mathrm{AS}}{\sqrt n},\qquad \mathrm{AB}=\operatorname{media}(|d_i|)$$
>
> **[NOTA AL INSTRUCTOR]** Leer $AS$ como la desviación estándar muestral de los valores absolutos $\lvert d_i\rvert $, no de los valores originales con signo. La deducción se remite a AX.11; el divisor $n−1$ se explica en AX.1.

Con los cuatro datos **simulados**, los valores absolutos son dos, uno, uno y dos por ciento. Su promedio $AB$ es uno coma cinco por ciento, y su desviación estándar $AS$ es cero coma cinco siete siete cuatro por ciento. El cuantil 95 de Student con tres grados de libertad es dos coma tres cinco tres. El término añadido vale aproximadamente cero coma seis ocho por ciento, y el límite superior unilateral resulta dos coma uno ocho por ciento. La cifra se parece a $\operatorname{media}(\lvert d_i\rvert )$, pero no es esa media: es una cota superior que incorpora la variabilidad y el tamaño muestral bajo el procedimiento indicado.

> **[EJEMPLO]** Datos **simulados**: $AB=1,5000 \%$, $AS=0,5774 \%$, $t₀,₉₅;₃=2,3534$, $n=4$. Resultado: $L₉₅(AB)=2,1794 \%$.
>
> **[PIZARRA]** $1,5000+2,3534\times0,5774/\sqrt4=2,1794\%$.

La magnitud absoluta no dice si el sesgo va hacia arriba o hacia abajo. El procedimiento regulatorio asigna una señal de signo usando los percentiles 25 y 75 de las diferencias originales. Se marca positivo si ambos son positivos, negativo si ambos son negativos y no se marca signo si quedan a lados opuestos de cero. En nuestros cuatro datos simulados hay diferencias positivas y negativas. Por eso no proclamamos «sesgo positivo» ni «sesgo negativo» a partir de $L₉₅(AB)$. La regla de signos y la definición del límite están separadas explícitamente en el documento. [CFR58-A §§4.1.3.1–4.1.3.2]

> **[PREGUNTA AL GRUPO]** ¿El límite de dos coma dieciocho por ciento nos dice en qué dirección se desvió el monitor? — *Respuesta esperada:* no; limita una magnitud absoluta. La dirección se evalúa con las diferencias firmadas y la regla de percentiles.

Hay otra pregunta posible: ¿qué intervalo bilateral de Student cubre la media firmada $μ_d$? Para los mismos datos, la media es cero por ciento; su error estándar es $s_d/√n$, que vale cero coma nueve uno tres por ciento. Para un intervalo bilateral central del 95 por ciento usamos el cuantil $t₀,₉₇₅;₃$, no $t₀,₉₅;₃$. El resultado es aproximadamente desde menos dos coma nueve uno por ciento hasta más dos coma nueve uno por ciento. Ese intervalo bilateral trata la media firmada; no es el límite unilateral del promedio de valores absolutos que acabamos de calcular. Es una demostración útil de que el nivel de confianza y el lado de la pregunta determinan el cuantil.

> **[PIZARRA]** $$\bar d\pm t_{0,975;n-1}\frac{s_d}{\sqrt n}$$ [GUM 4.2.2–4.2.3 y G.3.2; AX.1; AX.11]
>
> **[EJEMPLO]** Con datos **simulados**: $IC bilateral 95 \% para μ_d = [-2,9052 \%, +2,9052 \%]$. Este intervalo de la media firmada y $L₉₅(AB)=2,1794 \%$ son resultados distintos y no deben intercambiarse.

Un intervalo bilateral central reparte la probabilidad de no cobertura entre las dos colas; un límite superior unilateral deja esa probabilidad en una sola cola. En estos ejemplos, el límite superior del 90 por ciento para la desviación usa el cuantil inferior 0,10 de chi-cuadrado porque invertimos el cociente de varianzas. El límite superior del 95 por ciento para la media de magnitudes usa el cuantil 0,95 de Student. Cambian tanto el parámetro y su distribución como el nivel de confianza; no atribuimos esa diferencia solo al número de colas. Si el propósito es detectar cualquier dirección del desplazamiento, una pregunta bilateral puede ser adecuada. Si el criterio especifica una cota superior para una magnitud no negativa, corresponde la formulación unilateral de ese criterio. No elegimos unilateral o bilateral para conseguir una conclusión conveniente; lo fijan la pregunta y el procedimiento antes de mirar el resultado. Los límites aquí usados y las distribuciones de referencia están declaradas en el apéndice regulatorio. Para la distribución chi-cuadrado aplicada al límite de dispersión, seguimos el procedimiento específico de CFR58-A §4.1.2. Para el intervalo t de la media firmada suponemos observaciones independientes de una misma población normal: GUM G.3.2 explicita estas condiciones; GUM 4.2.2–4.2.3 define la desviación muestral y la del promedio. El intervalo no demuestra normalidad ni independencia. [GUM 4.2.2–4.2.3 y G.3.2] [CFR58-A §§4.1.2–4.1.3]

> **[ERROR CRÍTICO]** No usar $t₀,₉₅$ donde el intervalo bilateral de 95 por ciento requiere $t₀,₉₇₅$. No interpretar que un intervalo bilateral que contiene cero prueba equivalencia. No asignar signo al límite calculado con $\lvert d_i\rvert $ sin volver a la serie firmada.

### Escena I3. Un cambio de escala cambia el error relativo si cambia la respuesta

> **[DIAPOSITIVA]** Un monitor, una ganancia multiplicativa y una auditoría fija. Separar dos flechas: «cambiar unidades en ambas columnas» y «cambiar la escala de respuesta del monitor».

La palabra escala puede referirse a operaciones diferentes. Si solo cambiamos la unidad y multiplicamos tanto $\mathrm{meas}$ como $\mathrm{audit}$ por la misma conversión, la diferencia relativa no cambia: el factor común se cancela en el cociente. En cambio, si cambia la ganancia del monitor y su indicación se multiplica por un factor mientras la referencia se mantiene, cambia el numerador y por tanto cambia la diferencia relativa. Esto es un cambio del resultado del equipo, no una conversión de unidades. Antes de comparar series, debemos saber cuál de estas dos operaciones ocurrió.

En un ejemplo **simulado**, la auditoría vale cien nmol/mol y el monitor indica ciento uno. El indicador es más uno por ciento. Supongamos ahora que el resultado del monitor se transforma por un factor de escala de uno coma cero uno, mientras la auditoría y la convención siguen iguales. La nueva indicación es ciento dos coma cero uno nmol/mol. La diferencia absoluta pasa de más uno a más dos coma cero uno nmol/mol; la diferencia relativa pasa de más uno a más dos coma cero uno por ciento. El denominador sigue siendo cien nmol/mol, porque es la auditoría, no la indicación transformada.

> **[EJEMPLO]** Datos **simulados**: $\mathrm{audit}=100 nmol/mol$, $\mathrm{meas}=101 nmol/mol$; después $\mathrm{\mathrm{meas}}'=1,01×\mathrm{meas}=102,01 nmol/mol$. Resultado: $d=+1,00 \%$ antes y $d′=+2,01 \%$ después del cambio de escala.
>
> **[PIZARRA]** $$d'=\frac{1,01\,\mathrm{meas}-\mathrm{audit}}{\mathrm{audit}}\times100\%=2,01\%$$

No digamos que el porcentaje «no depende de la escala» sin precisar qué escala. La unidad común se cancela; la ganancia del instrumento no. Además, si se compara la magnitud del error relativo a distintas concentraciones, la misma desviación absoluta puede dar porcentajes diferentes porque cambia el denominador. En toda serie debe mantenerse explícito qué fue reescalado, cuál referencia se usó y si la métrica es absoluta o relativa. Esto completa la advertencia de M1 sobre el cambio de escala: la transformación se evalúa con los valores realmente implementados, no con el nombre que recibe el ajuste.

> **[PREGUNTA AL GRUPO]** Si convertimos ambos valores de nmol/mol a otra unidad con el mismo factor, ¿cambia $d_i$? — *Respuesta esperada:* no. Si multiplicamos solo la indicación del monitor por una ganancia nueva y dejamos fija la referencia, sí cambia.

### Escena I4. Dispersión del cero y umbral bajo hipótesis declaradas

> **[DIAPOSITIVA]** Una serie simulada de respuesta en cero alrededor de cero nmol/mol. Mostrar su media, desviación estándar $s₀$ y una línea marcada $±3s₀$ con el rótulo «umbral ilustrativo bajo hipótesis; no definición universal».

Cuando la referencia es cero, el porcentaje relativo no se puede calcular. Para estudiar las respuestas de cero en una escala absoluta, resumimos sus lecturas en nmol/mol. La desviación estándar de esas respuestas describe su dispersión bajo las condiciones muestreadas; su interpretación depende de que las lecturas representen la unidad de repetición y condiciones definidas. La norma EN 14625, por ejemplo, especifica una prueba de repetibilidad en cero y calcula una característica de detección usando la desviación estándar de repetibilidad en cero junto con la pendiente de la función de calibración. No define el límite de detección como $3·s₀$ sin más. [EN 14625 §3.12, §8.4.5 y fórmula 5]

Tomemos cinco respuestas al cero **simuladas**: menos cero coma dos, menos cero coma uno, cero, más cero coma uno y más cero coma dos nmol/mol. Su promedio es cero y la desviación estándar muestral, calculada con divisor cuatro, es cero coma uno cinco ocho uno nmol/mol. Si, solo para construir una regla didáctica de señal, suponemos respuestas independientes, una distribución normal estable, media de cero conocida y desviación representada por esa estimación, podemos mostrar el umbral simétrico $±3s₀$, que vale aproximadamente $±0,4743 nmol/mol$. Es un umbral definido por esas hipótesis, no una afirmación de que todo valor fuera de él sea detectable, ni una definición general del límite de detección. Con cinco respuestas estimamos la desviación; no conocemos su valor poblacional. Por eso $3s_0$ no garantiza la probabilidad de falsa alarma de una regla normal con desviación conocida. Para una decisión real habría que justificar la incertidumbre de esa estimación y la cobertura, como en M4 y M10. [GUM G.3.2]

> **[EJEMPLO]** Datos **simulados**: respuestas al cero $[−0,2; −0,1; 0; +0,1; +0,2] nmol/mol$. $s₀=0,1581 nmol/mol$; umbral didáctico $3s₀=0,4743 nmol/mol$, solo bajo las hipótesis narradas.
>
> **[PIZARRA]** Si se adopta expresamente el umbral de señal bajo el modelo indicado: $c_0=3s_0$, donde $c_0$ es el umbral de cero. No escribir «límite de detección universal».

En el método de EN 14625, el límite de detección especificado se calcula como $3,3·sᵣ,₀/B$, donde $sᵣ,₀$ es la desviación de repetibilidad en cero y $B$ es la pendiente de la función de calibración. El número tres coma tres, el uso de repetibilidad y la pendiente pertenecen a esa definición de método; no los reemplazamos por tres veces una desviación cualquiera. La norma también fija el diseño de mediciones para obtener $sᵣ$ y un criterio de repetibilidad en cero. Si el operador está trabajando bajo ese procedimiento, debe usar la definición completa y aplicable de la norma; el ejemplo $3s₀$ de esta clase solo enseña cómo se construye un umbral estadístico bajo condiciones previamente especificadas. [EN 14625 §§3.12 y 8.4.5, fórmula 5 y Tabla 1]

> **[ERROR CRÍTICO]** No llamar límite de detección a $3s₀$ sin establecer población, distribución, independencia, estabilidad, referencia y objetivo de decisión. No omitir la pendiente cuando se usa la definición de EN 14625. No calcular porcentaje relativo con cero como denominador.

### [PRÁCTICA] Indicadores, límites y cambio de escala

**Enunciado narrado.** «En I ya elegimos la referencia y conservamos el signo. Ahora aplicaremos límites de confianza y examinaremos una ganancia nueva y una serie de cero en verificaciones simuladas de un analizador de ozono de la red contrastado frente al SRP: auditoría de 100 nmol/mol en todas, e indicaciones 98, 101, 99, 102, 97 y 103 nmol/mol. Para el umbral del cero, recibimos además cinco respuestas simuladas. Son datos didácticos deterministas, construidos con esos valores, no mediciones de CALAIRE. La respuesta de interés son los indicadores de esta campaña simulada, no una lectura futura».

«Calculen la media y desviación muestral de $d$, el límite superior unilateral del 90 % para la desviación con chi-cuadrado, el límite superior unilateral del 95 % para la media de $|d|$ con la fórmula del capítulo y el intervalo bilateral del 95 % para la media firmada. Después multipliquen las indicaciones por una ganancia de 1,01 sin alterar la auditoría y repitan la media de magnitudes. Por último, calculen $s_0$ y $3s_0$ para las respuestas al cero; indiquen bajo qué hipótesis es solo un umbral didáctico y qué no permite concluir».

| Verificación | Auditoría (nmol/mol) | Indicación (nmol/mol) | $d_i$ (%) |
|---:|---:|---:|---:|
| 1 | 100,0 | 98,0 | −2,0 |
| 2 | 100,0 | 101,0 | +1,0 |
| 3 | 100,0 | 99,0 | −1,0 |
| 4 | 100,0 | 102,0 | +2,0 |
| 5 | 100,0 | 97,0 | −3,0 |
| 6 | 100,0 | 103,0 | +3,0 |

Respuestas simuladas al cero: $[−0,2;−0,1;0;+0,1;+0,2]$ nmol/mol.

**Solución docente verificable.** De la práctica B se obtiene $\bar d=0,0000\%$ y $s_d=2,3664\%$, con $n=6$ y 5 grados de libertad. El cuantil $\chi^2_{0,10;5}=1,6103$, así que $L_{90}(s_d)=2,3664\sqrt{5/1,6103}=4,1699\%$. Para los valores absolutos $[2;1;1;2;3;3]\%$, $AB=2,0000\%$ y $AS=0,8944\%$; con $t_{0,95;5}=2,0150$, $L_{95}(AB)=2+2,0150(0,8944/\sqrt6)=2,7358\%$. El intervalo bilateral de la media firmada usa $t_{0,975;5}=2,5706$ y queda $[−2,4834;+2,4834]\%$. Es distinto del límite unilateral de $AB$; ninguno prueba equivalencia ni establece una tolerancia.

Tras multiplicar cada indicación por 1,01, las diferencias relativas son aproximadamente $[−1,02;+2,01;−0,01;+3,02;−2,03;+4,03]\%$ y la media de magnitudes es 2,0200 %. La transformación de escala del equipo no es una conversión de unidades: referencia fija y respuesta modificada producen valores nuevos. En cero, $s_0=0,1581$ nmol/mol y $3s_0=0,4743$ nmol/mol. Solo se puede llamar umbral didáctico si se declaran independencia, normalidad, estabilidad y la interpretación de la media; con cinco observaciones la dispersión poblacional no es conocida. No se define universalmente un límite de detección, y la definición aplicable de EN 14625 incorpora repetibilidad y pendiente.

**Decisión operativa.** Informar los límites con su cola, nivel, grados de libertad, fórmula y supuestos. La serie corta y simulada no califica un monitor ni reemplaza el criterio del procedimiento. Si las verificaciones no son independientes, la muestra es insuficiente para la inferencia pretendida o el resultado está cerca de un criterio, detener la clasificación y escalar el modelo/cobertura. Para auditoría cero usar una diferencia absoluta, no un porcentaje indefinido.

**Criterio de logro.** Elige los cuantiles y colas correctos, diferencia el intervalo de la media del límite de magnitudes y describe correctamente qué cambió con la ganancia y qué hipótesis limitan $3s_0$.

## Nivel A — conservar la dependencia y separar los periodos

En A damos por visto todo B e I: cómo definimos las diferencias, cómo resumimos magnitud y dirección, qué límites de confianza corresponden y por qué la escala y las hipótesis importan. Ahora añadimos dos problemas de series agregadas. Primero, varias verificaciones pueden depender entre sí porque se hicieron en un mismo periodo o comparten una fuente. Segundo, una serie puede mezclar periodos distintos, por ejemplo, antes y después de un mantenimiento o cambio de escala. Un resumen agregado solo tiene interpretación si representa la población y el diseño que se quieren describir.

### Escena A1. Las verificaciones dependientes no equivalen a nuevas réplicas independientes

> **[DIAPOSITIVA]** Cuatro verificaciones organizadas por dos periodos, dos filas por periodo. En cada periodo, un sombreado une las dos verificaciones para indicar una causa temporal común. Debajo, una línea aparte marca una contribución de trazabilidad compartida por toda la serie.

Si varias verificaciones comparten una causa, no podemos tratarlas como información nueva e independiente solo porque ocupan filas diferentes. Dos mediciones próximas en el tiempo pueden verse afectadas por la misma condición operativa; dos verificaciones también pueden usar una misma referencia o corrección. La covarianza describe una parte de esa relación. La GUM indica que las correlaciones significativas entre resultados relacionados deben tomarse en cuenta. Su expresión de varianza combinada incluye covarianzas. La deducción de varianzas de combinaciones lineales está en AX.2; aquí nos quedamos con la consecuencia operativa: la incertidumbre del agregado depende de cómo se relacionan las observaciones. [GUM 5.2.1–5.2.2; AX.2]

> **[PIZARRA]** Para observaciones con varianzas y covarianzas, la varianza del promedio incluye términos cruzados: $$\operatorname{Var}(\bar d)=\frac{1}{n^2}\left[\sum_i\operatorname{Var}(d_i)+2\sum_{i<j}\operatorname{Cov}(d_i,d_j)\right].$$
>
> **[NOTA AL INSTRUCTOR]** Leer: «la varianza del promedio incluye las varianzas individuales y dos veces las covarianzas entre pares, todo dividido por ene al cuadrado». No desarrollar la deducción; remitir a AX.2. La expresión presupone que se está modelando un promedio y que la matriz de covarianza representa el diseño. Como $d_i$ está expresado en porcentaje, las desviaciones de sus valores numéricos se leen en puntos porcentuales; las covarianzas, en puntos porcentuales al cuadrado. El signo % que usamos en los resultados mantiene la convención del indicador EPA, no significa porcentaje relativo de otro porcentaje.

Construyamos una serie **simulada** por dos periodos, con dos verificaciones en cada uno: medio, uno y medio, dos y medio, tres y medio por ciento. La media agregada es dos por ciento. Si ignoramos el agrupamiento y calculamos el error estándar como si fueran cuatro observaciones independientes, la desviación estándar muestral dividida por raíz de cuatro da cero coma seis cuatro cinco por ciento. Si primero hacemos los dos promedios de periodo, obtenemos uno y tres por ciento; la desviación estándar de esos dos promedios dividida por raíz de dos da uno por ciento. No estamos proponiendo este último número como estimación estable: solo tenemos dos periodos, demasiado pocos para una inferencia fiable sobre la variabilidad entre periodos. La diferencia entre ambos cálculos ilustra que la unidad de repetición cambia la incertidumbre del agregado; no es permiso para elegir el resultado mayor ni para reemplazar un modelo de covarianza por dos grupos improvisados.

> **[EJEMPLO]** Datos **simulados**, agrupados por periodo: periodo 1 $[0,5; 1,5] \%$, periodo 2 $[2,5; 3,5] \%$. Media total $2,00 \%$; error estándar calculado como si las cuatro observaciones fueran independientes $0,6455 \%$; error estándar entre las dos medias de periodo $1,0000 \%$. El contraste es ilustrativo, no una estimación final ni una comparación de conformidad.
>
> **[PIZARRA]** «Antes de resumir: ¿cuál es la unidad independiente: la verificación, el periodo, la campaña o el bloque definido por el modelo?»

En un caso real, primero graficaríamos las diferencias por orden temporal y periodo, revisaríamos cómo se planificaron las verificaciones y consultaríamos si hay cambios de procedimiento, mantenimiento, condiciones o patrón. Si la dependencia temporal es relevante, la distribución de la media y sus límites no se obtienen aplicando mecánicamente la fórmula independiente. Habría que modelar la estructura o construir el resumen con la unidad de repetición apropiada. El detalle de métodos de series temporales queda fuera del contenido que asigna este módulo; la señal que sí debe reconocer quien trabaja en A es que un indicador calculado con supuestos de independencia no queda validado por una salida numérica reproducible. [GUM 5.2.1–5.2.2]

> **[ERROR CRÍTICO]** No contar verificaciones dependientes como réplicas independientes. No convertir una serie agrupada en una muestra iid mediante el simple acto de concatenar sus filas. No usar el resultado del script como evidencia de que el modelo de dependencia sea correcto.

### Escena A2. La trazabilidad común permanece en el indicador agregado

> **[DIAPOSITIVA]** Ocho verificaciones conectadas a una referencia común. Una flecha roja representa el componente compartido y flechas grises distintas representan fluctuaciones propias de cada verificación. Al promediar, solo las flechas independientes se atenúan; la componente común sigue presente.

Hay una dependencia que interesa especialmente en una red: la trazabilidad de varias verificaciones puede pasar por un mismo patrón, certificado, corrección o escala. Si esa contribución común mueve todas las diferencias en la misma dirección, promediar más verificaciones no la elimina. Para una suma ponderada de resultados, las covarianzas entre los términos compartidos contribuyen a la incertidumbre del agregado; la covarianza no es una característica que desaparezca porque cada observación tenga su propia fila. [GUM 5.2.1–5.2.2]

En una ilustración **simulada**, asignemos una contribución común de más cero coma ocho por ciento a cada verificación. El promedio de dos copias de esa contribución sigue siendo más cero coma ocho por ciento; el promedio de ocho copias también. Esto no significa que el sesgo real de una red sea cero coma ocho, ni que hayamos estimado una incertidumbre de trazabilidad. Es solo una identidad aritmética para ver el efecto de una contribución igual y común. Si añadimos variación independiente a cada verificación, esa parte puede promediarse según su diseño, pero la componente común debe mantenerse en el presupuesto o en el modelo de comparación.

> **[EJEMPLO]** Contribución compartida **simulada**: $+0,80 \%$ en cada verificación. Promedio de dos contribuciones: $+0,80 \%$; promedio de ocho: $+0,80 \%$. La cantidad no disminuye con $1/√n$ porque no representa ruido independiente entre observaciones.

Ahora cuantifiquemos la incertidumbre, no solo un desplazamiento fijo. En otro modelo **simulado** para la media firmada, cada verificación contiene una contribución común de media cero e incertidumbre estándar $u_{\mathrm{com}}=0,80$ puntos porcentuales y una contribución independiente de incertidumbre $u_{\mathrm{ind}}=0,60$ puntos porcentuales. Ambas fuentes son independientes entre sí. La varianza de la media es $u_{\mathrm{com}}^2+u_{\mathrm{ind}}^2/n$: leemos «la varianza común permanece y la independiente se divide por ene». Para dos verificaciones obtenemos $u(\bar d)=0,9055$ puntos porcentuales; para ocho, $0,8276$. El límite al aumentar la muestra es $0,80$, no cero. La matriz tiene diagonal $1,00$ y elementos fuera de diagonal $0,64$, todos en puntos porcentuales al cuadrado; representa exactamente esa fuente común. No aplicamos estos valores a los límites regulatorios calculados con independencia en I. [GUM 5.2.2; AX.2]

> **[PIZARRA]** «Más verificaciones pueden precisar la variación propia; no borran una fuente común de trazabilidad».

La media agregada de diferencias puede entonces ser precisa respecto a la variación propia de las verificaciones y, al mismo tiempo, conservar incertidumbre o sesgo común que no se revela por la dispersión entre filas. Esta es una razón para no confundir desempeño agregado con la incertidumbre de la calibración que estableció la escala del patrón. El primer indicador describe las diferencias que se observaron en una población y un periodo; el presupuesto de calibración describe las fuentes que afectan a un resultado de calibración particular. Para conectarlos hace falta conocer qué contribuciones son comunes, qué resultados dependen de ellas y cómo se incorporaron. [GUM 5.2.1–5.2.2; CFR58-A §§2.3.1.2 y 4.1.1–4.1.3]

> **[PREGUNTA AL GRUPO]** Si duplicamos el número de verificaciones y todas comparten el mismo desplazamiento de referencia, ¿ese componente se reduce a la mitad? — *Respuesta esperada:* no. El promedio conserva una contribución común; solo la variación independiente se reduce al promediar bajo sus supuestos.

### Escena A3. Mezclar periodos puede ocultar el desempeño que se quiere describir

> **[DIAPOSITIVA]** Dos periodos con sus propias series: antes de una intervención, diferencias alrededor de un nivel; después, diferencias alrededor de otro. A la derecha, una media conjunta que cae entre ambos. No asignar a la intervención una causa que los datos no prueban.

Supongamos que una base de verificaciones cubre meses anteriores y posteriores a un mantenimiento, o mezcla dos escalas de operación. Si juntamos todos los valores y reportamos una sola media de magnitudes, una sola media firmada y un solo límite, podemos ocultar que el sistema cambió de comportamiento. La media conjunta responde a la mezcla concreta de periodos y al número de observaciones de cada uno; no describe necesariamente ninguno de los periodos por separado. Un cambio aparente tampoco demuestra por sí solo qué intervención lo causó. La decisión de combinar periodos debe apoyarse en que el diseño y la pregunta de desempeño hagan comparable la población.

Volvamos al ejemplo **simulado** de dos periodos. El primero tiene media uno por ciento y el segundo media tres por ciento. La media conjunta de dos por ciento parece un valor intermedio razonable, pero ninguna de las dos medias de periodo es dos por ciento. Si el objetivo es describir el periodo posterior al mantenimiento, el promedio combinado contesta otra pregunta y pondera el resultado por la cantidad de observaciones de cada periodo. Si la pregunta es el desempeño anual, los periodos pueden combinarse solo si la definición anual, la cobertura y la métrica justifican esa agregación. No elegimos el periodo que dé el resultado más favorable.

> **[PIZARRA]** Antes de combinar: periodo, referencia, procedimiento, escala, cobertura y criterio. Presentar estratos cuando los periodos no representan la misma población o proceso.
>
> **[ERROR CRÍTICO]** No mezclar periodos, escalas o procedimientos sin declarar qué población representa el agregado. No retirar el periodo que empeora el indicador para cumplir un umbral. No atribuir causalidad al mantenimiento solo porque las medias sean distintas.

Ahora consultemos la ficha común `S3_01_ficha_criterios.md`, compartida con M10, M11 y el caso C. Identifica equipo o proceso, documento y edición, etapa, diseño, estadístico, divisor, unidades y fuente; los números docentes no autorizan decisiones reales. Vinculemos esta lectura con tres clases de criterios que suelen aparecer en un expediente. Una tolerancia es un límite de aceptación para un resultado bajo una regla de decisión. Un límite de control describe el comportamiento de un proceso en una carta y sirve para detectar señales en el tiempo. Un umbral de indicador es una regla de interpretación para una estadística agregada bajo el procedimiento que la define. Los tres pueden expresarse con números y aun así contestar preguntas distintas. La conformidad de un instrumento individual no se deduce del desempeño agregado de un conjunto de verificaciones; y un agregado favorable no demuestra que cada instrumento sea conforme. Para resolver una discrepancia hay que declarar muestra, referencia, periodo, métrica, cobertura y criterio, y luego aportar la evidencia que falta. [CFR58-A §§2.3.1.2 y 4.1.1–4.1.3; M10]

> **[PREGUNTA AL GRUPO]** Si un monitor individual cumple su tolerancia, ¿eso garantiza que la red tenga un indicador agregado aceptable? — *Respuesta esperada:* no. Son preguntas distintas y requieren evidencia y criterios distintos.

### [PRÁCTICA] Discrepancia entre conformidad individual y desempeño agregado

**Enunciado narrado.** «Una red de analizadores de ozono contrastados frente al SRP presenta dos señales que parecen discrepar. Las tres verificaciones posteriores son del mismo monitor, el monitor X, y forman parte de las seis verificaciones cronológicas completas de una campaña docente simulada de ese único equipo; la campaña no cubre otros monitores ni pretende representar una red. Todas usan una referencia de 100 nmol/mol cuya trazabilidad aporta una incertidumbre estándar común. Los datos son simulados de forma determinista, sumando las diferencias de la tabla a la referencia; no proceden de CALAIRE. Para este ejercicio fijamos tres criterios distintos: tolerancia individual $|e|\leq2,0$ nmol/mol para cada una de las tres comprobaciones posteriores; umbral de desempeño agregado $\operatorname{media}(|d_i|)\leq2,5\%$ para esas tres verificaciones posteriores; y límites de control de la carta histórica, ya calculados como $−1,0$ y $+1,0\%$. Son criterios docentes, no límites regulatorios ni decisiones reales».

| Periodo | Verificación | Auditoría (nmol/mol) | Indicación (nmol/mol) | $d_i$ (%) |
|---|---:|---:|---:|---:|
| Antes | 1 | 100,0 | 100,5 | +0,5 |
| Antes | 2 | 100,0 | 101,0 | +1,0 |
| Antes | 3 | 100,0 | 101,5 | +1,5 |
| Después | 4 | 100,0 | 102,5 | +2,5 |
| Después | 5 | 100,0 | 103,0 | +3,0 |
| Después | 6 | 100,0 | 103,5 | +3,5 |

«Calculen media firmada y media de magnitudes por periodo y en el conjunto. Evalúen por separado las tres comprobaciones individuales posteriores, el umbral agregado posterior y la señal frente a los límites de control en toda la secuencia cronológica. Expliquen por qué no deben combinarse los periodos automáticamente ni usar una de esas decisiones como sustituto de otra. La incertidumbre estándar común de trazabilidad es 0,80 puntos porcentuales y la independiente por verificación es 0,60 puntos porcentuales: calculen la incertidumbre estándar de la media posterior con tres verificaciones bajo el modelo común más independiente. Finalmente, indiquen qué evidencia se necesita para resolver la discrepancia sin atribuir causalidad al mantenimiento».

**Solución docente verificable.** Antes del mantenimiento, las diferencias son $[0,5;1,0;1,5]\%$: media firmada y media de magnitudes, ambas 1,00 %. Después son $[2,5;3,0;3,5]\%$: ambas medias son 3,00 %. Juntas, las seis tienen media firmada y media de magnitudes 2,00 %. El agregado de 2,00 % no describe ninguno de los dos periodos por separado y, además, no es el estadístico especificado para evaluar el periodo posterior.

Cada una de las tres comprobaciones posteriores del monitor X excede la tolerancia: $e_4=+2,5$, $e_5=+3,0$ y $e_6=+3,5$ nmol/mol, todos mayores que 2,0 nmol/mol; cada resultado es no conforme bajo la regla suministrada. Para el periodo posterior, la media de magnitudes 3,00 % supera el umbral agregado de 2,5 %. En la carta, la verificación 3 anterior al mantenimiento ya supera el límite superior de control (+1,5 % frente a +1,0 %), al igual que las tres verificaciones posteriores (+2,5; +3,0; +3,5 %); la señal no empieza exactamente después del mantenimiento. Son señales para investigar la secuencia completa, no pruebas de incumplimiento de la tolerancia ni reglas de aceptación del agregado. Los criterios contestan preguntas diferentes.

Bajo el modelo declarado de componente común de media cero y desviación estándar 0,80 puntos porcentuales, más componente independiente de 0,60 por verificación, $u(\bar d)=\sqrt{0,80^2+0,60^2/3}=0,8718$ puntos porcentuales. La contribución común no se divide por tres. Esta incertidumbre del promedio firmado no convierte automáticamente el umbral basado en media de magnitudes en prueba inferencial; el ejercicio suministra ese criterio como regla descriptiva.

**Decisión operativa.** Mantener estratos por periodo, etiquetar las decisiones individuales, agregada y de control por separado, y retener/investigar el monitor según el procedimiento aplicable; la carta muestra una señal antes y después, por lo que se revisa la secuencia completa y sus fechas, no se atribuye al mantenimiento ni se recalibra automáticamente solo por la carta. Antes de extender una conclusión a una red, solicitar datos de otros monitores y campañas, referencias y trazabilidad, fechas y definición de periodo, cambios de escala/procedimiento, serie temporal y dependencia, incertidumbres comunes e independientes, definición y cobertura del agregado, regla individual y límites de control documentados. Escalar si falta cualquiera de esos elementos o si se pretende inferencia que el modelo no respalda.

**Criterio de logro.** Separa correctamente conformidad individual, indicador agregado y señal de control; conserva los periodos y cuantifica la parte común sin promediarla como ruido independiente.

## Cierre del capítulo

Cerramos con tres escalas de trabajo. En B, ustedes definen la referencia, el signo y el denominador; distinguen la media de valores absolutos del valor absoluto de la media; y cambian a una métrica absoluta cuando el porcentaje pierde sentido cerca de cero. En I, añaden límites de confianza y distinguen un límite unilateral para una magnitud de un intervalo bilateral para una media firmada; interpretan el efecto de un cambio de ganancia y construyen un umbral de cero solo bajo hipótesis declaradas. En A, identifican dependencias, periodos mezclados y fuentes comunes de trazabilidad antes de aceptar un agregado.

El resultado de un indicador no es, por sí solo, una calificación de calibración. Las verificaciones de clientes describen el desempeño estadístico de los monitores en una población y periodo especificados. La incertidumbre de un certificado describe un resultado de calibración y sus fuentes bajo otro modelo. Una decisión sobre conformidad exige su tolerancia y regla de decisión; una alarma de seguimiento requiere límites de control; y un umbral de indicador pertenece al método que lo define. Si esos criterios parecen discrepar, no los sustituimos entre sí: definimos qué afirmación se quiere sostener y reunimos la evidencia estadística adecuada.

> **[TRANSICIÓN]** Con M12 completamos los indicadores agregados de precisión y sesgo. En el cierre del curso, volveremos a conectar las decisiones, el seguimiento y las evidencias de calibración sin confundir sus escalas.

## Referencias del capítulo

- **CFR58-A.** U.S. Environmental Protection Agency, *Code of Federal Regulations, Title 40, Part 58, Appendix A — Quality Assurance Requirements for Monitors used in Evaluations of National Ambient Air Quality Standards*, versión vigente al 20 de octubre de 2026. `docs/Appendix A to Part 58_ Title 40 (up to date as of 10-20-2026).pdf`. Numerales usados: §§2.3.1.2, 3.1.1, 4.1.1–4.1.3.2.
- **GUM.** JCGM 100:2008 (ISO/IEC Guide 98-3:2008), *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*. `docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf`. Numerales usados: §§4.2.2–4.2.3, 5.2.1–5.2.2 y G.3.2.
- **EN 14625.** BS EN 14625:2012, *Ambient air — Standard method for the measurement of the concentration of ozone by ultraviolet photometry*. `docs/BS EN 14625_2012.pdf`. Numerales usados: §3.12, §8.4.5, fórmula 5 y Tabla 1.
- **NIST/SEMATECH.** *e-Handbook of Statistical Methods*. National Institute of Standards and Technology / SEMATECH, recurso en línea (no disponible en `docs/`). Apartado 1.3.5.8, *Chi-Square Test for the Variance*, https://www.itl.nist.gov/div898/handbook/eda/section3/eda358.htm, consultado el 25 de octubre de 2026: límites de confianza de varianza y desviación estándar con chi-cuadrado. La afirmación general sobre dependencia temporal no se atribuye a NIST; las fórmulas de covarianza se respaldan con GUM 5.2.2. El intervalo t y las desviaciones muestrales se respaldan con GUM 4.2.2–4.2.3 y G.3.2.
