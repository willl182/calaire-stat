# M07 — revisión de cierre de las prácticas B, I y A (revisor: haiku)

Alcance: sección de prácticas de `curso/S2_modelos_calibracion/M07_libreto.md` (escenas de práctica, solución docente, escalamiento y criterio de logro), `curso/S2_modelos_calibracion/calc/M07_practicas_luna.py`, `curso/logs/M07_practicas_luna.md` y la salida `curso/logs/M07_B_residuos.html`. No se editó ningún libreto ni script, no se tocaron referencias ni citas y no se hizo ningún commit.

## Verificación por ejecución

- `curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M07_practicas_luna.py` → rc=0; la comprobación ISO imprime `PASS`. Este run regenera `curso/logs/M07_B_residuos.html` (salida determinista; ya era untracked).
- `curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M07_ejemplos.py` → rc=0. Se cruzaron con el libreto las cifras narradas fuera de las prácticas: `u(a)=0,2856`, `u(b)=0,0009433`, `cov(a,b)=−0,0002224`, pendiente forzada `1,00209`, `χ²=1,2796` (ν=10, cuantil 18,31), máximo residuo ponderado `0,6160`, `χ²=83,36`, cola inferior `0,01826`, cola superior `3,38·10⁻¹⁷`. Todas coinciden.

Cifras de los bloques de práctica comprobadas contra la salida:

- **B:** `a=0,242857`, `b=1,0014286`, `s_res=0,394606`, `R²=0,99999645`; residuos `−0,042857; 0,314286; −0,428571; 0,328571; −0,414286; 0,242857` (suma ≈ 0, error de redondeo `1,5·10⁻¹³`); ŷ(200)=200,528571 y r=−0,428571; `x̂=249,900143`, corrección `−0,599857`. Correctas.
- **I:** OLS `(0,447619; 1,000743)`, WLS `(0,416852; 1,000921)`; pesos `16; 11,111111; 6,25; 2,777778; 1,234568; 0,694444`; `u(x̂)=0,256446`, `ν_eff=25,8325`, `k=2,05618`, `U=0,527298` (`k·u` = 0,527300 con el redondeo de `k`, consistente); bandas en x=250: `±0,44728` (media) y `±1,18339` (predicción). Réplicas: `a=0,01`, `b=1,0026`, `SS_LOF=0,966`, `SS_PE=0,080`, `F(2,8)=48,3`, `p=3,42·10⁻⁵`. Correctas.
- **A:** OLS = WLS `(0,3047619; 1,00131429)`; GGMR `(0,3047254; 1,00131443)`; abscisas ajustadas, `Q=0,408901`, 4 gl, cola superior `0,98174`; `z_x`, `z_y` con suma de cuadrados igual a Q; `u(a)` sin/con componente común `0,341517 / 0,362038`; `u(b)=0,001128` en ambos casos (verificado: la componente común no cambia la pendiente, así que la frase «no cambia apreciablemente la pendiente ni su incertidumbre» es correcta). Contraste ISO: `a=0,3424009`, `b=1,0012308`, `Q=1,771847`, `u(a)=2,0569`, `u(b)=0,0090`, `cov=−0,0129`. Correctas.
- Gráfico: eje horizontal con marcas 0–500 cada 100 y vertical con −0,4…0,4 cada 0,2; paleta oscura `#3987e5` presente en el HTML. Correcto.

Coherencia de las decisiones registradas en `curso/logs/M07_practicas_luna.md` con el libreto:

- H-03 (chi-cuadrado y p-valor en A): presente en la tarea y en la solución (`p=0,98174`).
- H-04 (bandas de confianza y predicción en I): presente (tarea y solución, `0,447` y `1,183`).
- H-05 (retiro de «generaron»): aplicado en la práctica B; la práctica A dice «se fijaron» (ver H-07).
- H-06 (contexto de fotómetro y decisión de uso en B, I y A): presente en los tres bloques.
- H-07 (ν_eff con u(y) de grados infinitos y bloque de 4 gl): presente en la solución de I.
- S-M07-01 (carga de `M07_ejemplos.py` por ruta del script): presente; el script corre con `-I`.
- H-01, H-02 y H-08 son del script y del HTML; verificados por ejecución (ver arriba).

No encontré errores numéricos ni de fórmula en los bloques de práctica.

## Hallazgos

### H-01 — «Cada columna» donde debe decir «cada fila» (severidad: baja)
- **Ubicación:** `curso/S2_modelos_calibracion/M07_libreto.md`, línea 237, enunciado de la práctica I.
- **Problema:** la tabla de réplicas tiene una fila por valor de referencia `x` y tres columnas `y₁, y₂, y₃`. Las tres réplicas están en cada **fila** (mismo `x`), no en cada columna. Un operador puede leer mal la tabla y no reconocer la réplica verdadera que la prueba de falta de ajuste exige.
- **Corrección propuesta:** sustituir «Cada columna contiene tres réplicas independientes al mismo valor de referencia» por «Cada fila contiene tres réplicas independientes al mismo valor de referencia».

