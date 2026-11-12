# M05 — revisión de prácticas (haiku)

Revisor: Claude Haiku 5.5. Alcance: bloques `[PRÁCTICA]` B, I y A de `curso/S2_modelos_calibracion/M05_libreto.md` (B: líneas 96–107; I: 178–200; A: 267–278), `curso/S2_modelos_calibracion/calc/M05_practicas_luna.py` y la bitácora `curso/S2_modelos_calibracion/M05_practicas_luna.md`. No se editaron libretos ni scripts. No se auditaron referencias.

Nota de ubicación: la bitácora pedida como `curso/logs/M05_practicas_luna.md` no existe. La bitácora real está en `curso/S2_modelos_calibracion/M05_practicas_luna.md`. Se revisó esa. Ver H-10.

## Verificaciones ejecutadas

- `curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M05_practicas_luna.py` termina con código 0. Reproduce: 576 = 480 + 96; plan A base 3/12/24/192 y gl 2, 9, 12, 168; variante de seis analistas 6/24/48/384 con gl 5; efectos marginales F = 0,80, C = 0,20, T = −0,10 nmol/mol; F con C bajo 0,50 y con C alto 1,10; orden de 16 corridas con semilla 20261027.
- `curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M05_diseno.py` termina con código 0. Reproduce: medias 0,40 y 0,20/0,80 (diferencia 0,60); efectos F 0,800, C 0,200, T −0,100, FC 0,300, FT 0,040, CT −0,020, FCT 0,080; u(ē) = 0,083 / 0,082 / 0,059 nmol/mol; potencia 0,4951 (d = 6, n = 8), 0,5009 (d = 6, n = 16), 0,8733 (d = 12, n = 8); estratos 2, 9, 12, 168.
- Tabla I (ocho filas) recalculada a mano con la regla `e = 0,20 + 0,40F + 0,10C − 0,05T + 0,15FC + 0,02FT − 0,01CT + 0,04FCT`: coincide fila a fila con la tabla del libreto.
- Contraste simple de F con C alto y T alto: 0,85 − (−0,37) = 1,22 nmol/mol, correcto a mano.
- Fuente B (`docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm`, hoja `Fotometro`, celda E17): la nota dice «10 puntos de concentración, 2 puntos de cero, 8 repeticiones por punto», igual que el libreto. Las hojas `Dia1`–`Dia6` muestran dos puntos de cero, uno al inicio (punto 0) y otro al final (punto 11), y seis días de calibración, con `Dia0` como preparación. Esto confirma las afirmaciones de B. Hay discrepancia de datos, ver H-09.
- Diff de `M05_libreto.md` frente a HEAD: 44 líneas añadidas y 3 eliminadas, todas dentro de los tres marcadores de práctica. No hay cambios en otros capítulos, referencias ni citas.
- Coma decimal y unidades: no hay punto decimal en los bloques nuevos. Todas las magnitudes llevan nmol/mol.
- Etiquetado de datos: B = propio (solo descripción de diseño); I y A = simulados y rotulados como didácticos, sin atribución a CALAIRE. Correcto.
- Anexo `AX.4` existe y deduce `u²_prec = τ²/d + σ²/(dn)`, que es la base de la fórmula citada en I3.
- Potencia, incertidumbre y denominadores de A: fórmulas correctas bajo los supuestos declarados (t de un día medio con d − 1 gl; denominador de analista = día dentro de analista; día = ciclo dentro de día; ciclo = lectura dentro de ciclo).

## Hallazgos

### H-01 — Severidad alta — número inexistente en la solución de I

- **Ubicación:** `M05_libreto.md` L195, solución docente del bloque I: «El máximo valor de la tabla, 1,23, no sustituye el contraste definido».
- **Problema:** el valor máximo de la tabla es 0,85 nmol/mol. El valor 1,23 no aparece en la tabla ni en ningún cálculo. El rango entre filas es 0,85 − (−0,37) = 1,22, que es el contraste de la solución misma.
- **Escenario:** el participante busca 1,23 en la tabla, no lo encuentra y pierde confianza en toda la solución.
- **Corrección propuesta:** eliminar la frase o sustituirla por «el mayor contraste entre dos filas de la tabla es 1,22 nmol/mol (0,85 − (−0,37)), y coincide con el contraste simple de la solución».

### H-02 — Severidad alta — las ocho filas no son corridas independientes y la regla no tiene error

