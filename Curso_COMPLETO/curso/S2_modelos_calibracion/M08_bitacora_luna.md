# Bitácora de desarrollo — M08

## Plan

### Alcance por nivel (tomado literalmente de `prop_e.md`, §5, M8)

- **Competencia estadística:** «construir un presupuesto coherente con el resultado de interés y propagar varianzas y covarianzas.»
- **B:** «modelo de medición; evaluación tipo A y tipo B; `u = U/k`, resolución y tolerancias; elección entre `s` y `s/√n` según el resultado; presupuesto tabular con sensibilidades numéricas (Kragten) para entradas independientes; combinada y expandida; `k ≈ 2` solo donde el ejercicio lo justifica.»
- **I añade:** «sensibilidades analíticas; covarianzas; `ν_eff` y cobertura; resultado individual, promedio de calibración y resultado futuro; doble conteo entre residual de regresión y precisión; propagación por la cadena SRP 55 → Level 2 → cliente. En una práctica se selecciona y justifica la cobertura y los grados de libertad, incluida la adecuación y las limitaciones de Student y Welch–Satterthwaite. Este último se aplica de forma elemental solo a componentes independientes conforme al modelo; no se extiende mecánicamente a presupuestos correlacionados. Si el caso exige cobertura numérica no disponible en I, se escala a A. Un número pequeño de grados de libertad exige revisar la cobertura, no descarta por sí mismo una prueba t de media cuyos supuestos sí se cumplen.»
- **A añade:** «componentes comunes en resultados absolutos y diferencias; límites de la linealización; función de incertidumbre sobre un intervalo y su relación con la capacidad de medición y calibración (CMC; misma magnitud, unidades y cobertura).»

### Escenas previstas

1. Ficha: competencia, prerrequisitos M1/M3/M4/M6/M7, alcance aditivo B/I/A, orígenes de datos, anexos AX.2, AX.3, AX.7 y AX.13 cuando corresponda, referencias técnicas.
2. B1: mensurando, modelo directo/indirecto y presupuesto; evaluación tipo A y B; ejemplo numérico simulado de una calibración puntual.
3. B2: conversión `u=U/k`, resolución y tolerancias; distinguir semiamplitud de resolución total y variación observada; `s` frente a `s/√n`; ejemplo de lectura frente a promedio con componente común.
4. B3: presupuesto tabular estilo Kragten para entradas independientes, sensibilidades numéricas, `u_c`, `U` y criterio condicional para `k≈2`; marcador de práctica B y señales de escalamiento de prop_e §2.
5. I1: derivadas analíticas, ley de propagación con covarianza, cálculo independiente ilustrativo y remisión AX.2/AX.3.
6. I2: grados de libertad efectivos, Student, cobertura y Welch–Satterthwaite solo para contribuciones independientes; ejemplo reproducible y límites; escalar a A si se requiere cobertura no disponible.
7. I3: distinguir incertidumbre del resultado individual, promedio de calibración y uso futuro; precisión/residual sin doble conteo; ejemplo de presupuesto con resultados de interés explícitos.
8. I4: cadena de propagación SRP 55 → Level 2 → cliente, con entradas y ejemplo reproducible; marcador de práctica I.
9. A1: covarianza común en resultados absolutos y diferencias; cancelación parcial/total, ejemplo y límites de la linealización.
10. A2: función de incertidumbre a lo largo del intervalo y comparación con CMC de igual magnitud, unidades y cobertura; ejemplo punto a punto, máximo de `U` frente a CMC; marcador práctica A, señales de escalamiento y transición a M9.

### Datos y rótulo de origen

- Presupuestos didácticos de calibración puntual, evaluación tipo A/B, sensibilidad, cobertura, predicción futura y cadena: **simulados**, valores fijados y regla de generación explícita en `calc/M08_ejemplos.py`; no describen el desempeño de CALAIRE.
- Valores publicados del NIST SRP 6008 y BIPM-SRP27 (`u=√(0,28²+(0,011·x)²)` y `u=√(0,28²+(0,00292·x)²)`) solo si se verifican en sus documentos; rótulo **publicado**. No presentar el presupuesto SRP 27 como presupuesto del SRP 55.
- Diseño y cadena operativa del Level 2 (F-PSMT-01; 12 puntos × 8 lecturas × 6 días; SRP 55 → Level 2 → cliente): fuente **propia**, citado como contexto documental. Cualquier valor de ejemplo derivado se mantendrá simulado salvo cálculo documentado de los archivos reales.

