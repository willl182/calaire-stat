# Revisión de citas y prácticas — S1 Fundamentos (Haiku 5.5)

Fecha: 2026-10-27. Alcance: `curso/S1_fundamentos/M00–M04_libreto.md`, contrastados con `curso/citas/S1_inventario.md`, `S1_cotejo.md`, `S1_decisiones_luna.md`, `curso/guia_libreto.md` y `curso/revision_final.md`. No se ha editado ningún libreto ni ningún cotejo. No hay commits.

Fuentes contrastadas: PDF locales de `docs/` (extraídos a texto en `/tmp/s1rev_txt`, fuera del repositorio) y, para tres puntos, páginas NIST consultadas en línea. Los recálculos numéricos se hicieron en un script temporal fuera del repositorio.

## 1. Resumen

- **Hay un incumplimiento estructural:** M00 desarrolla las tres prácticas (B, I y A) con enunciado, solución y criterio de logro. La guía (§1) y la fase actual exigen solo el marcador «[PRÁCTICA — fase de ejercicios]». Es el hallazgo de mayor gravedad.
- **Hay correcciones declaradas en los cotejos que no están aplicadas en el texto:** M02 Ficha (línea 14), M01 línea 24, M01 líneas 78–100 (GUM-6 Anexo A, ahora confirmado), M02 atribuciones Crowder (líneas 106–140), M02 línea 164 y M03 línea 170 (nota interna). Ver sección 4.
- **Hay afirmaciones de verificación que no se sostienen:** M04 línea 233 (cotejada en 0,15.0, con `scipy.stats.nct`) y M04 línea 138 (promete una ilustración con G\*Power que no existe). Ver H-08 y H-09.
- **Las cifras numéricas de M02–M04 son correctas:** he recalculado Welch, F, chi-cuadrado, TOST, potencia (33,37 / 0,4649 / 25,52 / 0,4658), Grubbs (2,4374 frente a 2,2208 unilateral y 2,2744 bilateral), Dixon (0,8214 frente a 0,59 de Otto), varianzas de M03 y matrices. Son coherentes con los libretos.
- **Varias verificaciones del cotejo están desactualizadas** (por ejemplo, GUM-6 Anexo A, GUM 4.3.3, GUM E.4.3 (E.7), GUM-S2 3.20/3.21, Hahs-Vaughn 2020). Ver sección 5.

## 2. Cobertura de ocurrencias

- Las tablas de `S1_inventario.md` cubren las claves principales de los cinco capítulos (GUM, GUM-6, ISO 17025, EN 14625, VIM, NISTIR, CFR50-D, BIPM-K1, Hahs-Vaughn, Crowder, MMU, ASQ, NIST/SEMATECH, Otto, Lakens, Milton, statsmodels, ISO 28037, AX). No he encontrado ocurrencias de claves en el texto que falten en el inventario.
- **Lista de referencias incompleta (guía §5):** M03 cita AX.2 y AX.3 en el texto (líneas 13, 60, 98, 148, 156, 166, 236, 242, 246, 272), pero no aparecen en «Referencias del capítulo» (líneas 312–320). Ver H-16.
- **Año de Hahs-Vaughn:** el inventario de M04 dice «año no confirmado». El PDF local muestra «First published 2020» y «© 2020 Taylor & Francis». El año 2020 que usan M02, M03 y M04 es correcto; el inventario está desactualizado.
- **Alias:** el texto usa «Hahs-Vaughn» como clave, pero M02 línea 184 y M03 línea 314 mantienen «Statistical Concepts» solo en el título. Es admisible.

## 3. Hallazgos (H-xx)

Gravedad: **crítica** (rompe la guía o la fase), **alta** (afirmación o cita falsa o sin soporte que un lector tomaría como verificada), **media** (localizador, atribución o estado del cotejo incorrecto o incompleto), **baja** (cosmética o de cotejo).

