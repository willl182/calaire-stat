# Revisión focalizada M05/M06 — Sol

Fecha: 26-10-2026. Estado: revisión y correcciones aplicadas; comprobación independiente y cierre en curso. Este informe se actualiza antes del cierre para preservar la trazabilidad.

## Alcance y método

Se leyeron íntegros `prop_e.md`, `curso/guia_libreto.md`, `curso/00_plan_maestro.md` y `revision_final_prop_e.md`; después los dos libretos, sus bitácoras y revisiones Haiku completas. Se inspeccionaron las tres instantáneas de M05/M06 en `versiones/`, las auditorías sol_2 y sol_3 y los cambios de scripts respecto de `437e8bf`. Se extrajeron 19 PDF con `pdftotext -layout` exclusivamente a `calc/fuentes_sol/M05_M06_00.txt`–`18.txt`. Se ejecutan los scripts con `curso/.venv/bin/python -I`.

No se modifica `S2_revision_sol.md`, índice, bitácoras, revisiones Haiku ni versiones. Las ediciones se limitan a M05/M06 y sus tres scripts; auxiliares y este informe quedan en S2. No se delegó.

## Inventario histórico y decisiones de cada bloque

No existe `auditoria_interrupcion_sol/` en S2 ni auditoría anterior dentro de `versiones/`: el inventario recursivo contiene únicamente doce libretos (cuatro por instantánea). No existen C01–C27 en esta evidencia. No se inventan IDs Cxx ni se importan de otras secciones. Se numeran aquí los bloques `@@` por orden global dentro de cada diff.

Las instantáneas `20261025_202101_antes_P4_sol` y `20261025_220040_antes_P4_sol` son idénticas para M05 y M06. Los cambios hasta `20261026_052610_antes_P4_sol` son los de sol_3; esta última instantánea coincide con los libretos al iniciar esta revisión.

| Auditoría/bloque | Archivo y encabezado exacto | Decisión | Fundamento / hallazgo |
|---|---|---|---|
| sol_2 B01–B03 | Los tres bloques corresponden a M07 | Fuera del alcance, sin editar | No hay bloque M05/M06 en este diff |
| sol_3 B01 | M05 `@@ -11,7 +11,7 @@` | Conservar | Retira BIPM del mapa de referencias y añade fuentes realmente usadas; S-05-01 |
| sol_3 B02 | M05 `@@ -79,9 +79,9 @@` | Conservar | Retira protocolos BIPM de diapositiva y narración; exclusión prop_e §6; S-05-01 |
| sol_3 B03 | M05 `@@ -177,6 +177,8 @@` | Conservar, precisar adaptación | Ejemplo 8 resultados totalmente anidados frente a 4 escalonados, ISO 5725-3 §§9.5 y 9.8; adaptar laboratorio a campaña no acredita un estudio normativo; S-05-02 |
| sol_3 B04 | M05 `@@ -189,7 +191,7 @@` | Conservar | Una campaña propia por analista confunde; varias permiten componentes anidadas, no interacción cruzada; S-05-03 |
| sol_3 B05 | M05 `@@ -213,13 +215,13 @@` | Conservar y precisar terminología | Mantiene distinción confusión/anidación y retira protocolos BIPM; S-05-01/03 |
| sol_3 B06 | M05 `@@ -235,7 +237,6 @@` | Conservar | Retira referencia BIPM ya no usada; S-05-01 |
| sol_3 B07 | M06 `@@ -103,7 +103,7 @@` | Ajustar | Delta sí corresponde a propagación de primer orden, pero faltaban fundamento de la incertidumbre de la varianza y cautela cerca de cero; S-06-02/03 |
| sol_3 B08 | M06 `@@ -181,7 +181,11 @@` | Conservar con condiciones | Bonferroni correcto para diez pruebas; no valida el signo ni el cruce histórico de bloques; S-06-05/06 |
| sol_3 B09 | M06 `@@ -241,5 +245,6 @@` | Conservar y completar | Hahs-Vaughn §8.2.1 contiene Bonferroni; se añade año y cap. 9 para varianzas; S-06-02/06 |
| sol_3 B10–B20 | Once bloques M07 | Fuera del alcance, sin editar | Se registra pertenencia, no se decide contenido de otro capítulo |
| sol_3 B21–B32 | Doce bloques M08 | Fuera del alcance, sin editar | Se registra pertenencia, no se decide contenido de otro capítulo |

Así se contabilizan los 3 + 32 bloques reales: cero + nueve pertinentes, y tres + veintitrés ajenos. No se omite ningún bloque correspondiente a M05/M06.

### Scripts y salidas históricas

