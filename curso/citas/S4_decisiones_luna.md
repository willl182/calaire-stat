# Decisiones de cotejo bibliográfico — lote S4

Fecha: 2026-10-27. Alcance: `M13_libreto.md` y `AX_libreto.md`; se leyó `curso/guia_libreto.md` y `curso/revision_final.md`. El catálogo `curso/citas/inventario.md` se consultó solo como catálogo y no se editó. Las decisiones se limitan a citas; no se cambió contenido docente, cálculos ni prácticas.

## H-02 de O-02 — Montgomery en AX.12 y M11

**Hallazgo/prioridad.** `curso/revision_final.md` §5, líneas 56–61, deja H-02 como pendiente de unificar «Montgomery» frente a «Montgomery 2013» en AX.12 y M11. M11 está bajo otro lote activo; se consultó su libreto, pero no se editó.

**Identificación de la edición.** La fuente que corresponde al capítulo de control secuencial es Douglas C. Montgomery, *Introduction to Statistical Quality Control*, **7.ª edición**, Wiley, **2013**, ISBN 978-1-118-14681-1. El sitio compañero oficial de Wiley identifica autor, título y séptima edición por el ISBN 1118146816. La fecha 2013 aparece en el resultado bibliográfico de Wiley Online Library; el resultado indexado se conserva solo como dato bibliográfico y no como evidencia del contenido. Esta consulta no obtuvo el texto íntegro de portada/créditos de un ejemplar primario descargable; por eso edición/año se registran como identificación de catálogo editorial, no como cotejo de ejemplar físico ni como soporte del contenido.

**Localizadores.** Búsqueda editorial/indexada sitúa las cartas CUSUM y EWMA en el capítulo 9, §§9.1–9.2. No se accedió al pasaje primario ni a paginación verificable. No se añadieron numerales ni páginas a AX.12, y no se inventó localizador. Las afirmaciones de AX.12 quedan con estado de apoyo limitado/no verificable en `S4_cotejo.md` cuando requieren verificar contenido más allá de identificar la obra.

**Decisión aplicada.** En AX.12, ocurrencias de líneas 299, 309 y 315, se unificó la clave a `[Montgomery 2013, no disponible en docs/]`, en consonancia con la forma usada en M11. La referencia final de AX se normalizó a **Montgomery 2013**, 7.ª ed., Wiley, 2013, ISBN 978-1-118-14681-1; se conserva la advertencia de que no está en `docs/` y no se asigna numeral/página. **M11 no se editó.** Recomendación para futuros lotes: mantener clave canónica `Montgomery 2013` para esta edición concreta; no reducirla a `Montgomery` ni usarla para otra edición sin cotejo.

## Decisiones adicionales de cotejo

- Se inventariaron 69 ocurrencias de referencias entre corchetes, cada una con capítulo, línea, literal de clave/localizador y una fila de cotejo, incluidas repeticiones.
- AX.1 citaba antes `Hahs-Vaughn §2.3` y `Crowder2020 §4.3`, que no sostienen el divisor n−1. Se retiraron y se reemplazaron por `Hahs-Vaughn §3.3.3.3`, contrastado directamente en el cuerpo local (véase H-01). La explicación de grados de libertad se presenta como deducción del anexo.
- GUM §4.4.6 es una distribución trapezoidal y presenta triangular como caso límite (`β=0`); la base textual más directa para la afirmación sobre triangular está en GUM §4.3.9. El cotejo conserva esta distinción en lugar de atribuir a §4.4.6 una afirmación más fuerte.
- Efron–Tibshirani, Huber, JCGM 106 e ILAC-G8 no están en `docs/`; no se obtuvo texto primario abierto suficiente para verificar cada afirmación. Se dejan como no verificables; no se deduce verificación a partir de título o ficha bibliográfica.
- La evidencia de Crowder y Hahs-Vaughn se delimita a los apartados/pasajes realmente identificados; un encabezado no se trata como prueba de todas las fórmulas o aplicaciones del párrafo.
- No se editó `curso/citas/inventario.md` ni M11. Solo se corrigieron localizadores y claves en M13/AX; no se alteró contenido docente ni ejercicios.

## Resolución independiente de H-01..H-10 — 2026-10-27

