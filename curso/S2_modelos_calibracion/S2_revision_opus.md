# S2. Revisión de la sección entregada (Opus 5.5, paso 5)

Revisor: Claude Opus 5.5. Fecha: 27 de octubre de 2026. Fase: **solo contenido**. No se editó ningún libreto ni script; este archivo es la única salida.

## Plan de revisión

1. Leer `curso/00_plan_maestro.md`, `curso/guia_libreto.md`, `prop_e.md` (§§1–10, en especial §5 M5–M8 y §6), `S2_00_indice.md`, `S2_revision_sol.md` y los cuatro libretos completos (M05–M08). Consultar bitácoras, `AX_libreto.md` y la apertura de M09 cuando haga falta.
2. Fidelidad a prop_e: cotejar cada contenido separado por punto y coma en B/I/A con una escena narrada; comprobar exclusiones de §6 (búsqueda textual de ISO 13528, z, ζ, Mandel, PCR/PLS, Allan, KCRV, KCDB, QM-K1, `V_xy ≠ 0`); comprobar que nada queda como mención y que hay un marcador de práctica por nivel.
3. Corrección técnica: ejecutar los cinco scripts docentes con `curso/.venv/bin/python -I` y recalcular de forma **independiente** (código propio, no los scripts) una muestra amplia: potencia t no central, u(ē), ANOVA de un factor y cruzado, IC chi-cuadrado, u(τ̂²), REML de frontera, Cochran, OLS/inversión/bandas/Welch–Satterthwaite de M07, colas chi-cuadrado y F, presupuesto, ν_eff y CMC de M08, y dos niveles del R&R con statsmodels sobre el xlsx.
4. Referencias: `pdftotext -layout` sobre los PDF de `docs/` y comprobar al menos 10 numerales repartidos entre capítulos (se comprobaron 30, abajo).
5. Libreto oral: claridad, ritmo, acotaciones, lectura en voz alta de fórmulas, datos visibles para el instructor.
6. Coherencia interna y con el curso: notación prop_e §3, prerrequisitos, promesas entre capítulos (M06→M08, M07→M08), remisiones AX, transición a M09.
7. Auditorías: leer los LEEME y diffs de las cinco carpetas `auditoria_*`, cruzar los 94 identificadores de `calc/inventario_bloques_sol.json` más los 2 de R6 con `S2_revision_sol.md`, reejecutar `calc/continuidad_auditorias_sol.py` y comparar el último `estado_al_corte/` con los libretos entregados.

## Hallazgos

No hay hallazgos críticos. Los tres mayores son de coherencia de la sección (M06→M08), de interpretación (CMC) y de atribución de una referencia de nivel B.

