# M03 — Bitácora de desarrollo

## Plan

### Alcance por nivel (transcripción literal de prop_e §5, M3)

**B:** variable aleatoria; normal, rectangular y triangular; semiamplitud `h` frente a resolución total `δ` (`h/√3`, `δ/√12`); `u = U/k`; desviación de lecturas frente a desviación de un promedio; distribución t, cuantiles y grados de libertad (prerrequisito de M4-B). La reducción con `1/√n` tiene límite cuando hay un componente común o deriva.

**I añade:** covarianza y correlación; varianza de combinaciones lineales; distribuciones chi-cuadrado y F (prerrequisito de M4-I y M6-I); gráficos de probabilidad; dependencia temporal; separación entre variación de corto plazo y entre días.

**A añade:** covarianzas comunes entre canales y puntos; autocorrelación; manejo operativo de matrices y bloques de covarianza (unidades, simetría y admisibilidad), como prerrequisito para M7-A y M9-A.

### Escenas previstas

- Ficha del capítulo con competencia estadística, prerrequisitos M1–M2, alcance B/I/A, datos y rótulos, anexos y referencias.
- B1: probabilidad como modelo de repetición de una medida; probabilidad y reglas básicas.
- B2: variable aleatoria discreta/continua, densidad y acumulada; esperanza y varianza; normal y normal estándar, rectangular y triangular; conversión de especificaciones a incertidumbre estándar, `u = U/k`; resolución instrumental.
- B3: variación de una lectura y promedio; independencia, reducción `1/√n`, componente común/deriva; lectura de t, cuantiles y grados de libertad.
- I1: covarianza y correlación; varianza de combinaciones lineales con ejemplo de cancelación y ejemplo de patrón compartido.
- I2: chi-cuadrado y F, usos como distribución (sin adelantar las pruebas inferenciales de M4); gráficos de probabilidad normal y evaluación visual del ajuste.
- I3: dependencia temporal y distinción entre variación de corto plazo y entre días; marcadores de práctica en el punto correspondiente.
- A1: covarianzas comunes entre canales y puntos, caso de razón entre canales.
- A2: autocorrelación y matrices/bloques de covarianza: unidades, simetría y admisibilidad; remisión a AX.2 y exclusiones curriculares respetadas.
- Cierre por niveles, señales de escalamiento B y transición a M4.

### Datos y rótulo de origen

- Ejemplos probabilísticos sintéticos de lecturas, cuantización y componente común: **simulado** (se indicará expresamente; no son resultados de CALAIRE).
- Ejemplo de resolución 0,1 nmol/mol: especificación del analizador citada en prop_e M3, tratada como información de caso; cálculo didáctico propio, no resultado de desempeño: **adaptado**.
- Posible ejemplo ilustrativo de la razón entre canales con `s = 0,000012` frente a `0,000089` suponiendo independencia: **publicado** solo si se confirma la ubicación exacta en NISTIR 6963; si no, se omite o se registra pendiente sin adjudicarlo a CALAIRE.
- No se usarán datos propios del certificado ni del estudio R&R: no son necesarios para el alcance de M3.

### Cálculos previstos

- Incertidumbre estándar de distribución rectangular con semiamplitud `h` y con resolución total `δ`; triangular con semiamplitud `h`.
- Conversión ilustrativa `u = U/k` con factor declarado.
- Desviación estándar de lecturas frente a error estándar de promedio bajo independencia, y promedio con componente común/deriva.
- Varianza de suma/diferencia con y sin covarianza; relación entre `cov(X,Y)` y correlación.
- Razón entre canales y comparación entre cálculo correlacionado e hipótesis de independencia, únicamente si la fuente/valores quedan verificados.
- Autocorrelación ilustrativa y comprobaciones numéricas de una matriz de covarianza pequeña.

Todos los valores numéricos del libreto se reproducirán con scripts `curso/.venv/bin/python` guardados como `curso/S1_fundamentos/calc/M03_*.py`.

### Referencias a verificar en `docs/`

