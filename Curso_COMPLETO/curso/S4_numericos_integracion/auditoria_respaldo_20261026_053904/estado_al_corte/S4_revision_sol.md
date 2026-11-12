# S4. Revisión del contenido final y entrega de la sección

Sección: `curso/S4_numericos_integracion/` — M13 (Métodos numéricos, solo A) y AX (Anexos de deducciones).

## Nota de sustitución

Esta revisión la hace Claude Opus 5.5 (`claude-opus-5-5`, esfuerzo bajo) en sustitución de `claude-sol` (gpt-6.1-sol), supervisor previsto para el paso 4 del plan maestro. Motivo: cuota de `claude-sol` agotada; sustitución por decisión del usuario del 25-10-2026. El alcance y los entregables son los mismos del paso 4 (plan maestro §3). Solo se modifican archivos de `curso/S4_numericos_integracion/`.

## Plan de revisión

**Insumos leídos:** `curso/00_plan_maestro.md`, `curso/guia_libreto.md`, `prop_e.md` (completo), `revision_final_prop_e.md`; en la sección, `M13_libreto.md`, `M13_bitacora_luna.md`, `M13_revision_haiku.md`, `AX_libreto.md`, `AX_bitacora_luna.md`, `AX_revision_haiku.md` y `calc/`.

**Criterios.**
1. Fidelidad a prop_e: M13 solo A con sus cuatro temas (Monte Carlo GUM-S1 frente a linealización en calibración inversa; salidas múltiples GUM-S2; bootstrap por la agrupación del diseño; Huber frente a OLS) y una sola práctica integradora; AX con los trece identificadores de guía §7, sin prácticas ni evaluación (prop_e §9). Exclusiones de §6 (ISO 13528, z, ζ, Mandel, PCR/PLS, Allan, GGMR con `V_xy ≠ 0`, KCRV combinado, protocolo BIPM.QM-K1/KCDB).
2. Corrección estadística y metrológica: fórmulas, signos, unidades, supuestos.
3. Referencias: cada concepto o fórmula con fuente externa; numerales comprobados en `docs/`; fuentes ausentes marcadas «no disponible en docs/» y sin numeral; prop_e solo como alcance.
4. Formato libreto (guía §1–§2): prosa oral, etiquetas permitidas, marcador «[PRÁCTICA — fase de ejercicios]» por cada práctica de prop_e y nada más.
5. Coherencia de sección: notación (guía §4), prerrequisitos, remisiones M13 → AX, sin duplicaciones ni contradicciones.
6. Errores críticos y señales de escalamiento presentes donde corresponde.

**Orden:** M13 primero (consumidor), después AX (comprobando que cada remisión de M13 y de M0–M12 tiene destino), y por último coherencia entre ambos.

**Verificación de cálculos:** ejecutar `curso/.venv/bin/python -I calc/M13_ejemplos.py` y cada `calc/AX_*.py`; comparar cifra por cifra con el libreto; recalcular a mano los ejemplos cortos de AX (AX.1–AX.11) y comprobar órdenes de magnitud de AX.12 contra valores conocidos (EWMA λ = 0,2, L = 3: ARL₀ ≈ 562; CUSUM unilateral k = 0,5, h = 5: ARL₀ ≈ 930).

**Verificación de referencias:** `pdftotext -layout` de GUM, GUM-S1, GUM-S2 e ISO/TS 28037 en `docs/`; `grep` del encabezado de cada numeral citado y lectura del texto donde el contenido es dudoso.

## Hallazgos por capítulo

| Id | Capítulo | Ubicación | Severidad | Problema | Corrección |
|---|---|---|---|---|---|
| S-01 | M13 | Escena A1, `[PIZARRA]` de ∇gᵀV∇g y `[NOTA AL INSTRUCTOR]` siguiente | mayor | La ley de propagación con covarianzas se cita como [GUM 5.1.2]; ese numeral es el caso de entradas no correlacionadas. La forma con covarianzas está en GUM 5.2.2 (verificado). | Cambiar a [GUM 5.2.2] en ambos lugares y declarar 5.2.2 en Referencias. |
| S-02 | M13 | Escena A1 (tras «[ERROR CRÍTICO]» de entradas correlacionadas) y Escena A4 (tras «[ERROR CRÍTICO]» de Huber) | menor | Línea suelta «>» tras un párrafo en prosa: residuo de la corrección R03 de Haiku que rompe el bloque de acotaciones. | Sustituir por línea en blanco. |
| S-03 | M13 | Escena A4, intercepto de Huber | menor | El libreto dice 0,36428572; el script da 0,36428571. | Usar la cifra del script. |
| S-04 | AX | AX.3, ejemplo simulado | mayor | «Las tres cantidades se reproducen en .»: falta el script; la frase queda rota y sin trazabilidad. | «… en `calc/AX_03.py`.» |
| S-05 | AX | AX.3, triangular y cierre del anexo | menor | La distribución triangular se presenta en GUM 4.3.9; solo se citaba 4.4.6 (ejemplo de la figura 2 b). | Añadir [GUM 4.3.9]. |
| S-06 | AX | AX.12, primeras dos citas de Montgomery | menor | Fuente fuera de `docs/` sin la marca «no disponible en docs/» (guía §5); la última cita sí la tenía. | Añadir la marca. |
| S-07 | AX | AX.9, ejemplo simulado | observación | Repite el ejemplo numérico de AX.2 (0,30 común; 0,20 independientes). Es coherente (AX.9 = AX.2 con coeficientes ±1) y lo declara. | Sin cambio: la repetición es deliberada y refuerza la remisión. |
| S-08 | AX | AX.12, ARL por cadena de Markov | observación | 559,679 (EWMA) y 921,016 (CUSUM) con 240 estados; valores de referencia conocidos ≈ 562 y ≈ 930. Diferencia compatible con la discretización, que el libreto ya declara y pide refinar. | Sin cambio. |
| S-09 | M13/AX | Bibliografía externa (Efron–Tibshirani, Huber, Montgomery, JCGM 106, ILAC-G8) | observación | No están en `docs/`; se citan sin numeral y con la marca. Correcto según guía §5. | Sin cambio; queda como pendiente bibliográfico. |

