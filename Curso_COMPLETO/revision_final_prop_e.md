# Revisión final de la propuesta E

**Documento:** [prop_e.md](prop_e.md), versión final del 24 de octubre de 2026 (después de los ajustes de [obs](ajustes_obs_prop_e.md), la [redacción](correcciones_redaccion_prop_e.md), la [evaluación](eval_calidad_prop_e.md) y los [ajustes de la evaluación](ajustes_eval_prop_e.md)).

## Veredicto

**Aprobable como propuesta curricular.** Cumple el enfoque: es un curso de estadística aplicado a la fotometría de ozono y al SRP. Los títulos y las competencias son estadísticos, y el SRP 55, el Level 2, BIPM.QM-K1 y el F-PSMT-01 aparecen como casos. Todavía **no está lista para impartirse**, y la propia propuesta lo declara: faltan los paquetes B, C y D y los expedientes por tema (§9 y §10).

## Comprobaciones

| Criterio | Resultado |
|---|---|
| Objetivos con la forma «competencia estadística + caso» | Cumple en M0–M13 |
| sup_obs: E_n, KCRV acotado, GGMR definido, Allan verificable, falta de ajuste en general | Cumple (M9, M7, §6) |
| obs1/obs2: el básico no ejecuta el ANOVA (recibe las componentes), t en M3-B, F en I, orden M9 → M12 | Cumple (M3, M6, §4) |
| Exclusiones (ISO 13528, z, ζ, Mandel, PCR/PLS, KCDB) | Cumple (§6) |
| Ningún tema queda como «solo lectura», «para mostrar» u «opcional» | Cumple; las inclusiones condicionadas tienen un criterio verificable (Allan, bloques cruzados GGMR, KCRV combinado) |
| Demostraciones en los anexos, prácticas de aplicación | Cumple (§9) |
| Fórmulas revisadas | Correctas: `u²_prec(ē) = τ̂²/d + σ̂²/(d·n)`; `E_n = Δ/√(U₁² + U₂²)`; `u²(Δ)` con covarianza; `e = a + (b − 1)x + ε`; `k = t(0,975; ν_eff)`; Welch–Satterthwaite limitado a componentes independientes |
| Otros archivos | Sin cambios (prop_a–d, obs, sup_obs, casos_taller) |

## Observaciones pendientes (menores)

1. **Caso D-B frente a M2-A.** La comparación de `e` con `|e|` en el caso R&R aparece como práctica de A en M2. En la tabla de casos, D-B la asigna al básico. Conviene decidir el nivel. Propuesta: el básico calcula `media(|e|)` frente a `|media(e)|` (concepto de M12-B), y A analiza la sensibilidad de las conclusiones (M2-A). Además, la columna «ANOVA multifactor» del caso D no corresponde al básico.
2. **Notación de M6-B.** La convención define `s_r` y `s_entre`, pero la fórmula usa `σ̂` y `τ̂`. Sería más claro escribir `u²_prec(ē) = s²_entre/d + s²_r/(d·n)`, que además es la forma acordada en sup_obs, y poner `σ̂`/`τ̂` entre paréntesis.
3. **Práctica de M6-B.** Pide la «U del promedio», pero la fórmula da solo la contribución de precisión. Hay que indicar el `k` del ejercicio y que es una U parcial: el presupuesto completo se hace en M8.
4. **Allan repetido.** El criterio aparece completo en M3-A y en §6. Basta con dejarlo en §6 y remitir a él desde M3-A.
5. **Densidad de M9-A.** La distinción entre referencia común (BIPM-SRP27) y KCRV combinado es correcta, pero el párrafo es largo para una sola viñeta. Puede separarse en dos subviñetas.

Ninguna de estas observaciones cambia el alcance ni los acuerdos. Son ajustes de coherencia que pueden hacerse en la próxima versión.

## Próximos pasos

1. Resolver las observaciones 1–3 (las 4–5 son de forma).
2. Ejecutar las tareas de preparación externas de [ajustes_eval_prop_e.md](ajustes_eval_prop_e.md): coeficientes del caso B, paquetes C y D y expediente por tema.
3. Con el contenido cerrado, estimar las horas.

## Ajustes aplicados (24 de octubre de 2026, a pedido del usuario)

| Pendiente | Cambio en `prop_e.md` |
|---|---|
| 1. Caso D-B frente a M2-A | Básico: `media(|e|)` frente a `|media(e)|` (concepto de M12-B). M2-A: sensibilidad de las conclusiones al usar `e` o `|e|`. La columna del caso D distingue descriptiva con signo (B) de ANOVA multifactor (I y A). |
| 2. Notación de M6-B | `u²_prec(ē) = s²_entre/d + s²_r/(d·n)`, con `s_entre = τ̂` y `s_r = σ̂`. |
| 3. Práctica de M6-B | `U_prec = k·u_prec(ē)` con el `k` que declara el ejercicio; se indica que es una U parcial y que el presupuesto completo se construye en M8. |
| 4. Allan repetido | Resuelto con la exclusión (ver abajo). |
| 5. Densidad de M9-A | Separado en subviñetas. |

**Temas excluidos por decisión del usuario** (antes eran inclusiones condicionadas): la varianza de Allan, GGMR con covarianza cruzada entre ejes no nula (`V_xy ≠ 0`) y el grado de equivalencia frente a un KCRV combinado al que contribuye el participante. Se agregaron a «Fuera del curso» (§6). M7-A y M9-A trabajan solo con `V_xy = 0` y referencia común, y §10 ya no incluye la condición de Allan. Por eso dejan de aplicar las tareas externas 2, 6 y 8 de [ajustes_eval_prop_e.md](ajustes_eval_prop_e.md).
