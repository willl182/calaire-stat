# M01 — Bitácora de desarrollo

## Plan

### Alcance por nivel (tomado literalmente de `prop_e.md`, §5, M1)

- **B:** «mensurando, error, sesgo, corrección; modelo de medición como función `Y = f(X₁, …, X_N)`; sensibilidad numérica en plantilla. Caso: ecuación del SRP con entradas suministradas y conversión explícita a nmol/mol.»
  - **Práctica de prop_e:** «recalcular tres concentraciones con dos valores de sección eficaz declarados e indicar el signo y la magnitud relativa del cambio» (solo marcador en esta fase).
- **I añade:** «cambio de escala como cambio de un parámetro del modelo: efecto sobre `e` y sobre un error relativo con denominador definido; diferencia entre cambiar la escala y corregir un instrumento.»
  - **Práctica de prop_e:** «comparar dos mediciones en escalas distintas usando el cociente de los valores realmente implementados (los pares 1,147/1,1329 y 308,32/304,39 dan incrementos distintos; el ejercicio declara cuál usa)» (solo marcador en esta fase).
- **A añade:** «entradas comunes a dos resultados y su efecto en una diferencia frente a un resultado absoluto (prepara la covarianza de M8 y M9).»
  - **Práctica de prop_e:** «identificar qué contribuciones se cancelan en una diferencia entre dos fotómetros y cuáles permanecen en el resultado declarado» (solo marcador en esta fase).

### Escenas previstas

- Apertura/ficha: competencia estadística, acumulación de niveles, convención `x`, `y`, `e`, resultado estadístico antes de entrar en cada cálculo.
- B1: mensurando y distinción entre valor de referencia, indicación, error con signo, sesgo y corrección; ejemplo numérico ilustrativo.
- B2: modelo funcional `Y=f(X₁,…,X_N)` y lectura de entradas/salida; ecuación SRP con entradas suministradas, unidades y conversión explícita a nmol/mol.
- B3: sensibilidad numérica en plantilla, manteniendo las demás entradas; ejemplo resuelto para la sección eficaz, con cambio absoluto y relativo.
- Marcador de práctica B y señales de escalamiento.
- I1: cambio de escala como cambio de parámetro; cambios de `e` y del error relativo con denominador declarado; comparar los pares de escala dados por prop_e y distinguir cambio de escala de corrección instrumental.
- Marcador de práctica I.
- A1: separar resultado absoluto y diferencia entre dos fotómetros; entradas comunes, cancelación condicionada y contribuciones no canceladas; puente conceptual a covarianza de M8/M9.
- Marcador de práctica A; cierre y referencias.

### Datos y rótulo de origen

- Ejemplos B e I de calibración/escala: **simulados para enseñanza**, números definidos en scripts de `calc/`; no son mediciones ni resultados de CALAIRE. Se explicitarán los valores y unidades de entradas hipotéticas.
- Números derivados de los pares de sección eficaz indicados literalmente en `prop_e.md` M1/I: se rotulan como **publicados** cuando la fuente documental se verifica (308,32 en NISTIR 6963 y 304,39 en 40 CFR 50, Appendix D); el par 1,147/1,1329 se presenta como valores declarados por prop_e y queda pendiente verificar en `docs/` el origen documental de 1,1329. Los cocientes conservan las cifras realmente implementadas; ningún resultado simulado se atribuye a CALAIRE.
- Ejemplo A de entradas comunes: **simulado para enseñanza**, contribución aditiva común y términos particulares para mostrar algebraicamente qué permanece en el resultado absoluto y qué se cancela en la diferencia.

### Cálculos previstos

- Diferencia y corrección con signo en el ejemplo de B1 (`e=y−x`; corrección aditiva de aplicación `x̂−y`).
- Aplicación numérica de una ecuación SRP con entradas declaradas, logaritmo natural y conversión de la unidad de salida a nmol/mol.
- Sensibilidad por variación de una entrada manteniendo fijas las otras; efecto relativo de cambiar sección eficaz y dos cocientes de escala del contenido I.
- Efecto algebraico de una entrada aditiva común en cada resultado absoluto y en su diferencia, bajo la hipótesis explícita de igual efecto; no se calcula un presupuesto de incertidumbre.
- **Regla de reproducibilidad:** ningún número calculado aparecerá en el libreto sin estar generado o verificado por un script `curso/.venv/bin/python` bajo `curso/S1_fundamentos/calc/M01_*.py`.

