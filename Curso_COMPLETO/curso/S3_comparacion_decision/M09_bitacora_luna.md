# Bitácora de desarrollo — M09

## Plan

### Alcance por nivel (tomado literalmente de `prop_e.md`, §5, M9)

- **Competencia estadística:** «estimar la incertidumbre de una diferencia entre resultados, con la covarianza que corresponda, y decidir qué hipótesis contrasta el indicador de compatibilidad.»
- **B:** «diferencia, incertidumbre de la diferencia bajo independencia justificada y `E_n` en un escenario que cumpla las condiciones de su fórmula. Para el ejercicio se define `E_n = Δ/√(U₁² + U₂²)`, con incertidumbres expandidas `U₁` y `U₂` calculadas con el mismo factor de cobertura `k`, y criterio `|E_n| ≤ 1`. Reconoce que compartir un patrón **no invalida `E_n` en general**, pero impide suponer independencia: no debe usarse sin justificación la fórmula que la asume, y se identifica cuándo hay que tratar la covarianza.»
- **I añade:** «varianza de una diferencia con covarianza, `u²(Δ) = u²₁ + u²₂ − 2·cov(1,2)`; covarianza introducida por un patrón compartido; interpolación con una recta y la covarianza de sus parámetros; compatibilidad frente a conformidad. Para normalizar la diferencia se calcula `U(Δ) = k_Δ·u(Δ)` y se declara la cobertura; si se usa `Δ/U(Δ)` como extensión de `E_n`, se identifica expresamente y no se confunde con la definición de B. Con un mismo `k`, `U²(Δ) = k²[u₁² + u₂² − 2·cov(1,2)]`; el término de covarianza expandido es `−2·k²·cov(1,2)`.»
- **A añade:** «Matrices de covarianza y GGMR aplicado a una comparación, dentro del alcance `V_xy = 0` (ver M7-A); consistencia por chi-cuadrado. Grado de equivalencia frente a una referencia común: diferencia `D` respecto al valor de referencia clave (KCRV) y su incertidumbre. Caso docente: BIPM.QM-K1, donde el BIPM-SRP27 es la referencia común. El caso SRP 36/SRP 7 es una adaptación didáctica para interpolación. No se estudian el protocolo, la organización de la comparación ni la base de datos de comparaciones clave (KCDB).»
- En A se mantiene explícita la cautela curricular: «El caso SRP 36/SRP 7 es una adaptación didáctica; no se presenta como resultado oficial de CALAIRE. Un resultado de comparación es evidencia para evaluar una CMC, no su aprobación.»

### Escenas previstas

1. Ficha: competencia, prerrequisitos M3, M4, M7 y M8; alcance aditivo de B, I y A; orígenes de datos; anexos AX.2, AX.8 y AX.9; referencias técnicas verificables.
2. B1: pregunta estadística de comparación, diferencia con signo y ejemplo independiente simulado con `Δ`, `u(Δ)`, `U₁`, `U₂`, `k` común y `E_n` conforme a la definición de B; explicar exactamente qué evalúa `|E_n|≤1`.
3. B2: condiciones de independencia, cuándo una cuadratura está justificada, patrón común como fuente posible de dependencia y límite de inferencia; rótulo de escalamiento Level 2/SRP 55 sin calcular covarianza en B; marcador práctica B y señales de escalamiento.
4. I1: varianza de la diferencia con covarianza; ejemplo numérico simulado de una contribución de patrón compartido, efecto de signo/magnitud y `u(Δ)`/`U(Δ)` con cobertura declarada; marcador de práctica I.
5. I2: interpolar con recta `y=a+b·x`; diferencia interpolada y propagación de `cov(a,b)` para parámetros; ejemplo numérico simulado; aclarar diferencia entre compatibilidad y conformidad.
6. A1: matrices de covarianza y GGMR en `V_xy=0`; lectura del ajuste como estimación conjunta de línea y puntos latentes, consistencia mediante χ² y grados de libertad del ejemplo; advertir dominio de la validación numérica y excluir `V_xy≠0`.
7. A2: grado de equivalencia frente a referencia común; adaptación didáctica SRP 36/SRP 7 basada en doce pares publicados del QAPP y modelo de incertidumbre adaptado del BIPM-SRP27; cálculo ilustrativo de `D` y `u(D)` en niveles interpolados, chi-cuadrado diagnóstico y limitaciones; marcador práctica A y transición a M10.
8. Cierre narrado: resumir qué conclusión permite cada nivel, separar indicador normalizado de diferencia e incertidumbre, y tender puente hacia reglas de decisión/riesgo de M10.

