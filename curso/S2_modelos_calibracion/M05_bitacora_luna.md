# M05 — Bitácora de desarrollo

## Plan

### Alcance por nivel (transcripción literal de prop_e.md §5, M5)

> **B:** factor, nivel, bloque, réplica; lectura, ciclo, día; observación dependiente frente a repetición independiente.
>
> **I añade:** aleatorización, bloqueo, factoriales y robustez; distribución del esfuerzo entre niveles, ciclos y días; relación con potencia.
>
> **A añade:** diseños anidados escalonados; diseño de un estudio de repetibilidad y reproducibilidad (R&R); comparación de diseños por componentes identificables.

La competencia estadística del módulo, literalmente: «relacionar lo que se quiere estimar con lo que varía en el experimento: factores, réplicas, bloques, estructuras cruzadas y anidadas».

### Escenas previstas

- Ficha: competencia, prerrequisito M4, alcance B/I/A, rótulo de origen para los ejemplos, remisiones a AX y referencias.
- B1: definir respuesta, factor, nivel, unidad experimental y réplica con la calibración comparativa.
- B2: relacionar lectura, ciclo, día; dependencia, pseudorreplicación, bloques y estructuras anidadas/cruzadas.
- B3: lectura del diseño 12 puntos × 8 lecturas × 6 días; qué estima/separa, qué confunde y qué información falta, sin inferir independencia automáticamente.
- Señales de escalamiento B; marcador de práctica B en el punto curricular correspondiente.
- I1: aleatorización, bloqueo por día y diferencia entre aleatorizar corridas y puntos; límites operativos.
- I2: diseños factoriales completos, efectos principales e interacciones; ejemplo numérico 2³ con datos simulados.
- I3: un factor a la vez frente a factorial y robustez (flujo, acondicionamiento, temperatura); recursos por niveles/ciclos/días y vínculo conceptual con potencia, incluida la pregunta de detectar cambio de pendiente 0,005 sin sobredimensionar el alcance estadístico del módulo.
- Marcador de práctica I.
- A1: cruzado, anidado y anidado escalonado; ejemplo de lecturas dentro de ciclos y ciclos dentro de días.
- A2: plan de R&R con analistas, campañas/días/ciclos; efectos fijos/aleatorios, unidad de réplica e interacciones según el diseño, comparando componentes identificables.
- A3: comparación de diseños por componentes; por qué añadir analistas puede ser más informativo que sumar lecturas, con ejemplo cuantitativo rotulado como simulado.
- Marcador de práctica evaluable A.
- Cierre narrado y referencias verificadas.

### Datos y rótulos de origen

- Diseño del certificado F-PSMT-01: 12 puntos × 8 repeticiones × 6 días. Fuente: `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm`; rótulo **propio** para la descripción del diseño (no se atribuirán al laboratorio resultados calculados o simulados).
- Diseños BIPM.QM-K1, SRP QAPP, SRP SOP, EPA TAD, EN 14625 e ISO 13964 tal como se describen en `prop_e.md` §5 M5. Fuentes documentales correspondientes en `docs/`; rótulo **publicado** cuando se cite un diseño documental.
- Ejemplos aritméticos de reparto de tratamientos factoriales y de precisión de componentes: datos **simulados**, con valores pequeños elegidos únicamente para explicar el diseño; no son resultados CALAIRE.
- No se manipularán archivos reales defectuosos. No se requiere analizar lecturas crudas para el alcance de M5.

### Cálculos previstos

- Conteo factorial completo: `N = ∏ n_i`; para el ejemplo 2³, combinaciones y grados de contraste de efectos/interacciones.
- Conteo de corridas y lecturas por condición en el ejemplo simulado de robustez; cálculo de efectos como diferencias de medias y contraste de replicación si resulta necesario para explicar el diseño.
- Ilustración aritmética simulada de precisión de la estimación de una media/componente al cambiar unidades independientes (analistas/días/ciclos) frente a solo multiplicar lecturas subordinadas. Cada cifra del libreto tendrá script reproducible bajo `calc/M05_*.py`, ejecutado con `curso/.venv/bin/python`.

