# M00. Estructura de los datos y cálculo reproducible

## Ficha del capítulo

| Elemento | Descripción |
|---|---|
| Competencia estadística | Organizar observaciones en una estructura de análisis que conserve el emparejamiento, el signo y los factores del diseño. |
| Prerrequisitos | Ninguno formal; se usan las convenciones de referencia `x`, indicación `y` y error `e = y − x` establecidas para el curso. [prop_e §3] |
| Nivel B | Tabla larga e identificadores; emparejamiento referencia–indicación; unidades; faltantes; lecturas negativas del cero; separación entre datos originales y calculados. [prop_e §5, M0] |
| Nivel I | Datos de varios días, analistas y campañas; conteos y agrupaciones; transformación de ancho a largo; registro de exclusiones justificadas. [prop_e §5, M0] |
| Nivel A | Especificación de entradas, salidas y comprobaciones de un cálculo reproducible; contraste entre dos herramientas. [prop_e §5, M0] |
| Datos de los ejemplos | Conjuntos breves **simulados para docencia**, generados en `calc/M00_ejemplos.py`. No son datos ni resultados de CALAIRE, del SRP 55 o del Level 2. |
| Anexos | No remite a AX.1–AX.13; aquí no se desarrollan deducciones. |
| Referencias clave | prop_e §§3 y 5 (M0); ISO/IEC 17025:2017 §§7.5.1–7.5.2 y 7.11.2, 7.11.6. |

## Nivel B — Conservar cada lectura y su pareja

En este nivel empezamos desde cero. Vamos a poner en forma los datos que después describiremos, modelaremos y usaremos para calcular. No vamos a limpiar una hoja para que se vea ordenada; vamos a conservar el significado de cada observación. La tabla debe permitir responder sin adivinar: qué se midió, con qué se comparó, en qué punto y ciclo, en qué día y con qué instrumento. Este cuidado es estadístico: si se pierde la identidad de la observación o su pareja, el cálculo posterior puede producir un número preciso pero responder a una pregunta equivocada.

> **[DIAPOSITIVA]** Una fila, una observación identificable. Las columnas identifican la observación, el diseño y los valores, con sus unidades.

La unidad de observación es lo que representa una fila. Para este capítulo, cada fila de lectura identifica una indicación asociada con un valor de referencia y con las condiciones que distinguen esa lectura de las demás. No confundan esa unidad con el nivel de concentración ni con el conjunto completo de una calibración. Si hay varias lecturas de un mismo nivel, son observaciones distintas; si se promedian después, ese promedio será otra variable calculada y no reemplazará las lecturas originales.

La forma larga expresa esa idea directamente: una fila por lectura. Las columnas guardan los identificadores y las magnitudes. Es una recomendación de organización para este análisis, no una exigencia universal de una hoja de cálculo ni un cambio al procedimiento del laboratorio. Lo importante es conservar el vínculo entre cada fila y su evento de medición. En una hoja ancha, una fila podría guardar muchas lecturas en columnas como `lectura_1`, `lectura_2` y `lectura_3`. Esa forma puede servir para capturar o presentar datos, pero complica la agrupación si cambia el número de lecturas o si luego hay que relacionarlas con otros factores. La tabla larga hace visibles las lecturas como registros. Así facilita contar, filtrar o reagrupar sin perder las claves.

En una tabla de trabajo del SRP, los identificadores que pide este módulo son nivel, lectura, ciclo, día e instrumento. Agreguen además un `id_pareja` único dentro del conjunto. No confíen en el número de fila como identidad: ordenar o filtrar la tabla cambia las posiciones. Tampoco usen solo el nombre del nivel: varias lecturas pueden compartirlo. La clave debe distinguir las parejas que, por diseño, no son intercambiables. El campo `lectura` conserva el número de lectura dentro del nivel; no es otro nombre para la clave.

> **[PIZARRA]** `id_pareja | nivel | lectura | ciclo | día | instrumento | x (nmol/mol) | y (nmol/mol) | e (nmol/mol)`

Miren la diferencia entre identificadores y magnitudes. `nivel`, `ciclo`, `día` e `instrumento` describen qué observación es y cómo se organizó el trabajo. `x` es el valor de referencia y `y` es la indicación. Para este curso, el error con signo se calcula como indicación menos valor de referencia: $e = y − x$. La GUM permite usar en la práctica un valor convencional de referencia cuando el valor verdadero es desconocido. [GUM B.2.19; prop_e §3, convención curricular]

> **[PREGUNTA AL GRUPO]** Si una referencia es 50,0 nmol/mol y la indicación emparejada es 50,4 nmol/mol, ¿qué error con signo escribimos? — *Respuesta esperada:* $e = 50{,}4 − 50{,}0 = 0{,}4$ nmol/mol; la indicación supera la referencia.