### Cálculos previstos

- Crear `calc/M08_ejemplos.py`, ejecutable con `curso/.venv/bin/python`, para reproducir todos los números del capítulo: presupuesto independiente y tabla Kragten, sensibilidades analíticas, conversión rectangular/resolución/tolerancia, `s` y `s/√n`, covarianza, `u_c`, `ν_eff`, cuantiles Student, `U`, distinción de resultados, propagación de cadena y función `U(x)` frente a CMC. El script imprimirá datos de entrada, unidades y resultados sin redondeo prematuro; números del libreto deben corresponder a su salida.

### Referencias a verificar en `docs/` con `pdftotext`

- GUM (JCGM 100): §§4–7, Anexo H; verificar numerales precisos usados.
- JCGM GUM-6: §§11–12; modelo y desarrollo de modelos de medición.
- `Metrology and Measurement Uncertainty` capítulos 5–6: tipos A/B, incertidumbre combinada/expandida, grados de libertad, propagación/covarianza.
- `Introduction to Statistics in Metrology`, capítulos 6–7: evaluación, sensibilidades, covarianzas y límites de linealización.
- NIST SRP 6008, p. 2; BIPM.QM-K1, Apéndice 1; NISTIR 6963 §§10–11 y Tabla 6; EN 14625 anexos E–G, solo si se usan afirmaciones o numerales de esas fuentes.
- Numerales no confirmados se citarán sin numeral y se anotarán pendientes. No atribuir fuerza técnica a prop_e.

### Anexos previstos

- **AX.2:** varianza de combinaciones lineales y propagación con covarianza; remitir sin deducir.
- **AX.3:** varianzas rectangular/triangular (`h/√3`, `h/√6`, `δ/√12`); remitir sin deducir.
- **AX.7:** Welch–Satterthwaite y condiciones; remitir para deducción y advertir su aplicación limitada a componentes independientes en I.
- **AX.13:** fundamento Monte Carlo si se menciona únicamente como alternativa fuera del contenido M8; no impartir el método, que pertenece a M13.

## Ejecución

### Contenido escrito

- `M08_libreto.md`: ficha del capítulo; nivel B con escenas B1–B3 y señales de escalamiento; nivel I con escenas I1–I4; nivel A con escenas A1–A2 y señales de escalamiento; cierre y referencias del capítulo. La secuencia respeta B → I → A.
- Se dejaron únicamente los tres marcadores de práctica de prop_e, uno por nivel: presupuesto sencillo de punto de calibración (B), presupuestos de calibración/promedio/uso de cliente (I) y función de incertidumbre frente a CMC en el intervalo (A). No se escribieron enunciados, ejercicios, soluciones, evidencias ni rúbricas.
- Datos de ejemplo numérico: **simulados**, declarados como tales en el libreto y en `calc/M08_ejemplos.py`. El diseño F-PSMT-01 (12 puntos × 8 lecturas × 6 días) se usa solo como dato contextual **propio**; no se calcularon resultados del laboratorio. Se excluyó presentar fórmulas NIST/BIPM como presupuesto del SRP 55.

### Scripts y resultados

- Script: `curso/S2_modelos_calibracion/calc/M08_ejemplos.py`. Ejecutado con `curso/.venv/bin/python`; terminó sin error. Reproduce todos los resultados numéricos del libreto y el conteo contextual (576 observaciones; `√576=24`).
- Salida relevante tras alinear la etiqueta del script: `s_r/√8=0,0848528`; resolución media `0,0102062`; `u(y)=0,0854644`; valor de uso `x_hat=100,0000`; Kragten `u_c=0,2633766`, `U(k=2)=0,5267531`.
- Sensibilidades analíticas: `c_y=0,998004`, `c_a=−0,998004`, `c_b=−99,800399`; combinación lineal `u_c=0,2636774`; `ν_eff=657,9543`; `k_95=1,963576`; `U=0,5177507`.
- Conversión rectangular: resolución `0,10/√12=0,0288675`; tolerancia `±0,30` con distribución rectangular `u=0,1732051`; `s=0,24`, `s/√8=0,0848528`, g.l. tipo A `7`.
- Resultados simulados de calibración/promedio y futuro: `u=0,3741657` y `0,4846648`; ejemplo de doble conteo `0,4242641` frente a `0,3741657`. Cadena: `u(Level 2)=0,4482187`, `u(cliente)=0,6142475`, `U(k=2)=1,2284950`.
- Covarianza común simulada: `cov=0,0918 (nmol/mol)²`; `u(Δ)=0,3202124` con componente común frente a `0,5349168` bajo independencia. Función `U(x)` / CMC simulada calculada en 0, 80, 250 y 500 nmol/mol; máximos puntuales: 0,800; 1,120; 3,052; 6,026 nmol/mol, respectivamente.

