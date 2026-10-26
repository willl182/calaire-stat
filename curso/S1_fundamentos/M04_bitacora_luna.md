# Bitácora de desarrollo — M04

## Plan

### Alcance por nivel (texto literal de prop_e.md §5, M4)

- **B:** grados de libertad; intervalo de confianza con t; hipótesis, valor p y errores de decisión; prueba t de un error medio en un nivel, con la unidad de repetición justificada en el enunciado.
  - *Práctica:* calcular el intervalo del error medio del Level 2 en un nivel y contrastarlo con cero y con una magnitud relevante.
- **I añade:** t pareada y Welch; intervalos y pruebas sobre varianzas (chi-cuadrado, F); potencia y tamaño de muestra según el diseño (media, pareadas, dos grupos); incertidumbre de una desviación estimada; pruebas de Grubbs y Dixon solo bajo sus condiciones de aplicación.
  - *Práctica evaluable:* resolver un apartado distinto para cada familia: selección, cálculo e interpretación de t pareada y Welch; intervalo y contraste de varianzas con chi-cuadrado/F; cálculo de potencia o tamaño muestral para media, pares y dos grupos; incertidumbre de una desviación estimada; evaluación de los supuestos y conclusión de Grubbs y Dixon. La rúbrica registra método, supuestos, resultado e interpretación por apartado.
- **A añade:** multiplicidad; pruebas de equivalencia con márgenes definidos; consistencia por chi-cuadrado.
  - *Práctica:* un caso donde «no rechazar cero» y «demostrar equivalencia» llevan a conclusiones distintas.

Restricciones de alcance que se aplicarán en el libreto: niveles acumulativos; M04-B solo desarrolla inferencia para la media de un error en un nivel; I añade los métodos expresamente enumerados; A añade multiplicidad, equivalencia y consistencia chi-cuadrado. Prerrequisitos estadísticos según prop_e §5 M3: distribución t, cuantiles y grados de libertad para B; covarianza/correlación y chi-cuadrado/F para I. No importar temas del temario antiguo que no estén en el M4 final de prop_e. Las prácticas no se desarrollan en esta fase: marcador únicamente.

### Escenas previstas

- Ficha del capítulo: competencia estadística, prerrequisitos, alcance B/I/A, rótulos de origen de datos, anexos y claves bibliográficas.
- B1 — de la muestra al estimador: muestreo aleatorio, estimador/estadístico, sesgo, varianza del estimador y grados de libertad.
- B2 — incertidumbre de la media: distribución muestral, TCL, error estándar e intervalo de confianza normal/t.
- B3 — contrastar el error medio: H0/H1, estadístico t de una muestra, región crítica, α, valor p, errores tipo I/II y relevancia metrológica; ejemplo del Level 2 en un nivel.
- Marcador de práctica B y señales de escalamiento.
- I1 — seleccionar y leer las pruebas t pareada y Welch; ejemplos numéricos, unidad experimental y dependencia.
- I2 — inferencia sobre varianzas mediante chi-cuadrado y F; intervalo y contraste; ejemplo numérico.
- I3 — potencia y tamaño de muestra para media, pares y dos grupos; ejemplo numérico con supuestos explícitos.
- I4 — incertidumbre de una desviación estándar estimada; ejemplo numérico.
- I5 — valores atípicos: Grubbs y Dixon, condiciones, interpretación y prohibición de eliminación automática; ejemplo numérico ilustrativo sin convertirlo en ejercicio.
- Marcador de práctica evaluable I.
- A1 — multiplicidad: familia de hipótesis, error familiar y ajuste ilustrativo.
- A2 — equivalencia: márgenes predefinidos, TOST e interpretación distinta de «no rechazar cero»; ejemplo numérico.
- A3 — consistencia mediante chi-cuadrado, modelo/estadístico y ejemplo numérico.
- Marcador de práctica A.
- Cierre narrado con síntesis acumulativa y transición a M05; referencias del capítulo.

