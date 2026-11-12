# Verificación etapa 2 — M02

**Veredicto: CON OBSERVACIONES.** Un criterio no se cumple: quedan restos del nivel A en `calc/M02_examples.py`. Corregido eso, el módulo cumple lo pedido.

Alcance: `M02_libreto.md`, `calc/M02_examples.py`, `calc/M02_practicas_luna.py`, `M02_practica_B_grafico.html`, `M02_practica_I_grafico.html`, contra `00_plan_corto.md` (Etapa 2) y `logs_etapa2/cambios_M02.md`. No se editó ningún archivo del curso.

## Criterios

| Criterio | Resultado | Evidencia |
|---|---|---|
| Nivel A retirado sin menciones residuales | **No cumple** | `calc/M02_examples.py:89-106` (bloque «A» sin uso en el libreto; ver hallazgo 1). Libreto y HTML: sin menciones. |
| Agenda de sesión de 120 min | Cumple | `M02_libreto.md:3-12`: 10 + 47 + 25 + 15 + 23 = 120 min; coincide con la fila de Sesión 1 del plan. |
| Práctica B en clase | Cumple (con matiz) | Agenda (`:9`) y plan. El encabezado del bloque B (`:126`) no indica «en clase» ni 25 min (observación 1). |
| Práctica I partida en clase y tarea, con soluciones | Cumple | En clase: `:190-192` (solución docente en `:192`). Tarea: enunciado `:194-198`, solución `:200`, criterio de logro `:204`. |
| Revisión de la tarea anterior (salvo M02) | Cumple | M02 no la tiene y lo dice explícitamente en `:20`. |
| Apertura de 10 min en M02 | Cumple | `:14-20`. |
| Tareas específicas del módulo | Cumple | Ficha (`:22-32`), punto de partida con $e=y-x$ (`:36`), escalamiento (`:146-148`), cierre (`:206-211`). |
| Scripts M02 corren con `-I` en copia temporal | Cumple | `M02_examples.py` y `M02_practicas_luna.py`: exit 0 (copia en `/tmp/verif_m02/Curso_CORTO`). |
| Salidas coinciden con el libreto | Cumple | Ver tabla de cifras abajo. HTML regenerados idénticos a los del repositorio. |
| Temas PDF M2–M6 (M2: resumen, gráficos, atípicos) | Cumple | Resumen y cuantiles: B2–B3. Gráficos: B2, B5, I1. Atípicos: B6 (regla IQR, sin eliminación automática). |
| Referencias a fuentes del repositorio | Cumple | Las rutas `../Curso_COMPLETO/docs/…` y `../Curso_COMPLETO/prop_e.md` existen. |
| Grubbs/Dixon en M4 (puente de B6) | Cumple | `M04_libreto.md` menciona Grubbs 9 veces. |
| Sin referencias a M1, M7, M8, M10–M12 o AX | Cumple | Búsqueda sin coincidencias en `M02_libreto.md`. |

## Cifras comprobadas (libreto vs. salida de scripts)

- B, 8 lecturas: media = mediana = 100,15; $s^2=0{,}06$; $s=0{,}245$; $s/\sqrt8=0{,}0866$; $Q_1=99{,}975$; $Q_3=100{,}325$; CV = 0,2446 %. Histograma 2; 3; 3 (frecuencias 0,25; 0,375; 0,375). Coincide.
- B, 6 pares: $s^2(y)=0{,}05767$, $s^2(x)=0{,}032$, $s^2(e)=0{,}01767$, cov $=0{,}004$; reparto 55,5 %; 30,6 %; 13,9 %. Coincide.
- B, cero: media 0 y 0,06 truncado; 0,117 sin redondeo intermedio; 0 con redondeo a entero. Coincide.
- B práctica (12 pares): $y$: media 100,05, $s^2=0{,}07909$, $s=0{,}28123$, rango 0,9, $Q_1=99{,}875$, $Q_3=100{,}225$. $e$: media 0,05, $s^2=0{,}02091$, $s=0{,}14460$, rango 0,5, $Q_1=-0{,}025$, $Q_3=0{,}125$. Medias por día −0,05; 0,05; 0,15. Cajas y 1; 2; 3; 3; 2; 1 en el histograma. Coincide.
- I escena 1: MAD de {0,1; 0,2; 0,2; 0,3; 0,9} = 0,1. Coincide.
- I escena 2: $\hat a=0{,}080$, pendiente $0{,}002075$, $\hat b=1{,}002075$, predicciones 0,246; 0,412; 0,578; 0,744; 0,910. Coincide.
- I práctica (60 pares): celda día×nivel $s=0{,}0516398$ en las 15 celdas; agrupada por día $s=0{,}23664$; medias diarias 0,50; 0,58; 0,66; MAD 0,20; por nivel medias 0,26…0,90 con MAD 0,06; $\hat a=0{,}100$, pendiente $0{,}002$; residuos −0,14…0,14. Coincide.

## Hallazgos

1. **Restos del nivel A en `calc/M02_examples.py:89-106`** (criterio no cumplido). El bloque de grupos con sesgos opuestos y valor influyente, el ejemplo de tamaños desiguales y las etiquetas `"A group 1"`, `"A combined"`, `"A unequal group sizes"` y `"A combined plus influential"` son de A y no los usa el libreto de B/I. Este archivo no aparece en `cambios_M02.md`, así que no se tocó en la etapa. Acción: retirar `:89-106` (incluida la aserción `:100`, `0.8 / 6`), o al menos quitar las etiquetas «A» y justificar su uso en B/I.
2. **Registro de cambios con líneas desfasadas** (`logs_etapa2/cambios_M02.md:5-9`). Cita `M02_libreto.md:171-184` para la práctica I (en realidad está en `:188-204`), `:182-223` para retirar A (en realidad es el cierre y las referencias, `:206-225`) y `:1-41` para la agenda (`:1-20`). Corregir las referencias.
3. **Bloque B sin marcador de clase** (`M02_libreto.md:126`). El encabezado `[PRÁCTICA] B` no indica «en clase, 25 min», a diferencia de la práctica I. La agenda sí lo indica. Sugerencia: añadir «(en clase, 25 min)».
4. **Tiempo de narración sin medir frente a lo planificado.** El registro estima 33,9 min de narración frente a los 47 min del plan (`cambios_M02.md`, sección «Palabras y minutos»). No es un error, pero el plan asigna 47 min y el libreto no dice dónde caen los 13 min restantes (pausas, demostraciones). Opcional: aclararlo en la agenda.

## Pendiente antes de APROBADO

- Corregir el hallazgo 1 y volver a ejecutar `calc/M02_examples.py` con `-I` (debe seguir saliendo con código 0 y sin etiquetas «A»).
- Los hallazgos 2–4 son observaciones menores.
