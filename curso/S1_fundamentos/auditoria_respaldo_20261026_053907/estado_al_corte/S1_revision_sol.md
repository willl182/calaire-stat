# S1. Revisión de contenido y entrega — Sol

Fecha: 25 de octubre de 2026. Alcance de edición: exclusivamente `curso/S1_fundamentos/`. Fase: solo contenido; no acredita preparación de prácticas ni autorización para impartir.

## Nota del supervisor

Supervisor: claude-sol (gpt-6.1-sol). Reanudación: 2026-10-26, 05:27:40 −05:00 (hora local obtenida con `date -Is`). Se conserva íntegro el plan y la nota del orquestador. Las ediciones interrumpidas son candidatas, no resultados previamente aprobados.

## Plan de revisión

Plan registrado antes de revisar los capítulos. Se han leído íntegramente `curso/00_plan_maestro.md`, `curso/guia_libreto.md`, `prop_e.md` y `revision_final_prop_e.md`.

1. Leer, en orden M00 → M04, cada libreto, bitácora y revisión Haiku, sin dar por verificados sus dictámenes. Construir una correspondencia entre todos los contenidos B/I/A de prop_e §5 y las escenas; comprobar niveles acumulativos y exclusiones de §6.
2. Revisar corrección estadística y metrológica, notación, supuestos, unidad de repetición, escala, signo, cobertura, errores críticos y escalamiento. Distinguir ejemplos docentes resueltos de prácticas: conservar exactamente un marcador por práctica curricular y no desarrollar ejercicios, soluciones ni rúbricas.
3. Leer y ejecutar los cinco scripts con `curso/.venv/bin/python`, sin generar archivos fuera de S1. Recalcular los valores clave con una segunda implementación o identidades independientes; comprobar correspondencia entre resultados y narración. Incorporar comprobaciones reproducibles en `calc/` cuando sea necesario.
4. Verificar las referencias técnicas y sus numerales mediante `pdftotext` sobre los PDF de `docs/`; guardar la evidencia de verificación dentro de S1. No usar prop_e como respaldo técnico. Para fuentes ausentes, identificar expresamente esa condición y no inventar numerales.
5. Revisar el formato hablado, acotaciones, lectura de fórmulas, ejemplos por tema cuantitativo, rótulos de origen, transiciones, prerrequisitos y referencias AX; eliminar duplicaciones innecesarias sin suprimir la recapitulación acumulativa.
6. Registrar hallazgos con id S-…, capítulo, ubicación, severidad, problema y corrección. Aplicar las correcciones personalmente; conservar las bitácoras y revisiones previas como antecedentes, sin reescribirlas como si fueran esta revisión.
7. Crear el índice de entrega con escenas por nivel, los quince marcadores pendientes, datos y rótulos, anexos, estado y pendientes. Cerrar con pruebas ejecutadas, límites de la verificación y estado de entrega; no declarar listo para impartir el curso.

Severidad: crítica (resultado o decisión inválidos), alta (error técnico, referencia equivocada o contenido curricular ausente), media (ambigüedad de supuestos, reproducibilidad o forma), baja (claridad editorial). No se modificarán archivos externos a S1.

## Hallazgos por capítulo

Las dos interrupciones dejaron cambios sin dictamen. Esta reanudación distingue la propuesta anterior de su verificación actual. `Cxx` identifica la primera auditoría; `D2-xx` identifica el bloque global número xx, contando cada encabezado `@@` de `auditoria_interrupcion_sol_2/cambios_sol.diff` desde el principio. La ubicación usa escena y encabezado para sobrevivir a cambios de líneas. Severidad describe el defecto que motivó la corrección, no un defecto necesariamente abierto.

### M00 — estructura y cálculo reproducible

