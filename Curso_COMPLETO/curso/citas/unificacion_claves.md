# Unificación de claves bibliográficas entre libretos

Alcance: `curso/S*/M*_libreto.md` y `curso/S4_numericos_integracion/AX_libreto.md` (no se tocan `versiones/` ni `auditoria_*`). Clave final según `curso/citas/inventario.md`.

No se cambió ningún numeral verificado, cifra ni ejercicio. No se añadió ninguna página nueva.

## Tabla de variantes

| Variante encontrada | Clave final | Archivos:líneas (tras el cambio) |
|---|---|---|
| Montgomery, *Design and Analysis of Experiments* (no disponible en docs/) | Montgomery DAE (no disponible en docs/; contenido no cotejado) | M05_libreto.md:26, 30, 32, 44 (×2), 52, 58, 128, 138 (×2), 164, 168, 251 |
| Montgomery, *Design and Analysis of Experiments*. 10.ª ed., Wiley, 2020 (entrada bibliográfica) | Montgomery DAE: 9.ª ed., Wiley, 2017, según bibliografía de Crowder 2020 | M05_libreto.md:309 |
| Montgomery 2013, no disponible en docs/ (corchete propio) | Montgomery 2013, clave bibliográfica; contenido no cotejado | S4_numericos_integracion/AX_libreto.md:299, 309, 315 |
| Montgomery 2013, clave bibliográfica; contenido no cotejado (acompaña otra cita) | Montgomery 2013 (contenido no cotejado) | S3_comparacion_decision/M11_libreto.md:31, 122 |
| Hahs-Vaughn y Lomax (en corchete) | Hahs-Vaughn | M05_libreto.md:168 |
| Crowder2020 (sin espacio) | Crowder 2020 | AX_libreto.md:12, 107, 133, 139, 365 |

Sin cambios necesarios:

- **GUM-S1 / JCGM 101:2008** y **GUM-S2 / JCGM 102:2011**: en los libretos la forma `JCGM 101`/`JCGM 102` solo aparece en la entrada de referencias (M13:268–269, AX:360), junto a la clave `GUM-S1`/`GUM-S2`. En corchetes siempre se usa `GUM-S1 …`/`GUM-S2 …`. No hay variante que cambiar.
- **Hahs-Vaughn y Lomax** en entradas de referencias (M03:368, M04:284, M06:297, M07:365, M11:280, AX:364, M05:299): es la descripción completa de la obra, no una clave en corchete. Se dejó.
- **Montgomery 2013** en `M11_libreto.md:15, 196, 208, 282` (tabla, prosa y entrada de referencia): no es corchete; se dejó. M11:196 tiene la frase «Montgomery 2013 queda solo como clave bibliográfica…» dentro de un corchete de prosa; no se reescribió.

## Entradas nuevas o cambiadas en inventario y referencias

- `curso/citas/inventario.md`: fila nueva **Montgomery DAE** y regla 3 reescrita (dos obras, dos claves).
- Edición y año de la obra DAE: la bibliografía de Crowder 2020 (`curso/citas/extractos/S3_crowder2020_completo.txt`, PDF `docs/Introduction to Statistics in Metrology.pdf`) cita «Design and Analysis of Experiments, 9th edn. Wiley, New York (2017)». **M05:309 decía «10.ª ed., 2020», que no consta en `docs/`; se sustituyó por 9.ª ed., 2017.** Pendiente de cotejo directo del ejemplar; sin numeral.

## Recuento de «no disponible en docs/» por libreto (tras el cambio)

| Libreto | Marcas |
|---|---|
Recuento con `grep -ci 'no disponibles\? en .\?docs/'` (líneas que contienen la marca), sobre `curso/S*/M*_libreto.md` y `AX_libreto.md`; `guia_libreto.md` no es libreto y queda fuera.

| Libreto | Líneas con marca (`grep -ci`) | Ocurrencias (`grep -oi \| wc -l`) |
|---|---|---|
| S1 M00 | 0 | 0 |
| S1 M01 | 2 | 2 |
| S1 M02 | 1 | 1 |
| S1 M03 | 3 | 3 |
| S1 M04 | 7 | 8 |
| S2 M05 | 16 | 19 |
| S2 M06 | 8 | 8 |
| S2 M07 | 2 | 2 |
| S2 M08 | 5 | 6 |
| S3 M09 | 0 | 0 |
| S3 M10 | 2 | 2 |
| S3 M11 | 1 | 1 |
| S3 M12 | 2 | 2 |
| S4 M13 | 8 | 8 |
| S4 AX | 6 | 7 |
| **Total** | **63** | **69** |