### Datos y rótulo de origen

- Ejemplo base de error medio: datos docentes simulados de errores emparejados indicación–referencia de un único nivel del Level 2; se declarará que son una muestra ilustrativa generada en el script, no resultados de CALAIRE. Usar unidad de repetición explícita (una unidad independiente por día/ciclo docente), evitar llamar independientes a lecturas consecutivas.
- Ejemplos de I (pareadas, Welch, varianzas, potencia, desviación estimada, Grubbs/Dixon), A (multiplicidad, equivalencia, consistencia): vectores pequeños generados en scripts Python reproducibles, todos rotulados **simulado**; se declararán los supuestos y el diseño que representan.
- Contexto de campaña: la guía §6 indica como fuente propia el certificado F-PSMT-01 (`docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm`, Level 2 contra SRP 55; 12 puntos × 8 lecturas × 6 días). No presentar extractos o cálculos del certificado como si fueran la unidad experimental independiente. Se usará solo para nombrar el caso, salvo que el script documente una extracción limpia y estructura justificable.
- No se usarán datos publicados ni adaptados en este capítulo salvo que sean necesarios para una afirmación; la inferencia no requiere un ejemplo histórico del SRP.

### Cálculos previstos

Crear scripts `curso/.venv/bin/python` en `curso/S1_fundamentos/calc/M04_*.py`, con semillas fijas y resultados impresos/documentados. Todos los números que aparezcan en el libreto (datos de ejemplo, estimaciones, estadísticos, límites, valores p, potencias, tamaños muestrales, cuantiles, incertidumbres y decisiones numéricas) deberán reproducirse en uno de esos scripts. Prever: intervalo t y prueba t de una muestra; t pareada y Welch; intervalo/contraste chi-cuadrado y F; potencias/tamaños muestrales para media, diferencias pareadas y dos grupos; incertidumbre de s; estadísticos de Grubbs/Dixon; ajuste por multiplicidad; dos pruebas TOST con margen declarado; estadístico chi-cuadrado de consistencia. Validar cuantiles con scipy y fórmulas explícitas en el script. Redondear solo al presentar.

### Referencias a verificar

Usar `temario_curso.md` solo como mapa inicial: Statistical Concepts cap. 5 §5.2 (estimación); cap. 6 §§6.1, 6.4; cap. 7 §§7.1–7.2; cap. 8 §§8.2–8.3; cap. 9 §§9.1–9.3; Mark y Workman cap. 15; ASQ Metrology Handbook cap. 27; Brereton apéndice A.3. Verificar numeral y páginas en los PDFs de `docs/` mediante `pdftotext`; para cualquier numeral no confirmable, citar solo la obra sin numeral y anotarlo pendiente. Referencia de grados de libertad/intervalo t: Statistical Concepts, cap. 6. Familias de contraste: Statistical Concepts caps. 6–9. No citar ISO 13528, z, ζ, Mandel ni otros contenidos expresamente excluidos por prop_e §6. Referir deducciones a AX.1 y AX.7 cuando correspondan.

### Anexos previstos

- AX.1: divisor `n − 1` y grados de libertad de `s` (mención solo si se necesita para precisar el estimador de varianza).
- AX.7: fórmula de Welch–Satterthwaite y condiciones; remitir cuando se interprete ν efectivo/combinado, sin desarrollar la deducción.
- No se necesita remitir a otros anexos de deducciones en M04.

## Ejecución

### Libreto y alcance

Se completó `M04_libreto.md` en formato narrado, con ficha, escenas B1–B3, señales de escalamiento, escenas I1–I5, escenas A1–A3, cierre y referencias. Las tres prácticas de prop_e §5 M4 quedaron exclusivamente como marcadores; no se añadieron enunciados, soluciones, rúbricas ni evidencias evaluables. Se desarrollaron los ejemplos ilustrativos con vectores **simulados** fijados explícitamente en el script; no se extrajeron ni se atribuyeron datos a CALAIRE. El certificado F-PSMT-01 se menciona solo como contexto y fuente propia del caso según guía §6.

