# Revisión de citas y fichas — S3 Comparación y decisión (Haiku)

Fecha: 2026-10-27. Alcance: `M09_libreto.md`–`M12_libreto.md`, `S3_inventario.md`, `S3_cotejo.md`, `S3_decisiones_luna.md`, `guia_libreto.md` y las entradas de `inventario.md` y AX que comparten clave (Montgomery, Hahs-Vaughn, NIST).

Estado de los archivos: M09–M12 y `AX_libreto.md` cambiaron entre 14:19 y 14:22 por trabajo concurrente de otro lote (prácticas y ajuste de Montgomery en AX:366). Las líneas citadas son del estado de las 14:22. No se editó ningún libreto, cotejo, inventario ni ejercicio. Sin commits.

Alcance real de la comprobación: se verificó cada clave, sus cláusulas o numerales y las afirmaciones de mayor riesgo contra los PDF/extracciones locales de `docs/` y `curso/S3_comparacion_decision/calc/`, y contra copias NIST y fuentes web cuando la local no bastaba. No se recorrió ocurrencia por ocurrencia todo el conjunto de ~300 citas; los casos no revisados se indican al final.

## Resumen

| ID | Gravedad | Tema | Archivo/línea principal |
|---|---|---|---|
| H-01 | Alta | Montgomery atribuido a afirmaciones que el propio cotejo declara no verificadas | `M11_libreto.md` 31–282; `S3_cotejo.md:45` |
| H-02 | Media | Año 2013 y edición justificados con fuentes circulares o inexistentes | `S3_cotejo.md:45`; `inventario.md:52`; `AX_libreto.md:366` |
| H-03 | Media | Sub-claves NIST fuera del catálogo | `M11_libreto.md` 45, 108, 192, 208, 210, 281; `M12_libreto.md` 234, 310 |
| H-04 | Media | NIST atribuido a una afirmación que el cotejo marca «no verificable» | `M12_libreto.md:234`, `:310`; `S3_cotejo.md:56` |
| H-05 | Media | ISO/IEC 17025 §§7.8.2 y 7.8.4 atribuidos a requisitos que no contienen | `M10_libreto.md:110`; `S3_cotejo.md:32` |
| H-06 | Baja | «2,66» atribuido a Crowder §11.2.1 en la bitácora | `M11_bitacora_luna.md:100`; `M11_libreto.md:108` |
| H-07 | Baja | Cotejo NIST-CUSUM subestima lo que la fuente sí dice | `S3_cotejo.md:43` |
| H-08 | Baja | Grafía QAPP: la evidencia visual permite precisar la nota | `S3_cotejo.md:28`; `M10_libreto.md:85` |
| H-09 | Baja | Clave y edición de Hahs-Vaughn; alias ISO 17025 | `M11_libreto.md` 196, 218, 280; `inventario.md:24`; `M10_libreto.md` 14–110 |

Lo verificado sin defecto está en la sección final. Los límites aceptables están separados en la misma sección y no cuentan como defecto.

---

## H-01 — Alta · Montgomery atribuido a afirmaciones que el cotejo declara no verificadas

- **Archivo/línea:** `curso/S3_comparacion_decision/M11_libreto.md` líneas 31, 57, 59, 104, 122, 124, 140, 182, 186, 190, 192, 196, 208, 214 (narración), 15 (ficha) y 282 (referencias). Estado en `curso/citas/S3_cotejo.md:45`.
- **Evidencia:**
  - El propio cotejo (`S3_cotejo.md:45`) dice que el texto de Montgomery no está en `docs/`, que §§9.1–9.2 proceden del índice y que «no se verifican con Montgomery las afirmaciones concretas sobre límites, supuestos, alarma, deriva, dependencia, ARL o intervalo».
  - El libreto mantiene «[Montgomery 2013, no disponible en docs/]» en esas afirmaciones. La línea 196 usa «evaluación de cartas» sin localizador, que el cotejo también reconoce como no comprobable.
  - El estado «corregida» describe la normalización de la clave, no el soporte del contenido. Es la confusión que se pidió evitar: presencia de cita no equivale a respaldo de la afirmación.
  - Localizador: en la web, la 7.ª edición confirma el título «9.1 The Cumulative Sum Control Chart» dentro del cap. 9. §9.2 no aparece confirmado. En la 5.ª edición el mismo capítulo es el 8, así que el número depende de la edición. Esto debe quedar dicho, no solo «índice».
