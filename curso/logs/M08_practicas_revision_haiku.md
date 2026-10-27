# M08 — revisión de las prácticas nuevas (Haiku)

Revisor: Haiku 5.5. Alcance: `curso/S2_modelos_calibracion/M08_libreto.md` (prácticas B, I y A y el texto de cada nivel), `curso/S2_modelos_calibracion/calc/M08_practicas_luna.py` y `curso/logs/M08_practicas_luna.md`. No se revisaron referencias, claves ni citas (otro supervisor). No se editó ningún libreto ni script.

## Verificación ejecutada

- `curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M08_practicas_luna.py` → rc=0; todas las aserciones pasan. Cifras de salida: B `u_prec=0,12727922`, `u_c=0,25729361`, `U(k=2)=0,51458721`, sin día `0,22627417`, ingenuo `0,01`; I `u_ind=0,49759421`, `u_cal=0,34088121`, `u_fut=0,45945620`, `ν_eff=299,825783`, `k95=1,96790764`, `U95=0,67082274`, cadena `0,44821870` / `0,61424751` / `U=1,22849501`; A cruce `81,34713835` (único en `[0,500]`, confirmado por malla de 0,1).
- Recalculo independiente en `/tmp/m08rev/` (fuera del repositorio) de todas las cifras narradas en el libreto:
  - B: `x̂=100,000`; `s_r/√8=0,0849`; `δ/√12=0,0289`; `0,0102`; `u(y)=0,0855`; perturbaciones finitas `+0,0853 / −0,1497 / −0,1992`; `u_c=0,2634`; `U=0,527`.
  - I, sensibilidades: `c_b=−99,8004` (exacto), lineal `u_c=0,2637`; `ν_eff=657,95≈658`; `k=1,9636≈1,964`; `U=0,518`.
  - I3: `u_cal=0,3409`; `u_fut=0,4595`; `s_r/√48=0,0346`; `U(k=2)` de 0,6818 y 0,9189; `z=249,900`; `v_p=0,02596`; `u(x̂)=0,4256`; duplicado `0,5800`.
  - I4: cadena `0,4482` / `0,6142` / `U=1,2285`; modelo de función: `1/b=0,9986`, `0,2796`, `0,3226`, `0,5291`.
  - A1: `cov=0,0918`; `u(Δ)=0,3202` compartido, `0,5349` independiente.
  - A2: `U(0)=0,56`, `U(80)=1,1114`, `U(250)=3,0518`, `U(500)=6,0261`; polinomio `0,000128x²−0,0064x−0,3264`; raíz `81,347`.
- `M08_ejemplos.py` reproduce las cifras de B, I y A del libreto (`ν=657,95`, `U=0,5178`, `0,5800`, `0,4256`, cadena, cruce 81,35).
- Valores de M06 (`s_r=0,24`, `s_entre=0,30`, seis días × ocho lecturas) y de M07 (`a=0,242857`, `b=1,00143`, `u(a)=0,2856`, `u(b)=0,0009433`, `cov=−0,000222449`, `s_res=0,3946`) coinciden con los capítulos citados.
- Solo cambió el libreto en los tres marcadores (`git diff`: 44 inserciones, 3 eliminaciones).
- Convenciones: decimal con coma en el texto y unidades nmol/mol; datos rotulados como simulados y no atribuidos a CALAIRE. No hay deducciones largas en clase; las derivaciones se remiten a AX.2 y AX.7.

**Resultado numérico:** no hay errores de cálculo en las cifras narradas ni en la solución docente.

## Hallazgos

### H-01 — Medio — Nivel I sin señales de escalamiento
- **Ubicación:** `M08_libreto.md`, sección «Nivel I» (líneas 121–230). Falta un bloque «Señales de escalamiento» para I; la práctica I (línea 215) tampoco las indica. Nivel B (línea 113) y A (línea 305) sí las tienen.
- **Problema:** la petición pide señales de escalamiento y decisión operativa en las prácticas. M07 sí tiene «Señales de escalamiento en I» (`M07_libreto.md` línea 254), así que el patrón existe en el curso.
- **Corrección propuesta:** añadir antes de «Cierre del capítulo» un bloque «### Señales de escalamiento en I» con 3–4 señales del nivel: covarianza entre entradas no declarada o no justificada; grados de libertad efectivos bajos o distribución de salida dominada por una rectangular; residual de regresión y precisión sin decidir qué término representa la misma variación; y cadena con componente de patrón compartido sin término de covarianza. Cada señal debe nombrar la acción (consultar, escalar a A).

### H-02 — Medio — Contenidos de prop_e sin evidencia práctica ni agrupación declarada
- **Ubicación:** prácticas B (línea 99), I (línea 215), A (línea 288), frente a prop_e §5 M8, que exige para cada contenido separado por punto y coma una evidencia observable o una agrupación justificada.
- **Problema:**
  - B: «resolución y tolerancias» (`u=δ/√12`, `h/√3`, líneas 46–66) y «sensibilidades numéricas (Kragten)» (líneas 70–98) se enseñan, pero la práctica B no los ejercita.
  - I: «sensibilidades analíticas», «covarianzas» y «doble conteo entre residuo y precisión» (líneas 125–176 y 177–196) se enseñan; la práctica I no contiene covarianza ni residuo.
  - A: «componentes comunes en absoluto y diferencia» (líneas 235–254) y «límites de la linealización» (líneas 255–262) se enseñan; la práctica A solo cubre la verificación de función frente a CMC.
