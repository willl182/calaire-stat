# Revisión final de citas — S3 Comparación y decisión (Haiku)

Fecha: 2026-10-28. Alcance: `curso/S3_comparacion_decision/M09`–`M12_libreto.md`, `curso/citas/S3_cotejo.md`, `curso/citas/S3_decisiones_luna.md`, `curso/citas/S3_revision_haiku.md` (H-01…H-09) y, para propagación, `curso/citas/inventario.md` y `curso/S4_numericos_integracion/AX_libreto.md:366`. No se editó ningún libreto, cotejo, inventario ni ejercicio. Sin commits.

## Comprobación de hallazgos previos

| H | Estado | Nota |
|---|---|---|
| H-01 Montgomery | aplicado con residuo | Las afirmaciones de M11 ya llevan «contenido no cotejado» o se quitaron (F-01). |
| H-02 año/edición | parcial | M11 y decisiones aplicados; AX:366 e inventario:52 no (F-02). |
| H-03 sub-claves NIST | no aplicado | Las cuatro sub-claves siguen fuera del catálogo; la justificación está en el cotejo, no en el inventario (F-04). |
| H-04 NIST dependencia | aplicado | M12:234 solo cita `[GUM 5.2.1–5.2.2]`; M12:310 declara que no se atribuye a NIST. |
| H-05 ISO 17025 §§7.8.2/7.8.4 | parcial | El cuerpo de M10:110 ya no las atribuye; la referencia M10:195 y la fila del cotejo sí (F-05, F-06). |
| H-06 «2,66» | aplicado | M11:108 separa 1,128 (Crowder §11.2.1) de 2,66 = 3/1,128 y de 3,267 (NIST-R). |
| H-07 CUSUM | aplicado | Fila NIST-CUSUM del cotejo cita la forma tabular y la regla `>h`; NIST_CUSUM copy línea 440: «exceeds (h), the process is out of control». |
| H-08 grafía QAPP | aplicado | Fila QAPP del cotejo describe el signo ± subrayado y la presencia de «<» solo en Tabla 7-1 y §6.2.2. Página PDF 18 y 23 confirmadas. |
| H-09 Hahs-Vaughn/ISO | parcial | Libreto y referencia M11:280 aplicados (4.ª ed., 2020); `inventario.md:24` sigue con «año debe confirmarse» (F-03). |

## Hallazgos

**F-01 · Media · Etiqueta de Montgomery no uniforme.** `curso/S3_comparacion_decision/M11_libreto.md:31` y `:122` dicen «[Montgomery 2013, no disponible en `docs/`]», mientras el resto (`:57`, `:59`, `:104`, `:124`, `:140`, `:182`, `:186`, `:214`) dice «contenido no cotejado». La primera etiqueta describe disponibilidad, no soporte. Propuesta: usar la misma etiqueta en todas: «[Montgomery 2013, clave bibliográfica; contenido no cotejado]».

**F-02 · Media · H-02 no propagado; contradicción entre libretos.** `curso/S4_numericos_integracion/AX_libreto.md:366` sigue con «7.ª ed., Wiley, 2013, ISBN 978-1-118-14681-1» y «catálogo editorial de Wiley», mientras M11:282 retira la 7.ª edición e ISBN. `curso/citas/inventario.md:52` sigue con «año/editorial según bibliografía de M11» y `:58` pide mantener Montgomery «diferenciada por año/edición», contrario a la unificación de `S3_decisiones_luna.md` punto 7. Propuesta: en AX:366, dejar «Montgomery, D. C., *Introduction to Statistical Quality Control*, Wiley, 2013» con la misma nota de no consulta íntegra; en `inventario.md:52` y `:58`, reemplazar por la unificación y la justificación de Crowder 2020 (PDF pp. 96 y 145, confirmadas: «Montgomery … Wiley (2013)»). AX es fuera de lote: coordinar.

**F-03 · Baja · Año de Hahs-Vaughn sin actualizar en catálogo.** `curso/citas/inventario.md:24` dice «año debe confirmarse en portada/créditos». Está confirmado en `docs/Statistical Concepts – A First Course.pdf` («First published 2020»). Propuesta: sustituir por «4.ª ed., Routledge, 2020 (verificado en créditos)».

**F-04 · Media · Sub-claves NIST sin entrada en catálogo.** `curso/citas/inventario.md:30` solo registra `NIST/SEMATECH`, pero `M11_libreto.md:45`, `:108`, `:192`, `:208`, `:210`, `:281` usan `NIST-I`, `NIST-R`, `NIST-EWMA`, `NIST-CUSUM`. El cotejo (`S3_cotejo.md`, fila 240) justifica los alias, pero la regla de la guía §5 exige que el catálogo recoja las claves. Propuesta: añadir las cuatro filas al inventario con su sección (6.3.2.2, 6.3.2.1, 6.3.2.4, 6.3.2.3) y URL, o cambiar en M11 a «NIST/SEMATECH §6.3.2.x».

**F-05 · Media · Referencia de M10 conserva las secciones retiradas.** `curso/S3_comparacion_decision/M10_libreto.md:195` lista «§§7.1.3, 7.6, 7.8.2, 7.8.4 y 7.8.6.1–7.8.6.2» como numerales usados, pero `:110` ya no atribuye §§7.8.2/7.8.4. Verificado en `docs/BS EN ISO_IEC 17025_2017.pdf`: §7.8.2.1 a–p no incluye «intervalo de uso» ni «k»; §7.8.4.1 a) pide la incertidumbre en la unidad o en término relativo, sin factor k. Propuesta: en `:195` dejar «§§7.1.3, 7.6, 7.8.4.1 a)–c) y e), 7.8.6.1–7.8.6.2» y, si se cita §7.8.2, indicar que solo se usa el alcance del informe.

