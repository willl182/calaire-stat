# Revisión de citas — S2 Modelos y calibración (M05–M08)

Fecha: 2026-10-27. Revisor: Haiku (revisión independiente del cotejo de S2).
Alcance: cobertura de todas las ocurrencias de `S2_inventario.md`, `S2_cotejo.md` y `S2_decisiones_luna.md`, con comprobación de edición, numeral y pasaje contra los PDF de `docs/` (texto extraído con `pdftotext -layout` en `/tmp`). No se confió en estados ni en revisiones previas. No se revisaron ejercicios, prácticas ni cifras de los libretos, que cambian por otra supervisión; las líneas del inventario están desplazadas y se citan las líneas actuales.

Este archivo es el único escrito. No se editaron libretos, bitácoras, inventarios, cotejos ni decisiones, y no se hizo commit.

## Alarmas del supervisor

**Ambas alarmas están confirmadas.** Las dos correcciones actuales son falsas y deben revertirse antes de dar S2 por cerrado.

### H-01 · alta · Corrección falsa: Hahs-Vaughn cap. 6 sí trata potencia

- **Archivos:** `S2_decisiones_luna.md` decisión 2 y decisión 3; `S2_cotejo.md` filas «M05:32/34/48», «M05:156, 160, 162 y referencia final M05:248» (fe de erratas); `M05_libreto.md:166`, `:170`, `:172` (cita a §9.3), `:289` (referencia final).
- **Evidencia:** el PDF completo `docs/Statistical Concepts – A First Course.pdf` (texto en `hv.txt`) tiene en su índice del capítulo 6: «6.1.2 Sample Size», «6.1.3 Power», «6.1.4 Effect Size», «6.5 Power Using G*Power». El cuerpo lo confirma: `6.1.3 Power` (línea 10436), «6.5 Power Using G*Power… one-sample t test» (línea 11712). Cap. 9 también tiene potencia (§9.3, línea 18488), pero en el contexto de varianzas. La afirmación «el capítulo 6 no trata potencia» es falsa. `S1` lo verificó bien.
- **Corrección:**
  1. Restaurar en el cotejo la verificación de §§6.1.3–6.1.4 y §6.5 para potencia de una media. Retirar «no trata potencia» de la fe de erratas y de las decisiones 2 y 3.
  2. En `M05_libreto.md:166` y `:172`, la potencia de una muestra y el cálculo de potencia deben apoyarse en §6.1.3/§6.5. §9.3 puede mantenerse solo como localizador adicional de tamaño de efecto y potencia en contexto de varianzas.
  3. En la referencia final `M05_libreto.md:289`, citar los dos capítulos y ajustar la descripción.
  4. Estos cambios deben hacerse en el libreto y en la bitácora de forma coherente. Como los libretos están bajo otra supervisión, dejo la edición a esa supervisión.

### H-02 · alta · Rechazo falso: EPA TAD §4.4.1 sí sustenta tres ciclos y seis puntos

- **Archivos:** `M05_libreto.md:86` («El EPA TAD §4.4.1 no se usa aquí como respaldo de un número de ciclos o puntos, porque ese pasaje no sustenta el esquema»); `S2_cotejo.md` fe de erratas («M05:86 — EPA TAD §4.4.1 | corregida»); `S2_decisiones_luna.md` decisión 2.
- **Evidencia:** `docs/o3_tad_508_20230906_final.pdf`, §4.4.1 «Verification Requirements» (texto en `tad.txt`, línea 1323): «A verification consists of a minimum of three (3) stable testing cycles, each cycle consisting of a zero and at least six (6) upscale concentration points.» Línea 1423: «Run at least three (3) complete cycles consisting of six (6) concentration points… and a zero.» Requisitos: pendiente 1,00 ± 0,03; intercepto 0 ± 3 ppb; SD de pendientes < 0,0075; SD de interceptos < 1,00 ppb. Además, el documento indica que se aplica a transferencia de Level 2 y Level 3 (líneas 1168–1171). `S3_revision_haiku.md:127` lo cotejó bien. Además, `docs/srp_qapp.pdf` §6.2.2 (línea 580 y siguientes) dice que la comparación SRP–Level 2 consta de «a minimum… three cycles», cada uno con seis puntos de concentración y cero. El libreto contradice al QAPP y al propio TAD.
- **Corrección:**
  1. Revertir la frase de `M05_libreto.md:86`. Redactarla así: el EPA TAD §4.4.1 exige, para verificar estándares de transferencia de Level 2 y Level 3, al menos tres ciclos estables, cada uno con cero y al menos seis puntos ascendentes, con los criterios de pendiente, intercepto y dispersión entre ciclos. Puede añadirse que el SRP QAPP §6.2.2 describe el mismo esquema para la comparación SRP–Level 2.
  2. Retirar la marca «corregida» de la fe de erratas y de la decisión 2 del cotejo. El estado correcto es verificada, con alcance a verificación de Level 2/3.
  3. Mantener la precisión de que el TAD es una guía de verificación, no la norma de CALAIRE.

