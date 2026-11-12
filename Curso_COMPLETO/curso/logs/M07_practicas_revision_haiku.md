# M07 — revisión de las prácticas B, I y A (revisor: haiku)

Alcance: `curso/S2_modelos_calibracion/M07_libreto.md` (bloques de práctica, escalamiento y ficha), `curso/S2_modelos_calibracion/calc/M07_practicas_luna.py`, `curso/logs/M07_practicas_luna.md` y la salida gráfica `curso/logs/M07_B_residuos.html`. No se editó ningún archivo del curso. Referencias bibliográficas y citas no auditadas (otro supervisor).

## Verificación por ejecución

- `curso/.venv/bin/python curso/S2_modelos_calibracion/calc/M07_practicas_luna.py` → rc=0; la comprobación ISO imprime `PASS`.
- Los números de los bloques coinciden con la salida del script: B (a=0,242857; b=1,001428571; s_res=0,394606; R²=0,99999645; x̂=249,900143; corrección −0,599857); residuos −0,042857; 0,314286; −0,428571; 0,328571; −0,414286; 0,242857 (suma cero); I (OLS 0,447619/1,000743; WLS 0,416852/1,000921; pesos 16; 11,111111; 6,25; 2,777778; 1,234568; 0,694444; u(x̂)=0,256446; ν_eff=25,8325; k=2,05618; U=0,527298; SS_LOF=0,966; SS_PE=0,080; F(2,8)=48,3; p=3,42·10⁻⁵); A (OLS=WLS 0,304762/1,00131429; GGMR 0,304725/1,00131443; abscisas ajustadas; Q=0,408901; gl=4; u(a) 0,341517 → 0,362038; u(b)=0,001128; ISO publicado a=0,3424009, b=1,0012308, Q=1,771847, u(a)=2,0569, u(b)=0,0090, cov=−0,0129).
- Comprobación de la solución de B a mano: en x=200, ŷ=200,528571; r=200,1−200,528571=−0,428571. Correcta.
- Comprobación de I: pv=u²(x̂)·b²−0,04≈0,02595; ν_eff=(0,04+pv)²/(pv²/4)≈25,8, consistente con el script.
- Gráfico: `curso/logs/M07_B_residuos.html` renderizado con Chromium headless (`/usr/bin/chromium --headless --screenshot`) y revisado visualmente en modo oscuro: abre, muestra línea, marcadores, línea de cero, leyenda y tabla accesible. Ver H-01.
- Estadística: la prueba de falta de ajuste (réplicas al mismo x, 4 niveles × 3, gl 2 y 8) está bien planteada. La lectura de GGMR con Vxy=0 respeta el alcance declarado. La explicación de por qué la componente común no se promedia con más puntos es correcta.

No encontré errores numéricos ni de fórmula en los bloques.

## Hallazgos

### H-01 — Gráfico sin escala legible (severidad: media)
- **Ubicación:** `curso/S2_modelos_calibracion/calc/M07_practicas_luna.py`, cadena `svg` (textos de ejes con solo «0» y «500»; eje vertical sin marcas). Salida: `curso/logs/M07_B_residuos.html`.
- **Problema:** el eje horizontal tiene marcas solo en 0 y 500; el eje vertical solo muestra «0». No hay marcas en 100–400 ni en valores de residuo (por ejemplo ±0,2 y ±0,4 nmol/mol). El lector no puede leer la magnitud de los residuos en el gráfico; solo la tabla lo permite. La práctica pide «unidades y marcas distinguibles» y el skill dataviz exige ejes con escala.
- **Corrección propuesta:** añadir marcas y valores en x (0, 100, 200, 300, 400, 500) y en y (−0,4; −0,2; 0; 0,2; 0,4 nmol/mol), con líneas de rejilla tenues; regenerar el HTML con el script y revisar el render.