- **Ubicación:** enunciado del bloque I, L180: «para cada combinación, e = …. Cada fila es una corrida independiente simulada»; tabla de tratamientos L184–191; tarea de réplicas L182.
- **Problema:** la regla es determinista. Cada combinación produce un único valor, así que las dos réplicas independientes por combinación tendrían el mismo valor y la variación entre corridas es nula. La tabla tiene ocho filas, no dieciséis, y la frase «cada fila es una corrida independiente» contradice la tabla. La solución habla de «dos corridas independientes» y de que una corrida por combinación no estima variación entre corridas, pero con esta regla no hay variación que estimar.
- **Escenario:** un participante que genera dos réplicas con la regla obtiene valores idénticos y no puede interpretar la variación entre corridas, aunque el enunciado le pide especificar réplicas independientes.
- **Corrección propuesta:** decidir y declarar una de dos opciones. (a) La tabla es el valor esperado por combinación; cada combinación tiene dos réplicas con el mismo valor, y se escribe «la tabla da la respuesta esperada por tratamiento; no hay error de corrida en esta regla». (b) Añadir un término de error reproducible con semilla declarada y una tabla de dieciséis corridas. En ambos casos cambiar «cada fila es una corrida independiente» por una frase exacta.

### H-03 — Severidad media — criterio de escalamiento ambiguo en I

- **Ubicación:** enunciado del bloque I, L180: «detenerse y escalar si cualquier cambio absoluto de respuesta entre niveles supera 0,50 nmol/mol»; solución, L195: «el contraste simple de F … 1,22 … se escala».
- **Problema:** el criterio dice «cualquier cambio entre niveles». El efecto principal de F (0,80 nmol/mol, L195 y script) también supera 0,50, y el enunciado no dice si el criterio se aplica a efectos principales, a contrastes simples o a pares de filas. La solución solo lo aplica al contraste simple y no menciona que el efecto principal de F ya lo activa.
- **Escenario:** un participante aplica el criterio al efecto principal de F, obtiene 0,80 > 0,50 y se pregunta por qué la solución no lo menciona. O bien aplica el criterio solo a pares de filas y llega a una conclusión distinta.
- **Corrección propuesta:** definir el conjunto sobre el que se aplica el umbral, por ejemplo «cualquier efecto principal o contraste simple de F, C o T», y en la solución decir que F supera el umbral como efecto principal (0,80) y como contraste condicional (1,22).

### H-04 — Severidad media — convención de interacción inconsistente

- **Ubicación:** `M05_libreto.md` L144 (I2): «La interacción flujo × acondicionamiento tiene contraste 0,30 nmol/mol»; L195 (práctica I): «su diferencia, 0,60 nmol/mol, muestra interacción F×C».
- **Problema:** las dos cifras describen la misma interacción con convenciones distintas. 0,30 es la convención de I2 (diferencia de medias de la columna FC, igual a 2 × coeficiente 0,15). 0,60 es la diferencia entre los efectos simples de F con C alto y con C bajo. El script `M05_diseno.py` imprime 0,300 y `M05_practicas_luna.py` imprime 0,50 y 1,10, pero ningún script imprime 0,60. La bitácora dice que la diferencia 0,60 fue reproducida, y no lo fue.
- **Escenario:** un participante que lee I2 y después la práctica no sabe si la interacción vale 0,30 o 0,60 y puede reportar la cifra que le conviene.
- **Corrección propuesta:** en la solución I escribir la convención: «interacción F×C = (efecto de F con C alto − efecto de F con C bajo)/2 = 0,30 nmol/mol (convención de I2); la diferencia sin dividir es 0,60». Añadir la línea de cálculo al script.

### H-05 — Severidad media — el plan alternativo de A no se resuelve

- **Ubicación:** tarea de A, L271: «Expliquen qué estimaría un plan alternativo con seis analistas pero solo una lectura por ciclo, frente al plan base»; solución A, L273.
- **Problema:** la solución responde solo a «seis analistas con ocho lecturas» (24 días, 48 ciclos, 384 lecturas, 5 gl de analista). No responde al plan con una lectura por ciclo. Con una lectura por ciclo, el estrato «lectura dentro de ciclo» tiene 6 × 4 × 2 × (1 − 1) = 0 gl. Ciclo y error de lectura no se pueden separar, y el componente de ciclo no es identificable por separado. Es el caso más importante para la enseñanza de la sección y falta.
- **Escenario:** un participante que ve que el número de analistas se duplica concluye que el plan alternativo es mejor, sin darse cuenta de que pierde toda la información sobre la variación dentro de ciclo.
- **Corrección propuesta:** añadir a la solución: «con una lectura por ciclo, el estrato lectura-dentro-de-ciclo tiene 0 gl; la variación de ciclo queda confundida con el error; el plan gana cobertura de analistas y pierde identificación del componente de ciclo». Añadir el conteo 6 × 4 × 2 × 1 = 48 lecturas y los gl a `M05_practicas_luna.py`.

### H-06 — Severidad media — «escalonado» no está en la práctica A