**Comprobaciones sin hallazgo.**
- *Alcance M13:* solo A, ficha lo declara; los cuatro temas de prop_e §5 están narrados con ejemplo numérico; un único marcador de práctica (la integradora evaluable), sin enunciado ni solución. No aparece ningún tema excluido por §6.
- *Alcance AX:* AX.1–AX.13 con los contenidos de guía §7; AX.8 limitado a `V_xy = 0`; AX.9 a referencia común (sin KCRV combinado); sin prácticas ni rúbricas; declara que no se evalúa.
- *Cálculos:* todas las cifras de M13 (A1–A4) coinciden con `calc/M13_ejemplos.py` (salvo S-03); A2 usa ya la covarianza agrupada por día (corrección del hallazgo crítico R01 de Haiku, verificada). AX.1–AX.13 coinciden con sus scripts; AX.2, AX.4, AX.6, AX.7, AX.10 y AX.11 recalculados a mano. El intervalo bootstrap de A3 es coherente con la covarianza agrupada (semiancho/1,96 ≈ 4·10⁻⁵ frente a u(b) ≈ 4,7·10⁻⁵).
- *Referencias verificadas con `pdftotext`:* GUM 4.3.7, 4.3.9, 4.4.5, 4.4.6, 5.1.2, 5.2.2, G.4 (ec. G.2b), H.5; GUM-S1 5.3–5.6, 5.9, 5.10, 5.11, 6.4.8.4, 7.2.2 (M ≥ 10⁴/(1 − p)), 7.3, 7.5–7.8, 7.9.2–7.9.4; GUM-S2 5.2, 5.3, 6.2, 7.6; ISO/TS 28037 5.2.2, 5.5, 5.6, 5.8.1, 10, 10.1, 10.2. Ninguno inventado. prop_e se cita en AX solo como alcance.
- *Coherencia:* notación de guía §4 (`x̂ = (y − a)/b`, corrección `x̂ − y`, `s_r`, `s_entre`, `d`, `n`) igual en M13 y AX; M13 remite a AX.2, AX.5, AX.9 y AX.13, todos presentes y con M13-A como consumidor en la tabla de AX; la regla de ensayos de M13-A1 y el error de Monte Carlo de AX.13 no se contradicen.
- *Errores críticos y escalamiento:* presentes en cada escena de M13 y en cada anexo (dependencia ignorada, independencia con patrón compartido, eliminar datos para cumplir, extrapolar).

## Correcciones aplicadas

| Hallazgo | Cambio | Ubicación |
|---|---|---|
| S-01 | `[GUM 5.1.2]` → `[GUM 5.2.2]` en la pizarra de ∇gᵀV∇g y en la nota al instructor; Referencias: «numerales 5.1.2 y 5.2.2 verificados». | `M13_libreto.md`, Escena A1; Referencias del capítulo |
| S-02 | Eliminadas dos líneas «>» sueltas. | `M13_libreto.md`, Escenas A1 y A4 |
| S-03 | 0,36428572 → 0,36428571. | `M13_libreto.md`, Escena A4 |
| S-04 | Añadido `calc/AX_03.py`. | `AX_libreto.md`, AX.3 |
| S-05 | `[GUM 4.4.6]` → `[GUM 4.3.9; GUM 4.4.6]`; cierre `[GUM 4.3.7; GUM 4.3.9; GUM 4.4.5–4.4.6]`. | `AX_libreto.md`, AX.3 |
| S-06 | Añadido «no disponible en docs/» a dos citas de Montgomery. | `AX_libreto.md`, AX.12 |

No se tocaron cálculos: los scripts de `calc/` quedan sin cambios y reproducen todas las cifras del libreto.

## Estado de entrega

**Sección S4 entregada** para el paso 5 (revisión Opus), fase solo contenido. M13 y AX cumplen alcance, cálculos, referencias, formato y coherencia tras las seis correcciones; no quedan hallazgos críticos ni mayores abiertos.

Pendientes que no bloquean la entrega: (1) verificación bibliográfica local de Efron–Tibshirani, Huber, Montgomery, JCGM 106 e ILAC-G8 (fuera de `docs/`, citados sin numeral); (2) numerales de Crowder 2020 y Hahs-Vaughn y Lomax en AX, citados sin numeral; (3) desarrollo de la práctica integradora de M13 en la fase de ejercicios, con datos, solución revisada y rúbrica (si no se preparan, prop_e §5 M13 indica que el método no se imparte); (4) contraste opcional del ARL de AX.12 con una malla más fina.
