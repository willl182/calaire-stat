# Revisión de redacción y errores — M10. Reglas de decisión y riesgo

## Plan de revisión

**Qué se revisó.** `curso/S3_comparacion_decision/M10_libreto.md` completo (5 071 palabras aprox.), contra:

- `curso/guia_libreto.md` §§1–8 (forma, convenciones, referencias, anexos).
- `prop_e.md`: §2 (señales del básico), §3 (convenciones), §5 (M9 y M10), §6 (inclusiones y exclusiones), §8 (errores críticos y evaluación), §9–§10.
- `curso/S3_comparacion_decision/M10_bitacora_luna.md` (plan, datos y pendientes).
- `curso/S3_comparacion_decision/calc/M10_ejemplos.py`, ejecutado con `curso/.venv/bin/python -I` para comparar cada número del libreto con la salida.

**Cómo.**

1. Lectura completa del libreto, escena por escena, con atención a redacción para voz alta, terminología, signos y unidades.
2. Recalculo de todos los números del libreto con el script y comprobación a mano de las fórmulas y de las cifras derivadas.
3. Comprobación de formato con búsquedas: viñetas en contenido narrado, etiquetas de acotación, decimales con punto, citas entre corchetes, marcadores de práctica.
4. Verificación de referencias: extracción de texto con `pdftotext -layout` de los documentos de `docs/` a `/tmp/m10rev` (fuera del repositorio) y búsqueda de cada numeral citado. Ningún archivo de `docs/` se modificó.
5. Cobertura: comparación de cada nivel con su asignación en prop_e §5 y con las exclusiones de prop_e §6.

No se editó el libreto. No se revisaron las páginas impresas que la bitácora indica; se comprobaron numerales y textos.

## Hallazgos