- **Corrección propuesta:**
  1. Por cada línea listada, elegir una de tres salidas: (a) quitar Montgomery si la afirmación ya tiene soporte cotejado en NIST-EWMA/CUSUM/IMR, Crowder §10.8 o §11.2.2, o si es derivación del curso (AX.12); (b) si la afirmación es general, citar «[Montgomery 2013, cap. 9 — solo índice; contenido no cotejado]»; (c) reformular como afirmación del curso sin cita.
  2. Línea 196: quitar «evaluación de cartas» o sustituirla por una referencia comprobable.
  3. En `S3_cotejo.md:45`, cambiar el estado a «no verificada (sin texto del libro); localizador 9.1 confirmado solo en índice web; 9.2 no confirmado».

## H-02 — Media · Año 2013 y edición justificados con fuentes circulares o inexistentes

- **Archivo/línea:** `curso/citas/S3_cotejo.md:45` («adopta año bibliográfico/copyright de la obra»; «decisión S4»); `curso/citas/inventario.md:52` («año/editorial según bibliografía de M11»); `curso/S4_numericos_integracion/AX_libreto.md:366` («catálogo editorial»); `curso/citas/S4_decisiones_luna.md:9` (resultado de Wiley Online Library).
- **Evidencia:**
  - M11 no es fuente de su propio año: es el libreto en revisión. El catálogo `inventario.md:52` aún lo justifica así.
  - No se consultó portada ni colofón. El cotejo habla de «copyright de la obra» sin haber leído ninguno; `S4_decisiones_luna.md:9` lo reconoce.
  - Fuente independiente disponible: la bibliografía de Crowder 2020 en `docs/Introduction to Statistics in Metrology.pdf` (págs. PDF 96 y 145) lista «Montgomery, D.: Introduction to Statistical Quality Control. John Wiley & Sons, New York (2013)». El cap. 11 del mismo libro cita «Montgomery (2013)». Eso respalda el año 2013 sin edición.
  - Edición 7.ª e ISBN 978-1-118-14681-1: aparecen en registros de catálogo de búsqueda web con «c2013». No pude abrir los registros (403 y bloqueo Anubis), así que es fuente secundaria. La variante «2012» que menciona el cotejo no aparece en esos registros, y el cotejo no la resuelve.
- **Corrección propuesta:**
  1. Año 2013: citar la bibliografía de Crowder 2020 (local, independiente de M11).
  2. Edición 7.ª e ISBN: citar catálogo como fuente secundaria, con la nota «no se consultó ejemplar».
  3. Quitar «copyright de la obra» del cotejo salvo que se consulte la portada.
  4. `inventario.md:52` y `AX_libreto.md:366`: sustituir la justificación por la de Crowder y el catálogo. Dejar registrado que la variante 2012 queda sin resolver si no se comprueba.

## H-03 — Media · Sub-claves NIST fuera del catálogo

- **Archivo/línea:** `M11_libreto.md` 45, 108, 192, 208, 210, 281 (`NIST-I`, `NIST-R`, `NIST-EWMA`, `NIST-CUSUM`); `M12_libreto.md` 234 y 310 (`NIST/SEMATECH`).
- **Evidencia:** la guía §5 y `inventario.md` solo registran la clave genérica `NIST/SEMATECH` (`inventario.md:30`), con la regla «citar URL/pasaje y no asignar numeral no cotejado». Las cuatro sub-claves de M11 no existen en el catálogo, y eso rompe la coherencia de claves que se pidió.
- **Corrección propuesta:** o bien añadir las cuatro sub-claves al catálogo con su sección del e-Handbook (6.3.2.2, 6.3.2.1, 6.3.2.4, 6.3.2.3), o bien usar en narración «NIST/SEMATECH §6.3.2.x» con la clave genérica. En ambos casos, mantener URL y copias locales en la referencia de M11. El caso de M12 se trata en H-04.

## H-04 — Media · NIST atribuido a una afirmación que el cotejo marca «no verificable»

