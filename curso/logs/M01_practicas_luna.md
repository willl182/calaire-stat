# Bitácora: prácticas de M01

## Plan

- Alcance tomado de `prop_e.md` §5, M1 y §2–§3: tres prácticas, una por nivel acumulativo. B: recalcular tres concentraciones con dos coeficientes/secciones eficaces declarados y comunicar signo y cambio relativo. I: comparar mediciones en escalas distintas usando los cocientes de valores implementados (pares 1,147/1,1329 y 308,32/304,39), sin confundir cambio de escala con corrección instrumental. A: identificar contribuciones comunes y específicas en resultados absolutos y diferencias; no adelantar una propagación matricial de M8/M9.
- Formato: sustituir exclusivamente los tres marcadores del libreto M01, con enunciado narrado, datos suficientes, tareas, solución docente con cifras/comprobaciones, interpretación, decisión operativa, señales de escalamiento y criterio de logro. Sin taller adicional.
- Datos: B y A simulados expresamente y generados por reglas numéricas incluidas en el enunciado/script. I usa los pares declarados que ya figuran en M01 y prop_e; se agrega un valor base de ejemplo expresamente simulado para aplicar el factor. No se presentan resultados como propios de CALAIRE.
- Cálculos: crear `curso/S1_fundamentos/calc/M01_practicas_luna.py` y ejecutar con `curso/.venv/bin/python`. No gráficos. No modificar citas ni referencias.

## Ejecución

- Sustituidos únicamente los marcadores en `curso/S1_fundamentos/M01_libreto.md` por bloques `[PRÁCTICA]` completos para B, I y A.
- B: regla simulada $T=\exp[-\alpha_1 L(c/10^9)p_0]$ con $\alpha_1=308,32\ \mathrm{atm^{-1}cm^{-1}}$, $\alpha_2=304,39\ \mathrm{atm^{-1}cm^{-1}}$, $L=90,0\ \mathrm{cm}$, $p_0=1\ \mathrm{atm}$ y objetivos 100,0, 250,0 y 500,0 nmol/mol. Las indicaciones calculadas son 100,000→101,291; 250,000→253,228; 500,000→506,456 nmol/mol. Cambio relativo común: +1,2911068 %; cambios absolutos: +1,291; +3,228; +6,456 nmol/mol.
- I: 1,147/1,1329 = 1,012445935; incremento +1,2445935 %. 308,32/304,39 = 1,012911068; incremento +1,2911068 %. Con base simulada 400,0 nmol/mol, salida 405,164, error +5,164 nmol/mol y error relativo +1,2911 % con referencia como denominador.
- A: con S=2,0, C1=+0,3 y C2=−0,1 nmol/mol, Y1=2,3, Y2=1,9 y Δ=+0,4 nmol/mol; se comprueba igualdad con C1−C2. Con sensibilidad 0,8 a S en Y2, Y2=1,5 y Δ=+0,8 nmol/mol, mostrando cancelación parcial.
- Archivos creados: `curso/S1_fundamentos/calc/M01_practicas_luna.py`; `curso/logs/M01_practicas_luna.md`.
- Archivo editado: `curso/S1_fundamentos/M01_libreto.md`, solo los tres bloques de práctica. No se tocaron `curso/guia_libreto.md`, `prop_e.md`, `curso/revision_final.md`, otros capítulos, claves, citas ni referencias.

## Ronda de correcciones Haiku

Archivo revisado: `curso/logs/M01_practicas_revision_haiku.md`. Se decidieron los nueve hallazgos individualmente:

