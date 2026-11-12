# S3. Índice de la sección entregada

Fecha: 26 de octubre de 2026. Supervisor: claude-sol (gpt-6.1-sol). Paso 6: correcciones tras la revisión Opus incorporadas; decisiones sobre O-01–O-17 y los 24 bloques del intento interrumpido en `S3_revision_sol.md`. La entrega sigue limitada a la fase de contenido.

## Alcance y orden

M09 prepara diferencias y dependencia para M10; M11 usa M3 y M7–M8 para tiempo, regresión y propagación, sin exigir M09 para calcular covarianza temporal. M12 distingue indicadores agregados de decisiones individuales y límites de control. Niveles acumulativos: I incluye B; A incluye B e I. Fase exclusivamente de contenido.

## [M09. Comparación de resultados: diferencias, covarianza y consistencia](M09_libreto.md)

### Nivel B — comparar cuando la independencia está justificada

- Escena B1. La diferencia tiene signo y una pregunta definida
- Escena B2. La cuadratura necesita independencia justificada

> **[PRÁCTICA — fase de ejercicios]** Diferencia y $E_n$ en dos puntos independientes y reconocimiento de la dependencia Level 2–SRP 55

### Nivel I — modelar la dependencia antes de comparar

- Escena I1. La covarianza puede reducir o aumentar la incertidumbre de la diferencia
- Escena I2. Interpolar con una recta y propagar la covarianza de sus parámetros

> **[PRÁCTICA — fase de ejercicios]** Diferencia con covarianza del SRP 55 compartido

### Nivel A — modelar la comparación con matrices y referencia común

- Escena A1. De incertidumbres por punto a matrices de covarianza
- Escena A2. Grado de equivalencia y diferencia interpolada respecto a un patrón de trabajo

> **[PRÁCTICA — fase de ejercicios]** Comparación con referencia común y grado de equivalencia

### Datos, anexos y evidencia

Datos de los ejemplos: B e I y grado de equivalencia de A: datos **simulados**, fijados explícitamente en `calc/M09_ejemplos.py`; no son resultados de CALAIRE. GGMR de A: pares **publicados** en US EPA SRP QAPP, Element 14.2, Figura 14.2; incertidumbres y covarianzas **adaptadas** del modelo BIPM-SRP27, con $V_{xy}=0$ por hipótesis didáctica. No son datos de CALAIRE ni resultado oficial.

Anexos: AX.2: varianza de combinaciones lineales y covarianza. AX.8: GGMR con $V_{xy}=0$ y chi-cuadrado de consistencia. AX.9: diferencia con patrón compartido y grado de equivalencia frente a referencia común.

Bitácora: [M09_bitacora_luna.md](M09_bitacora_luna.md). Revisión de redacción: [M09_revision_haiku.md](M09_revision_haiku.md). Cálculo: `calc/`.

## [M10. Reglas de decisión y riesgo](M10_libreto.md)

### Nivel B — Aplicar una regla suministrada

- Escena B1. El resultado no es todavía una decisión
- Escena B2. Aplicar la regla y detenerse cerca del límite

> **[PRÁCTICA — fase de ejercicios]** Completar un certificado docente y resolver resultados dentro, cerca y fuera del límite

### Nivel I — Elegir y justificar una regla

- Escena I1. Seleccionar la banda de guarda según el riesgo
- Escena I2. Presupuesto, declaración y criterios con ámbito definido

> **[PRÁCTICA — fase de ejercicios]** Resolver un resultado próximo al límite con dos reglas y explicar el riesgo que asume cada una

### Nivel A — Modelar y contrastar el riesgo

- Escena A1. Riesgo específico y global bajo modelos explícitos
- Escena A2. Requisitos bilaterales y decisiones con dependencia

> **[PRÁCTICA — fase de ejercicios]** Cuantificar el riesgo de una decisión para una distribución y una especificación definidas

### Datos, anexos y evidencia

Datos de ejemplos: Todos los números de los ejemplos didácticos son **simulados** por `calc/M10_ejemplos.py`; no son resultados ni criterios de CALAIRE. Criterios de EPA/BIPM, cuando se nombran, son **publicados** y solo valen en el documento, equipo y etapa expresamente descritos.

Anexos: AX.2 y AX.9 para varianzas y dependencia; AX.10 para deducción de probabilidades de falsa aceptación y falso rechazo. A2 incluye un ejemplo bilateral con dos colas relevantes: $u=6$, $y=0$, riesgo específico total $0,05246774$.

Bitácora: [M10_bitacora_luna.md](M10_bitacora_luna.md). Revisión de redacción: [M10_revision_haiku.md](M10_revision_haiku.md). Cálculo: `calc/`.

## [M11. Control estadístico y series temporales](M11_libreto.md)

### Nivel B — Leer una carta ya definida y responder con criterio

- Escena B1. Variación común y señal especial
- Escena B2. Carta de individuales y rango móvil
- Escena B3. Control estadístico no es tolerancia

> **[PRÁCTICA — fase de ejercicios]** Carta del historial preparado del Level 2 y decisión de acción

### Nivel I — Construir una base y modelar la deriva

- Escena I1. Una línea base homogénea
- Escena I2. Dependencia y regresión de deriva
- Escena I3. De la deriva a la incertidumbre de uso

> **[PRÁCTICA — fase de ejercicios]** Línea base homogénea, deriva y predicción de uso

### Nivel A — Detectar cambios pequeños y justificar la revisión