No intercambien el orden de la resta. El signo no es decoración: informa la dirección de la diferencia. Para un resultado de cero, una lectura negativa sigue siendo un valor observado. No la trunquen a cero ni la borren por parecer físicamente imposible como concentración de ozono. El registro representa una indicación ruidosa del sistema en esa condición, no la afirmación de que exista ozono con concentración física negativa. Aquí conservamos la lectura con su signo; la interpretación estadística se desarrolla en módulos posteriores. La convención `e = y − x` y el tratamiento de las lecturas negativas del cero pertenecen al alcance de M00. [prop_e §§3, 5, M0]

Una unidad acompaña a cada magnitud medida o calculada, no solo al encabezado de una presentación. En estos ejemplos expresaremos las concentraciones y los errores en nmol/mol; aquí ppb significa una fracción molar de una parte en mil millones. EN 14625 usa esa equivalencia en la nota de su tabla 2. [EN 14625 §8.2, tabla 2, nota] Si una columna guarda identificadores, no le asignen unidad física; si guarda referencia, indicación o diferencia, declaren la unidad en su nombre o en un diccionario de datos. Antes de comparar o restar valores, confirmen que `x` e `y` están expresados en la misma unidad y escala. Una etiqueta de columna como `valor` no basta: no dice si es referencia, indicación, error, concentración, fracción o resultado ya transformado.

### Escena B1. Identificar la pareja antes de restar

Ahora trabajemos una tabla pequeña, inventada para enseñar la estructura. Es **simulada**: no procede de una hoja de calibración ni representa resultados de CALAIRE. Partimos de una tabla de referencias y otra de indicaciones. Las relacionamos mediante un identificador de pareja, no por el orden de las filas. En la diapositiva ven ambas ya emparejadas. Luego calculo el error únicamente cuando existen los dos miembros de la pareja.

> **[DIAPOSITIVA]** Registros de cinco referencias y cuatro indicaciones; datos simulados.
>
> **[EJEMPLO]** Datos simulados; concentraciones en nmol/mol. Las filas de referencia y de indicación son originales del ejemplo. La columna `e` es calculada.

| `id_pareja` | Nivel | Referencia original `x` | Indicación original `y` | Error calculado `e = y − x` |
|---|---|---:|---:|---:|
| P01 | L0 | 0,0 | −0,2 | −0,2 |
| P02 | L1 | 50,0 | 50,4 | 0,4 |
| P03 | L1 | 50,0 | — faltante — | no calculable |
| P04 | L2 | 100,0 | 100,8 | 0,8 |
| P05 | L3 | 150,0 | 150,7 | 0,7 |

Los números de esta tabla los reproduce `calc/M00_ejemplos.py`. En el ejemplo hay cinco referencias originales y cuatro indicaciones originales. Al hacer el emparejamiento por clave, quedan cuatro parejas completas y una referencia sin indicación asociada. Por eso reporto un faltante y no invento la lectura de P03. Tampoco desplazo las indicaciones posteriores para rellenar el hueco.

Veamos el error calculado de P04 en voz alta. La referencia es 100,0 nmol/mol; la indicación es 100,8 nmol/mol. Restamos la referencia a la indicación: cien coma ocho menos cien coma cero es 0,8 nmol/mol. Para P01, la referencia del cero es 0,0 y la indicación observada es −0,2; el error queda en −0,2 nmol/mol. Ese valor no se convierte en cero. La tabla distingue el dato original `y` de la columna derivada `e`, y permite reconstruir cómo se obtuvo el error.

> **[ERROR CRÍTICO]** No emparejen por la posición de las filas ni por la apariencia de que dos cifras están una al lado de la otra. Si falta una lectura y se desplazan las demás, la referencia de P03 podría asociarse por error con la indicación de P04. En este ejemplo fabricado, esa resta equivocada daría 50,8 nmol/mol, aunque no existe una indicación P03 que permita calcular su error. Ese valor espurio no es un error grande observado; es una pareja mal construida. La clave evita atribuirlo a una medición. [prop_e §8]

El resultado del ejemplo también muestra el efecto de incluir solo parejas completas cuando resumimos este pequeño conjunto: la media aritmética de los cuatro errores disponibles es 0,425 nmol/mol. [prop_e §5, M0; cálculo reproducible en `calc/M00_ejemplos.py`] Esta cifra es únicamente una ilustración de trazabilidad entre datos y cálculo; no es una estimación del desempeño de ningún fotómetro. Que sepamos calcular una media no significa que debamos borrar la fila incompleta ni que podamos ocultar cuántos datos faltaron. El resumen debe conservar ese contexto.

Cuando `x` o `y` no está disponible, representen explícitamente el faltante con la convención del sistema de datos. En una hoja puede verse como celda vacía; en un archivo tabular puede aparecer como un valor nulo. No lo conviertan a cero, porque cero es una observación posible y tiene significado distinto. No calculen `e` como si el valor faltante fuera cero. La indicación ausente de P03 no permite conocer su error. Mantengan una razón o estado de faltante si se conoce; no supongan la causa cuando no se haya investigado.