- **Ubicación:** bloque A, L267–278; prop_e, M5 A: «A añade: diseños anidados escalonados».
- **Problema:** la escena A1 enseña el diseño escalonado de ISO 5725-3 (cuatro resultados frente a ocho), pero la práctica solo trabaja con un diseño anidado equilibrado (3 × 4 × 2 × 8) y sus alternativas de número de analistas y lecturas. Ningún apartado pide construir, contar ni comparar un plan escalonado. Según prop_e, cada tema enseñado en un nivel debe practicarse y evaluarse en ese nivel.
- **Escenario:** el participante aprende la diferencia entre anidado completo y escalonado, pero la evaluación no le pide aplicarla.
- **Corrección propuesta:** añadir a la tarea de A un plan escalonado simulado (por ejemplo, una fracción de etapas con conteo de resultados y gl por estrato) con su comparación frente al plan base, o indicar en el bloque que el escalonado se enseña y no se evalúa en M5-A, con justificación en prop_e.

### H-07 — Severidad media — potencia y reparto del esfuerzo no están en la práctica I

- **Ubicación:** bloque I, L178–200. Contenido correspondiente en la escena I3, L160–172 (potencia 0,495, 0,501 y 0,873; u(ē) = 0,083, 0,082 y 0,059).
- **Problema:** prop_e, M5 I, añade «distribución del esfuerzo entre niveles, ciclos y días; relación con potencia». La escena lo enseña con cifras, pero la práctica de I solo trabaja el factorial. No hay tarea ni solución que pida calcular o decidir con potencia o con reparto del esfuerzo.
- **Escenario:** el participante aprende a calcular potencia en I3 pero no se evalúa. Según la regla de prop_e (enseñar, practicar y evaluar), el tema queda sin práctica.
- **Corrección propuesta:** añadir un apartado breve a la práctica I: con las cifras de I3 (τ = 0,20, σ = 0,10, Δ = 0,20), elegir entre tres repartos: seis días con ocho lecturas, doce días con ocho lecturas, o seis días con dieciséis lecturas, y justificar la elección por potencia. La solución ya existe en `M05_diseno.py`.

### H-08 — Severidad media — la escala temporal no se declara en ninguna práctica

- **Ubicación:** bloques B (L98), I (L180) y A (L269); regla en prop_e, §3 Convenciones comunes: «Antes de calcular, cada ejercicio declara: respuesta, resultado de interés …, unidad de repetición y escala temporal».
- **Problema:** las tres prácticas declaran respuesta y unidad de repetición, pero ninguna declara la escala temporal (minuto, ciclo, día, campaña). En B y en A esa escala es central, porque la discusión de ciclo y día depende de ella.
- **Corrección propuesta:** añadir en el enunciado de cada bloque una frase «Escala temporal: …». Para B, «día de calibración, con ciclo no identificado en el resumen»; para I, «corrida de la jornada»; para A, «campaña, día y ciclo».

### H-09 — Severidad media — discrepancia entre el certificado y el conteo de B; no debe convertirse en ejercicio

- **Ubicación:** bloque B, L98 y L102 («ocho posiciones registradas por punto y día»); bitácora `curso/S2_modelos_calibracion/M05_practicas_luna.md`, sección Comprobaciones («conteo documentado del certificado»).
- **Problema:** la nota del certificado (hoja `Fotometro`, E17) confirma 8 repeticiones por punto. Pero los datos de `Dia1`–`Dia6` tienen 117 filas por día: 13 bloques de 9 filas, con etiquetas de repetición 0–8 (nueve valores por bloque). El punto 11 aparece dos veces: un bloque extra etiquetado `rep 9`, con un primer valor de 62,3 nmol/mol, y luego el bloque final de cero. Además, la columna `Cycle` vale 1 en todas las filas. Ninguna de estas observaciones aparece en el libreto ni en la bitácora. Por tanto, el conteo 576 es la descripción del diseño del certificado y no el número de filas del archivo. Es un defecto del archivo que debe registrarse, no un ejercicio.
- **Escenario:** si un participante cuenta filas en el archivo, obtiene 702 (6 × 117) en lugar de 576, y el libreto no le explica por qué.
- **Corrección propuesta:** (a) en B, citar la fuente exacta: «nota de la hoja Fotometro, celda E17» en lugar de solo «archivo del certificado»; (b) no cambiar el ejercicio, pero registrar en la bitácora, como hallazgo de archivo para el responsable del certificado: 117 filas por día, nueve etiquetas de repetición por bloque, bloque extra en el punto 11 con `rep 9`, y `Cycle = 1` en todas las filas; (c) en la solución, decir que el conteo de 576 es el de la descripción y no el de las filas del archivo. El hecho de que `Cycle` sea 1 reafirma la escalación de B; puede citarse como apoyo.

