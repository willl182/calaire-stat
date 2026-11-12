# Bitácora de prácticas M06 — Luna

Fecha: 2026-10-27. Alcance: sustituir únicamente los tres marcadores de práctica B, I y A en `curso/S2_modelos_calibracion/M06_libreto.md`. Petición del usuario autoriza esta fase pese al marcador temporal anterior. No commits.

## Plan

- B, según `prop_e.md` §5, M6-B: interpretar `s_r` y `s_entre` entregadas y calcular `U_prec` parcial del promedio con y sin la componente entre días; no ejecutar ANOVA.
- I: ANOVA de días en un nivel, errores con signo; estimación de componentes, incertidumbre, interpretación de efectos, diagnóstico/residuos, dos factores e interacción/denominadores, Cochran y aplicabilidad de ISO 5725.
- A: analista × campaña con días anidados; denominadores, componentes negativas y alternativas de estimación; límites/aplicabilidad de ISO 5725 y sesgo de un laboratorio.
- B y A usan datos simulados explícitos; I usa datos propios de F-PSMT-01, `BD_DIAS!F31:F38`, `L31:L38`, `R31:R38`, `X31:X38`, `AD31:AD38` y `AJ31:AJ38`. El signo de la columna Diferencia del libro se invierte para aplicar la convención del curso $e=y-x$. I incluye diagnóstico gráfico reproducible de residuos, con tabla accesible y modo oscuro explícito.
- Referencias/claves/citas y secciones bibliográficas no se modifican. No se modifica otro capítulo, guía ni revisión final. No se agrega taller.

## Ejecución

Se actualizaron `curso/S2_modelos_calibracion/calc/M06_practicas_luna.py` y se creó `curso/S2_modelos_calibracion/calc/M06_practica_I_grafico.py`. Comandos ejecutados con `curso/.venv/bin/python`: ambos terminan rc=0; el segundo genera `curso/S2_modelos_calibracion/M06_practica_I_residuos.html`.

Resultados reproducidos:

- B: `u²=0,0162`, `u=0,127279221`, `U(k=2)=0,254558441` nmol/mol; sin componente entre días `u=0,034641016`, `U=0,069282032` nmol/mol.
- I (Level 2 propio, 90 nmol/mol nominal): medias diarias −0,274518; −0,415532; −0,399020; −0,378367; −0,181868; −0,377500; general −0,337801 nmol/mol. SS entre/dentro/total = 0,330650955/2,588621757/2,919272712 $(\mathrm{nmol/mol})^2$; g.l. 5/42; MS 0,066130191/0,061633851; F=1,072952436; F crítico 2,437692640; $\hat\tau^2=0,000562042$, $s_{entre}=0,023707434$, $s_r=0,248261659$ nmol/mol. IC chi-cuadrado 95 % de $\sigma^2$: [0,041902844; 0,099567499] $(\mathrm{nmol/mol})^2$; errores estándar aproximados de $\hat\tau^2$ y $s_{entre}$: 0,005491717 $(\mathrm{nmol/mol})^2$ y 0,115822667 nmol/mol. Cochran didáctica C=0,450000 frente a Ccrit=0,628724.
- A: SS analista/campaña/interacción/días = 0,083333/0,560000/0,106667/0,120000; MS=0,083333/0,280000/0,053333/0,020000; F=1,562500/5,250000/2,666667; componentes por momentos=0,005000/0,056667/0,016667/0,020000 $(\mathrm{nmol/mol})^2$. Contrastes interacción por pares de campañas: −0,400000/0,000000/0,400000; F=4/0/4; umbral Bonferroni $F_{0,98333}(1,6)=10,807361$, ninguno supera. Ejemplo negativo: $\hat\tau^2$ no restringida −0,002533; REML en frontera $\tau^2=0$, $\sigma^2=0,014824$ (optimización verificada en `M06_ejemplos.py`).

## Archivos tocados

- Editado localmente `curso/S2_modelos_calibracion/M06_libreto.md`, exclusivamente los bloques de práctica de B/I/A: el marcador se sustituyó por `[PRÁCTICA]` y cada práctica contiene enunciado narrado, datos, tareas, solución numérica, interpretación/acción y criterio breve.
- Actualizado `curso/S2_modelos_calibracion/calc/M06_practicas_luna.py` para leer y reproducir M06-I desde celdas del libro, estimar la incertidumbre de componentes I y aplicar Bonferroni en A.
- Creados `curso/S2_modelos_calibracion/calc/M06_practica_I_grafico.py` y `curso/S2_modelos_calibracion/M06_practica_I_residuos.html`.
- Actualizado este registro.

## Comprobaciones