| Hallazgo | Candidata | Ubicación | Severidad | Problema y decisión técnica |
|---|---|---|---|---|
| S-001 | C01 | Introducción B, definición de error | alta | prop_e solo justifica convención curricular. **Conservada**: GUM B.2.19 define el error y su nota 1 admite valor convencional de referencia cuando no se conoce el verdadero. |
| S-002 | C02 | Introducción B, unidades | alta | Equivalencia nmol/mol–ppb correcta, pero C02 inventariaba tabla 2. **Ajustada**: EN 14625 §8.2, tabla 1, nota, contiene la equivalencia; tabla 2 no. |
| S-003 | C03 | Marcador B | media | Marcador abreviado omitía pareja desplazada, faltante y trazabilidad. **Conservada**: restaura práctica completa sin desarrollarla. |
| S-004 | C04 | I2, pizarra de tabla larga | media | `lectura` designaba índice y concentración. **Conservada**: magnitud `y (nmol/mol)`, índice separado. |
| S-005 | C05 | I2, narración ancho/largo | media | Colisión de nombre con índice de lectura. **Conservada**: `y` contiene indicación; ciclo identifica evento. |
| S-006 | C06 | Referencias del capítulo | alta | Faltaban entradas de GUM/EN para las citas técnicas. **Ajustada**: conservar entradas, corregir EN a tabla 1 e incorporar GUM C.2.19. |
| S-007 | C07 | calc/M00_ejemplos.py, contraste Calc | media | Criterio numérico solo se imprimía. **Conservada**: aserciones de longitud y tolerancia detectan discrepancias; ejecución real satisfactoria. |
| S-028 | D2-02 | B1, promedio 0,425 | media | Media respaldada solo por alcance curricular. **Conservada**: GUM C.2.19 respalda media aritmética; cálculo Decimal independiente confirma 0,425 nmol/mol. No se interpreta como precisión del instrumento. |
| S-029 | D2-03 | I2, ejemplo y script | media | Enumeración aún usaba lectura como magnitud y no documentaba salida explícita del faltante. **Conservada**: `y`, lectura oral, tres indicaciones y estado separado con clave; script verifica 3+1=4 celdas. |
| S-030 | D2-01 | Introducción B, unidades | alta | Numeral falso de C02. **Conservada**: tabla 1 verificada con pdftotext; complementa S-002. |
| S-031 | D2-04 | Referencias del capítulo | alta | Bibliografía mantenía tabla falsa y no registraba C.2.19. **Conservada**: referencias sincronizadas con narración y PDF, sin ampliar alcance. |

Hallazgo adicional de esta reanudación:

| Hallazgo | Origen | Ubicación | Severidad | Problema y corrección |
|---|---|---|---|---|
| S-100 | Reanudación actual | M00 I2, criterio de validación | media | Tras conservar el faltante, «número de registros resultantes» podía incluir también registros sin indicación y contradecir el conteo 3+1. **Corregida**: comparar valores no faltantes solo con registros que contienen indicación y comprobar aparte las claves/estados faltantes. No cambia ninguna cifra ni requiere cambiar el script. |

Verificación directa M00: lectura íntegra de libreto, bitácora, revisión Haiku y scripts; cotejo curricular B/I/A completo. Tablas largas, faltantes y exclusiones se presentan como convenciones del análisis, no como mandatos textuales de ISO 17025. No hay temas excluidos ni deducciones nuevas; tres marcadores, sin desarrollo de prácticas.

### M01 y M02 — modelo, escala y respuesta

