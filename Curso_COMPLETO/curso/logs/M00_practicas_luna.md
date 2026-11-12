# M00: desarrollo y correcciones de prácticas — bitácora luna

Fecha: 2026-10-27

## Alcance

Reanudación A/B/M00: decisiones H-01–H-07 están consolidadas en `reanudacion_AB_M00_decisiones_luna.md`. Se restituyeron localizadamente los bloques completos B, I y A de M00, alineados con el script propio. Las prácticas quedan como borrador corregido, no aprobado. No se desarrolló taller ni otros capítulos.

## Plan y ejecución inicial preservados

El plan inicial fue resolver la discrepancia de claves sin inferir por magnitud ni posición, conservar originales y faltantes, ejecutar el script y no declarar aprobación sin revisión Haiku. La primera ejecución de la corrección S-02 quedó registrada en `M00_practicas_ejecucion.log` y `M00_practicas_revision.log`; su versión de datos y resultado se conserva como histórico, no como estado vigente: P03=100,2, P99=50,8 sin asignar y P04 faltante, con tres parejas completas y un huérfano. Esa solución no cumplía el objetivo de evidenciar una pareja desplazada; se reemplazó en la aplicación final por la asociación documentada en R03.

## S-02 aplicada — evidencia R03

Se aplican exactamente los datos simulados solicitados. Referencias: P01=0,0, P02=50,0, P03=50,0 y P04=100,0 nmol/mol. Indicaciones originales: P01=−0,2, P02=50,4 y P99=50,8; P04 no fue adquirido. La indicación transcrita como P99 lleva ID de adquisición R03. La especificación para la práctica usa el registro original de adquisición, cuyo campo de asociación vincula R03 con P03; el script propio conserva esa evidencia y la utiliza como fundamento documental, nunca por orden o magnitud.

Antes de consultar el registro original: dos parejas completas; P99 es una indicación huérfana; P03 y P04 son referencias no emparejadas. Aplicado el campo de asociación de R03, se conservan `id_original=P99` y `y_original=50,8`, se agrega `id_corregido=P03`, motivo «el registro de adquisición R03 vincula esta lectura con P03» y fuente «registro de adquisición R03». Después: tres parejas completas P01/P02/P03 con `e=−0,2; 0,4; 0,8` nmol/mol; P04 permanece con indicación faltante porque no fue adquirido; cero indicaciones huérfanas. La fila P04 puede aparecer en la tabla de referencias con `y` faltante y no se cuenta como indicación. No se infiere por magnitud ni orden.

## Script y ejecución actualizada

`curso/S1_fundamentos/calc/M00_practicas_luna.py` reproduce los datos, claves y errores de B; aplica el registro original de adquisición R03, conserva P99/50,8 como originales y documenta P03 como ID corregido. El libreto ahora contiene los tres bloques completos: B (tareas, registro de adquisición, solución trazable, decisión y rúbrica), I (tabla C1 de ocho filas, resumen, solución, decisión y rúbrica) y A (seis parejas, contrato, comparación, solución, decisión y rúbrica). En I la clave del script incluye campaña C1. En A se verifican claves únicas, ausencia de faltantes, valores numéricos y compatibilidad de unidades declaradas, además del desacuerdo.

Ejecución final real: `./curso/.venv/bin/python -I curso/S1_fundamentos/calc/M00_practicas_luna.py`, rc=0. Salida íntegra en `reanudacion_AB_M00_ejecucion_luna.log`; decisiones H-01–H-07 actualizadas en `reanudacion_AB_M00_decisiones_luna.md`. B termina con tres parejas completas, P04 sin adquirir y cero huérfanas; I conserva 7 completas y 1 faltante, con medias de error 0,3; 0,1; −0,2; 0,2; A detecta máximo desacuerdo 0,1 frente a tolerancia 1e-6 (sin acuerdo).

## Estado de revisión

La revisión obligatoria Haiku no está disponible: `API Error: 400 unknown provider for model claude-haiku-5-5`, documentado en `M00_practicas_revision.log`. No hubo revisión Haiku ni aprobación. M00 permanece borrador corregido.