- Statistical Concepts: §§5.1, 4.1, 8.2 y 9.1.1.
- Metrology and Measurement Uncertainty: §§3.2.1–3.2.5, incluidas las distribuciones rectangular, triangular, normal y t.
- Introduction to Statistics in Metrology: §§4.4, 7.2 y 7.4.1.
- NISTIR 6963: §§8–11 y Tablas 2, 3 y 5, solo si se usa el ejemplo instrumental.
- BIPM.QM-K1, Apéndice 1, ecuación 11, solo si se usa dependencia común entre canales/puntos.
- Brereton, apéndice A, solo para cuantiles/tablas si se cita.

Se comprobarán numerales y páginas con `pdftotext`; cualquier ubicación no confirmable se citará sin numeral y quedará pendiente. Las citas de textos sin ubicación corroborada se marcarán como pendientes.

### Anexos previstos

- AX.2 para varianza de combinaciones lineales y propagación con covarianza.
- AX.3 para varianzas de las distribuciones rectangular y triangular.
- AX.7 únicamente como remisión contextual si aparece el tema de grados de libertad; no desarrollar su fórmula, que corresponde a M8.

## Ejecución

### Contenido escrito

Se creó `M03_libreto.md` (aprox. 6 800 palabras) con ficha; B1–B3; I1–I3; A1–A2; señales de escalamiento B, I y A; cierre y referencias. Los tres marcadores de práctica se dejaron sin desarrollo en sus niveles: B «Convertir especificaciones del certificado en incertidumbres estándar y comparar el promedio de datos independientes con el de una serie con deriva»; I «Calcular la incertidumbre de una diferencia con y sin covarianza»; A «Construir y comprobar una matriz pequeña de covarianza, verificar unidades, simetría y admisibilidad, y comparar estrategias de promediado en una serie con ruido y deriva».

### Scripts y resultados reproducidos

- `calc/M03_ejemplos.py`, ejecutado con `curso/.venv/bin/python curso/S1_fundamentos/calc/M03_ejemplos.py`.
- Resultados: rectangular con `h=0,3`: `u=0,1732050808`; resolución total `δ=0,1`: `u=0,02886751346`; triangular con `h=0,3`: `u=0,1224744871`; `U=0,60`, `k=2`: `u=0,3`.
- Lectura con `s=0,8`; promedio de `n=16` independientes: `0,2`; con ruido independiente `0,8` y componente común `0,3`: `u=0,3605551275`.
- Para `u1=0,8`, `u2=0,6`, `ρ=0,75`: covarianza `0,36`; incertidumbre estándar de la suma con independencia `1`; de la suma correlacionada `1,311487705`; de la diferencia correlacionada `0,5291502622`.
- Ejemplo sintético de razón de canales: `A=1,0000`, `B=0,8000`, `u(A)=0,00005`, `u(B)=0,00004`, `ρ=0,90`; `u(A/B)` correlacionada `2,795084972×10⁻⁵`, sin covarianza `8,838834765×10⁻⁵`.
- Probabilidad de unión del ejemplo: `0,35`; puntaje normalizado ilustrativo `z=2`; muestra de cinco observaciones: `ν=4`; cuantiles al 0,975: `t(4)=2,776445105` y normal `1,959963985`; ejemplo chi-cuadrado `2`; ejemplo F `1`.
- Matriz de correlaciones del ejemplo: simétrica y admisible; autovalores aproximados `0,40692967`, `0,75`, `1,84307033`. Correlación simulada de retardo uno: `0,5`.

Todos los ejemplos de datos son simulados salvo la resolución de 0,1 nmol/mol, marcada como adaptada al dato citado en la propuesta B (M3-B); la especificación técnica queda pendiente de confirmar con el manual del 49C o el certificado. No se usaron datos propios del certificado ni valores del ejemplo NIST de razón de canales. Se omitieron los valores `0,000012` y `0,000089` citados en el mapa curricular porque no se verificó su localización exacta en NISTIR 6963; no se presentan como datos CALAIRE.

### Referencias verificadas con `pdftotext`