### H-01 · crítica · M00_libreto.md:88–117, 194–215, 261–280
- **Hallazgo:** las tres prácticas están desarrolladas (enunciado, datos, tareas, «Solución docente verificable», «Criterio de logro»). La guía §1 y la fase actual exigen solo el marcador «[PRÁCTICA — fase de ejercicios]», sin enunciado, datos, solución ni rúbrica. En M01–M04 los marcadores están bien aplicados.
- **Agravante en la práctica B (líneas 92, 109, 113):** la práctica se apoya en un «cotejo docente autorizado R03» que asigna P99 → P03. Es una autoridad ficticia dentro del material, y el libreto la presenta como fuente. No puede servir de base para enseñar a reasignar identificadores.
- **Evidencia:** `grep -n "Solución docente\|Criterio de logro\|Enunciado narrado" M0[0-4]_libreto.md` devuelve solo M00.
- **Propuesta:** sustituir cada bloque por el marcador de la guía, con su título. Si se quiere conservar el material, trasladarlo a la bitácora o a la fase de ejercicios. Retirar la referencia al «cotejo autorizado R03».

### H-02 · alta · M02_libreto.md:14 (Ficha, «Referencias clave»)
- **Hallazgo:** dice «Numerales localizados en los PDF». El cotejo (`S1_cotejo.md`, filas M02:14/182 y `S1_cotejo.md` línea 49) declara que esta afirmación global «no procede». CV (ASQ) y MAD (NIST, sin numeral) no son localizados en los PDF, y varias atribuciones a Crowder no se sostienen.
- **Propuesta:** reemplazar por «Localizadores verificados en PDF: …; no verificados o externos: …» con la lista de fuentes sin numeral.

### H-03 · media · M02_libreto.md:106, 110, 140 (y revisar 82, 86)
- **Hallazgo:** el cotejo declaró «corregida» la atribución a Crowder §4.3 y no se aplicó en el texto. Lo que sí contiene Crowder §4.3 (`intro_stats_metro_c04.txt`, líneas 83–86): «identificar valores atípicos y tendencias», con la regla de causa asignable. Por tanto, 82 y 86 están respaldados. No están respaldados: 106 (agrupación por día), 110 (diferencia entre precisión y calibración) y 140 (distinción entre precisión y calibración), que no aparecen en el texto de §4.3.
- **Propuesta:** en 106, 110 y 140 quitar la cita de Crowder o sustituirla por un enunciado no atribuido. Conservar 82 y 86.

### H-04 · media · M02_libreto.md:150, 164
- **Hallazgo:** definiciones de «observación influyente» y de «error absoluto» atribuidas a NIST/SEMATECH. El cotejo las marcó «no verificable» (sin pasaje externo). En el texto no hay ninguna señal de esa limitación, más allá de «sin numeral; no disponible en docs/».
- **Propuesta:** añadir «(definición general; no contrastada con pasaje externo)» o citar un pasaje concreto. No basta con la clave.

### H-05 · media · M03_libreto.md:170
- **Hallazgo:** el texto contiene una nota interna: «[Chi-cuadrado: fuente de la construcción pendiente de verificar, registrada en la bitácora; …]». Es una nota de proceso visible en el libreto (prosa oral), y la cita a la fuente de chi-cuadrado sigue sin resolver.
- **Propuesta:** eliminar el corchete del libreto y mover la nota a la bitácora. Localizar la fuente de la construcción chi-cuadrado (p. ej., Hahs-Vaughn §9.1.1, que sí existe en el PDF local) o retirar la cita.

### H-06 · media · M04_libreto.md:138
- **Hallazgo:** «el planteamiento de planificación por software también se ilustra con G\*Power en el texto». G\*Power no aparece en ninguna parte del libreto (`grep -i gpower` solo encuentra esta línea). Es una promesa sin contenido.
- **Propuesta:** eliminar la frase, o añadir la ilustración si se quiere mantener.