| Hallazgo | Candidata | Capítulo y ubicación | Severidad | Problema y decisión técnica |
|---|---|---|---|---|
| S-008 | C08 | M01, ficha | media | No constaba prerrequisito real de parejas/unidades. **Conservada**: M00 prepara esas entradas; no amplía temario. |
| S-009 | C09 | M02 B4, CV | alta | Cita sin localización comprobada. **Conservada**: ASQ, apéndice C, entrada coefficient of variation, p. 572 (PDF 605), verificada. |
| S-012 | C12 | M01 B2, trayecto óptico | alta | Entradas simplificadas podían confundirse con configuración real del SRP. **Conservada**: longitud y transmitancia corresponden a un trayecto hipotético, no a combinación de canales reales. |
| S-013 | C13 | M02 B4, parejas | alta | Ejemplo anterior mezclaba niveles cuando M2-B exige un nivel durante varios días. **Conservada**: seis parejas de tres días en nivel nominal 200; errores preservados. |
| S-016 | C16 | M02 B4, dispersión de y | alta | 154,27 pertenecía al conjunto anterior. **Conservada**: desviación muestral actual 0,240138849 nmol/mol, comprobada independientemente. |
| S-019 | C19 | M01 I1, error y error relativo | alta | prop_e usado como respaldo técnico. **Conservada**: GUM B.2.19–B.2.20 respalda definiciones y denominador; prop_e queda como alcance. |
| S-020 | C20 | M02 B4, interpretación | alta | La diferencia entre dispersiones no constituye atribución causal completa a la referencia. **Conservada**: se evita descomposición injustificada; referencia y error covarían en el conjunto. |
| S-023 | C23 | M01, marcador B | media | Marcador abreviado no explicitaba las tres concentraciones ni signo/cambio relativo. **Conservada**: práctica curricular completa, sin desarrollo. |
| S-024 | C24 | M01 A1, párrafo eliminado | baja | Repetía cancelación ya explicada con las mismas cifras. **Conservado el borrado**: permanece explicación suficiente; D2-08 incorpora caso distinto de cancelación parcial. |
| S-025 | C25 | M02 B4, diapositiva | alta | Arrastre de s(y)=154,27 tras cambio de datos. **Conservada**: s(y)=0,240 nmol/mol coherente con C13/C16. |
| S-032 | D2-05 | M01, ficha/origen de 1,1329 | alta | Valor sin fuente ni unidad confirmadas. **Conservada**: BIPM-K1 p. 3 documenta 1,1329(35)×10⁻¹⁷ cm²/molécula; se usa valor central sin propagar incertidumbre ni enseñar protocolo. |
| S-033 | D2-06 | M01 B3, conversión | media | ppb y nmol/mol no ilustraban un factor de conversión numérico distinto. **Conservada**: contraste ppm–nmol/mol sí exige conversión. |
| S-034 | D2-07 | M01 I1, cocientes y reescalamiento | alta | Unidades pendientes, corrección confundida con ajuste y pregunta ambigua sobre qué valor cambia. **Conservada**: unidades documentadas, corrección separada de ajuste físico y escenarios solo y/ambos explícitos. Resultados +6,73477 y +1,31677 nmol/mol comprobados; se conserva también el marcador I con el par de coeficientes declarado. |
| S-035 | D2-08 | M01 A1, cancelación parcial | media | Condición de igual sensibilidad quedaba solo verbal. **Conservada**: sensibilidades 1 y 0,8 dejan cambio residual 0,2 por unidad de entrada común; no se interpreta como incertidumbre. |
| S-036 | D2-09 | M01, marcador A | media | Título genérico. **Conservada**: identifica contribuciones canceladas y persistentes como pide M1-A. |
| S-037 | D2-10 | M01, bibliografía | alta | Nuevas afirmaciones requerían fuentes completas. **Conservada**: GUM B.2.19–20 y BIPM-K1, versión 2.1, 09-10-2025, p. 3, verificados. |
| S-038 | D2-11 | M02, ficha/referencias clave | media | Ficha seguía diciendo CV sin numeral. **Conservada**, con ajuste adicional S-065 para MMU; ASQ p. 572 correcto. |
| S-039 | D2-12 | M02 B2, histograma/caja | media | Bordes no explícitos y caja sin convención numérica. **Conservada**: intervalos coherentes con numpy.histogram, conteos 2/3/3; bigotes mínimo–máximo declarados y admitidos por Hahs-Vaughn §2.3.4. |
| S-040 | D2-13 | M02, marcador B | media | Título insuficiente respecto de M2-B. **Conservada**: un nivel, varios días, referencia variable y negativos del cero, sin ejercicio. |
| S-041 | D2-14 | M02 I2, recta descriptiva | media | Enseñar ajuste aquí adelantaba M07. **Conservada**: recta entregada ya calculada; ISO 28037 §5.8 respalda preparación docente. Parámetros comprobados. |
| S-042 | D2-15 | M02 A1, error con signo | alta | Numeral VIM no contrastable en docs/. **Conservada**: GUM B.2.19 disponible respalda signo y definición. |
| S-043 | D2-16 | M02 A1, agregación | media | Efecto de tamaños desiguales quedaba sin ejemplo. **Conservada**: media de grupos cero frente a media de seis lecturas +0,133333 nmol/mol; conjunto distinto declarado, no exclusión de datos reales. |
| S-044 | D2-17 | M02, marcador A | media | Título no identificaba práctica de sesgos opuestos R&R. **Conservada**: restitución curricular sin desarrollo. |
| S-045 | D2-18 | M02, bibliografía | alta | Archivos parciales no contenían todos los pasajes; CV pendiente y VIM no cotejado. **Conservada**, con ajuste S-065: libro completo Hahs-Vaughn, GUM y ASQ localizados; MMU incluye §3.1.3. |
| S-065 | Reanudación actual | M02 B5, ficha y bibliografía | alta | Regla de redondear al final está en MMU §3.1.3, no solo §3.1.1. **Corregida**: conservar §3.1.1 para redondeo de un número y añadir §3.1.3 para operaciones. |
| S-066 | Reanudación actual | M01, cierre | media | «Corregir físicamente» volvía a confundir corrección y ajuste. **Corregida**: cambio de escala no constituye automáticamente corrección individual ni ajuste físico. |
| S-067 | Reanudación actual | calc/, salidas M01/M02 | alta | Salidas antiguas no correspondían a scripts/libretos actuales; M02 aún mostraba 154,266493. **Corregida**: regeneradas ambas salidas; ahora s(y)=0,240139 y M01 incluye ambos reescalamientos/cancelación parcial. |

