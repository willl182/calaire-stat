# Verificación etapa 2 — M03

**Veredicto: CON OBSERVACIONES**

No hay errores numéricos ni de agenda. Quedan una inexactitud en el log de cambios, un comentario residual, un encabezado sin la etiqueta «en clase» y una pérdida de cobertura del PDF en M3 que conviene decidir.

## Comprobaciones que pasan

- **Nivel A retirado.** No hay «Nivel A», «práctica A», «Escena A…» ni rótulos A en `M03_libreto.md`. La ficha (`M03_libreto.md:21-29`) solo lista B e I.
- **Agenda de 120 min.** `M03_libreto.md:5-11`: 15 + 49 + 25 + 15 + 16 = 120. La narración B + I es 49 min (`:8`), coherente con `00_plan_corto.md` (sesión 2).
- **Práctica B en clase.** Presente (`M03_libreto.md:139-155`), con enunciado y solución docente. Ver observación 2 sobre su etiqueta.
- **Práctica I partida.** Inicio en clase 15 min (`:223-225`) y tarea (`:227-235`), cada una con enunciado. La solución docente de la tarea está en `:231`.
- **Revisión de la tarea anterior.** `M03_libreto.md:15-17` revisa la práctica I de M02 (60 pares, tres días, cinco niveles, cuatro lecturas). Coincide con `M02_libreto.md:196`. M02 queda sin revisión, como se pidió.
- **Tareas del módulo.** Conversiones de incertidumbre (`:145`), semiancho t con 15 gl (`:147`), promedio con componente común (`:149`), serie con deriva (`:151`), gráfico de Blom (`:231`) y covarianza de la diferencia (`:233`) están en el libreto.

### Scripts (copia temporal, `python -I`)

Copia en `/tmp/verif_M03.1B1l/`.

- `M03_ejemplos.py`: código 0, imprime `comprobaciones_M03=OK`. Cifras comparadas con el libreto:
  - rectangular 0,1732 / resolución 0,02887 / triangular 0,1225 / u=U/k 0,300 (`:83-97`, `:145`);
  - u(promedio con componente común) 0,3606 (`:113`, `:149`);
  - covarianza 0,36, u(suma) 1,311, u(diferencia) 0,529 (`:187`, `:233`);
  - t(0,975;4)=2,776 y normal 1,960 (`:133`); t(0,975;15)=2,131 y semiancho 0,4263 (`:147`; el libreto escribe 0,4262, redondeo truncado, menor);
  - deriva: medias de mitades 420,175 / 420,575; bloques 420,075 a 420,675; media global 420,375; s/√16 de la serie 0,2150 (`:123`).
  - Todo coincide.
- `M03_practicas_luna.py`: código 0 y sus `assert` pasan (valores B e I, Blom, covarianza). **No imprime nada** (ver hallazgo 1).
- `write_probability_html` regenera un HTML de 4245 bytes **idéntico** a `calc/M03_practica_I_probabilidad.html`.

## Hallazgos

1. **Log inexacto.** `logs_etapa2/cambios_M03.md`, sección Verificación, dice que `M03_practicas_luna.py` imprimió `comprobaciones_M03_practicas=OK`. El archivo no tiene ese `print` (`calc/M03_practicas_luna.py:1-93`; `grep print` no devuelve nada). El script sí se ejecuta bien (solo `assert`). Corregir el log o añadir la línea de impresión.
2. **Etiqueta de práctica B.** `M03_libreto.md:139` dice «Práctica B. Convertir…» sin «(en clase, 25 min)». Compárese con `M03_libreto.md:223` y con el patrón de M02 (`M02_libreto.md:126`). Añadir la etiqueta para que la agenda y la sección coincidan.
3. **Residuo de A.** `calc/M03_ejemplos.py:24`: el comentario «Deriva B3/A2» cita la antigua escena A2, que ya no existe. Cambiar a «Deriva B3».
4. **Cobertura del PDF (M3, «En el SRP»).** `Curso_COMPLETO/temario_curso.md:111-135` lista como contenido de M3:
   - «Covarianza en acción: razón entre canales» (s = 0,000012 frente a 0,000089 con independencia). Estaba en la antigua escena A1 (original `Curso_COMPLETO/curso/S1_fundamentos/M03_libreto.md:256-272`), que se retiró. **Hoy M3 no lo cubre** en B ni en I. La I1 solo trata covarianza de dos resultados (`M03_libreto.md:185-191`). Decidir: reubicar un ejemplo corto de razón/covarianza en I1, o anotar la excepción en el plan.
   - «Ruido de conteo: cuantización ±0,5 cuentas = 0,5/√3». **No aparece** en M03 (ni en la versión original). Brecha previa, no introducida en etapa 2. Puede resolverse con una frase en B2 junto a la resolución (`M03_libreto.md:75-83`).
   - «Primera propagación con las reglas de la varianza, u(x)/x = u(D)/|D·ln D|». **No aparece** en M03 (brecha previa). Puede corresponder a M8; confirmarlo.
   - «¿Son normales las lecturas de un nivel? ¿Y las del cero?» Solo se trata en forma genérica, con datos simulados (`M03_libreto.md:213-217`), sin aplicarlo a lecturas del SRP. Aceptable si el alcance lo admite; anotarlo.
   - «Resolución del analizador 0,1 nmol/mol como variable rectangular»: cubierto con entrada hipotética (`M03_libreto.md:81-83`).
   - Tema del módulo («modelos de variabilidad»): cubierto (B1–B3, I1, I3). «Ruido del SRP»: cubierto solo con ejemplos simulados y advertidos como tales.

## Lo que no se verificó

- Recuento de palabras (3065 B / 2781 I): no se recontó; se acepta el dato del log.
- No se editó ningún archivo.