### H-07 · media · M04_libreto.md:233; `S1_cotejo.md` (M04, fila statsmodels, línea 77)
- **Hallazgo:** conflicto de estado. El libreto dice «Implementación cotejada en la versión instalada 0.15.0; potencia contrastada con scipy.stats.nct». El cotejo dice «La revisión no reprodujo versión 0.15.0 ni contrastó documentación/ejecución».
- **Evidencia:** la versión instalada es statsmodels 0.15.0 (`curso/.venv`). El script `calc/M04_ejemplos.py` líneas 202–203 contrasta con `scipy.stats.nct`. Recalculé los cuatro valores de potencia y tamaño del texto y coinciden. La afirmación del libreto se sostiene por el script, pero el cotejo la contradice.
- **Propuesta:** actualizar el cotejo para reflejar esta verificación, o ajustar el libreto a «cálculo reproducido con statsmodels 0.15.0 y contrastado con scipy.stats.nct en `calc/M04_ejemplos.py`».

### H-08 · media · `S1_cotejo.md` (decisión D-10) y `S1_decisiones_luna.md` D-10
- **Hallazgo:** D-10 justifica el cambio de Welch con «cita a Welch con sección incorrecta». Hahs-Vaughn §7.1.3.2 es precisamente «The Welch t′ Test» (`hv.txt` línea 12722). La cita anterior no era incorrecta. El cambio a §§7.3.1 y 7.5.3 es admisible (7.3.1 interpreta el resultado y 7.5.3 genera el test), pero la justificación del cotejo es falsa.
- **Propuesta:** corregir la justificación de D-10 en el cotejo. Dejar el libreto como está.

### H-09 · alta · M04_libreto.md:188–192 (Bonferroni, NIST/SEMATECH)
- **Hallazgo:** la fórmula de la pizarra (línea 190, `p_ajustado = min(mp,1)`) y la frase «sin exigir independencia» (línea 188) se citan a NIST, pero la página NIST prc473 (consultada en línea) no da p ajustados, ni `min(mp,1)`, ni menciona independencia; da el nivel por comparación α/g y la cobertura conjunta. El cotejo ya lo señaló (fila 14/184…237) y el libreto no cambió.
- **Propuesta:** atribuir a NIST solo el principio de intervalos simultáneos y la cobertura conjunta (lo que sí respalda la página). Para `min(mp,1)` citar otra fuente o indicar que es la regla estándar de Bonferroni, sin atribuirla a NIST.

### H-10 · media · M01_libreto.md:24–25
- **Hallazgo:** el cotejo marcó «corregida» las citas GUM B.2.9, GUM-6 §6.1 y VIM 2.3, pero el texto las mantiene sin marca. Solo VIM 2.3 está corroborada por la cita de GUM-6 §5.1; B.2.9 y GUM-6 §6.1 no se han contrastado en este lote (en mi búsqueda plana de `B.2.9` no aparece la definición con ese formato).
- **Propuesta:** en la línea 24, dejar «VIM 2.3 (remitido por GUM-6 §5.1; VIM no disponible en docs/)» y quitar B.2.9 y GUM-6 §6.1, o marcarlos como no verificados.

### H-11 · media · M02_libreto.md:189 y 74 (ASQ, localizador de página)
- **Hallazgo:** el libreto cita «p. impresa 572 (p. 605 del PDF)». En el PDF local, la definición de «coefficient of variation» (línea de texto 27180) está entre el pie «572 Appendix C» (línea 27144) y el pie «Appendix C 573» (línea 27190), por lo que cae en la **página impresa 573**. El conteo de saltos de página da PDF 598, no 605.
- **Propuesta:** corregir a «p. 573» y comprobar el número de página PDF visualmente, ya que el pie y el conteo no cuadran con el 605 declarado.

