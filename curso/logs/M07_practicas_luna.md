# M07 — bitácora de prácticas (luna)

## Plan

Desarrollar únicamente los tres bloques marcados de `curso/S2_modelos_calibracion/M07_libreto.md`, conforme a `prop_e.md` §5, M7, y al nivel de autonomía de §2:

| Nivel | Alcance de la práctica | Datos y verificaciones previstas |
|---|---|---|
| B | OLS en condiciones adecuadas, residuos, R² con sus límites, intervalo observado, inversión y signo de corrección. No añadir inferencia ni elección de método. | Conjunto de seis pares simulados, con generación reproducible por valores fijados; ajuste, residuos y uso inverso. Gráfico de residuos con tabla accesible. |
| I | Comparar OLS/WLS y justificar pesos; incertidumbre de predicción inversa; falta de ajuste solo con réplicas reales al mismo valor de referencia. Escalar si la incertidumbre de `x` importa. | Serie heteroscedástica simulada; cálculo de `u`, `U`, grados efectivos y cobertura declarada; conjunto simulado con réplicas al mismo `x` para F de falta de ajuste. |
| A | Ajustar el mismo conjunto con OLS, WLS y GGMR en idéntica orientación; componente común; matrices; diagnóstico y verificación de la implementación con ejemplo publicado ISO/TS 28037 dentro del alcance `V_xy=0`. No afirmar validación universal ni uso de producción. | Conjunto sintético y covarianzas fijados en script; contraste publicado sin modificar datos ni matrices con resultados normativos publicados. |

No crear taller adicional, no modificar otros capítulos, guía, revisión final ni referencias bibliográficas/citas/sección de referencias del capítulo. Mantener referencias existentes intactas. Ejecutar cálculo con `curso/.venv/bin/python`; conservar datos simulados explícitamente rotulados y no atribuirlos a CALAIRE. Leer e implementar la habilidad dataviz antes de generar el gráfico.

## Ejecución

- Se sustituyeron de forma localizada los marcadores B, I y A por prácticas terminadas con narración dirigida a operadores, datos suficientes, tareas, solución docente verificable, interpretación, criterio de logro y señales de escalamiento pertinentes al nivel.
- B: recta OLS $a=0,24285714$ nmol/mol, $b=1,0014285714$; residuos $-0,042857; 0,314286; -0,428571; 0,328571; -0,414286; 0,242857$ nmol/mol; $s_{res}=0,39460649$ nmol/mol; $R²=0,99999645$. En $y=250,50$, $\hat x=249,90014265$ nmol/mol y corrección $-0,59985735$ nmol/mol. El conjunto está identificado como simulado, fijado en el enunciado/script, y explícitamente no representa Level 2 ni CALAIRE.
- I: OLS $(a,b)=(0,44761905;1,0007428571)$; WLS $(0,41685160;1,0009213402)$. En uso inverso, $u(\hat x)=0,25644562$ nmol/mol, $\nu_{eff}=25,832495$, $k_{95}=2,056178$, $U=0,52729793$ nmol/mol. El ejemplo de falta de ajuste produce $SS_{LOF}=0,966$, $SS_{PE}=0,080$, $F(2,8)=48,3$, $p=3,4216313\cdot10^{-5}$; se explicita rechazo bajo los supuestos del caso, sin convertirlo en causa ni permiso de exclusión.
- A: mismo conjunto y orientación para OLS/WLS/GGMR. OLS=WLS $a=0,3047619$, $b=1,00131429$; GGMR $a=0,30472535$, $b=1,00131443$, $Q=0,40890065$, cuatro grados de libertad declarados. Las abscisas ajustadas se reproducen en el capítulo/script. La componente común cambia $u(a)$ de $0,34151683$ a $0,36203815$ nmol/mol. Con ISO/TS 28037 §10.3, tablas 25–26, se reproducen al redondeo publicado $a=0,3424$, $b=1,0012$, $Q=1,772$ y también errores estándar/covarianza/abscisas con aserciones en código. Datos y covarianzas publicados no se modificaron.
- El gráfico se implementó como HTML/SVG con línea y círculos diferenciados, leyenda, unidades, títulos de punto y tabla accesible. Para corregir H-01, se añadieron marcas y rejilla tenue sólida en x (0–500 cada 100) e y (−0,4 a 0,4 cada 0,2 nmol/mol). La paleta clara usa #2a78d6 y la oscura #3987e5 por variables CSS con tema explícito. Validación reproducible: `/tmp/claude-1000/bundled-skills/2.1.310/61ae7f16d6904594c66415b5d33a16e9/dataviz/scripts/validate_palette.js`, invocado con `node ... "#2a78d6" --mode light` y `node ... "#3987e5" --surface "#1a1a19" --mode dark`; ambas pasaron. El HTML se regeneró por el script de la sección y se renderizó con Chromium headless; la práctica mantiene el trazado manual como tarea.
- Primer intento de ejecución de la gráfica con matplotlib no fue posible porque la dependencia no está instalada en `curso/.venv`; se reemplazó por SVG/HTML usando solo biblioteca estándar, sin instalar paquetes. La ejecución posterior completó con código de salida 0.

## Archivos tocados

1. `curso/S2_modelos_calibracion/M07_libreto.md` — solo los tres bloques de práctica; no se editaron otras escenas, la ficha ni Referencias del capítulo.
2. `curso/S2_modelos_calibracion/calc/M07_practicas_luna.py` — cálculos y generación reproducible del gráfico accesible.
3. `curso/logs/M07_B_residuos.html` — salida gráfica reproducible y tabla accesible.
4. `curso/logs/M07_practicas_luna.md` — esta bitácora.

## Comprobaciones