| Id | Capítulo | Ubicación (texto citado) | Severidad | Problema | Evidencia | Corrección propuesta |
|---|---|---|---|---|---|---|
| O-01 | M08 (con M06) | M08 I3, l. 167: «Para una media de cuatro lecturas independientes, solo la repetibilidad baja a $0{,}40/\sqrt{4}=0{,}20$»; M06 B2, l. 44: «deja el presupuesto completo para M8» | mayor | M06-B promete que el presupuesto completo del promedio se construye en M8 (prop_e M6-B: «Las demás contribuciones del presupuesto se incorporan en M8»; práctica: «el presupuesto completo del promedio se construye en M8»). M08 nunca incorpora $u^2_{\mathrm{prec}}(\bar e)=s^2_{\mathrm{entre}}/d+s^2_r/(dn)$: el «promedio de calibración» de I3 solo reduce la repetibilidad por $\sqrt n$ y no tiene componente entre días. Queda rota la cadena M06→M08 del caso A (prop_e §7: «promedio frente a uso futuro»), y la advertencia de √576 de M08-B3 no se cierra con el cálculo correcto. | `grep` de `s_entre`, `u_prec` y `M06` en M08: solo aparece «M6» en la ficha de prerrequisitos. | En M08-I3, construir el presupuesto del promedio de calibración de 6 días × 8 lecturas tomando de M06-B $u_{\mathrm{prec}}(\bar e)=0{,}1273$ nmol/mol ($s_{\mathrm{entre}}=0{,}30$, $s_r=0{,}24$) y sumarlo a las componentes de referencia y corrección. Contrastarlo con el valor erróneo $s_r/\sqrt{48}=0{,}0346$ y con el divisor √576. Remitir a M06-B y a AX.4, y actualizar `calc/M08_ejemplos.py`. |
| O-02 | M08 | A2, l. 227: «El máximo puntual es una construcción del ejemplo, no una regla de decisión de la GUM ni la aprobación de una CMC»; l. 229: «se toma el máximo» | mayor | Se calcula $\max(U,\mathrm{CMC})$ y el cruce en 81,35 nmol/mol, pero no se dice qué significa ni qué acción sigue. No se explica por qué se toma el máximo (la incertidumbre declarada a un cliente no puede ser menor que la CMC), ni que por encima de 81,35 nmol/mol la función propuesta queda por debajo del presupuesto y, por tanto, no está respaldada. Así no se cumple prop_e §3 («Al cerrar, se entrega el resultado con unidades, interpretación estadística y acción») en el tema central de M8-A («relación con la CMC», «máximo puntual entre U y CMC»). | Lectura de l. 221–246. El script solo imprime «CMC dominates below, U above». | Añadir un párrafo narrado y una [PREGUNTA AL GRUPO]. Por debajo de 81,35 nmol/mol se declara la CMC porque la incertidumbre informada no puede ser menor que ella. Por encima, $U(x)>\mathrm{CMC}$: la CMC propuesta subestima la incertidumbre alcanzable con ese presupuesto, así que hay que revisar la función de CMC o el presupuesto. Citar CIPM MRA-G-13 sin numeral (no disponible en docs/). Si se usa ILAC-P14 para la regla de declaración, marcarlo «no disponible en docs/» y sin numeral. |
| O-03 | M07 | B1, l. 41: «R² puede aumentar simplemente porque se amplía el intervalo de `x` … Por eso R² acompaña al diagnóstico; no lo sustituye [Crowder 2020 §10.4, PDF pp. 9–10]» | mayor | La referencia está mal atribuida. Crowder §10.4 («How Good Is the Model?»: residuos, prueba de pendiente) no trata R² ni su dependencia del intervalo; el capítulo 10 no contiene «R2» ni «coefficient of determination». «Límites de R²» es un contenido explícito de M7-B y se queda sin respaldo externo válido. | `pdftotext intro_stats_metro_c10.pdf`: §10.4 (l. 349–380) sin mención de R²; `grep R2` solo da código R. Fuentes válidas en docs/: Otto §6.1, ec. (6.17), $R^2$; Hahs-Vaughn §10.1.1.5.2 «Restriction of Range». | Cambiar la cita: [Otto §6.1, ec. (6.17)] para la definición de R², [Hahs-Vaughn §10.1.1.5.2] para el efecto del intervalo y [Crowder 2020 §10.4.1] solo para los residuos. |
| O-04 | M08 | I4, l. 183: «tres componentes independientes, todas expresadas como incertidumbres estándar equivalentes en el resultado final» | menor | La «propagación por la cadena SRP 55 → Level 2 → cliente» (M8-I) se reduce a sumar en cuadratura tres cifras ya llevadas al resultado final. No se ve cómo la salida de un eslabón entra como entrada del siguiente: ni sensibilidades ni transferencia de la función de calibración del Level 2 (a, b, cov) al valor que recibe el cliente. | l. 181–189. | Añadir un paso explícito: $\hat x_{\mathrm{cliente}}=(y-a)/b$ con a y b del Level 2. La sensibilidad de la incertidumbre del SRP 55 en el resultado del cliente se obtiene con la ley de M08-I1 (p. ej., $c=1/b$), conservando cov(a,b) de M07-I. Mostrar el número. |
| O-05 | M08 | I3, l. 171: «Supongamos que el residuo de una regresión ya representa la dispersión… si añadimos de nuevo una componente de `0,20 nmol/mol` ya incluida, obtenemos `0,4243`» | menor | prop_e pide el doble conteo «entre residual de regresión y precisión», pero el ejemplo numérico sale de un modelo aditivo sin regresión: el 0,20 es la repetibilidad de la media. La narración habla de residuo y el número no lo representa. | l. 167–171 frente a M07 I1, l. 115 (allí sí hay un caso de $s_{\mathrm{res}}$ frente a $u(y)$). | Basar el ejemplo en M07-I: $u(y)$ de la lectura futura ya contiene la dispersión que estima $s_{\mathrm{res}}=0{,}3946$, y añadir otra vez $s_r$ como renglón separado es doble conteo. Dar ambas cifras. |
| O-06 | M08 | I2, l. 143–159 | menor | prop_e M8-I pide «la adecuación y las limitaciones de Student y Welch–Satterthwaite». Se explican las de WS (correlación), pero no las de Student/t: la t supone una salida aproximadamente normal y falla, por ejemplo, si domina una componente rectangular de límites exactos. | GUM G.6.5 (verificado): «if uc(y) is dominated by a component … from a rectangular distribution … y ± Up could lie outside the bounds». | Añadir dos o tres frases con [GUM G.6.5] y una [PREGUNTA AL GRUPO]. Opcionalmente, un ejemplo numérico con la resolución dominante. |
| O-07 | M07 | I3, l. 141–143: «$w_i=1/u^2(y_i)$ … [Crowder 2020 §10.2.3; ISO 28037 §§6.1–6.2]» | menor | ISO 28037 §6.1.3 define $w_i=1/u(y_i)$ y minimiza $\sum w_i^2(\cdot)^2$. El libreto usa $w_i=1/u^2$ y $\sum w_i(\cdot)^2$ citando la misma norma, sin avisar del cambio de notación. Puede confundir en la práctica A, que verifica contra el ejemplo de ISO/TS 28037. | `ISO_28037` l. 949: «Let wi = 1/u(yi)». | Añadir una [NOTA AL INSTRUCTOR]: ISO 28037 llama peso a $1/u$ y eleva al cuadrado en la suma; las dos formulaciones son equivalentes. |
| O-08 | M07 | B3, l. 71: «No extrapolamos… [Crowder 2020 §10.1.2; ISO 28037 §5.7]»; l. 73: «La corrección aditiva … $\hat x - y$ … [prop_e §3; ISO 28037 §5.7]» | menor | ISO 28037 §5.7 trata la evaluación inversa y directa y, en su nota, que las condiciones de calibración se mantengan en el uso. No trata la extrapolación ni define la corrección aditiva ni su signo. | `ISO_28037` l. 868–888. | Extrapolación: dejar [Crowder 2020 §10.1.2]. Signo: presentarlo como convención del curso (prop_e §3, alcance) junto a la definición de corrección del VIM (no disponible en docs/, sin numeral). Mantener §5.7/§11.1 solo para la inversión. |
| O-09 | M07 | I3, l. 147: «Con los datos fijados para comparar los métodos, OLS da…»; I4, l. 169: «cuatro niveles y tres observaciones…»; A2, l. 219: ejemplo WLS de 12 niveles | menor | El libreto da resultados de tres ejemplos sin mostrar los datos (y de WLS, las 12 observaciones de falta de ajuste, las y de los 12 niveles). El instructor no los puede proyectar ni el grupo seguir el cálculo sin abrir el script. | Lectura de las escenas; los datos solo están en `calc/M07_ejemplos.py`. | Añadir una tabla [MATERIAL] o [DIAPOSITIVA] con los datos de cada ejemplo, como en B1. |
| O-10 | M07 | A1, l. 209: «La componente común aditiva de referencia … aumenta $u(a)$ de $0{,}34152$ a $0{,}36204$» | menor | Ambiguo: en la frase anterior se habla de OLS y WLS, pero las dos cifras son de GGMR (sin y con componente común). Con $u(y)=0{,}40$ y x fijo, el $u(a)$ de WLS sería ≈0,29. | Salida del script: «u(a) con=0.36203815, sin=0.34151683». Recálculo: $0{,}34152^2+(b\cdot0{,}12)^2\approx0{,}3620^2$. | Decir: «en GGMR, $u(a)$ pasa de 0,342 sin componente común a 0,362 con ella». |
| O-11 | M06 | A1, l. 196: «En 405 y 455 nmol/mol destacan medias diarias de 0,73 y 0,83 nmol/mol para el analista 2 en el segundo bloque» | menor | 0,73 y 0,83 no son medias diarias: son medias de bloque (seis días). | Script: `405_block_means_by_analyst … 0.728979`, `455 … 0.827887`, de `data.mean(axis=2)`. | Cambiar a «medias de bloque (seis días)». |
| O-12 | M06 | B1, l. 26: «En la notación del curso, `s_entre` estima `τ` y `s_r` estima `σ` [ISO 5725-3 §8]»; también l. 30 y 32 | menor | El modelo estadístico de ISO 5725-3 está en §6 («Statistical model», §6.1 «Basic model»). §8 trata el estudio dentro del laboratorio. | Índice de `ISO 5725-3_1994.pdf`: §6 Statistical model; §8 Within-laboratory study. | Citar [ISO 5725-3 §6.1] para el modelo y dejar §8 para el estudio intralaboratorio. |
| O-13 | M06 | I2, l. 106: «$u^2(\hat\tau^2)\approx[2MS^2_{\mathrm{entre}}/(d-1)+…]/n^2$ … [Hahs-Vaughn, cap. 9; GUM 5.1.2]» | menor | La base de la fórmula (varianza 2ν de la chi-cuadrado) está en Hahs-Vaughn cap. 8 (§8.2.1), no en el 9. | `hv.txt` l. 16758: «the variance is 2ν», dentro de §8.2.1. | Citar [Hahs-Vaughn §8.2.1; GUM 5.1.2] o Searle et al. (no disponible en docs/). |
| O-14 | M06 | B1, l. 22 y I5, l. 150/152: «[VIM; ISO 5725-1; MMU §4.4]» | menor | En docs/ solo está el corrigendum de ISO 5725-1, y en el texto se cita sin la marca «(no disponible en docs/)» que exige la guía §5. La lista final sí lo aclara. | Lista de referencias de M06; `docs/ISO 5725-1_1994_Cor 1_1998 .pdf`. | Añadir la marca en el texto o sustituir por [ISO 5725-3 §§5–6; MMU §4.4] (verificados). |
| O-15 | M05 | I3, l. 156: «¿cuántas corridas hacen falta para detectar un cambio de pendiente de 0,005?… este ejemplo no calcula esa potencia»; también l. 104, 158 y 162 | menor | La pendiente de 0,005 no está en prop_e (viene de `temario_curso.md`). Se menciona cuatro veces solo para decir que no se calcula: es justo la «mención» que prohíbe prop_e §1.4. | `grep 0,005 prop_e.md` sin resultados; `temario_curso.md:200`. | Quitar las cuatro menciones y conservar el ejemplo de potencia de la media (0,495/0,501/0,873), que sí cubre «relación con potencia». |
| O-16 | M05 | I3, l. 158: «$u^2(\bar e)=s^2_{entre}/d+s^2_r/(dn)$ … [ISO 5725-3; la deducción está en el Anexo AX.4]» | menor | ISO 5725-3 se cita sin numeral para una fórmula que M06 respalda con GUM H.5. | Comparación con M06 B2 y AX.4. | Citar [GUM H.5; AX.4] o el numeral concreto si se localiza. |
| O-17 | S2 (M06, M07) | M07 B1–B3: «`0,99999645`», «`1,0014285714`», «`0,24285714 nmol/mol`»; I4: «$p = 0{,}00003422$»; M06 A1, l. 172–196 | menor | Ritmo oral: se leen cifras de 8 a 10 decimales, y el caso R&R repite las mismas salvedades («condicional», «no confirmado», «no afirmamos») al menos seis veces. Eso dificulta impartirlo sin rehacerlo. | Lectura de las escenas. | En la narración, redondear a 3–4 cifras significativas y dejar las completas en una [NOTA AL INSTRUCTOR] o en el script. En M06-A1, reunir las salvedades en una sola [NOTA AL INSTRUCTOR] al inicio. |
| O-18 | M05, M06 | M05, l. 16: «## Nivel B — Lo que se añade»; M06 B (l. 16–18) sin párrafo inicial de lo que se da por visto | menor | Guía §2: cada nivel indica al inicio qué se da por visto, y B no «añade» sobre otro nivel. Detalle de forma. | Guía §2; M07 y M08 sí abren B con ese párrafo. | Rotular «Nivel B — <subtítulo>» en M05 y añadir en M06-B un párrafo de apertura con los prerrequisitos (M3-B, M4-B, M5-B). |