### Referencias a verificar en `docs/`

- `VIM`: definiciones de mensurando, error, sesgo y corrección. No está disponible en `docs/`; citar sin numeral.
- `JCGM GUM-6:2020`, `JCGM_GUM_6_2020.pdf`: modelo de medición, entradas y salida; verificar numerales con `pdftotext` antes de citarlos.
- `JCGM GUM-1:2023`, `JCGM_GUM-1.pdf`: expresiones generales de modelo e incertidumbre; verificar numerales si se usan.
- `NISTIR 6963`, `nistir6963.pdf`: ecuación del SRP y unidades/conversiones pertinentes; verificar numerales y página impresa con `pdftotext`.
- `40 CFR 50, Appendix D`, `Appendix D to Part 50_ Title 40 (up to date as of 10-16-2026).pdf`: coeficiente de absorción/sección eficaz y unidades, si hace falta para el ejemplo; verificar texto y numeral.
- `prop_e.md` §3 para convenciones (`x`, `y`, `e`, recta y escala), sin atribuirle respaldo bibliográfico externo.

### Anexos

- AX.2: remisión breve para la derivación de varianzas de combinaciones lineales y ley de propagación con covarianza; no desarrollar la deducción en M01.

## Ejecución

### Contenido escrito

- Se redactó `M01_libreto.md` con ficha, apertura y escenas B1–B3, marcador de práctica B, señales de escalamiento, escena I1 y marcador I, escena A1 y marcador A, cierre y referencias.
- En B se narran mensurando, referencia/indicación, error con signo, sesgo, corrección, modelo como función, ecuación simplificada del SRP con unidades y conversión explícita a nmol/mol, y sensibilidad numérica por variación de entradas.
- En I se narran el modelo de escala multiplicativa, efecto sobre error absoluto y relativo con denominador `x`, los pares de cocientes prescritos por prop_e y la diferencia entre cambiar escala y corregir el instrumento.
- En A se muestra algebraicamente la cancelación condicionada de una entrada común en una diferencia y su presencia en los resultados absolutos; se remite la deducción de varianza a AX.2 y no se desarrolla el presupuesto de covarianza.
- Los tres lugares de práctica tienen únicamente los marcadores exigidos. No se escribieron prácticas, ejercicios, soluciones, evidencias evaluables ni rúbricas.
- Se respetó la exclusión de desarrollar temas de módulos posteriores y no se añadieron tópicos ajenos al alcance M1.

### Scripts y resultados

- Script: `curso/S1_fundamentos/calc/M01_modelo_variables.py`.
- Ejecución: `curso/.venv/bin/python curso/S1_fundamentos/calc/M01_modelo_variables.py` (exitosa).
- Resultados reproducidos: error `+1,300000 nmol/mol`, corrección aditiva `−1,300000 nmol/mol`; modelo SRP ilustrativo con coeficiente `308,32` da `493,474569423 nmol/mol` y con `304,39` da `499,845853164 nmol/mol`, incremento absoluto `6,371283741 nmol/mol` y relativo `1,291106804 %`; cocientes `1,147/1,1329 = 1,012445935` (incremento `1,244593521 %`) y `308,32/304,39 = 1,012911068` (incremento `1,291106804 %`).
- Sensibilidad aproximada por diferencias finitas, con pasos explícitos en el script: transmitancia `−37004,286363431 nmol/mol` por unidad de `T`, y coeficiente `−1,642069163 nmol/mol` por `(atm⁻¹ cm⁻¹)`.
- Ejemplo de escala `s=1,0129`: para `x=100` y `500 nmol/mol`, errores `+1,29` y `+6,45 nmol/mol`; en ambos casos `e/x=+1,29 %`.
- Ejemplo de término común: `Y₁=2,3`, `Y₂=1,9`, `Δ=0,4 nmol/mol`. Los datos de escala y término común son simulados para enseñanza; no describen resultados de CALAIRE. Todos los cálculos indicados se ejecutaron con el entorno pedido.