`M05_diseno.py` no tenía diff contra `437e8bf`. En `M06_ejemplos.py` había un bloque que cambia la etiqueta de la componente negativa de I a A: **conservar**, porque prop_e la asigna a A (S-06-08). En `M06_RR_CALAIRE.py` había un bloque que añade Bonferroni: **conservar y condicionar interpretación** (S-06-06). La lista `calc_tocados_22h.txt` de sol_3 está vacía: no equivale a prueba de ausencia de cambios contra el commit. Las salidas antiguas `M05_diseno_sol.out`, `M06_ejemplos_sol.out`, `M06_RR_CALAIRE_sol.out` se preservan como evidencia histórica, no se consideran resultados actualizados. Las ejecuciones nuevas quedan separadas en `*_revision_sol.out`; no se sobrescriben las salidas de M07/M08.

## Hallazgos y correcciones

Severidad: mayor = afecta cobertura, interpretación, método o trazabilidad; menor = editorial o precisión terminológica sin alterar resultados centrales. Los IDs siguientes cubren tanto decisiones históricas como problemas adicionales comprobados.

| ID | Ubicación | Severidad | Hallazgo, decisión y cambio |
|---|---|---|---|
| S-05-01 | Ficha, B4, A3 y referencias | Mayor, histórico resuelto | Conservar retirada completa de protocolos BIPM, incluso identificación A/B innecesaria en M05; respeta exclusión y mantiene ejemplos SRP/EPA/ISO pertinentes. |
| S-05-02 | A1, ejemplo escalonado | Mayor, histórico resuelto con precisión | ISO confirma ocho resultados por laboratorio en árbol binario de cuatro factores y cuatro en escalonado. Se conserva, distinguiendo patrón adaptado para un laboratorio de cumplimiento ISO. |
| S-05-03 | A2–A3 | Mayor, histórico resuelto | Se conserva la corrección: anidación con varias campañas propias permite separar componentes bajo modelo; no hay confusión total universal. Se precisa variación entre ciclos, sin llamarla otra repetibilidad indistinta. |
| S-05-04 | I3; `M05_diseno.py` | Mayor, corregido | Incertidumbre del promedio no sustituye ejemplo de potencia. Se añade prueba t bilateral de media de días, Delta 0,20, alfa 0,05, parámetros poblacionales simulados y potencia con t no central para tres repartos del esfuerzo. No se calcula ni atribuye a prop_e una potencia de pendiente 0,005. |
| S-05-05 | A1–A2, denominadores; `M05_diseno.py` | Mayor, corregido | Se afirmaba enseñar denominadores pero no se identificaba ninguno. Se especifican los estratos analista/día/ciclo/lectura, sus denominadores y g.l. 2/9/12/168; además el cruzado con interacción. Se retiran promesas de deducción multifactor en AX.4; respaldo Crowder tablas 9.9–9.10 e ISO 5725-3 anexos B/C. |
| S-05-06 | B1, I3, A2 y bibliografía | Menor, corregido | Se sustituye Montgomery de control estadístico por *Design and Analysis of Experiments*, fuente adecuada a diseño; sin numeral no cotejado y marcado no disponible. Se elimina «linealidad» de la afirmación respaldada solo por EN §§8.4.7–8.4.8. Se completa año de Hahs-Vaughn y fuente técnica de t no central. |
| S-05-07 | B1 y B3 | Menor, corregido | Se distingue M6-B (componentes entregadas) de M6-I (estimación) y se explicita exclusión de Dia0 del conteo de seis días. 576 sigue siendo conteo estructural, no independencia. |
| S-05-08 | A2, R&R | Menor, corregido | Se distingue uso industrial R&R de reproducibilidad normativa; cambios internos de día/operador estudian precisión intermedia. |
| S-06-01 | B2, fórmula U_prec | Menor, corregido | Faltaba cierre `$` tras nmol/mol. Se cierra fórmula, se cambia «ejercicio» por «ejemplo» sin desarrollar práctica. |
| S-06-02 | Ficha, I1–I3 y referencias | Mayor, corregido | AX.4 solo un factor; AX.11 solo indicadores M12. Se eliminan falsas remisiones para modelos multifactor e incertidumbre de componentes; se usan GUM H.5, Crowder tablas 9.9–9.10, ISO anexos B/C y Hahs-Vaughn cap. 9. |
| S-06-03 | I2 | Mayor, corregido | Se escribe y narra fórmula del error estándar de tau² basada en cuadrados medios normales independientes; se distingue sustitución aproximada de IC exacto. Delta se respalda por GUM 5.1.2–5.1.3 y se advierte mala linealización cerca de cero/error relativo grande. |
| S-06-04 | I4 y `M06_ejemplos.py` | Mayor, corregido | «Tamaños comparables» no basta para umbral convencional Cochran. Se exigen igualdad de tamaños, independencia, normalidad e igualdad de varianza bajo H0; se completa ejemplo con cuatro grupos n=5, crítico 0,629 verificado en ISO tabla 4, decisión sin borrado. |
| S-06-05 | A1 y `M06_RR_CALAIRE.py` | Mayor, corregido con pendiente documental | No se acredita cruce de bloques entre analistas ni signo y fechas. Las 360 entradas son no negativas; no prueba ABS, pero tampoco signo y−x. Se retira certeza de días diferentes, se recoge contradicción 171/173 y se condiciona toda inferencia histórica. Se añade ejemplo jerárquico simulado firmado con modelo y componentes explícitos; script real imprime advertencia y comprueba valores finitos. |
| S-06-06 | A1, multiplicidad | Mayor, histórico conservado con condiciones | Diez pruebas al 5 % dan 0,5 falsos positivos esperados bajo H0 global si pruebas válidas, sin exigir independencia. Bonferroni da F crítico 6,354689 y niveles 135/405. No valida correspondencia de bloques; interpretación queda condicionada. |
| S-06-07 | I5 y A2 | Mayor, corregido | Era falso excluir toda ISO 5725-4 como interlaboratorio: introducción y §5 incluyen sesgo de un laboratorio. Se corrige y se añade ejemplo de sesgo con incertidumbre de referencia explícita, sin confundir precisión con veracidad. |
| S-06-08 | A2 y `M06_ejemplos.py` | Mayor, corregido | Las alternativas a componente negativa estaban solo nombradas. Se compara truncamiento con REML restringido en ejemplo normal equilibrado; la frontera reestima sigma², no solo tau². Se calcula también cambio de contribución al promedio. Se conserva traslado de etiqueta I→A. |
| S-06-09 | B2, A1 y cierre | Menor, corregido | s_medias es resumen compatible construido desde componentes dadas, no dispersión observada independiente. Rango 0,13–0,49 se limita a 405/455. Se eliminan conclusiones históricas categóricas del cierre y se explicita que residual de medias diarias no separa repetibilidad. |