| id | ubicación (escena y texto citado) | tipo | severidad | problema | corrección propuesta |
|---|---|---|---|---|---|
| R01 | Nivel A, intro: «En una comparación frente a una referencia común, el grado de equivalencia se expresa como diferencia… el protocolo BIPM.QM-K1 presenta esa evaluación en dos concentraciones nominales, 80 y 420 nmol/mol [BIPM.QM-K1, §8]» | alcance | mayor | prop_e §5 asigna el grado de equivalencia frente a referencia común (caso BIPM.QM-K1) a **M9-A**. M10-A solo tiene riesgo específico y global, requisitos bilaterales y decisiones con dependencia. El libreto introduce un tema de M9 como si fuera de M10 (guía §3: «sin quitar ni añadir temas») y duplica AX.9. | Suprimir las frases sobre grado de equivalencia, protocolo y «Esa magnitud describe una comparación…». Conservar la exclusión de KCDB y de la organización del protocolo. Quitar la cita [BIPM.QM-K1, §8] y su entrada en «Referencias del capítulo», o dejar una remisión: «el grado de equivalencia frente a referencia común se vio en M9-A». |
| R02 | Escena B1: «…escribimos $c=(y-y_0)\,c_c/(y_c-y_0)$… la corrección resulta $c=199,00$ nmol/mol» | terminología / cálculo | mayor | La fórmula da el **valor corregido** $\hat x$ (199,00 nmol/mol), no una corrección. La guía §4 define la corrección aditiva como $\hat x - y$, que sería −6,00 nmol/mol. Además $c_c = 398$ es un valor de referencia del span, no una corrección. `M10_ejemplos.py` imprime «corrección aplicada c» (líneas 37–39), con el mismo error. | Llamar $\hat x$ al valor corregido. Escribir la corrección aditiva $\hat x - y = -6{,}00$ nmol/mol. Llamar a $c_c$ «valor declarado del span». Cambiar el script para imprimir $\hat x$ y $\hat x - y$, y actualizar la bitácora. |
| R03 | Escena B1, después de la fórmula de la función de uso: no hay advertencia sobre el signo | contenido | mayor | prop_e §8 lista «invertir el signo de una corrección» como error crítico. El libreto introduce una corrección sin decir su convención de signo ni advertir del error. | Añadir `[ERROR CRÍTICO]`: «La corrección aditiva es valor corregido menos indicación, $\hat x - y$. Con 199,00 y 205 nmol/mol da −6,00 nmol/mol. Si se invierte el signo, el ajuste se aplica al revés.» |
| R04 | Escena B1: «La función y sus entradas deben describirse como parte del método de uso [ISO/TS 28037:2010, §5.7]» | referencia | mayor | La atribución no coincide con el texto. ISO/TS 28037 §5.7.1 describe la predicción inversa, en la que la incertidumbre usa $a$, $b$ y su covarianza. La nota de §5.7 supone que las condiciones de la calibración se mantienen. No dice que la función deba describirse como parte del método. | Reformular: «La predicción inversa usa la función de calibración; su incertidumbre depende de $a$, $b$ y de su covarianza [ISO/TS 28037:2010, §5.7.1]. La nota de §5.7 supone que las condiciones de la calibración se mantienen.» |
| R05 | Escena I2: «…la trazabilidad pertinente, la sección eficaz usada y la regla de decisión» | redacción / terminología | mayor | «Sección eficaz» (sección transversal de absorción) no tiene sentido en la lista de contenido de un certificado. Es un error de término. | «…la trazabilidad pertinente, la especificación o norma aplicada y la regla de decisión.» |
| R06 | Escena A2, último párrafo de la sección: «…no supongan independencia sin justificación; deténganse y escalen la formulación del modelo a A.» | redacción / alcance | mayor | Está en el nivel A y pide escalar «a A». Es contradictorio. La señal de I2 escala a quien modele la covarianza; aquí debe decir lo mismo. | «…deténganse y escalen la formulación del modelo a la persona responsable del modelo de covarianza del laboratorio.» |
| R07 | Señales de escalamiento (Nivel B): lista de señales | contenido | mayor | prop_e §2 lista como señales del básico, entre otras, «cambio de escala» y «pocos grados de libertad». La lista del capítulo no las incluye. El cambio de escala aparece en B1 sin señal asociada. Los pocos grados de libertad afectan a $k=2$ (ver R14). | Añadir a la lista: «si hay cambio de escala o de unidad sin conversión documentada; si los grados de libertad son tan pocos que $k=2$ no es razonable». |
| R08 | Escena I1: «La probabilidad de falsa aceptación en un valor verdadero θ fuera de tolerancia es…»; Escena A1: «definimos riesgo global de falsa aceptación como la probabilidad conjunta…» | referencia | mayor | Son definiciones sin referencia; la guía §5 exige referencia para toda definición. Hay fuentes verificadas para falso positivo/negativo: MMU cap. 8 §8.4, y Crowder 2020 cap. 5 §5.2.1.3 (título «False Accept and False Reject Risks»). Para el riesgo global (promedio sobre una distribución de θ) no hay numeral verificado en `docs/`. | En I1: «[MMU cap. 8, §8.4; Crowder 2020, cap. 5, §5.2.1.3]». En A1: «[Crowder 2020, cap. 5, §5.2.1.3; definición de riesgo global sin numeral verificado, pendiente en bitácora]». Anotar el pendiente en la bitácora. |
| R09 | Escena A2, diapositiva: $u^2(\bar Y)=[u_1^2+u_2^2+2\operatorname{cov}(Y_1,Y_2)]/4$; luego «…el cálculo da… 0,74833148» | referencia / lectura | mayor | La fórmula no tiene referencia (guía §5). Es un caso particular de la propagación con entradas correlacionadas: GUM §5.2.2, ec. (13) (verificado). En la narración la fórmula no se dice en palabras (guía §1 y §4). | Añadir «[GUM, §5.2.2, ec. (13)]» junto a la explicación. Decir en voz alta: «la varianza del promedio es la suma de las dos varianzas, más dos veces la covarianza, dividido entre cuatro». |
| R10 | Escena I2 completa: «coherencia entre presupuesto y declaración» | contenido | mayor | La guía §3 exige, en cada tema cuantitativo, al menos un ejemplo resuelto con números. I2 trata la coherencia de forma cuantitativa, pero solo cita criterios publicados y no tiene ejemplo. | Añadir un ejemplo simulado: con $\sigma = 1{,}5$ nmol/mol (lectura individual, simulada), la declaración de $U = 1{,}2$ nmol/mol del promedio no sirve para una lectura. Para una lectura, $U = 2 \times 1{,}5 = 3{,}0$ nmol/mol. Incluir el cálculo en `calc/M10_ejemplos.py`. |
| R11 | Escena I2: «Compatibilidad y conformidad tampoco son sinónimos… la compatibilidad pregunta si la diferencia observada es coherente…» | alcance | menor | «Compatibilidad frente a conformidad» es contenido de M9-I (prop_e §5, M9). M10-I lo narra de nuevo en un párrafo largo. | Reducirlo a una remisión («la compatibilidad se vio en M9; aquí importa para la regla»). Conservar las dos frases sobre conformidad: «Una diferencia compatible con cero no demuestra… ni una diferencia detectable demuestra por sí sola falta de conformidad». |
| R12 | Intro del Nivel B: «…determina cómo se toma en cuenta la incertidumbre [Metrology and Measurement Uncertainty, cap. 8, §8.1; ISO/IEC 17025:2017, §7.8.6.1]»; ficha: «ISO/IEC 17025:2017 §§7.6 y 7.8.6» | referencia | menor | §7.8.6.1 trata del nivel de riesgo y los supuestos estadísticos, no de la incertidumbre. La evaluación de la incertidumbre es §7.6 (verificado). §7.6 aparece en la ficha pero no se cita en ninguna escena. | Citar «[…; ISO/IEC 17025:2017, §§7.6 y 7.8.6.1]» en la intro, y citar §7.6 donde se hable de U (B1 o I2). Si no se usa, quitarlo de la ficha. |
| R13 | Escena B2: «Esa protección tiene un costo: aumenta la posibilidad de retener o rechazar resultados que en realidad cumplen… [Metrology and Measurement Uncertainty, cap. 8, §8.5]» | referencia | menor | La idea de que reducir un riesgo aumenta el otro está en MMU §8.4, que es donde la cita dice «at the cost of increasing the other». §8.5 trata la banda de guarda. | «[Metrology and Measurement Uncertainty, cap. 8, §§8.4–8.5]». |
| R14 | Escena B1: «…$k=2$…» y Escena I1: «…$U=2u=1,6$ como aproximación de cobertura del noventa y cinco por ciento» | convención | menor | La guía §4 fija para el 95 % bilateral con Student $k = t(0{,}975;\nu_{eff})$. El libreto usa $k=2$ sin decir que es una aproximación normal que no ajusta los grados de libertad. | En B1, tras «$k=2$»: «es una aproximación normal; con pocos grados de libertad, la convención del curso es $k = t(0{,}975;\nu_{eff})$». En I1, remitir a la misma frase. |
| R15 | Escena I1: «incertidumbre estándar simulada de 0,8 unidades»; «desde menos diez hasta más diez unidades». Escena I2: «…intercepto de 0±4 ppb…» (ppb) | unidades | menor | La guía §4 fija nmol/mol. En I1 las unidades son genéricas sin declararlo. En I2 aparece «ppb» sin equivalencia, aunque prop_e §3 dice que nmol/mol equivale a ppb en esta aplicación. | En I1, decir «unidades genéricas del modelo pedagógico» o usar nmol/mol. En el primer uso de ppb en I2, escribir «ppb (equivalente a nmol/mol)». |
| R16 | Escena B1: «…expresarse como $y \pm U$, donde $U=k\,u$…»; «…el valor estándar asociado es $u=U/k=0,6$ nmol/mol» | redacción (lectura en voz alta) | menor | Guía §1 y §4: las fórmulas se dicen en palabras en la narración. Aquí están solo escritas. | Decir: «y más o menos U; U igual a k por u». Y: «u igual a U entre k, es decir, 0,6 nmol/mol». |
| R17 | Escena I2, párrafo «Miremos los números publicados para fijar el alcance…» | redacción | menor | Una sola frase larga con cuatro documentos y once cifras. Es difícil de decir en voz alta y contradice la guía §1 (frases cortas). | Dividir en un párrafo por documento (SRP QAPP §6.2.1, SRP/SOP-1 §9.1.1, SRP/SOP-1 §9.1.3, EPA TAD §4.4.1 y §4.4.2), cada uno con su cita. No cambiar las cifras. |
| R18 | Escena A2, último párrafo: «…una probabilidad calculada no aprueba… ni una CMC.»; Escena A intro: «…ni estudiamos la KCDB» | redacción / terminología | menor | Siglas sin definir para operadores (CMC, KCDB). | «…ni una capacidad de medición y calibración (CMC) declarada». «…la base de datos de comparaciones clave (KCDB)». |
| R19 | Escena I1: «…la probabilidad de rechazar o retener un valor verdadero que sí está dentro» | coherencia | menor | I1 usa una regla binaria (aceptar o rechazar). «Retener» aparece solo en B2, con zona intermedia. | «…la probabilidad de rechazar un valor verdadero que sí está dentro». |
| R20 | Escena I1: «…defino el TUR como la semiamplitud de la especificación dividida por esa incertidumbre expandida: $10/1,6=6,25$» | referencia | menor | La definición coincide con la ec. (5.1) de Crowder 2020 §5.2.1.1 para límites absolutos, $(SL_U - SL_L)/(2U_c)$ (verificado). El libreto no lo dice, aunque dice que hay convenciones distintas. | Citar «[Intro. Statistics in Metrology, §5.2.1.1, ec. (5.1)]» y señalar que la fórmula del curso es la misma para límites absolutos. |
| R21 | Escena I2: «…un intercepto de $0\pm1$ ppb para que el promedio de ciclos sea aceptable» (SRP QAPP §6.2.1) | cita | menor | El QAPP escribe «intercept must be + 1ppb» (§6.2.1) y, en la Tabla 7-1, «intercept <+ 1 ppb». «0±1» no es la redacción del documento. | «intercepto de valor absoluto menor que 1 ppb (QAPP, Tabla 7-1: «<+ 1 ppb»)». |
| R22 | «Referencias del capítulo»: entradas de BIPM.QM-K1, EPA TAD, SRP/SOP-1, MMU e Intro; claves usadas en la narración | formato de referencias | menor | (a) Las claves de la narración (p. ej. «Intro. Statistics in Metrology», «EPA TAD», «BIPM.QM-K1») no coinciden con las de la tabla de la guía §5 (Crowder 2020, EPA-TAD, BIPM-K1, MMU). (b) Las entradas llevan notas de trabajo («numerales verificados en la extracción de texto»; «Capítulo consultado en docs/…») que pertenecen a la bitácora. (c) BIPM: «v2.1, 9-10-2025» es ambiguo; el documento tiene fecha «09 Oct. 25», y el §8 es del Protocolo A (el §10 es del Protocolo B). (d) TAD: el título tiene un «the» que el documento no tiene. | Usar las claves de la guía §5 en narración y lista. Trasladar las notas de verificación a la bitácora. Escribir «9 de octubre de 2025» y «Protocolo A, §8». Usar el título TAD exacto: «Transfer Standards for Calibration of Air Monitoring Analyzers for Ozone». |
| R23 | Cierre del capítulo: «…aplican la acción prevista sin cambiarla para obtener un resultado conveniente» | redacción | menor | Frase ambigua: al leerla en voz alta puede entenderse como que se cambia la acción para obtener un resultado conveniente. | «…y aplican la acción prevista tal como está acordada, sin modificarla para obtener un resultado favorable». |
| R24 | Escenas B1 y A2: «la tolerancia», «la especificación bilateral», «el límite» | terminología | menor | Los términos tolerancia, especificación y límite se usan como sinónimos sin decirlo. Crowder 2020 §5.2.1.1 los trata como intercambiables; el libreto los distingue de límite de control en I2. | En B1, añadir: «tolerancia y especificación se usan como sinónimos; no se confunden con el límite de control». |