- **Archivo/línea:** `M12_libreto.md:234` (afirmación de dependencia temporal con «[GUM 5.2.1–5.2.2; NIST/SEMATECH e-Handbook of Statistical Methods, no disponible en docs/]»); `M12_libreto.md:310` (entrada de referencia: «La mención general a dependencia se cita sin numeral»). Cotejo en `S3_cotejo.md:56`: «no verificable… no se mantiene como afirmación verificada de NIST».
- **Evidencia:**
  - El cotejo retira la atribución y el libreto la mantiene.
  - `inventario.md:30` prohíbe citar NIST sin URL/pasaje.
  - La página NIST §1.3.5.8 (consultada en la web) trata intervalos de varianza y desviación con χ², no dependencia temporal. Así que el apoyo de NIST a esa frase no existe.
- **Corrección propuesta:** en la línea 234 dejar solo «[GUM 5.2.1–5.2.2]» y quitar la mención NIST. En la línea 310, eliminar la frase sobre dependencia citada sin numeral, o reescribirla para indicar que el capítulo no usa NIST para esa afirmación. En `S3_cotejo.md:56`, marcar «retirada».

## H-05 — Media · ISO/IEC 17025 §§7.8.2 y 7.8.4 atribuidos a requisitos que no contienen

- **Archivo/línea:** `M10_libreto.md:110`: «El certificado identifica el mensurando, el intervalo de uso, el método, los resultados, U con su k, la trazabilidad pertinente, la especificación o norma aplicada y la regla de decisión [ISO/IEC 17025:2017, §§7.8.2 y 7.8.4]». Cotejo en `S3_cotejo.md:32`: «verificada… referencia normativa correctamente acotada».
- **Evidencia (texto local `calc/auditoria_M09_M10/BS EN ISO_IEC 17025_2017.txt`):**
  - §7.8.4.1 a) exige la incertidumbre de medida en la unidad del mensurando o en término relativo. No menciona el factor k.
  - §7.8.4.1 b) pide condiciones; c) trazabilidad; e) declaración de conformidad «cuando sea pertinente», con remisión a §7.8.6.
  - §7.8.2.1 (a–p) no incluye «intervalo de uso» ni «k».
  - Por tanto «intervalo de uso» y «U con su k» son buenas prácticas del curso, no exigencias de §§7.8.2 o 7.8.4. Presentarlas como exigencia atribuida a la norma no respalda la frase.
- **Corrección propuesta:** dividir la frase en dos: «la norma exige…» (U con unidad, condiciones, trazabilidad, declaración de conformidad y regla; §7.8.4.1 a–c, e; §7.8.6) y «recomendamos…» (k explícito, intervalo de uso). En `S3_cotejo.md:32`, cambiar el estado a «corregida», con la nota de qué exige la norma.

## H-06 — Baja · «2,66» atribuido a Crowder §11.2.1 en la bitácora

- **Archivo/línea:** `curso/S3_comparacion_decision/M11_bitacora_luna.md:100` (afirma que Crowder respalda 1,128 y 2,66). `M11_libreto.md:108` cita «[Crowder 2020 §11.2.1; NIST-I; NIST-R]» para la cadena de constantes.
- **Evidencia:** el extracto local `calc/fuentes_M11/Crowder11.txt` da 1,128, pero no 2,66 ni 3,267. 2,66 es 3/1,128 (cálculo). 1,128 aparece en `NIST_IMR.html` y 3,267 (D4, n = 2) en `NIST_constants.html`, donde D3 = 0 para n = 2 (confirmado).
- **Corrección propuesta:** en la bitácora, escribir «Crowder da 1,128; 2,66 = 3/1,128 por cálculo; 3,267 de NIST-R». En el libreto basta con separar: «1,128 [Crowder 2020 §11.2.1; NIST-I]; 2,66 = 3/1,128; 3,267 [NIST-R]».

## H-07 — Baja · Cotejo NIST-CUSUM subestima lo que la fuente sí dice

- **Archivo/línea:** `curso/citas/S3_cotejo.md:43`: fila NIST-CUSUM «verificada», con la nota de que la forma de dos acumuladores y la regla estricta «no se atribuyen como fórmula textual de esa página».
- **Evidencia:** `calc/fuentes_M11/NIST_CUSUM.html` describe la forma tabular con acumuladores `S_hi(i)` y `S_lo(i)` que parten de cero, y dice que cuando cualquiera «exceeds h» el proceso está fuera de control. Por tanto la estructura de dos acumuladores y la regla estricta `>h` sí tienen soporte literal en NIST. Lo que no lo tiene es el V-mask, la longitud media de corrida ni el cálculo del ejemplo.
- **Corrección propuesta:** en `S3_cotejo.md:43`, citar esa frase de NIST para la forma tabular y la regla `>h`; mantener sin atribuir ARL y ejemplo. No hay que cambiar M11 por esto.

