# Revisión independiente de citas — lote S4

Fecha: 2026-10-27. Revisor: Haiku 5.5. Alcance: `M13_libreto.md` y `AX_libreto.md`, contrastados con `curso/citas/S4_inventario.md`, `S4_cotejo.md`, `S4_decisiones_luna.md` y `curso/guia_libreto.md`. No se editaron libretos, inventarios ni cotejos. Los ejercicios y prácticas no se revisaron (autorizados en otra supervisión).

Contraste realizado con texto extraído (`pdftotext -layout`, en `/tmp/s4txt/`) de: GUM (JCGM 100), GUM-S1, GUM-S2, ISO/TS 28037, protocolo BIPM.QM-K1 v2.1, 40 CFR 58 Ap. A, Crowder 2020 (caps. 4, 9, 10), Hahs-Vaughn y Lomax (índice y cuerpo).

## 1. Cobertura por ocurrencia

- Conteo independiente con `grep` sobre los corchetes de referencia: **M13 = 22** y **AX = 47**, total **69**. Coincide con el inventario (filas 1–22 y 23–69) y con sus líneas.
- No hay ocurrencias bibliográficas fuera del inventario. Las remisiones internas («AX.13», «M9», etc.) y los `[PIZARRA]`, `[EJEMPLO]`… se excluyen correctamente.
- Las ocurrencias repetidas se contaron por separado (p. ej. `GUM 5.2.2` aparece en 13 filas). Cobertura **completa**.
- Problema de cobertura **no** de conteo: el cotejo de varias filas dice «verificada» con evidencia solo de índice. Ver H-05.

## 2. Hallazgos

### H-01 — Alta · AX.1: localizadores que no sostienen la afirmación
- **Archivo/línea:** `AX_libreto.md:37` (y `:49`, que no lleva localizador).
- **Evidencia:** la afirmación es que el divisor `n−1` es el insesgado porque la media muestral consume un grado de libertad. «Crowder 2020 §4.3» es *Exploratory Data Analysis* (`crowder_c04.txt`, encabezado 4.3). «Hahs-Vaughn §2.3» es *Percentiles* (TOC y cuerpo, `hv.txt`). Ninguno trata el estimador de la varianza. La fila 23 del cotejo marca «**verificada**», contradiciendo su propia evidencia; `S4_decisiones_luna.md` lo reconoce pero no cambia el estado.
- **Propuesta:** cambiar el estado de la fila 23 a «no respalda el localizador». Sustituir por el pasaje real de Hahs-Vaughn sobre varianza muestral y grados de libertad; la sección de *degrees of freedom* en `hv.txt` (línea ~10270, «n − 1 in general») es candidata a verificar, pero no debe citarse sin confirmar la sección. En `:49`, añadir localizador o marcarlo como pendiente.

### H-02 — Alta · AX.5: WLS citado a la sección equivocada
- **Archivo/línea:** `AX_libreto.md:139` («ISO 28037 6.1.3, 6.2; Crowder 2020 §10.2.1»).
- **Evidencia:** en `crowder_c10.txt`, §10.2.1 es *Linear Least Squares*; la ponderación no constante es **§10.2.3** («Weighted Least Squares: Non-constant u(y)»). La fila 36 del cotejo marca «verificada» sin haber comprobado Crowder.
- **Propuesta:** `Crowder 2020 §10.2.3`. Reclasificar la fila 36 como «localizador corregido».

### H-03 — Alta · Cotejo BIPM incoherente con el protocolo
- **Archivo/línea:** `AX_libreto.md:233` (`[BIPM-K1 §8, ec. 2–3]`); `AX_libreto.md:362` (referencias: «verificado con pdftotext»); `S4_cotejo.md` fila 49 («no verificable»).
- **Evidencia:** `bipm.txt`, §8 «Degrees of equivalence», ecuaciones [2] `D = x_NS − x_SRP27` y [3] `u(D) = √(u²(x_NS) + u²(x_SRP27))`. La definición de D y de u(D) está verificada, y la [3] sin término de covarianza confirma lo que dice AX.9 («ec. 3 supone independencia»). La fila 49 dice no haber extraído el pasaje, pero el pasaje existe y está en el PDF local. Hay contradicción entre el cotejo y la referencia del propio AX.
- **Propuesta:** cambiar la fila 49 a «verificada (§8, [2]–[3])». Nota: la numeración del protocolo usa corchetes `[2]`, `[3]`; conviene escribir «ec. [2]–[3]» o conservar «ec. 2–3» aclarando la notación.