Corregido tras la revisión U-03: la tabla anterior daba 60 líneas y no coincidía con el conteo. Las cifras «antes» (64, 20, 7) no se pueden comprobar sin copia previa. El recuento cuenta marcas de forma textual; no comprueba que el documento falte en `docs/`.

## Respuesta a la revisión

Respuesta del ejecutor a `curso/citas/unificacion_revision_haiku.md`. Solo se tocan los puntos indicados por el supervisor; cifras y ejercicios no se modifican.

| U | decisión | evidencia |
|---|---|---|
| U-01 | **Hecho.** M06:219 vuelve a citar NIST/SEMATECH §7.4.7.3 con el mismo texto y URL de HEAD, seguida de Hahs-Vaughn §8.2.1, PDF p. 332, en el mismo corchete separado por «;». La entrada de la tabla de variantes ya no describe M06:219 como cambio de clave: es restauración de la fuente, más apoyo general. | `git show HEAD:curso/S2_modelos_calibracion/M06_libreto.md` (línea 219, cita NIST); M06:219 actual; `grep -c NIST` en M06 = 1. La página PDF 332 para Hahs-Vaughn la confirmó la revisión; no se reverificó en esta sesión. |
| U-02 | **Fuera de alcance.** No se ha actuado. Los cambios de cifras en M02:186/188, M06:172 y M10:195 quedan para el supervisor de prácticas y no están en el cotejo. | Instrucción del supervisor. Sin cambios en esos archivos desde esta sesión. |
| U-03 | **Hecho.** Recuento recalculado con `grep -ci` por libreto y la tabla corregida: 63 líneas con marca (69 ocurrencias). El total de 60 se retira. | Salida de `grep -ci 'no disponibles\? en .\?docs/'` sobre S*/M*_libreto.md y AX_libreto.md. La revisión daba 69 como total de ocurrencias; la coincidencia es de total, no fila a fila (M05: 16 líneas, 19 ocurrencias). |
| U-04 | **Parcial.** Añadidas a `inventario.md` las filas Searle–Casella–McCulloch y Efron–Tibshirani 1993, marcadas «no disponible en `docs/`» y sin edición, editorial ni numeral no consignados. Pendientes (no señalados por el supervisor): Huber 1981, CIPM MRA-G-13, ILAC-P14, CALAIRE R&R, F-PSMT-01, Johnson, Kotz y Balakrishnan. | Ningún archivo en `docs/` con esos nombres. El extracto de Crowder cita «Searle and Gruber (2016), *Linear Models*»: es otra obra, no la de Searle, Casella y McCulloch. |
| U-05 | **Parcial.** En corchetes de M05:84, :86 y :271: `EPA TAD` → `EPA-TAD`, `SRP QAPP` → `SRP-QAPP`, `SRP SOP` → `SRP-SOP`. Sin tocar tablas (M05:14, :82) ni prosa de esas mismas líneas. Pendientes: Milton et al. 2006, ISO/IEC 17025 §7.2.2, JCGM 106:2012, ILAC-G8:09/2019 y calificador de Montgomery 2013 (no señalados por el supervisor). | `grep` de corchetes con esas claves antes y después del cambio. |
| U-06 | **Hecho.** `guia_libreto.md` §5 incluye filas para Montgomery 2013, Montgomery DAE (9.ª ed., Wiley, 2017), Searle–Casella–McCulloch y Efron–Tibshirani 1993, con «no disponible» en la columna de archivo. | Montgomery DAE: `curso/citas/extractos/S3_crowder2020_completo.txt` líneas 10198 y 14919 (bibliografía de Crowder; PDF `docs/Introduction to Statistics in Metrology.pdf`). Searle y Efron: sin archivo en `docs/`. |

Sin commits. Quedan abiertos U-02 (fuera de alcance) y los pendientes marcados en U-04 y U-05.