## H-08 — Baja · Grafía QAPP: la evidencia visual permite precisar la nota

- **Archivo/línea:** `curso/citas/S3_cotejo.md:28` (estado «corregida»: «carácter/raya ambiguos… la grafía no se resuelve sin interpretación autorizada»); `M10_libreto.md:85`.
- **Evidencia (render de `docs/srp_qapp.pdf`, p. PDF 18 y p. PDF 23):**
  - §6.2.1: «the intercept must be + 1ppb» con un «+» subrayado.
  - Tabla 7-1: «intercept <+ 1 ppb», también con «+» subrayado y «<» antes.
  - El mismo glifo subrayado aparece como ± en la misma tabla: «Regression slope = 1.00 ± 0.01», «1) ± 0.2 mb», y en §6.2.2 «0 + 3ppb» (en el texto, con «Intercept of 0 +/- 3ppb» en la Tabla 7-1).
  - Conclusión visual: el signo es ±. La única diferencia real es la presencia de «<» en la Tabla 7-1 y su ausencia en §6.2.1.
  - La grafía del libreto («<± 1 ppb» en Tabla 7-1; «±» en §6.2.1 según la lectura del texto) es fiel a la imagen.
- **Corrección propuesta:** es una limitación aceptable: mantener la grafía y registrar «<» como diferencia entre pasajes. Cambiar en el cotejo «carácter ambiguo» por «signo ± subrayado en la fuente, confirmado visualmente; «<» solo en Tabla 7-1», citando las páginas PDF. No hace falta tocar el libreto.

## H-09 — Baja · Clave y edición de Hahs-Vaughn; alias ISO 17025

- **Archivo/línea:**
  - `M11_libreto.md` 196 y 218 («Hahs-Vaughn 2020 §8.1.1»); 280 (referencia sin edición).
  - `curso/citas/inventario.md:24` («4.ª ed.; año debe confirmarse»).
  - `S3_cotejo.md:44`.
  - `M10_libreto.md` 14, 18, 41, 62, 110, 112 («ISO/IEC 17025:2017») frente a la clave «ISO 17025» de la guía.
- **Evidencia:**
  - La guía §5 registra la clave «Hahs-Vaughn», no «Hahs-Vaughn 2020».
  - La copia local `docs/Statistical Concepts – A First Course.pdf` dice «First published 2020 by Routledge» y «© 2020 Taylor & Francis», con autores Hahs-Vaughn y Lomax; el prólogo habla de la cuarta edición. Con esto queda confirmado el año 2020 que `inventario.md:24` dejaba pendiente.
  - §8.1.1 trata la desviación estándar de la proporción y el error estándar de la proporción (`σp`). El localizador es correcto.
  - ISO/IEC 17025 es el nombre oficial del documento; la clave de catálogo es «ISO 17025». No es un error de contenido, es un alias.
- **Corrección propuesta:** en M11 usar la clave «Hahs-Vaughn» y en la referencia «4.ª ed., Routledge, 2020». En `inventario.md:24`, quitar «año debe confirmarse» y registrar la verificación. En M10, normalizar la clave a «ISO 17025» en las citas cortas y dejar el nombre completo en la referencia.
- **Fuera de lote (para coordinar):** `AX_libreto.md:12` escribe «Crowder2020» sin espacio, y las claves de AX.12 cuentan con «Montgomery 2013» en las líneas 299, 309 y 315 para derivaciones propias del curso (ver H-01).

---

## Verificado sin defecto (con evidencia)

