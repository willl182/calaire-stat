# M12 — Revisión de redacción y errores (Haiku)

Revisión de `M12_libreto.md`. No se ha editado el libreto.

## Plan de revisión

1. **Lectura completa** de `curso/guia_libreto.md` (§§1–8), de `prop_e.md` (§2 niveles, M12 en §5, §§6–8) y de `M12_libreto.md` (239 líneas). Se consultó la bitácora para contrastar el alcance y las páginas declaradas.
2. **Recálculo de cifras.** Ejecuté `curso/S3_comparacion_decision/calc/M12_indicadores.py` con `curso/.venv/bin/python -I` y comparé cada cifra del libreto con la salida: diferencias, `media(|dᵢ|)`, `|media(dᵢ)|`, `s_d`, intervalo bilateral, `L₉₀`, `AB`, `AS`, `L₉₅(AB)`, cambio de escala, `s₀` y `3s₀`, contraste de periodos y componente común. Además recalculé a mano las cifras de A1 y A2 que no estaban en la salida (por ejemplo, `0,6455`, `1,0000`, error estándar de periodos).
3. **Referencias.** `pdftotext` sobre `docs/` para 40 CFR Part 58, Appendix A (§§2.3.1.2, 3.1.1, 4.1.1–4.1.3.2; páginas 4, 7, 18–20). Como las ecuaciones de 40 CFR son imágenes, rendericé las páginas 18 y 19 y comparé visualmente las ecuaciones 1–5. Para EN 14625, `pdftotext` sobre §3.12 (p. 10), Tabla 1 (p. 19), §8.4.5 y fórmula 5 (pp. 25–26). Para GUM, `pdftotext` sobre §§5.2.1–5.2.2 (p. 29 del PDF). Para las fuentes estadísticas de intervalos chi-cuadrado y t, busqué en el índice de Crowder 2020 y en Hahs-Vaughn.
4. **Alcance.** Contraste de la ficha y de cada nivel con prop_e §5 (M12), §2 (señales de escalamiento del básico), §6 (exclusiones) y §8 (errores críticos). Comprobación de los tres marcadores de práctica (B, I y A) y de que no hay enunciados ni soluciones.
5. **Forma.** Viñetas en contenido narrado, etiquetas de acotación (todas permitidas por §1), coma decimal, notación (§4), estructura de capítulo (§2), rótulos de datos (§4 y §6), formato de referencias (§5).
6. **Redacción.** Lectura de cada escena en voz alta, buscando frases ambiguas, concordancia, terminología y frases excesivamente largas.

## Hallazgos