| Hallazgo | Decisión y justificación/evidencia |
|---|---|
| H-01 | **Aplicado.** En AX.1 se retiraron Crowder §4.3 (Exploratory Data Analysis) y Hahs-Vaughn §2.3 (percentiles); se cita Hahs-Vaughn §3.3.3.3. Evidencia primaria: `docs/Statistical Concepts – A First Course.pdf`, texto extraído `/tmp/hvS4.txt`, líneas 5627–5687: la sección «Sample Variance and Standard Deviation» explica que estimar con media muestral subestima y que divisor n−1 produce estimador insesgado. La deducción de AX es propia; la fuente respalda la fórmula y propósito, no se atribuye como prueba del argumento de grados de libertad. En AX.1 segunda mención se añadió el mismo localizador. Alias originales anotados en bibliografía final. |
| H-02 | **Aplicado.** AX.5 WLS quedó como `[Crowder2020 §10.2.3]`, no §10.2.1. `docs/intro_stats_metro_c10.pdf`, extracción `/tmp/crowder10S4.txt`, §10.2.3 líneas 214–220: «Weighted Least Squares: Non-constant u(y)» y variación de incertidumbre entre puntos. Se eliminó §6.2 de ISO de esa afirmación porque no hacía falta para respaldar definición de WLS. |
| H-03 | **Aplicado.** Cotejo de BIPM revisado con el documento existente, sin inferir por símbolos: `docs/BIPM.QM-K1_2.protocol.txt`, §8 líneas 378–387 define D en [2] y u(D) en [3]; esta última combina dos incertidumbres sin covarianza. Se ajustó la notación a `ec. [2]–[3]` y se aclaró la referencia final. |
| H-04 | **Aplicado.** AX.13 separa la fórmula `sY/√M` del inciso GUM-S1 7.9.4 g), que corresponde a la desviación de la media de h estimaciones adaptativas. Cita corregida a `[GUM 4.2.3; AX.13]`: `/tmp/gum.txt`, §4.2.3, líneas 1023–1031, da `s²(q)=s²(qk)/n` para n observaciones independientes; AX.13 aporta la deducción aplicada a M salidas independientes. No se atribuye la fórmula a GUM-S1 g). |
| H-05 | **Aplicado parcialmente con alcance honesto.** Se reclasifican como `no verificable` las ocurrencias cuyo soporte en el cotejo era índice/título o no separaba evidencia por componente. No se convierte índice en verificación. En M13 y AX se acotaron las frases bibliográficas: solo los pasajes con cuerpo realmente cotejado se denominan verificados. Los estados del cotejo usan exclusivamente `verificada`, `corregida` o `no verificable`; `corregida` solo indica referencia corregida, no prueba el contenido. |
| H-06 | **Aplicado.** En M13:73 se retiró ISO 28037 §11.1 de la frase sobre covarianzas de parámetros; quedó §5.5. `docs/ISO 28037.txt`, líneas 803–820, contiene la matriz de covarianza y su descripción. AX.6 conserva §11.1 para predicción inversa: texto local líneas 2672–2691 presenta la función inversa y sus incertidumbres/covarianza. |
| H-07 | **Rechazado como verificada; queda no verificable.** `pdftotext` de CFR (§4.1.2–4.1.3; `/tmp/cfrS4.txt`, líneas 1036–1068) confirma la descripción textual de percentil chi-cuadrado, cuantil t, AB y AS; sin embargo las ecuaciones que contienen la forma algebraica son imágenes y no se inspeccionaron visualmente. Por instrucción, no se valida la fórmula de AX a partir de símbolos o texto circundante. |
| H-08 | **Aplicado.** Las tres filas Montgomery conservan estado `no verificable` para contenido (solo ficha/editorial reconocida), sin atribución circular a M11/Crowder ni uso de snippet como evidencia. No se editó M11. Se quitó de la ficha AX la aseveración «el año 2013 consta en la bibliografía de M11/Crowder»; el año se conserva como identificación de catálogo editorial, no como cotejo de contenido. La referencia final mantiene clave `Montgomery 2013`, ISBN y limita explícitamente la verificación al catálogo; las fórmulas de EWMA/CUSUM continúan declaradas no verificadas. |
| H-09 | **Rechazado como obligación local.** Una guía de lote no está obligada a listar todas las claves globales. No se editó `curso/citas/inventario.md`; se propone mantener un catálogo global que incluya `Hahs-Vaughn`, `Crowder2020` y `Montgomery 2013`, sin bloquear el lote por ausencias de tabla. |
| H-10 | **Aplicado en las ocurrencias tocadas.** Se normalizó BIPM a `ec. [2]–[3]`; se corrigieron los localizadores erróneos de H-01/H-02/H-04. No se hizo una normalización estilística indiscriminada de localizadores que no cambiaban evidencia. |

### Auditoría posterior de claves y estados

