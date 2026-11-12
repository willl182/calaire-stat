# Revisión de cierre de las prácticas B, I y A de M06 — Haiku

Fecha: 2026-10-28. Revisor: Haiku 5.5. Alcance: `curso/S2_modelos_calibracion/M06_libreto.md` (bloques `[PRÁCTICA]` B, I y A, y las frases de narración pendientes), `curso/S2_modelos_calibracion/calc/M06_practicas_luna.py` (ejecutado con `curso/.venv/bin/python -I`, sin error), `curso/logs/M06_practicas_luna.md` y los hallazgos previos de `curso/logs/M06_practicas_revision_haiku.md`. Contrastes adicionales: `docs/F-PSMT-01 …xlsm` (hoja `BD_DIAS`), `calc/M06_ejemplos.py` y `calc/M06_RR_CALAIRE.py` (ejecutados). No se han editado libretos, scripts ni bitácora. No se ha auditado ni modificado ninguna referencia o cita. No hay commits.

## Resumen

Las cifras de las tres prácticas coinciden con la ejecución. Los datos de la práctica I se corresponden celda a celda con el archivo (48 valores, signo invertido en la columna «Diferencia», `e = y − x`). Sin embargo, quedan dos problemas de contenido que hay que resolver antes de cerrar M06: la etiqueta «nivel nominal de 90 nmol/mol» no coincide con el archivo (que indica 94), y la bitácora dice haber retirado una afirmación de validación que sigue escrita. Las tres frases de narración pendientes siguen sin corregir.

## Estado de los hallazgos previos (`M06_practicas_revision_haiku.md`)

| Hallazgo previo | Estado en esta revisión |
|---|---|
| H-01 (I sin nivel del Level 2) | Resuelto en la práctica: datos propios de `BD_DIAS` F/L/R/X/AD/AJ, filas 31–38; inversión de signo verificada. **Queda abierta la etiqueta de nivel** (H-01 de este informe). |
| H-02 (A sin multiplicidad ni R&R condicional) | Resuelto: tres contrastes con Bonferroni `F(1,6)=10,807`; R&R condicionado a confirmación. Cifra `Fcrit(2,6)` retirada correctamente. |
| H-03 (incertidumbre de componentes en I) | Resuelto: IC chi-cuadrado de σ² y errores estándar de τ̂² y s_entre en la práctica y en la solución; cifras verificadas. |
| H-04 (cita NIST en lugar de Hahs-Vaughn) | **No resuelto y mal descrito en la bitácora** (H-06 de este informe). |
| H-05 (trazabilidad de la matriz de A) | Resuelto en la práctica (pares listados y matriz en el script). Queda una referencia residual a «la tabla simulada de I3» (H-05 de este informe). |
| H-06 (REML en el script de prácticas) | Resuelto en el script (comentario). **Pendiente en la narración, línea 237** (H-03 de este informe). |
| H-07 (redacción de líneas 152 y 219) | **Pendiente en ambas líneas** (H-03 y H-04 de este informe). |
| H-08 (validación de paleta en la bitácora) | **Parcial**: la afirmación de validación sigue en la bitácora, línea 35 (H-06 de este informe). |

## Verificación numérica

| Cifra del libreto | Ejecución | Estado |
|---|---|---|
| B: `u²=0,0162`; `u=0,1273`; `U=0,2546`; sin s_entre `u=0,0346`, `U=0,0693` nmol/mol | `0.0162`; `0.127279`; `0.254558`; `0.034641`; `0.069282` | OK |
| B: componentes `0,015` y `0,0012`; `s_medias=0,3118` | `0.30²/6=0.015`; `0.24²/48=0.0012`; `√(0,0162·6)=0,31177` | OK |
| I: medias diarias −0,274518 … −0,377500; general −0,337801 | `[-0.274518, -0.415532, -0.399020, -0.378367, -0.181868, -0.377500]`; `-0.337801` | OK |
| I: SS entre/dentro/total 0,330651/2,588622/2,919273; g.l. 5/42 | idem | OK |
| I: MS 0,066130/0,061634; F = 1,072952; F_0,95(5,42) = 2,437693 | idem | OK |
| I: σ̂² = 0,061634; s_r = 0,248262; τ̂² = 0,000562; s_entre = 0,023707 | idem | OK |
| I: IC chi-cuadrado 95 % de σ²: [0,041903; 0,099567] | `[0.041903, 0.099567]` (42 g.l.) | OK |
| I: EE de τ̂² 0,005492; de s_entre por delta 0,115823 | `0.005492`; `0.115823` | OK |
| I: Cochran C = 0,450; crítico 0,628724 | `0.450000`; `0.628724` (= `beta.ppf(1-0.05/4, 2, 6)`, verificado) | OK |
| I: 48 valores de la tabla del enunciado | Comparados fila a fila con `BD_DIAS` filas 31–38, columnas F/L/R/X/AD/AJ, signo invertido | OK |
| A: SS 0,08333/0,56/0,10667/0,12; MS; F 1,5625/5,25/2,6667 | idem | OK |
| A: componentes por momentos 0,00500/0,05667/0,01667/0,02000; raíces 0,0707/0,2380/0,1291/0,1414 | idem | OK |
| A: contrastes −0,40/0,00/0,40; F = 4/0/4; umbral `F_0,98333(1,6)=10,8074` | `-0.4, ~0, 0.4`; `4, 0, 4`; `10.807361` | OK |
| A ejemplo negativo: τ̂² = −0,002533; REML frontera σ̂² = 0,014824; contribuciones 0,03727 (truncado) y 0,03515 (REML) | `M06_practicas_luna.py`: `-0.002533`, `0.014824`; `M06_ejemplos.py`: `0.037268`, `0.035148`, `τ²=0` | OK |
| Narración A1 (no práctica): contraste de Bonferroni `F_0,995(2,30)` ≈ 6,35; cuatro niveles con interacción > 3,32; mayor F analista 1,24 | `M06_RR_CALAIRE.py`: `6.3547`; `[135, 360, 405, 455]`; `1.238163` | OK |

