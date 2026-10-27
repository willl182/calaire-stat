# Verificación final acotada — S1 Fundamentos (Haiku 5.5)

Fecha: 2026-10-27. Alcance: decisiones de `S1_decisiones_luna.md` (H-01–H-18, S-01), `S1_cotejo.md`, `S1_inventario.md`, `S1_ocurrencias.tsv` y los libretos `curso/S1_fundamentos/M00–M04_libreto.md` en su estado actual. No se ha repetido la revisión completa ni se han revisado ejercicios. No se ha editado ningún libreto, ejercicio, inventario ni cotejo. No hay commits.

Este archivo sustituye como referencia a `S1_revision_haiku.md`, que queda superado: su H-01 («crítica») está rechazado por decisión del supervisor, y cita localizadores y decisiones (D-07, D-10) que ya no existen en el registro actual.

## 1. Resumen

- **El TSV es correcto.** Regenerado con `python3 -I curso/citas/_extrae_s1.py` desde la raíz del repo: 184 filas, idéntico a `S1_ocurrencias.tsv`. El enlace del inventario al TSV existe.
- **S-01 (M01 líneas 156 y 180) está bien aplicada.** Se retira la causa no comprobada; se conservan cifras, fórmulas y ejercicios.
- **Las páginas directas están confirmadas.** ASQ: PDF 605 contiene «coefficient of variation» y pie «572 Appendix C»; PDF 598 no contiene la entrada. EN 14625: PDF 20 contiene «NOTE nmol/mol = ppb» y pie impreso 18.
- **Hay tres problemas graves de integridad del registro:** (F-01) la tabla literal del inventario no coincide con el TSV; (F-02) dos correcciones declaradas como aplicadas no están en M04; (F-03) las huellas SHA-256 de M00, M02, M03 y M04 no coinciden con los archivos actuales.
- **Los estados del cotejo no son todos coherentes** con el inventario ni con la regla de grupos (F-04 a F-08).

## 2. Decisiones H-01–H-18 y S-01: coherencia

| Ítem | Decisión | Estado en texto | Coherente |
|---|---|---|---|
| S-01 | Quitar causa redondeo/constantes | M01 156 y 180: «no se determina la causa»; cifras intactas (1,147/1,1329 = 1,012446; 308,32/304,39 = 1,012911; cocientes 268,81 y 268,68) | Sí |
| H-01 | Rechazado; prácticas B/I/A se conservan | M00 conserva las tres prácticas; sin marcadores de fase; «R03» es registro simulado explícito | Sí (ver F-07 sobre su estado en el cotejo) |
| H-02 | Ficha separa localizadores verificados y parciales | M02 línea 14 | Sí |
| H-03 | Crowder limitado a §4.3 | M02 82/86 con nota de alcance; 106/110/140 sin atribución Crowder | Sí |
| H-04 | Definiciones NIST sin pasaje, marcadas | M02 150/164 sin corchete NIST; el cotejo aún las lista en filas de línea distintas (F-03) | Sí, con F-03 |
| H-05 | Nota de proceso retirada; cita §9.1.1 | Nota retirada (0 coincidencias). La cita §9.1.1 no aparece como corchete en M03 | Parcial (ver F-02) |
| H-06 | G\*Power atribuido a Hahs-Vaughn §6.5 | No hay ninguna mención a G\*Power en M04 | **No** (F-02) |
| H-07 | Versión statsmodels 0.15.0 y contraste con `scipy.stats.nct` | No hay mención a 0.15.0 ni a `scipy.stats.nct` en M04 | **No** (F-02) |
| H-08 | D-10: Welch §7.1.3.2 correcto | D-10 no existe en el registro actual; el registro usa solo H-xx | Sin efecto; la revisión anterior es obsoleta |
| H-09 | Bonferroni: separar NIST, statsmodels y deducción | M04 226–232: «no requiere independencia… deducción de la cota de la unión, no atribuida aquí a NIST»; `multipletests` citado | Sí |
| H-10 | GUM B.2.9 y GUM-6 §6.1 conservadas; VIM marcada | M01 línea 24: VIM «remitido por GUM-6 §5.1; VIM no disponible en docs/» | Sí (ver F-05 sobre el estado en inventario) |
| H-11 | ASQ: p. impresa 572, PDF 605 | M02 líneas 74/189: «p. impresa 572 (PDF p…)»; comprobado directamente en PDF 605 | Sí |
| H-12 | GUM 4.3.3, G.3.2, F.1.1.3 con alcances | M03 con alcances en referencias | Sí en texto; **estados** en F-06 |
| H-13 | GUM E.4.3 (E.7) | M04 160/164/172–176 | Sí |
| H-14 | GUM-S2 §3.20 nota 4; §3.21 nota 4 | M03 276 y referencias | Sí |
| H-15 | AX.2 y AX.3 en referencias M03 | M03 líneas 375–376 de la lista (sección de referencias) | Sí |
| H-16 | Autocorrelación: consulta web, no PDF | M03 373: «consultada en línea el 2026-10-27; no está en docs/» | Sí |
| H-17 | M01 línea 64 localiza CFR50-D §4.5.3.10 ec. 4 | M01 línea 64: «CFR50-D §§4.1, 4.5.2.5 y 4.5.3.10» | Sí (D-07 ya no existe como registro) |
| H-18 | EN 14625 PDF 20 / impresa 18 | M00 línea 36 sin localizador de página; cotejo y inventario lo registran | Sí (verificado en PDF) |