## Verificaciones hechas

### Cálculos (script `calc/M10_ejemplos.py` con `curso/.venv/bin/python -I`)

Todas las cifras del libreto coinciden con la salida del script:

| Cifra en el libreto | Salida del script | Resultado |
|---|---|---|
| B2: intervalos $[98{,}8;101{,}2]$, $[101{,}0;103{,}4]$, $[104{,}8;107{,}2]$; decisiones aceptar, zona intermedia, rechazar | idénticos; decisión por caso | Coincide |
| B1: $u = U/k = 0{,}6$ | 0.6 | Coincide |
| B1: corrección $c = 199{,}00$ | 199.00 | Coincide (nombre erróneo, ver R02) |
| I1: TUR $= 6{,}25$ | 6.250 | Coincide |
| I1, sin guarda, $\theta=9$: $P_R = 0{,}10564977$ | 0.10564977 | Coincide |
| I1, con guarda 1, $\theta=9$: $P_R = 0{,}5$ | 0.50000000 | Coincide |
| I1, sin guarda, $\theta=10{,}5$: $P_{FA} = 0{,}26598553$ | 0.26598553 | Coincide |
| I1, con guarda 1, $\theta=10{,}5$: $P_{FA} = 0{,}03039636$ | 0.03039636 | Coincide |
| A1, sin guarda: $FA_{glob} = 0{,}02646254$; $FR_{glob} = 0{,}02659615$ | 0.02646254; 0.02659615 | Coincide |
| A1, con guarda 1: $FA_{glob} = 0{,}00337106$; $FR_{glob} = 0{,}08670579$ | 0.00337106; 0.08670579 | Coincide |
| A2: $u_{ind} = 0{,}56568542$; $u_{dep} = 0{,}74833148$; cov $= 0{,}48$ | 0.56568542; 0.74833148; 0.48 | Coincide |
| A2: $P_{FA}$ independiente $= 0{,}00400497$; con dependencia $= 0{,}02251044$ | 0.00400497; 0.02251044 | Coincide |