## Verificaciones

### Cálculos

Scripts ejecutados con `curso/.venv/bin/python -I`: `M05_diseno.py`, `M06_ejemplos.py`, `M06_RR_CALAIRE.py`, `M07_ejemplos.py` y `M08_ejemplos.py`, todos sin error. Cada cifra narrada que se cotejó coincide con su salida. Además se recalcularon de forma independiente, con código propio:

| Capítulo | Cálculo | Libreto | Recálculo | Resultado |
|---|---|---|---|---|
| M05 I3 | u(ē) con s_entre 0,20 y s_r 0,10, para (6,8), (6,16), (12,8) | 0,083; 0,082; 0,059 | 0,0829; 0,0823; 0,0586 | conforme |
| M05 I3 | potencia t no central, Δ = 0,20, (6,8), (6,16), (12,8) | 0,495; 0,501; 0,873 | 0,4951; 0,5009; 0,8733 | conforme |
| M05 A2 | g.l. por estrato 3 × 4 × 2 × 8 | 2, 9, 12, 168 | 2, 9, 12, 168 | conforme |
| M06 B2 | u²_prec; u; U(k=2); s_r/√48; s_medias; s_medias/√6 | 0,0162; 0,1273; 0,2546; 0,0346; 0,3118; 0,1273 | iguales | conforme |
| M06 I1 | SS 0,56/0,18; F 14,0; F crítico(2;9) | 4,26 | 4,2565 | conforme |
| M06 I2 | IC 95 % de σ² (9 g.l.); τ̂²; u(τ̂²); u(s_entre) delta | 0,00946–0,06666; 0,065; 0,0700; 0,1374 | 0,009462–0,066657; 0,065; 0,07004; 0,13736 | conforme |
| M06 I3/A1 | F cruzado 1,5625/5,25/2,667; componentes 0,005/0,0567/0,0167/0,020 | — | iguales | conforme |
| M06 I4 | C = 0,45; crítico de Cochran p = 4, n = 5, 5 % | 0,629 (0,628724) | 0,628724 (aproximación beta); 0,629 en ISO 5725-2, tabla 4 | conforme |
| M06 A1 | F críticos (1;2), (2;30), Bonferroni (2;30; 0,005) | 18,51; 3,32; 6,35 | 18,513; 3,316; 6,355 | conforme |
| M06 A1 | R&R desde xlsx, 135 y 405 nmol/mol, con statsmodels (OLS `C(A)*C(B)`) | F_A 0,662/0,291; F_AB 6,61/6,47 | 0,6620/0,2907; 6,6115/6,4735 | conforme. Mínimo de los datos > 0 en ambos niveles: confirma la advertencia de signo |
| M06 A2 | REML de frontera σ̂² = SS_total/11; u de la media truncada/REML | 0,014824; 0,03727/0,03515 | iguales | conforme |
| M06 A2 | sesgo simulado: u = √(0,2²/8 + 0,05²) | 0,08660 | 0,086603 | conforme |
| M07 B/I | a, b, s_res, u(a), u(b), cov, R², pendiente por el origen | 0,242857; 1,0014286; 0,394606; 0,285595; 0,00094329; −0,00022245; 0,99999645; 1,0020909 | iguales | conforme |
| M07 I1 | semiamplitudes IC/IP en x = 250 | ±0,44728; ±1,18339 | iguales | conforme |
| M07 I1 | x̂, corrección, u(x̂), ν_eff, k, U | 249,90014; −0,59986; 0,25645; 25,83; 2,05618; 0,52730 | iguales | conforme |
| M07 I4 | p de F(2;8) = 48,3 | 0,00003422 | 3,4216·10⁻⁵ | conforme |
| M07 A | χ² 0,95;10; cola inferior de 0,4089 (4 g.l.); cola superior de 83,36 | 18,307; 0,01826; 3,38·10⁻¹⁷ | 18,307; 0,018258; 3,376·10⁻¹⁷ | conforme |
| M08 B | u(y), Kragten, u_c, U(k=2) | 0,0855; 0,2634; 0,527 | 0,08546; 0,26338; 0,5268 | conforme |
| M08 I2 | u_c lineal, ν_eff, U | 0,2637; 658; 0,518 | 0,263677; 657,95; 0,51775 | conforme |
| M08 I3/I4 | 0,5099/0,3742/0,4847/0,4243; cadena 0,4482/0,6142 | — | iguales | conforme |
| M08 A1 | u(Δ) con y sin covarianza | 0,320; 0,535 | 0,32021; 0,53492 | conforme |
| M08 A2 | U(x) en 0/80/250/500; raíz de U² − CMC² | 0,560/1,111/3,052/6,026; 81,35 | iguales; 81,347 | conforme |