- **Corrección propuesta:** la opción de menor alcance, respetando la escala de prop_e, es declarar en la «Solución docente» de cada práctica la agrupación de contenidos con una frase del tipo «Los contenidos X e Y se evalúan en la práctica Z porque…». Si se prefiere evidencia directa, añadir una sola subtarea por contenido ausente con su respuesta numérica ya presente en el libreto (por ejemplo, `u=0,30/√3=0,1732` en B; `u(Δ)=0,320` frente a `0,535` en A).

### H-03 — Medio — Dos modelos de cadena con las mismas entradas dan totales distintos sin explicación
- **Ubicación:** `M08_libreto.md`, línea 205 («Veamos además cómo una función transfiere…») y la frase «Este es otro modelo docente, no una ampliación de las cifras anteriores».
- **Problema:** el primer modelo da `u(Level 2)=0,4482` y `u(cliente)=0,6142`. El segundo, con los mismos `0,28` y `0,42`, da `0,3226` y `0,5291`. La diferencia es que el segundo sustituye la componente `0,35` SRP 55–Level 2 por `u(a)`, `u(b)` y `cov(a,b)`. El texto no lo dice, por lo que un operador puede sumar `0,35` de nuevo o creer que una cifra está mal.
- **Corrección propuesta:** añadir una frase tras la línea 205 que indique que en el modelo de función la contribución de calibración SRP 55–Level 2 ya está dentro de `u(a)`, `u(b)` y `cov(a,b)`, por lo que no se suma `0,35`, y que por eso `0,3226` y `0,4482` no son comparables. Alternativamente, renombrar el segundo bloque como variante y no comparar cifras.

### H-04 — Bajo — Ficha incompleta: AX.4 y script de prácticas
- **Ubicación:** `M08_libreto.md` línea 13 («Anexos») y línea 12 («Datos de ejemplo»).
- **Problema:** la ficha no lista AX.4, que el texto cita en la línea 183–189 y que la práctica I usa (`u²_prec = s²_entre/d + s²_r/(d·n)`). La línea 12 atribuye todas las cifras a `calc/M08_ejemplos.py`, pero las prácticas están en `calc/M08_practicas_luna.py`.
- **Corrección propuesta:** añadir «AX.4: cuadrados medios esperados y `u²_prec` del promedio» a la fila «Anexos» y citar también `calc/M08_practicas_luna.py` en la fila «Datos de ejemplo».

### H-05 — Bajo — Tabla de B3 con unidades y signos inconsistentes
- **Ubicación:** `M08_libreto.md` líneas 83–84.
- **Problema:** la fila de `b` tiene `0,0020` sin unidad y el cambio `-0,1992` usa guion ASCII, mientras que la fila de `a` usa `−`.
- **Corrección propuesta:** escribir `0,0020 nmol/mol` y `−0,1992 nmol/mol`.

### H-06 — Bajo — Diapositiva de A2 pide una curva sin datos de trazado reproducibles
- **Ubicación:** `M08_libreto.md` línea 259 (`[DIAPOSITIVA]`, «Curva de la función de incertidumbre U(x)…»).
- **Problema:** prop_e M8 no exige gráfico, y la práctica A se resuelve con tabla y raíz; no hay omisión. Pero la diapositiva sí pide una curva, y `calc/M08_practicas_luna.py` no exporta la malla de datos para trazarla.
- **Corrección propuesta:** o bien retirar la mención de curva de la diapositiva y dejar la tabla, o bien exportar la malla (por ejemplo cada 5 nmol/mol) desde el script y tratar el gráfico con la habilidad dataviz, con marcas distintas para `U`, CMC y máximo, leyenda, unidades y tabla accesible.

### H-07 — Bajo — Frase confusa sobre la aproximación normal en B1
- **Ubicación:** `M08_libreto.md` línea 38: «Esta ficha y la linealidad local, no solo los grados de libertad, sostienen la aproximación normal de cobertura usada en B3».
- **Problema:** la frase no dice qué sostiene qué y repite una idea que B3 ya trata. Además hay doble espacio tras la sustitución.
- **Corrección propuesta:** reescribir como: «La aproximación normal de cobertura de B3 se apoya en la linealidad local y en los grados de libertad grandes de a y b; no depende solo de los grados de libertad.»

## Observaciones sin hallazgo

- Alcance B/I/A: B no incluye cobertura ni covarianza fuera de `k≈2` condicionado; I no añade la covarianza de la regresión en la práctica; A se limita a CMC y función. No hay contenido fuera de prop_e §5 M8.
- Origen de datos: todos los valores son simulados, rotulados y reproducibles desde `calc/`; la práctica A declara que la CMC es hipotética y no de CALAIRE.
- Soluciones: todas las soluciones docentes coinciden con la ejecución; la práctica I aplica Welch–Satterthwaite solo a componentes independientes, como exige prop_e.
- Aplicación ozono/SRP: el contexto SRP 55 → Level 2 → cliente y el diseño F-PSMT-01 (12×8×6, 576 observaciones no intercambiables) están presentes y son coherentes.
- Escalamiento: B y A tienen señales; I queda pendiente (H-01).

## Conclusión

Hay siete hallazgos: tres de severidad media (H-01, H-02, H-03) y cuatro de severidad baja (H-04 a H-07). No hay errores numéricos ni incoherencias de cálculo. Lo más útil antes de cerrar M08 es H-01 y H-03; H-02 requiere decidir si se añade evidencia o se declara la agrupación.