Comprobaciones a mano, fuera del script:

- $0{,}75 \times 0{,}8 \times 0{,}8 = 0{,}48$. Correcto.
- $\sqrt{0{,}64\cdot 2/4} = \sqrt{0{,}32} = 0{,}565685$; $\sqrt{(1{,}28+0{,}96)/4} = \sqrt{0{,}56} = 0{,}748331$. Correcto.
- $10/1{,}6 = 6{,}25$. Igual a $(SL_U-SL_L)/(2U)=20/3{,}2=6{,}25$ de Crowder ec. (5.1). Correcto.
- $(205-5)\cdot 398/(405-5) = 199{,}00$; $199{,}00-205 = -6{,}00$ nmol/mol. Correcto (R02).
- $P_R(\theta=9)$ sin guarda $= 1-[\Phi(1{,}25)-\Phi(-23{,}75)] = 1-0{,}89435 = 0{,}10565$. Correcto.
- Denominador de los riesgos globales: $24 = 12-(-12)$, longitud de la distribución uniforme. Correcto.
- Cálculo con el signo de la corrección (R03): aplicar la regla $\hat x - y$ con datos de B1 da −6,00. Correcto.

Ningún número del libreto está mal calculado. Los problemas son de nombre, de convención y de atribución (R02, R03, R14).