### Referencias comprobadas con pdftotext (30 numerales)

| Capítulo | Cita | Documento | Resultado |
|---|---|---|---|
| M05 | ISO 5725-3 §9.5, figura 2; §9.8; anexos B y C | `ISO 5725-3_1994.pdf` | conforme (escalonado de 4 factores con 4 resultados; 2ⁿ⁻¹ en el totalmente anidado; anexo B totalmente anidado, anexo C escalonado) |
| M05 | ISO 5725-3 §§9.3–9.4 | ídem | conforme. Son diseños **interlaboratorio**; el libreto lo declara como adaptación (l. 184) |
| M05/M06 | Crowder 2020 §9.2; §9.3.1, tablas 9.9–9.10; §9.3.2, tablas 9.11–9.12; §9.3.3; §9.3.4 | `intro_stats_metro_c09.pdf` | conforme |
| M05 | Hahs-Vaughn §§6.1.2–6.1.4 | `statistical_concepts_c06.pdf` | conforme (Sample size, Power, Effect size) |
| M05 | SRP QAPP §6.2.1; SRP SOP §9.7.19; EPA TAD §4.4.1; ISO 13964 §6.2.2; EN 14625 §§8.4.7–8.4.8 | PDFs respectivos | conforme (mínimo de 3 ciclos; zero + ≥6 puntos; zero + ≥5 concentraciones; sensibilidad a presión y temperatura) |
| M05 | ISO/IEC 17025 §7.2.2 (robustez) | `BS EN ISO_IEC 17025_2017.pdf` | conforme (7.2.2.1 c y nota: «robustness against external influences») |
| M05 | Brereton cap. 2 (aleatorización) | `chemometrics_c02.pdf` | conforme en §2.2.4.7, p. 38 («randomise the sequence of experiments») |
| M06 | Hahs-Vaughn §9.1 (IC chi-cuadrado de una varianza) | libro completo, §9.1.1.1 | conforme |
| M06 | Hahs-Vaughn §8.2.1 (Bonferroni) | libro completo | conforme, en el contexto de pruebas chi-cuadrado de proporciones |
| M06 | Hahs-Vaughn cap. 9 para u(τ̂²) | — | **no conforme** (O-13) |
| M06 | ISO 5725-2 §7.3.3, §8.1, tabla 4 (0,629) | `ISO 5725-2_1994.pdf` | conforme |
| M06 | ISO 5725-4 §5 y §5.5.2 (sesgo de un laboratorio) | `ISO 5725-4_1994.pdf` | conforme |
| M06 | ISO 5725-3 §8 para el modelo | — | ubicación inexacta: el modelo está en §6 (O-12) |
| M06/M08 | MMU §4.4; §§5.2.2, 5.3.1; §6.1 | `metrology_measure_uncer_c04/05/06.pdf` | conforme |
| M07 | ISO 28037 §10.3, tablas 25–26 (a = 0,3424; b = 1,0012; χ² = 1,772, ν = 5) | `ISO 28037.pdf` | conforme; el script reproduce |
| M07/M08 | ISO 28037 §§11.1.1–11.1.3, notas 1 y 3 | ídem | conforme (fórmula de u²(x); linealización; b = 0) |
| M07 | ISO 28037 §5.8 (OLS), §5.2.2, §6.3 (χ², ν = m − 2) | ídem | conforme |
| M07 | ISO 28037 §5.7 para extrapolación y signo de la corrección | ídem | **no respalda** (O-08) |
| M07 | ISO 6143 §5.2.2 y nota 1 (2u por punto, k = 2) | `ISO 6143 2001.pdf` | conforme |
| M07 | Otto §6.1, tabla 6.1, p. 217; ec. (6.20) | `Chemometrics Statistics and Computer Application.pdf` | conforme |
| M07 | Crowder §§10.1.2, 10.2.1, 10.2.3, 10.3.1–10.3.3, 10.4.1 | `intro_stats_metro_c10.pdf` | conforme |
| M07 | Crowder §10.4 para límites de R² | ídem | **no respalda** (O-03) |
| M08 | GUM 4.3.10 («double-count»); 4.2.3; 3.3.4–3.3.5; 5.1.2; 5.2.2; 6.2.1; 6.3.1; G.3; G.4.1; G.6.5; H.5 | GUM (JCGM 100) | conforme |
| M08 | GUM-6 F.2, ec. (47), nota 3 (Kragten); §8.4; §§11.2–11.4; F.1 | `JCGM_GUM_6_2020.pdf` | conforme |
| M08 | Crowder §§6.2.1–6.2.5; §§7.2–7.4.1; §7.7 | `intro_stats_metro_c06/c07.pdf` | conforme |

