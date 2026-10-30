# Revisión final de citas — S2 (M05–M08), revisor Haiku

Fecha: 2026-10-28. Alcance: (a) aplicación de los hallazgos H-01…H-08 de `S2_revision_haiku.md`; (b) reapertura de localizadores sobre `docs/` con `pdftotext` (salida a stdout, sin ficheros en `/tmp`); (c) páginas. Solo escribe este archivo; no se editaron libretos, cotejo, decisiones ni inventario, y no se hizo commit.

## Hallazgos

**F-01 · alta · decisiones 2 y 3 conservan la corrección falsa**
- `curso/citas/S2_decisiones_luna.md:9` (decisión 2): «EPA TAD §4.4.1 no aporta respaldo suficiente»; «Hahs-Vaughn del capítulo 6 a §9.3».
- `curso/citas/S2_decisiones_luna.md:11` (decisión 3): «el capítulo 6 no trata potencia».
- Contradice el libreto ya corregido (`M05_libreto.md:86`, `:166–172`, `:297`) y el cotejo (`S2_cotejo.md:155–156`). Verificado: `docs/o3_tad_508_20230906_final.pdf` PDF p. 36 contiene «a minimum of three (3) stable testing cycles»; `docs/Statistical Concepts – A First Course.pdf` PDF p. 210 contiene «6.1.3 Power» y p. 234 «6.5 Power Using G*Power».
- Propuesta: reescribir decisiones 2–3 con el estado vigente: TAD verificada (Level 2/3); potencia de una media en HV §§6.1.3/6.5; §9.3 solo como contexto de varianzas.

**F-02 · media · cita entrecomillada que no existe en el PDF**
- `curso/citas/S2_cotejo.md:190` (fila M07:41, Hahs-Vaughn §10.1.1.5.2) cita «the magnitude of the correlation will usually be reduced». La frase no aparece en `curso/citas/extractos/hv_s2.txt` ni en `docs/Statistical Concepts – A First Course.pdf` (búsqueda sin coincidencias). El texto real es «the strength of the relationship … is reduced to a…» (PDF p. 399).
- Propuesta: sustituir la comilla por paráfrasis o por la frase literal, con PDF p. 399.

**F-03 · media · página citada que no coincide**
- `curso/citas/S2_cotejo.md:156` sitúa «There is really not much we can report…» (§9.3) en «PDF p. 364». En el PDF esa frase está en la página 377 (`pdftotext` por página).
- Propuesta: corregir a «PDF p. 377» o indicar explícitamente que el número es de paginación impresa y comprobarlo.

**F-04 · media · páginas de Otto no reproducibles con la copia en `docs/`**
- `curso/citas/S2_cotejo.md:101`, `:114`, `:195`: «tabla 6.1, p. 217» y «ec. (6.20), p. 222». En `docs/Chemometrics Statistics and Computer Application.pdf`, «Table 6.1» está en PDF p. 221–222 y «(6.20)» en PDF p. 227. La ec. (6.17) sí se encuentra (línea 11475 del texto extraído).
- Propuesta: indicar «PDF pp. 221–222 / 227» o declarar «p. impresa 217/222» y anotar cómo se obtuvo esa paginación.

**F-05 · media · ISO 13964 §6.2.2 no está en la página indicada**
- `curso/citas/S2_cotejo.md:154`: «§6.2.2, p. impresa 6». El encabezado «6.2.2 Calibration procedure using the primary UV calibration photometer» está en PDF p. 14 de `docs/Air quality_ Determination of ozone in ambient air_ ISO 13964.pdf`; en p. 6 no aparece. El contenido («at least five ozone concentrations») sí coincide.
- Propuesta: corregir la página o anotar la paginación impresa comprobada.

**F-06 · media · evidencia de la propia revisión en `/tmp`**
- `curso/citas/S2_revision_haiku.md:4` declara que el texto se extrajo «en `/tmp`», y sus evidencias (`hv.txt`, `tad.txt`, `iso6143.txt`, `mmu.txt`, `hv.txt` H-01/H-02/H-04) no están en `docs/` ni en `extractos/`. No es reproducible desde el repositorio.
- Propuesta: en `S2_revision_haiku.md`, sustituir las referencias a `/tmp` por el comando reproducible (`pdftotext -layout docs/<archivo> -`) o por `curso/citas/extractos/`. Verificado en esta revisión: las citas de H-01/H-02/H-04 coinciden con el PDF en stdout.

**F-07 · baja · H-07 no aplicado (anclas de línea obsoletas)**
- `curso/citas/S2_cotejo.md` sigue anclando por línea del inventario (p. ej. «M05:86», «M05:156, 160, 162», «M07:41»). El propio cotejo reconoce el desfase (`S2_cotejo.md:5`). Las citas textuales de las filas ya corregidas sí coinciden con el libreto vigente.
- Propuesta: añadir la cita textual de anclaje en cada fila o regenerar las líneas tras la última edición.

