# Evaluación de obs1 y obs2 con el criterio «estadística aplicada a A»

**Conclusión:** casi todo lo que proponen es estadística, así que van bien encaminadas. El riesgo de que el curso se convierta en un curso del SRP está en cómo se redacten los objetivos de dos o tres puntos, no en los temas elegidos.

## Lo que respeta el criterio

| Punto | Por qué es estadística |
|---|---|
| ANOVA: el básico interpreta las componentes, el intermedio ejecuta el análisis | Es el modelo de componentes de varianza. El SRP solo aporta los datos. |
| U del promedio con y sin la componente entre días (obs2.1) | Es correcto, y la idea de «no aplicar un divisor automático» es justo la competencia estadística que se busca: u²(x̄) = s²_entre/d + s²_r/(d·n). Conviene escribir así el objetivo. |
| t en básico y F en intermedio (obs2.2) | Ordena las herramientas según cuándo se necesitan, no según el instrumento. Bien. |
| Falta de ajuste: hace falta replicar al mismo valor de referencia | Es un supuesto del diseño experimental. Bien. |
| Fuera ISO 13528, z, ζ y Mandel | Recorte razonable. |
| Allan, condicionado a que haya series | Es varianza de series temporales. El criterio se puede verificar. |
| Corrección de obs2 sobre E_n | Es más precisa que la de obs1, y es la que debe quedar: el problema no es E_n, sino suponer independencia sin justificarla. |

## Dónde se acerca a ser un curso «de A»

1. **E_n del Level 2 frente al SRP 55 (obs1).** «Muestra si el Level 2 es compatible con su propia calibración» es una conclusión sobre el instrumento. El objetivo debería ser estadístico: *comparar dos resultados con incertidumbres correlacionadas y decidir qué hipótesis contrasta esa comparación*. El caso Level 2 frente al SRP 55 queda como ejemplo.
2. **BIPM.QM-K1 y los grados de equivalencia.** Hay que acotarlo a la estadística: la diferencia frente al valor de referencia (KCRV) y su incertidumbre, que incluye la correlación cuando el participante contribuye al KCRV. Ese contenido enlaza muy bien con la covarianza del punto anterior. Lo que no debe entrar es cómo funciona la comparación clave, su protocolo o la KCDB.
3. **«GGMR» no está definido.** En un curso de estadística hay que nombrar el método (qué estimador o qué regresión es) y no solo la sigla.
4. **Allan «para elegir el tiempo de promedio del seguimiento del patrón».** La competencia es *identificar regímenes de ruido y el τ óptimo en una serie*. La condición para incluirlo debería ser «existen series adecuadas» (del SRP 55, del Level 2 o de otra fuente del laboratorio), no solo series del SRP 55.
5. **La referencia al F-PSMT-01.** Sirve como fuente de datos, pero el argumento de la falta de ajuste debe plantearse en general: el supuesto de réplicas y qué hacer cuando no se cumple. El formato concreto queda como el caso que lo ilustra.

## Coherencia entre las dos observaciones

No se contradicen. obs2 añade lo de la F en intermedio, mantiene el orden M9 → M12 y afina lo de E_n. El cierre de obs2 («base A, básico acotado…») sirve como conclusión consolidada.

**Recomendación:** al consolidar, redacta cada objetivo como *competencia estadística + caso de A*. Por ejemplo: «Estimar u de una diferencia con covarianza (caso: Level 2 frente al SRP 55)». Así el temario lo define la estadística y A aporta los datos.