Comprobación de forma: las cifras de la práctica usan coma decimal; no encontré cifras con punto decimal en prosa.

## Hallazgos

### H-01 — La etiqueta «nivel nominal de 90 nmol/mol» no coincide con el archivo (media)

- **Ubicación:** `M06_libreto.md` línea 172 (enunciado de la práctica I). Mismo error en `calc/M06_practicas_luna.py` línea 21 (comentario) y línea 79 (salida impresa: «90 nmol/mol nominal»). En `curso/logs/M06_practicas_luna.md` líneas 10 y 20.
- **Problema:** las filas 31–38 de `BD_DIAS` tienen en la columna AL (rótulo de nivel, la misma para todas las filas del bloque) el valor **94**, y las lecturas del SRP (columna C) están alrededor de 94,4. No he encontrado en el libro ningún «90». Los datos son correctos; la etiqueta de nivel no lo es, y un lector que compare con el certificado encontrará 94.
- **Corrección propuesta:** cambiar «90» por «94» en el libreto, el comentario y la salida del script, y en la bitácora, citando la columna AL de `BD_DIAS` como fuente del nivel. Si el instructor tiene el nominal 90 de otro documento, cítese ese documento y explíquese la diferencia entre nominal y nivel de la hoja. No cambiar cifras: solo la etiqueta.

### H-02 — La bitácora dice haber retirado la validación de la paleta, pero la conserva (baja)

- **Ubicación:** `curso/logs/M06_practicas_luna.md` línea 35 (sección «Comprobaciones») frente a la línea 52 (H-08).
- **Problema:** la línea 52 afirma «Se retiró la afirmación de validación previa», pero la línea 35 sigue diciendo que la paleta «pasa el validador en ambos modos» y que el gráfico «se renderizó con Chromium para inspección visual». Ninguna de las dos afirmaciones se reejecutó en esta ronda. La bitácora se contradice.
- **Corrección propuesta:** en la línea 35 eliminar «pasa el validador en ambos modos» y «se renderizó…», o sustituirlos por «la validación de paleta no se reejecutó en la ronda de correcciones». Mantener la mención de que el gráfico existe (`M06_practica_I_residuos.html`, generado por `calc/M06_practica_I_grafico.py`). Verificado: el HTML contiene `#2a78d6` y `#3987e5`, pero eso no prueba el validador.

### H-03 — Línea 237: la optimización REML se atribuye a «el script» sin nombrarlo (baja)

- **Ubicación:** `M06_libreto.md` línea 237 («El script contrasta la solución de frontera con la optimización de la verosimilitud restringida»).
- **Problema:** en el párrafo anterior (línea 233) el único script citado es `calc/M06_ejemplos.py`, pero «el script» de la línea 237 se lee también como `M06_practicas_luna.py`, que no optimiza nada. Sí es correcto el contenido: `M06_ejemplos.py` líneas 109–118 optimizan la verosimilitud restringida y dan σ̂² = 0,014824 y τ̂² = 0. La frase es ambigua, no falsa.
- **Corrección propuesta:** sustituir por «El script `calc/M06_ejemplos.py` contrasta la solución de frontera con la optimización de la verosimilitud restringida». Es la misma corrección de H-06 de la revisión previa, pendiente aún en narración.

### H-04 — Línea 219: «medio falso positivo» es una frase poco clara (baja)

- **Ubicación:** `M06_libreto.md` línea 219 («esperaríamos en promedio medio falso positivo»).
- **Problema:** la cifra es correcta (10 pruebas × 0,05 = 0,5 falsos positivos esperados bajo H₀ global, como imprime el script), pero la frase se lee mal en voz alta. El script ya lo calcula (`esperados falsos positivos bajo H0 global=0.50`), así que la narración debe decir el número.
- **Corrección propuesta:** «esperaríamos, en promedio, medio falso positivo: diez pruebas por cinco centésimas». El resto de la frase («este cálculo no requiere independencia entre niveles, pero sí contrastes individuales válidos») es correcto y se mantiene.

