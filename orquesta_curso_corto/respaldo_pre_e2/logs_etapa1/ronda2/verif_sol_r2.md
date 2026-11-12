# Re-verificación global — etapa 1, tras la ronda 2

Fecha: 2026-11-11. Directorio: `Curso_CORTO/`. Los localizadores `archivo:línea` son relativos a este directorio y corresponden al estado final revisado, incluido el cierre manual de `cambios_r3.md`.

## Veredicto final

**ETAPA 1 NO CERRADA.**

**F01–F06 están resueltos y las tres discrepancias de la sección 6 del informe anterior también.** Se conserva íntegra la cobertura M2–M6 del PDF, no se detecta pérdida ni duplicación de contenido por las ediciones paralelas y no quedan remisiones docentes que exijan módulos excluidos. **Los 12 scripts terminan con código 0 y stderr vacío; los cinco HTML se regeneran idénticos.**

La condición «no quedan rutas rotas» todavía no se cumple globalmente: aunque las rutas señaladas originalmente en los libretos ya están corregidas, **cuatro scripts de M06 conservan instrucciones de ejecución con rutas inexistentes**. Por ello F07 sigue pendiente en su alcance de reproducción documental. Subsisten además delimitaciones ambiguas de alcance de la observación 5.6. No son fallos de cálculo ni huecos del PDF, pero no corresponde certificar una limpieza global completa.

No se editó ningún material del curso ni ningún registro anterior. La única entrega persistente de esta revisión es este informe.

## 1. Fuentes y método

