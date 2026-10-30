# Decisiones bibliográficas — lote S3

Fecha: 2026-10-27. Alcance: M09–M12. Se leyeron `curso/citas/S3_inventario.md`, la versión de `S3_cotejo.md` ya existente, esta bitácora previa y los cuatro libretos. Para cotejar se consultaron pasajes en PDFs/extracciones locales de `docs/` y `curso/S3_comparacion_decision/calc/`, incluida la copia oficial JCGM 106 y las copias archivadas NIST. No se editó `curso/citas/inventario.md`.

## Decisiones y resultado

1. **Se conserva el trabajo previo.** `S3_inventario.md` se mantiene sin rehacerlo. El cotejo previo y las decisiones se tomaron como punto de partida; se ajustaron estados y se añadieron evidencias precisas cuando se pudo leer pasaje, sin asumir que el número de sección bastara para verificarlo.
2. **Alcance.** Se cotejaron todas las ocurrencias bibliográficas externas indicadas en `S3_inventario.md` y las citas repetidas en cada libreto, incluyendo las secciones de referencias. Remisiones a AX y módulos no se tratan como bibliografía externa. No se desarrollaron prácticas ni se modificaron cálculos.
3. **M09, GUM, ISO y BIPM.** Los pasajes locales respaldan la ley de propagación/covarianza (GUM §§5.2.1–5.2.4, F.1.2.3), cobertura (6.2.1, 6.3.3, G.1.3), predicción inversa (ISO/TS 28037 §5.7), GGMR y consistencia (cláusula 10 y Tablas 25–26), compatibilidad particular de ISO 6143 §6.1, y las definiciones del protocolo BIPM.QM-K1. Se mantienen los límites de interpretación ya escritos: criterio ISO 6143 no universal, `Vxy=0` supuesto didáctico, y SRP 7 no identificado con BIPM-SRP27.
4. **QAPP y SOP.** La lectura de los pasajes cuantitativos confirma SRP/SOP-1 §9.1.1: pendiente 1±0,04 e intercepto 0±4 ppb; §9.1.3: 1±0,03 y 0±3 ppb; y el número de ciclos/rango citado. En SRP-QAPP §6.2.1 y Tabla 7-1 persiste una discrepancia de grafía del intercepto y una diferencia en el modo de describir puntos/ciclos. Se conserva exactamente la grafía existente en el libreto (incluidos `<+` y `±`), sin interpretar el signo ambiguo ni normalizarlo. El cotejo identifica esta limitación, no reescribe el criterio.
5. **M10, JCGM 106 y textos técnicos.** Se leyeron los pasajes de JCGM 106:2012 §§3.3.13–.16, 9.3.2, 9.4 y 9.5 (definiciones de riesgo específico/global y cálculo por densidad conjunta); apoyan las distinciones narradas. Los escenarios numéricos/prior uniforme son simulaciones del curso. Extractos locales de Crowder cap. 5, MMU cap. 8 y ASQ cap. 30 respaldan los conceptos de curva de operación, TUR, guard band y riesgo, sin atribuirles cifras didácticas.
6. **M11, NIST y Crowder.** Las extracciones locales de Crowder caps. 10–11 sí permiten cotejar deriva, incertidumbre durante uso, intervalo de calibración, control estadístico y cartas X-MR. Las copias archivadas NIST confirman rango móvil/límites para individuales, recurrencia EWMA, límite estacionario, y parámetros/detección CUSUM. La fórmula EWMA de arranque variable por `t` no aparece en la página NIST: se delimita como derivación del curso remitida a AX.12; la cita NIST se entiende para recurrencia y estado estacionario. No se cambiaron cifras ni ecuaciones.
7. **Montgomery — unificación real, sin sobreafirmar contenido.** Siguiendo `curso/citas/S4_decisiones_luna.md`, M11 usa la forma canónica **Montgomery 2013**, *Introduction to Statistical Quality Control*, Wiley, 2013 (la 7.ª ed. e ISBN de esta versión se retiran; ver «Respuesta a revisión Haiku», H-02). Se preserva la nota de que se identificó la edición por fuentes bibliográficas/editoriales, no se consultó un ejemplar íntegro; §§9.1–9.2 son localizadores identificados por índice y no evidencia de soporte de contenido. El título/edición/ISBN no se utilizan como verificación de ninguna afirmación concreta de M11. No se editaron AX ni referencias fuera de M11.
8. **M12.** Se consultaron los fragmentos de CFR 40 Part 58 Appendix A §§2.3.1.2 y 4.1.1–4.1.3.2, incluidas ecuaciones leídas visualmente en PDF; EN 14625 §§3.12 y 8.4.5/fórmula 5; GUM §§4.2, 5.2 y G.3.2; y la página NIST de chi-cuadrado ya identificada en la bitácora local. Se confirma el uso acotado de las fuentes. La cita narrativa general a NIST/SEMATECH sobre dependencia temporal en M12:188 queda **no verificable** (sin URL/localizador; la referencia §1.3.5.8 trata chi-cuadrado). GUM respalda aparte la covarianza. No se inventó localizador NIST.
9. **Citas no verificables o parcialmente cotejadas.** Solo se mantiene no verificable cuando falta texto directo o localizador: la mención NIST general de dependencia en M12; el contenido de Montgomery más allá del índice, que se marca corregido/limitado; y la grafía/interpretación normativa del QAPP, no resoluble con evidencia textual ambigua. Las demás referencias locales recibieron cotejo de pasajes relevantes, acotando los límites en `S3_cotejo.md`.
10. **Preservación.** No se tocaron prácticas, ejercicios, cifras, scripts, documentos QAPP, catálogos ni bibliografía externa de capítulos salvo la referencia de Montgomery que ya constaba modificada en M11 al reanudar. Se preservó la grafía QAPP y el trabajo previo. Sin commits.