### H-04 — Media-alta · AX.13: atribución a GUM-S1 7.9.4 g) fuera de lugar
- **Archivo/línea:** `AX_libreto.md:327` («…$s_Y/\sqrt M$… [GUM-S1 7.9.4 g)]»).
- **Evidencia:** en `s1.txt` (línea ~2569), 7.9.4 g) es el paso del procedimiento adaptativo que calcula la desviación estándar del promedio de `h` estimaciones (`s_y`). No es la fórmula del error estándar de la media de `M` ensayos. La fila 64 del cotejo califica la cita como «no verificable» y la propone como respaldo de la fórmula, sin verificar la fórmula.
- **Propuesta:** atribuir la fórmula de `s_Y/√M` al pasaje de GUM-S1 donde se describe la salida y su error estándar (sección de propagación/resumen, a localizar en `s1.txt`; no se ha localizado en esta revisión). Mantener 7.9.4 g) solo para la regla de corridas adaptativas.

### H-05 — Media · Estado «verificada» sobrevalorado (evidencia solo de índice)
- **Archivo/línea:** filas del cotejo que se apoyan en índice o títulos sin pasaje.
- Filas y evidencia:
  - Fila 4 (`M13:35`, GUM-S1 5.9, 6.4.8, 7.3): solo índice.
  - Fila 13 (`M13:73`, GUM-S2 5.2–5.3): solo índice; 6.2.1.3 sí está en texto.
  - Fila 14 (`M13:73`, ISO 28037 11.1): solo índice («Prediction», p. 37). Ver H-06.
  - Filas 31–34 (`AX:107–125`, GUM H.5): solo título del anexo; el cotejo mismo dice que hay que revisar el texto.
  - Fila 35 (`AX:133`, Crowder §10.2.1–10.2.2): §10.2.2 trata varianzas de A y B (`σ_A`, `σ_B`, ec. 10.3), no la covarianza que AX.5 afirma.
  - Filas 37, 38, 43, 44, 47 (ISO cláusulas 5.5, 10.1, 10): título o índice; el texto de 5.5 sí aparece (líneas 803–820), el de 10 no se ha citado en el cotejo.
  - Fila 46 (`AX:209`, ISO 5.6.2): la evidencia citada es el título de §6.2, que no es 5.6.2. El texto de 5.6.2 existe (`iso28037.txt`, línea 836) y no se citó.
  - Filas 63, 66, 67 (GUM-S1 5.9–5.10, 7.9.2, 7.9.4): solo índice.
- **Propuesta:** introducir una categoría «ubicado (índice/título), contenido no verificado» distinta de «verificada». Reclasificar esas filas; corregir la fila 46 por su evidencia real. En «Referencias del capítulo» de M13 (`M13_libreto.md:232–235`) y AX (`:359–366`), la frase «numerales verificados con pdftotext» debe limitarse a los que tienen texto.

### H-06 — Media · ISO 28037 §11.1 en M13 no respalda lo que se dice
- **Archivo/línea:** `M13_libreto.md:73` («la ISO/TS 28037 trata las incertidumbres y covarianzas asociadas con los valores y los parámetros… [ISO 28037 5.5; 11.1]»).
- **Evidencia:** §11.1 es *Prediction* (índice `iso28037.txt`, línea 115), no la covarianza de los parámetros. §5.5 sí lo respalda.
- **Propuesta:** dejar `[ISO 28037 5.5]` y `6.2` en M13:73; conservar `11.1` solo en AX.6 (línea 155), y verificar el cuerpo de 11.1 antes de decir que la inversa «se desarrolla» allí.

### H-07 — Media · CFR58-A: el cotejo no reconoce una verificación posible
- **Archivo/línea:** `AX_libreto.md:287`; fila 57 del cotejo («no verificable»).
- **Evidencia:** `cfr.txt` §4.1.3: «bias upper bound … t_{0.95,n−1} … AB … AS», lo que coincide con `AB + t·AS/√n` de AX.11. §4.1.2 usa el percentil 10 de chi-cuadrado, consistente con el `L_90` de AX.11. Las ecuaciones están como imagen en el PDF, pero el texto confirma los símbolos y el uso.
- **Propuesta:** cambiar la fila 57 a «verificada (texto §4.1.2–4.1.3; ecuaciones como imagen)». Matiz: la cita de AX.11 dice «su deducción es la de la cota t…»; la deducción no está en CFR, solo la fórmula, y el texto ya lo dice.