### H-10 — Severidad baja — bitácora en ubicación distinta a la solicitada

- **Ubicación:** `curso/S2_modelos_calibracion/M05_practicas_luna.md`. Se pidió `curso/logs/M05_practicas_luna.md`, que no existe.
- **Problema:** los capítulos M01–M04 registran sus bitácoras de prácticas en `curso/logs/`. Esta quedó en la carpeta del capítulo.
- **Corrección propuesta:** mover la bitácora a `curso/logs/M05_practicas_luna.md` (o confirmar con quien coordina que la ubicación del capítulo es la correcta) y actualizar la referencia en la bitácora.

### H-11 — Severidad baja — orden aleatorio «dentro de cada día» frente a una secuencia única

- **Ubicación:** enunciado del bloque I, L180: «orden aleatorio dentro de cada día»; solución, L195: «sortear las 16 etiquetas … con semilla 20261027».
- **Problema:** el script y la solución generan una sola secuencia de 16 corridas. El enunciado habla de un orden por día, pero el ejercicio no define cuántos días hay.
- **Corrección propuesta:** cambiar «dentro de cada día» por «en la jornada» o definir el número de jornadas y generar un orden por cada una, con semilla declarada.

### H-12 — Severidad baja — «nivel de referencia nominal de 100 nmol/mol» sin función en los datos

- **Ubicación:** enunciado del bloque I, L180: «la respuesta es el cambio del error medio frente al nivel de referencia nominal de 100 nmol/mol».
- **Problema:** la regla simulada no usa el nivel 100 nmol/mol. El dato parece real y puede confundirse con un nivel de CALAIRE, aunque el bloque dice que es simulado.
- **Corrección propuesta:** eliminar «frente al nivel de referencia nominal de 100 nmol/mol» o marcarlo como etiqueta sin efecto en la regla.

### H-13 — Severidad baja — el script no imprime las cifras que la solución cita

- **Ubicación:** `curso/S2_modelos_calibracion/calc/M05_practicas_luna.py`, función `factorial()`; solución I, L195 (contraste 1,22 y diferencia 0,60).
- **Problema:** el script no imprime el contraste simple de F con C alto y T alto (1,22) ni la diferencia 0,60. Además, imprime valores flotantes sin redondear (−0.13000000000000006), que no coinciden con el formato de la tabla.
- **Corrección propuesta:** añadir las dos líneas de cálculo y redondear las salidas a dos decimales con coma o con formato fijo.

### H-14 — Severidad baja — la solución de A sobre fijo frente a aleatorio no dice qué cambia

- **Ubicación:** solución A, L273: «Analista fijo limita la conclusión a las personas seleccionadas; aleatorio permite generalizar…».
- **Problema:** en esta estructura anidada, el denominador del contraste de analista sigue siendo la variación de día dentro de analista en ambos casos. Lo que cambia es la población de inferencia y el significado del componente, no el denominador. La solución no lo dice, y la tarea pide comparar las «consecuencias».
- **Corrección propuesta:** añadir una frase: «en esta estructura anidada, el denominador del contraste de analista es día dentro de analista tanto si analista es fijo como aleatorio; cambia la población a la que se generaliza».

## Sin hallazgos

- Cifras de B, I y A: todas coinciden con la ejecución de los dos scripts y con la aritmética a mano (salvo H-01 y H-04).
- Coma decimal y unidades nmol/mol: correctas en los bloques nuevos.
- Origen de datos: B propio con descripción de diseño; I y A simulados y rotulados; ninguna atribución a CALAIRE.
- Alcance: la práctica B cubre lo que prop_e pide (representar 12 × 8 × 6, identificar lo que se observa, lo confundido y los datos necesarios). La práctica I cubre el factorial de robustez. La práctica A cubre el R&R con efectos fijos y aleatorios, unidades, interacciones, denominadores y comparación de analistas frente a lecturas. Las carencias están en H-06, H-07 y H-08.
- Gráficos: prop_e no exige gráficos en M5. El bloque usa tablas con unidades y esquemas trazados por los participantes. No hace falta salida gráfica.
- Solución, decisión y escalamiento: presentes en los tres bloques.
- Ediciones fuera de los bloques: ninguna.

## Fuera de alcance (no auditado)

- Referencias bibliográficas, citas y secciones de referencias del capítulo (trabaja otro supervisor).
- Escenas B1–B4, I1–I3 y A1–A3, salvo donde contradicen un bloque práctico (I3 para H-07; B3 para H-09).
- `calc/M05_diseno.py` (no es un script de práctica nuevo). Contiene una constante `target_slope_change` impresa sin uso. Es una observación menor, no un hallazgo.