> **[PIZARRA]** Regla de emparejamiento: buscar por identificador; comprobar que cada clave esperada tiene la referencia y la indicación correspondientes; calcular `e` solo para parejas completas.

La clave única debe conectar la indicación con su referencia correcta y con la descripción del diseño. En la tabla docente usamos `P01` a `P05` como identificadores de pareja. En un registro de trabajo, la identidad también debe poder vincularse al nivel, lectura, ciclo, día e instrumento, tal como pide M00. No interpreten los nombres `L0`, `L1`, `L2`, `L3` como magnitudes: son etiquetas. Las magnitudes son `x` y `y`, con unidades declaradas.

Fíjense en que P02 y P03 tienen la misma referencia y el mismo nivel, pero son parejas distintas. Eso es intencional: repetir una referencia no convierte dos indicaciones en una sola observación, ni hace que el valor de referencia sea una clave única. La identificación del nivel indica el punto que se está midiendo; la identificación de lectura distingue el evento dentro de ese nivel. Si se usara únicamente `x` para unir dos tablas, las filas repetidas podrían multiplicarse al relacionarlas o quedar emparejadas de manera ambigua. La clave describe el vínculo correcto, y los identificadores de nivel y lectura preservan el contexto de cada registro.

En términos sencillos, antes de unir dos tablas preguntamos qué representa cada fila y cuántas filas de un lado pueden corresponder a cada fila del otro. En nuestro ejemplo, la referencia de nivel L1 aparece asociada con dos parejas de lectura. No asumimos que las indicaciones sean idénticas ni que se puedan intercambiar; relacionamos cada valor mediante su identificador de pareja. Esta verificación sencilla evita que una operación de unión duplique filas o asocie una indicación con una referencia que comparte el mismo valor numérico, pero no el mismo evento de medición.

### Escena B2. Dato original, valor calculado y corrección trazable

Hay otra separación esencial: lo que se observó originalmente no es lo mismo que lo que calculamos a partir de la observación. `x` y `y` son entradas del ejemplo. `e` se deriva mediante una operación declarada. Si alguien corrige una etiqueta de pareja, una unidad mal transcrita o una identificación de día, no debe borrar silenciosamente el registro inicial. La estructura debe dejar claro cuál fue la observación original y qué campo se cambió. También registra por qué, cuándo y quién hizo el cambio, según el sistema de registros del laboratorio.

La ISO/IEC 17025 establece que los registros técnicos deben conservar información suficiente para facilitar la identificación de factores que afectan el resultado y permitir repetir la actividad en condiciones tan cercanas como sea posible; pide que las observaciones originales, los datos y los cálculos se registren cuando se producen y se identifiquen con la tarea. También indica que las enmiendas deben poder rastrearse a versiones previas u observaciones originales y que se retengan tanto los datos originales como los enmendados, con la fecha, el aspecto modificado y la persona responsable. [ISO 17025 §7.5.1–7.5.2] En nuestra tabla didáctica la columna calculada no reemplaza ni la referencia ni la indicación. En el registro operativo, una rectificación debe seguir el procedimiento aprobado por el laboratorio.

> **[DIAPOSITIVA]** Tres capas: (1) datos originales; (2) transformaciones declaradas; (3) resultados derivados. Una corrección no destruye la capa anterior.

Veamos qué quiere decir en la práctica de registro, sin convertirlo en una tarea de clase. Supongamos que durante la revisión se descubre que una indicación cargada con clave P03 pertenecía en realidad a otra clave, o que se detectó que una fila se importó con la unidad incorrecta. La acción no consiste en editar la cifra hasta que el cálculo parezca razonable. Primero se preserva lo recibido; se identifica el campo afectado; se registra el cambio y su justificación; y se recalculan las salidas desde la versión autorizada. Si no se sabe cuál era la pareja correcta, el valor se mantiene sin asignación o se marca para revisión, en vez de completarlo por intuición.

> **[ERROR CRÍTICO]** No eliminen una fila, sustituyan una lectura negativa por cero ni sobrescriban el dato de origen para conseguir un resultado esperado. La modificación debe ser visible y rastreable; si no hay base documentada para corregir una clave, detengan el cálculo que depende de ella. [ISO 17025 §7.5.2; prop_e §8]

La reproducibilidad empieza por guardar qué datos recibió el cálculo y cómo los trató. No exigimos construir un software en este nivel. Sí necesitamos distinguir la lectura transcrita, la lectura asociada con su referencia, el error calculado y el caso incompleto. La columna de resultado no es una caja negra: la operación se escribe con su convención y sus unidades. Si ejecutamos la misma operación sobre las mismas entradas y con la misma regla, debemos reconstruir la misma salida, dentro de la precisión informada. Si eso no ocurre, revisamos qué entrada, asociación o transformación cambió. No reemplazamos la observación original por el resultado más reciente.