### H-12 · media · M03_libreto.md:60, 76, 110, 106, 266
- **Hallazgo:** el cotejo dejó como «no verificable» GUM §4.3.3, GUM §6.2.1, GUM G.3.2–G.3.4 y GUM F.1.1.3. Las he comprobado: §4.3.3 (`gum.txt` línea 1130) define u = U/k para una especificación de fabricante o un certificado (respalda la línea 76 y 82); G.3.2 trata de la t de Student (respalda la línea 110); F.1.1.3 (línea 4067) trata de si las influencias supuestamente aleatorias lo son de verdad, lo que respalda cualitativamente la línea 106. Las líneas 266 y la discusión de subperiodos son cálculo propio.
- **Propuesta:** actualizar el cotejo a «verificada» para 4.3.3 y G.3.2, y «apoyo cualitativo» para F.1.1.3. No hace falta cambiar el libreto.

### H-13 · media · M04_libreto.md:160, 164, 234 (GUM E.4.3, ecuación E.7)
- **Hallazgo:** el cotejo dejó «E.4.3 (E.7)» como cita no necesaria. Está en el PDF (`gum.txt` línea 3881: σ²[s(q)] ≈ σ²(q)/(2ν), E.7 bajo E.4.3). Es el soporte exacto para u(s) ≈ s/√(2ν).
- **Propuesta:** actualizar el cotejo: E.4.3 (E.7) verificada. El libreto es correcto.

### H-14 · media · M03_libreto.md:276 (GUM-S2 §3.20 notas 3–5, §3.21 nota 4)
- **Hallazgo:** el cotejo dijo «no verificable». En `gums2.txt`, §3.20 define matriz de covarianza como «symmetric positive semi-definite» y la nota 4 trata de varianzas negativas y matrices no definidas positivas; §3.21 nota 4 relaciona matriz de correlación definida positiva o singular con la covarianza. La cita se sostiene.
- **Propuesta:** actualizar el cotejo a «verificada» (3.20 nota 4; 3.21 nota 4). Libreto correcto.

### H-15 · media · M03_libreto.md:314–320 (Referencias del capítulo)
- **Hallazgo:** la guía (§5) exige «lista completa». El texto cita AX.2 y AX.3 (líneas 13, 60, 98, 148, 156, 166, 236, 242, 246, 272); la lista de referencias no los incluye. M01, M02 y M04 sí incluyen sus AX.
- **Propuesta:** añadir «AX.2 — Varianza de combinaciones lineales y propagación con covarianza (remisión; deducción no desarrollada)» y «AX.3 — Varianzas de rectangular y triangular (remisión)».

### H-16 · baja · M03_libreto.md:319 frente a `S1_cotejo.md` M03:63
- **Hallazgo:** el libreto dice que la página NIST de Autocorrelación «no fue cotejada con pdftotext», mientras el cotejo dice «verificada externamente». Ambas afirmaciones describen el mismo proceso (una página web) con distintos estados.
- **Propuesta:** homogeneizar la formulación: «consultada en línea el 2026-10-27; no está en docs/».

### H-17 · baja · M01_libreto.md:64 frente a `S1_decisiones_luna.md` D-07
- **Hallazgo:** D-07 dice «queda pendiente aplicar ajuste de localizador». El texto ya dice «§4.5.3.10, ecuación 4» (línea 64) y §4.1 para el coeficiente (CFR50-D línea 114, 304,39 ± 0,94). La corrección sí está aplicada; el registro de decisión está desactualizado.
- **Propuesta:** actualizar D-07 a «aplicada».

### H-18 · baja · M00_libreto.md:36 frente a `S1_cotejo.md` M00:11
- **Hallazgo:** el cotejo dice «PDF p. 18». En el PDF local, la nota «NOTE nmol/mol = ppb» (línea de texto 1131) queda en la **página impresa 18** (pie «18» en la línea 1150); la página PDF por conteo es 20. El cotejo confunde ambas numeraciones. §8.2 está confirmada por el índice (línea 1018), y la nota está bajo la Tabla 1 (línea 1031) en §8.2.
- **Propuesta:** corregir el cotejo a «página impresa 18 (PDF 20)». Libreto correcto.