## Archivos del lote

- `curso/citas/S3_inventario.md` — existente; se conserva.
- `curso/citas/S3_cotejo.md` — completado con estado por grupo de ocurrencias, evidencia de pasaje/localizador y motivo cuando no se verifica.
- `curso/citas/S3_decisiones_luna.md` — actualizado con las decisiones y límites anteriores.
- `curso/S3_comparacion_decision/M11_libreto.md` — Montgomery figura como Montgomery 2013 (Wiley), sin edición ni ISBN, y advierte que no se consultó texto íntegro.

No se editó `curso/citas/inventario.md`; no se cambiaron cifras, ejercicios, cálculos ni grafía QAPP. No se hicieron commits ni se atendieron pendientes ajenos a S3.

## Ronda final — respuesta a F-xx

Fecha: 2026-10-28. Fuente: `curso/citas/S3_revision_final_haiku.md`. Cada hallazgo se comprobó contra `docs/` (`pdftotext -f N -l N`); las copias usadas están en `curso/citas/extractos/`. Sin cambios de cifras, cálculos ni ejercicios. Sin commits.

| F | decisión | evidencia |
|---|---|---|
| F-01 | Aplicado. M11:31 y :122 usaban «no disponible en `docs/`»; ahora «clave bibliográfica; contenido no cotejado», igual que el resto de M11. | Verificado en `M11_libreto.md` (8 ocurrencias uniformes). |
| F-02 | Aplicado. AX:366 retira 7.ª ed. e ISBN y deja «Wiley, 2013»; `inventario.md` (Montgomery y regla 3) unifica la clave según el punto 7. | Crowder 2020 PDF pp. 96 y 145: «Montgomery … Wiley, New York (2013)» (`extractos/S3_crowder2020_montgomery_p96_p145.txt`). |
| F-03 | Aplicado. `inventario.md` Hahs-Vaughn: «verificado en portada/créditos, PDF p. 7». | `docs/Statistical Concepts – A First Course.pdf` p. 7: «First published 2020» (`extractos/S3_hahs_vaughn_p7_creditos.txt`). |
| F-04 | Aplicado en el catálogo: cuatro filas NIST-I, NIST-R, NIST-EWMA, NIST-CUSUM con sección, URL y copia local. M11 no cambia. | Secciones 6.3.2.2, 6.3.2.1, 6.3.2.4, 6.3.2.3 en las copias `extractos/S3_NIST_*.html`. |
| F-05 | Aplicado. M10:195 lista §§7.1.3, 7.6, 7.8.4.1 a)–c) y e), 7.8.6.1–.2; §7.8.2 se retira de la referencia. | ISO/IEC 17025 PDF p. 24: §7.8.4.1 a) (incertidumbre), §7.8.2 sin «intervalo de uso» ni «k» (`extractos/S3_iso17025_p24.txt`). |
| F-06 | Aplicado. Página corregida a PDF p. 24 (impreso 16); la p. 19 es impreso 11 y no contiene §7.8.4. Apunta al extracto. | `extractos/S3_iso17025_p24.txt`: 7.8.4.1 a) en PDF p. 24; pie «16». |
| F-07 | Aplicado en parte. (a) Ruta corregida a `calc/M12_evidencias_fuentes.md`. (b) Copias NIST de §§6.3.2.x en `extractos/`. §1.3.5.8 pasa a «no verificable (copia local pendiente)»: la herramienta de consulta solo devuelve resúmenes y no permite guardar la página íntegra. | Copias `extractos/S3_NIST_{IMR,constants,EWMA,CUSUM}.html`; §1.3.5.8 sin copia local. |
| F-08 | Aplicado. Localizador ASQ: «Calculation of Test Uncertainty Ratio» en PDF p. 2 (encabezado 360); p. 3 = 367; p. 4 = 368 (tabla TUR). El «366» no aparece en el extracto. | `docs/asq_metrological_handbook_c30.pdf` p. 2–4; `extractos/S3_asq_c30_pdf1-4.txt`. |
| F-09 | Aplicado. Dependencia NIST: «234; referencia 310» (antes 188, 241). Chi-cuadrado: «14, 88; referencia 310». | `M12_libreto.md` :234 (dependencia temporal) y :310 (referencia NIST). |

Pendientes tras esta ronda: §1.3.5.8 de NIST sin copia local (F-07b); la revisión de Haiku citaba «p. 366» en `S3_revision_haiku.md`, que no se editó por estar fuera del alcance.