> **[PREGUNTA AL GRUPO]** Si las referencias se conservan en cinco filas y solo hay cuatro indicaciones, ¿qué hacemos con la quinta referencia? — *Respuesta esperada:* la mantenemos, señalamos que falta su indicación y no calculamos el error de esa pareja hasta tener un dato válido y correctamente identificado.

> **[PRÁCTICA — fase de ejercicios]** Organizar un conjunto corto del Level 2, calcular $e=y-x$, detectar una pareja desplazada y un faltante, y documentar la corrección sin borrar el original.

### Señales de escalamiento

Antes de continuar un procedimiento básico, paren y consulten cuando la dependencia entre observaciones no esté contemplada en la plantilla; cuando el comportamiento sugiera un cambio de escala; cuando aparezca un valor inusual sin causa documentada; o cuando los residuos muestren estructura en lugar de fluctuar sin patrón alrededor del modelo. También se escala si la incertidumbre de la referencia y de la indicación es relevante en ambos ejes, si hay pocos grados de libertad para justificar el cálculo previsto o si el resultado queda próximo a un límite que pueda cambiar la decisión. Estas son señales para detenerse y pedir apoyo, no una invitación a corregir el archivo por cuenta propia. [prop_e §2]

En M00, una pareja no identificable o un faltante que altera la correspondencia también impide seguir con el cálculo dependiente de esa fila. No se “resuelve” el problema copiando la lectura vecina. Si la estructura de la tabla no permite verificar nivel, lectura, ciclo, día e instrumento, se detiene el proceso hasta aclarar la clave y el origen del registro. Así protegemos el signo y la identidad de las observaciones antes de pasar a su descripción.

## Nivel I — Lo que se añade al registro de una lectura

Ustedes ya conocen la tabla larga, el emparejamiento, las unidades, los faltantes y la diferencia entre observación y cálculo. En el nivel intermedio añadimos la estructura que aparece cuando el trabajo se reparte entre días, analistas y campañas. La pregunta ya no es solo “¿qué lectura es esta?”, sino también “¿a qué grupo pertenece y qué registros deben existir para que el resumen responda a la pregunta?”. Las etiquetas de agrupación no son adornos: permiten reconstruir las condiciones en las que se generaron las observaciones. [prop_e §5, M0]

### Escena I1. Conservar los factores al agrupar

Una campaña no es simplemente una pila de números. Cada observación mantiene su identidad y se relaciona con su analista, día, ciclo, nivel e instrumento. Si trabajamos con varias campañas, la campaña también forma parte de la descripción. No reemplazamos los campos anteriores por un nombre general como “resultado”. Cada variable responde a una pregunta: quién ejecutó la medición, cuándo, en qué campaña, con qué ciclo y a qué nivel.

> **[PIZARRA]** Una fila por observación; claves persistentes para `campaña`, `analista`, `día`, `ciclo`, `nivel`, `lectura` e `instrumento`; columnas separadas para referencia, indicación, error, unidad y estado del dato.

Voy a mostrar un ejemplo **simulado**, deliberadamente pequeño. Tiene dos campañas; cada una contiene dos analistas; para cada combinación hay dos días; y en cada día se registran dos ciclos. Cada fila representa un ciclo observado. El script `calc/M00_ejemplos.py` genera los registros y calcula sus conteos. Como el ejemplo está construido de forma balanceada, contiene dieciséis filas: ocho por campaña y ocho por analista. En cada combinación campaña por analista hay cuatro filas. Para cada combinación de analista por día hay también cuatro filas, porque el registro recorre las dos campañas y dos ciclos.

> **[EJEMPLO]** Tabla de conteos de datos simulados; no son jornadas, analistas ni resultados de CALAIRE.
>
> | Comprobación | Conteo del ejemplo |
> |---|---:|
> | Registros totales | 16 |
> | Registros por campaña C1 / C2 | 8 / 8 |
> | Registros por analista A1 / A2 | 8 / 8 |
> | Registros por cada combinación campaña × analista | 4 |
> | Registros por cada combinación analista × día | 4 |

No memoricen estos conteos como un diseño real del Level 2. Son una demostración de una comprobación, y sus valores salen de los factores que declaré. En una campaña real, el número de lecturas puede ser distinto; lo que hacemos es calcular los conteos esperados a partir del diseño documentado y compararlos con las filas observadas. Si el diseño dice que deben existir determinadas combinaciones, la tabla debe dejar ver qué combinaciones están presentes, cuáles faltan y si hay filas duplicadas. Un total global correcto no garantiza grupos correctos: una fila de más en un grupo y una de menos en otro podrían compensarse al mirar solo el total.

