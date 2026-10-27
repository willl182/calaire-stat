# Bitácora Luna — prácticas M12

## Plan y alcance

- Alcance de `prop_e.md` §5, M12: B calcula indicadores de errores de ambos signos; I añade límites de confianza con chi-cuadrado y t, colas, cambio de escala, dispersión del cero bajo hipótesis expresas; A trata dependencia, mezcla de periodos y efectos comunes de trazabilidad, distinguiendo conformidad individual y desempeño agregado.
- Los conjuntos de práctica son simulados deterministas y declarados como tales; no se atribuyen a CALAIRE. Unidad: nmol/mol; errores y diferencias relativas se derivan de la referencia indicada. No se exigen gráficos en las prácticas de M12.
- Solo se modificaron bloques de práctica en `M12_libreto.md`, el script propio `calc/M12_practicas_luna.py` y esta bitácora. Referencias, claves, citas existentes, referencias bibliográficas, otros capítulos, guía y revisión final permanecen fuera del alcance. Sin commits.

## Ronda de correcciones Haiku

Hallazgos leídos en `curso/logs/M12_practicas_revision_haiku.md`; se resolvió cada uno:

| Hallazgo | Decisión | Ubicación y resultado |
|---|---|---|
| H-01 | Aplicado | `M12_libreto.md`, práctica A, enunciado y solución: se identifica el mismo monitor X y se evalúan las tres filas posteriores. Errores +2,5, +3,0 y +3,5 nmol/mol; las tres exceden la tolerancia de 2,0 nmol/mol. |
| H-02 | Aplicado | `M12_libreto.md`, solución y decisión operativa A: se declara que la fila 3 anterior (+1,5 %) ya supera el límite de control +1,0 %, y que las filas posteriores también lo superan. La señal no empieza exactamente tras el mantenimiento; se instruye revisar la secuencia completa y fechas, sin atribuir causa. |
| H-03 | Aplicado | `M12_libreto.md`, enunciado A: muestra definida como las seis verificaciones cronológicas completas de una campaña simulada de un único equipo, tres antes y tres después; cobertura explícita, sin otros monitores. Los criterios agregado e individual se vinculan al periodo posterior. |
| H-04 | Aplicado | `calc/M12_practicas_luna.py`: añadida reproducción de ejemplos de escena I (límite chi-cuadrado, límite de AB, intervalo bilateral, cambio de escala y cero), incertidumbre común con n=3, errores individuales posteriores y señales de control antes/después. Salida ejecutada abajo. |
| H-05 | Aplicado | `M12_libreto.md`, enunciados B, I y A: cada práctica enmarca expresamente verificaciones simuladas de analizadores de ozono/SRP o de la red; conserva su origen didáctico y no atribución a CALAIRE. |
| H-06 | Aplicado | `M12_libreto.md`, enunciado B: se sustituye la frase ambigua por la entrega concreta de seis diferencias; se quita la afirmación de escala temporal no representada y se especifica que el orden no representa tiempo ni independencia. |

## Ejecución y resultados finales

Ejecutado con el intérprete del entorno del curso:

```text
curso/.venv/bin/python -I curso/S3_comparacion_decision/calc/M12_practicas_luna.py
```

Resultado: rc=0. El script reproduce B/I: n=6, media firmada 0, media absoluta 2,00 %, s=2,3664 %; errores absolutos 2, 1, 1, 2, 3 y 3 nmol/mol. Para I: χ²(0,10;5)=1,6103, L90(s)=4,1699 %, AB=2,0000 %, AS=0,8944 %, t(0,95;5)=2,0150, L95(AB)=2,7358 %, IC bilateral 95 % de la media [−2,4834; +2,4834] %. Tras la ganancia 1,01, media de magnitudes=2,0200 %. Para el ejemplo de cuatro diferencias: L90=4,1367 %, L95(AB)=2,1794 %, IC bilateral de la media [−2,9052; +2,9052] %; cambio puntual de escala +2,0100 %; cero s₀=0,1581 y 3s₀=0,4743 nmol/mol.

Para A: medias antes/después/conjunta 1,00/3,00/2,00 %; errores individuales posteriores +2,5, +3,0 y +3,5 nmol/mol. Control sobre +1,0 %: antes [falso, falso, verdadero] y después [verdadero, verdadero, verdadero]. Con u_com=0,80 y u_ind=0,60 pp, u(media) para n=3=0,8718 pp (n=2: 0,9055; n=8: 0,8276); covarianza común=0,64 pp². Se mantienen separadas las decisiones individual, agregada y de control; no se infiere causalidad ni se generaliza la muestra de un equipo a la red.

## Comprobaciones

- Se ejecutó el script tras las correcciones, rc=0; los resultados finales anteriores incluyen las magnitudes solicitadas por H-04 y H-01/H-02.
- Se respetaron los límites de edición solicitados; no se tocaron bibliografía ni archivos ajenos a M12/prácticas propias.
- No se generaron gráficos: ninguna práctica M12 exige gráfico según su alcance curricular.