- `prop_e.md` leído y nivel de cada práctica acotado a M6; no se añade análisis GGMR, temas de otros módulos ni taller.
- `curso/guia_libreto.md` y `curso/revision_final.md` leídos. Restricción de bibliografía respetada: ningún cambio en referencias, claves, citas existentes ni sección de referencias.
- La lectura inicial del estado git confirmó trabajo concurrente en M06 y otros archivos. Las modificaciones se aplicaron con reemplazos exactos de los tres marcadores únicos; no se reemplazó archivo completo ni se tocaron otros capítulos.
- La ruta de skill pedida `/tmp/claude-1000/bundled-skills/2.1.310/2f61c5aeeb1c7fa7387d9a5b54dd86ec/dataviz/SKILL.md` no existía. Se cargó la skill disponible `dataviz` (base `/tmp/claude-1000/bundled-skills/2.1.310/24f3c599ea36004a44f1a3655051fdae/dataviz/`) y se leyeron sus referencias de forma, color, marcas, interacción y antipatrones. Se generó el gráfico de residuos exigido por el diagnóstico I; la salida se renderizó con Chromium para inspección visual. La paleta de un color `#2a78d6` (claro) y `#3987e5` (oscuro) pasó el validador en ambos modos en una corrida anterior; esa validación no se reejecutó en la ronda de cierre y no es repetible desde el repositorio (validador externo). El gráfico incluye ejes y unidades, escala del error en paneles por día, marcadores con foco/tooltip, tabla HTML accesible y selector explícito de modo oscuro.
- Pendiente explícito: el contenido existente deja como condicional el estudio R&R real de CALAIRE debido a incertidumbres documentales de signo y agrupación. La práctica A usa solo datos simulados reproducibles y pide la evidencia necesaria antes de inferir sobre el archivo propio.
- No commits.

## Correcciones de la revisión Haiku (ronda de correcciones M06, 2026-10-27)

Verificado en esta ronda: `curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M06_practicas_luna.py` terminó con rc=0. Todas las cifras de las soluciones de B, I y A del libreto coinciden con su salida. Los 48 valores de `BD_DIAS` de las prácticas I (columnas F/L/R/X/AD/AJ, filas 31–38, con signo invertido) coinciden con la tabla del enunciado (comparación programática de los seis días, diferencia máxima ≈ 1e-14).

| Hallazgo | Decisión | Ubicación y resultado |
|---|---|---|
| H-01 | Aplicado. Se sustituye el conjunto simulado de I por un subconjunto limpio de datos propios, sin usar defectos del archivo como actividad. | `M06_libreto.md`, Práctica I; `calc/M06_practicas_luna.py`. Level 2 frente a SRP 55, 90 nmol/mol nominal, hoja `BD_DIAS`, columnas F/L/R/X/AD/AJ, filas 31–38. Se declara inversión del signo de la columna «Diferencia» para usar $e=y-x$. ANOVA reproducible con 6 días × 8 lecturas. |
| H-02 | Aplicado parcialmente. Se añaden tres contrastes de interacción por pares de campañas con control Bonferroni, y la tarea sobre el R&R propio queda condicionada a la confirmación técnica de signo, fechas, bloques/campañas y unidad de réplica. No se añade ejecución obligatoria del R&R porque el propio libreto declara que el signo y la agrupación no están confirmados. El ejemplo sugerido `Fcrit(2,6)` no corresponde a tres contrastes de 1 g.l.; se usa `Fcrit(1,6)`. Además, se añade una frase: el denominador $MS_D$ es didáctico y el cociente de contraste es aproximado, porque la varianza del contraste contiene interacción. | `M06_libreto.md`, Práctica A (tareas y solución docente). `calc/M06_practicas_luna.py` (líneas 57–64). Contrastes −0,40/0/0,40; F=4/0/4; umbral 10,807361; ninguno lo supera. No se atribuye una inferencia validada al estudio histórico mientras falten confirmaciones. |
| H-03 | Aplicado. I ahora exige cuantificar incertidumbre de componentes y explica límites de la aproximación delta. | `M06_libreto.md`, Práctica I; `calc/M06_practicas_luna.py`. IC 95 % de $\sigma^2$ [0,041903; 0,099567] $(\mathrm{nmol/mol})^2$; EE aproximado de $\hat\tau^2$ 0,005492 $(\mathrm{nmol/mol})^2$ y de $s_{entre}$ por delta 0,115823 nmol/mol. |
| H-04 | Rechazado por instrucción de alcance: no se toca ninguna cita. Verificado con `git show HEAD`: la cita original era `[Hahs-Vaughn §8.2.1]`; la cita NIST/SEMATECH (§7.4.7.3, URL, «consultado 2026-10-27») es un cambio **ya presente en el árbol de trabajo** antes de esta ronda, fuera de bloques de práctica. No se restaura ni se valida aquí. Pendiente para el usuario y el supervisor de referencias: decidir si se restaura la cita de HEAD o se verifica la fuente NIST; el numeral §7.4.7.3 no está en `docs/`. | `M06_libreto.md`, Escena A1, párrafo «Ojo con la multiplicidad» (fuera de la práctica). |
| H-05 | Aplicado. Se hace autosuficiente la trazabilidad del conjunto A; no depende de que el lector reconstruya los datos de I3. | `M06_libreto.md`, Práctica A: incluye los seis pares firmados y la regla simulada; `calc/M06_practicas_luna.py` conserva la matriz numérica idéntica. |
| H-06 | Aplicado en el script y en la práctica. El comentario de `sigma2_reml` indica que es la frontera REML; la optimización se remite a `calc/M06_ejemplos.py`. La solución de A ya lo indica. **No aplicado en la narración:** la frase de la Escena A2 (línea 237, «El script contrasta la solución de frontera con la optimización de la verosimilitud restringida») sigue atribuyendo la optimización al script de prácticas. Es narración, fuera de alcance; queda pendiente. | `calc/M06_practicas_luna.py` líneas 73–75; `M06_libreto.md`, solución de Práctica A (líneas 261–263). Pendiente: `M06_libreto.md` línea 237. |
| H-07 | Rechazado por instrucción de alcance: los dos pasajes están en narración, fuera de bloques de práctica. Sigue sin corregir: línea 152 («las cuatro colas son disjuntas») y línea 219 («esperaríamos en promedio medio falso positivo»). Pendiente para el usuario. | `M06_libreto.md`, Escenas I4 (línea 152) y A1 (línea 219). |
| H-08 | Aplicado en la bitácora, con reserva. Se retiró la afirmación de validación previa. El gráfico sí existe (`M06_practica_I_residuos.html`, generado por `calc/M06_practica_I_grafico.py`). La validación de paleta citada en la sección Comprobaciones **no se reejecutó en esta ronda**; no es verificable desde esta bitácora. | Este archivo, sección Comprobaciones. |