### Datos y rótulo de origen

- Ejemplo independiente de B y mini-ejemplo I de patrón compartido: datos **simulados**, establecidos expresamente por el script `calc/M09_ejemplos.py`; no son resultados de CALAIRE.
- Ejemplo I de interpolación con recta: datos **simulados**, parámetros y matriz de covarianza declarados por el script; no representa una calibración real.
- Ejemplo A: pares de SRP 36/SRP 7 **publicados** en US EPA SRP QAPP, Element 14.2, Figura 14.2; para el GGMR son **adaptados** los modelos de incertidumbre/covarianza inspirados en BIPM.QM-K1 Apéndice 1, con hipótesis declaradas `V_xy=0`; no es resultado de CALAIRE ni reproducción oficial. Datos accesibles en `casos_taller/datos_caso_B.csv`, fuente descrita en `caso_B_comparacion_clave.md`.
- La referencia común BIPM-SRP27 y su significado se describirán solo en el alcance necesario; no se reconstruirá el protocolo ni se usarán resultados propios de CALAIRE. La asociación de factores comunes con magnitudes compartidas solo se afirma si el numeral correspondiente se verifica en el PDF.

### Cálculos previstos

- `calc/M09_ejemplos.py` reproducirá todos los valores numéricos del capítulo: diferencia independiente, incertidumbres estándar/expandidas, `E_n`; diferencia con covarianza común, incertidumbre y sensibilidad a covarianza; diferencia interpolada y su incertidumbre incluyendo `cov(a,b)`; matrices de covarianza del ejemplo A; ajuste GGMR no lineal con `V_xy=0`; covarianzas de parámetros, χ² y grados de libertad; `D` y `u(D)` en los puntos elegidos. Sin redondeo prematuro y con comprobaciones de consistencia.
- Ejecutar con `curso/.venv/bin/python`; transcribir al libreto solo cifras emitidas por el script o fórmulas no numéricas.

### Referencias a verificar en `docs/` con `pdftotext`

- GUM JCGM 100: apartados de covarianza y propagación (confirmar texto y numerales antes de citar).
- ISO/TS 28037:2010: cláusula 10 y ejemplo/tablas GGMR para la formulación dentro de alcance `V_xy=0` y validación del cálculo.
- BIPM.QM-K1: §7–§8 y Apéndice 1 únicamente para referencia común, grado de equivalencia y componente común, si los pasajes se verifican.
- US EPA SRP QAPP: Element 14.2/Figura 14.2 para procedencia de los pares publicados; validar en `pdftotext` página PDF.
- Milton et al. 2006: descripción de mínimos cuadrados generalizados solo si se verifica en `docs/milton2006.pdf`.
- ISO 6143 §6.1 puede respaldar el caso particular de criterio de compatibilidad con `k=2`; verificar el pasaje antes de citarlo. No se compararán métodos más allá del alcance M9 de prop_e.
- Numeral no verificable: citar fuente sin numeral y registrarla como pendiente. `prop_e` y `temario_curso.md` orientan el alcance, no sirven de respaldo técnico.

### Anexos previstos

- **AX.2:** remisión a la ley de varianza de una diferencia como combinación lineal y su covarianza; no desarrollar deducción.
- **AX.8:** remisión a formulación matricial de GGMR con `V_xy=0` y chi-cuadrado de consistencia; no desarrollar deducción.
- **AX.9:** remisión a varianza de diferencia con patrón compartido y grado de equivalencia frente a referencia común; no desarrollar deducción.

## Ejecución

### Contenido escrito

- `M09_libreto.md`: ficha del capítulo; nivel B con escenas B1–B2 y señales de escalamiento; nivel I con escenas I1–I2; nivel A con escenas A1–A2; cierre y referencias del capítulo. Todo el contenido está narrado en voz del instructor, con acotaciones de escena, ejemplos numéricos y advertencias de errores críticos.
- Se dejaron únicamente los tres marcadores requeridos para las prácticas de B, I y A. No se escribieron enunciados, actividades, soluciones, evidencias, rúbricas ni taller.
- Los ejemplos B e I se rotulan **simulados**. El ejemplo A separa los datos **publicados** del QAPP del modelo y resultados **adaptados**; el texto advierte que no son resultados de CALAIRE ni oficiales.

