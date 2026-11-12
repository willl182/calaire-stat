# S4. Métodos numéricos y anexos — índice de la sección entregada

Fase: solo contenido. Revisión de entrega: [S4_revision_sol.md](S4_revision_sol.md); revisión Opus: [S4_revision_opus.md](S4_revision_opus.md).

## Capítulos

| Capítulo | Archivo | Niveles | Escenas | Marcadores de práctica pendientes | Anexos a los que remite |
|---|---|---|---|---|---|
| M13. Métodos numéricos (solo A) | [M13_libreto.md](M13_libreto.md) | A (sin B ni I, declarado en la ficha) | A1 Propagación lineal y Monte Carlo en calibración inversa; A2 Pendiente, intercepto y correcciones como salidas conjuntas; A3 Bootstrap por bloques del diseño; A4 Huber frente a OLS | 1: «Práctica integradora evaluable de métodos numéricos» | AX.2, AX.4, AX.5, AX.9, AX.13 |
| AX. Anexos de deducciones | [AX_libreto.md](AX_libreto.md) | Primer uso: B (AX.1, AX.3, AX.4), I (AX.2, AX.5–AX.7, AX.9–AX.11), A (AX.8, AX.12, AX.13) | Una escena por anexo, AX.1–AX.13 (guía §7) | Ninguno (los anexos no tienen práctica ni se evalúan, prop_e §9) | — (recibe remisiones de M01–M13) |

## Datos usados

| Capítulo | Datos | Rótulo | Script |
|---|---|---|---|
| M13-A1 | Entradas y, a, b normales conjuntas, corr(a,b) = −0,60; 400 000 ensayos, semilla fija; validación GUM-S1 §8 (δ = 0,05) | simulado | `calc/M13_ejemplos.py` |
| M13-A2, A3 | 6 días × 6 niveles (40–440 nmol/mol), efecto común por día; covarianza por promedio de rectas diarias (ν = 5), contrastada con la OLS clásica; 20 000 réplicas bootstrap por día | simulado | `calc/M13_ejemplos.py` |
| M13-A4 | 8 niveles (20–370 nmol/mol), última respuesta alterada +8,0 nmol/mol de forma declarada; Huber con c = 1,345·MAD/0,67449 (≈ 0,276) y tabla de sensibilidad a c | simulado (alteración deliberada) | `calc/M13_ejemplos.py` |
| AX.1–AX.13 | Valores numéricos cortos para cada deducción | simulado | `calc/AX_01.py` … `calc/AX_13.py` |

Ningún dato es propio de CALAIRE ni se atribuye al SRP 55 o al Level 2.

## Estado

Revisión Opus atendida: 17 hallazgos O-01 a O-17 aplicados (6 mayores, 11 menores); ver «Correcciones tras la revisión Opus» en S4_revision_sol.md. Sin hallazgos críticos ni mayores abiertos. Antes: S-01 a S-06.

## Pendientes

1. Fase de ejercicios: práctica integradora de M13 (datos, enunciado, solución revisada, rúbrica por apartado).
2. Verificación local de fuentes fuera de `docs/`: Efron y Tibshirani 1993, Huber 1981, Montgomery, JCGM 106, ILAC-G8.
3. ~~Numerales de Crowder 2020 y Hahs-Vaughn en AX~~ — cerrado (O-14).
