# Revisión de la unificación de claves bibliográficas (Haiku)

Revisado: `curso/citas/unificacion_claves.md` contra `curso/S*/M*_libreto.md`, `curso/S4_numericos_integracion/AX_libreto.md`, `curso/citas/inventario.md`, `curso/guia_libreto.md` §5, y `git diff curso/` (referencia HEAD). No se editó ningún otro archivo.

## Verificado sin incidencias

- `Crowder2020` (sin espacio): 0 ocurrencias en los libretos; la entrada de AX está como `Crowder 2020`.
- `Hahs-Vaughn y Lomax` dentro de corchetes: 0 ocurrencias; M05:168 y M06:219 usan `Hahs-Vaughn`.
- Montgomery: no hay mezcla de «Montgomery DAE» y «Montgomery 2013» en la misma cita. DAE aparece solo en M05; 2013 solo en M11 y AX.
- M05:309 (DAE 9.ª ed., Wiley, 2017): consta en la bibliografía de Crowder en `curso/citas/extractos/S3_crowder2020_completo.txt` (líneas 10198 y 14919).
- Las claves en corchetes del inventario (GUM, GUM-6, GUM-S1/S2, ISO 17025, ISO 28037, EN 14625, MMU, Crowder 2020, Otto, ASQ, NISTIR 6963, CFR50-D, BIPM-K1, prop_e, VIM, Lakens 2017, NIST-I/R/EWMA/CUSUM, etc.) existen en `inventario.md`.

## Hallazgos

**U-01 (alta). M06:219: cambio de fuente, no de clave, y mal descrito en la unificación.**
En HEAD, la frase de multiplicidad («cada una se evalúa al cero coma cinco por ciento») citaba `[NIST/SEMATECH, «Bonferroni’s method», §7.4.7.3, …prc473.htm (consultado 2026-10-27)]`. Ahora dice `[Hahs-Vaughn §8.2.1, PDF p. 332]`. La cita NIST desaparece del libreto (M06 tiene 0 menciones de NIST frente a 1 en HEAD). `unificacion_claves.md` y `citas/citas_unificacion_luna.out` (línea 7) describen el cambio como «Hahs-Vaughn y Lomax → Hahs-Vaughn», lo cual no corresponde.
Comprobado en `docs/Statistical Concepts – A First Course.pdf`, PDF p. 332 (impreso 313): trata el método de Bonferroni para pruebas de proporciones, así que hay soporte parcial. Pero el texto del libreto habla de diez contrastes de interacción, no de proporciones.
Propuesta: restaurar la cita NIST §7.4.7.3 o citar ambas fuentes, y registrar el cambio como cambio de fuente. Lo decide quien redacta el libreto.

**U-02 (alta). Cifras y datos cambiados frente a HEAD que no figuran en el registro de unificación.**
- `S1_fundamentos/M02_libreto.md:186` y `:188`: el punto influyente pasa de +1,8 a +1,6 nmol/mol, con medias recalculadas en la misma escena (0,2→0,178; 0,556→0,533; 0,725→0,670).
- `S2_modelos_calibracion/M06_libreto.md:172`: «nivel nominal de 90 nmol/mol» pasa a «94 nmol/mol».
- `S3_comparacion_decision/M10_libreto.md:195` (entrada de referencias ISO 17025): «§§7.1.3, 7.6, 7.8.2, 7.8.4 y 7.8.6.1–7.8.6.2» pasa a «§§7.1.3, 7.6, 7.8.4.1 a)–c) y e), y 7.8.6.1–7.8.6.2 … (PDF p. 24 para §7.8.4.1)».
No hay copia previa (`curso/versiones/` no existe), así que no puedo confirmar si estos cambios son anteriores a la unificación. Lo que sí consta es que ninguno está en los logs de unificación, que solo describen cambios de claves. Propuesta: confirmar con el autor de esos cambios (sesiones previas de corrección) y, si no están verificados, revertirlos. No es decisión de este revisor.
El cambio de M05:309 (DAE 10.ª 2020 → 9.ª 2017) sí está documentado y verificado; no se incluye aquí.