### Scripts y resultados

- Script: `curso/S3_comparacion_decision/calc/M09_ejemplos.py`; ejecutado con `curso/.venv/bin/python curso/S3_comparacion_decision/calc/M09_ejemplos.py`.
- B, independencia simulada: `Δ=0,35 nmol/mol`, `u(Δ)=0,25 nmol/mol`, `U₁=0,40`, `U₂=0,30 nmol/mol`, denominador `0,50` y `E_n=0,70`; pasa el criterio didáctico `|E_n|≤1` bajo los supuestos declarados.
- I, patrón compartido simulado: con `cov(1,2)=0,018 (nmol/mol)²`, `u²(Δ)=0,0265 (nmol/mol)²`, `u(Δ)=0,162788206 nmol/mol`, `U(Δ)=0,325576412 nmol/mol` para `k_Δ=2`; término expandido `−0,144 (nmol/mol)²`.
- I, interpolación simulada: `D(200)=0,32 nmol/mol`; componentes de varianza `0,0100`, `0,0100` y `−0,0140 (nmol/mol)²`; `u(D)=0,077459667 nmol/mol`.
- A, GGMR adaptado, orientación `x=SRP 7`, `y=SRP 36`: `a=−0,184237121 nmol/mol`, `b=0,998350748`, `u(a)=0,031189175 nmol/mol`, `u(b)=0,004125035`, `cov(a,b)=−3,83046347099×10⁻⁶ nmol/mol`; `χ²_obs=6,318259554`, `ν=10`, cuantil 95 % `18,307038053`. Interpolación: `D(80)=−0,316177317`, `u(D)=0,330547626 nmol/mol`; `D(420)=−0,876923148`, `u(D)=1,731866683 nmol/mol`.
- Validación del método GGMR en el script con el ejemplo de ISO/TS 28037 cl. 10, Tablas 25–26: reproduce `a=0,3424`, `b=1,0012`, `u(a)=2,0569`, `u(b)=0,0090`, `cov(a,b)=−0,0129` y `χ²=1,772` dentro de tolerancia absoluta `0,0002`. Corrida completada sin error.

### Referencias verificadas con `pdftotext`

| Clave y numeral citado | Archivo en `docs/` | Página PDF comprobada | Pasaje comprobado |
|---|---|---:|---|
| GUM 5.2.2; 6.2.1 | `ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf` | 29; 31 | Varianza combinada para entradas correlacionadas; definición de incertidumbre expandida y factor de cobertura. |
| ISO 28037 cl. 10.1–10.3 | `ISO 28037.pdf` | 39–44 | Matriz de covarianza, GGMR, ajuste iterativo, covarianza de parámetros y validación chi-cuadrado. |
| ISO 28037, Tablas 25–26 | `ISO 28037.pdf` | 43–44 | Ejemplo de siete puntos y salida del ajuste; validación numérica incluida en el script. |
| BIPM-K1 §§7–8 | `BIPM.QM-K1_2.protocol.pdf` | 8–9 | Ajuste de regresión y definición de grado de equivalencia respecto a SRP27. |
| BIPM-K1, Apéndice 1 §§2–3 | `BIPM.QM-K1_2.protocol.pdf` | 22–25 | Modelo de incertidumbre SRP27; `u_b=2,92×10⁻³`; covarianzas por variables comunes (temperatura, presión y longitud óptica). |
| ISO 6143 §6.1 | `ISO 6143 2001.pdf` | 20 | Criterio de compatibilidad para contenido determinado y preasignado, expresado con incertidumbres y factor de cobertura `k=2`. |
| SRP-QAPP, Element 14.2, Figura 14.2 | `srp_qapp.pdf` | 37 | Informe ilustrativo, identificación SRP 36/SRP 7, doce puntos y desviaciones estándar publicadas. |

No se citan numerales técnicos sin verificación. **Pendientes de referencia: ninguno.** No se usaron Milton ni fuentes externas no disponibles.

### Decisiones y límites