No se encontraron referencias inventadas. Las fuentes que no están en docs/ (VIM, Montgomery, Johnson-Kotz-Balakrishnan, Searle et al., CIPM MRA-G-13) se citan sin numeral y con la marca, salvo ISO 5725-1 en el texto de M06 (O-14). Las citas a prop_e en M07 y M08 acompañan siempre a una fuente externa o se limitan al alcance y a las señales de escalamiento.

### Fidelidad, exclusiones y marcadores

Todos los contenidos B/I/A de prop_e §5 M5–M8 tienen escena narrada y ejemplo numérico cuando el tema es cuantitativo. Las excepciones parciales son O-01 (promedio completo en M8), O-02 (relación con la CMC), O-04 (cadena) y O-06 (límites de Student). La búsqueda de exclusiones no encontró nada fuera de alcance: «KCDB» solo aparece en la referencia de M08 para declararla excluida. Hay doce marcadores «[PRÁCTICA — fase de ejercicios]», uno por nivel y capítulo, con títulos alineados a prop_e y sin desarrollo. No falta ninguno. Las remisiones AX.2–AX.8 y AX.11 existen en `S4_numericos_integracion/AX_libreto.md` y su contenido coincide con lo que se les atribuye. Monte Carlo se remite a M13 sin desarrollarse. La transición M08→M09 es coherente con la ficha de M09.