- **GUM** (`calc/fuentes_M11/GUM.txt`): 3.3.7 (U = k·u_c); 4.2.2–4.2.3; 5.1.2; 5.2.1 (fórmula independiente solo válida sin correlación); 5.2.2 (covarianza, ec. 13); 5.2.4 (instrumento o patrón común como fuente de correlación); F.1.2.3 y ec. (F.2); 6.2.1; 6.3.3 (la relación k–p no se fija universalmente); G.1.3 y Tabla G.1 (k = 2 ↔ 95,45 %); G.3.2 (Student para la media con normalidad e independencia).
- **ISO 6143:2001 §6.1** (`docs/ISO 6143 2001.pdf`): criterio con k = 2 para contenido determinado frente a preasignado, texto «may be used». Concuerda con M09 y con la advertencia de no ser regla universal.
- **ISO/TS 28037:2010** (`docs/ISO 28037.pdf`): §5.7 y 5.7.1 (predicción inversa con incertidumbre de a, b y su covarianza; nota de condiciones); §10.3 (χ²_obs = Σ f²_ei, ν = m − 2, cuantil 95 %, con nota de normalidad y primer orden); Tablas 25–26 existen.
- **BIPM.QM-K1 v2.1, 9 Oct 2025** (`docs/BIPM.QM-K1_2.protocol.pdf`): §6 (sección eficaz puede fijarse en cero cuando todos usan el mismo valor); §7, ec. [1] (covarianza intraeje α·x_i·x_j); §8, ecs. [2]–[3]; Apéndice 1 §1 con 2,89×10⁻³·x; Apéndice 1 §3, ec. [21] con u_b = 2,92×10⁻³. Las cifras y numerales de M09 y M10 coinciden.
- **SRP-QAPP 2017** (`docs/srp_qapp.pdf`): Element 14.2 y Figura 14.2 «SRP 36 vs. SRP 7», 12 puntos con desviaciones estándar; la etiqueta «Calibrated Instrument: SRP 7» sostiene que el ajuste impreso tiene orientación distinta a la usada en M09, como dice el libreto.
- **SRP-SOP rev. 1 (vigente 18-09-2015)** (`docs/srp_sop.pdf`): §9.1.1 (pendiente 1±0,04; intercepto 0±4 ppb); §9.1.3 (reverificación anual, rango completo, 1±0,03 y 0±3 ppb).
- **EPA-TAD, EPA-454/B-22-003 (enero 2023)** (`docs/o3_tad_508_20230906_final.pdf`): §4.4.1 (≥3 ciclos estables con cero y ≥6 niveles; pendientes 1,00±0,03; interceptos 0±3 ppb; SD de pendientes < 0,0075; SD de interceptos < 1,00 ppb; límites ±3,1 % o ±1,5 ppb bajo 50 ppb); §4.4.2 (±0,015 y ±1,5 ppb frente a la verificación previa); Apéndice A, ecs. 8–9 con factor 1/3 dentro de la raíz.
- **ISO/IEC 17025:2017** (`docs/BS EN ISO_IEC 17025_2017.pdf`): §7.1.3 (regla de decisión acordada con el cliente); §7.6 (evaluación de incertidumbre); §7.7.1 d) («use of check or working standards with control charts»), que concuerda con la advertencia de M11 de no prescribir reglas de alarma; §7.8.6.1–.2 (documentar y reportar la regla).
- **Crowder 2020** (`docs/Introduction to Statistics in Metrology.pdf`, `intro_stats_metro_c05.pdf`, extractos de caps. 10–11): autores correctos (Crowder, Delker, Forrest, Martin); cap. 5 §5.2.1.1 ec. (5.1) (TUR); §5.2.1.3 ecs. (5.6)–(5.7), donde la integral interior es la probabilidad condicional de aceptar dado el valor verdadero; cap. 10 §10.8 y §10.8.1 (deriva e incertidumbre durante el uso) y §10.8.2 (validación de la pendiente, advertencia de muestras cortas); §10.9 (Calibration Interval Analysis); cap. 11 §11.2.1 (X-MR; 49 rangos y 1,128) y §11.2.2 (CUSUM y EWMA como alternativas).
- **MMU** (`docs/metrology_measure_uncer_c08.pdf`, libro completo): Novellino do Rosario y Mendes, Springer 2025; cap. 8 §8.1 (ILAC-G8 y definiciones), §8.4 (falsos positivos y negativos) y §8.5 (banda de guarda). Nombres completos confirmados en portada.
- **ASQ Metrology Handbook, 3.ª ed.** (`docs/asq_metrological_handbook_c30.pdf`; portada © 2013, 2022; Wade, ed.): cap. 30, «Test Uncertainty Ratio» en pp. 366–367, con las limitaciones del TUR para decisiones de conformidad y control de riesgo.
- **JCGM 106:2012** (`calc/auditoria_M09_M10/jcgm106_fuente/JCGM_106_2012_E.txt`): 3.3.13 (riesgo específico del consumidor), 3.3.14, 3.3.15 (riesgo global del consumidor), 3.3.16; 9.3.2 (cuatro resultados de decisión); 9.4 (densidad conjunta); 9.5 ecs. (17)–(18); encabezados de 6.2 (Bayes) y 7.1 (regla general de probabilidad de conformidad).
- **40 CFR Part 58, App. A** (`docs/Appendix A to Part 58_ Title 40 (up to date as of 10-20-2026).pdf`): §2.3.1.2 (CV superior 90 % ≤ 7 % y sesgo absoluto superior 95 % ≤ 7 % para O₃ automático); §4.1.1 (d_i = (meas − audit)/audit); §4.1.2 (cuantil inferior χ² 10 % con n − 1 grados); §4.1.3 (t 0,95, n − 1, AB, AS); §4.1.3.1–.2 (signo por percentiles 25 y 75). Los cuantiles de M12 I1–I2 (χ²₀,₁₀;₃ = 0,5844; t₀,₉₅;₃ = 2,3534; t₀,₉₇₅;₃ = 3,1824) son valores estadísticos estándar, no del CFR; no los recalculé con software, así que no los doy por verificados numéricamente.
- **EN 14625:2012** (`docs/BS EN 14625_2012.pdf`): §3.12, nota 1 («3,3 × (s_z/B)»); §8.4.5 (20 lecturas en cero y en c_t; ec. 4); fórmula (5) l_det = 3,3·s_r,z/B; Tabla 1 (s_r,z ≤ 1,0 nmol/mol).
- **NISTIR 6963, Tabla 4, p. 20** (`docs/nistir6963.pdf`): diez pendientes SRP-0/SRP-2 coinciden con M11 I1. Autores verificados en portada.
- **NIST e-Handbook (copias locales y web):**
  - §6.3.2.2 (MR = |x_i − x_{i−1}|; límites con 1,128; `NIST_IMR.html`).
  - §6.3.2.1 (factores para n = 2: D3 = 0, D4 = 3,267; `NIST_constants.html`).
  - §6.3.2.4 (EWMA: recurrencia, s²_ewma = λ/(2 − λ)·s², límite estacionario). No contiene la fórmula de arranque dependiente de t; la «corregida» de M11 es correcta.
  - §6.3.2.3 (CUSUM tabular; ver H-07).
  - §1.3.5.8 (χ² para la varianza, con intervalos para σ; consultado en web) — M12 I1 y la referencia son coherentes.