### Referencias a verificar con `pdftotext`

- Introducción a Statistics in Metrology, §9.2 (archivos por capítulo en `docs/intro_stats_metro_c*.pdf`).
- Brereton, capítulo 2 (`docs/chemometrics_c02.pdf` / libro si hace falta).
- Mark y Workman, capítulos 8–16 (archivos de secciones disponibles en `docs/chemometrics_spectroscopy_s*.pdf`); usar solo numerales verificables.
- ISO 5725-3: §§5–6 y 9.3–9.5 (`docs/ISO 5725-3_1994.pdf` y versión con corrigendum).
- EN 14625: §§8.4.6–8.4.8 (`docs/BS EN 14625_2012.pdf`).
- ISO/IEC 17025: §7.2.2 (`docs/BS EN ISO_IEC 17025_2017.pdf`).
- Protocolo BIPM.QM-K1 A §§3–7 y B §§5–8 (`docs/BIPM.QM-K1_2.protocol.pdf`).
- SRP QAPP Elementos 6.2.1 y 7.1, Tabla 7-1 (`docs/srp_qapp.pdf`); SRP SOP §§9.7.19–9.7.20 (`docs/srp_sop.pdf`).
- EPA TAD Tabla 4-1 (`docs/o3_tad_508_20230906_final.pdf`); ISO 13964 §6.2 (`docs/Air quality_ Determination of ozone in ambient air_ ISO 13964.pdf`); NISTIR 6963 §§8–10 (`docs/nistir6963.pdf`).
- Si un numeral no puede comprobarse, se citará la fuente sin numeral y quedará anotado como pendiente, sin reconstruir numeración por conjetura.

### Anexos previstos

- AX.4 para fundamentos/deducciones de cuadrados medios esperados y componentes de varianza (remisión, sin desarrollar deducciones).
- AX.11 solo si una explicación de precisión estimada requiere remitir a límites de confianza; evitar introducir contenido inferencial fuera del M5.
- No se prevén otras remisiones de deducciones: M5 enseña a formular y comparar diseños, no a ejecutar ANOVA ni a deducir estimadores.

## Ejecución

### Contenido escrito

Se completó `M05_libreto.md` con ficha; nivel B (escenas B1–B4 y señales de escalamiento); nivel I (escenas I1–I3); nivel A (escenas A1–A3); cierre y referencias. Se incluyeron advertencias narradas de errores críticos y las remisiones de diseño a AX.4 sin deducciones. Se dejaron únicamente los tres marcadores de prácticas exigidos por la guía —uno por nivel—; no se desarrollaron enunciados, ejercicios, soluciones, evidencias ni rúbricas. Todos los datos simulados se identifican como tales; el diseño F-PSMT-01 se presenta solo como descripción de fuente propia.

### Scripts y resultados