**U-03 (media). El recuento de «no disponible en docs/» no coincide.**
Contado por ocurrencia con la misma expresión (`no disponibles? en `?docs/`?`, sin distinguir mayúsculas):

| Libreto | Declarado | Contado |
|---|---|---|
| M01 | 1 | 2 |
| M04 | 7 | 8 |
| M10 | 1 | 2 |
| M13 | 5 | 8 |
| AX | 4 | 7 |
| Resto | igual | igual |
| **Total** | **60** | **69** |

Propuesta: corregir la tabla y el total de `unificacion_claves.md` a 69, o explicar qué criterio distinto se aplicó. El «antes 64» no se puede comprobar sin copia previa.

**U-04 (media). Claves en corchetes que no están en `inventario.md`.**
- Searle, Casella y McCulloch: M06:235, :237 (y referencia :299).
- Efron y Tibshirani 1993: M13:116, :130 (referencia :271).
- Huber 1981: M13:150, :158, :180 (referencia :272).
- CIPM MRA-G-13: M08:11, :241, :290 (referencia :335).
- ILAC-P14: M08:290 (referencia :342).
- CALAIRE R&R: M06:221 (referencia :296).
- F-PSMT-01: M05:64, M07:214 (referencia en M05:307, M07:368, M08:337).
- Johnson, Kotz y Balakrishnan: M05:174 (cita completa en corchete, sin clave).
Propuesta: añadir filas a `inventario.md` (con «no disponible en docs/» cuando proceda), siguiendo su regla 2, o marcar explícitamente las fuentes internas (CALAIRE R&R, F-PSMT-01) como datos propios fuera del catálogo.

**U-05 (media). Variantes de una misma clave sin unificar.**
- `EPA TAD §4.4.1` (M05:86) frente a `EPA-TAD` (inventario; M10:105). Mismo problema en la tabla M05:82 («EPA TAD»), que no es corchete.
- `SRP QAPP` y `SRP SOP` (M05:84, :86, :271) frente a `SRP-QAPP` y `SRP-SOP` (inventario; M09:209; M10:103).
- `Milton et al. 2006` (M04:250, :254, :256) frente a `Milton 2006` (inventario).
- `ISO/IEC 17025 §7.2.2` (M05:90, :164) frente a `ISO 17025` (clave del inventario; alias `ISO/IEC 17025`). Baja.
- `JCGM 106:2012` y `ILAC-G8:09/2019` (AX:245, :251, :257) frente a `JCGM 106` e `ILAC-G8` (inventario). La edición va en la referencia, no en la clave. Baja.
- Calificador de Montgomery 2013: «(contenido no cotejado)» en M11:31 y :122, frente a «, clave bibliográfica; contenido no cotejado» en el resto. Baja.
Propuesta: usar en corchetes las claves del inventario (`EPA-TAD`, `SRP-QAPP`, `SRP-SOP`, `Milton 2006`, `ISO 17025`, `JCGM 106`, `ILAC-G8`) y un único calificador para Montgomery 2013.

**U-06 (baja). `guia_libreto.md` §5 no recoge Montgomery.**
La tabla «Claves bibliográficas» (líneas 85–118) no incluye ni Montgomery 2013 ni Montgomery DAE; solo la prosa de la línea 120 menciona «Montgomery, *Introduction to Statistical Quality Control*». Tampoco recoge las claves de U-04. Propuesta: añadir las dos filas de Montgomery con su estado («no disponible en docs/»), o remitir explícitamente al inventario.

## Resultado

**No aprobado con observaciones.**

- Las claves de la unificación están bien aplicadas en lo esencial: Crowder2020, Hahs-Vaughn y Lomax, y la separación Montgomery 2013 / DAE son correctas, y M05:309 coincide con la bibliografía de Crowder.
- Pero el registro de unificación no describe fielmente M06:219 (U-01), el recuento de «no disponible en docs/» está mal (U-03: 69, no 60), y el diff contiene cambios de cifras y datos (U-02) que no están en el registro. Hay que resolver U-01 y U-02 antes de dar la unificación por cerrada.
- Las variantes y claves faltantes (U-04 a U-06) son de consistencia y no afectan a cifras.