| id | Ubicación (escena y texto citado) | Tipo | Severidad | Problema | Corrección propuesta |
|---|---|---|---|---|---|
| R01 | Ficha del capítulo, fila «Nivel B», expresión «media del valor absoluto de dᵢ» frente a «valor absoluto de la media de dᵢ» | forma (tabla) | mayor | Las barras verticales dentro de la celda se leen como separadores de columna, así que la fila gana columnas y el render queda mal. | Reescribir la celda con LaTeX y `\lvert`: «$\operatorname{media}(\lvert d_i\rvert)$ frente a $\lvert\operatorname{media}(d_i)\rvert$». Revisar que ninguna otra celda tenga `|`. |
| R02 | Todo el capítulo, p. ej. B1 «`meas`… `audit`», B2 «`media` del valor absoluto», I1 «`n−1` grados de libertad», I2 «`AB`», «`L₉₅(AB)`», A1 «`n`», A2 «`C`» | notación (§4) | mayor | §4 pide fórmulas en LaTeX (`$…$` en línea). El libreto usa backticks para variables, expresiones y resultados en prosa (decenas de casos), y mezcla `dᵢ` (Unicode) con `d_i` (LaTeX) en la misma página. | Convertir a `$…$` las variables y expresiones en prosa (`$d_i$`, `$n-1$`, `$\mathrm{AB}$`, `$L_{95}(\mathrm{AB})$`). Mantener backticks solo para nombres de archivo o script. Unificar a LaTeX en todo el capítulo. |
| R03 | Referencias en la narración, p. ej. B1 «[40 CFR 58, Appendix A §4.1.1]»; «Referencias del capítulo»: «**40 CFR 58.**» | referencia (§5) | menor | §5 y la tabla de claves usan `CFR58-A` para 40 CFR Part 58, Appendix A. El libreto usa «40 CFR 58», que no coincide con la clave de la guía. | Usar `[CFR58-A §4.1.1]` en todas las citas y «**CFR58-A.**» como encabezado de la entrada. |
| R04 | Escena I1, pizarra y narración de la distribución chi-cuadrado; Escena I2, «IC bilateral 95 %» con `s_d/√n` y `t₀,₉₇₅;₃` | referencia (§5, «cada fórmula se respalda con una fuente externa») | mayor | Las fórmulas de `χ²` con `n−1` grados de libertad, del intervalo bilateral de Student y de la desviación muestral solo tienen cita de 40 CFR (que fija el cuantil del límite, no la distribución). Falta una fuente estadística para el intervalo bilateral y para el divisor `n−1`. | Citar `[Crowder 2020]` para chi-cuadrado y para el intervalo de la media (el índice de la obra tiene «Chi-square» en las pp. 106, 214, 215 y 286; verificar el capítulo con `pdftotext` antes de dar numeral). Si no se confirma el numeral, citar sin numeral y anotar «pendiente» en la bitácora. Añadir `[AX.1]` para `s_d` y `AS`. |
| R05 | Señales de escalamiento de B: «Antes de cerrar el nivel B, repasemos cuándo detener la plantilla…» | alcance (§2 de prop_e, señales del básico) | mayor | prop_e §2 fija para B: dependencia no contemplada, cambio de escala, atípico sin causa, residuos con estructura, incertidumbre relevante en ambos ejes, pocos grados de libertad y resultado próximo a un límite. Las señales de B cubren referencia, denominador, cancelación y criterio ajeno; faltan «pocos grados de libertad» (el ejemplo de B usa `n=4`, y I usa 3 grados de libertad), «resultado próximo a un límite» (el 4,14 % se compara con el 7 %) y «cambio de escala» y «dependencia no contemplada», que el libreto solo introduce en I y A. | Añadir a las señales de B, en prosa: «Si tienen pocas verificaciones, como las cuatro de este ejemplo, no presenten un límite como estable; si el resultado queda cerca del criterio, detengan y consulten; si el monitor cambió de escala o de ganancia, no compare antes con después sin declararlo; si las verificaciones vienen agrupadas en el tiempo, no las traten como independientes.» Mantener la nota de que estas señales complementan el contenido. |
| R06 | Escena I1, narración: «la expresión utiliza la desviación estándar muestral de los `dᵢ` y la raíz de `(n−1)` dividida por el cuantil del diez por ciento de chi-cuadrado» | redacción / exactitud | menor | La frase describe mal la fórmula `L₉₀ = s_d·√((n−1)/χ²)`: la raíz no divide al cuantil en el sentido literal; la raíz afecta al cociente. | «…la desviación estándar muestral de los `dᵢ` multiplicada por la raíz del cociente entre `n−1` y el cuantil del diez por ciento de chi-cuadrado.» |
| R07 | Escena I1 (sin remisión a anexo), frase «Partamos de la medida de dispersión de M4» | referencia / anexos (§3 de la guía) | menor | §3 exige una remisión a anexo cuando una deducción se usa. En I1 aparecen la fórmula de `L₉₀` y el divisor `n−1` sin remisión a AX.11 (límites de confianza) ni a AX.1 (divisor `n−1`). La remisión a AX.11 solo aparece en la nota de I2. | Añadir a I1, tras la pizarra: «La deducción de esta expresión está en el Anexo AX.11; aquí la usamos.» y, al decir `n−1`, «la razón del divisor `n−1` está en el Anexo AX.1». |
| R08 | Escena I2, EJEMPLO: «IC bilateral 95 % para μ_d = […]»; Escena I4, EJEMPLO: «respuestas al cero `[-0,2; −0,1; 0; +0,1; +0,2]`» | notación (§4) | menor | `μ_d` aparece sin LaTeX y el ejemplo usa un guion ASCII (`-`) junto a signos menos Unicode (`−`), lo que no se lee igual en voz alta ni en pantalla. | Escribir `$\mu_d$` y usar siempre el signo menos Unicode `−` en todos los vectores de ejemplo. |
| R09 | Escena B2, párrafo que empieza «La estadística publicada para verificaciones de un punto…»; Escena A1, párrafo «En la propagación de la incertidumbre…»; Escena B-final «En este nivel no decidimos…», frase «La primera resume resultados…» | redacción (§1: frases cortas, ritmo oral) | menor | Hay párrafos de 6–8 frases con subordinadas largas; en «La primera resume…» el antecedente de «la primera» no es inmediato (el lector debe volver al inicio del párrafo). | Dividir cada párrafo en frases de una idea. Ejemplo: «El indicador agregado describe verificaciones bajo una población, un diseño y un periodo definidos. El certificado describe un resultado individual de calibración bajo su propio modelo. Una no sustituye a la otra.» |
| R10 | Transición final de B: «En I añadiremos incertidumbre a los indicadores» | terminología (§1, consistencia) | mayor | La ficha, el cierre y la introducción de I usan «límites de confianza», y el propio capítulo separa «indicador» de «incertidumbre de calibración» (B, A y cierre). «Añadiremos incertidumbre a los indicadores» contradice esa separación y prepara una confusión que el capítulo intenta evitar. | «En I añadiremos límites de confianza a los indicadores: veremos qué límite se calcula, si es unilateral o bilateral y bajo qué hipótesis se interpreta.» |