- `curso/.venv/bin/python curso/S2_modelos_calibracion/calc/M07_practicas_luna.py`: rc=0; imprimió los resultados anteriores y `A comprobación publicada: PASS`.
- Validación de colores: `#2a78d6` light sobre `#fcfcfb` PASS; `#3987e5` dark sobre `#1a1a19` PASS.
- `grep -n '\[PRÁCTICA' curso/S2_modelos_calibracion/M07_libreto.md`: exactamente tres bloques desarrollados, B/I/A, sin marcador pendiente ni taller adicional.
- `git diff --check` para libreto y script: sin errores de whitespace.
- Sin commits.

## Correcciones tras revisión Haiku

Se evaluaron los ocho hallazgos individualmente. H-01 a H-08 se aplican; no se rechaza ningún hallazgo.

| Hallazgo | Decisión | Ubicación y resultado |
|---|---|---|
| H-01 | Aplicar | `calc/M07_practicas_luna.py` genera marcas x cada 100 y y cada 0,2 nmol/mol, con rejilla tenue sólida. HTML regenerado en `curso/logs/M07_B_residuos.html`; marcas, ejes, unidades, leyenda y tabla presentes; paleta validada en modo claro y oscuro por la ruta anotada arriba. |
| H-02 | Aplicar | Se corrigió esta bitácora: modo claro #2a78d6, modo oscuro #3987e5 mediante variables CSS; el validador exacto y ambos comandos quedaron documentados. Resultado: PASS para ambos modos. |
| H-03 | Aplicar | `M07_libreto.md`, Práctica A: ahora exige obtener z_x/z_y, verificar que suman Q, evaluar chi-cuadrado con 4 gl y reportar cola superior. Solución actualizada: Q=0,40890065; p_superior=0,98174172; residuos blanqueados y su suma de cuadrados registrados. Se aclara que p alto no demuestra validez. |
| H-04 | Aplicar | `M07_libreto.md`, escena I1 y Práctica I: se solicita calcular y comparar bandas puntuales en x=250. `calc/M07_practicas_luna.py` reproduce IC de media ±0,44727816 e intervalo de predicción ±1,18338678 nmol/mol. La solución explica la dispersión adicional de nueva respuesta. |
| H-05 | Aplicar | `M07_libreto.md`, Práctica B: se reemplazó «generaron» por la aclaración de valores fijados, sin generador aleatorio. El origen simulado queda reproducible junto con el script. |
| H-06 | Aplicar | `M07_libreto.md`, prácticas B, I y A: contexto explícito de fotómetro de ozono, puntos/indicación en nmol/mol y decisión estadística de uso, no aceptación del instrumento. Valores numéricos no cambiaron. |
| H-07 | Aplicar | `M07_libreto.md`, Práctica I: se explicita u(y) con grados de libertad infinitos, bloque de parámetros con 4 gl y fórmula de Welch–Satterthwaite. El cálculo reproduce ν_eff=25,832495, k=2,056178 y U=0,52729793 nmol/mol. |
| H-08 | Aplicar | `calc/M07_practicas_luna.py`: eliminado el import `_unused`; se agregó `comma()` y se eliminó el encadenamiento de `.replace` en celdas y tabla SVG/HTML. Script ejecutado con éxito. |

### Corrección de importación bajo Python aislado

- Decisión S-M07-01: se carga `M07_ejemplos.py` desde el directorio del script mediante `importlib.util.spec_from_file_location` y `Path(__file__).with_name(...)`. No se modifica `sys.path` ni se añade el directorio de trabajo.
- Ejecución exacta: desde `curso/`, `.venv/bin/python -I S2_modelos_calibracion/calc/M07_practicas_luna.py`; código de salida 0. El script regeneró `logs/M07_B_residuos.html`; todas las comprobaciones existentes, incluido el `assert` de ISO y `A comprobación publicada: PASS`, se completaron.
- Salida real:

```text
B OLS a=0.24285714 b=1.0014285714 s_res=0.39460649 R2=0.99999645
B residuos [-0.04285714, 0.31428571, -0.42857143, 0.32857143, -0.41428571, 0.24285714] máximo abs 0.42857143
B inversión xhat=249.90014265 corrección=-0.59985735
I OLS [0.44761905, 1.00074286] WLS [0.4168516, 1.00092134]
I bandas en x=250 IC95 media ±0.44727816 IP95 nueva respuesta ±1.18338678 nmol/mol
I pesos 1/u2 [16.0, 11.111111, 6.25, 2.777778, 1.234568, 0.694444]
I uso inverso u(xhat)=0.25644562 nu_eff=25.832495 k95=2.056178 U95=0.52729793
I falta de ajuste SS_LOF=0.966000 SS_PE=0.080000 F(2,8)=48.300000 p=3.4216313e-05
A mismo conjunto OLS [0.3047619, 1.00131429] WLS [0.3047619, 1.00131429] GGMR [0.30472537, 1.00131443]
A x ajustadas [-0.00133, 99.98983, 200.03721, 299.94405, 400.04764, 499.98259] Q 0.40890065 df=4 p_superior=0.98174172
A residuos blanqueados zx [0.0047893, 0.03640504, -0.14506621, 0.22308804, -0.19377201, 0.07326999] zy [-0.00848877, -0.06497411, 0.23782564, -0.35758733, 0.30449751, -0.11127292] suma cuadrados 0.40890065
A componente común u(a) sin=0.34151683 con=0.36203815 u(b)=0.00112799
A ISO publicado a=0.3424009 b=1.0012308 Q=1.771847 objetivo norma: 0,3424; 1,0012; 1,772
A comprobación publicada: PASS (parámetros, Q y errores estándar al redondeo de tabla)
```