### Scripts y resultados reproducidos

- `calc/M04_ejemplos.py`, ejecutado con `curso/.venv/bin/python curso/S1_fundamentos/calc/M04_ejemplos.py`.
- **B, media y t:** vector simulado de ocho errores; media `0,0375`, `s=0,5263`, error estándar `0,1861`, `7` gl, IC95% `[-0,4025; 0,4775]`, `t=0,2015`, `p=0,8460`.
- **I, pareada:** ocho diferencias; media `0,1625`, `s=0,1188`, error estándar `0,0420`, IC95% `[0,0632; 0,2618]`, `t=3,8697`, `p=0,006134`.
- **I, Welch:** muestras de `6` y `7`; medias `10,0167` y `10,9571`, diferencia `-0,9405`, error estándar `0,1531`, `10,9272` gl, IC95% `[-1,2778; -0,6032]`, `t=-6,1418`, `p=0,0000750`.
- **I, varianza (chi-cuadrado):** varianza muestral `0,2770`, IC95% `[0,1211; 1,1473]`, contraste contra `0,25`: `χ²=7,755`, `p=0,7094`.
- **I, cociente de varianzas (F):** razón `0,8408`, IC95% `[0,1404; 5,8669]`, `F=0,8408`, `p=0,8678`.
- **I, potencia/tamaño muestral:** media y pareadas con `d=0,5`, `n=16`: potencia `0,4649`, `n` calculado `33,3672`, tamaño entero `34`; dos grupos con `d=0,8`, `12` por grupo: potencia `0,4658`, `25,5246` por grupo, tamaño entero `26` por grupo.
- **I, incertidumbre de s:** aproximación `u(s)=0,1407` para `s=0,5263` y `7` gl.
- **I, atípicos:** para el vector fijo simulado de `8` valores, Grubbs `G=2,4374 > 2,22` y Dixon `Q=0,8214 > 0,59` según las tablas verificadas de Otto al nivel `0,99`; el texto advierte expresamente que no se elimina un valor sin causa documentada.
- **A, multiplicidad:** tres valores p simulados `[0,012; 0,031; 0,20]`; Bonferroni `α` por prueba `0,0167`; ajustados `[0,036; 0,093; 0,600]`, rechazo solo del primer contraste.
- **A, equivalencia:** media `0,08`, `s=0,40`, `n=20`, márgenes `[-0,50; 0,50]`; IC90% `[-0,0747; 0,2347]`, ambos contrastes unilaterales con `p<0,0001`; conclusión de equivalencia condicionada a los supuestos y al margen predefinido.
- **A, consistencia chi-cuadrado:** residuos `[0,12; -0,05; 0,08]` y `u=0,10`; `χ²=2,33`, `3` gl, crítico al 95% `7,8147`, `p=0,5068`; no se detecta inconsistencia bajo el modelo simulado independiente.

Los resultados impresos corresponden al código ejecutado. Se redondearon en el libreto solo al reportar; los cálculos usan precisión completa.

### Referencias verificadas mediante `pdftotext`

| Clave y numeral citado | Archivo comprobado | Página PDF comprobada |
|---|---|---:|
| Statistical Concepts §5.2 | `docs/statistical_concepts_c05.pdf` | 3 |
| Statistical Concepts §6.1, §6.4 (incluye 6.1.2–6.1.5; sección de revisión de datos 6.4) | `docs/statistical_concepts_c06.pdf` | 2 y 5 |
| Statistical Concepts §§7.1–7.2 (incluye 7.1.4–7.1.7 y 7.2.2–7.2.3) | `docs/statistical_concepts_c07.pdf` | 2–4 |
| Statistical Concepts §8.3.1 | `docs/statistical_concepts_c08.pdf` | 5 |
| Statistical Concepts §§9.1–9.3 | `docs/statistical_concepts_c09.pdf` | 2–4 |
| Otto §2.2; ecuaciones/tablas de Dixon y Grubbs, con valores críticos usados | `docs/Chemometrics Statistics and Computer Application.pdf` | 51–52 (paginación impresa 42–43) |
| Milton et al. 2006 (sin numeral citado); χ² para validar calibración con incertidumbre general | `docs/milton2006.pdf` | 4 |
| Datos de origen propio y caso de contexto (sin usar cifras de ejemplo) | `curso/guia_libreto.md` §6 | §6 |