## 4. Correcciones declaradas pero no aplicadas

| Documento | Corrección declarada | Estado en el libreto |
|---|---|---|
| `S1_cotejo.md` M02:14/182 | Ficha «numerales localizados» no procede | Sin cambios (H-02) |
| `S1_cotejo.md` M02:82–140 | Crowder §4.3 corregida (no cubre truncamiento/influencia) | Sin cambios en 106, 110, 140 (H-03) |
| `S1_cotejo.md` M02:56 | Hahs-Vaughn §5.2 no respalda la fórmula s/√n | Aplicada parcialmente: el texto ya atribuye la fórmula solo a GUM (correcto) |
| `S1_cotejo.md` M02:150/164 | NIST sin pasaje | Sin cambios (H-04) |
| `S1_cotejo.md` M01:24–25 | GUM B.2.9, GUM-6 §6.1 no verificadas | Sin cambios (H-10) |
| `S1_cotejo.md` M03:170 | Fuente chi-cuadrado pendiente | Nota interna en el texto (H-05) |
| `S1_cotejo.md` M04:14/184–237 | NIST Bonferroni: alcance estrecho | Sin cambios; la fórmula sigue atribuida (H-09) |
| `S1_cotejo.md` M04:160 | Alcance de E.4.3/E.7 | No aplicado; de hecho la cita es correcta (H-13) |
| `S1_decisiones_luna.md` D-07 | Localizador ecuación de concentración pendiente | Ya aplicado (H-17) |
| `S1_decisiones_luna.md` D-10 | Welch «sección incorrecta» | Justificación errónea; el texto es admisible (H-08) |

## 5. Verificaciones confirmadas en esta revisión (estado actualizable)

- GUM §4.3.3 (u = U/k para especificación de fabricante o certificado); GUM §G.3.2 (t de Student); GUM §E.4.3 (E.7); GUM §4.2.3 (ec. 5); GUM §5.1.3 y §5.2.2; GUM §4.2.7 (correlación temporal).
- GUM-6 Anexo A, símbolo c «sensitivity coefficient (first partial derivative)», PDF p. 74 (respalda M01).
- GUM-S2 §3.20 nota 4 y §3.21 nota 4 (respalda M03:276).
- ISO 17025 §§7.5.1, 7.5.2, 7.11.2, 7.11.6 (texto literal presente).
- CFR50-D §4.1 (304,39 ± 0,94) y §4.5.3.10 ec. 4 con factor L de §4.5.2.5 (respalda M01).
- NISTIR 6963: 308,32 atm⁻¹ cm⁻¹ y 1,147 × 10⁻¹⁷ cm²/molécula.
- BIPM-K1 §1.1: 1,1329(35) × 10⁻¹⁷; PDF p. 3.
- EN 14625 §8.2, Tabla 1: nota «nmol/mol = ppb» (página impresa 18).
- Hahs-Vaughn: §2.3.4 (box plot), §3.2.2 (median), §3.3.1 (range), §7.1.3.2 (Welch t′), §7.3.1, §7.5.3, §9.1.1 (F), 6.1.2. Año 2020 («First published 2020»).
- Crowder §4.3 (EDA: outliers y trends, c04), §4.4.3 (distributional fit), §7.2 (Mathematical Basis), §7.4.1 (covariance). Estos ya figuraban como «no verificables» en el cotejo y ahora están confirmados.
- MMU §3.2.5.2 (triangular); 2025 (Springer).
- Otto §2.2 (Statistical tests): Tabla 2.10 Q(0,99; n=8) = 0,59; Tabla 2.11 T(0,99; n=8) = 2,22. Recalculé Grubbs: 2,2208 unilateral y 2,2744 bilateral (α total 0,01), lo que confirma la afirmación de convención unilateral de M04:172. Dixon Q = (0,28 − 0,05)/(0,28 − 0) = 0,8214.
- ISO 28037 §5.8 (OLS, índice) y §5.
- Milton et al. 2006: Metrologia 43 S291 (identificación). Chi-cuadrado con p = m − n grados de libertad (contexto GLS, `milton.txt` línea 236).
- Recálculos (script temporal): B (media 0,0375; s 0,5263; IC 95 % [−0,4025; 0,4775]; t 0,2015; p 0,8460; χ² 0,2770 con IC [0,1211; 1,1473] y p 0,7094; u(s) 0,1407). Pareadas (t 3,8697; p 0,0061; IC [0,0632; 0,2618]). Welch (medias 10,0167 y 10,9571; diferencia −0,9405; error estándar 0,1531; df 10,9272; t −6,1418; p 0,000075; IC [−1,2778; −0,6032]). F (R 0,8408; IC [0,1404; 5,8669]; p 0,8678). TOST (IC90 [−0,0747; 0,2347]; p 0,0002172 y 0,01183). B con margen ±0,30 (IC90 [−0,3150; 0,3900]). Chi-cuadrado de residuos (2,33; p 0,5068; crítico 7,8147). Potencia (33,37; 0,4649; 25,52; 0,4658). Pearson 0,5. Autovalores de la matriz de correlación (0,407; 0,750; 1,843). Bonferroni (×3). Serie M03 (media de bloques 420,075…420,675; s/√16 = 0,215; 0,207).
- Cálculos de M02 (desviación 0,2449; IQR 0,350; errores 0,133; influyente +1,8: 0,2, 0,556, 0,725, mediana 0,3, MAD 0,6; regresión a = 0,080 y b = 0,002075).

