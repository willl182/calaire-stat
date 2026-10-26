# Revisión Haiku de M00. Estructura de los datos y cálculo reproducible

## Plan de revisión

Revisé `curso/S1_fundamentos/M00_libreto.md` (216 líneas) frente a estas fuentes: `curso/guia_libreto.md` (§§1–5, 7–8), `prop_e.md` (§§2, 3, 5 módulo M0 y M1–M2 solo para la secuencia, §6, §7, §8), y `curso/S1_fundamentos/calc/M00_ejemplos.py`, que ejecuté con `curso/.venv/bin/python -I`. No consulté la bitácora ni edité el libreto.

Recorrido en cinco pasos:

1. **Redacción.** Leí cada escena en voz alta mentalmente: ortografía, puntuación, frases largas, terminología (`pareja`, `lectura`, `registro`), coma decimal y unidades (`nmol/mol`).
2. **Errores.** Recalculé los números de los ejemplos con el script (errores de B1, media, falso error posicional de P03, conteos de I1, Python frente a Calc de A2) y revisé signos y notación (`e = y − x`).
3. **Formato libreto.** Comprobé que las etiquetas de acotación estén en la lista permitida de la guía §1, que no haya viñetas en contenido narrado, y que cada nivel tenga su estructura de la guía §2 (escenas, señales de escalamiento, cierre, referencias).
4. **Referencias.** Cada cita de ISO/IEC 17025 se comparó con el PDF `docs/BS EN ISO_IEC 17025_2017.pdf` extraído con `pdftotext -layout`. Revisé además que las citas a `prop_e` apunten a la sección correcta.
5. **Alcance.** Contrasté el contenido de cada nivel con prop_e §5 (M0) y con las exclusiones de prop_e §6, y comprobé que cada práctica aparezca solo como marcador `[PRÁCTICA — fase de ejercicios]` con el título de prop_e.

## Hallazgos