### Referencias comprobadas con `pdftotext -layout`

| Clave y numeral citado | Documento | Resultado |
|---|---|---|
| GUM §3.3.7 (U = k·u_c) | `ISO_IEC Guide 98-3_2008 … libgen.li.pdf` | Coincide: «expanded uncertainty U is obtained by multiplying the combined standard uncertainty uc by a coverage factor k». |
| GUM §5.2.2, ec. (13) (entradas correlacionadas) | mismo | Existe: «When the input quantities are correlated, the appropriate expression… Equation (13)». Se propone para R09. |
| GUM §5.1.2, ec. (10) | mismo | Existe; se usa solo como referencia de la ec. (13). |
| ISO/TS 28037 §5.7 y §5.7.1 | `ISO 28037.pdf` | §5.7 existe. §5.7.1 trata la predicción inversa. La frase «deben describirse como parte del método» no aparece (R04). |
| ISO/IEC 17025 §7.6 | `BS EN ISO_IEC 17025_2017.pdf` | Existe: «Evaluation of measurement uncertainty». No se cita en la narración (R12). |
| ISO/IEC 17025 §§7.8.6.1–7.8.6.2 | mismo | Contenido verificado: documentar la regla considerando el nivel de riesgo; informar cuándo la regla no es inherente. Correcto en I2 y B2. En la intro, la palabra «incertidumbre» no aparece en §7.8.6.1 (R12). |
| MMU cap. 8: §8.1 «Statement of Conformity and Decision Rules»; §8.4 «False Positive and False Negative»; §8.5 «Decision Rules and Guard Band» | `metrology_measure_uncer_c08.pdf` | Existen. §8.5 indica que la banda de guarda se define generalmente como U. §8.4 indica que reducir un riesgo aumenta el otro (R13). |
| MMU, título del capítulo | mismo | «Measurement Uncertainty in Conformity Assessment»; coincide con la referencia. |
| Crowder 2020, cap. 5 «Measurement Uncertainty in Decision Making»; §5.2; §5.2.1.1 ec. (5.1) | `intro_stats_metro_c05.pdf` y libro completo | Existen. Ec. (5.1) para límites absolutos = $(SL_U-SL_L)/(2U_c)$ (R20). Autores Stephen Crowder, Collin Delker, Eric Forrest, Nevin Martin; Springer Nature 2020: coinciden. |
| Crowder §5.2.1.3 «False Accept and False Reject Risks»; §5.2.1.4 «Guardbanding»; §5.2.1.5 «Risk with Biased Measurements» | libro completo | Títulos verificados; se proponen para R08. |
| ASQ Metrology Handbook, cap. 30 «Measurement Risk and Decision Rules»; sección TUR | `asq_metrological_handbook_c30.pdf` | Existe. Tercera edición (libro: «third edition»), © 2013, 2022; editor Heather A. Wade. La editorial «ASQ Quality Press» no se verificó en la extracción. |
| SRP QAPP §6.2.1 y Tabla 7-1 | `srp_qapp.pdf` | Título «Quality Assurance Project Plan for the Standard Reference Photometer Program», febrero de 2017: coincide. Pendiente 1.00 ± 0.01 y promedio de ciclos: coincide. Intercepto redactado como «+ 1 ppb»/«<+ 1 ppb» (R21). |
| SRP/SOP-1 §9.1.1 | `srp_sop.pdf` | Calificación: pendiente 1 ± 0,04; intercepto 0 ± 4 ppb. Coincide. |
| SRP/SOP-1 §9.1.3 | mismo | «Re-Verification», rango completo, pendiente 1 ± 0,03, intercepto 0 ± 3 ppb; «Re-Verification: Annual» (línea 814). Coincide. Puede correrse en Level 2. |
| SRP/SOP-1, título y revisión | mismo | Revisión 1, vigente desde el 18 de septiembre de 2015. Documento interno de OAQPS. Coincide con «rev. 1, 2015». |
| EPA TAD Tabla 4-1 | `o3_tad_508_20230906_final.pdf` | Pendientes 1,00 ± 0,03; intercepto 0 ± 3 ppb; desviación estándar de pendientes < 0,0075; de interceptos < 1,00 ppb; reverificación anual. Coincide. |
| EPA TAD §4.4.1 | mismo | Tres ciclos: 1,00 ± 0,03; 0 ± 3 ppb; SD pendientes < 0,0075; SD interceptos < 1,00 ppb. Coincide literalmente. |
| EPA TAD §4.4.2 | mismo | Requisitos de reverificación para Levels 2 y 3. Coincide. |
| EPA TAD, título | mismo | «Transfer Standards for Calibration of Air Monitoring Analyzers for Ozone»; el libreto añade «the» (R22). EPA-454/B-22-003 coincide con el libreto. |
| BIPM.QM-K1, §8 «Degrees of equivalence» | `BIPM.QM-K1_2.protocol.pdf` | Existe en el Protocolo A: 80 y 420 nmol/mol; $D = x_{NS} - x_{SRP27}$, con SRP27 como referencia común. El §10 (Protocolo B) es otra sección con el mismo título. No se encontró un KCRV combinado como referencia del grado de equivalencia; la exclusión de §6 se respeta, pero el tema es de M9-A (R01). |
| BIPM.QM-K1, versión y fecha | mismo | «protocol v2.1», «09 Oct. 25»; el libreto escribe «9-10-2025» (R22). |
| VIM (JCGM 200) | no disponible en `docs/` | No verificado. Se cita sin numeral, como indica la guía §5. |