## 6. Limitaciones documentales admisibles (no son errores)

- VIM (JCGM 200:2012) no está en `docs/`; la cita se mantiene como «no disponible en docs/», como exige la guía §5.
- `prop_e` es referencia curricular, no técnica; no se contrasta.
- Crowder «influencia» y «truncamiento» no aparecen en el capítulo 4; la limitación se mantiene solo si el texto la reconoce (H-03, H-04).
- ASQ: la página 573 se deduce de la posición de los pies de página en el texto extraído; falta confirmación visual del PDF (H-11).
- NIST (MAD, Bonferroni, autocorrelación) y Lakens se consultaron en línea; no están en `docs/`. Solo MAD y Bonferroni se han recontrastado aquí; Autocorrelación y Lakens no.
- Milton 2006: el contexto de la cita se lee del texto extraído; no se ha revisado el artículo completo.
- No se han verificado el año y la edición de MMU más allá de la página de copyright.
- Las páginas «p. 3» (BIPM) y «p. 74» (GUM-6) son páginas PDF por conteo de saltos de página; la numeración impresa puede diferir.

## 7. Lo que no se ha podido verificar en esta revisión

- GUM B.2.9, B.2.19, B.2.20 y B.2.23 en forma literal (la búsqueda plana no encontró las definiciones; el cotejo las dio por correctas).
- GUM-6 §5.1 y §6.1 (VIM 2.3).
- Autocorrelación NIST (M03:252–260) y Lakens (M04:198–206), contrastados solo por el cotejo.
- Otto §2.2 en la parte de pruebas no tabulares (no revisada en detalle).
- Hahs-Vaughn §§5.2, 6.4–6.5, 7.8, 9.2 (no revisadas línea a línea).

## 8. Propuesta de orden de corrección

1. H-01 (crítica): sustituir las tres prácticas de M00 por marcadores y retirar el «cotejo autorizado R03».
2. H-09, H-06, H-05, H-02, H-03, H-04: ajustar el texto de M04 (Bonferroni, G\*Power), M03 (nota interna) y M02 (Ficha, Crowder, NIST).
3. H-11, H-10, H-15: corregir localizador ASQ, citas de M01 y lista de referencias de M03.
4. H-07, H-08, H-12, H-13, H-14, H-16, H-17, H-18: actualizar los cotejos y decisiones (estados de verificación, justificación D-10, año de Hahs-Vaughn).