### H-08 — Media · Montgomery (H-02 de O-02): clave y ficha
- **Archivo/línea:** `AX_libreto.md:299, 309, 315, 366`; `M11_libreto.md:15, 31, 57`; `S4_decisiones_luna.md` §H-02; `S4_cotejo.md` filas 60–62 y «Fuentes abiertas».
- **Veredicto sobre la unificación:** **aceptable**. M11 usa «Montgomery 2013» de forma consistente (líneas 15, 31, 57), y AX.12 ya usa la misma clave. Sin embargo, la clave en M11 no tiene edición ni editorial; la ficha completa solo existe en AX.
- **Ficha editorial (catálogo, no contenido):** Montgomery, *Introduction to Statistical Quality Control*, 7.ª ed., Wiley, ISBN 978-1-118-14681-1 (equivalente a 1118146816). Confirmado por el sitio compañero de Wiley (catálogo editorial). El año **2013** solo consta en un resultado indexado de Wiley Online Library, no en el colofón del libro. El cotejo dice además que el año «consta en la bibliografía de M11/Crowder»: **circular**, porque M11 es el mismo libreto en revisión, y no se ha comprobado en Crowder.
- **Contenido:** la asignación de CUSUM/EWMA al cap. 9 (§§9.1–9.2) viene de un snippet de búsqueda. Las fórmulas de AX.12 (varianza EWMA, ARL por cadena de Markov, CUSUM) **no** se han comprobado en texto. El cotejo marca las filas 60–62 como «corregida», lo que puede leerse como «verificada».
- **Propuesta:** estado de las filas 60–62: «clave unificada; ficha editorial por catálogo; contenido no verificado». Quitar «2013 consta en Crowder» o comprobarlo en el texto de Crowder. Para una verificación de contenido, se necesita un ejemplar o capítulo de Montgomery; hasta entonces, las fórmulas de AX.12 quedan como limitación declarada. (No se editó M11, según la instrucción.)

### H-09 — Baja · Claves no listadas en la tabla de la guía
- **Archivo/línea:** `curso/guia_libreto.md` §5 (tabla de claves, líneas 85–118).
- **Evidencia:** `Efron y Tibshirani 1993`, `Huber 1981`, `Montgomery 2013` y `Hahs-Vaughn y Lomax` no aparecen como claves en la tabla, aunque la guía exige que cada clave esté allí. Además, `Hahs-Vaughn §2.3` en el libreto usa la clave «Hahs-Vaughn» de la tabla y `Crowder 2020` también (correcto).
- **Propuesta:** anotar como pendiente para la guía (no editar aquí): añadir esas claves con su ficha y la marca «no disponible en docs/».

### H-10 — Baja · Notación de localizadores
- Formas mezcladas en el libreto: `GUM-S1 5.4` / `GUM-S1 6.4.8.4`, `ISO 28037 5.5` / `ISO 28037, cláusula 10.1`, `BIPM-K1 §8, ec. 2–3` / `BIPM-K1 §8` y `CFR58-A §§4.1.2–4.1.3`. La guía (§5) pide la forma `[CLAVE numeral]`.
- **Propuesta:** normalizar en una pasada posterior; no bloquea la revisión.

## 3. Limitaciones aceptables (declaradas, no son error)

- **Efron y Tibshirani 1993 (M13:116, 130)** y **Huber 1981 (M13:150, 158, 180)**: no están en `docs/`; se citan sin numeral y con la marca. Correcto según la guía §5. Las afirmaciones de Huber (1,345 ≈ 95 % de eficiencia, MAD/0,67449) y de bootstrap no quedan verificadas; se aceptan como limitación declarada.
- **JCGM 106 e ILAC-G8 (AX:245, 251, 257)**: no están en `docs/`; «no verificable» es el estado honesto.
- **Hahs-Vaughn §6.1 y §9.1 (AX:271, 265, 287, 291)**: los títulos de sección coinciden con el uso (inferencias sobre una media, sobre varianzas), pero no se ha comprobado el pasaje. Se aceptan como «no verificable» con la nota de que el título es coherente.
- **GUM H.5 (AX:107–125)** y **GUM G.4 (AX:179–191)**: G.4 tiene texto (ec. G.2b, línea 4868 de `gum.txt`) y se puede dar por verificada. H.5 requiere lectura del ejemplo; se acepta como limitación.
- **GUM 5.1.2 / 5.2.2 y p. impresas** (bitácora S4, cotejo filas 6, 39): la cita de 5.2.2 con texto literal está verificada (`gum.txt` línea 1664). Las páginas impresas (27, 29) provienen de la bitácora, que no se ha revisado; no se usan como prueba.
- **AX.12 (Montgomery)**: ver H-08; las fórmulas de EWMA/CUSUM quedan como limitación.

## 4. Resumen

- Cobertura: **completa** (69 ocurrencias, conteo verificado).
- Verificación real: confirman el libreto en texto GUM 5.2.2, GUM 4.3.9/4.4.6, GUM-S1 7.2.2, GUM G.2b, ISO 5.8.1, 5.6.4, 6.1.3 y BIPM [2]–[3], CFR 4.1.3. Pero **H-01, H-02 y H-04** son localizadores incorrectos o mal atribuidos que el cotejo marca como verificados.
- Prioridad de corrección: H-01, H-02, H-03 (alta), luego H-04, H-05, H-06, H-07 (media), H-08 (decisión Montgomery), y el resto (baja).
- No se hizo commit ni otro pendiente.