### Formato y estructura

- Sin viñetas ni listas numeradas en el contenido narrado (búsqueda de `^\s*[-*+]` y `^\s*[0-9]+\.` sin resultados fuera de la ficha y las referencias).
- Etiquetas de acotación usadas: `[DIAPOSITIVA]`, `[PIZARRA]`, `[EJEMPLO]`, `[PREGUNTA AL GRUPO]` (2, con respuesta esperada), `[ERROR CRÍTICO]` (4), `[ESCALAMIENTO]` (1). Todas están en la lista permitida por la guía §1.
- Tres marcadores `[PRÁCTICA — fase de ejercicios]`, uno por nivel. Los títulos coinciden con prop_e §5 M10: B «Completar un certificado docente y resolver resultados dentro, cerca y fuera del límite»; I «Resolver un resultado próximo al límite con dos reglas y explicar el riesgo que asume cada una»; A «Cuantificar el riesgo de una decisión para una distribución y una especificación definidas». No hay enunciados, soluciones ni rúbricas.
- Estructura de la guía §2: ficha, Nivel B (B1, B2, marcador, señales), Nivel I (I1, I2, marcador), Nivel A (A1, A2, marcador), cierre y referencias. Correcta.
- Decimales con coma en el texto y en las fórmulas. Se encontraron puntos decimales solo en el texto de la ficha y en el nombre «Level 2» (no son cifras). No hay errores.
- Ningún libreto menciona deducciones en clase: AX.10, AX.2 y AX.9 se remiten con frases del tipo «aquí las usamos». Correcto (guía §3).
- Nota para la guía (no es un hallazgo del libreto): la guía §1 escribe el marcador como cita anidada («> >»), mientras que el §2 y el libreto usan cita simple. El libreto sigue el §2. Conviene unificar en la guía.

