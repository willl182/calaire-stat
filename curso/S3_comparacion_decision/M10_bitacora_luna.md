# Bitácora de desarrollo — M10

## Plan

### Alcance por nivel (tomado literalmente de `prop_e.md`, §5, M10)

- **Competencia estadística:** «aplicar y elegir reglas de decisión con incertidumbre y cuantificar el riesgo de falsa aceptación y falso rechazo.»
- **B:** «resultado, U, k, intervalo y función de uso; regla de decisión suministrada; banda de guarda; acción en la zona próxima al límite.»
- **I añade:** «selección y justificación de reglas; riesgo de falsa aceptación y rechazo; relación incertidumbre–tolerancia; coherencia entre presupuesto y declaración.»
- **A añade:** «riesgo específico y global con modelos explícitos; requisitos bilaterales; decisiones con dependencia.»
- **Prácticas fijadas por prop_e (se dejan solo como marcadores en esta fase):** B, «completar un certificado docente y resolver resultados dentro, cerca y fuera del límite»; I, «resolver un resultado próximo al límite con dos reglas y explicar el riesgo que asume cada una»; A, «cuantificar el riesgo de una decisión para una distribución y una especificación definidas».
- La ficha común de criterios externos para M10/M11/M12/caso C debe identificar equipo o proceso, documento y edición, etapa, diseño, estadístico, divisor, unidades y fuente, y distinguir tolerancias, límites de control y criterios de indicadores. En M10 solo se usarán criterios que se puedan verificar en sus documentos, sin generalizarlos fuera de su ámbito.

### Escenas previstas

1. Ficha: competencia, prerrequisitos M4, M8 y M9, contenido aditivo por nivel, rótulos de datos, anexos y referencias.
2. B1: qué significa conformidad estadística, resultado e intervalo de uso con U, k, unidad y decisión suministrada.
3. B2: banda de guarda y ejemplo de aceptación/rechazo/zona próxima al límite; acción y marcador de práctica B; señales de escalamiento.
4. I1: elección de regla, límite de tolerancia y banda de guarda; riesgos de falsa aceptación/rechazo en ejemplo normal simulado, relación incertidumbre–tolerancia.
5. I2: coherencia del presupuesto, cobertura y declaración del certificado; TUR como relación descriptiva, no regla automática; criterios externos solo en la etapa/documento que los prescribe; marcador de práctica I.
6. A1: riesgo específico y global, modelo explícito de medición, especificación y regla, con cálculo simulado de probabilidades.
7. A2: requisito bilateral y decisión con dependencia; ejemplo simulado de dos límites y resultados correlacionados; grado de equivalencia BIPM.QM-K1 frente a referencia común como caso y no regla de conformidad; límites de combinar o separar decisiones; marcador de práctica A.
8. Cierre narrado y transición a M11 (seguimiento), manteniendo decisiones distintas de límites de control.

### Datos y rótulo de origen

- Ejemplos cuantitativos B/I/A: **simulados**, generados de distribuciones normales declaradas y parámetros pedagógicos explícitos en `calc/M10_ejemplos.py`; no representan datos ni desempeño de CALAIRE.
- Criterios documentales: SRP QAPP, SRP SOP, EPA TAD y BIPM.QM-K1, solo como **criterios publicados** en su ámbito propio y tras verificar cada numeral con `pdftotext`. No se presentan como tolerancias universales ni se reinterpretan como criterios de conformidad de CALAIRE.
- No se utilizarán como datos de ejemplo los archivos propios de calibración, pues el propósito de esta fase es contenido ilustrativo y el paquete docente de decisión no está cerrado.

### Cálculos previstos

`calc/M10_ejemplos.py`, ejecutado con `curso/.venv/bin/python`, reproducirá todos los resultados numéricos derivados: intervalos con U; regla suministrada y clasificación según distancia a tolerancia/banda de guarda; comparación de dos reglas; TUR bajo definiciones declaradas; probabilidades normales de falsa aceptación/rechazo; riesgo específico y global con casos independientes y correlacionados; y verificación de probabilidades bilaterales. Los valores normativos/documentales se citarán desde sus fuentes, no se recalcularán como resultados de CALAIRE.

### Referencias a verificar en `docs/` con `pdftotext`

