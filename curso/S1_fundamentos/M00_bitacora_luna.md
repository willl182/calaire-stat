# Bitácora de desarrollo — M00

## Plan

### Alcance por nivel (transcripción literal de prop_e §5, M0)

- **B:** «tabla larga con identificadores de nivel, lectura, ciclo, día e instrumento; emparejamiento referencia–indicación; unidades; datos faltantes; lecturas negativas del cero; separación entre dato original y calculado.»
  - Práctica fijada: «organizar un conjunto corto del Level 2, calcular `e`, detectar una pareja desplazada y un faltante, y documentar la corrección sin borrar el original.»
- **I añade:** «datos de varios días, analistas y campañas; comprobación de conteos y agrupaciones; paso de tablas anchas a largas; registro de exclusiones justificadas.»
  - Práctica fijada: «reconstruir los resúmenes diarios de una campaña desde las parejas originales.»
- **A añade:** «especificación de entradas, salidas y comprobaciones de un cálculo reproducible; contraste entre dos herramientas.»
  - Práctica fijada: «reproducir un resultado con una segunda herramienta y explicar las discrepancias.»

### Escenas previstas

- **B1.** Por qué la forma de los datos debe conservar las unidades de observación y el diseño; tabla larga con identificadores y tipos de campo.
- **B2.** Emparejamiento por claves, convención `e = y − x`, unidad, faltante, observación negativa del cero y separación inmutable de origen/cálculo; ejemplo docente simulado de parejas.
- **B3.** Trazabilidad de cambios sin sobrescribir; marcador de práctica B y señales de escalamiento.
- **I1.** Extensión a días, analistas y campañas; validación de conteos y agrupaciones con un ejemplo balanceado simulado.
- **I2.** Transformación ancho→largo, conservación de claves, faltantes y registro de exclusión documentada; marcador de práctica I y señales de escalamiento.
- **A1.** Contrato reproducible: entradas, salidas, validaciones, metadatos, captura del entorno y resultados; ejemplo numérico contrastable entre Python y hoja de cálculo.
- **A2.** Marcador de práctica A, señales de escalamiento y cierre acumulativo.

### Datos y rótulo de origen

- Ejemplos cortos de estructura de parejas y de agrupación: **simulados**, fabricados explícitamente para docencia; no son datos ni resultados de CALAIRE, del SRP 55 ni del Level 2.
- No se tomarán celdas del certificado ni del libro R&R como valores de ejemplo. Se alude al contexto Level 2 solo para dar nombres de factores, no para atribuirle resultados.
- Datos generados y salidas numéricas que aparecerán en el libreto: `calc/M00_ejemplos.py`.

### Cálculos previstos

- Errores con signo por pareja (`e = indicación − referencia`) y promedio de los errores del ejemplo básico.
- Recuento de registros completos, emparejados y ausentes; ilustración de detección de una clave de ciclo desplazada sin eliminar ni reescribir el dato original.
- Conteos por analista, campaña, día y ciclo; comprobación de balance del ejemplo intermedio.
- Una operación de ejemplo reproducida en dos herramientas, comparando salidas y comprobaciones de aceptación. Todo valor mostrado tendrá salida correspondiente del script.

### Referencias a verificar antes de citarlas con numeral

- ISO/IEC 17025:2017, §§7.5.1–7.5.2 (registros técnicos, observaciones originales y cambios trazables) y §§7.11.2, 7.11.6 (validación del sistema y comprobación de cálculos/transferencias); verificación posterior con `pdftotext` anotada en Ejecución.
- JCGM 200:2012 (VIM), términos de dato de medición/trazabilidad: no disponible en `docs/`; evitar atribuir definiciones formales a ese documento y dejar pendiente si se requiere en otro capítulo.
- Fuentes de estructura de datos estadísticos: `temario_curso.md` no lista una referencia asignada a M0; no se añadió bibliografía externa no verificada.

### Anexos

- No se prevé remitir a AX.1–AX.13: M00 no contiene deducciones estadísticas que correspondan a esos anexos. El cálculo aritmético ilustrativo se explica en escena y se reproduce en el script.

## Ejecución

### Libreto y prácticas