### Referencias verificadas con `pdftotext`

| Clave | Numerales usados en el libreto | Archivo y páginas PDF comprobadas |
|---|---|---|
| GUM | §§3.3.4–3.3.5, 4.1–4.3, 5.1–5.2, 6.2–6.3; Anexo G.3–G.4 | `docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf`; PDF pp. 12–25 (clasificación y §§4.1–4.3), 26–32 (§§5.1–5.2 y 6.2–6.3), 80–81 (G.3–G.4). |
| JCGM GUM-6 | §§8.4, 11.2–11.4 y 11.9 | `docs/JCGM_GUM_6_2020.pdf`; PDF pp. 30–32, 47–51 y 58. |
| Crowder 2020 | §§6.2.1–6.2.5, 6.3–6.4; §§7.2–7.7 y 7.4.1 | `docs/intro_stats_metro_c06.pdf`, PDF pp. 1–11; `docs/intro_stats_metro_c07.pdf`, PDF pp. 2–11 (el encabezado exacto 7.4.1 se confirmó además en la extracción integral del capítulo). |
| MMU | §§5.2.1–5.3.1, 6.1–6.2 | `docs/metrology_measure_uncer_c05.pdf`, PDF pp. 1–15; `docs/metrology_measure_uncer_c06.pdf`, PDF pp. 1–7. |

Se verificó además con `pdftotext` la portada y los datos bibliográficos: Crowder, Delker, Forrest y Martin, Springer Nature Switzerland AG, 2020; Novellino do Rosario y Mendes, Springer Nature Switzerland AG, 2025. No se citó numeral de ISO/IEC 17025 ni se usaron cifras del NIST SRP 6008 o BIPM-SRP27 en el libreto; por tanto, no quedan numerales externos pendientes. AX y `prop_e` son referencias internas, no respaldo técnico externo.

### Decisiones y pendientes

- Se mantuvo la aproximación de Kragten como cálculo numérico de primer orden por perturbación finita en B, y se presentó aparte la propagación analítica en I; no se presentan como cifras idénticas.
- En I, Welch–Satterthwaite se limita explícitamente a componentes independientes del modelo docente; las covarianzas se tratan con la ley general y se remite la deducción a AX.2/AX.7. La CMC del ejemplo A es ficticia y se etiqueta como simulada.
- Se dejó AX.13 fuera del desarrollo de contenido: Monte Carlo pertenece a M13. No se presenta el presupuesto del SRP 27 ni el del SRP 6008 como presupuesto del SRP 55.
- No hay pendientes de referencias numéricas verificables en `docs/` ni de resultados del script. La definición de CMC se respalda con la descripción institucional del BIPM-KCDB, sin asignar numeral no comprobado. La guía y prop_e señalan que paquetes y ejercicios se preparan en una fase posterior; aquí solo quedan los marcadores.

## Correcciones (revisión Haiku)