- **Hahs-Vaughn & Lomax, 4.ª ed., Routledge 2020** (`docs/Statistical Concepts – A First Course.pdf`): §8.1.1 (proporción, desviación y error estándar de la proporción). Ver H-09 para la clave.

## Limitaciones aceptables (no son defectos)

- **Montgomery sin texto íntegro:** es aceptable citar la obra, siempre que la cita esté marcada como no cotejada en el contenido (H-01 cubre las citas que no están marcadas así).
- **Ediciones de catálogo por búsqueda web:** la 7.ª edición y el ISBN son fuente secundaria. Aceptable si se declara (H-02).
- **Grafía QAPP con «<» en la Tabla 7-1:** se conserva, sin reescribir el criterio (H-08).
- **Predicción con x₀ incierto:** el cotejo atribuye la propagación adicional a la GUM y no a ISO 28037; es aceptable.
- **2,66 como cálculo:** aceptable si se escribe como 3/1,128 (H-06).

## Lo que no se revisó

- No se leyó ocurrencia por ocurrencia cada una de las ~300 citas; se verificaron todas las claves, sus cláusulas y las afirmaciones de mayor riesgo.
- Crowder §10.9 (intervalos de calibración) se confirmó solo por título y localizador; no se leyó el contenido.
- Las ecuaciones de BIPM (ecs. 15–20) y del CFR (ec. 2–3 como imágenes) se leyeron en texto extraído, no visualmente, salvo lo que el cotejo dice haber inspeccionado.
- Los registros de catálogo de Montgomery no se pudieron abrir (403/Anubis).
- Los cambios concurrentes de M09–M12 (14:19–14:22, incluidas prácticas de otra supervisión y sus soluciones numéricas en M12) no se revisaron como contenido; solo se comprobó que las citas siguen en su sitio.