- Creado `M00_libreto.md` con ficha, narración por niveles B, I y A, escenas previstas, ejemplos numéricos ilustrativos, advertencias de error crítico, señales de escalamiento, cierre y referencias.
- **B:** escenas B1–B2 (estructura y claves; ejemplo simulado de parejas; faltante; signo del cero; separación origen/cálculo y trazabilidad), marcador de práctica «Organizar un conjunto corto del Level 2 y calcular `e`» y señales de escalamiento.
- **I:** escenas I1–I2 (agrupación de campañas, analistas, días y ciclos; conteos; ancho a largo; exclusiones documentadas), marcador de práctica «Reconstruir los resúmenes diarios de una campaña desde las parejas originales» y señales de escalamiento.
- **A:** escenas A1–A2 (contrato de entradas/salidas/comprobaciones; contraste Python–LibreOffice Calc y tolerancia), marcador de práctica «Reproducir un resultado con una segunda herramienta y explicar las discrepancias» y señales de escalamiento.
- Las tres prácticas son solo marcadores, sin enunciados, datos adicionales, soluciones, rúbricas ni evidencias evaluables. No se escribieron ejercicios ni actividades que sustituyan esos marcadores.
- Los conjuntos ilustrativos son **simulados para docencia**, no provienen del certificado F-PSMT-01 ni del estudio R&R y no describen resultados reales de CALAIRE.

### Scripts y resultados

- Script: `calc/M00_ejemplos.py`; ejecutado con `curso/.venv/bin/python curso/S1_fundamentos/calc/M00_ejemplos.py`.
- B: cinco referencias, cuatro indicaciones, cuatro parejas completas y un faltante; error de P01 = −0,2 nmol/mol, P02 = 0,4, P04 = 0,8 y P05 = 0,7; media de los cuatro errores completos = 0,425 nmol/mol. El pareo posicional incorrecto para P03 daría 50,8 nmol/mol; se muestra expresamente como error, no como resultado medido.
- I: dieciséis registros simulados; ocho por campaña, ocho por analista; cuatro por combinación campaña×analista y cuatro por combinación analista×día.
- A: Python y LibreOffice Calc recalculan los errores [0,4; 0,8; 0,7] nmol/mol y coinciden al redondear a tres decimales. Diferencia máxima antes del redondeo: `4,441e-16` nmol/mol; la prueba docente con tolerancia `1e-12` nmol/mol da acuerdo. La tolerancia es ilustrativa, no límite del laboratorio. Las salidas se generaron en un directorio temporal dentro de `calc/`, eliminado al finalizar.
- Todos los valores numéricos de ejemplos del libreto se originan en este script. Las operaciones adicionales citadas son fórmulas o identificadores, no datos/resultados atribuidos al laboratorio.

### Referencias verificadas

- **ISO 17025 §7.5.1–7.5.2:** texto sobre registros técnicos, observaciones/cálculos originales y enmiendas rastreables; verificado mediante `pdftotext -f 21 -l 27 -layout` sobre `docs/BS EN ISO_IEC 17025_2017.pdf`. Corresponde a la página impresa 13 del PDF (página física 21).
- **ISO 17025 §7.11.2:** validación de sistemas de gestión de información y documentación/validación de cambios; verificado con el mismo `pdftotext -f 21 -l 27 -layout`, página impresa 18 (página física 26).
- **ISO 17025 §7.11.6:** comprobación apropiada y sistemática de cálculos y transferencias; verificado con el mismo comando, página impresa 18 (página física 26).
- **prop_e §§2–3 y §5, M0:** alcance por nivel, convenciones y señales de escalamiento cotejadas directamente con `prop_e.md`; es fuente curricular Markdown, no requiere verificación PDF.
- No se usaron numerales de fuentes bibliográficas externas no verificadas. VIM/JCGM 200 no se cita en el libreto porque no está disponible en `docs/`; queda pendiente solo si otro capítulo necesita una definición formal de sus términos.

### Decisiones y pendientes

- En B se planificaron tres temas de escena; la trazabilidad de cambios (B3 del plan) se integró en la escena B2 para mantener el flujo dato original → cálculo → corrección rastreable, sin agregar una escena redundante. El libreto ejecutado queda con B1–B2.
- Se eligieron ejemplos simulados porque el capítulo necesita demostrar estructura y cálculo, no auditar ni corregir los archivos originales del laboratorio.
- La cita ISO 17025 respalda trazabilidad de registros y verificación de cálculos/sistemas; la tabla larga se presenta como convención pedagógica del capítulo, no como mandato de la norma.
- No se remite a AX.1–AX.13: M00 no contiene deducciones asignadas a esos anexos.
- No quedan referencias con numeral pendientes de verificación. Pendiente documental no bloqueante: el VIM no está disponible en `docs/`, por lo que se evitó citarlo y no se formularon definiciones formales atribuibles a él.

## Correcciones (revisión Haiku)

