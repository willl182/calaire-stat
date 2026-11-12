# Verificación ronda 2 — etapa 1

Fecha: 2026-11-11. Directorio: `Curso_CORTO/`. Fuentes: `logs_etapa1/verif_sol_etapa1.md` y `logs_etapa1/ronda2/cambios_r2.md`. No se editó ningún archivo del curso; cambios de otros agentes ignorados.

## Veredicto

**CON OBSERVACIONES**

Los siete cambios de r2 están presentes en el estado actual y sus cifras coinciden con la ejecución. Hay una incoherencia nueva en el texto vecino de la corrección de M05 (la diapositiva de B3 todavía atribuye los seis días al certificado) y una mención residual de MAD en B6 que F04 pedía retirar o hacer autosuficiente.

## Ejecución de scripts modificados

Se ejecutaron en una copia temporal (`cp -r` del directorio) con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I`, para no sobrescribir los HTML del directorio.

| Script | Resultado |
|---|---|
| `calc/M02_examples.py` | rc=0. Sensibilidad con +1,6 (`calc/M02_examples.py:94`): media firmada 0,177778, media absoluta 0,533333, s=0,670406. Coincide con `cambios_r2.md` y con la narración de `M02_libreto.md:198`. |
| `calc/M06_practica_I_grafico.py` | rc=0. Genera `M06_practica_I_residuos.html`; el HTML regenerado es idéntico byte a byte al del directorio. Título con 94 nmol/mol (`M06_practica_I_residuos.html`, elemento `<title id="chart-title">`). |

## Verificación por cambio de r2

| Cambio declarado | Estado actual | Resultado |
|---|---|---|
| `M02_libreto.md:9` — ficha B6 con regla IQR | Presente en la fila «Nivel B» | Resuelto |
| `M02_libreto.md:96` — retirar introducción prematura de MAD (F04) | La MAD sigue nombrada en B6: «la mediana y la MAD (desviación absoluta mediana) se incorporan en el nivel I». | Resuelto en lo esencial; ver hallazgo 2 |
| `M02_libreto.md:174` — leer e interpretar la recta sin estimarla (F03) | Presente: «Lean la recta descriptiva ya ajustada… No estimen los coeficientes». Armoniza con `:160` y la solución de `:176`. | Resuelto |
| `M02_libreto.md:239` — referencia Otto §2.2 (F06) | Entrada «Otto, M.» presente con §2.2 y ruta en `../Curso_COMPLETO/docs/`; cita en `:98` ya resuelve. | Resuelto (la correspondencia de contenido con Otto no se verificó) |
| `M05_libreto.md:64,70` — seis días como supuesto didáctico | Presente en `:64` y `:72`; la práctica (`:98`) declara lo mismo. | Resuelto en el texto indicado; ver hallazgo 1 |
| `M06_libreto.md:172` — nivel nominal 94 nmol/mol | Presente. Verificado en `F-PSMT-01 ... .xlsm`, hoja `BD_DIAS`, filas 31–38: columna de nivel nominal = 94 en las ocho filas, con 6 réplicas por fila. | Resuelto |
| `calc/M06_practica_I_grafico.py:3,39,94` — rótulo 90 → 94 | Comentario, `<title>` y texto con 94; el HTML lo refleja. | Resuelto |

Además se comprobó la discrepancia heredada de la sección 6 de `verif_sol_etapa1.md`: el script de M02 ya no contiene +1,8 (`calc/M02_examples.py:94` usa 1,6).

## Hallazgos

### 1. La diapositiva de B3 sigue atribuyendo los seis días al certificado (incoherencia con el cambio de M05)
- **Archivo:línea:** `M05_libreto.md:62`
- **Texto:** «[DIAPOSITIVA] Presentar la estructura: 10 puntos de concentración + 2 puntos de cero; 8 lecturas por punto y día (el certificado las llama repeticiones); 6 días. Rótulo visible: «Descripción del certificado F-PSMT-01; datos de diseño propios».»
- **Problema:** `M05_libreto.md:64` y `:72` dicen que los seis días son un supuesto didáctico que «no se atribuye a la nota», y la celda E17 solo declara 8 repeticiones por punto. La diapositiva, con el rótulo «Descripción del certificado», vuelve a atribuir el 6 al certificado. Además dice «8 lecturas por punto y día» mientras el texto narrativo dice «ocho repeticiones por punto».
- **Severidad:** media. Es exactamente la discrepancia que r2 declaró resuelta, y queda en el texto vecino inmediato.
- **Corrección sugerida:** en la diapositiva, separar «nota del certificado: 10+2 puntos, 8 repeticiones por punto» de «supuesto didáctico: 6 días».

### 2. MAD sigue mencionada en B6 (F04 resuelto solo parcialmente)
- **Archivo:línea:** `M02_libreto.md:96`
- **Texto:** «En el nivel B usamos la regla IQR anterior como referencia descriptiva; la mediana y la MAD (desviación absoluta mediana) se incorporan en el nivel I.»
- **Problema:** la regla de B ya no depende de MAD, así que no es prerrequisito. La mención actual es una referencia hacia adelante, definida en el lugar y sin uso, por lo que no contradice F04. Sin embargo, `cambios_r2.md` dice «retirada la introducción prematura de mediana/MAD», y la frase la conserva.
- **Severidad:** baja (observación). Se puede eliminar la frase o dejar solo «la mediana y la MAD se incorporan en el nivel I».

### 3. Pendientes de la verificación global no tratados en r2 (fuera de alcance de esta ronda)
`cambios_r2.md` no declara cambios para F01 (`M03_libreto.md:18`, referencia a M1), F02 (`M06_libreto.md:283`, `M05_libreto.md:78`, `M03_libreto.md:326`), F05 (unidades en `M02_libreto.md:18`) ni F07 (rutas de `M04_libreto.md:152`, `M06_libreto.md:189`, `M02_libreto.md:120,176,216`). No se verificaron aquí; siguen abiertos según `verif_sol_etapa1.md`. Si estaban asignados a r2, la ronda queda incompleta.

## Ajuste sobre el registro

No hubo cambios en `calc/` que rompan la ejecución. Dos scripts cambiaron y ambos corren sin error. Los demás scripts no se volvieron a ejecutar en esta ronda.