**F-06 · Media · Localizador de página incorrecto en el cotejo.** `curso/citas/S3_cotejo.md`, fila ISO 17025 (§§7.1.3, 7.6, 7.8.2, 7.8.4…), dice «PDF p. 19 / impreso p. 16». En `docs/BS EN ISO_IEC 17025_2017.pdf` el texto «7.8.4.1 … a) the measurement uncertainty…» está en **PDF p. 24**; la p. 19 no contiene §7.8.4. Además, la fila cita `calc/auditoria_M09_M10/…` cuando existe el extracto reproducible `curso/citas/extractos/S3_iso17025_2017.txt`. Propuesta: corregir a «PDF p. 24» (y comprobar la página impresa antes de citarla) y apuntar al extracto.

**F-07 · Media · Evidencia fuera de `docs/` y `extractos/`; ruta rota.** (a) La fila `M12_evidencias_fuentes.md` del cotejo indica un archivo que no está en la raíz de `curso/S3_comparacion_decision/`; existe en `curso/S3_comparacion_decision/calc/M12_evidencias_fuentes.md`. (b) Las filas NIST verificadas (§§6.3.2.1–6.3.2.4 y 1.3.5.8) se apoyan en `calc/fuentes_M11/NIST_*.html` y en consulta web del 25-10-2026; ninguna copia está en `docs/` ni en `curso/citas/extractos/`, y §1.3.5.8 no es reproducible sin red. Propuesta: copiar las páginas NIST a `curso/citas/extractos/` (o marcar «web, no reproducible»), y corregir la ruta de M12.

**F-08 · Baja · Página ASQ no reproducible.** `S3_cotejo.md` (fila ASQ) y `S3_revision_haiku.md` citan «p. 366 y siguientes». El extracto `docs/asq_metrological_handbook_c30.pdf` tiene 4 páginas PDF con encabezados impresos 367 y 368; no encontré «366» impreso ni la sección «Test Uncertainty Ratio» con ese número. Propuesta: citar «cap. 30, pp. 367–368 (extracto local)» o confirmar 366 con una vista del ejemplar.

**F-09 · Baja · Localizadores obsoletos en el cotejo.** La fila NIST-dependencia cita `M12:188, 241`; la frase ya está en `M12_libreto.md:234` y la referencia en `:310`. Propuesta: actualizar la línea.

## Muestreo de localizadores (reabiertos con `pdftotext` sobre `docs/`)

Ocho de doce comprobados OK:
1. GUM §5.2.2, ec. (13) — texto «When the input quantities are correlated» (`GUM … libgen.li.pdf`, línea 2112).
2. ISO 6143 §6.1 — «compatibility criterion, based on a coverage factor of k = 2, may be used» (línea 1362).
3. ISO/TS 28037 §10.3 y Tabla 25 — «10.3 Validation of the model» (líneas 2481, 2504).
4. Crowder 2020 §11.2.1 — «49 moving ranges … divided by the constant 1.128» (línea 16266).
5. SRP-SOP §9.1.1 — «Slope 1±.04 and Intercept 0 ppb ±4 ppb» (línea 907).
6. EPA-TAD §4.4.1 — «All 3 regression intercepts = 0 ± 3 ppb»; «SD of the 3 slopes < 0.0075» (líneas 1484–1685).
7. 40 CFR 58 App. A §4.1.2 — «precision estimate… 10th percentile of a chi-squared» (líneas 1069–1082).
8. ISO 17025 §7.8.4.1 a) y §7.8.6.1 — PDF p. 24 y texto (línea 1435, 1496).
9. Hahs-Vaughn §8.1.1 y «First published 2020» (líneas 71, 18986).
10. BIPM.QM-K1 Apéndice 1 §3 — «u_b = 2.92×10⁻³» (línea 1123 del `.txt`).
11. BS EN 14625 §3.12 — «3,3 x (sz/B)» (línea 525).
12. NISTIR 6963 Tabla 4 (p. 20) — localizada.

Además: Montgomery en Crowder PDF pp. 96 y 145 (1 coincidencia cada una); QAPP PDF p. 18 («intercept must be + 1ppb», «0 + 3ppb») y p. 23 (Tabla 7-1); NIST_CUSUM copy línea 440.

No reabiertos: Crowder §10.8 (p. 249) y §10.9 (p. 258): el PDF da errores de xref y no pude localizar las páginas de forma fiable. ASQ «p. 366» (F-08).

## Páginas inventadas

No encontré páginas inventadas en los localizadores comprobados. Las discrepancias son de número o de ruta (F-06, F-08) y no de contenido.

## Resultado

**Parcial.** La mayoría de hallazgos H-01…H-09 se aplicaron en los libretos y en el cotejo con justificación coherente con el texto. Quedan pendientes en el lote: F-01 (etiqueta de Montgomery), F-04 (catálogo NIST), F-05 (referencia M10), F-06 (página ISO) y F-07 (evidencia NIST fuera de `docs/`/`extractos/` y ruta rota). F-02 y F-03 afectan a `inventario.md` y AX fuera del lote y conviene coordinarlos. Ningún estado «verificada» de NIST tiene hoy evidencia reproducible en `docs/` o `extractos/` (F-07). Las demás filas verificadas que cité sí tienen evidencia en `docs/` o `extractos/` o en `calc/` con PDF correspondiente en `docs/`.