## Hallazgos de cobertura y precisión

### H-03 · media · Cita en texto sin entrada en la bibliografía final

- **Archivos:** `M06_libreto.md:210` cita «NIST/SEMATECH, «Bonferroni's method», §7.4.7.3, https://itl.nist.gov/…/prc473.htm (consultado 2026-10-27)». La sección «Referencias del capítulo» de M06 (desde la línea 276) no tiene ninguna entrada NIST/SEMATECH. `S2_inventario.md` la registra como ocurrencia de cuerpo/ficha, y `S2_cotejo.md` la marca «verificada con evidencia web no archivada».
- **Evidencia:** búsqueda de «NIST», «SEMATECH» e «itl.nist» en `M06_libreto.md`: una sola coincidencia, la del cuerpo (línea 210). La guía (§5, «Referencias del capítulo») exige la cita completa de cada clave usada.
- **Corrección:** añadir a las referencias del capítulo de M06: «NIST/SEMATECH, *e-Handbook of Statistical Methods*, §7.4.7.3, «Bonferroni's method», consultado el 2026-10-27; no disponible en `docs/`; evidencia web no archivada». No es necesario añadir numeral no comprobado.

### H-04 · media · Localizador de Hahs-Vaughn §9.3 aplicado a distribución t no central

- **Archivo:** `M05_libreto.md:172`: «[Hahs-Vaughn §9.3; distribución t no central: Johnson, Kotz y Balakrishnan…]» aplicado al cálculo de potencia de una media con `d−1` grados de libertad y parámetro de no centralidad `Δ√d/√(τ²+σ²/n)`.
- **Evidencia:** en `hv.txt`, §9.3 (línea 18488) pertenece al cap. 9, «Inferences About Variances», y trata potencia para pruebas de varianza. Para la potencia de una media, el texto aplicable es §6.1.3 y §6.5 (ver H-01). Ningún pasaje leído de Hahs-Vaughn describe la t no central para una media. Johnson–Kotz–Balakrishnan no está en `docs/`.
- **Corrección:** cambiar el localizador de la potencia de una media a Hahs-Vaughn §6.1.3/§6.5. Mantener la frase sobre t no central como «no verificable en docs/», sin atribuirla a §9.3.

### H-05 · baja · Restricción de rango: la cita existe, pero la frase del libreto va más allá del texto

- **Archivo:** `M07_libreto.md:41`: «R² puede aumentar simplemente porque se amplía el intervalo de x… [Hahs-Vaughn §10.1.1.5.2, restricción del intervalo]». `S2_cotejo.md` lo marca como «no verificable en el pasaje preciso».
- **Evidencia:** el encabezado «10.1.1.5.2 Restriction of Range» existe (`hv.txt`, línea 20383). El texto dice que si se restringe el rango de una variable, la magnitud de la correlación «will usually be reduced» (ejemplo GRE/GGPA: r = 0,60 baja a 0,20). Así que el pasaje sostiene que el rango restringido reduce la correlación, y la afirmación del libreto es su inversa lógica. No dice que R² aumente al ampliar el rango ni habla de R² en calibración.
- **Corrección:** cambiar el cotejo de «no verificable» a «verificada parcialmente: restricción del rango reduce la correlación». En el libreto, reformular como consecuencia: «si el rango de x se restringe, la correlación baja; al ampliarlo, la correlación tiende a subir», citando el pasaje, y dejar la afirmación sobre R² como consecuencia del modelo o de Otto §6.1, ec. (6.17).

### H-06 · baja · Descripción de ISO 6143 §5.2.2 en el cotejo no coincide con el encabezado

