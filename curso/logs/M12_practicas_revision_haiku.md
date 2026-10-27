# Revisión de las prácticas M12 — revisor Haiku

Alcance: `curso/S3_comparacion_decision/M12_libreto.md` (bloques de práctica B, I y A, y su contexto inmediato), `curso/S3_comparacion_decision/calc/M12_practicas_luna.py` y `curso/logs/M12_practicas_luna.md`. No se editó ningún archivo del curso. No se auditaron referencias bibliográficas (otro supervisor).

## Verificaciones ejecutadas

- `curso/.venv/bin/python -I curso/S3_comparacion_decision/calc/M12_practicas_luna.py` → rc=0. Reproduce: B $\bar d=0$, media de |d| = 2,0 %, $s_d=2,3664$ %; I $\chi^2_{0,10;5}=1,6103$, $L_{90}(s_d)=4,1699$ %, $AB=2,0$ %, $AS=0,8944$ %, $t_{0,95;5}=2,0150$, $L_{95}(AB)=2,7358$ %, IC 95 % de $\bar d$ = [−2,4834; +2,4834] %; cambio de escala: media de |d| = 2,0200 %; cero: $s_0=0,1581$, $3s_0=0,4743$ nmol/mol; A: medias por periodo 1,00 y 3,00 %, conjunta 2,00 %.
- Recalculado a mano/Python fuera del script: $u(\bar d)=\sqrt{0{,}80^2+0{,}60^2/3}=0{,}8718$ pp; $\sqrt{0{,}64+0{,}60^2/2}=0{,}9055$ y $\sqrt{0{,}64+0{,}045}=0{,}8276$; valores de los ejemplos de I1 ($L_{90}=4{,}1367$ %), I2 ($L_{95}(AB)=2{,}1794$ %, IC ±2,9052 %), A1 ($0{,}6455$ % y $1{,}0000$ %). Todos coinciden con el libreto.
- Texto normativo comprobado en `docs/Appendix A to Part 58_…pdf`: §2.3.1.2 (metas O₃: CV 7 % límite superior 90 %, sesgo absoluto 7 % límite superior 95 %), §3.1.1 (one-point QC SO₂/NO₂/O₃/CO), §4.1.1 (diferencia porcentual), §4.1.2 (cuantil 10 % chi-cuadrado, n−1 g.l.), §4.1.3 (AB, AS, t₀,₉₅), §4.1.3.1–4.1.3.2 (signo por percentiles 25 y 75). Coinciden con el libreto.
- `docs/BS EN 14625_2012.pdf`: fórmula (5) $l_{det}=3{,}3\cdot s_{r,z}/B$ con §8.4.5. Coincide con la escena I4.
- Aritmética de las prácticas B e I (sumas, divisores, cuantiles, cambio de escala 1,01) revisada: correcta.

Conclusión de cálculo: los números de las soluciones docentes son correctos. Los hallazgos siguientes son de coherencia del enunciado, de alcance y de trazabilidad.

## Hallazgos

### H-01 — Severidad media — práctica A: «la comprobación individual posterior» es ambigua y la solución omite dos incumplimientos

- **Ubicación:** `M12_libreto.md` líneas 274 (enunciado: «La comprobación individual de un monitor se hizo después del mantenimiento») y 276–283 (tabla con tres filas «Después»), y 289 (solución: «En la comprobación individual posterior de 100 nmol/mol, la indicación 103,0 produce e=+3,0…»).
- **Problema:** el enunciado habla de una sola comprobación individual, pero la tabla contiene tres verificaciones posteriores (4, 5 y 6). La solución elige la fila 5 sin decirlo. Con la tolerancia ±2,0 nmol/mol del propio enunciado, las filas 4 (e = +2,5 nmol/mol) y 6 (e = +3,5 nmol/mol) también son no conformes; la solución no lo dice, y el estudiante puede concluir que solo una verificación falla.
- **Escenario de fallo:** un estudiante que calcula solo la fila 5 declara «una no conformidad» y no revisa las otras dos, o bien confunde «comprobación individual» (una pareja) con «monitor» (varias parejas).
- **Corrección propuesta:** en el enunciado, sustituir «La comprobación individual de un monitor» por una frase que fije la unidad de análisis («las tres verificaciones posteriores son del monitor X» o «la comprobación individual es la verificación 5»). En la solución, evaluar las tres filas posteriores: e = +2,5; +3,0; +3,5 nmol/mol, todas por encima de 2,0 nmol/mol; estado no conforme bajo la regla suministrada.

### H-02 — Severidad media — práctica A: la señal de control también aparece antes del mantenimiento y la solución no lo menciona

- **Ubicación:** `M12_libreto.md` líneas 289 (solución) y 293 (decisión operativa).
- **Problema:** el límite superior de control de +1,0 % se aplica a todas las filas. La verificación 3 («Antes», d = +1,5 %) también lo supera. La solución dice «las tres diferencias posteriores también exceden el límite superior de control» y calla la fila 3. Esto afecta a la narrativa del caso: la señal no empieza en el mantenimiento y el ejercicio parece atribuir el cambio al periodo posterior, justo lo que la decisión operativa dice no hacer («no afirmar que el mantenimiento causó el cambio»).
- **Escenario de fallo:** el estudiante concluye que la carta «detecta el mantenimiento» porque solo ve las filas posteriores como fuera de control; el docente no tiene respuesta a «¿por qué la verificación 3 también es señal?».
- **Corrección propuesta:** en la solución, añadir: «Además, la verificación 3 (antes, +1,5 %) supera +1,0 %: la señal de control no coincide exactamente con el periodo posterior; el investigador debe revisar la carta completa y las fechas, no solo el periodo.» Ajustar la decisión operativa para mencionar que la señal de control es anterior y posterior.