También se comprobó con `pdftotext` la información bibliográfica de Otto y Statistical Concepts en sus PDFs completos, y la cita/título/paginación de Milton en `docs/milton2006.pdf`. En el libreto no se atribuyen numerales a fuentes externas ausentes de `docs/`.

### Decisiones y pendientes

- Se dio prioridad al alcance del M4 final de prop_e frente al temario previo. La práctica no se desarrolló; los ejemplos son explicación docente, como permite guía §1.
- Se usaron datos simulados con vectores deterministas para que todos los resultados se reproduzcan; no se usaron las 8 lecturas × 6 días del certificado como si fueran independientes.
- La consistencia A se ilustró primero con residuos independientes y luego se narró la extensión matricial cuando existe covarianza; el ejemplo no representa una comparación real.
- La equivalencia se explicó mediante TOST/IC90 y márgenes previos; multiplicidad con Bonferroni. Son concreciones de los temas asignados a A, no datos ni criterios oficiales de CALAIRE.
- Pendiente bibliográfico: Lakens (equivalencia) y NIST/SEMATECH (multiplicidad) no están en `docs/`; se citan sin numeral verificable y quedan anotados para incorporación/verificación. Las referencias de capítulos de conceptos estadísticos no se ampliaron a asuntos que exceden el M4 de prop_e.

## Correcciones (revisión Haiku)