- Lectura íntegra de `logs_etapa1/verif_sol_etapa1.md`, incluidos F01–F07 y secciones 5–6, y de los seis registros `logs_etapa1/ronda2/cambios_r1.md`, `cambios_r2.md`, `cambios_r3.md`, `verif_r1.md`, `verif_r2.md` y `verif_r3.md`.
- Contraste de los cinco libretos actuales con sus fuentes en `../Curso_COMPLETO/curso/S1_fundamentos/` y `../Curso_COMPLETO/curso/S2_modelos_calibracion/`. Comprobación contextual de continuidad, prerrequisitos y exclusiones; no solo búsqueda de códigos de módulo.
- Fuente de cobertura: PDF `/home/w421/.t3/userdata/attachments/a4307bec-cdcb-489e-82fa-5e2e16ccbd98-3ba09308-7d01-4dd1-9c26-73aa937425e7-pdf.pdf`, «Temario resumido SRP», página 1 de 1, mediante extracción de texto del documento real.
- Comprobación de existencia de rutas locales, instrucciones en scripts, dependencias Excel y regeneración de HTML. No se revalidó el contenido de toda la bibliografía externa ni se hizo revisión visual en navegador.
- Ejecución de todos los `.py` de `calc/` en copia temporal, con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I`, sin `-O`, procesos independientes y límite de 120 s por script.
- Se excluyen el recorte a diez horas de la etapa 2 y la validación histórica del estudio CALAIRE. Las limitaciones históricas expresamente declaradas no se convierten aquí en nuevos requisitos de adaptación.

## 2. Tabla de cierre F01–F07 y sección 6 anterior

| Punto anterior | Estado | Evidencia actual y conclusión |
|---|---|---|
| **F01 — referencia explícita a M1** | **resuelto** | `M03_libreto.md:18` remite al punto de partida y a la ecuación de M02. La búsqueda de M0/M1 y M7–M13, con y sin cero inicial, y AX.x no encuentra remisiones a capítulos excluidos en los cinco libretos. |
| **F02 — promesas de formación excluida** | **resuelto** | `M03_libreto.md:326,354` excluye GGMR y exige escalar, sin prometer su aplicación; `M05_libreto.md:78` remite a M02 y excluye regresión/control; `M06_libreto.md:283` cierra el curso corto, sin anunciar un módulo posterior de regresión. Las continuaciones restantes conducen a capítulos incluidos. |
| **F03 — práctica que exigía ajustar una recta no enseñada** | **resuelto** | `M02_libreto.md:174` pide leer e interpretar la recta ya ajustada y dice expresamente «No estimen los coeficientes». Es coherente con la recta entregada en `:160`, el gráfico suministrado y la solución en `:176`. |
| **F04 — MAD antes de su definición** | **resuelto** | El cierre manual está presente: `M02_libreto.md:96` ya no menciona MAD. B6 funciona con IQR; MAD se introduce y define en I, `:146–150`, conforme a la ficha `:9–10`. |
| **F05 — unidades y condición del modelo SRP** | **resuelto** | `M02_libreto.md:18` declara modelo simplificado a condiciones estándar, T adimensional, c en atm, α en atm⁻¹ cm⁻¹ y L en cm; incluye Y=(c/p₀)·10⁹, p₀=1 atm, para nmol/mol y advierte que no sustituye las correcciones operativas fuera de esas condiciones. |
| **F06 — cita Otto no resoluble en M02** | **resuelto** | La cita de `M02_libreto.md:98` resuelve en la referencia completa de `:238`, con autor, título, edición, año, §2.2 y un PDF existente. Se cierra la trazabilidad local; no se certifica por ello toda la atribución estadística de la fuente. |
| **F07 — rutas y reproducción documental** | **pendiente** | Los destinos originales de los libretos están corregidos: M04 `:152`, M06 `:189`, M03 `:220` y M02 `:120,176,216`. Las bibliografías con rutas explícitas y la bitácora de M05 tienen destino existente. Sin embargo, las instrucciones de `calc/M06_practicas_luna.py:3`, `calc/M06_practica_I_grafico.py:4–5`, `calc/M06_ejemplos.py:4` y `calc/M06_RR_CALAIRE.py:8` conservan `curso/.venv/bin/python` y, en dos casos, `curso/S2_modelos_calibracion/calc/...`, inexistentes desde el curso corto y desde la raíz actual del repositorio. Véase sección 3. |
| **Sección 6, discrepancia 1 — +1,8 frente a +1,6** | **resuelto** | `calc/M02_examples.py:94` usa +1,6. Su ejecución produce media firmada 0,177777778, media absoluta 0,533333333 y s=0,670406179, concordantes con `M02_libreto.md:198,216` y con el script de prácticas. |
| **Sección 6, discrepancia 2 — figura 90 frente a nominal 94** | **resuelto** | `M06_libreto.md:172`, `calc/M06_practica_I_grafico.py:3,39,94` y el HTML regenerado identifican 94 nmol/mol. Se comprobó el Excel: `BD_DIAS!AL31:AL38` corresponde al nominal 94; C31:C38 contiene indicaciones próximas a 94, no el rótulo nominal. `calc/M06_practicas_luna.py:79` también imprime 94. |
| **Sección 6, discrepancia 3 — seis días atribuidos al certificado** | **resuelto** | La ficha, diapositiva, narración y práctica de `M05_libreto.md:12,62,64,72,98` declaran los seis días como supuesto didáctico. El cierre manual corrigió los dos lugares vecinos que faltaban. `Fotometro!E17` declara 10 puntos de concentración, 2 de cero y 8 repeticiones por punto, sin declarar seis días. El conteo 576 queda condicionado al supuesto, no atribuido a esa nota. |

### Lectura de los verificadores parciales

Los pendientes de MAD y de la diapositiva de M05 que describe `verif_r2.md` ya no representan el estado final. También están eliminadas las repeticiones concretas de M02:128 y M06:46 que describía `verif_r1.md`. `cambios_r3.md` **sí existe ahora**, contiene la reconstrucción de cambios y el cierre manual; la ausencia consignada en `verif_r3.md:9–16,43` corresponde a un estado anterior. No es necesario reescribir esos testimonios históricos para reconocer las correcciones actuales.

## 3. Rutas: qué quedó corregido y qué sigue pendiente

### Comprobaciones satisfactorias

- Se comprobaron **56 destinos locales explícitos distintos, en 134 menciones**, en los cinco libretos y el registro auxiliar `M05_practicas_luna.md`; todos existen. El recuento incluye rutas en código entre comillas invertidas y los componentes de los comandos documentados, no todas las alusiones textuales a fuentes.
- En `M03_libreto.md:368`, `c05.pdf`, `c06.pdf`, `c08.pdf` y `c09.pdf` son abreviaciones de la serie bibliográfica inmediatamente precedente. Sus expansiones `../Curso_COMPLETO/docs/statistical_concepts_cXX.pdf` existen; no se cuentan como cuatro archivos faltantes en la raíz.
- Las referencias web o bibliográficas marcadas expresamente como no suministradas no se trataron como rutas locales rotas. `GUM-S2` es una referencia bibliográfica, no una remisión a un módulo excluido.
- `calc/M03_practica_I_probabilidad.html` se generó de nuevo en su ubicación real. Los otros cuatro HTML también se recrearon. Los cinco son autocontenidos respecto de enlaces `href`/`src`: no contienen dependencias locales mediante esos atributos.
- La decimotercera entrada de `calc/` es precisamente `M03_practica_I_probabilidad.html`, **no un script faltante**. Hay 12 `.py`.

### Residuo que impide certificar F07 globalmente

| Archivo:línea | Instrucción todavía suministrada | Efecto |
|---|---|---|
| `calc/M06_practicas_luna.py:3` | `curso/.venv/bin/python curso/S2_modelos_calibracion/calc/M06_practicas_luna.py` | No existe el intérprete ni ese destino de script desde la raíz de `Curso_CORTO/`; tampoco desde la raíz actual del repositorio. Omite `-I`. |
| `calc/M06_practica_I_grafico.py:4–5` | «Ejecutar desde la raíz» con `curso/.venv/bin/python curso/S2_modelos_calibracion/calc/M06_practica_I_grafico.py` | Mismo problema. El programa funciona con el comando adaptado, pero no con la instrucción incluida en su cabecera. |
| `calc/M06_ejemplos.py:4` | «Ejecutar con curso/.venv/bin/python desde la raíz del repositorio» | El entorno indicado no existe en esa ubicación actual. |
| `calc/M06_RR_CALAIRE.py:8` | La misma ubicación heredada del intérprete | Mismo problema de localización, aunque BOOK y ROOT sí están adaptados y el programa corre. |

Para cerrar este residuo basta armonizar esas instrucciones con el patrón que ya usan los libretos: desde `Curso_CORTO/`, `../Curso_COMPLETO/curso/.venv/bin/python -I calc/<script>.py`. **No se aplicó esa corrección durante esta revisión.**

Además, `calc/M03_practicas_luna.py:138` todavía imprime `I_salida_grafica=M03_practica_I_probabilidad.html` sin `calc/`. El archivo se crea junto al script (`:94`), no en el directorio de trabajo. El libreto ya da la ruta correcta; queda una salida de localización ambigua que conviene armonizar en la misma pasada.

## 4. Seguimiento de las observaciones de la sección 5 anterior

| Observación | Estado | Comprobación final |
|---|---|---|
| **5.1 — inventario 13/12** | **resuelto** | `00_plan_corto.md:16–17` declara 12 scripts, que coincide con el inventario y con la ejecución. |
| **5.2 — localizadores históricos desplazados y registros incompletos** | **resuelto** | Esta re-verificación proporciona localizadores actuales y contrasta los cambios con los archivos, incluido el cierre manual reconstruido. Los números de línea de rondas anteriores son históricos, no enlaces de uso del curso que deban seguir coincidiendo tras cada inserción. |
| **5.3 — conclusión anterior de limpieza demasiado amplia** | **pendiente** | No se puede elevar a una certificación de ausencia global de rutas rotas: persisten las instrucciones de los scripts indicadas en F07. Sí se confirma la limpieza de remisiones docentes fuera de M2–M6. |
| **5.4 — M1, unidades, MAD, Otto y transición inicial** | **resuelto** | F01/F04/F05/F06 resueltos; `M02_libreto.md:22` recuerda las definiciones recién presentadas, sin «ya damos por visto». |
| **5.5 — ficha B6 no anunciaba IQR** | **resuelto** | `M02_libreto.md:9` anuncia detección gráfica y regla IQR. Se mantiene la distinción entre bigotes mínimo/máximo del ejemplo y cercas exploratorias de B6. |
| **5.6 — redundancias y exclusiones ambiguas** | **pendiente** | El cierre manual simplificó M02:128 y M06:46. Sin embargo, M02:128 aún excluye en bloque el «tratamiento» de residuos, incertidumbre en ambos ejes y pocos grados de libertad, aunque M03/M04 sí enseñan grados de libertad y sus consecuencias. M06:140 conserva «no cubre estas tablas» con referente poco claro; M06:211 sigue poniendo «fuera del alcance de este curso» dentro de la cita del párrafo que enseña denominadores. Debe distinguirse la deducción excluida de la aplicación incluida. La reiteración en M04:13,34,292 es editorial, no duplicación por colisión. |
| **5.7 — AX.4 en comentario auxiliar** | **resuelto** | `calc/M05_diseno.py:48` remite al modelo planteado en el capítulo, no a AX.4. |

**Errata del registro nuevo, sin efecto en los libretos:** `cambios_r1.md:13` dice «M3/M4 excluidos». Ambos módulos están incluidos. Esa explicación del cambio no debe usarse como delimitación del curso; su alcance real es el del PDF y de los cinco capítulos revisados. No se corrigió el registro.

Las ambigüedades de 5.6 son de coherencia editorial y no significan que falte la enseñanza de grados de libertad o de denominadores. Deben evitarse formulaciones que presenten como excluido lo que se utiliza y explica en el curso.

## 5. Integridad de las ediciones paralelas y cobertura del PDF

**No se detecta pérdida ni duplicación accidental de las intervenciones en el estado final.** La comparación con las fuentes conserva todas las escenas originales y las tres prácticas B/I/A de cada capítulo. Las secciones nuevas son la apertura y B6 de M02; no aparecen dos copias de ellas. Permanecen simultáneamente la autonomía inicial, las sustituciones de remisiones, la regla IQR, el cambio de tarea de la práctica I, la cita Otto y la vuelta explícita a M02 en M04-I5.

En M05 coexisten la limpieza de regresión/control y la atribución corregida de los seis días en ficha y diapositiva. M06 conserva tanto las adaptaciones de alcance como el nominal 94 y el comando corregido del libreto. En los scripts, las diferencias con las fuentes son compatibles con los cambios registrados y la reubicación de entradas/salidas; no se observa reversión del +1,6, del nominal 94 ni de la eliminación de AX.4.

Esto acredita la integración visible de los archivos finales frente a las fuentes actuales, no reconstruye la secuencia histórica de escrituras concurrentes.

| Módulo y requisito literal del PDF | Evidencia actual | Cobertura |
|---|---|---|
| **M2:** «resumen y gráficos de las lecturas; valores atípicos» | `M02_libreto.md:34–60`, frecuencias, histograma, cuantiles, caja y dispersión; `:84–100`, secuencia temporal, regla IQR, investigación y conservación. Puente formal a `M04_libreto.md:180–188`. | **Completa** |
| **M3:** «modelos de la variabilidad y del ruido del SRP» | `M03_libreto.md:20–118`, variables, distribuciones, ruido independiente/común, deriva y t; `:228–246,284–306`, escala temporal y autocorrelación. | **Completa** |
| **M4:** «intervalos de confianza y pruebas de hipótesis» | `M04_libreto.md:40–68`, intervalo y contraste; `:98–130`, pareadas, Welch y varianzas; `:224–270`, multiplicidad, equivalencia y consistencia. | **Completa** |
| **M5:** «planificación de las comparaciones» | `M05_libreto.md:20–58`, respuesta, factores, unidades y réplicas; `:118–176`, aleatorización, factoriales y reparto del esfuerzo; `:233–285`, planificación R&R. | **Completa** |
| **M6:** «repetibilidad, precisión intermedia y estudios R&R» | `M06_libreto.md:24–56`, precisión; `:82–166`, ANOVA y componentes; `:195–267`, estructura R&R, componentes negativas y límites del histórico. El caso simulado permite practicar sin depender de validar el histórico. | **Completa** |

El puente exploración en M02 → pruebas en M04 satisface la opción autorizada por `00_plan_corto.md:24`. No es necesario trasladar toda I5 a M02, incorporar M1 ni añadir un módulo de regresión para cubrir el PDF.

## 6. Ejecución completa de `calc/` y protección del original

Se copió el curso a `/tmp/curso_corto_verif_sol_r2_4twji4ol/Curso_CORTO/`. Se verificó igualdad SHA-256 de los 12 scripts antes de ejecutarlos. Para comprobar generación real y no solo presencia de artefactos antiguos, se retiraron **únicamente de la copia** los cinco HTML suministrados antes de la ejecución.

Intérprete utilizado: `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python`, **Python 3.14.7**, siempre con `-I`. Directorio de trabajo: raíz de la copia temporal.

| Script | Código de salida | stderr | Tiempo (s) |
|---|---:|---|---:|
| `calc/M02_examples.py` | 0 | vacío | 0,298 |
| `calc/M02_practicas_luna.py` | 0 | vacío | 0,196 |
| `calc/M03_ejemplos.py` | 0 | vacío | 1,572 |
| `calc/M03_practicas_luna.py` | 0 | vacío | 1,118 |
| `calc/M04_ejemplos.py` | 0 | vacío | 1,625 |
| `calc/M04_practicas_luna.py` | 0 | vacío | 1,423 |
| `calc/M05_diseno.py` | 0 | vacío | 1,054 |
| `calc/M05_practicas_luna.py` | 0 | vacío | 1,055 |
| `calc/M06_RR_CALAIRE.py` | 0 | vacío | 1,330 |
| `calc/M06_ejemplos.py` | 0 | vacío | 1,070 |
| `calc/M06_practica_I_grafico.py` | 0 | vacío | 0,736 |
| `calc/M06_practicas_luna.py` | 0 | vacío | 1,022 |

No hubo timeout ni `assert` fallido. Se regeneraron y compararon byte a byte `M02_practica_B_grafico.html`, `M02_practica_I_grafico.html`, `M02_practica_A_grafico.html`, `calc/M03_practica_I_probabilidad.html` y `M06_practica_I_residuos.html`: **5/5 idénticos a los entregados**.

Comprobaciones numéricas adicionales: M04-I5 conserva G=2,437429532, crítico unilateral=2,220833452, bilateral=2,274365127 y Q=0,821428571; M06-I reproduce F=1,072952436, s_r=0,248261659 y s_entre=0,023707434. La concordancia corregida del ejemplo M02 está documentada en la tabla de cierre.

`M06_RR_CALAIRE.py` sigue advirtiendo «EXPLORATORIO CONDICIONAL: signo, fechas y cruce de bloques pendientes». La advertencia es coherente con `M06_libreto.md:197–207`; no se presenta su ejecución satisfactoria como validación histórica del estudio.

Una consulta auxiliar de esta revisión al Excel falló inicialmente al pedir `.coordinate` a una `EmptyCell`; se corrigió la consulta y se completó el contraste. No fue un fallo de ninguno de los 12 scripts del curso.

Los SHA-256 de los **55 archivos preexistentes** se conservaron durante la revisión y antes de escribir este informe. Evidencia temporal: `/tmp/curso_corto_verif_sol_r2_4twji4ol/results.json` y archivos individuales `*.stdout.txt` / `*.stderr.txt`. Es evidencia de revisión, no una dependencia permanente del curso.

## 7. Condición de cierre

No se requiere rehacer el contenido ni repetir las correcciones de F01–F06 o de la sección 6 anterior. Falta:

1. **Completar F07**: armonizar las cuatro instrucciones heredadas de los scripts M06 y la localización impresa del HTML de M03. La condición de ausencia global de rutas rotas no puede darse por cumplida mientras se suministren esos comandos inexistentes.
2. **Precisar la delimitación pendiente de 5.6**: separar lo que no se desarrolla en una escena básica de lo que realmente queda fuera del curso; en M06, excluir inequívocamente las deducciones, no las aplicaciones enseñadas.
3. Como ajuste documental menor, corregir la afirmación «M3/M4 excluidos» del registro r1 cuando se actualicen los registros de cierre.

**Balance:** cobertura del PDF completa; integración sin pérdidas o duplicaciones detectadas; cálculos y HTML reproducibles; correcciones sustantivas y discrepancias heredadas resueltas. **ETAPA 1 NO CERRADA por limpieza documental de rutas todavía incompleta, con observaciones de alcance pendientes.**