| ID del hallazgo | Decisión | Cambio hecho | Ubicación | Justificación |
|---|---|---|---|---|
| R01 | aplicado | `u_c` lineal actualizado a `0,2637 nmol/mol`. | I1, ejemplo analítico | Coincide con la cifra del texto y del cálculo reproducible (`0,2636774`). |
| R02 | aplicado | Fórmula de Welch–Satterthwaite escrita con $c_i^4u^4(x_i)$ y definición de contribución. | I2, pizarra | El denominador debe elevar al cuadrado las contribuciones de varianza $(c_i^2u^2(x_i))$; así concuerda con el modelo y script. |
| R03 | aplicado | Cita sustituida por GUM-6 F.2, ecuación (47) y nota 3; se distingue la diferencia central de GUM-6 de la perturbación hacia arriba usada aquí. | B3, método numérico | La verificación reportada en la revisión confirma que MMU §6.1 y Crowder §7.2 no documentan Kragten, mientras GUM-6 F.2 sí lo menciona. |
| R04 | aplicado con cambios | CMC definida en la primera aparición mediante la descripción de BIPM-KCDB: capacidad ofrecida a clientes bajo condiciones normales; añadido registro bibliográfico externo sin numeral. | Ficha, introducción del nivel A y referencias | Se conserva la exigencia de definir el término, pero no se atribuye una definición abreviada al VIM: la descripción de CMC se cita a BIPM-KCDB, fuente institucional pertinente, sin inventar numeral. |
| R05 | aplicado | Explicación del diseño propio de 12 × 8 × 6 y de por qué no dividir por $\sqrt{576}$ se trasladó a B3 antes de su práctica; I4 remite a B3. | B3 e I4 | Cumple el alcance B y aclara que concentraciones distintas y lecturas agrupadas por día no son 576 réplicas intercambiables. |
| R06 | aplicado | Notación y denominación unificadas como valor de uso $\hat{x}=(y-a)/b$; retirada de «indicación corregida» para este resultado y etiquetas del script alineadas a `x_hat`. | B1, B3, I1, I2 y `calc/M08_ejemplos.py` | Sigue la convención de prop_e §3 para el uso inverso y evita confundirlo con una indicación; las cifras del script se mantienen. |
| R07 | aplicado | Desviación de lectura y cocientes de la media expresados con $s_r$. | Ficha, B1, B2 y cierre | Sigue la convención: $s_r$ estima repetibilidad dentro del día; no se atribuye `s` a la notación específica de esta fuente. |
| R08 | aplicado | Expresiones algebraicas y numéricas en prosa pasadas a delimitadores LaTeX; identificadores aislados y rutas se mantienen como código. | Todo el capítulo | Ajusta fórmulas narradas a guía §4, con notación LaTeX para raíces, subíndices, signos y unidades. |
| R09 | aplicado | Clave `Intro` normalizada a `Crowder 2020`; GUM G.4 uniformado; retirado `prop_e` de citas técnicas. | Citas del capítulo | La clave bibliográfica coincide con guía §5; `prop_e` respalda alcance, no contenido técnico. |
| R10 | aplicado | Añadidas referencias para los anexos internos AX.2, AX.3 y AX.7, y entrada de BIPM-KCDB para CMC. | Referencias del capítulo | La lista ahora registra cada clave citada y distingue fuentes internas de la referencia externa no disponible en `docs/`. |
| R11 | aplicado | Frase vaga reemplazada por referencia explícita a GUM-6 F.1–F.2 y Crowder 2020 §7.7; retirada la cita inadecuada a GUM-6 11.9. | A2, límites de linealización | Esas ubicaciones tratan linealización y validez de la propagación según la verificación documentada en la revisión. |
| R12 | aplicado | Insertada línea en blanco antes del encabezado de nivel A. | Entre I4 y nivel A | Evita que el encabezado quede unido al bloque de cita del marcador de práctica. |
| R13 | aplicado | El resultado futuro se identifica como $u_c$. | I3 | Mantiene consistencia con la incertidumbre combinada indicada en el ejemplo y en el resto del capítulo. |
| R14 | aplicado con cambios | Frases extensas de B1 se dividieron en unidades orales más cortas y se simplificaron las explicaciones de la desviación y de la cobertura. | B1, B2 e I2 | Mejora la locución manteniendo intactos los datos, supuestos y conclusiones técnicas. |
| R15 | aplicado | Eliminada la mención de AX.13 de la ficha de M08. | Ficha | El anexo corresponde al desarrollo de Monte Carlo de M13, no a contenido de este capítulo. |
| R16 | aplicado | Símbolo de resolución escrito como `\delta` en la fórmula de pizarra; se revisó también la notación de $h$. | B2, pizarra | Evita Unicode dentro de LaTeX y conserva la distinción entre semiamplitud $h$ y ancho total $\delta$. |

Correcciones adicionales por iniciativa propia:

- La explicación de $s_r$ reemplazó el uso genérico de `s` en el cierre y en la pregunta de comprobación, para no reintroducir la notación señalada en R07.
- Se revisaron las citas técnicas restantes para que usen la clave bibliográfica declarada y no presenten `prop_e` como autoridad técnica.
- Se ampliaron las expresiones LaTeX a unidades, derivadas y covarianzas además de los ejemplos señalados; los resultados numéricos se cotejaron contra la ejecución de `calc/M08_ejemplos.py`.