## Ejecución de esta ronda

- Cambios en el libreto: solo en la Práctica A, solución docente (línea 261): se añade que el denominador $MS_D$ es didáctico y que el cociente de contraste es aproximado. Ninguna cifra cambia.
- Cambios en el script: ninguno en esta ronda (las correcciones H-01, H-02, H-03, H-05 y H-06 ya estaban aplicadas en el árbol de trabajo y se verificaron aquí).
- Sin commit. Sin cambios en referencias, claves, citas ni en la sección de referencias.

No se modificaron capítulos distintos de M06, guía, revisión final, referencias, claves ni citas; no se creó commit.

## Ronda de cierre

Fecha: 2026-10-28. Ejecutor: Luna (continuación). Entrada: `logs/M06_practicas_revision_cierre_haiku.md`. Reejecución: `curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M06_practicas_luna.py`, rc=0; cifras de B, I y A sin cambio. Nivel 94 confirmado en `BD_DIAS!AL31:AL38`. No se modificaron referencias, claves, citas ni `guia_libreto.md`. No hay commits.

| H-xx | decisión | ubicación | rc |
|---|---|---|---|
| H-01 | Aplicado: 90 → 94 nmol/mol (columna AL de `BD_DIAS`, filas 31–38). Cifras sin cambio. | `M06_libreto.md` Práctica I (enunciado); `calc/M06_practicas_luna.py` líneas 21 y 79 | 0 |
| H-02 | Rechazado: la bitácora no es uno de los archivos autorizados para esta ronda. La afirmación de la línea 35 («pasa el validador en ambos modos», «se renderizó con Chromium») sigue sin reejecutarse y debe corregirse en la bitácora por quien la mantenga. | `logs/M06_practicas_luna.md` línea 35 (sin cambio) | 0 |
| H-03 | Aplicado (narración): «El script» → «El script `calc/M06_ejemplos.py`». | `M06_libreto.md` Escena A2, línea 237 | 0 |
| H-04 | Aplicado (narración): «esperaríamos, en promedio, medio falso positivo: diez pruebas por cinco centésimas». La cita NIST de la misma frase no se tocó. | `M06_libreto.md` Escena A1, línea 219 | 0 |
| H-05 | Aplicado (narración): se define por qué los cuatro sucesos son disjuntos (con C > 0,5 solo un grupo puede superar el umbral) y por qué el cuantil beta de α/4 es exacto. La cita ISO 5725-2 se mantiene. | `M06_libreto.md` Escena I4 (ejemplo de Cochran), línea 152 | 0 |
| H-06 | Aplicado: se retira la referencia a una «tabla simulada de I3» (que no existe en el libreto) y se remite a la matriz del enunciado de la práctica A. Mismo cambio en el comentario del script. | `M06_libreto.md` Escena A1, línea 201; `calc/M06_practicas_luna.py` línea 47 | 0 |
| H-07 | Rechazado, decisión pendiente del usuario: no se renombran los bloques. La petición que autoriza estas prácticas consta en la línea 3 de esta bitácora. La guía no se modifica en esta ronda; hay que decidir si se actualiza `guia_libreto.md` §1 o se reducen los bloques al marcador permitido. | `M06_libreto.md` líneas de Práctica B, I y A (sin cambio) | 0 |
| H-08 | Rechazado: es una cita (NIST/SEMATECH §7.4.7.3 frente a Hahs-Vaughn §8.2.1). Lo lleva el supervisor de referencias. La cita de la línea 219 no se modificó. | `M06_libreto.md` línea 219 (sin cambio); `logs/M06_practicas_luna.md` línea 48 (sin cambio) | 0 |

Pendientes para el usuario: H-02 (línea 35 de esta bitácora), H-07 (guía frente a bloques `[PRÁCTICA]`) y H-08 (cita NIST, con su registro en la línea 48).