- *Introduction to Statistics in Metrology*, capítulo 5, riesgo e incertidumbre en decisiones (numerales visibles en el texto extraído).
- *Metrology and Measurement Uncertainty*, capítulos 8–9, reglas, bandas de guarda y decisiones.
- *The ASQ Metrology Handbook*, capítulo 30, TUR y riesgo.
- GUM (JCGM 100) §3.3.7 para incertidumbre expandida y factor de cobertura.
- ISO/TS 28037 §5.7 para contexto del uso de una función de calibración lineal.
- ISO/IEC 17025:2017 §§7.6 y 7.8.6, incertidumbre y declaraciones de conformidad.
- SRP QAPP Tabla 7-1; SRP SOP §9.1; EPA TAD §4: criterios publicados de cada procedimiento/etapa.
- BIPM.QM-K1 §8: uso de grado de equivalencia como caso de comparación, sin equipararlo a una especificación del cliente.
- Toda ubicación no verificable se citará sin numeral y quedará como pendiente; `prop_e.md` y `temario_curso.md` fijan alcance, no respaldan técnicamente.

### Anexos previstos

- **AX.2:** relación entre resultado, incertidumbre y covarianza como base de decisiones dependientes; no desarrollar deducciones.
- **AX.9:** incertidumbre de una diferencia con patrón compartido; remitir al tratar decisiones con dependencia.
- **AX.10:** deducción de probabilidades de falsa aceptación y falso rechazo; usar las expresiones y resultados aquí, sin desarrollar la deducción.
- No se prevé remisión a otros anexos.

## Ejecución

### Contenido escrito

- Ficha del capítulo con competencia estadística, prerrequisitos, alcances acumulativos, orígenes, anexos y fuentes.
- **B:** escenas B1 (resultado, U, k, intervalo y uso) y B2 (regla suministrada, banda de guarda, clasificación, acción); función de corrección de lecturas; certificado y señales de escalamiento; marcador único para la práctica B.
- **I:** escenas I1 (selección de regla, TUR declarado, riesgos específicos, relación incertidumbre–tolerancia) e I2 (coherencia presupuesto/declaración, compatibilidad frente a conformidad, ficha de criterios publicados por etapa y contenido del certificado); marcador único para la práctica I.
- **A:** escenas A1 (riesgo específico y global con distribución explícita) y A2 (requisito bilateral y decisión con dependencia); advertencias críticas, pregunta al grupo, escalamiento; marcador único para la práctica A.
- Cierre narrado y transición a M11. No se desarrollaron enunciados, actividades, soluciones, evidencias ni rúbricas. Los tres marcadores reproducen los títulos de práctica de prop_e M10.
- Extensión final: aproximadamente 5 000 palabras; menos que la orientación de 6 000–10 000, pero incluye todos los contenidos curriculares M10, los ejemplos resueltos narrados, las citas, las exclusiones y las acotaciones exigidas. No se añadió teoría ajena al alcance salvo contexto explicativo estrictamente necesario para aplicar los contenidos asignados.

### Scripts y resultados

- `calc/M10_ejemplos.py`, ejecutado con `curso/.venv/bin/python curso/S3_comparacion_decision/calc/M10_ejemplos.py`; ejecución completada sin errores.
- Ejemplo B simulado: $U=1,2$, $k=2$ como aproximación normal, $u=0,6$ nmol/mol. Resultado $100,0$: intervalo $[98,8;101,2]$, aceptar. Resultado $102,2$: $[101,0;103,4]$, zona intermedia/retener. Resultado $106,0$: $[104,8;107,2]$, rechazar. Función simulada de cero/span: valor corregido $\hat{x}=199,00$ nmol/mol y corrección aditiva $\hat{x}-y=-6,00$ nmol/mol.
- Ejemplo I simulado: semitolerancia $10$, $u=0,8$, $U=1,6$ y TUR definido como semitolerancia/$U=6,25$. Sin guarda, con valor verdadero $9$, $P_{FR}=0,10564977$; con guarda $1$, $P_{FR}=0,5$. Con valor verdadero $10,5$, $P_{FA}$ sin guarda $=0,26598553$, y con guarda $=0,03039636$. Ejemplo adicional de coherencia presupuesto/uso: desviación estándar de lectura individual $1,5$ nmol/mol, por lo que con $k=2$, $U=3,0$ nmol/mol; no se reutiliza para una lectura el $U=1,2$ correspondiente al promedio.
- Ejemplo A simulado: distribución previa uniforme en $[-12,12]$; sin guarda, riesgo global incondicional $P_{FA}=0,02646254$ y $P_{FR}=0,02659615$; con guarda $1$, $P_{FA}=0,00337106$ y $P_{FR}=0,08670579$. Se definió claramente el riesgo global como probabilidad conjunta en toda la población simulada, no como probabilidad condicionada a conformidad/no conformidad.
- Decisión dependiente simulada: $u_1=u_2=0,8$, correlación $0,75$, covarianza $0,48$; para el promedio, $u$ bajo falsa independencia $0,56568542$ y con covarianza $0,74833148$. Para valor verdadero $10,5$ y zona de aceptación $[-9,9]$, falsa aceptación calculada bajo el primer modelo $0,00400497$ y con dependencia $0,02251044$. El script imprime el resto de probabilidades de aceptación/rechazo utilizadas para comprobar los ejemplos.
- Todos los datos de ejemplo son simulados y no describen el SRP, Level 2 ni fotómetros de CALAIRE. Los límites publicados en QAPP/SOP/TAD y las concentraciones del BIPM son citas documentales, no cálculos o datos simulados.