| id del hallazgo | decisión | cambio hecho | ubicación | justificación |
|---|---|---|---|---|
| R01 | aplicado | Se eliminó la mención a `prop_e` y se expresó la pregunta como parte de la explicación para operadores. | Libreto, B3, ejemplo Level 2 | `prop_e` justifica alcance, no es referencia técnica ni material para narración; guía §5. |
| R02 | aplicado con cambios | Las citas de Welch se ajustaron a §§7.3.1 y 7.5.3; se conservó §7.1 solo para la comparación de grupos independientes. | Libreto, I1; ficha y cierre | La revisión comprobó que Welch se aborda en §§7.3.1 y 7.5.3, no en §7.1. |
| R03 | aplicado | Se retiró §8.3.1 y se citó Milton et al. 2006 en la explicación y ejemplo de consistencia; también se corrigieron la ficha, el cierre y la bibliografía. | Libreto, ficha, A3, cierre y referencias | §8.3.1 trata bondad de ajuste de conteos. Milton et al. sustenta la prueba chi-cuadrado con incertidumbres generales y grados de libertad del ajuste. |
| R04 | aplicado con cambios | Se quitó la cita numérica §§9.1–9.2 y se dejó la cita amplia «Statistical Concepts, cap. 9»; se registra como pendiente localizar una fuente específica para la aproximación de `u(s)`. | Libreto, I4; esta bitácora, pendientes | El capítulo 9 trata inferencia sobre varianzas, pero la búsqueda reportada no localizó allí la fórmula de incertidumbre aproximada de `s`; no se atribuye un numeral no comprobado. |
| R05 | aplicado | Se eliminó la marca errónea «no disponible en docs/» de la cita de Milton. | Libreto, A3 | `docs/milton2006.pdf` existe y la referencia completa está en el capítulo. |
| R06 | aplicado | La acotación de diapositiva se pasó a bloque de cita con etiqueta permitida. | Libreto, B1 | Cumple el formato obligatorio de guía §1. |
| R07 | aplicado | «Predeclarado en el cálculo docente» se cambió por «que fijamos de antemano». | Libreto, B3 | Elimina jerga de preparación y conserva el sentido temporal del nivel de significación. |
| R08 | aplicado con cambios | Se quitaron las menciones al script de la narración y se añadieron notas al instructor en B, I y A que identifican `calc/M04_ejemplos.py`. | Libreto, inicio de B, I y A; ejemplos B1, B2, I1, I5 y A2 | Se separa la trazabilidad del discurso oral sin perder la reproducibilidad exigida por guía §6. |
| R09 | aplicado con cambios | Se conservó la explicación de error tipo II y se trasladó la definición explícita de potencia al nivel I. | Libreto, B3 | Potencia y planificación corresponden al alcance I de prop_e §5 M4. |
| R10 | aplicado | Se actualizaron los encabezados de I y A para indicar que presentan contenido añadido. | Libreto, encabezados I y A | Sigue la plantilla de guía §2 y hace explícita la acumulación de niveles. |
| R11 | aplicado | La expresión del intervalo al 95 % usa `t_{0,975;ν}` y se lee en voz alta con el cuantil correspondiente. | Libreto, B2, pizarra | Se alinea con la convención de guía §4. |
| R12 | aplicado | Se reescribió la definición del pivote t para identificar claramente la diferencia dividida por el error estándar. | Libreto, B2 | Evita ambigüedad sintáctica al leerla en voz alta. |
| R13 | aplicado | Se nombró explícitamente el estadístico chi-cuadrado y se precisó su cociente. | Libreto, I2 | Distingue el estadístico de la distribución y evita la construcción ambigua «se basa en». |
| R14 | aplicado | Se separaron en frases breves la suma de residuos, los grados de libertad y el caso con covarianzas. | Libreto, A3 | Facilita la narración y mantiene las condiciones del modelo y del ajuste. |
| R15 | aplicado | La lectura oral de la forma cuadrática ahora nombra el vector y la matriz de covarianza. | Libreto, A3, pizarra | Corresponde a la notación matricial escrita y evita referirse vagamente a «el residuo». |
| R16 | aplicado con cambios | Se precisó «nivel de concentración» donde podía confundirse con B/I/A y se normalizó la denominación narrativa a «ejemplo ilustrativo», manteniendo «simulado» para indicar el origen de los datos. | Libreto, B1–B3, I2–I5 y A1–A3 | Distingue el nivel de concentración del nivel curricular y respeta el rótulo de origen de guía §§1 y 4. |
| R17 | aplicado | Las citas sobre t, hipótesis, nivel de significación y valor p se colocaron junto a los conceptos que respaldan. | Libreto, B2–B3 | Cumple guía §5, que pide la referencia inmediatamente después del concepto. |
| R18 | aplicado | Se quitó el año 2020 de la cita bibliográfica de Statistical Concepts. | Libreto, referencias | El año no pudo verificarse en el material consultado; se conservan los datos confirmados de edición y editorial. |

**Correcciones adicionales por iniciativa propia**

- Retiré también §8.3.1 de la referencia bibliográfica final y del cierre, donde quedaba citado pese a corregir A3; añadí Milton et al. 2006 a la síntesis del cierre.
- Actualicé la ficha y las secciones utilizadas de Statistical Concepts para reflejar las referencias verificadas de Welch (§§7.3.1 y 7.5.3), y revisé los textos restantes para uniformar «ejemplo ilustrativo» y aclarar los niveles de concentración.
- No hubo cambios en cifras, fórmulas numéricas ni diseño de los ejemplos; por tanto, no se modificó `calc/M04_ejemplos.py`. Verificación final ejecutada con `curso/.venv/bin/python -I curso/S1_fundamentos/calc/M04_ejemplos.py`: las cifras del libreto se reprodujeron sin discrepancias.