| id | Ubicación (escena · texto citado) | Tipo | Severidad | Problema | Corrección propuesta |
|---|---|---|---|---|---|
| R01 | Cierre del capítulo, párrafo del nivel A (línea 210): «Estos hábitos preparan la descripción estadística del siguiente módulo» | contenido / transición | mayor | El siguiente módulo es M1 (modelo de medición). La descripción estadística es M2. Además, el cierre no hace la transición al capítulo siguiente que pide la guía §2. | «Estos hábitos preparan M1, donde expresaremos el resultado como función de sus entradas, y M2, donde describiremos la respuesta y elegiremos su resumen.» |
| R02 | Escena I2 (línea 150, `[TRANSICIÓN]`): «el marcador queda aquí, sin enunciado ni solución en esta fase» | formato libreto / marcador | mayor | Señala la falta de desarrollo de la práctica. La instrucción de esta fase es no señalarla; el marcador debe aparecer sin comentario. | Eliminar «el marcador queda aquí, sin enunciado ni solución en esta fase». Dejar: «En la práctica del nivel intermedio reconstruiremos los resúmenes diarios a partir de las parejas originales.» |
| R03 | Escena A2 (línea 196, `[TRANSICIÓN]`): «aquí queda únicamente el marcador» | formato libreto / marcador | mayor | Mismo problema que R02 en el nivel A. | Sustituir «En la última práctica del módulo, … aquí queda únicamente el marcador» por «Ahora practicaremos el contraste con una segunda herramienta y explicaremos sus discrepancias.» |
| R04 | Escena I1 (línea 122, `[ERROR CRÍTICO]`): «[prop_e §§2–3]» | referencia | mayor | El error crítico de «tratar observaciones dependientes como independientes» está en prop_e §8 (Errores críticos), no en §§2–3. La cita apunta a una sección que no contiene el criterio. | Cambiar a «[prop_e §8]». |
| R05 | Errores críticos de B1 (línea 56), B2 (línea 80), I2 (línea 148) y A2 (línea 192) | referencia | menor | Las cajas `[ERROR CRÍTICO]` no citan la fuente. La guía §3 exige que los errores críticos se fundamenten según prop_e §8. | Añadir «[prop_e §8]» al final de cada caja, por ejemplo: «… en vez de completarlo por intuición. [prop_e §8]» en B2. |
| R06 | Escena A2 (línea 182 y línea 184) y Escena B1 (línea 32): `$50,4 - 50,0 = 0,4$`, `$4,441\times10^{-16}$`, `$e = y - x$` (línea 30) | notación / LaTeX | menor | (a) En modo matemático, la coma decimal se renderiza con espacio tras la coma («50, 4»). (b) Se usa guion `-` donde prop_e §3 y la convención del curso usan el signo menos `−`. | Escribir `$50{,}4 - 50{,}0 = 0{,}4$`, `$4{,}441\times10^{-16}$` y `$e = y - x$` → `$e = y − x$` (con U+2212). |
| R07 | Escena A2 (línea 184): «El acuerdo con tolerancia de $10^{-12}$ nmol/mol es verdadero» | voz / fórmulas | menor | La guía §1 pide que toda fórmula se lea en voz alta. Aquí `$10^{-12}$` y `$4,441\times10^{-16}$` no se dicen. También se cita `=C2-B2` (línea 182) sin lectura. | Añadir la lectura: «diez elevado a menos doce nanomoles por mol»; «cuatro coma cuatrocientos cuarenta y uno por diez elevado a menos dieciséis»; «la fórmula es igual a C dos menos B dos». Cambiar «es verdadero» por «se cumple». |
| R08 | Escena B1 (línea 28, pizarra): «`id_lectura`»; Escena B1, línea 26: «identificador de la pareja o del registro de medición»; tabla B1: columna «Pareja» (P01…P05) | terminología | menor | Tres nombres para la misma clave (`id_lectura`, «pareja», «registro de medición»). En la pizarra, `id_lectura` no coincide con la columna «Pareja» de la tabla. | Usar `id_pareja` en la pizarra y en la tabla de la línea 26, y reservar «lectura» para el número de lectura dentro del nivel. Unificar «pareja» en todo el capítulo. |
| R09 | Escena B1 (línea 40): «En la pizarra proyecto los registros» (y tabla de línea 44–50 sin etiqueta) | formato libreto | menor | Mezcla «pizarra» con «proyecto». La tabla de registros se presenta sin `[DIAPOSITIVA]` ni `[MATERIAL]`, y la narración habla de «una tabla de referencias y otra de indicaciones» mientras se muestra una sola tabla. | Insertar `> **[DIAPOSITIVA]** Registros de cinco referencias y cuatro indicaciones (datos simulados)` antes de la tabla, y cambiar la frase de la línea 40 a «En la diapositiva tienen los registros; luego calculo el error…». |
| R10 | Escena B1 (línea 24, 124 palabras); Escena B2 (línea 74, 122 palabras; línea 82, 121 palabras); Escena I1 (línea 126, 122 palabras) | redacción / oral | menor | Frases de más de 100 palabras que no se pueden decir de un tirón en clase. La guía §1 pide frases cortas y ritmo oral. | Dividir cada una en tres o cuatro frases. Ejemplo para la línea 24: «La forma larga expresa esa idea: una fila por lectura. Las columnas guardan los identificadores y las magnitudes. Es una recomendación de organización para este análisis; no es una exigencia de la hoja de cálculo ni cambia el procedimiento del laboratorio.» |
| R11 | Escena A2 (línea 182): «con una hoja de cálculo abierta y recalculada»; «50,0; 100,0; y 150,0» (y lo mismo con las indicaciones) | redacción / puntuación | menor | «Hoja abierta» es ambiguo (¿abierta en qué sentido?). El punto y coma antes de «y» en la enumeración no es estándar. | «con una hoja de cálculo que LibreOffice Calc recalcula»; «50,0; 100,0 y 150,0» y «50,4; 100,8 y 150,7». |
| R12 | Escena I1 (línea 124): «La norma de registros técnicos exige trazabilidad de cambios; para las exclusiones analíticas…» con cita «[ISO 17025 §7.5.1–7.5.2; …]» | referencia / interpretación | menor | La cláusula 7.5.2 trata de enmiendas a los registros técnicos, no de exclusiones de datos. La frase extiende la cita a un caso que la norma no nombra, aunque la redacción es prudente. | Precisar: «La norma exige trazabilidad de las enmiendas (§7.5.2). Una exclusión analítica no es una enmienda, pero la registramos con el mismo criterio de trazabilidad; ese criterio es del curso y no de la norma.» |
| R13 | Escena I2 (líneas 134–142): transformación de tabla ancha a larga | ejemplo | menor | La guía §3 pide al menos un ejemplo numérico en cada tema cuantitativo. Aquí la explicación está completa, pero no hay ejemplo con números: la validación («número de valores no faltantes = número de registros») queda solo en palabras. | Añadir un `[EJEMPLO]` con una tabla ancha de dos filas y dos ciclos, una celda vacía, y tres registros resultantes con la comprobación «3 valores no faltantes = 3 registros». Rotular «simulado». |

## Verificaciones hechas

**Cálculos** (script `curso/S1_fundamentos/calc/M00_ejemplos.py`, ejecutado con `curso/.venv/bin/python -I`):