### Cobertura frente a prop_e

| Nivel | Asignación de prop_e §5 | Dónde aparece en el libreto | Estado |
|---|---|---|---|
| B | resultado, U, k, intervalo, función de uso; regla suministrada; banda de guarda; acción cerca del límite | B1 (resultado, U, k, intervalo, función); B2 (regla, banda, acción); señales | Completo. Señales incompletas (R07) |
| I | selección y justificación de reglas; riesgo FA/FR; relación U–tolerancia; coherencia presupuesto–declaración | I1 (regla, banda, FA/FR, TUR); I2 (coherencia, ficha de criterios, certificado) | Completo. Ejemplo numérico de coherencia ausente (R10). Compatibilidad duplica M9 (R11) |
| A | riesgo específico y global; requisitos bilaterales; decisiones con dependencia | A1 (específico y global); A2 (bilateral y dependencia) | Completo. Añade grado de equivalencia de M9-A (R01) |

Exclusiones de prop_e §6, revisadas una por una: ensayos de aptitud, ISO 13528, PCR/PLS, Allan, GGMR con $V_{xy}\neq 0$, KCRV combinado, valores de diseño ambientales y promedios regulatorios: no aparecen. KCDB aparece solo para excluirla. El «promedio de ciclos» de SRP QAPP §6.2.1 es un criterio de verificación de un patrón, no un promedio regulatorio ambiental; no se considera infracción. El protocolo BIPM se usa para el grado de equivalencia; esa parte sobra (R01).

## Resumen

- **Libreto:** redactado con cuidado, sin viñetas, con etiquetas correctas, marcadores de práctica bien formados y estructura de la guía §2. Los números coinciden exactamente con el script. Las cifras de QAPP, SRP/SOP-1 y TAD son fieles al texto de los documentos.
- **Hallazgos:** 0 críticos, 10 mayores y 14 menores (24 en total).
- **Mayores que conviene corregir antes de la revisión de sección:**
  - R01: el grado de equivalencia de BIPM es de M9-A, no de M10-A.
  - R02 y R03: la función de corrección produce un valor corregido, no una corrección; falta la advertencia de signo que prop_e §8 exige.
  - R04: la atribución a ISO/TS 28037 §5.7 no es literal.
  - R05: «sección eficaz» es un término incorrecto.
  - R06: el nivel A pide escalar «a A».
  - R07: las señales de escalamiento de B omiten cambio de escala y pocos grados de libertad.
  - R08 y R09: definiciones y una fórmula sin referencia.
  - R10: falta un ejemplo numérico de coherencia entre presupuesto y declaración.
- **Pendiente de confirmar por el autor:** la definición de riesgo global no tiene numeral verificado en `docs/` (R08); el VIM no está en `docs/`.
- **No se hizo:** no se editó el libreto; no se modificó `docs/`; el script no se cambió (las correcciones de R02 y R10 requieren cambiarlo, y eso corresponde al desarrollador).