> **[PREGUNTA AL GRUPO]** Si el total coincide con el esperado, ¿podemos concluir por eso que cada día y analista tiene el número de registros previsto? — *Respuesta esperada:* no; hay que revisar los conteos dentro de cada combinación de factores, no solo el total.

La comprobación de conteos no es un análisis de variabilidad. Es un control estructural: verifica que el conjunto que se va a analizar corresponde al diseño que se declara. Si se quiere reconstruir un resumen diario, cada lectura necesita un día identificable y su pareja correcta. Si un ciclo tiene identificador duplicado o una lectura está asociada al día incorrecto, el agrupamiento puede incluirla en un resumen que no le corresponde. No arreglamos esa inconsistencia sumando o promediando; primero se investiga el origen y se documenta la decisión.

> **[ERROR CRÍTICO]** No supongan que dos días con la misma etiqueta pertenecen a la misma unidad de calendario o campaña si las claves no lo establecen. Tampoco traten como independientes filas que pertenecen a una misma agrupación solo porque aparecen en filas separadas. La dependencia estadística se estudia después; aquí preservamos la estructura que permite reconocerla. [prop_e §8]

Cuando un dato se excluye de un cálculo, el conjunto de trabajo debe conservarlo y dejar constancia del motivo, de la regla aplicada y de la salida afectada. «Se quitó porque se veía raro» no basta. La exclusión es una decisión sobre el análisis, no una desaparición del registro. Su justificación debe ser revisable y coherente con el objetivo y el método.

La norma exige trazabilidad de las enmiendas a los registros técnicos (§7.5.2). Una exclusión analítica no es una enmienda. Aquí la registramos con el mismo criterio de trazabilidad, como convención del curso y no como exigencia específica de la norma. Conservamos el original y anotamos qué se excluyó y por qué. [ISO 17025 §7.5.2; prop_e §5, M0]

Al documentar la decisión, distinguimos un dato que nunca estuvo disponible de otro que sí se observó, pero no entró en una salida particular. Se debe poder seguir desde el identificador de la observación hasta el cálculo donde se incluyó o excluyó, y hasta la justificación registrada. La fila original permanece en el archivo fuente. El conjunto derivado puede marcar su estado si la regla de selección es visible. Si luego cambia la decisión, el historial muestra las versiones anterior y nueva. Así no presentamos la última tabla como si siempre hubiera sido igual. La exclusión tampoco corrige el resto de la estructura: seguimos comprobando que las filas estén emparejadas y agrupadas correctamente.

> **[DIAPOSITIVA]** Para reconstruir un resumen de grupo: conservar claves originales → verificar parejas → contar filas por cada factor y combinación pertinente → identificar faltantes o duplicados → resumir solo con una regla documentada.

Esa secuencia importa porque el resumen diario depende de dos cosas que no se deben confundir: la pertenencia de cada fila al día y la regla estadística con la que después se calcula el resumen. M00 nos enseña a dejar disponible la primera; los módulos posteriores enseñan a elegir y evaluar la segunda. Si los conteos son inesperados, no interpreten el resumen como si el diseño estuviera completo. Primero aclaren si hay dato faltante, duplicado, exclusión documentada o una descripción incompleta del diseño.

### Escena I2. De ancho a largo, sin inventar observaciones

Es posible que reciban una tabla ancha, por ejemplo una fila por grupo con columnas para distintas lecturas. Pasar de ancho a largo significa reorganizar esas columnas en filas, de manera que cada observación ocupe su propio registro, mientras se repiten en cada fila los identificadores del grupo que le corresponden. La transformación no crea nuevas mediciones: preserva los valores originales y los enlaces entre cada valor y sus factores.

> **[PIZARRA]** Antes: `campaña | analista | día | ciclo_1 | ciclo_2`.
>
> Después: `campaña | analista | día | ciclo | y (nmol/mol)`. El índice `lectura` se conserva como identificador cuando el diseño contiene varias lecturas por ciclo.

En la tabla ancha, `ciclo_1` y `ciclo_2` están representados en dos columnas. En la tabla larga, `ciclo` identifica a qué ciclo pertenece la fila y `y` contiene la indicación que ocupaba la celda. No reutilizamos `lectura`, que antes definimos como índice, para nombrar una concentración. Al transformar, trasladamos las claves del grupo a cada registro nuevo, y dejamos cada observación con su identificador. Si una celda está vacía, no la convertimos en lectura cero. Registramos que no hay valor y preservamos, cuando se conoce, el estado o la razón. Si hay una columna de referencia emparejada con cada indicación, conservamos esa pareja; no reordenamos por magnitud.

La validación compara el número de valores originales no faltantes con el número de registros resultantes. También verifica las claves de grupo, busca duplicados, comprueba las unidades y confirma que los faltantes sigan siendo faltantes. Una tabla larga sin las etiquetas de campaña, analista y día no es correcta para este propósito: los valores pueden haber sobrevivido, pero se perdió parte de su diseño.