## 3. Hallazgos

### F-01 · alta · `S1_inventario.md`, tabla «Ocurrencias literales por capítulo»
- **Hallazgo:** la tabla dice que cada fila es una ocurrencia detectada por `_extrae_s1.py` y que «el campo literal conserva el texto íntegro». No es así. De 35 filas, 30 no coinciden con el TSV en la misma línea y literal (p. ej. M00 línea 30: inventario `[GUM B.2.19]`, TSV `[GUM B.2.19; prop_e §3, convención curricular]`; M01 línea 18: inventario `[GUM-6 §§5.1, 6.1]`, TSV `[VIM, sin numeral; GUM-6 5.1–5.2]`; M00 línea 155 y M01 línea 148 no existen en el TSV en esa línea). Solo 5 coinciden. La tabla cubre M00 y M01 y no tiene filas para M02–M04; las 184 ocurrencias no están en la tabla.
- **Evidencia:** comparación automática fila a fila entre la tabla y el TSV.
- **Propuesta:** regenerar la tabla desde el TSV (o sustituirla por un enlace al TSV como fuente única) y eliminar la frase «conserva el texto íntegro» hasta que sea cierta.

### F-02 · alta · M04 (H-06, H-07) y M03 (H-05); registros `S1_cotejo.md` y `S1_decisiones_luna.md`
- **Hallazgo:** las decisiones declaran aplicados cambios que no aparecen en los libretos:
  - H-06: no hay ninguna mención a G\*Power en M04 (`grep -i "g\*power\|power using"` vacío). La fila de cotejo «150 · G\*Power, Hahs-Vaughn §6.5 · verificada» describe texto que no existe.
  - H-07: no hay «0.15.0» ni `scipy.stats.nct` en M04. La fila de cotejo «138–164 · statsmodels/SciPy · verificada» describe una frase ausente.
  - H-05: la cita a Hahs-Vaughn §9.1.1 para la construcción chi-cuadrado no aparece como corchete en M03 (solo en prosa).
- **Propuesta:** decidir si estos cambios se perdieron en una edición paralela o si las decisiones son incorrectas. Si el libreto debe conservarlos, reaplicar; si no, retirar las filas de cotejo y las decisiones. No hay una corrección que aplicar en este paso.

### F-03 · alta · huellas SHA-256 y líneas de referencia (`S1_inventario.md`, «Huellas»)
- **Hallazgo:** solo M01 coincide con la huella registrada. No coinciden M00, M02, M03 ni M04:

| Archivo | Huella registrada | Huella actual |
|---|---|---|
| M00 | `4ca1223b…ebefc` | `4df8a520…2c697969` |
| M02 | `c2f3104b…07de71` | `048650a8…3dd73125` |
| M03 | `ab775192…33e0a` | `01191164…7f615` |
| M04 | `63d29724…bc0be6` | `837c2128…241851d` |

  Las líneas de cotejo e inventario también han derivado. Ejemplos: el cotejo sitúa la nota G\*Power en M04:150 y la versión statsmodels en M04:233, pero no existen en esas líneas. El cambio de M00 por prácticas paralelas es admisible; el de M02–M04 no está explicado.
- **Propuesta:** tras congelar el texto, recalcular las huellas y revalidar cada línea de cotejo; la regla del propio inventario exige hacerlo.

### F-04 · media · Lakens (`S1_cotejo.md` M04 198–206; `S1_inventario.md` catálogo y URL)
- **Hallazgo:** el cotejo marca Lakens 2017 como «no verificable» (sin pasaje ni fecha archivados). El catálogo del inventario y su tabla de URL lo marcan como «verificada con límite». Son estados contradictorios para la misma fuente.
- **Propuesta:** dejar «no verificable» (el cotejo tiene la evidencia más completa) y corregir el inventario.

### F-05 · media · M01 líneas 24 y 156 (`S1_inventario.md`)
- **Hallazgo:** el inventario marca `[GUM-6 §5.1; VIM 2.3]` (línea 24) y `[VIM 2.3]` como «verificada» en la línea 24, y la línea 156 como «verificada». El cotejo marca el grupo GUM-6 §5.1 / VIM 2.3 como «no verificable» (VIM primario no está en `docs/`) y la línea 156 como «corregida».
- **Propuesta:** alinear el inventario con el cotejo: grupo de VIM «no verificable» y línea 156 «corregida».