## Resultados calculados hasta este registro

M06 ejecutado sin errores: u_prec=0,127279221; U_prec=0,254558441 nmol/mol; repetibilidad sola=0,034641016; s_medias=0,311769145. ANOVA un factor: SS 0,56/0,18/0,74; g.l. 2/9/11; MS 0,28/0,02; F=14; crítico 4,256494729; tau²=0,065; sigma²=0,02. IC sigma²=[0,009462345;0,066657051]; SE tau²=0,070039671; SE delta=0,137359096.

Negativa: tau² no restringida=−0,002533333; REML restringido tau²=0, sigma²=0,014824242; u_media truncada=0,037267800 y REML=0,035147596. Caso firmado A: componentes analista/campaña/interacción/día=0,005/0,056666667/0,016666667/0,02; F=1,5625/5,25/2,666666667. Cochran C=0,45, crítico=0,628724461; no señal. Sesgo=0,30, u_media=0,070710678, u_sesgo=0,086602540 nmol/mol.

R&R real exploratorio: max F_analista=1,238163; crítico=18,512821; interacción crítica=3,315830, sobrepasan 135/360/405/455 con 6,611516/4,308688/6,473497/5,065435; Bonferroni=6,354689, sobrepasan 135/405. s_día=0,106090–0,206247. Las cifras reproducen la descomposición tabulada, no validan el diseño histórico.

M05: efectos factoriales y conteos reproducidos. Se detectó al ejecutar la ampliación una colisión local entre la variable codificada `t` de temperatura y el objeto distribución t; se corrige antes de cerrar y se reejecutará. La salida parcial no se considera ejecución válida.

## Fuentes verificadas / pendientes

Verificadas por extracción local: Crowder cap. 9 (§9.2, §§9.3.1–9.3.3, tablas 9.9–9.10); Brereton cap. 2 y edición 2.ª/2018; Hahs-Vaughn cap. 6, cap. 9 y §8.2.1, portada legal 2020; ISO 5725-3 §§5–6, §8, §§9.3–9.5, §9.8 y anexos; ISO 5725-2 §7.3.3 y tabla 4; ISO 5725-4 introducción y §5.5.2; GUM H.5, G.4, §§5.1.2–5.1.3; EN 14625 §§8.4.7–8.4.8; ISO/IEC 17025 §7.2.2; SRP QAPP §6.2.1; SOP §§9.7.19–9.7.20 y fecha 18-09-2015; EPA TAD §4.4.1; ISO 13964 §6.2.2; MMU §4.4 y año 2025. Se completará mapa extracto→archivo y páginas en el cierre.

El archivo llamado `ISO 5725-1_1994_Cor 1_1998 .pdf` contiene solo corrigendum, no la Parte 1 completa: no acredita sus definiciones originales. Se corregirá la bibliografía y no se declarará verificado el texto íntegro de la Parte 1. VIM, Montgomery DOE, Johnson/Kotz/Balakrishnan y Searle/Casella/McCulloch no están en docs/: sin numerales inventados y pendientes de cotejo documental. Pendientes del R&R: signo, fechas, identificación/cruce de campañas y criterio tres bloques frente a cinco pares. No se resuelven por suposición.