### Referencias verificadas con `pdftotext`

Las páginas indicadas son páginas **PDF** donde se encontró el pasaje en la extracción; cuando se indica, se añade la paginación impresa del libro.

| Clave y numeral citado | Archivo en `docs/` | Página comprobada | Resultado |
|---|---|---:|---|
| Intro. Statistics in Metrology §§5.2 y 5.2.1.1 | `intro_stats_metro_c05.pdf` | PDF 2–3 (impresas 82–83) | Riesgo, TUR y falsa aceptación/rechazo verificados. |
| Metrology and Measurement Uncertainty §§8.1 y 8.5 | `metrology_measure_uncer_c08.pdf` | PDF 1 y 5 (impresa §8.5 en p. 234) | Definición de regla de decisión, conformidad y banda de guarda verificados. |
| ASQ Metrology Handbook, cap. 30, sección TUR sin numeral | `asq_metrological_handbook_c30.pdf` | PDF 2–4 (impresas 360–368) | El texto indica límites/interpretaciones del TUR; no se inventó numeral interno. |
| GUM (JCGM 100) §3.3.7 | `ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf` | PDF 15 | Define incertidumbre expandida y factor de cobertura. |
| ISO/TS 28037:2010 §5.7 | `ISO 28037.pdf` | PDF 16 | Uso de la función de calibración para predicción y evaluación; se cita solo como contexto de función de uso. |
| ISO/IEC 17025:2017 §§7.6, 7.8.6.1–7.8.6.2 | `BS EN ISO_IEC 17025_2017.pdf` | PDF 21 y 24 (cláusula 7.8.6 impresa p. 16) | Evaluación de incertidumbre y requisitos/reporting de regla de decisión verificados. |
| SRP QAPP §6.2.1 | `srp_qapp.pdf` | PDF 18 | Promedio de ciclos y pendiente/intercepto para comparación SRP #7–SRP regional verificados. |
| SRP QAPP, Tabla 7-1 | `srp_qapp.pdf` | PDF 23 | Ficha/resumen de especificaciones por estándar verificada. |
| SRP/SOP-1 §§9.1.1 y 9.1.3 | `srp_sop.pdf` | PDF 20 y 22 (páginas impresas 17 y 19) | Calificación y reverificación con sus pendientes, interceptos y ámbito verificados. |
| EPA TAD Tabla 4-1 | `o3_tad_508_20230906_final.pdf` | PDF 33 (impresa p. 19) | Tabla de requisitos de estándares de transferencia verificada. |
| EPA TAD §§4.4.1–4.4.2 | `o3_tad_508_20230906_final.pdf` | PDF 36 (impresa p. 22) | Requisitos de verificación/reverificación y estadísticos de ciclos verificados. |
| BIPM.QM-K1 §8 | `BIPM.QM-K1_2.protocol.pdf` | PDF 9 | Grado de equivalencia en los dos valores nominales de referencia común verificado. |

### Decisiones tomadas y pendientes

- Se siguió el alcance de `prop_e.md` §5, M10 aunque el mapa preliminar de `temario_curso.md` refleje la estructura anterior del módulo; para B/I/A mandó la propuesta final y su revisión.
- Los criterios QAPP, SRP/SOP-1 y EPA TAD se presentan con documento y etapa; se advierte que no son tolerancias universales ni se aplican automáticamente a certificados de clientes. Tras R01, el grado de equivalencia y la referencia a BIPM se retiraron del libreto M10 por corresponder a M9-A.
- El TUR fue definido expresamente como semitolerancia dividida por incertidumbre expandida, evitando una convención implícita. El riesgo global quedó definido como probabilidad incondicional sobre la distribución previa simulada.
- Se remitió a AX.2, AX.9 y AX.10 sin desarrollar las deducciones.
- Pendiente: VIM (JCGM 200:2012) no está disponible en `docs/`; por eso se citó sin numeral para la distinción terminológica compatibilidad/conformidad. El numeral pertinente queda sin verificar y no se atribuye a una ubicación específica.
- Pendiente de etapa posterior: revisión de sección. La revisión Haiku y las correcciones asociadas se registran en la sección siguiente.