## Verificaciones hechas

**Cálculos** (`calc/M12_indicadores.py`, `curso/.venv/bin/python -I`):

| Cifra del libreto | Valor en el libreto | Salida del script | Resultado |
|---|---|---|---|
| `media(\|dᵢ\|)` y `\|media(dᵢ)\|` (B2) | 1,50 % y 0,00 % | 1,500000 % y 0,000000 % | Coincide |
| `s_d` (I1) | 1,8257 % | 1,825742 % | Coincide |
| `χ²₀,₁₀;₃` (I1) | 0,5844 | 0,584374 | Coincide |
| `L₉₀(s_d)` (I1) | 4,1367 % (aprox. 4,14 %) | 4,136704 % | Coincide |
| `AB`, `AS`, `t₀,₉₅;₃`, `L₉₅(AB)` (I2) | 1,5000 %; 0,5774 %; 2,3534; 2,1794 % | 1,500000 %; 0,577350 %; 2,353363; 2,179358 % | Coincide |
| `SE` de la media e IC bilateral (I2) | 0,9129 % (texto: «cero coma nueve uno tres»); [−2,9052 %; +2,9052 %] | 0,912871 %; [−2,905163 %; +2,905163 %] | Coincide |
| Cambio de escala `d` (I3) | +1,00 % → +2,01 % | 1,000000 % → 2,010000 % | Coincide |
| `s₀` y `3s₀` (I4) | 0,1581 y 0,4743 nmol/mol | 0,158114 y 0,474342 nmol/mol | Coincide |
| Error estándar iid y de dos periodos (A1) | 0,6455 % y 1,0000 % | 0,645497 % y 1,000000 % | Coincide |
| Componente común (A2) | +0,80 % con dos y con ocho copias | 0,800000 % en ambos casos | Coincide |
| Ejemplos sin script (B2, cero en el denominador) | `0,50−0,20 = 0,30 nmol/mol`; `0,30/0,20 = 150 %` | Aritmética manual | Coincide |
| Fórmula de A1 `Var(d̄)` | `(1/n²)[ΣVar + 2ΣCov]` | Comprobación algebraica | Correcta |
| Ejemplo B1 (`d₁ = (98−100)/100 × 100 %`) | −2 % | Aritmética manual | Coincide |

Ninguna cifra del libreto está fuera del script, y todas las del script que el libreto usa están reproducidas. No hay errores numéricos ni de signo.

**Referencias en `docs/`** (`pdftotext` y render de páginas):

| Numeral citado en el libreto | Documento y página | Comprobación | Resultado |
|---|---|---|---|
| 40 CFR 58, App. A §2.3.1.2 | PDF p. 4 (texto) | «upper 90 percent confidence limit for the CV of 7 percent», «upper 95 percent … absolute bias of 7 percent» | Verificado |
| 40 CFR 58, App. A §3.1.1 | PDF p. 7 (encabezado de sección visible) | Sección de checks de un punto | Verificado (ubicación) |
| 40 CFR 58, App. A §4.1.1 y Ecuación 1 | PDF p. 18 (texto e imagen) | `dᵢ = (meas − audit)/audit · 100`, con `meas` = indicación del monitor y `audit` = referencia de auditoría | Verificado |
| 40 CFR 58, App. A §4.1.2 y Ecuación 2 | PDF pp. 18–19 (texto e imagen) | `CV = √[(n·Σd² − (Σd)²)/(n(n−1))] · √((n−1)/χ²₀,₁₀;ₙ₋₁)`, con `χ²₀,₁₀` como percentil 10 | Verificado. Equivale a `s_d·√((n−1)/χ²)`, como usa el libreto. |
| 40 CFR 58, App. A §4.1.3, Ecuaciones 3–5 | PDF p. 19 (texto e imagen) | Sesgo absoluto = `AB + t₀,₉₅;ₙ₋₁·AS/√n`; `AB = (1/n)·Σ` de los valores absolutos de `dᵢ`; `AS = √[(nΣ` de los `dᵢ` absolutos `² − (Σ` de los `dᵢ` absolutos`)²)/(n(n−1))]` | Verificado |
| 40 CFR 58, App. A §§4.1.3.1–4.1.3.2 | PDF p. 20 (texto) | Percentiles 25 y 75; signo positivo o negativo solo si ambos tienen el mismo signo | Verificado |
| GUM §§5.2.1–5.2.2 | PDF p. 29 (texto) | 5.2.1: la Ecuación (10) solo vale con entradas independientes; si hay correlación significativa, se deben considerar. 5.2.2: expresión con covarianzas | Verificado |
| EN 14625 §3.12 | PDF p. 10 (texto) | Nota 1: `detection limit = 3,3 × (sz/B)` | Verificado |
| EN 14625 §8.4.5 | PDF pp. 25–26 (texto) | Repetibilidad en cero y en `ct`, con `sr` por la Ecuación (4) y 20 medidas | Verificado |
| EN 14625 fórmula 5 | PDF p. 26 (texto) | `l_det = 3,3 · s_r,z / B` | Verificado |
| EN 14625 Tabla 1 | PDF p. 19 (texto) | `s_rz ≤ 1,0 nmol/mol` (repetibilidad en cero) | Verificado |
| Crowder 2020, «Chi-square» | Índice del PDF (texto) | Entradas en pp. 106, 214, 215 y 286 | Localiza el tema; falta el numeral (R04) |
| Hahs-Vaughn (chi-cuadrado) | Texto del PDF | Solo aparece en el capítulo de proporciones (§8.2–8.4); no es un apoyo para intervalos de varianza | Descartado como cita de este uso |