### Referencias verificadas

Los numerales usados se cotejaron con el texto extraído mediante `pdftotext` y se contrastaron con las páginas del PDF:

| Clave y numeral citado | Archivo en `docs/` | Página PDF comprobada | Comprobación |
|---|---|---:|---|
| GUM-6 §§5.1–5.2 | `JCGM_GUM_6_2020.pdf` | 3 | §5.1: mensurando/salida y entradas; §5.2: forma `Y=f(X₁,…,X_N)`. |
| GUM-6 §5.4 | `JCGM_GUM_6_2020.pdf` | 4 | Uso del modelo y evaluación de incertidumbre/covarianza. |
| GUM-6 §§5.6, 5.8–5.9 | `JCGM_GUM_6_2020.pdf` | 4–5 | Adecuación, efectos relevantes y dominio de validez. |
| GUM-6 §6.1 | `JCGM_GUM_6_2020.pdf` | 5 | Selección del mensurando. |
| NISTIR 6963 §8 | `nistir6963.pdf` | 9–11 | pdftotext confirma §8 y la sección describe la relación de concentración, transmitancia, coeficiente y longitud, así como el ajuste de temperatura/presión; se cotejaron las ecuaciones en las páginas del PDF. |
| 40 CFR 50, Appendix D §4.1 | `Appendix D to Part 50_ Title 40 (up to date as of 10-16-2026).pdf` | 2–3 | pdftotext confirma §4.1 y coeficiente 304,39 atm⁻¹ cm⁻¹; las fórmulas de concentración en atm y ppm se cotejaron en las páginas del PDF. |

### Decisiones tomadas y pendientes

- La ecuación del SRP se usa en forma fotométrica simplificada y con la muestra declarada a condiciones estándar; la salida intermedia en atm se convierte a nmol/mol bajo la condición de 1 atm. La presentación limita el ejemplo al modelo y a la sensibilidad, no representa un cálculo operativo ni un certificado.
- La transmitancia, longitud óptica de 90,0 cm y cambios de escala de los ejemplos se rotulan simulados; los valores de sección eficaz se reportan como pares declarados en prop_e, con las fuentes documentales verificadas indicadas arriba y la procedencia de 1,1329 pendiente. No se atribuye a CALAIRE ningún resultado calculado.
- Se citó VIM sin numeral porque el documento no está disponible en `docs/`; queda pendiente su verificación documental. No se usaron numerales de GUM-1, ISO 13964 ni otras fuentes del mapa inicial.
- Pendiente de fase posterior: desarrollar los ejercicios y materiales de prácticas; no corresponde a la fase actual.

## Correcciones (revisión Haiku)