## Correcciones (revisión Haiku)

| id del hallazgo | decisión | cambio hecho | ubicación | justificación |
|---|---|---|---|---|
| R01 | aplicado con cambios | Se retiró el desarrollo del grado de equivalencia y del protocolo BIPM; se dejó una remisión breve a M9-A y se expandió KCDB. | `M10_libreto.md`, intro de Nivel A | Mantiene el alcance de M10-A sin perder la orientación curricular; no se mantiene la referencia BIPM. |
| R02 | aplicado | La función ahora nombra $\hat{x}$ como valor corregido, $x_c$ como valor declarado del span y reporta $\hat{x}-y=-6,00$ nmol/mol. El script imprime ambos resultados. | `M10_libreto.md`, B1; `calc/M10_ejemplos.py` | Distingue el valor corregido de la corrección aditiva conforme a la convención de `guia_libreto.md` §4. |
| R03 | aplicado | Se añadió la advertencia `[ERROR CRÍTICO]` sobre la convención de signo y el efecto de invertirla. | `M10_libreto.md`, B1 | Previene aplicar la corrección en sentido contrario. |
| R04 | aplicado | Se atribuyó a ISO 28037 §5.7.1 la predicción inversa y su incertidumbre dependiente de $a$, $b$ y su covarianza; se acotó la nota de §5.7 a las condiciones de calibración. | `M10_libreto.md`, B1 | La reformulación refleja el contenido verificado del numeral, sin atribuirle requisitos sobre documentación del método. |
| R05 | aplicado | «Sección eficaz» se sustituyó por «especificación o norma aplicada». | `M10_libreto.md`, I2 | Corrige el término impropio en la lista de información del certificado. |
| R06 | aplicado | El escalamiento se dirige ahora a la persona responsable del modelo de covarianza del laboratorio. | `M10_libreto.md`, A2 | Evita que el nivel A se escale a sí mismo. |
| R07 | aplicado | Las señales B incorporan cambio de escala/unidad sin conversión y pocos grados de libertad que vuelven inadecuado $k=2$. | `M10_libreto.md`, Señales de escalamiento | Completa las señales básicas previstas por prop_e; es coherente con la convención de cobertura de la guía §4. |
| R08 | aplicado con cambios | Se citaron MMU §8.4 y Crowder 2020 §5.2.1.3 para falsa aceptación/rechazo. El riesgo global queda definido como probabilidad conjunta incondicional con cita disponible y nota explícita de numeral pendiente. | `M10_libreto.md`, I1 y A1 | Los numerales de riesgos específicos fueron comprobados; no se inventó una referencia para riesgo global. Pendiente bibliográfico conservado de forma transparente. |
| R09 | aplicado | Se añadió GUM §5.2.2, ec. (13), a la expresión de la varianza y se lee en voz alta la suma de varianzas más dos veces la covarianza, dividida entre cuatro. | `M10_libreto.md`, A2 | La fórmula es el caso de dos entradas correlacionadas de la propagación GUM. |
| R10 | aplicado | Se añadió ejemplo simulado: $U=1,2$ para un promedio no se traslada a una lectura individual con $s=1,5$; para esta, con $k=2$, $U=3,0$ nmol/mol. Se añadió el cálculo al script. | `M10_libreto.md`, I2; `calc/M10_ejemplos.py` | Muestra numéricamente la incoherencia entre presupuesto y uso y es reproducible. |
| R11 | aplicado | El desarrollo de compatibilidad se redujo a remisión a M9; se mantuvieron las dos cautelas que distinguen compatibilidad de conformidad. | `M10_libreto.md`, I2 | Evita duplicar el contenido asignado a M9-I sin quitar la aplicación pertinente a la regla. |
| R12 | aplicado | La introducción B cita ISO/IEC 17025 §§7.6 y 7.8.6.1, y la coherencia del presupuesto cita §7.6. | `M10_libreto.md`, intro B e I2 | Se vincula evaluación de incertidumbre con §7.6 y regla/riesgo con §7.8.6. |
| R13 | aplicado | La cita sobre compensación entre riesgos y banda de guarda se amplió a MMU §§8.4–8.5. | `M10_libreto.md`, B2 | §8.4 respalda el intercambio de riesgos y §8.5 la banda de guarda. |
| R14 | aplicado | Se declara $k=2$ como aproximación normal y se da la convención $k=t(0,975;\nu_{eff})$ para pocos grados de libertad en B1 e I1. | `M10_libreto.md`, B1 e I1 | Alinea los ejemplos con la convención de cobertura de la guía §4; los valores numéricos existentes se mantienen como aproximación pedagógica. |
| R15 | aplicado | I1 llama genéricas a las unidades del modelo; la primera referencia de I2 a ppb aclara la equivalencia con nmol/mol. | `M10_libreto.md`, I1 e I2 | Evita presentar unidades genéricas como unidades físicas y hace explícita la equivalencia indicada para la aplicación. |
| R16 | aplicado | Se verbalizaron $y\pm U$, $U=ku$ y $u=U/k=0,6$ en la narración. | `M10_libreto.md`, B1 | Cumple las pautas de lectura oral de las fórmulas en `guia_libreto.md` §§1 y 4. |
| R17 | aplicado | El párrafo de criterios se separó por documento/procedimiento, con citas en cada segmento. | `M10_libreto.md`, I2 | Reduce la carga oral y conserva las cifras y ámbitos verificados. |
| R18 | aplicado | Se expandieron KCDB y CMC en su primera mención. | `M10_libreto.md`, intro A y A2 | Desarrolla las siglas para operadores. |
| R19 | aplicado | Se cambió «rechazar o retener» por «rechazar» para la regla binaria de I1. | `M10_libreto.md`, I1 | Mantiene coherencia entre las decisiones contempladas por esa regla. |
| R20 | aplicado | Se añadió la referencia a Crowder 2020 §5.2.1.1, ec. (5.1), y se indicó la equivalencia de la fórmula para límites absolutos. | `M10_libreto.md`, I1 | Respaldada por la ecuación comprobada, sin asumir una convención universal de TUR. |
| R21 | aplicado | El criterio QAPP se expresa como valor absoluto del intercepto menor que 1 ppb, conservando la nota textual de Tabla 7-1. | `M10_libreto.md`, I2 | Evita sustituir la redacción del QAPP «<+ 1 ppb» por «0±1». |
| R22 | aplicado con cambios | Se estandarizaron las claves bibliográficas, se retiraron notas de verificación del listado, se quitó BIPM al eliminar el tema, y se corrigió el título de EPA-TAD. | `M10_libreto.md`, ficha, citas y referencias | La fecha/versionado BIPM dejó de ser pertinente al suprimirse su contenido, no se conservó una referencia innecesaria. |
| R23 | aplicado | El cierre indica que la acción se aplica tal como está acordada, sin modificarla para obtener un resultado favorable. | `M10_libreto.md`, Cierre | Elimina la ambigüedad sintáctica detectada. |
| R24 | aplicado | Se aclaró en B1 que tolerancia y especificación se usan como sinónimos y no equivalen al límite de control. | `M10_libreto.md`, B1 | Sigue la terminología de Crowder 2020 §5.2.1.1 y conserva la distinción operativa con límites de control. |