- **Archivo:** `S2_cotejo.md`, sección M07, fila «ISO 6143 §5.2.2» («selección/comparación de mezclas de calibración»; también la fila de la fe de erratas «ISO 6143 §5.2.2 — extracción líneas 784–819: comparación punto a punto»).
- **Evidencia:** `docs/ISO 6143 2001.pdf`, línea 784 de `iso6143.txt`: el encabezado es «5.2.2 Validation of the response model». El texto valida si la función de respuesta es compatible con los datos de calibración, con ajuste punto por punto por un test. Sí incluye comparación punto a punto, pero no «selección de mezclas».
- **Corrección:** corregir la descripción en el cotejo a «validación del modelo de respuesta; ajuste punto por punto». No cambia el uso que hace el libreto, que es de apoyo contextual.

### H-07 · baja · Cotejo basado en líneas de inventario obsoletas

- **Archivos:** `S2_inventario.md` y `S2_cotejo.md` citan líneas que ya no corresponden a los libretos. Ejemplos verificados: `M05` ancla 86 contiene ahora la frase del TAD, y `M05:166–172` contiene la potencia de Hahs-Vaughn (no en la línea 156/160/162 del inventario). `M07:41` tiene la restricción de rango. Como los libretos siguen cambiando, cualquier verificación basada en líneas puede quedar desalineada.
- **Corrección:** antes de dar el cotejo por cerrado, regenerar las anclas de línea a partir del texto vigente, o anclarlas por cita textual y no por número de línea.

### H-08 · baja · Nombre del autor de MMU inconsistente entre capítulos

- **Archivos:** `M06_libreto.md:288` (versión actual: «Rosario, P. P. N. do; Mendes, A.») frente a `M08_libreto.md` (sección de referencias: «Novellino do Rosario, P. P.; Mendes, A.»).
- **Evidencia:** la portada de `docs/Metrology and Measurement Uncertainty.pdf` (texto en `mmu.txt`, línea 1) da «Pedro Paulo Novellino do Rosario» y «Alexandre Mendes».
- **Corrección:** usar la forma de la portada, «Novellino do Rosario, P. P.; Mendes, A.», en M06 y M08. Verificar la edición e ISBN en la portada antes de cerrar.

## Estado por grupo de citas