Verificación M01/M02: extracción nueva con pdftotext de diez PDF, ejecución de ambos scripts con `curso/.venv/bin/python -I`, aserciones, contraste Decimal/statistics y compilación en memoria satisfactorios. Evidencia: `calc/verificacion_M01_M02_personal/pruebas.txt` y extractos del mismo directorio. Auxiliares `referencias_12/` preservados como históricos, no como pruebas nuevas. VIM y NIST/SEMATECH ausentes de docs/: citas sin numeral, limitación explícita.

### Control transversal y auxiliares

| Hallazgo | Ubicación | Severidad | Problema | Corrección |
|---|---|---|---|---|
| S-101 | calc/verificar_entrega_sol.py | media | Control heredado solo comprobaba C01–C27 y podía admitir id/candidata en filas distintas; no cubría la segunda interrupción. | Comprueba en ambos registros la asociación por fila de los 27 Cxx y 37 D2-xx con su S-…, nota del supervisor, ausencia de «En revisión.» y quince marcadores en capítulos/índice. El control estructural no sustituye la revisión técnica. |
| S-102 | calc/informe_00.md; referencias_12/ y referencias_34/ | media | Auxiliares antiguos podían leerse como evidencia de una ejecución actual. | Informe M00 identifica procedencia histórica y recomprobación; LEEME de ambos directorios diferencia extractos/salidas históricos de las pruebas nuevas. No se borran antecedentes ni se atribuyen consultas inexistentes. |
| S-103 | S1_00_indice.md | media | Índice previo fechado el 25 solo remitía a primera interrupción, aunque la entrega necesita ambas. | Actualizada fecha al 26 y enlace a las dos auditorías, decisiones Cxx/D2-xx y evidencia vigente; conserva escenas B/I/A, quince marcadores, rótulos, AX y pendientes. |

## Correcciones aplicadas

Las correcciones conservadas ya estaban materializadas en el árbol recibido: se revisan y ratifican, no se atribuyen falsamente a una nueva edición. Las ajustadas identifican el estado final autorizado. No se alteran los antecedentes de Luna/Haiku ni las instantáneas de auditoría.

| Hallazgo y edición | Decisión | Cambio autorizado | Ubicación final |
|---|---|---|---|
| S-001, C01 | conservada | Respaldo externo GUM para error, convención curricular separada. | M00, introducción B |
| S-002, C02 | ajustada | Sustituir tabla 2 por tabla 1 en EN 14625. | M00, introducción B |
| S-003, C03 | conservada | Marcador B completo, sin ejercicio. | M00, final B2 |
| S-004, C04 | conservada | Columna `y` con unidad; índice lectura separado. | M00, I2 pizarra |
| S-005, C05 | conservada | Narración coherente con esquema. | M00, I2 |
| S-006, C06 | ajustada | Bibliografía GUM/EN correcta y ampliación C.2.19. | M00, referencias |
| S-007, C07 | conservada | Aserciones de longitud y tolerancia en contraste real Python/Calc. | calc/M00_ejemplos.py, bloque A |
| S-028, D2-02 | conservada | Referencia GUM C.2.19 para promedio, no prop_e. | M00 B1 |
| S-029, D2-03 | conservada | Nombrar `y`, conservar faltante identificado; script comprueba tres indicaciones y un faltante. | M00 I2; calc/M00_ejemplos.py, bloque I2 |
| S-030, D2-01 | conservada | Corregir numeral a tabla 1. | M00, introducción B |
| S-031, D2-04 | conservada | Sincronizar tabla 1 y C.2.19 en bibliografía. | M00, referencias |

### M01 y M02 — decisiones materializadas