- `calc/M05_diseno.py`, ejecutado con `curso/.venv/bin/python curso/S2_modelos_calibracion/calc/M05_diseno.py`.
- Resultado de ocho lecturas simuladas: media 0,40 nmol/mol; medias de las condiciones simuladas baja/alta: 0,20 y 0,80 nmol/mol; contraste alta menos baja: 0,60 nmol/mol.
- Conteo de la estructura descrita para F-PSMT-01: 12 × 8 × 6 = 576 registros (10 puntos de concentración y 2 de cero). El objetivo de cambio de pendiente de 0,005 se registra como problema curricular, sin calcular su potencia.
- Factorial simulado 2³: 8 combinaciones; 16 corridas con dos repeticiones independientes por combinación. Contrastes corregidos (diferencia de medias nivel + menos nivel −), nmol/mol: flujo 0,800; acondicionamiento 0,200; temperatura −0,100; flujo×acondicionamiento 0,300; flujo×temperatura 0,040; acondicionamiento×temperatura −0,020; interacción triple 0,080.
- Ejemplo R&R simulado con 4 días, 2 ciclos por día y 8 lecturas por ciclo: para 3 analistas, 12 días, 24 ciclos, 192 lecturas y 3 niveles del factor analista; para 6 analistas, 24 días, 48 ciclos, 384 lecturas y 6 niveles del factor analista. En ambos casos hay 16 lecturas subordinadas por día.
- Ejemplo de precisión simulado bajo el modelo de AX.4, con $s_{entre}=0,20$ y $s_r=0,10$ nmol/mol: incertidumbre estándar del promedio de errores $u(\bar e)$ = 0,083 (d=6, n=8), 0,082 (d=6, n=16) y 0,059 nmol/mol (d=12, n=8). Se interpreta como ilustración de asignación, no como potencia del cambio de pendiente.
- El script se reejecutó tras la revisión; no se calculó potencia, ANOVA ni componentes de varianza.

### Referencias verificadas con `pdftotext`

| Clave y numeral citado | Archivo en `docs/` | Página comprobada | Comprobación |
|---|---|---:|---|
| Crowder et al., §9.2 | `intro_stats_metro_c09.pdf` | PDF 2 (página impresa 182); continúa en PDF 3 | Encabezado «Factorial Experiments in Metrology» y definición del patrón factorial. |
| Statistical Concepts, §§6.1.2–6.1.4 | `statistical_concepts_c06.pdf` | PDF 1 | Encabezados «Sample Size», «Power» y «Effect Size». |
| Brereton, cap. 2 | `chemometrics_c02.pdf` | PDF 1–3 (título/capítulo); PDF 13 (aleatorización) | Encabezado «Experimental Design» y pasaje sobre aleatorizar la secuencia experimental. |
| ISO 5725-3, §§9.3–9.5 | `ISO 5725-3_1994.pdf` | PDF 15–17 (páginas impresas 7–9) | §9.3 nested experiments; §9.4 fully-nested; §9.5 staggered-nested. |
| EN 14625, §§8.4.6–8.4.8 | `BS EN 14625_2012.pdf` | PDF 26–27 | Linealidad, sensibilidad a presión y sensibilidad a temperatura. |
| ISO/IEC 17025, §7.2.2 | `BS EN ISO_IEC 17025_2017.pdf` | PDF 19 | Encabezado y texto de validación de métodos. |
| SRP QAPP, §6.2.1 | `srp_qapp.pdf` | PDF 18 | Descripción de ciclos y puntos de comparación. |
| SRP SOP, §§9.7.19–9.7.20 | `srp_sop.pdf` | PDF 60–61 | Número de puntos, repeticiones/ciclos y mínimo de ciclos indicado por el procedimiento. |

El protocolo BIPM.QM-K1 fue consultado con `pdftotext` para las descripciones de los protocolos A y B y de los niveles nominales (PDF 5–7 y 11–13); el capítulo lo cita por nombre y protocolo, sin numeral. Las referencias al certificado se basan en la estructura indicada en la guía §6 y prop_e §5; no se extrajeron resultados ni se corrigieron datos del libro de cálculo.

### Decisiones tomadas y pendientes

- Se mantuvo el alcance curricular literal de prop_e §5 M5. No se desarrollan ANOVA ni estimadores de componentes. Se añadió una ilustración aritmética de precisión del promedio bajo el modelo ya previsto en AX.4, sin calcular potencia para el cambio de pendiente.
- El ejemplo de robustez factorial y el ejemplo de asignación R&R son simulados; no se presentan como observaciones ni desempeño de CALAIRE.
- La regla de aleatorización se explicó con restricciones operativas; no se presentó como requisito de aleatorizar órdenes institucionales que los documentos mantienen fijos.
- EPA TAD §4.4.1 e ISO 13964:1998 §6.2.2 se verificaron en la revisión Haiku y se incorporaron en el libreto; se eliminaron las marcas de pendiente.
- Brereton, capítulo 2, sí se incorporó y se verificó en `chemometrics_c02.pdf`; no se usaron como referencias finales Mark y Workman ni NISTIR 6963, aunque figuraban entre las verificaciones previstas en el plan.