| Hallazgo | Decisión | Ubicación y resultado |
|---|---|---|
| H-01 | Aplicado | `M01_libreto.md`, práctica I, enunciado. Se declara que 308,32 atm⁻¹ cm⁻¹ corresponde a la salida de referencia simulada de 400,0 nmol/mol y 304,39 atm⁻¹ cm⁻¹ a la salida reescalada. |
| H-02 | Aplicado | `calc/M01_practicas_luna.py` calcula y comprueba $y$, $e$ y $100e/x$; `M01_libreto.md`, práctica I, ya queda respaldada por el script. Resultado: 405,164427 nmol/mol; +5,164427 nmol/mol; +1,2911068 %. |
| H-03 | Aplicado | `M01_libreto.md`, práctica B. Se solicita error con signo y corrección aditiva opuesta en el primer punto, además de explicar la conversión de atm a nmol/mol. La solución da $e=+1,291107$ y corrección −1,291107 nmol/mol; $10^{-7}$ atm / 1 atm × $10^9$ = 100,000 nmol/mol. Criterio de logro actualizado para cubrir estas evidencias. |
| H-04 | Aplicado | `M01_libreto.md`, práctica B. El título nombra el coeficiente de absorción; se aclara que la relación con la sección eficaz incluye un factor de número molecular constante y se opera con α, como en el modelo. |
| H-05 | Aplicado | `M01_libreto.md`, práctica I, enunciado. Los pares de σ y α quedan rotulados como publicados (fuentes ya citadas en la ficha/escena); la base x=400,0 nmol/mol se etiqueta como simulada. |
| H-06 | Aplicado | `M01_libreto.md`, escenas I1 y práctica I. Se explica que los cocientes implícitos α/σ son 268,805580 y 268,682143, con diferencia relativa 0,045941 %, consistente con pares publicados redondeados; no es error de cálculo ni corrección instrumental. El cálculo y aserción se añadieron al script. |
| H-07 | Aplicado | `M01_libreto.md`, práctica A, solución. Se indica qué permite afirmar el modelo sobre la cancelación y Δ=+0,4 nmol/mol, y qué no permite concluir sobre $u(Δ)$ sin covarianzas. |
| H-08 | Aplicado | `calc/M01_practicas_luna.py`. Se importa `exp` explícitamente de `math` y se elimina `__import__`. |
| H-09 | Aplicado con ajuste | `M01_libreto.md`, práctica B, enunciado/solución. Se conserva la regla reproducible y se declara que solo documenta cómo se generaron los datos, no es tarea de inversión; la solución llama a la recuperación una comprobación, no una actividad del operador. |

## Ejecución final tras correcciones

`curso/.venv/bin/python curso/S1_fundamentos/calc/M01_practicas_luna.py` terminó con rc=0. Resultados impresos: B 100,000→101,291 (Δ +1,291), 250,000→253,228 (Δ +3,228), 500,000→506,456 (Δ +6,456) nmol/mol; incremento relativo +1,2911068 % en cada nivel; punto B1 $e=+1,291106804$ y corrección $-1,291106804$ nmol/mol, con conversión $10^{-7}$ atm a 100,000 nmol/mol. I: cocientes 1,012445935 (+1,244593521 %) y 1,012911068 (+1,291106804 %); aplicación a x=400,0: y=405,164427 nmol/mol, e=+5,164427 nmol/mol, relativo +1,291106804 %; cocientes implícitos α/σ 268,805580 y 268,682143, diferencia +0,045941 %. A: Y1=2,300, Y2=1,900, Δ=+0,400; con sensibilidad desigual Y2=1,500, Δ=+0,800 nmol/mol. Las aserciones del script cubren las salidas de B e I y las restas de A.

## Corrección supervisor S-M01-01

- En la solución de práctica B se aclaró la secuencia de unidades del punto 1: presión parcial $p_{O_3}=-\ln(T)/(\alpha L)=1,00000\times10^{-7}\ \mathrm{atm}$; fracción molar $p_{O_3}/p_0=1,00000\times10^{-7}$ adimensional; conversión a $100,000\ \mathrm{nmol/mol}$ al multiplicar por $10^9\ \mathrm{nmol/mol}$. Se diferenciaron las variables para no repetir la división por $p_0$.
- Alcance: solo ese párrafo de práctica B; no se modificaron otros capítulos, escenas, citas, bibliografía, scripts ni hitos.
- Comprobación: `curso/.venv/bin/python curso/S1_fundamentos/calc/M01_practicas_luna.py` y `git diff --check` para los dos archivos modificados.

## Comprobaciones

- `curso/.venv/bin/python curso/S1_fundamentos/calc/M01_practicas_luna.py`: rc=0; tras aplicar correcciones, imprime las cifras finales y ejecuta aserciones sobre recuperación de objetivos, error/corrección, salida I aplicada, cocientes publicados y diferencias de A.
- `curso/.venv/bin/python curso/S1_fundamentos/calc/M01_modelo_variables.py`: rc=0 en la ejecución anterior; script de ejemplos existente ejecutado sin cambios.
- `git diff --check -- curso/S1_fundamentos/M01_libreto.md curso/S1_fundamentos/calc/M01_practicas_luna.py curso/logs/M01_practicas_luna.md`: sin errores de whitespace tras las correcciones.
- El diff de M01 incluye además un cambio concurrente de citas en una escena anterior a las prácticas. Se preservó sin editar; no es parte de esta ronda. Los cambios propios al libreto se limitaron a los bloques B, I y A. No se modificaron referencias ni citas.
- Pendiente: revisión editorial independiente y validación de los resultados de práctica por supervisor, fuera de este alcance.