| Id del hallazgo | Decisión | Cambio hecho | Ubicación | Justificación |
|---|---|---|---|---|
| R01 | aplicado | Se reemplazó GUM-6 §5.4 por GUM §5.1.3 y se añadió GUM-6, Anexo A, símbolo $c$. | Libreto, B3; referencias | GUM §5.1.3 define los coeficientes de sensibilidad y GUM-6, Anexo A, identifica $c_i$; §5.4 no respalda esa definición. |
| R02 | aplicado | Se sustituyeron las citas sobre entradas correlacionadas por GUM §5.2.2 y se mantuvo AX.2 para la deducción. | Libreto, A1 | GUM §5.2.2 trata la varianza combinada cuando las entradas están correlacionadas; §5.4 no es la cita específica adecuada. |
| R03 | aplicado | Se separaron el coeficiente de §4.1 y la fórmula de ppm de §4.5.3.10, ecuación 4, con mención del factor de pérdidas de §4.5.2.5; se aclaró que el modelo docente lo omite. | Libreto, ficha y B2 | La fórmula operativa indicada incorpora temperatura, presión y pérdidas; no es una mera conversión desde atm. |
| R04 | aplicado con cambios | Se aclaró que NISTIR 6963 relaciona $1,147\times10^{-17}\ \mathrm{cm^2/molécula}$ con $308,32\ \mathrm{atm^{-1}cm^{-1}}$. El valor 1,1329 se mantiene solo como número prescrito por prop_e, sin asignarle unidad no comprobada. | Libreto, ficha e I1 | Sección eficaz y coeficiente de absorción son magnitudes distintas aunque estén relacionadas; la unidad de 1,1329 no se verificó. |
| R05 | aplicado con cambios | Se reemplazó la atribución documental de 1,1329 por «fuente y unidad pendientes de verificación en `docs/`»; se conservó la fuente comprobada de 1,147/308,32 y de 304,39 ± 0,94. | Libreto, ficha e I1 | La revisión no encontró 1,1329 en NISTIR, Appendix D ni en Daumont/Malicet. No se inventa una procedencia ni se busca sostenerla con el documento curricular. |
| R06 | aplicado | Se pasó la notación matemática que estaba en código a LaTeX y se unificaron variables, fórmulas, cocientes y unidades en la narración y las acotaciones. | Libreto, capítulo completo | La guía §4 requiere fórmulas en LaTeX; la notación matemática uniforme se lee mejor y evita alternar código con fórmulas. |
| R07 | aplicado | Se añadió la lectura en voz alta de la ecuación del SRP, la diferencia finita y el modelo de escala multiplicativa. | Libreto, B2, B3 e I1 | La guía §1 pide narrar también las fórmulas, no solo escribirlas. |
| R08 | aplicado | Se reescribió la frase para explicar que la salida es inversamente proporcional al coeficiente y que el orden del cociente determina el factor de escala. | Libreto, I1 | La nueva redacción elimina la construcción incompleta y hace explícita la dirección de la relación. |
| R09 | aplicado | «Pregunta de centro» se sustituyó por «pregunta sobre la posición de los errores». | Libreto, B1 | La frase nombra la idea estadística sin una metáfora indefinida para el oyente. |
| R10 | aplicado | Se sustituyó la entrada «presión» aislada por sección eficaz/coeficiente, longitud, transmitancia o factor de temperatura y presión. | Libreto, B3 | El modelo didáctico mantiene fijo el factor de temperatura y presión; la lista ahora coincide con sus entradas declaradas. |
| R11 | aplicado | Se dividió la frase extensa de escalamiento en instrucciones y condiciones breves. | Libreto, «Señales de escalamiento» B | Se conserva el contenido y se mejora la lectura oral, como recomienda la revisión. |
| R12 | aplicado con cambios | Se definió la clave local CFR50-D en el capítulo y se usó en las citas y la bibliografía; no se modificó la tabla de claves de `guia_libreto.md`. | Libreto, ficha, B2, I1 y referencias | La tabla de claves pertenece a la guía, fuera del alcance autorizado. La clave local permite referencias internas consistentes sin editar archivos ajenos a `S1_fundamentos/`; GUM se incorporó a la bibliografía por R01. |

### Correcciones adicionales por iniciativa propia

- Hice explícita la normalización dimensional del resultado: para pasar de $c$ en atm a fracción molar, se divide por la presión estándar $p_0=1\ \mathrm{atm}$ antes de multiplicar por $10^9$. Actualicé `calc/M01_modelo_variables.py` para aplicar esa división; al recalcular con `curso/.venv/bin/python`, los resultados se mantuvieron iguales porque el ejemplo usa $p_0=1\ \mathrm{atm}$ (por ejemplo, $499,845853164$ nmol/mol y sensibilidad de $-37\ 004,286363431$ nmol/mol por unidad de transmitancia).
- Corregí la cita de sensibilidad en el cierre para no volver a atribuirla a GUM-6 §5.4; se remite a GUM §5.1.3 y GUM-6 §5.8 cuando corresponde.
- Mantuve la convención del capítulo: la concentración calculada del ejemplo SRP se identifica como salida $Y$, no como $x$, que ya representa el valor de referencia.

