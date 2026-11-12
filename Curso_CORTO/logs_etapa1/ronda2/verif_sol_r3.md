# Verificación de cierre de la etapa 1 — tras verif_sol_r2.md

Fecha: 2026-11-11. Directorio revisado: `Curso_CORTO/`. Los localizadores `archivo:línea` son relativos a este directorio y corresponden al estado comprobado en esta revisión.

## Veredicto

**ETAPA 1 NO CERRADA.**

Las cuatro instrucciones heredadas de los scripts M06 están corregidas y las delimitaciones pendientes de la observación 5.6 están aclaradas. **Los 12 scripts de `calc/` terminan con código 0 y stderr vacío; los cinco HTML se regeneran idénticos.** Sin embargo, **sigue sin resolverse la localización impresa del HTML de M03**, señalada expresamente en `verif_sol_r2.md:64,135`. Por tanto, F07 no puede cerrarse en su totalidad ni certificarse que no quedan rutas documentales incorrectas en `calc/`.

No se modificó ningún archivo preexistente. La única entrega persistente de esta revisión es este informe.

## 1. Alcance y método

- Lectura de `logs_etapa1/ronda2/verif_sol_r2.md` y de la sección «Cierre tras verif_sol_r2.md» de `logs_etapa1/ronda2/cambios_r3.md:16–19`.
- Comprobación de esos pendientes y del contexto inmediato de los pasajes modificados; no se reabrió la auditoría curricular ni la cobertura del PDF ya comprobadas en la ronda anterior.
- Barrido de rutas locales en los cinco libretos y en `calc/`; se incluyó como comprobación auxiliar `M05_practicas_luna.md`. Se contrastaron destinos explícitos, componentes de comandos, entradas y salidas de los programas y atributos `href`/`src` de los HTML. Las abreviaciones bibliográficas `c05.pdf`, `c06.pdf`, `c08.pdf` y `c09.pdf` de M03 se resolvieron dentro de la serie indicada en su bibliografía; las fuentes expresamente no suministradas no se trataron como archivos locales prometidos.
- Ejecución de los 12 `.py` en una copia temporal, con el intérprete solicitado y `-I`, sin `-O`, en procesos independientes y con límite de 120 s por script. Se comprobaron los SHA-256 de los scripts copiados antes de ejecutarlos y la integridad de los originales.
- No se verificó la disponibilidad de las páginas web ni se hizo revisión visual en navegador. La ejecución del estudio CALAIRE no se interpreta como validación histórica de sus datos o supuestos.

## 2. Estado de los pendientes

| Pendiente | Resultado | Evidencia actual |
|---|---|---|
| F07: cuatro cabeceras M06 | **Resuelto** | `calc/M06_RR_CALAIRE.py:8`, `calc/M06_ejemplos.py:4`, `calc/M06_practicas_luna.py:3` y `calc/M06_practica_I_grafico.py:4–5` usan `../Curso_COMPLETO/curso/.venv/bin/python -I calc/<script>.py`. Tanto el intérprete como los scripts existen desde la raíz de `Curso_CORTO/`. |
| F07: localización impresa del HTML M03 | **Pendiente** | `calc/M03_practicas_luna.py:138` sigue imprimiendo el nombre sin `calc/`; el destino real se fija junto al script en `:94`. Véase H01. Este pendiente no figura entre las correcciones declaradas en la sección nueva de `cambios_r3.md`, pero sí estaba incluido en la condición de cierre anterior. |
| 5.6: alcance en M02 | **Resuelto** | `M02_libreto.md:128` remite los grados de libertad a M3/M4 y limita la exclusión al análisis de residuos de un modelo de calibración y a la incertidumbre en ambos ejes. Se conserva la instrucción vecina de escalar, sin presentar los grados de libertad como excluidos del curso completo. |
| 5.6: consulta de tablas en M06-I | **Resuelto** | `M06_libreto.md:140` declara «Aquí usamos esas tablas como consulta; su deducción queda fuera del alcance». Es coherente con los cocientes F y denominadores explicados en `:134–138` y no excluye su aplicación. |
| 5.6: denominadores en M06-A | **Resuelto en contenido** | `M06_libreto.md:211` excluye la deducción de las esperanzas y afirma expresamente que su aplicación no está excluida. Conserva el modelo condicional y los denominadores del párrafo, coherentes con `:203,207,213–215`. Queda una errata de puntuación menor, H02. |

No se observó pérdida ni duplicación del contenido inmediato de los pasajes comprobados. La errata H02 no cambia la delimitación estadística; el impedimento de cierre es H01.

## 3. Hallazgos

### H01 — F07 residual: la salida de M03 anuncia un destino inexistente desde la raíz del curso

**Archivo:línea:** `calc/M03_practicas_luna.py:138`. Destino efectivo: `calc/M03_practicas_luna.py:94`.

La ejecución desde la raíz de la copia temporal reproduce literalmente:

```text
I_salida_grafica=M03_practica_I_probabilidad.html
```