### H-03 — Severidad media — práctica A: el alcance de prop_e pide que el escenario defina muestra y cobertura, y el enunciado no las define

- **Ubicación:** `M12_libreto.md` líneas 274 (enunciado) y 293 (solicitud de evidencia). `prop_e.md` línea 216 (M12-A): «El escenario define muestra, referencia, periodos, métrica agregada, cobertura y criterio».
- **Problema:** el enunciado define referencia (100 nmol/mol), periodos (antes/después), métrica (media de |d|) y criterio (tres criterios). No define la muestra (cuántas verificaciones, cómo se seleccionaron) ni la cobertura (qué monitores o fechas abarca). La solución después pide «tamaño y selección de muestra» y «definición y cobertura del agregado» como evidencia que falta. Eso es correcto como escalamiento, pero contradice el alcance de prop_e: el escenario debía fijar esos elementos.
- **Corrección propuesta:** o bien añadir al enunciado una línea que defina muestra y cobertura (por ejemplo: «seis verificaciones de un único monitor, selección cronológica completa en la campaña, sin cobertura de otros monitores»), o bien, si la intención docente es dejarlos abiertos, indicarlo en la solución y dejar anotado que la práctica no cumple al 100 % el alcance de prop_e. Se recomienda la primera opción: es coherente con la solicitud posterior de evidencia.

### H-04 — Severidad baja-media — trazabilidad: la bitácora afirma que el script reproduce «todos» los valores declarados, y no es cierto

- **Ubicación:** `curso/logs/M12_practicas_luna.md` líneas 16 y 29 («Script reproduce todos los valores numéricos declarados»); `curso/S3_comparacion_decision/calc/M12_practicas_luna.py` líneas 51–54.
- **Problema:** el script no imprime $u(\bar d)$ para n = 3 (0,8718 pp), que es el valor de la práctica A; solo imprime n = 2 y n = 8. Tampoco reproduce los valores de los ejemplos de I1 (4,1367 %), I2 (2,1794 % y ±2,9052 %) y A1 (0,6455 %, 1,0000 %), ni las diferencias posteriores e = +2,5; +3,0; +3,5 nmol/mol. Los valores son correctos (los comprobé fuera del script), pero el registro de reproducibilidad es incompleto.
- **Escenario de fallo:** alguien que ejecute el script no encuentra el 0,8718 que la solución docente declara y no puede verificar la práctica A sin escribir código propio.
- **Corrección propuesta:** en el script, añadir `n=3` al bucle de `A common` y los ejemplos de I1, I2 y A1 (o retirar de la bitácora la frase «todos los valores»). Cambiar la bitácora a: «El script reproduce los valores de las prácticas; los ejemplos de escena se comprobaron aparte».

### H-05 — Severidad baja — ozono/SRP: las prácticas no citan la aplicación

- **Ubicación:** `M12_libreto.md` líneas 72–91 (B), 191–212 (I) y 274–295 (A).
- **Problema:** las prácticas usan «monitor», «red» y «referencia de 100 nmol/mol», pero no dicen que son verificaciones de analizadores de ozono (SRP). La unidad nmol/mol sugiere el contexto, pero el encuadre que pide la guía («aplicación ozono/SRP») está solo en las escenas, no en los enunciados prácticos. La solicitud del supervisor exige que el caso ozono/SRP esté presente.
- **Corrección propuesta:** en cada enunciado práctico, añadir una frase: «Son verificaciones simuladas de un analizador de ozono (SRP), con referencia de 100 nmol/mol; no son datos de CALAIRE.» No cambiar los datos ni las soluciones.

### H-06 — Severidad baja — redacción: frase de cierre ambigua en la práctica B

- **Ubicación:** `M12_libreto.md` línea 72.
- **Problema:** «La respuesta es el conjunto de diferencias de estas seis verificaciones» no dice qué se entrega: la frase mezcla la respuesta esperada con el contenido de la tabla. Además «Los datos son didácticos y no proceden de CALAIRE» aparece bien, pero «la escala temporal es una campaña breve» no tiene datos de tiempo en la tabla.
- **Corrección propuesta:** sustituir la primera frase por «Entreguen las seis diferencias d_i y los tres resúmenes pedidos más abajo», y eliminar la referencia a la escala temporal o darle una fecha/orden en la tabla.

## Resumen

- Cálculos y soluciones numéricas: correctos (verificados por ejecución y recálculo).
- Coherencia estadística de B, I y A: correcta; límites, colas y uso de chi-cuadrado y t, cambio de escala y hipótesis de $3s_0$ coinciden con CFR58-A §§2.3.1.2, 4.1.1–4.1.3.2 y EN 14625 (5).
- Puntos a corregir antes de cerrar M12: H-01 y H-02 (práctica A, coherencia de la solución con la tabla y la carta de control), H-03 (alcance de prop_e en la práctica A). H-04 es de trazabilidad. H-05 y H-06 son de redacción y de encuadre ozono/SRP.
- No hay hallazgos sobre orígenes de datos: todos los datos están declarados como simulados, con regla reproducible y sin atribución a CALAIRE.