### Auditorías

- Los 94 identificadores de `calc/inventario_bloques_sol.json` (R2: 3; R3: 32; R4: 40; R5: 19) más R6-M07-01 y R6-M08-01 aparecen todos, por nombre o por rango, en `S2_revision_sol.md`, con decisión «conservar» y justificación por hallazgo (S-M05-01/02, S-M06-01/02, S-M07-01/02/03, S-M08-01/02). No falta ninguno y no sobra ninguno.
- `calc/continuidad_auditorias_sol.py` reejecutado: reconstruye exactamente los cuatro diffs y confirma la identidad de los cortes con las instantáneas.
- `diff` entre `auditoria_respaldo_20261026_201411/estado_al_corte/` y los libretos entregados: solo cambian los cuatro títulos de marcador registrados en S-M05-03, S-M06-03 y S-M08-03. No hay ediciones sin registrar.
- Contenido de los bloques conservados: comprobado por muestreo (R2-M07: eliminación del doble conteo de s_res y U inversa 0,5273; R3/R4-M05: sustitución de BIPM.QM-K1; R4-M06: caso R&R condicional; R4-M07: WS por bloques; R3-M08: 7 g.l. de s_r; R6-M07-01: z_x, z_y por Cholesky; R6-M08-01: a y b independientes). Son correctos según los recálculos anteriores. Los defectos de O-03, O-08 y O-12 ya estaban en el texto previo a las auditorías: no los introdujo ningún bloque, pero tampoco se detectaron al decidir.
- Scripts `calc/` (≈150 líneas cambiadas respecto de `437e8bf`, listadas en `auditoria_interrupcion_sol_2/archivos_nuevos_o_modificados.txt`): decididos en conjunto en S-T08 («conservar») y S-T02 (`ajustes_sol.py` deshabilitado). Su salida coincide con el libreto. La decisión en bloque es suficiente porque la salida se verificó.

## Veredicto

| Capítulo | Veredicto | Motivo principal |
|---|---|---|
| M05. Diseño de experimentos | **aprobada con correcciones** | Solo menores (O-15, O-16, O-18). Técnica y referencias sólidas. |
| M06. ANOVA y componentes de varianza | **aprobada con correcciones** | Solo menores de ubicación de cita y redacción (O-11 a O-14, O-17, O-18). El caso R&R está bien acotado. |
| M07. Regresión y calibración inversa | **aprobada con correcciones** | Un mayor de referencia en contenido de B (O-03) y menores (O-07 a O-10, O-17). |
| M08. Propagación de incertidumbre | **aprobada con correcciones** | Dos mayores: presupuesto del promedio sin la componente de M06 (O-01) y CMC sin interpretación (O-02); menores O-04 a O-06. |
| **Sección S2 (global)** | **aprobada con correcciones** | Cálculos correctos y reproducibles, exclusiones respetadas, marcadores completos y auditorías registradas sin pendientes. Para cerrar faltan O-01, O-02 y O-03 y las menores. |

Recuento: **0 críticas, 3 mayores, 15 menores (18 hallazgos).**