| Hallazgo y edición | Decisión | Cambio autorizado | Ubicación final |
|---|---|---|---|
| S-008, C08 | conservada | Prerrequisito M00 explícito. | M01, ficha |
| S-009, C09 | conservada | CV localizado en ASQ apéndice C p. 572. | M02 B4 |
| S-012, C12 | conservada | Trayecto hipotético, no configuración real SRP. | M01 B2 |
| S-013, C13 | conservada | Parejas de tres días en un único nivel nominal. | M02 B4 |
| S-016, C16 | conservada | s(y)=0,240 nmol/mol. | M02 B4 |
| S-019, C19 | conservada | GUM para error/error relativo; prop_e solo alcance. | M01 I1 |
| S-020, C20 | conservada | Interpretación sin atribución causal injustificada de dispersiones. | M02 B4 |
| S-023, C23 | conservada | Marcador B completo. | M01, final B3 |
| S-024, C24 | conservado el borrado | Suprimir párrafo redundante sin perder explicación de cancelación. | M01 A1 |
| S-025, C25 | conservada | Diapositiva sincronizada a 0,240. | M02 B4 |
| S-032, D2-05 | conservada | Fuente/unidad de 1,1329 documentadas. | M01 ficha |
| S-033, D2-06 | conservada | Ejemplo ppm frente a nmol/mol. | M01 B3 |
| S-034, D2-07 | conservada | Cocientes documentados, corrección distinta de ajuste, dos escenarios de reescalamiento y marcador I completo. | M01 I1 |
| S-035, D2-08 | conservada | Ejemplo de sensibilidades distintas y cancelación parcial. | M01 A1; calc/M01_modelo_variables.py |
| S-036, D2-09 | conservada | Marcador A completo. | M01, final A1 |
| S-037, D2-10 | conservada | Referencias completas GUM/BIPM. | M01 bibliografía |
| S-038, D2-11 | conservada; complementada S-065 | CV localizado; ficha MMU ampliada a §3.1.3. | M02 ficha |
| S-039, D2-12 | conservada | Bordes explícitos y bigotes mínimo–máximo declarados. | M02 B2 |
| S-040, D2-13 | conservada | Marcador B completo. | M02, final B |
| S-041, D2-14 | conservada | Recta entregada, ajuste se enseña en M07. | M02 I2 |
| S-042, D2-15 | conservada | Sustituir numeral VIM no cotejado por GUM B.2.19. | M02 A1 |
| S-043, D2-16 | conservada | Ejemplo numérico de agregación desigual. | M02 A1; calc/M02_examples.py |
| S-044, D2-17 | conservada | Marcador A de sesgos opuestos R&R. | M02, final A |
| S-045, D2-18 | conservada; complementada S-065 | Bibliografía cotejada, MMU actualizado. | M02 bibliografía |
| S-065 | aplicada en esta reanudación | Citas MMU §§3.1.1 y 3.1.3 para operaciones y redondeo final. | M02 ficha, B5 y bibliografía |
| S-066 | aplicada en esta reanudación | Corrección individual separada de ajuste físico también en cierre. | M01 cierre |
| S-067 | aplicada en esta reanudación | Salidas regeneradas desde scripts actuales sin alterar cálculos correctos. | calc/M01_modelo_variables_salida_sol.txt; calc/M02_examples_salida_sol.txt |
| S-100 | aplicada en esta reanudación | Distinguir conteo de registros con indicación y estados faltantes. | M00 I2, validación ancho/largo |

### Controles y documentación de esta reanudación

| Hallazgo | Cambio aplicado | Ubicación |
|---|---|---|
| S-101 | Ampliar comprobación estructural a 64 candidatas, asociaciones por fila, nota del supervisor y cierre documental sin marcador pendiente de revisión. | calc/verificar_entrega_sol.py |
| S-102 | Identificar procedencia y vigencia de auxiliares; preservar originales de auditoría y resultados anteriores como históricos. | calc/informe_00.md; calc/referencias_12/LEEME.md; calc/referencias_34/LEEME.md |
| S-103 | Actualizar fecha, enlaces de ambas auditorías y alcance de decisiones en índice de entrega. | S1_00_indice.md, cabecera y estado |

### Nota del orquestador: ediciones previas a la interrupción

Antes de la interrupción, sol aplicó 27 ediciones sin registrarlas: 25 en los libretos M00–M04 y una en `calc/M00_ejemplos.py`. Están reconstruidas y verificadas byte a byte en `auditoria_interrupcion_sol/LEEME.md` (tabla C01–C27, versiones previas `*.pre_sol.*` y `cambios_sol.diff`). Al reanudar, cada Cxx debe quedar aquí asociada a un hallazgo S-…, con su decisión (conservada, ajustada o revertida) y su justificación.