**Correcciones adicionales por iniciativa propia**

- Se actualizaron en esta bitácora los resultados y etiquetas del ejemplo de corrección: valor corregido $\hat{x}=199,00$ nmol/mol y corrección aditiva $-6,00$ nmol/mol; también se registró el nuevo cálculo de incertidumbre para lectura individual.
- Se ajustó la ficha de referencias del libreto para que use las claves definidas en `guia_libreto.md` y que la fuente indicada en cada cita tenga entrada bibliográfica completa.
- Se mantuvo la advertencia de que los criterios QAPP/SRP-SOP/EPA-TAD solo aplican a sus procedimientos y etapas; no son reglas universales de conformidad.
- Recalculación verificada con `curso/.venv/bin/python -I curso/S3_comparacion_decision/calc/M10_ejemplos.py`: los resultados numéricos previos permanecen idénticos; se añadieron los dos valores de corrección y $U=3,0$ nmol/mol para la lectura individual.
- **Decisión S-M10-01:** se separó la práctica A en tres subcasos con modelo, objeto de decisión, evento y condicionamiento explícitos: riesgo global de una medición individual con $u=0,8$ y previa uniforme; probabilidad condicional de falsa aceptación del promedio correlacionado en $\theta=10,5$; y riesgo específico posterior para una medición individual $y=0,u=6$. La cifra $u(\bar Y)=0,74833148$ queda restringida al promedio correlacionado; los riesgos globales conservan el modelo individual de $u=0,8$ del script. Se conservaron las cifras verificadas y se corrigió el enunciado/solución para no atribuir los riesgos globales al promedio.