**F-08 · baja · H-03 aplicado por retirada; no reverificado el resto**
- La cita NIST/SEMATECH se ha retirado de `M06_libreto.md`: no hay coincidencias de «NIST», «SEMATECH» ni «itl.nist» en los cuatro libretos. `S2_cotejo.md:75` y `:179` lo registran como «retirada». Es una solución coherente con H-03 (la alternativa era añadir la entrada).
- Propuesta: confirmar que el texto de M06 que trataba la multiplicidad (cerca de `M06_libreto.md:219`) no afirma la regla de Bonferroni sin cita. No se ha reverificado en esta revisión.

**F-09 · baja · rutas de origen del manifiesto no portables**
- `curso/S2_modelos_calibracion/calc/fuentes_M05_M06_final_sol/manifest.json` registra `source` como `/home/w182/w421/calaire-stat/docs/…`. Los `.txt` existen en el repositorio, pero la trazabilidad no se reproduce desde esta ruta.
- Propuesta: registrar la ruta relativa `docs/…` en el manifiesto.

## Estado de H-01…H-08 (a)

| Hallazgo | Estado | Nota |
|---|---|---|
| H-01 Hahs-Vaughn cap. 6 trata potencia | Aplicado en libreto y cotejo; **no** en decisiones | Ver F-01 |
| H-02 TAD §4.4.1 tres ciclos y seis puntos | Aplicado (`M05_libreto.md:86`, cotejo:155) | Correcto; `docs/` PDF p. 36 |
| H-03 NIST sin entrada en M06 | Aplicado por retirada | Ver F-08 |
| H-04 t no central atribuida a §9.3 | Aplicado (`M05_libreto.md:172`: §§6.1.3/6.5 y JKB «no disponible») | Correcto |
| H-05 restricción de rango | Aplicado parcialmente (`M07_libreto.md:41` reformulado) | Cita literal incorrecta: F-02 |
| H-06 ISO 6143 §5.2.2 mal descrita | Aplicado (`S2_cotejo.md:197`) | Encabezado «5.2.2 Validation of the response model» confirmado |
| H-07 anclas de línea obsoletas | No aplicado | F-07 |
| H-08 autor MMU | Aplicado (`M06_libreto.md:295`, `M08_libreto.md:334`) | Portada `docs/Metrology and Measurement Uncertainty.pdf`: «Pedro Paulo Novellino do Rosario», «Alexandre Mendes». Edición/ISBN no anotados |

## Localizadores reabiertos (b)

Diez localizadores comprobados sobre `docs/` (pdftotext):
1. TAD §4.4.1, «three (3) stable testing cycles»: PDF p. 36. OK.
2. Hahs-Vaughn §6.1.3 «Power»: PDF p. 210. OK.
3. Hahs-Vaughn §6.5 «Power Using G*Power»: PDF p. 234. OK.
4. Hahs-Vaughn §10.1.1.5.2 «Restriction of Range»: PDF p. 399. OK (la cita literal falla: F-02).
5. Hahs-Vaughn §9.3 «not much we can report»: PDF p. 377, no 364 (F-03).
6. ISO 6143 §5.2.2 «Validation of the response model»: `docs/ISO 6143 2001.pdf`. OK.
7. Otto ec. (6.17): texto extraído línea 11475. OK; tabla 6.1 y ec. (6.20): páginas distintas (F-04).
8. ISO 28037 §6.1.3 «wi = 1/u(yi)» y minimización ponderada: `docs/ISO 28037.pdf`. OK.
9. Crowder §10.1.2 «Considerations When Fitting Models to Data» (advertencia de extrapolación): `docs/intro_stats_metro_c10.pdf` PDF p. 3. OK.
10. ISO 13964 §6.2.2 «at least five ozone concentrations»: PDF p. 14 (F-05).
Además: EN 14625 §8.4.7 «Sensitivity coefficient to sample gas pressure» (OK); SRP SOP §9.7.19.12 «select 12» (OK, `docs/srp_sop.pdf`); SRP QAPP §6.2.2 «SRP to Level 2 Standard Re-Verifications» (OK, `docs/srp_qapp.pdf` línea 580); MMU autor (OK).

## Páginas inventadas (c)

No encontré páginas inventadas: todas las páginas citadas corresponden a un pasaje real en el PDF, salvo los casos en que el número no coincide con el PDF (F-03, F-04, F-05). Esos no son invenciones del pasaje, sino localizadores mal situados o de paginación no declarada.

## Resultado

**No cerrar S2 todavía.** Hay un bloqueante de consistencia (F-01): las decisiones 2–3 de `curso/citas/S2_decisiones_luna.md` siguen afirmando lo que H-01 y H-02 ya refutaron, aunque el libreto y el cotejo estén corregidos.

Por prioridad:
1. F-01 (alta): reescribir decisiones 2–3.
2. F-02 y F-03 (media): corregir la cita de la frase de Hahs-Vaughn y su página (PDF p. 377).
3. F-04 y F-05 (media): corregir o declarar la paginación de Otto y ISO 13964.
4. F-06 (media): sustituir la referencia a `/tmp` en `S2_revision_haiku.md`.
5. F-07 a F-09 (baja): anclas, verificación de Bonferroni y rutas del manifiesto.

Ninguna página se ha inventado; el problema es de precisión en los localizadores.