## Correcciones (revisión Haiku)

| Id | Decisión | Cambio hecho | Ubicación | Justificación |
|---|---|---|---|---|
| R01 | aplicado | Corregidos los efectos factoriales; el script ahora imprime el contraste calculado sin duplicar por dos y se reejecutó. | `M05_libreto.md` I2; `calc/M05_diseno.py`; esta bitácora, Ejecución | Con codificación ±1, la diferencia de medias es 2β; el cálculo de sumas ya devolvía esa diferencia. Valores reproducidos por el script: 0,800; 0,200; −0,100; 0,300; 0,040; −0,020; 0,080 nmol/mol. |
| R02 | aplicado con cambios | Quitada la atribución no respaldada a Crowder para valores/unidades; la fórmula del total factorial se presenta como conteo combinatorio y se referencia a una fuente externa sin numeral disponible en docs/. | `M05_libreto.md` B1 e I2; Referencias | Crowder 2020 §9.2 no respalda esas dos afirmaciones según la verificación de Haiku; no se inventa un subapartado. |
| R03 | aplicado | Sustituida la referencia de bloqueo de Brereton por Montgomery (no disponible en docs/) y agregada en I1. | `M05_libreto.md` B2 e I1 | Brereton cap. 2 no trata bloqueo; Montgomery se usa sin numeral no verificado. |
| R04 | aplicado con cambios | Añadidas referencias a unidad experimental, réplica/pseudorreplicación, aleatorización, interacción, robustez y repetibilidad; VIM se cita sin numeral. | `M05_libreto.md` B1–B2, I1–I3 y A2 | Las definiciones ahora tienen respaldo documental o una fuente externa identificada como no disponible en docs/; no se atribuyen numerales no comprobados. |
| R05 | aplicado | Precisado que el certificado tiene 10 puntos de concentración y 2 de cero; conservado el total de 576 y aclarado el orden temporal de ambos ceros. | `M05_libreto.md` ficha, B3 y práctica B | La hoja del certificado especifica esos 12 puntos; 12 × 8 × 6 sigue siendo 576. |
| R06 | aplicado con cambios | Retirada la narración de secuencias y estabilización BIPM; se conserva solo la identificación general de la comparación y de los protocolos A/B, con nota explícita de exclusión. | `M05_libreto.md` B4 y A3 | prop_e §6 excluye la organización y el protocolo de BIPM.QM-K1; se usa únicamente como referencia contextual de un diseño publicado. |
| R07 | aplicado | Corregida la referencia de sensibilidad de EN 14625 a §§8.4.7–8.4.8. | `M05_libreto.md` B4 e I3 | §8.4.6 corresponde a falta de ajuste de linealidad, no a sensibilidad. |
| R08 | aplicado | Incorporados EPA TAD §4.4.1 e ISO 13964:1998 §6.2.2; retiradas las notas de pendiente de las citas y bibliografía. | `M05_libreto.md` B4 y Referencias | Numerales verificados en la revisión Haiku con `pdftotext`; coinciden con las afirmaciones incluidas. |
| R09 | aplicado | Corregida la cita de comparación de diseños a ISO 5725-3 §§9.4–9.5 y 9.8. | `M05_libreto.md` A1 | La comparación entre diseños está en §9.8; §§9.4–9.5 describen los diseños. |
| R10 | aplicado con cambios | Añadida explicación narrada de efectos fijos/aleatorios y de cómo el patrón define el denominador; A1 ahora enseña identificación del término y remite deducción a AX.4 y el cálculo a M6. | `M05_libreto.md` A1–A2 | Cubre la distinción y el razonamiento requeridos por la práctica de prop_e sin desarrollar ANOVA; se distingue seleccionar el denominador de calcular el contraste. |
| R11 | aplicado | Cambiado «parcialmente confundidos» por «quedan confundidos» cuando cada analista tiene campañas propias sin campaña compartida. | `M05_libreto.md` A2 | En ese diseño campaña está anidada en analista y sus efectos no se separan. |
| R12 | aplicado | Separadas lecturas intradía para repetibilidad de ciclos independientes para variación entre ciclos. | `M05_libreto.md` A2 | Alineado con la convención curricular de `s_r` y con la jerarquía descrita en B2. |
| R13 | aplicado con cambios | Añadido ejemplo simulado de $u(\bar e)$ para (d,n)=(6,8), (6,16), (12,8); actualizado el script. Se aclara que no calcula potencia para el cambio de pendiente 0,005. | `M05_libreto.md` I3; `calc/M05_diseno.py` | AX.4 cuantifica precisión del promedio, no potencia de una pendiente; además, los parámetros dados tienen unidades de error, no de pendiente. Se mantiene una ilustración cuantitativa válida sin afirmar una potencia incompatible. |
| R14 | aplicado | Reemplazadas atribuciones imprecisas a «la propuesta curricular» por formulación directa de candidatos y plan posible. | `M05_libreto.md` I1, I3 y A3 | Las fuentes de esas afirmaciones son el temario o una propuesta docente, no prop_e; la nueva redacción no confunde los documentos. |
| R15 | aplicado | Leída en voz alta la ecuación simulada, término por término, usando coma decimal. | `M05_libreto.md` I2 | Cumple guía_libreto §1 y §4: las fórmulas se escriben y también se dicen en palabras. |
| R16 | aplicado | Convertida la acotación en pregunta al grupo con respuesta esperada y etiqueta permitida. | `M05_libreto.md` A1 | La intervención es una pregunta, no un ejemplo; se ajusta a guía_libreto §1. |
| R17 | aplicado | Ficha, diapositiva y marcador de práctica distinguen 10 puntos de concentración + 2 de cero y dicen «8 lecturas»; se conserva que el certificado las llama repeticiones. | `M05_libreto.md` ficha, B3 y práctica B | Mantiene terminología coherente con prop_e y guía_libreto §6 sin borrar el término literal de la fuente propia. |
| R18 | aplicado | Normalizadas las citas de Crowder a la clave Crowder 2020 y la de ISO 13964 a ISO 13964:1998; unificada la referencia bibliográfica del estándar. | `M05_libreto.md` B1–I2 y Referencias | Coincide con las claves de guía_libreto §5. |
| R19 | aplicado | Indicados los módulos donde se trabajan cambio de escala, atípicos, residuos, incertidumbre en ambos ejes, grados de libertad y cercanía a límite. | `M05_libreto.md` Señales de escalamiento B | prop_e §2 pide reconocer estas señales en B; se evita sugerir que sean exclusivas de módulos posteriores. |

Correcciones adicionales por iniciativa propia:

- Actualicé el registro de resultados de la Ejecución para retirar los contrastes factoriales erróneos previos y consignar la salida recalculada del script.
- Revisé la atribución de la definición de respuesta a una fuente curricular: prop_e fija convenciones y alcance, no es respaldo técnico; la referencia se sustituyó por una fuente técnica externa identificada como no disponible en docs/.
- En la ilustración de precisión, limité explícitamente la conclusión al promedio bajo el modelo equilibrado de AX.4; no se presenta como estimación de potencia ni como resultado observado de CALAIRE.
- Alineé también el cierre de A3 con la enseñanza de denominadores añadida en A1–A2, y corregí el redondeo del caso d=12, n=8 a 0,059 nmol/mol para que coincida con el script.