| Cifra del libreto | Resultado del cálculo | Estado |
|---|---|---|
| B1: errores de P01, P02, P04, P05 = −0,2; 0,4; 0,8; 0,7 nmol/mol | −0,2; 0,4; 0,8; 0,7 | correcto |
| B1: P03 sin error («no calculable») | 1 faltante; 5 referencias, 4 indicaciones | correcto |
| B1: media de los cuatro errores válidos = 0,425 nmol/mol | 0,425 | correcto |
| B1: emparejar P03 por posición daría 100,8 − 50,0 = 50,8 nmol/mol | 50,8 | correcto |
| B1: `e = y − x` con P04: 100,8 − 100,0 = 0,8 | 0,8 | correcto |
| I1: 16 registros; 8/8 por campaña y por analista; 4 por campaña × analista; 4 por analista × día | 16; 8/8; 4 (×4); 4 (×4) | correcto |
| A2: errores Python = [0,4; 0,8; 0,7] nmol/mol | [0,4; 0,8; 0,7] | correcto |
| A2: errores LibreOffice Calc = [0,4; 0,8; 0,7] nmol/mol | [0,4; 0,8; 0,7] | correcto |
| A2: diferencia máxima antes de redondear = 4,441×10⁻¹⁶ nmol/mol; tolerancia 10⁻¹² | 4,441e-16; acuerdo con tolerancia = True | correcto |
| A2: los bits no son idénticos | igualdad binaria exacta = False | correcto |
| A2: fórmula de la primera fila `=C2-B2` con B referencia y C indicación | coincide con el script (`f"=C{row}-B{row}"`) | correcto |

**Referencias** (`docs/BS EN ISO_IEC 17025_2017.pdf`, `pdftotext -layout`, búsqueda de cláusulas):

| Cita del libreto | Texto verificado | Estado |
|---|---|---|
| ISO 17025 §7.5 «Technical records» (encabezado) | encabezado de sección 7.5 | verificado |
| ISO 17025 §7.5.1: factores que afectan el resultado y su incertidumbre; repetición en condiciones lo más cercanas; observaciones originales registradas al producirse e identificadas con la tarea | coincide con la paráfrasis de B2 | verificado |
| ISO 17025 §7.5.2: enmiendas rastreables a versiones previas u observaciones originales; retención de original y enmendado, fecha, aspecto modificado y responsable | coincide con B2 | verificado |
| ISO 17025 §7.11 «Control of data and information management» (encabezado) | encabezado de sección 7.11 | verificado |
| ISO 17025 §7.11.2: sistemas de información validados antes de su introducción; cambios autorizados, documentados y validados antes de aplicarse | coincide con A1 | verificado |
| ISO 17025 §7.11.6: «Calculations and data transfers shall be checked in an appropriate and systematic manner» | coincide con A1 | verificado |
| prop_e §8 contiene la lista de errores críticos (no §§2–3) | lectura de prop_e.md líneas 257 | verificado (fundamenta R04) |
| prop_e §2 contiene las señales de escalamiento del básico, con las siete señales del libreto | lectura de prop_e.md línea 33 | verificado |

**Alcance** (prop_e §5 M0, §6, §8):

- B, I y A: cada tema de prop_e §5 M0 tiene escena. B: tabla larga con identificadores, emparejamiento, unidades, faltantes, lecturas negativas, separación original/calculado. I: varios días/analistas/campañas, conteos, ancho a largo, exclusiones. A: entradas/salidas/comprobaciones, contraste de dos herramientas. Sin faltantes ni sobrantes.
- Marcadores: tres `[PRÁCTICA — fase de ejercicios]` con los títulos de prop_e (B: Level 2 y `e`; I: resúmenes diarios; A: segunda herramienta). Presentes y con el formato de la guía §1.
- Exclusiones de prop_e §6: ninguna aparece en el texto (búsqueda de ISO 13528, PCR/PLS, Allan, KCRV, BIPM, KCDB, aprendizaje automático, z/ζ/Mandel, valores regulatorios). Sin hallazgos.
- Etiquetas de acotación: solo `[PIZARRA]`, `[DIAPOSITIVA]`, `[PREGUNTA AL GRUPO]`, `[EJEMPLO]`, `[ERROR CRÍTICO]`, `[TRANSICIÓN]` y `[PRÁCTICA — fase de ejercicios]`. Todas están en la lista de la guía §1.
- Viñetas en contenido narrado: ninguna. Las únicas viñetas están en la sección de referencias.
- Datos rotulados: B1, I1 y A2 se rotulan como simulados. Ningún resultado se atribuye a CALAIRE.
- Estructura §2: ficha, niveles B/I/A con escenas y señales, cierre y referencias. Presente.

## Resumen

Hallazgos: 13 en total. Críticos: 0. Mayores: 4 (R01–R04). Menores: 9 (R05–R13).

Los cuatro mayores son: transición errónea del cierre (R01), dos transiciones que señalan la falta de desarrollo de la práctica (R02, R03) y una referencia a sección incorrecta de prop_e (R04). Los menores son de notación LaTeX, lectura en voz alta, terminología, puntuación, frases largas, una referencia ISO extendida a un caso no nombrado y la falta de un ejemplo numérico en I2.

Los cálculos y las citas de ISO 17025 coinciden con el script y con el PDF. Ningún número del libreto es incorrecto. El alcance por nivel coincide con prop_e §5 M0, sin exclusiones de prop_e §6.