| ID del hallazgo | Decisión | Cambio hecho | Ubicación | Justificación |
|---|---|---|---|---|
| R01 | aplicado | Se corrigió el cierre: ahora anuncia M1 como capítulo siguiente y M2 como el módulo posterior de descripción estadística. | `M00_libreto.md`, cierre del capítulo | M1 es el siguiente módulo; la secuencia de prop_e ubica después la descripción en M2. La guía §2 pide una transición al capítulo siguiente. |
| R02 | aplicado | Se quitó la mención de que el marcador queda sin desarrollo; la transición habla de reconstruir resúmenes diarios. | `M00_libreto.md`, transición I2 | Guía del libreto §1: el marcador de práctica se deja sin comentario sobre su falta de desarrollo. |
| R03 | aplicado | Se quitó la frase «aquí queda únicamente el marcador» y se dejó la transición al contraste de herramientas. | `M00_libreto.md`, transición A2 | Guía del libreto §1: las prácticas aparecen solo como marcadores, sin explicación de lo que se pospone. |
| R04 | aplicado | La caja de error crítico sobre dependencia ahora cita prop_e §8. | `M00_libreto.md`, escena I1 | prop_e §8 contiene los errores críticos; §§2–3 no sustentaban ese criterio. |
| R05 | aplicado | Se añadió prop_e §8 a las cajas de error crítico de B1, B2, I2 y A2. | `M00_libreto.md`, cuatro cajas `[ERROR CRÍTICO]` | Guía del libreto §3 remite los errores críticos a prop_e §8. |
| R06 | aplicado con cambios | En fórmulas se añadieron llaves a las comas decimales y se usó el signo menos matemático; la fórmula de Excel conserva el guion ASCII propio de su sintaxis. | `M00_libreto.md`, pregunta B y escena A2 | La notación evita el espaciado de puntuación decimal en modo matemático y conserva la convención de prop_e §3. El guion de `=C2-B2` es sintaxis de hoja de cálculo, no notación matemática. |
| R07 | aplicado | Se verbalizaron las potencias de diez y la fórmula de Calc; «es verdadero» pasó a «se cumple». | `M00_libreto.md`, escena A2 | Guía del libreto §1 exige leer las fórmulas en voz alta y usar prosa oral clara. |
| R08 | aplicado | Se unificó la clave como `id_pareja`; `lectura` queda como número de lectura dentro del nivel. | `M00_libreto.md`, definición de claves, pizarra y tabla B1 | Evita colisión de términos y mantiene separados identificador de pareja e identificador de lectura requeridos por prop_e §5, M0. |
| R09 | aplicado | Se cambió «en la pizarra proyecto» por «en la diapositiva tienen» y se agregó la acotación `[DIAPOSITIVA]` antes de la tabla simulada. | `M00_libreto.md`, escena B1 | La narración y la acotación ahora describen el mismo soporte visual, conforme a la guía §1. |
| R10 | aplicado | Se dividieron las frases largas señaladas y se acortaron otras de B2 e I1, incluida la explicación de exclusiones. | `M00_libreto.md`, escenas B1, B2 e I1 | Se mejora la oralidad y el ritmo breve pedidos en la guía §1, sin quitar contenido técnico. |
| R11 | aplicado | Se aclaró que Calc recalcula la hoja y se normalizaron las enumeraciones sin punto y coma antes de «y». | `M00_libreto.md`, escena A2 | La redacción evita la ambigüedad de «hoja abierta» y usa puntuación estándar en enumeraciones. |
| R12 | aplicado con cambios | Se precisó que ISO 17025 §7.5.2 trata de enmiendas; el registro de exclusiones se identifica explícitamente como convención del curso. | `M00_libreto.md`, escena I1 | La cláusula no regula específicamente exclusiones analíticas; la redacción separa el requisito normativo de la práctica pedagógica. |
| R13 | aplicado | Se incorporó un ejemplo simulado de dos filas anchas, tres valores presentes y tres registros largos; el script ahora genera y comprueba esa transformación. | `M00_libreto.md`, escena I2; `calc/M00_ejemplos.py`, bloque I2 | Guía §3 requiere ejemplo numérico para temas cuantitativos. La comprobación ejecutada confirma 3 valores no faltantes = 3 registros largos. |

Correcciones adicionales por iniciativa propia:

- Revisé el libreto en busca de otros casos del tipo señalado en R06; no quedan fórmulas matemáticas con guion ASCII en lugar del signo menos, ni comas decimales sin proteger en modo matemático. Se conservó `-` solo donde pertenece a la fórmula de Calc.
- Revisé las transiciones de las tres prácticas: cada una mantiene el marcador sin desarrollar la práctica ni explicar su ausencia.
- Recalculé todo `calc/M00_ejemplos.py` con `curso/.venv/bin/python -I`. Se conservaron los resultados previos de B, I1 y A; I2 añadió `filas anchas=2`, `celdas no faltantes=3`, `registros largos=3`. Python/Calc continúan coincidiendo redondeados; diferencia máxima `4,441e-16` nmol/mol y tolerancia `1e-12` cumplida.