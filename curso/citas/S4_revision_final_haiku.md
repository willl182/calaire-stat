# Validación final de citas — cierre S4

Fecha: 2026-10-27. Revisor: Haiku 5.5. Alcance acotado: comprobar la aplicación de H01–H10 de `S4_revision_haiku.md` (decisiones en `S4_decisiones_luna.md`) sobre `M13_libreto.md` y `AX_libreto.md`, contra `S4_inventario.md` y `S4_cotejo.md`. No se rehízo la investigación ni se revisaron ejercicios o prácticas. No se editaron libretos, inventarios, cotejos ni otros archivos; no hay commits.

## Veredicto

Cierre de citas S4 **aceptable con defectos residuales menores**. Ningún defecto bloquea el cierre; F01 y F02 conviene corregirlos antes de declarar el lote cerrado.

## Estado de H01–H10

| Hallazgo | Estado verificado en archivo | Observación |
|---|---|---|
| H01 | Aplicado. `AX_libreto.md:37` y `:49` citan Hahs-Vaughn §3.3.3.3; ya no hay Crowder §4.3 ni HV §2.3. | Título «3.3.3.3 Sample Variance and Standard Deviation» confirmado en `/tmp/hvS4.txt:5627`. |
| H02 | Aplicado. `AX_libreto.md:139` cita Crowder2020 §10.2.3. | Título «10.2.3 Weighted Least Squares: Non-constant u(y)» confirmado en `/tmp/crowder10S4.txt:214`. |
| H03 | Aplicado. `AX_libreto.md:233` usa «ec. [2]–[3]»; fila 49 «verificada». | Ver F01 (corchetes anidados). |
| H04 | Aplicado. `AX_libreto.md:327` cita [GUM 4.2.3; AX.13]; GUM-S1 7.9.4 g) ya no respalda la fórmula. | §4.2.3 confirmado en `/tmp/gum.txt:1023–1031`. |
| H05 | Aplicado con la categoría «no verificable» en lugar de «ubicado (índice)». Filas 31–34, 41–45, 47, 58–59, 63, 66–67, 69 quedan no verificables. | Estado correcto. Ver L03. |
| H06 | Aplicado. `M13_libreto.md:73` cita solo [ISO 28037 5.5] y [GUM-S2 6.2.1.3]; §11.1 queda en `AX_libreto.md:155`. | Cuerpo de §5.5.2 confirmado en `/tmp/s4txt/iso28037.txt:803–820`. |
| H07 | Decisión: queda «no verificable». `AX_libreto.md:287` mantiene la cita y la afirmación sobre la deducción. | Ver F03 y L02. |
| H08 | Aplicado. Filas 60–62 «no verificable» para contenido; `AX_libreto.md:366` dice «consta en un resultado indexado». | Ver F04 (matiz en el cotejo). |
| H09 | Rechazado por decisión de lote (no editar la guía). | Ver L04. |
| H10 | Parcial: BIPM normalizado; notación ISO y GUM mixta. | Ver F05. |

Conteo: inventario = 69 ocurrencias (M13 22; AX 47). Los corchetes de referencia en los libretos coinciden con esa cifra, y las 69 filas están en `S4_cotejo.md`. Cobertura completa.

## Defectos residuales

- **F01 — Baja.** `AX_libreto.md:233`: `[BIPM-K1 §8, ec. [2]–[3]]` anida corchetes dentro de corchetes. Rompe la forma `[CLAVE localizador]` de la guía §5 y no coincide con la clave literal del inventario. Propuesta: `[BIPM-K1 §8, ec. 2–3]` con una nota en la ficha, o `[BIPM-K1 §8, ecs. 2 y 3]`.
- **F02 — Baja/media.** Línea de evidencia equivocada en el cotejo para GUM 5.2.2. `S4_cotejo.md` filas 2, 3, 25, 48, 50, 51 citan «línea de extracción 1692», pero en `/tmp/gum.txt` el encabezado 5.2.2 está en la línea 1664 (la fila 15 sí dice 1664). Fila 11 y 65 citan «línea 2275» para «10⁴/(1−p)»; en `/tmp/s4txt/s1.txt` esa línea es un encabezado de página y el pasaje está en la línea 2239. El contenido del pasaje es correcto; solo falla el localizador de trazabilidad. Propuesta: corregir las líneas en el cotejo.
- **F03 — Media.** `AX_libreto.md:287`: la frase «su deducción es la de la cota t unilateral para una media» termina con «[Hahs-Vaughn §§6.1, 9.1]». Las filas 56, 58 y 59 de ese localizador están «no verificable», pero el texto le atribuye una deducción. Propuesta: quitar la atribución a Hahs-Vaughn de esa frase, o marcarla como «título de sección, no verificado».
- **F04 — Baja.** Matiz de estado en el cotejo. La cabecera dice «Se comprobó cada localizador en el PDF…», pero varias filas no se comprobaron (no verificables). Las «Fuentes abiertas» dicen que Wiley «confirma la 7.ª edición como 2013», mientras `AX_libreto.md:366` dice que el año «consta en un resultado indexado». Propuesta: en el cotejo, sustituir «confirma» por «consta».
- **F05 — Baja.** Notación de localizadores (H10) sin normalizar: `ISO 28037 5.5` frente a `ISO 28037, cláusula 10.1`; `GUM-S1 5.4, 5.10–5.11` frente a la forma `[CLAVE numeral]` de la guía. No cambia evidencia; es pulido.

## Limitaciones (declaradas, no son error)

- L01. Efron–Tibshirani, Huber, JCGM 106, ILAC-G8 y Montgomery no están en `docs/`; sus afirmaciones quedan no verificables.
- L02. CFR58-A (`AX_libreto.md:287`): las ecuaciones 2–5 son imágenes en el PDF. El texto confirma símbolos y uso (`/tmp/cfrS4.txt:1036–1068`), pero la forma algebraica no se inspeccionó. Se mantiene «no verificable» como decisión conservadora de lote.
- L03. Filas que dependen del título de anexo o de sección (GUM H.5, ISO cláusula 10, GUM-S1 7.9.x) quedan no verificables, no verificadas por título.
- L04. La guía `curso/guia_libreto.md` §5 no lista Efron–Tibshirani, Huber, Montgomery 2013 ni Hahs-Vaughn; H09 se rechazó por decisión de lote. Sigue pendiente para la guía si se quiere cumplir §5 al pie de la letra.
- L05. La evidencia citada en el cotejo apunta a `/tmp/s4txt/` y `/tmp/*S4.txt`, fuera del repositorio. No se puede reproducir desde el repo; en esta validación solo se reabrieron algunas líneas (`/tmp/hvS4.txt:5627`, `/tmp/gum.txt:1023–1031,1664`, `/tmp/crowder10S4.txt:214`, `/tmp/cfrS4.txt:1036`, `/tmp/s4txt/s1.txt:2239`, `/tmp/s4txt/iso28037.txt:803–820`).
- L06. Huber (1,345 y MAD/0,67449), Efron–Tibshirani sobre bootstrap y la fórmula de la matriz de covarianza en statsmodels quedan sin verificar; son limitaciones declaradas en M13.
- L07. Montgomery 2013: solo la ficha editorial está identificada; las fórmulas EWMA/CUSUM de AX.12 no están verificadas.

## Páginas

No se citan páginas impresas como evidencia. Las referencias usan numerales o líneas de extracción.