| Clave y numeral usado | Archivo comprobado | Página PDF comprobada |
|---|---|---:|
| Statistical Concepts §4.1 | `docs/statistical_concepts_c04.pdf` | 1–2 |
| Statistical Concepts §5.1 | `docs/statistical_concepts_c05.pdf` | 1–2 |
| Statistical Concepts §8.2 | `docs/statistical_concepts_c08.pdf` | 1, 3 |
| Statistical Concepts §9.1.1 | `docs/statistical_concepts_c09.pdf` | 1–2 |
| Metrology and Measurement Uncertainty §3.2.1 | `docs/metrology_measure_uncer_c03.pdf` | 6 |
| Metrology and Measurement Uncertainty §3.2.3 | `docs/metrology_measure_uncer_c03.pdf` | 10 |
| Metrology and Measurement Uncertainty §3.2.4 | `docs/metrology_measure_uncer_c03.pdf` | 12–13 |
| Metrology and Measurement Uncertainty §3.2.5.1 (rectangular) | `docs/metrology_measure_uncer_c03.pdf` | 14 |
| Metrology and Measurement Uncertainty §3.2.5.2 (triangular simétrica) | `docs/metrology_measure_uncer_c03.pdf` | 15 |
| Metrology and Measurement Uncertainty §3.2.5.5 (t de Student) | `docs/metrology_measure_uncer_c03.pdf` | 18–19 |
| Introduction to Statistics in Metrology §4.4.3 (gráficos de probabilidad) | `docs/intro_stats_metro_c04.pdf` | 11 |
| Introduction to Statistics in Metrology §7.2 (esperanza y varianza de combinaciones) | `docs/intro_stats_metro_c07.pdf` | 2–3 |
| Introduction to Statistics in Metrology §7.4.1 (covarianza y correlación) | `docs/intro_stats_metro_c07.pdf` | 6–7 |

Se comprobaron los numerales y el contenido con extracciones `pdftotext -f … -l … -layout`; la columna indica la página física PDF consultada, no necesariamente la paginación impresa del libro. Las referencias GUM-1, GUM-6 y NIST/SEMATECH se citan sin numeral. Sus ubicaciones específicas quedan pendientes; NIST/SEMATECH no está en `docs/`.

### Decisiones y pendientes

- Las deducciones de propagación y de desviaciones estándar se remiten a AX.2 y AX.3; no se desarrollan en el capítulo. No se remite a AX.7 porque Welch–Satterthwaite pertenece a M8 y no se desarrolla en M3.
- No se incluyó la razón de canales publicada del NISTIR ni el ejemplo de BIPM.QM-K1: no era necesario para cubrir el nivel A y no se verificaron numerales y páginas que justificaran su uso. Se utilizó en su lugar una razón sintética rotulada.
- Quedan pendientes de ubicación exacta en GUM-1/GUM-6 la conversión general `u=U/k` y la admisibilidad matricial; queda pendiente una referencia documental específica para el error estándar del promedio. Se citan sin numeral, según la guía.
- No se desarrollaron prácticas, ejercicios, soluciones, evidencias ni rúbricas, de acuerdo con la fase actual.

## Correcciones (revisión Haiku)