- `E_n` y `|E_n|≤1` se presentan como definición operativa y criterio explícito del ejercicio básico; no se anuncian como regla universal, ni como decisión de conformidad. La conclusión del indicador se limita a compatibilidad bajo el modelo declarado.
- En el caso A, se conserva la orientación didáctica SRP 7 (`x`, referencia) → SRP 36 (`y`, comparado), distinta de la orientación del informe de QAPP. Las desviaciones estándar publicadas se convierten en incertidumbres estándar de medias con `/√12` solo bajo el supuesto didáctico declarado; la fuente no confirma que esa interpretación sea el origen de esas cifras.
- El modelo de incertidumbre A adapta la componente relativa común del SRP27 de BIPM, aplica matrices de covarianza intraje y fija `V_xy=0`. No se atribuye esa hipótesis a los datos fuente. Se excluyen GGMR con `V_xy≠0`, protocolo y organización de BIPM.QM-K1, KCDB y KCRV combinado con participación del laboratorio evaluado, de acuerdo con prop_e §6.
- La referencia común BIPM-SRP27 se explica como contexto curricular; SRP 7 del caso no se identifica con BIPM-SRP27. El caso publicado SRP 36/SRP 7 y los cálculos adaptados no son resultados de CALAIRE ni acreditan una CMC.
- No se añadieron temas, prácticas o ejercicios fuera del contenido asignado. Las deducciones se remiten a AX.2, AX.8 y AX.9.

## Correcciones (revisión Haiku)