- Escena A1. EWMA: memoria gradual de la serie
- Escena A2. CUSUM, falsas alarmas e intervalo de revisión

> **[PRÁCTICA — fase de ejercicios]** EWMA, CUSUM y revisión del intervalo bajo riesgo declarado

### Datos, anexos y evidencia

Datos de ejemplo: Serie I-MR, regresión de deriva y series para EWMA/CUSUM: simulados, deterministas y pedagógicos; no describen CALAIRE. NISTIR 6963 Tabla 4: serie publicada de SRP-0/SRP-2, usada solo en su propio contexto, nunca como línea base del Level 2. F-PSMT-01: datos propios de seis días; no constituyen historial de largo plazo ni base de límites operativos.

Anexos: AX.2: propagación con covarianza; AX.12: varianza de EWMA y longitud media de corrida de EWMA/CUSUM. En M11-A se enseña el conteo de trayectorias y su error estándar para estimar falsa alarma en un horizonte; no se confunde con ARL. El fundamento general de simulación se remite a M13/AX.13, sin exigirlo como prerrequisito. Los parámetros del ejemplo ARL de AX.12 son distintos; la coordinación de su redacción con S4 queda documentada, sin editar archivos fuera de S3.

Bitácora: [M11_bitacora_luna.md](M11_bitacora_luna.md). Revisión de redacción: [M11_revision_haiku.md](M11_revision_haiku.md). Cálculo: `calc/`.

## [M12. Indicadores de precisión y sesgo a partir de diferencias relativas](M12_libreto.md)

### Nivel B — definir la diferencia antes de resumirla

- Escena B1. La diferencia relativa necesita una referencia explícita
- Escena B2. La magnitud media y el sesgo firmado no responden lo mismo

> **[PRÁCTICA — fase de ejercicios]** Indicadores con diferencias de ambos signos

### Nivel I — cuantificar límites y hacer explícita la escala

- Escena I1. Un límite superior de precisión con chi-cuadrado
- Escena I2. El límite de sesgo absoluto no conserva el signo por sí solo
- Escena I3. Un cambio de escala cambia el error relativo si cambia la respuesta
- Escena I4. Dispersión del cero y umbral bajo hipótesis declaradas

> **[PRÁCTICA — fase de ejercicios]** Indicadores, límites y cambio de escala

### Nivel A — conservar la dependencia y separar los periodos

- Escena A1. Las verificaciones dependientes no equivalen a nuevas réplicas independientes
- Escena A2. La trazabilidad común permanece en el indicador agregado
- Escena A3. Mezclar periodos puede ocultar el desempeño que se quiere describir

> **[PRÁCTICA — fase de ejercicios]** Discrepancia entre conformidad individual y desempeño agregado

### Datos, anexos y evidencia

Datos de los ejemplos: Todos los datos numéricos didácticos son **simulados**, generados de forma determinista en `calc/M12_indicadores.py`. No son datos ni resultados de CALAIRE. Las fórmulas y criterios regulatorios citados son **publicados**; se distingue su aplicación original de los ejemplos simulados.

Anexos: AX.1: divisor y grados de libertad de la desviación muestral. AX.2: varianza de combinaciones lineales para el término de covarianza en un promedio dependiente. AX.11: límites de confianza de indicadores de precisión y sesgo (chi-cuadrado y t). Las deducciones se remiten a los anexos; aquí se interpretan y aplican las expresiones.

Bitácora: [M12_bitacora_luna.md](M12_bitacora_luna.md). Revisión de redacción: [M12_revision_haiku.md](M12_revision_haiku.md). Cálculo: `calc/`.

## Recursos transversales

- [Ficha común de criterios](S3_01_ficha_criterios.md): tolerancias, límites de control e indicadores, con diseño, divisor, unidades y fuente.
- [Revisión del supervisor](S3_revision_sol.md): hallazgos, decisiones sobre ediciones interrumpidas, tabla de correcciones O-01–O-17, cálculos, referencias y estado.
- [Revisión Opus](S3_revision_opus.md): informe del paso 5, preservado como antecedente; su veredicto corresponde al texto anterior a estas correcciones.
- [Anexos AX](../S4_numericos_integracion/AX_libreto.md): AX.1, AX.2, AX.8, AX.9, AX.10, AX.11 y AX.12. Deducciones fuera de la narración evaluable.
- `calc/S3_verificar_entrega.py`: estructura, etiquetas y un marcador por nivel y capítulo.

## Estado y pendientes

Correcciones de la revisión Opus (O-01–O-17) aplicadas el 2026-10-26; respaldos interrumpidos P01–P24 y Q01–Q07 decididos en la revisión del supervisor.

Doce prácticas pendientes: tres por capítulo, una por nivel; solo marcadores, sin enunciados, soluciones ni rúbricas. Los ejemplos numéricos resueltos son explicación docente, no paquetes de prácticas.

Estado técnico definitivo y limitaciones: consultar «Estado de entrega» de la revisión del supervisor. La entrega de contenido no autoriza impartir el curso ni emitir declaraciones reales. Pendientes de fase posterior: paquetes B/C/D, datos y diccionarios, plantillas, soluciones revisadas, evidencia y rúbricas; adoptar criterios y acciones mediante procedimientos autorizados; confirmar interpretación tipográfica del QAPP y validar modelos y coberturas del caso real. Ningún resultado simulado o adaptado describe desempeño de CALAIRE.