### H-05 — Línea 152: «las cuatro colas son disjuntas» no define las colas y omite la razón del valor crítico (baja)

- **Ubicación:** `M06_libreto.md` línea 152.
- **Problema:** «las cuatro colas» no está definido en el texto. La razón es que, con C > 0,5, solo puede superar el umbral un grupo a la vez; por eso los cuatro sucesos «el grupo i supera el umbral» son disjuntos. Esa disjunción es la que hace exacto el valor crítico `beta.ppf(1 − α/4; 2, 6)` que usa el script (0,628724). La frase actual no lo dice, y el lector no ve por qué el umbral se calcula con α/4. La conclusión matemática es correcta.
- **Corrección propuesta:** sustituir la última frase del párrafo por: «Por encima de 0,5 solo puede superar el umbral un grupo a la vez, así que los cuatro sucesos «el grupo i supera el umbral» son disjuntos. Por eso la probabilidad de que alguno lo supere es cuatro veces la de un grupo, y el cuantil beta de α/4 da el valor crítico exacto.» Mantener la cita ISO 5725-2 tal como está.

### H-06 — La referencia a «la tabla simulada de I3» en A1 no tiene datos en el libreto (baja)

- **Ubicación:** `M06_libreto.md` línea 201 («Se obtuvieron restando 0,4 a la tabla simulada de I3»). Escena I3, línea 134–136, solo da las sumas de cuadrados.
- **Problema:** la práctica A ya incluye los seis pares y declara la regla (cumple H-05 previo). Pero A1 sigue remitiendo a una tabla de I3 que el libreto no muestra. Quien lea solo el libreto no puede comprobar la traslación. Verificado: `calc/M06_practicas_luna.py` línea 48 reconstruye los mismos pares desde la matriz cruda, así que el cálculo es correcto.
- **Corrección propuesta:** en A1, sustituir «la tabla simulada de I3» por «la matriz fijada en el enunciado de la práctica A» o publicar la matriz cruda en I3.

### H-07 — El marcador `[PRÁCTICA]` no está en la lista de etiquetas de la guía, y la guía dice que la fase es solo de contenido (media, decisión del usuario)

- **Ubicación:** `M06_libreto.md` líneas 62, 170 y 255 (`> **[PRÁCTICA]**`). `curso/guia_libreto.md` §1: etiquetas permitidas; la única forma de práctica admitida es `[PRÁCTICA — fase de ejercicios]` y solo como marcador; el bloque de «Fase actual: solo contenido».
- **Problema:** los tres bloques ya tienen enunciado, datos, solución y criterio, lo que la guía reserva para la fase de ejercicios. La bitácora (línea 3) dice que la petición del usuario autoriza esta fase, pero la guía no se ha actualizado. Esto no es un error numérico, sino una incoherencia entre libreto y guía que el usuario debe decidir.
- **Corrección propuesta:** o bien actualizar `guia_libreto.md` §1 para admitir `[PRÁCTICA]` con contenido desarrollado (y fijar la nueva fase), o bien renombrar los tres bloques a la forma permitida. No edito la guía en esta revisión.

### H-08 — Referencia NIST en la línea 219 y bitácora H-04: el registro no coincide con HEAD (media, no resuelto; decisión de referencias)

- **Ubicación:** `M06_libreto.md` línea 219 (cita `NIST/SEMATECH, «Bonferroni’s method», §7.4.7.3, …(consultado 2026-10-27)`); `curso/logs/M06_practicas_luna.md` línea 48.
- **Problema:** la bitácora dice que la cita original era `[Hahs-Vaughn §8.2.1]` y que el cambio NIST estaba solo en el árbol de trabajo. Verificado con `git`: la versión de HEAD ya contiene la cita NIST en la línea 219, y `git diff HEAD` sobre el libreto está vacío. Es decir, el cambio ya está confirmado en HEAD y la bitácora está desfasada. El numeral §7.4.7.3 y la URL no están en `docs/`, y la entrada de la sección «Referencias del capítulo» no lista NIST. Esta revisión no audita referencias y no las toca.
- **Corrección propuesta:** decisión del usuario y del supervisor de referencias: restaurar `[Hahs-Vaughn §8.2.1]` o validar NIST y añadirlo a «Referencias del capítulo». En la bitácora, actualizar la línea 48 para reflejar que el cambio está en HEAD.

## Conclusión

Hallazgos abiertos: 8 (0 altos, 3 medios, 5 bajos). Antes de dar por cerrado M06 conviene resolver, por orden:

1. **H-01** (etiqueta de nivel: 90 frente a 94 del archivo).
2. **H-08** (cita NIST, decisión de referencias; el registro de la bitácora está desfasado).
3. **H-07** (etiqueta `[PRÁCTICA]` frente a la guía; decisión del usuario).
4. **H-02** (bitácora con afirmación de validación contradictoria).
5. **H-03, H-04, H-05, H-06** (redacción de líneas 237, 219, 152 y 201).

Las cifras de B, I y A y la reproducibilidad con `M06_practicas_luna.py` quedan verificadas sin hallazgos.