| Id del hallazgo | Decisión | Cambio hecho | Ubicación | Justificación |
|---|---|---|---|---|
| R01 | aplicado con cambios | Se declara la hipótesis nula de diferencia verdadera cero en B, para la extensión normalizada de I y para el grado de equivalencia frente al KCRV; se aclara que el criterio práctico no prueba equivalencia ni asigna significación exacta. | `M09_libreto.md`, escenas B1, I1 y A2 | El criterio de ISO 6143 §6.1 se describe como opción práctica («may be used»), no como prueba con nivel de significación especificado. |
| R02 | aplicado | Se añadió advertencia crítica que distingue $u(\Delta)$ del denominador formado por $U_1$ y $U_2$ en $E_n$. | `M09_libreto.md`, B1, tras la pizarra de $E_n$ | La fórmula de B utiliza incertidumbres expandidas; sustituirlas por estándar cambia el indicador y contradice prop_e §8. |
| R03 | aplicado con cambios | Se define KCRV operacionalmente como el valor que el protocolo designa para comparar diferencias; en BIPM.QM-K1 se identifica BIPM-SRP27 como referencia. Se amplía KCDB al primer uso. | `M09_libreto.md`, introducción de A y A2 | Evité afirmar una definición universal del KCRV no verificada en `docs/`; la descripción se limita al uso comprobado en BIPM-K1, Protocolo A §8, ecs. 2–3. |
| R04 | aplicado con cambios | Se renombró A2 y el resultado numérico como diferencia interpolada SRP 36 menos patrón de trabajo SRP 7; se reserva «grado de equivalencia» para la diferencia contra BIPM-SRP27 y se explica que no hay cálculo numérico de ese caso. | `M09_libreto.md`, título y escena A2 | SRP 7 es solo el eje de referencia del caso didáctico de dos patrones; no es BIPM-SRP27 ni el KCRV del protocolo. |
| R05 | aplicado | Se desambiguaron las citas a Protocolo A §7, ec. 1 y §8, ecs. 2–3; se advirtió que la cuadratura de la ecuación 3 exige justificar independencia y se mencionó el término de covarianza común. | `M09_libreto.md`, A2 | La ecuación de incertidumbre del protocolo no autoriza omitir covarianza cuando hay dependencia; se conserva la coherencia con B2 e I1. |
| R06 | aplicado con cambios | Se explicó la cadena Level 2–SRP 55, la posible causa común y la información de presupuesto que falta, sin asignar covarianza numérica. En A se añadió el caso conceptual SRP 55 frente a BIPM-SRP27, sin inventar datos. | `M09_libreto.md`, B2, I1 y A2 | Cumple los casos de prop_e §6; al faltar presupuesto completo no puede determinarse numéricamente la covarianza ni el grado de equivalencia. |
| R07 | aplicado con cambios | Se pasaron los símbolos y expresiones matemáticas a LaTeX en línea y se uniformaron subíndices; se conservaron backticks solo para rutas. | `M09_libreto.md`, todo el capítulo | Cumple la convención de guia_libreto §4 sin alterar los valores ni la aritmética. |
| R08 | aplicado | Se añadieron instrucciones de lectura oral a las pizarras de incertidumbre expandida, ajuste GGMR e informe de $D$ y su incertidumbre. | `M09_libreto.md`, I1, A1 y A2 | La guía §1 exige narrar las fórmulas que se escriben. |
| R09 | aplicado | La identidad expandida ahora condiciona explícitamente en $k_\Delta=k$, tanto en narración como en pizarra. | `M09_libreto.md`, I1 | La covarianza se multiplica por el mismo factor al cuadrado solo bajo ese supuesto. |
| R10 | aplicado | Se sustituyó «demostración» por «ilustración», se cambió a «repasemos», se denomina especificación técnica a ISO/TS 28037, se corrigió «el chi-cuadrado» y «residuos transformados con la factorización de Cholesky», y se simplificó la pregunta oral. | `M09_libreto.md`, B2, I1 y A1 | Ajusta el registro oral y la terminología al documento ISO/TS 28037 §10.2.1. |
| R11 | aplicado con cambios | Se dividieron y simplificaron los pasajes sobre el criterio B, el modelo adaptado A y la referencia común en frases más cortas; se mantuvieron las limitaciones técnicas necesarias. | `M09_libreto.md`, B1, A1 y A2 | Se mejora la narrabilidad sin perder supuestos, alcance ni cautelas. |
| R12 | aplicado | Se unificó la notación de cláusulas como §, Figura 14.2 y la referencia al Apéndice 1 §3, ec. 21; la cita del protocolo quedó fechada 9 de octubre de 2025. | `M09_libreto.md`, ficha, A1, A2 y referencias | Se sigue la forma de cita de la guía y la fecha que aparece en el pie del PDF. |
| R13 | aplicado | Se indicó la discrepancia entre $2,89\times10^{-3}$ en Apéndice 1 §1 y $2,92\times10^{-3}$ en §3, ec. 21, y se identificó cuál se usa en la adaptación. | `M09_libreto.md`, A1 | La fuente presenta ambos valores; la nota evita ocultar esa diferencia y especifica el valor usado. |
| R14 | aplicado | Se añadió la señal de detenerse cuando hay pocas réplicas o una fuente domina $U_1$ o $U_2$, con revisión de grados de libertad y cobertura. | `M09_libreto.md`, señales de escalamiento B | Atiende la señal de pocos grados de libertad de prop_e §2 sin ampliar el tema. |
| R15 | aplicado | Se definió la suma en cuadratura al introducirla y se unificó la notación de matrices como $U_x$, $U_y$ y $V_{xy}$. | `M09_libreto.md`, B1, B2 y A1 | La definición evita jerga sin explicación y la notación distingue correctamente los bloques de covarianza. |
| R16 | aplicado | Se explicó que la covarianza $0,018$ produce una mejora parcial y se añadió el límite admisible $0,030$ con $u(\Delta)=0,05$ nmol/mol; el script calcula y emite ese caso. | `M09_libreto.md`, I1; `calc/M09_ejemplos.py` | Con covarianza positiva máxima $u_1u_2$, la matriz $2\times2$ es semidefinida positiva y la varianza de la diferencia es $(u_1-u_2)^2=0,0025$; el nuevo número es reproducible. |

### Correcciones adicionales por iniciativa propia

- Corregí la hipótesis de independencia y señalé que compartir patrón no invalida por definición $E_n$; el problema es usar su denominador independiente sin justificarlo.
- Aclaré que los pares SRP 36/SRP 7 publicados no constituyen el cálculo del grado de equivalencia contra el KCRV, y que sus resultados y modelo son adaptados.
- Afiné la interpretación del chi-cuadrado: quedar bajo el cuantil no prueba equivalencia, conformidad ni veracidad del modelo.
- Recalculé `calc/M09_ejemplos.py` con `curso/.venv/bin/python`; la validación ISO/TS 28037 y los resultados B, I y A se reproducen, incluido el nuevo límite de covarianza $0,030$ y $u(\Delta)=0,050000$ nmol/mol.