No existe `M03_practica_I_probabilidad.html` en esa raíz. El programa escribe el archivo mediante `Path(__file__).with_name(...)`, de modo que el destino real es **`calc/M03_practica_I_probabilidad.html`**, que sí existe y se regeneró correctamente. El libreto ya remite al destino correcto en `M03_libreto.md:220`.

No es un fallo de cálculo ni de generación: es una salida documental de localización incorrecta para el directorio de ejecución usado en la verificación. Es el mismo residuo señalado en `verif_sol_r2.md:64` y requerido para cerrar F07 en `:135`. **Impide certificar la condición solicitada de ausencia de rutas rotas en libretos y `calc/`.** Falta armonizar esa salida con su destino real; no se aplicó ninguna modificación.

### H02 — Errata menor en el pasaje modificado de M06-A

**Archivo:línea:** `M06_libreto.md:211`.

El final del párrafo contiene «una tabla de F memorizada no resuelve un diseño distinto La deducción de esas esperanzas…»: falta un punto entre «distinto» y «La». La nueva delimitación se entiende y distingue correctamente deducción y aplicación, pero el empalme de las frases quedó sin puntuación. **No bloquea por sí solo el cierre** ni constituye un defecto del modelo estadístico.

## 4. Resultado del barrido de rutas

- Los destinos locales comprobados en los cinco libretos y en el registro auxiliar `M05_practicas_luna.md` existen, incluidos los PDF bibliográficos, las remisiones al curso completo, los dos libros Excel y los componentes de los comandos documentados.
- Las cuatro instrucciones de ejecución de M06 ya no contienen las ubicaciones heredadas inexistentes. Conservan `-I` y apuntan al intérprete y al script correspondientes.
- Las entradas Excel de `calc/M06_RR_CALAIRE.py:16–17`, `calc/M06_practicas_luna.py:12–13` y `calc/M06_practica_I_grafico.py:12–14` resuelven dentro del curso; su lectura y la escritura de las salidas se comprobaron mediante ejecución.
- Los cinco HTML no contienen dependencias mediante atributos `href` o `src`.
- **Único residuo de localización detectado en este barrido: H01.** La correcta ruta del libreto no corrige la ruta que imprime el programa.

## 5. Ejecución de los 12 scripts

Copia utilizada: `/tmp/curso_corto_verif_sol_r3_d6nhpjbi/Curso_CORTO/`.

Intérprete: `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python`, Python **3.14.7**, siempre con **`-I`**. Directorio de trabajo: raíz de la copia temporal. Los originales no se ejecutaron en su ubicación de entrega.

| Script | Código de salida | stderr | Tiempo (s) |
|---|---:|---|---:|
| `calc/M02_examples.py` | 0 | vacío | 0,171 |
| `calc/M02_practicas_luna.py` | 0 | vacío | 0,194 |
| `calc/M03_ejemplos.py` | 0 | vacío | 1,094 |
| `calc/M03_practicas_luna.py` | 0 | vacío | 1,064 |
| `calc/M04_ejemplos.py` | 0 | vacío | 1,375 |
| `calc/M04_practicas_luna.py` | 0 | vacío | 1,361 |
| `calc/M05_diseno.py` | 0 | vacío | 1,060 |
| `calc/M05_practicas_luna.py` | 0 | vacío | 1,070 |
| `calc/M06_RR_CALAIRE.py` | 0 | vacío | 1,268 |
| `calc/M06_ejemplos.py` | 0 | vacío | 1,033 |
| `calc/M06_practica_I_grafico.py` | 0 | vacío | 0,612 |
| `calc/M06_practicas_luna.py` | 0 | vacío | 0,948 |

**12/12 ejecuciones satisfactorias**, sin timeout ni aserciones fallidas.

Antes de ejecutar se retiraron exclusivamente de la copia temporal los cinco HTML existentes. Se regeneraron y sus SHA-256 coinciden con los entregados: `M02_practica_B_grafico.html`, `M02_practica_I_grafico.html`, `M02_practica_A_grafico.html`, `M06_practica_I_residuos.html` y `calc/M03_practica_I_probabilidad.html`: **5/5 idénticos**.

Evidencia temporal: `/tmp/curso_corto_verif_sol_r3_d6nhpjbi/results.json`, `paths.json`, `source_before.json` y archivos individuales `*.stdout.txt` / `*.stderr.txt`. No son dependencias permanentes del curso.

Los SHA-256 de los **57 archivos preexistentes** permanecieron iguales durante la revisión y antes de escribir este informe.

## 6. Condición restante de cierre

No hace falta repetir las correcciones de las cuatro cabeceras M06 ni las delimitaciones de 5.6. **Falta corregir la localización que imprime `calc/M03_practicas_luna.py:138`** para que coincida con `calc/M03_practica_I_probabilidad.html`. H02 es una observación editorial menor.

**ETAPA 1 NO CERRADA por el residuo documental H01 de F07; ejecución completa y reproducción de HTML satisfactorias.**