> **[EJEMPLO]** Datos simulados. En la tabla ancha, las dos lecturas representan los ciclos 1 y 2; las concentraciones están en nmol/mol.
>
> | Campaña | Analista | Día | Ciclo 1 | Ciclo 2 |
> |---|---|---:|---:|---:|
> | C1 | A1 | 1 | 10,0 | 11,0 |
> | C1 | A2 | 1 | 12,0 | faltante |
>
> Al pasar a largo obtenemos tres registros: campaña C1, analista A1, día 1, ciclo 1, lectura 10,0; campaña C1, analista A1, día 1, ciclo 2, lectura 11,0; y campaña C1, analista A2, día 1, ciclo 1, lectura 12,0 nmol/mol. La celda faltante no se convierte en observación. La comprobación es «tres valores no faltantes igual a tres registros largos». El script `calc/M00_ejemplos.py` reproduce este conteo y las filas transformadas.

> **[PREGUNTA AL GRUPO]** Si una fila de la tabla ancha tiene vacía la celda del segundo ciclo, ¿qué aparece en la tabla larga? — *Respuesta esperada:* no aparece una observación ficticia con valor cero; queda ausente o se representa con el estado faltante acordado, y se conserva el registro de esa condición si el sistema lo permite.

Las tablas resumen también se pueden convertir de nuevo a datos largos para comunicar resultados, pero no confundan una fila resumen con una observación original. Un promedio por día no reemplaza las lecturas que lo formaron. Si el objetivo requiere reconstruirlo, se parte de las parejas originales y de la agrupación documentada, no de una hoja de promedios que ya perdió los valores individuales.

> **[ERROR CRÍTICO]** No agreguen filas para “completar” el conteo ni dupliquen un valor existente para sustituir una lectura faltante. Un conteo que no coincide es una señal que se investiga, no una instrucción para fabricar datos. Una exclusión se registra con su razón; un faltante no se rellena sin un método explícito autorizado para ese fin. [ISO 17025 §7.5.1–7.5.2; prop_e §8]

> **[TRANSICIÓN]** Ya podemos describir los grupos de manera rastreable. En la práctica del nivel intermedio reconstruiremos los resúmenes diarios a partir de las parejas originales.

> **[PRÁCTICA — fase de ejercicios]** Reconstruir los resúmenes diarios de una campaña desde las parejas originales

### Señales de escalamiento

Escalen si no se puede reconstruir qué filas pertenecen a cada día, analista o campaña; si los conteos por grupo contradicen el diseño y la diferencia no está explicada; si la conversión de ancho a largo altera el número de observaciones o deja claves sin resolver; o si una exclusión carece de criterio y justificación documentados. No sigan a un resumen diario o a otra salida que dependa de esas filas hasta aclarar la estructura. La persona responsable del método debe decidir cómo tratar un dato no conforme; quien prepara la tabla no debe ocultar el problema con una transformación.

## Nivel A — Especificar y contrastar el cálculo

Ustedes ya conocen cómo mantener las claves, comprobar las agrupaciones y conservar el dato original. En el nivel avanzado vamos a describir un cálculo reproducible como un contrato que cualquiera pueda revisar. No basta con guardar un archivo con resultados. Debe quedar definido qué entra, qué sale, qué relación entre filas se aplica, qué comprobaciones se ejecutan y con qué implementación se puede contrastar el resultado. El objetivo estadístico de M00 sigue siendo conservar emparejamiento, signo y factores del diseño; la automatización no compensa una estructura equivocada. [prop_e §5, M0]

### Escena A1. El contrato de entradas, salidas y comprobaciones

Primero describimos las entradas. Indicamos el archivo o conjunto de datos, su versión o identificador, las columnas usadas, su significado y sus unidades. Identificamos las claves que definen cada observación y la pareja referencia–indicación. Declaramos las reglas para valores ausentes y exclusiones. Especificamos el sentido de la resta, `e = y − x`, y la representación de las concentraciones. Si el cálculo agrupa por día, analista o campaña, decimos qué campos definen cada grupo. Esa descripción tiene que bastar para que otra persona use exactamente las mismas entradas y entienda qué filas quedan fuera de una operación.

Después describimos las salidas. Por ejemplo, el resultado puede ser una columna de errores por pareja y una tabla con conteos por grupo. Cada salida se nombra, lleva unidad cuando corresponda y queda asociada a su entrada. Si hay parejas incompletas, declaramos si la salida conserva el faltante, lo informa en un estado separado o detiene la operación; no dejamos que cada programa decida silenciosamente. El resultado no puede presentarse sin indicar qué versión de los datos y qué reglas lo produjeron.

> **[PIZARRA]** Contrato mínimo: entrada identificada + esquema y unidades + claves + regla de cálculo + política de faltantes/exclusiones → salidas nombradas + controles + registro de ejecución.