- Alias de AX normalizados: `Crowder 2020` → `Crowder2020`; `Statistical Concepts` y `Hahs-Vaughn y Lomax` → `Hahs-Vaughn`. Se preservaron en las referencias finales las fichas completas y el registro de alias originales.
- Montgomery continúa como `Montgomery 2013` por ser edición identificada; la ficha editorial no valida las fórmulas.
- En ocurrencias con citas múltiples, el cotejo debe registrar la evidencia de cada componente o quedar `no verificable` si uno no se pudo cotejar. Límites de evidencia (índice, cuerpo, ecuación-imagen y ficha editorial) quedan separados; no se asignan páginas sin inspección directa.

## Ajustes F01–F05

Fecha: 2026-10-27. Fuente: `curso/citas/S4_revision_final_haiku.md`. Sin commits. No se editó `curso/citas/inventario.md` ni M11; no se tocaron cifras, cálculos ni ejercicios.

| Hallazgo | Decisión | Justificación y evidencia |
|---|---|---|
| F01 | **Aplicado.** `AX_libreto.md:233` queda `[BIPM-K1 §8, ecs. 2 y 3]`; fila 49 del cotejo actualizada. | Se evita el corchete anidado. La bibliografía (`AX_libreto.md:362`, «ecs. [2]–[3]») no se cambia: ahí los corchetes son numerales del documento, no una cita dentro de `[CLAVE localizador]`. |
| F02 | **Aplicado, y ampliado.** Anclas corregidas contra extractos regenerados. | GUM 5.2.2: encabezado en línea 1664, no 1692 (filas 2, 3, 25, 48, 50, 51). GUM-S1 7.2.2: línea 2239, no 2275 (filas 11, 65). Fila 68: §8.1.3 en 2678–2694, no 2720 (que es una nota sobre δ/5). ISO 28037 (`docs/ISO 28037.txt`): §5.8.1 en 892, no 908 (filas 19, 35); §6.1.3 en 949, no 965 (fila 36); §5.5.2 en 805–820 (filas 14, 37); §5.6.2 en 836–865 (fila 46). Al regenerar también se hallaron, fuera de F02: GUM 4.3.9 en 1273 y 4.4.6 en 1445 (filas 29–30 citaban 1294/1301); GUM-S1 5.9.1 en 1242 (fila 4); GUM-S1 7.9.2 en 2488 (filas 9, 12). |
| F03 | **Aplicado.** `AX_libreto.md:287` ya no atribuye la deducción a Hahs-Vaughn §§6.1, 9.1; la frase dice «aquí la deducimos como cota t unilateral para una media». | La fila 58 queda como retirada en el cotejo (la ocurrencia ya no está en el libreto); la fila no se renumera. El cálculo de la cota no cambia. `AX_libreto.md:291` mantiene HV §§6.1, 9.1 y sigue «no verificable» (fila 59). |
| F04 | **Aplicado.** Cabecera del cotejo: «Se intentó comprobar…; las filas “no verificable” no tienen pasaje de cuerpo comprobado». Montgomery: «confirma la 7.ª edición como 2013» → «consta». | El año 2013 sigue siendo solo dato de catálogo; `AX_libreto.md:366` ya decía «consta». |
| F05 | **Aplicado parcialmente.** `[ISO 28037, cláusula 10.1]` → `[ISO 28037 10.1]` (`AX_libreto.md:199`); `[ISO 28037, cláusula 10]` → `[ISO 28037 10]` (`AX_libreto.md:203`, `:215`); claves de las filas 43, 44, 47. | **Rechazado** el resto: las listas tipo `GUM-S1 5.4, 5.10–5.11` siguen la forma `[CLAVE numeral]` de la guía sin ambigüedad; cambiarlas no mejora la trazabilidad. |
| L05 | **Aplicado.** Extractos en `curso/citas/extractos/`: `gum.txt` (GUM), `s1.txt` (GUM-S1), `gums2_s1.txt` (GUM-S2), `hvS4.txt` (Hahs-Vaughn), `crowder10S4.txt` (Crowder c10), `cfrS4.txt` (40 CFR 58, ap. A). | Generados con `pdftotext -layout` desde `docs/`. Ya no hay rutas a `/tmp` en `S4_cotejo.md`. ISO 28037 y BIPM-K1 se citan desde los `.txt` ya existentes en `docs/`. Los números de línea dependen de `-layout`. Los extractos de otros lotes (p. ej. `hv_s2.txt`) no se tocaron. |

Pendiente: sin cambios de estado de verificación. Las filas «no verificable» siguen así; F03 solo retira una ocurrencia.