### F-06 · media · estados de grupo en el cotejo
- **M03 110 (GUM G.3.2–G.3.4):** el cotejo dice «verificada», pero solo se ha comprobado G.3.2 (t de Student). G.3.3 y G.3.4 no están comprobadas. El estado de grupo debe ser «no verificable» o separarse.
- **M03 106/108/266 (GUM F.1.1.3):** marcada «verificada», pero H-12 limita el alcance a apoyo cualitativo. Debe decir «apoyo cualitativo», no «verificada».
- **M03 18–74 (MMU §§3.2.1, 3.2.3–3.2.5.2):** marcada «verificada», pero en este lote solo se ha comprobado §3.2.5.2 (triangular). Ver también §4 de este informe.
- **M04 184–186, 279 (Otto §2.2):** marcada «no verificable». Este lote sí confirma Tablas 2.10 (Q = 0,59) y 2.11 (T = 2,22) y la convención unilateral de Grubbs. El cotejo debe registrar esa verificación parcial, sin subir el grupo a «verificada».
- **Propuesta:** en todos los casos, el estado de grupo es «verificada» solo si cada afirmación del grupo está comprobada; si no, «no verificable» con la parte comprobada descrita.

### F-07 · baja-media · M00 prácticas B/I/A en `S1_cotejo.md` (filas 88–115, 192–213, 259–278)
- **Hallazgo:** el cotejo marca «verificada» un bloque que no es una cita bibliográfica. Es contenido didáctico autorizado (H-01). Declarar «verificada» confunde la cobertura de citas con la aprobación de contenido.
- **Propuesta:** marcar esas filas como «no aplica (contenido didáctico autorizado; sin cita externa)».

### F-08 · baja · vocabulario de estados en `S1_inventario.md`
- **Hallazgo:** la decisión dice que solo existen «verificada», «corregida» y «no verificable». El inventario usa además «Parcialmente verificada» (ISO 28037, Milton), «Verificada/corregida en pasajes concretos» (Crowder), «Solo pasajes delimitados» (NIST) y «Verificada por pasajes; … no verificable» (Hahs-Vaughn).
- **Propuesta:** normalizar a los tres estados; el alcance parcial va en la columna de evidencia.

### F-09 · baja · `S1_revision_haiku.md` (obsoleto)
- **Hallazgo:** su H-01 («crítica»), su H-11 (rechazo del cambio ASQ en sentido contrario) y su mención a D-07/D-10 ya no reflejan el registro. No debe usarse como autoridad.
- **Propuesta:** marcarlo como superado por este informe y por `S1_decisiones_luna.md`.

## 4. Cobertura literal S1

- **TSV:** 184 ocurrencias, completas (archivo, línea, literal sin truncar). Coincide con el extractor. He comprobado que no hay corchetes con marcadores de cita fuera del patrón del extractor (búsqueda de `§` o números de dos cifras fuera de las claves reconocidas: sin resultados).
- **Tabla literal del inventario:** no cubre el TSV (F-01).
- **Cobertura temática del cotejo:** agrupada por clave, no por ocurrencia. Es admisible siempre que el grupo no se declare verificado si no lo está (F-06).

## 5. Diferencias de alcance pendientes (no reverificadas en este paso)

- MMU §§3.2.1 y 3.2.3–3.2.4 (M03 18–74): no comprobadas en este lote.
- GUM G.3.3 y G.3.4 (M03 110): no comprobadas.
- Otto §2.2 tablas no tabulares y §§ de prueba: no revisadas en detalle.
- Autocorrelación NIST (M03) y Lakens (M04): solo registro web, no recomprobadas.
- VIM 2.3: sin fuente primaria en `docs/`; la remisión por GUM-6 §5.1 es el único soporte.
- Hahs-Vaughn §§5.2, 6.4–6.5 (G\*Power), 7.8, 9.2: no revisadas línea a línea en esta verificación (G\*Power solo se contrastó en el lote anterior).
- Las huellas y las líneas de cotejo deben recalcularse tras cualquier cambio posterior (F-03).

## 6. Resultado

- **Verificado en este paso:** TSV completo y reproducible; S-01 aplicada; ASQ PDF 605 y EN 14625 PDF 20; H-02, H-03, H-05 (nota retirada), H-09, H-10, H-11, H-15, H-16, H-17, H-18; H-01 rechazado y coherente con M00.
- **Incoherente:** H-06 y H-07 (F-02); tabla literal del inventario (F-01); huellas de M00, M02, M03 y M04 (F-03).
- **No se ha declarado globalmente verificado ningún grupo** que solo tenga título o comprobación parcial; los casos están en F-04 y F-06.