| ID | Decisión | Cambio hecho | Ubicación | Justificación |
|---|---|---|---|---|
| R01 | aplicado | Se retiraron la regla de unión, su pizarra y el ejemplo de marcas; se añadió un ejemplo discreto de cinco ciclos con probabilidades para X=0 y X=1. | Libreto, B1; `calc/M03_ejemplos.py` | La regla de unión excedía prop_e §5 y §5.1 citado no la respaldaba. El nuevo ejemplo ilustra variable aleatoria discreta, que sí está en alcance. |
| R02 | aplicado con cambios | Se atribuyó 0,1 nmol/mol a la propuesta B (M3-B), se mantuvo como ejemplo adaptado y se añadió advertencia de verificación con manual/certificado. | Ficha; libreto, B2 | prop_e no contiene el dato y el certificado consultado tampoco; no afirmamos que la fuente curricular confirme la especificación técnica. Pendiente de verificación antes de impartir. |
| R03 | aplicado | Se eliminó la mención de 0,000012 y 0,000089 y se dejó el ejemplo sintético de razón. | Libreto, A1 | La propuesta B no constituye fuente técnica, y los valores no tenían fuente técnica corroborada. |
| R04 | aplicado | Se cambió la desviación del proceso de `s` a `σ`; `s` queda para la estimación muestral. | Libreto, B3 | Respeta la convención de símbolos de la guía §4 y evita contradecir la pizarra. |
| R05 | aplicado | Se sustituyó «varianza común» por «varianza desconocida». | Libreto, B3 | Es el supuesto de una muestra normal cuya varianza se estima; «varianza común» no corresponde aquí. |
| R06 | aplicado | La lectura oral define F con `ν₁` y `ν₂` grados de libertad y divide cada chi-cuadrado por su propio grado de libertad. | Libreto, I2 | F depende de dos grados de libertad, no de uno solo. |
| R07 | aplicado | Se agregó un ejemplo numérico de cinco observaciones ordenadas y sus cuantiles normales teóricos. | Libreto, I2; script | Cumple la exigencia de ejemplo cuantitativo. Cuantiles reproducidos: −1,2816; −0,5244; 0; 0,5244; 1,2816. |
| R08 | aplicado | Se incorporó ejemplo simulado de dos puntos, factor común relativo de 1 %, incertidumbres, covarianza, correlación, matriz y comparación de diferencia. | Libreto, A1; script | Hace operativa la covarianza entre puntos exigida por prop_e. El cálculo correlacionado da 3,0 nmol/mol y el de independencia 4,1231 nmol/mol. |
| R09 | aplicado | Se quitó la etiqueta AR(1); se describe únicamente una asociación ilustrativa de retardo uno entre observaciones consecutivas. | Libreto, A2; script | AR(1) no forma parte del alcance y no se definía; la autocorrelación sí está en prop_e. |
| R10 | aplicado con cambios | Las citas numéricas usan las claves Hahs-Vaughn, MMU y Crowder 2020; se identificaron esas claves en la bibliografía final. | Libreto, citas y referencias | Alinea las citas con las claves bibliográficas de la guía §5 sin alterar títulos ni numerales comprobados. |
| R11 | aplicado | Se quitó NISTIR 6963 de las referencias clave de la ficha. | Ficha | No se cita ni se usa en el capítulo. |
| R12 | aplicado | Se añadió advertencia `[ERROR CRÍTICO]` sobre no confundir U expandida con u estándar ni cambiar entre ellas sin k. | Libreto, B2 | Atiende el error crítico explícito de prop_e §8. |
| R13 | aplicado | El modelo de dos escalas ahora declara `sd(D_d)=τ` y `sd(ε_dj)=σ`; la narración nombra `s_entre` y `s_r`. | Libreto, I3 | Mantiene la notación fijada por la guía §4 y prop_e §3 para efectos entre días y variación de lectura. |
| R14 | aplicado | En las señales de nivel I se habla de dependencia temporal aparente, con rachas, tendencia o ciclos, sin nombrar autocorrelación como contenido de I. | Libreto, I3, señales | La autocorrelación se desarrolla en A2; I conserva el objetivo más general de dependencia temporal. |
| R15 | aplicado | Se especificaron nmol/mol y (nmol/mol)² en el ejemplo de entradas correlacionadas. | Libreto, I1 | Evita unidades genéricas y muestra que la covarianza tiene unidades producto. |
| R16 | aplicado | Se reescribió la exclusión como «covarianza cero entre ejes, `V_xy=0`» y se repitió de forma oral en el escalamiento A. | Libreto, A | Reduce ambigüedad oral y conserva el límite curricular de GGMR. |
| R17 | aplicado con cambios | Se eliminó la pizarra de probabilidad retirada con R01; se añadió lectura en voz alta de las expresiones de error estándar. | Libreto, B1 y B3 | Las fórmulas conservadas quedan leídas en la narración, según guía §1 y §4. |
| R18 | aplicado | La lectura de la fórmula de razón se dividió en frases más cortas, separando los términos. | Libreto, A1 | Facilita seguir oralmente la expresión sin cambiar el contenido matemático. |
| R19 | aplicado | Se cambió «razón real» por «razón entre dos canales» y se corrigió la enumeración de autovalores. | Libreto, A1 y A2 | Elimina ambigüedad expresiva y puntuación innecesaria. |

### Correcciones adicionales por iniciativa propia

- Se actualizó `calc/M03_ejemplos.py` para reproducir las probabilidades del nuevo ejemplo discreto, los cuantiles normales del gráfico y los cálculos de covarianza entre puntos; se ejecutó con `curso/.venv/bin/python -I` y los resultados coincidieron con el libreto.
- Se corrigió el nombre de salida del script para que no etiquete la correlación ilustrativa como AR(1).
- Se homogeneizaron referencias sin numeral a la clave bibliográfica `MMU`; se mantiene en bitácora la advertencia de que confirmar el dato de resolución del Level 2 es pendiente documental.