**Alcance y formato:**

- **Niveles.** B cubre definición de la diferencia, signo, `media(|dᵢ|)` frente a `|media(dᵢ)|`, porcentajes cerca de cero y métrica absoluta (prop_e §5 M12, B). I cubre límites con chi-cuadrado y t, unilateral frente a bilateral, cambio de escala, dispersión del cero y umbral bajo hipótesis, con la advertencia sobre `3·s₀` (I). A cubre dependencia, periodos mezclados y trazabilidad común (A). Ninguno tiene contenido añadido ni faltante respecto de prop_e.
- **Exclusiones (§6).** No aparecen ISO 13528, ensayos de aptitud, PCR, PLS, varianza de Allan, GGMR con `V_xy ≠ 0`, grado de equivalencia ni BIPM.QM-K1. El libreto cita criterios regulatorios de 40 CFR, pero como metas de otro marco y con advertencia expresa; no son «promedios regulatorios» ni valores de diseño (que es lo que excluye §6). No se encontró violación.
- **Marcadores.** Están los tres en su nivel (B: «Indicadores con diferencias de ambos signos»; I: «Indicadores, límites y cambio de escala»; A: «Discrepancia entre conformidad individual y desempeño agregado»). No hay enunciados, datos, soluciones ni rúbricas.
- **Etiquetas de acotación.** Solo se usan `[DIAPOSITIVA]`, `[PIZARRA]`, `[PREGUNTA AL GRUPO]`, `[EJEMPLO]`, `[ERROR CRÍTICO]`, `[NOTA AL INSTRUCTOR]`, `[ESCALAMIENTO]` y `[TRANSICIÓN]`, todas en la lista permitida de §1.
- **Viñetas.** No hay viñetas en la narración. Las únicas viñetas están en «Referencias del capítulo», que es una lista permitida.
- **Coma decimal.** Todas las cifras del libreto usan coma decimal. Las referencias por numeral (`§4.1.2`) usan punto por ser numerales de norma, lo que es correcto.
- **Estructura (§2).** Ficha, tres niveles con escenas, señales de escalamiento de B, cierre y referencias, en ese orden. Los niveles I y A abren diciendo qué se da por visto.
- **Anexos (§7).** AX.2 y AX.11 están bien identificados; AX.1 no se remite (R07).

## Resumen

Revisé la redacción, las cifras, las referencias y el alcance de `M12_libreto.md` frente a `guia_libreto.md` y `prop_e.md`. Todas las cifras coinciden con `calc/M12_indicadores.py` y con mi recálculo manual; los numerales de 40 CFR (§§2.3.1.2, 4.1.1–4.1.3.2), GUM (§§5.2.1–5.2.2) y EN 14625 (§3.12, §8.4.5, fórmula 5, Tabla 1) están confirmados en `docs/`. No hay errores críticos.

Los hallazgos son de forma, cobertura de referencias y alcance, con cinco mayores y cinco menores. Los mayores son: las barras verticales que rompen la tabla de la ficha (R01), la notación con backticks en lugar de LaTeX (R02), la falta de fuente estadística para chi-cuadrado y el intervalo bilateral (R04), las señales de escalamiento de B incompletas frente a prop_e §2 (R05) y el término «incertidumbre» usado para los indicadores en la transición de B (R10). Las correcciones son concretas y no cambian el contenido ni el alcance; el libreto no se ha editado.