Las comprobaciones son parte de la especificación, no una revisión informal al final. Confirmamos que las claves de observación no estén duplicadas según el diseño; que las referencias y las indicaciones se emparejen con las claves esperadas; que el número de parejas completas y de faltantes sea visible; y que los conteos por factor y grupo concuerden con el diseño declarado. Confirmamos también que las magnitudes que vamos a restar tengan unidades y escalas compatibles, que la fórmula respete el signo definido y que una observación negativa del cero siga conservada. Si el cálculo se transfiere entre archivos o programas, comprobamos que la transferencia no cambió claves, unidades, valores ni estados faltantes.

La ISO/IEC 17025 exige que los sistemas de gestión de información usados para recopilar, procesar, registrar, informar, almacenar o recuperar datos se validen para su funcionalidad antes de introducirlos, y que los cambios sean autorizados, documentados y validados antes de aplicarse. También establece que los cálculos y las transferencias de datos se comprueben de manera apropiada y sistemática. [ISO 17025 §7.11.2, §7.11.6] En el curso lo traducimos a una regla práctica: cada cálculo que sostenga un resultado debe tener entradas identificables, una transformación explícita y verificaciones suficientes para detectar una pareja cambiada, una unidad incompatible o una salida inesperada.

> **[DIAPOSITIVA]** Traza de ejecución: identificación de entrada → parámetros y reglas → comprobaciones de estructura → cálculo → comprobaciones de salida → herramienta/versión → fecha y responsable.

Cuando el cálculo depende de un entorno informático, registramos además la herramienta y la versión con que se ejecutó, las dependencias que puedan afectar el resultado y la configuración de lectura de archivos que sea relevante, como separador decimal, codificación o interpretación de valores vacíos. No hace falta copiar indiscriminadamente toda la configuración de un equipo; se documenta aquello que permite reconstruir la ejecución y entender una discrepancia. Se conservan la especificación y el resultado de las comprobaciones junto con la identificación de los datos, de modo que la revisión no dependa de que otra persona adivine qué opciones se usaron.

La especificación también diferencia resultado de cálculo y resultado de medición. Un programa puede evaluar correctamente una fórmula sobre las filas recibidas, pero si esas filas tienen parejas equivocadas el número no representa el mensurando previsto. Por eso el primer control es estructural. El segundo es aritmético: comprobar que la operación implementada corresponde a la definición. El tercero es de salida: verificar que el formato, unidad y agrupación sean los declarados. No sustituimos uno por otro.

### Escena A2. Contrastar dos herramientas sin confundir redondeo con discrepancia

Ahora comparo una implementación breve en Python con una hoja de cálculo que LibreOffice Calc recalcula. Los datos son **simulados** y se han escogido solo para verificar el signo y la operación. Para tres parejas completas, las referencias son 50,0; 100,0 y 150,0 nmol/mol; las indicaciones son 50,4; 100,8 y 150,7 nmol/mol. En Python se calcula, para cada fila, la indicación menos la referencia. En Calc, la fórmula de la primera fila es `=C2-B2` —se lee «igual a C dos menos B dos»—, con `B` como referencia y `C` como indicación. Se copia siguiendo las filas que corresponden a parejas válidas. El script `calc/M00_ejemplos.py` genera el libro temporal, pide a Calc que lo recalcule y lee sus salidas, además de producir el resultado en Python.

> **[EJEMPLO]** Salidas de las dos herramientas, redondeadas aquí a tres decimales: Python `[0,4; 0,8; 0,7]` nmol/mol; LibreOffice Calc `[0,4; 0,8; 0,7]` nmol/mol. El acuerdo se cumple con una tolerancia de $10^{-12}$ nmol/mol, que se lee «diez elevado a menos doce nanomoles por mol». La mayor diferencia antes del redondeo es $4{,}441\times10^{-16}$ nmol/mol, que se lee «cuatro coma cuatrocientos cuarenta y uno por diez elevado a menos dieciséis nanomoles por mol». [cálculo reproducible en `calc/M00_ejemplos.py`]

No exigiríamos igualdad binaria exacta entre las salidas en coma flotante. El script muestra que las representaciones internas de Python y Calc no son idénticas en todos los decimales, aunque el desacuerdo máximo calculado sea mucho menor que la tolerancia que fijamos para esta prueba docente. La tolerancia del ejemplo es una decisión numérica de la comparación de software; no es un límite de aceptación de una calibración ni un criterio general del laboratorio. En un cálculo real, quien valida la herramienta debe justificar la tolerancia de acuerdo con el propósito, las unidades, el redondeo y la resolución necesaria.

> **[PREGUNTA AL GRUPO]** Si las dos herramientas no tienen idénticos todos sus bits, ¿eso demuestra por sí solo que una está equivocada? — *Respuesta esperada:* no; hay que comparar la diferencia con una tolerancia definida previamente, revisar la fórmula, las entradas, unidades y redondeo, y confirmar que ambas usan las mismas parejas.