### H-02 — «Declarando grande la contribución externa de u(y)» confunde magnitud con grados de libertad (severidad: baja)
- **Ubicación:** `curso/S2_modelos_calibracion/M07_libreto.md`, línea 233, enunciado de la práctica I.
- **Problema:** lo que se declara es que `u(y)` tiene grados de libertad infinitos; la magnitud de `u(y)` (0,20 nmol/mol) no se declara «grande». Con la palabra «grande», un lector puede creer que se pide una valoración de la contribución y no el tratamiento de los grados de libertad que luego usa la solución.
- **Corrección propuesta:** sustituir «declarando grande la contribución externa de u(y)» por «tratando u(y) con grados de libertad infinitos», en línea con la solución docente de la misma práctica.

### H-03 — Etiqueta `[PRÁCTICA]` fuera de la lista de `guia_libreto.md` §1 (severidad: baja)
- **Ubicación:** `curso/S2_modelos_calibracion/M07_libreto.md`, líneas 85, 222 y 329.
- **Problema:** la guía (§1) define la etiqueta `[PRÁCTICA — fase de ejercicios]` solo como marcador de práctica pendiente. El texto ahora desarrollado usa `[PRÁCTICA]` a secas, que no figura en la lista de etiquetas permitidas. Es un cambio de fase que la guía no contempla todavía.
- **Corrección propuesta:** o bien registrar en la guía la etiqueta `[PRÁCTICA]` para prácticas desarrolladas (decisión del responsable de la guía), o bien usar la etiqueta permitida. Mientras no se decida, anotarlo en la bitácora de M07 como decisión pendiente. No cambiar el texto por cuenta propia.

### H-04 — Validación de paleta no reproducible desde el repositorio (severidad: baja)
- **Ubicación:** `curso/logs/M07_practicas_luna.md`, sección «Correcciones tras revisión Haiku», fila H-01/H-02, y «Ejecución» (ruta `/tmp/claude-1000/bundled-skills/.../validate_palette.js`).
- **Problema:** la bitácora documenta que la paleta se validó con un validador situado en un directorio temporal de la sesión. Ese archivo no está en el repositorio (`curso/scripts/` no lo contiene), así que nadie puede repetir el PASS desde el proyecto.
- **Corrección propuesta:** en la bitácora, indicar que la validación se hizo con un validador externo de la sesión, copiar el resultado (contraste calculado de `#2a78d6` y `#3987e5`) y no presentar la ruta temporal como reproducible. No es un error de cifras; solo afecta la trazabilidad.

### H-05 — Notación de `u_c²` en la solución de I puede leerse como varianza de x̂ (severidad: baja)
- **Ubicación:** `curso/S2_modelos_calibracion/M07_libreto.md`, línea 233 («u_c²=0,04+u_param²») y línea 248 (`ν_eff=u_c⁴/(u_param⁴/4)`).
- **Problema:** las dos cantidades están en unidades de `y` (nmol²/mol²), mientras que `u(x̂)` está en nmol/mol y se obtiene dividiendo por `b²`. El script hace exactamente eso: `u_x² = (0,04 + param_var)/b²` y `ν = (0,04 + param_var)²/(param_var²/4)`. El cociente de grados de libertad no depende de la escala, así que el número es correcto, pero el texto no dice en qué unidades está `u_c²`.
- **Corrección propuesta:** añadir «(varianzas en nmol²/mol², antes de dividir por b²)» junto a la fórmula, o escribirla como `u²(x̂)·b² = 0,04 + u²_param`. No cambia ninguna cifra.

### H-06 — Práctica B y referencia de SRP poco explícita (severidad: baja)
- **Ubicación:** `curso/S2_modelos_calibracion/M07_libreto.md`, línea 85 (enunciado de B).
- **Problema:** el enunciado habla de «referencia» e «indicación» y de un «fotómetro de ozono», pero no dice qué estándar es la referencia en el caso (por ejemplo, el SRP en su rol de patrón) ni qué significa en la práctica el punto de 0 nmol/mol o el de 500 nmol/mol. Para operadores de SRP la aplicación queda genérica en B, aunque I y A ya tienen el contexto de decisión de uso.
- **Corrección propuesta:** en una frase del enunciado de B, identificar `x` como concentración asignada al patrón de referencia (por ejemplo, el SRP en el rango declarado) y `y` como la respuesta del fotómetro bajo prueba. No cambiar los números.

### H-07 — «Generación» en el material de A2 contradice la decisión H-05 (severidad: baja)
- **Ubicación:** `curso/S2_modelos_calibracion/M07_libreto.md`, línea 298, material de la escena A2.
- **Problema:** la decisión H-05 retiró «generaron» de la práctica B porque sugiere un proceso aleatorio que no existe. La línea 298 dice «Generación: y_i = 0,3 + 1,001 x_i + δ_i, con desviaciones fijadas en el script». La regla es determinista, pero la palabra reintroduce la confusión que la decisión quiso evitar.
- **Corrección propuesta:** sustituir «Generación:» por «Regla de construcción (determinista):» o «Valores fijados como:» y mantener la fórmula y la referencia a `calc/M07_ejemplos.py`.

## Resumen

- Hallazgos: 7 (0 críticos, 0 de severidad media; todos de severidad baja).
- Números, fórmulas, solución y escalamiento de B, I y A: verificados por ejecución; sin errores.
- Decisiones de `curso/logs/M07_practicas_luna.md`: todas presentes en el libreto o en el script; el único punto no reproducible es la ruta de validación de color (H-04).
- Ozono/SRP: aplicación presente (fotómetro, decisión de uso, no aceptación del instrumento); la identificación del patrón de referencia como SRP es débil en B (H-06).
- Sin cambios en libretos, scripts, referencias ni citas. No se hicieron commits.