### H-02 — La bitácora describe una paleta oscura que no está en el HTML (severidad: baja)
- **Ubicación:** `curso/logs/M07_practicas_luna.md`, líneas 21 y 34 («su paso oscuro #3987e5 validado en modo oscuro»).
- **Problema:** `grep` sobre `curso/logs/M07_B_residuos.html` solo encuentra `#2a78d6` como color de las marcas en ambos modos. `#3987e5` no aparece. El contraste de `#2a78d6` sobre `#1a1a19` es 3,94:1 (sobre `#fcfcfb` es 4,3:1); cumple el mínimo de 3:1 para elementos gráficos, pero no es lo que la bitácora declara. Además, la validación con `validate_palette.js` no está en el repositorio del curso (`scripts/` no contiene el validador) ni en el script, así que no es reproducible desde el proyecto.
- **Corrección propuesta:** o bien usar `#3987e5` para las marcas en modo oscuro mediante variables CSS y regenerar, o bien corregir la bitácora para decir que el modo oscuro usa `#2a78d6` con contraste 3,94:1. En ambos casos, anotar la ruta exacta del validador usado.

### H-03 — Falta el diagnóstico chi-cuadrado en la práctica A (severidad: media)
- **Ubicación:** `curso/S2_modelos_calibracion/M07_libreto.md`, bloque «Práctica A», tarea y «Solución docente» (líneas ~323–349).
- **Problema:** la ficha de M07 (Nivel A) incluye «diagnóstico por residuos ponderados y chi-cuadrado». El bloque pide Q y los grados de libertad, pero no pide calcular ni interpretar los residuos ponderados ni la cola superior del chi-cuadrado. El script sí los calcula (Q=0,408901, gl=4, p=0,98174; discrepancias blanqueadas zx y zy). Además, la solución dice «la cifra pequeña no certifica bondad», sin p-valor que sostenga el argumento.
- **Corrección propuesta:** añadir a la tarea A: «calculen los residuos ponderados blanqueados de x e y, comparen Q con χ²(4) y expliquen qué significa p=0,98 y por qué no prueba la validez del modelo». Añadir a la solución el valor p=0,98174 y el texto de interpretación.

### H-04 — Bandas de confianza y predicción de I no están en la práctica (severidad: media)
- **Ubicación:** `curso/S2_modelos_calibracion/M07_libreto.md`, ficha («Nivel I añade… bandas de confianza y predicción») y bloque «Práctica I».
- **Problema:** la ficha declara las bandas como competencia de I, pero la práctica I no pide ninguna. El script del base (`calc/M07_ejemplos.py`) ya las calcula para x=250 (IC95 media ±0,447 nmol/mol; IP95 nueva lectura ±1,183 nmol/mol), pero el operador no las usa. Sin esta tarea, la diferencia entre media y nueva lectura no se practica en I.
- **Corrección propuesta:** añadir una subtarea corta en I: con la recta B, calcular la banda de confianza y la de predicción en x=250 nmol/mol, y comparar ±0,447 con ±1,183 (la predicción incluye la dispersión de una nueva lectura). Añadir la solución con esos valores y una línea de interpretación. Incluir el cálculo en el script de la sección.

### H-05 — El enunciado habla de «generación» sin regla declarada (severidad: baja)
- **Ubicación:** `curso/S2_modelos_calibracion/M07_libreto.md`, bloque «Práctica B», primera frase («Se generaron fijando x=… y=…»).
- **Problema:** los valores de y se escribieron a mano en el script y en el enunciado. No hay una regla (semilla, modelo de error) que los genere. La instrucción del trabajo exige datos simulados con regla reproducible; «fijados» cumple reproducibilidad, pero «generaron» sugiere un proceso que no existe.
- **Corrección propuesta:** sustituir por «Los valores están fijados en el enunciado y en `calc/M07_practicas_luna.py`; no proceden de un generador aleatorio».

### H-06 — Poco contexto SRP/ozono en las prácticas (severidad: baja)
- **Ubicación:** bloques «Práctica B», «Práctica I» y «Práctica A» (primeros párrafos).
- **Problema:** los números se presentan como «referencia» e «indicación» sin decir qué representan en el SRP: un punto de calibración de un fotómetro de ozono, la decisión que sigue (aceptar, ajustar, escalar) o el uso de la indicación de 250,50 nmol/mol. El caso ozono/SRP queda casi solo en la frase «fotómetro real». Para operadores, el ejercicio se lee como una tarea estadística genérica.
- **Corrección propuesta:** en el primer párrafo de B y de I, indicar en una frase que la indicación de 250,50 nmol/mol es la respuesta de un fotómetro en un punto del intervalo de trabajo, y que el resultado alimenta una decisión de uso (no de aceptación). No cambiar los números.

### H-07 — Welch–Satterthwaite sin justificación en la solución de I (severidad: baja)
- **Ubicación:** `curso/S2_modelos_calibracion/M07_libreto.md`, «Solución docente» de Práctica I («ν_eff=25,8325»).
- **Problema:** el lector no puede reproducir ν_eff sin saber que u(y) se trata con grados infinitos y el bloque de parámetros con 4 gl. El script lo hace bien (`nu=(0,04+pv)²/(pv²/4)`), pero el texto no lo dice.
- **Corrección propuesta:** añadir una línea: «ν_eff = u_c⁴ / (u_param⁴/4), con u(y) tratada como de grados infinitos y el bloque de parámetros con 4 gl; u_c² = 0,04 + pv».

### H-08 — Código auxiliar sin uso en el script (severidad: baja)
- **Ubicación:** `curso/S2_modelos_calibracion/calc/M07_practicas_luna.py`, línea con `from M07_ejemplos import main as _unused` y el comentario que la acompaña; también las líneas `circles=`/`rows=` que usan `.replace` para formatear la coma.
- **Problema:** el import no ejecuta nada y su comentario no explica lo que hace; los `.replace` encadenados son frágiles de mantener.
- **Corrección propuesta:** eliminar el import y usar una función de formato (`f"{r:.5f}".replace(".", ",")` una sola vez por valor).

## Resumen

- Hallazgos: 8 (0 críticos; 3 de severidad media: H-01, H-03, H-04; el resto baja).
- Números, fórmulas y solución de B, I y A: verificados por ejecución; sin errores.
- Alcance: B, I y A respetan el nivel; I y A necesitan completar tareas que ya figuran en su ficha (H-03, H-04).
- Ozono/SRP: presente pero débil (H-06).