El contraste sirve solo si las dos herramientas reciben la misma entrada interpretada de la misma forma. Una hoja puede tratar una celda vacía, una coma decimal o un número almacenado como texto de manera distinta del programa. Por eso guardamos una copia o identificación inequívoca de las entradas y mostramos qué regla se usó para emparejar y manejar los faltantes. También revisamos las fórmulas de las celdas, en lugar de asumir que el contenido visible es la operación correcta. Una segunda herramienta ayuda a descubrir errores de implementación; no valida automáticamente la definición del resultado ni el diseño de datos.

> **[ERROR CRÍTICO]** No declares reproducible un cálculo solo porque dos pantallas muestran cifras parecidas. Si las herramientas se alimentaron con filas distintas, tuvieron claves desplazadas, interpretaron unidades diferentes o aplicaron políticas distintas a los faltantes, la comparación no verifica el mismo cálculo. Y si la diferencia se redondea a cero, eso no prueba igualdad matemática exacta: se informa con la tolerancia acordada y se conserva suficiente precisión para evaluarla. [prop_e §8]

La misma disciplina aplica a cambios de código o de plantilla. Si se cambia una fórmula, una columna de entrada, una versión del programa o la forma de manejar celdas vacías, se repiten las pruebas que correspondan y se documenta qué cambió y qué resultados se comprobaron. La norma se refiere a validar cambios en sistemas de información antes de implementarlos y a comprobar cálculos y transferencias. [ISO 17025 §7.11.2, §7.11.6] Esta cita no convierte este ejemplo simulado en una validación del sistema informático del laboratorio; solo fundamenta por qué las verificaciones deben formar parte del sistema de trabajo.

> **[TRANSICIÓN]** La tabla preserva quién, cuándo y qué se comparó; el contrato del cálculo deja explícitas las entradas, las salidas y las pruebas. Ahora practicaremos el contraste con una segunda herramienta y explicaremos sus discrepancias.

> **[PRÁCTICA — fase de ejercicios]** Reproducir un resultado con una segunda herramienta y explicar las discrepancias

### Señales de escalamiento

Detengan y escalen si una de las herramientas modifica o pierde claves, unidades o faltantes; si no coinciden los datos de entrada o las reglas de emparejamiento; si la diferencia entre implementaciones supera la tolerancia que se definió para la comparación; si no se puede reconstruir una salida desde sus entradas; o si una conversión de archivo o cambio de versión altera el resultado sin explicación. No ajusten la tolerancia después de ver la discrepancia solo para declarar acuerdo. La comparación debe dejar evidencia de qué se revisó y de cuál decisión queda pendiente.

## Cierre del capítulo

En el nivel B organizamos cada observación con sus identificadores, emparejamos referencia e indicación mediante claves, declaramos unidades, conservamos los faltantes y mantenemos las lecturas negativas del cero con su signo. Separamos el dato original del error calculado y no sustituimos una observación por un valor inventado.

En el nivel I añadimos los factores que agrupan las observaciones en días, analistas y campañas. Comprobamos conteos en cada grupo y combinación pertinente, transformamos tablas anchas a largas sin perder claves y dejamos trazabilidad de las exclusiones justificadas. Un resumen se reconstruye desde las parejas originales, no desde filas que ya perdieron su identidad.

En el nivel A expresamos el cálculo como un contrato de entradas, salidas y comprobaciones. Contrastamos dos herramientas sobre los mismos datos y reglas. También distinguimos una diferencia numérica de una discrepancia que excede la tolerancia establecida. Estos hábitos preparan el siguiente módulo, M1, donde expresaremos el resultado como función de sus entradas. Después, en M2, describiremos la respuesta y elegiremos su resumen. Así podremos analizarla sin perder la estructura de las observaciones.

## Referencias del capítulo

- **prop_e.** *Propuesta E: curso de estadística aplicada a la fotometría de ozono*, 24 de octubre de 2026, §§2–3 y §5, M0. Archivo: `prop_e.md`.
- **ISO 17025.** BS EN ISO/IEC 17025:2017, *General requirements for the competence of testing and calibration laboratories*. Cláusulas 7.5.1–7.5.2 y 7.11.2, 7.11.6. Archivo: `docs/BS EN ISO_IEC 17025_2017.pdf`.
- **GUM.** JCGM 100:2008, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*, B.2.19. Archivo: `docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf`.
- **EN 14625.** BS EN 14625:2012, *Ambient air — Standard method for the measurement of the concentration of ozone by ultraviolet photometry*, §8.2, tabla 2, nota. Archivo: `docs/BS EN 14625_2012.pdf`.
- **Cálculos ilustrativos.** Conjunto simulado y script de reproducción: `curso/S1_fundamentos/calc/M00_ejemplos.py`.