| Grupo | Ocurrencias en libreto (corchetes) | Resultado de la revisión |
|---|---|---|
| M05 — SRP QAPP/SOP, EN 14625, ISO 13964, ISO 17025, Crowder §9.2/§9.3.1/tabla 9.9, GUM H.5, ISO 5725-3, Hahs-Vaughn, TAD | 62 | SRP SOP §9.7.19.12–.14 (mínimo de seis ciclos, 12 puntos), EN 14625 §8.4.7 (80/110 kPa, tres medidas), ISO 13964 §6.2.2 (cero y ≥5 concentraciones), QAPP §6.2.1/§6.2.2 (SRP #7 vs. Level 2), Crowder §9.2 y §9.3.1/tabla 9.9, GUM H.5.2.6 y ISO 5725-3 §6, §8, §9.5 y anexo B confirmados en su encabezado. **Errores:** H-01, H-02, H-04. |
| M06 — ISO 5725-2/-3/-4/-6, GUM H.5/G.4, Crowder §9.3.x, Hahs-Vaughn §8.2.1/§9.1, MMU, NIST | 88 | ISO 5725-3 §6.1/§8, Crowder §9.3.1–9.3.4 y GUM G.4 confirmados. ISO 5725-4 §5.5.2 existe. **Errores:** H-03 (NIST sin entrada), H-08 (autor MMU). |
| M07 — Crowder cap. 10, Otto §6.1 (ec. 6.17, tabla 6.1, ec. 6.20), ISO 28037 §5.7/§5.8.1/§6.1.3/§10.3/§11.1, ISO 6143 §5.2.2, Hahs-Vaughn §10.1 | 101 | Crowder §10.1.2, §10.2.1, §10.2.3, §10.3.1–3, §10.4.1 confirmados por encabezado. Otto eq. (6.17) y (6.20), y tabla 6.1 confirmados. ISO 28037 §5.8.1, §6.1.3 (peso 1/u), §11.1 confirmados; §5.7 es predicción/uso, no define el signo, como dice el cotejo. **Errores:** H-05 (rango), H-06 (ISO 6143). |
| M08 — GUM §§4.1–4.3, 5.1–5.2, 6.2–6.3, G.3–G.6.5; GUM-6 §8.4, §11.2–11.4, F.2 (eq. 47); Crowder caps. 6–7; MMU caps. 5–6; ISO 28037 §11.1.1–11.1.3; CIPM/ILAC | 107 | GUM 4.3.10, G.3, G.6.5 y GUM-6 F.2 eq. (47) y §11.4 existen en el PDF. Crowder cap. 6 (§6.2.2–6.2.5) y cap. 7 (§7.2–7.7) confirmados por encabezado. MMU §4.4, §5.2.2, §5.3.1, §6.1 confirmados como encabezados del índice. **Pendiente:** contenido de esos pasajes no leído para M08 (ver limitaciones). |

Cobertura de fichas y referencias: M05, M06, M07 y M08 tienen sección «Referencias del capítulo». M06 no tiene entrada para NIST/SEMATECH (H-03). M07 y M08 tienen las claves de la guía (`guia_libreto.md` §5) con archivo. Los nombres de archivo de M05 y M06 coinciden con los de `docs/`, salvo que el texto de la guía use el nombre sin la forma final.

## Limitaciones aceptables (no son hallazgos)

Estas limitaciones son explícitas en el cotejo y no las considero errores si se mantienen tal cual:

- **Fuentes no disponibles en `docs/`:** VIM (JCGM 200:2012), Montgomery *Design and Analysis of Experiments*, Johnson–Kotz–Balakrishnan, Searle–Casella–McCulloch *Variance Components*, CIPM MRA-G-13, ILAC-P14. Se citan sin numeral y con la marca «(no disponible en docs/)». Correcto según la guía §5.
- **ISO 5725-1:1994:** el PDF local es solo el corrigendum 1:1998. Las definiciones de la Parte 1 quedan no verificables. Correcto.
- **NIST/SEMATECH en línea:** el contenido de la URL no está archivado en `docs/`. No puedo confirmarlo sin conexión. Se acepta como «consultado 2026-10-27, no archivado» (ver H-03).
- **Páginas impresas:** algunas páginas del cotejo (p. ej., GUM H.5.2.6 «pp. 101–102», G.4 «pp. 73–75», ISO 13964 §6.2.2 «p. 6», Crowder §9.2 «libro p. 182») no se revisaron una a una. La de Crowder es coherente con el encabezado de la página 182; el índice indica 183 para otro tramo. Estas páginas son aceptables mientras se identifiquen como no comprobadas.
- **ISO 5725-2 §8.1, tabla 4:** no encontré la tabla en la extracción; el cotejo ya lo deja como no comprobado. Aceptable.
- **Otras ocurrencias:** no comprobé el contenido de cada ocurrencia individual de Crowder caps. 6–7 y MMU caps. 5–6 más allá del encabezado. El cotejo ya las marca como verificadas solo por sección o como no verificables. Aceptable, pero no deben presentarse como verificadas por contenido.
- **Scripts, prop_e, AX, F-PSMT-01 y R&R:** no son fuentes externas y el cotejo los trata como internos o propios. Correcto. No revisé AX ni los scripts.
- **Ejercicios, prácticas y cifras:** fuera de alcance por instrucción.
- **Estado cambiante de los libretos:** durante la revisión M07 se leyó en dos momentos con conteos distintos de citas por grep. Con Python el conteo vigente es 101 corchetes. Si la otra supervisión sigue editando, las líneas citadas aquí pueden cambiar.

## Resumen para el supervisor

- **Ambas alarmas están confirmadas como correcciones falsas.** H-01 (Hahs-Vaughn cap. 6 sí trata potencia) y H-02 (TAD §4.4.1 sí exige tres ciclos y seis puntos, y el QAPP §6.2.2 lo confirma para SRP–Level 2).
- **Bloqueante para cerrar S2:** H-01 y H-02. Corregir decisiones 2 y 3, la fe de erratas del cotejo y las frases de `M05_libreto.md:86`, `:166`, `:172` y `:289`.
- **Pendiente antes de cerrar:** H-03 (entrada NIST en M06), H-04 (localizador de la t no central), H-05 (formulación de rango).
- **Menor:** H-06, H-07, H-08.
