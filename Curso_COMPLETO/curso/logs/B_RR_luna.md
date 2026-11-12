# Hito B — suficiencia histórica del estudio R&R

Fecha: 2026-10-27. S-03 del supervisor aplicado como diagnóstico reproducible solo lectura. No es hallazgo Haiku.

## Fuentes examinadas

- `docs/Resultados R&r_2022 2023 (1).xlsx`: hojas `45ppb`, `90ppb`, `135ppb`, `180ppb`, `225ppb`, `270ppb`, `315ppb`, `360ppb`, `405ppb`, `455ppb` y `BASE DE DATOS`.
- `curso/S2_modelos_calibracion/calc/M06_RR_CALAIRE.py` y sus advertencias.
- `curso/S2_modelos_calibracion/calc/revision_M05_M06_sol.md`.
- `casos_taller/caso_C_historial_level2.md`, `datos_caso_C1.csv`, `datos_caso_C2.csv` y `calc_casos.py`.

## Diagnóstico de inventario reproducible (solo lectura)

Se ejecutó desde la raíz del repositorio con `curso/.venv/bin/python -I -c` y `openpyxl.load_workbook(..., data_only=True, read_only=True)`. Se inspeccionaron `sheetnames`, `calculate_dimension()` para `BASE DE DATOS`, las etiquetas que contienen «ABSOLUT» o comienzan con «A1 E»/«A2 E», y B6:C23 en cada hoja cuyo nombre termina en `ppb`; se contaron celdas numéricas, mínimos, máximos y valores negativos. El comando no escribe el libro ni calcula errores firmados.

Resultado: hojas `Plantilla`, diez hojas por nivel y `BASE DE DATOS`; hojas por nivel con rango B6:C23 (18×2), 36 valores numéricos cada una, 360 en total. Valores globales entre 0,001857 y 0,948727; cero negativos. `BASE DE DATOS` tiene dimensión A2:AT139 y su campo de objeto describe errores entre el SRP y Nivel 2; el libro rotula sus datos analizados como «VALORES ABSOLUTOS» y columnas «A1 E…»/«A2 E…». Por tanto, no se convierten magnitudes absolutas a errores firmados, ni se presentan como mediciones con signo. El diagnóstico confirma inventario y ausencia de signo almacenado en las hojas por nivel; no valida el cálculo histórico.

Comando reproducible (lectura solamente):

```bash
./curso/.venv/bin/python -I -c $'from pathlib import Path\nimport openpyxl\np=Path("docs/Resultados R&r_2022 2023 (1).xlsx")\nw=openpyxl.load_workbook(p,data_only=True,read_only=True)\nprint("sheets=",w.sheetnames)\nallv=[]\nfor s in w.sheetnames:\n ws=w[s]\n if s.endswith("ppb"):\n  vals=[c.value for row in ws.iter_rows(min_row=6,max_row=23,min_col=2,max_col=3) for c in row]\n  nums=[v for v in vals if isinstance(v,(int,float))]\n  allv.extend(nums)\n  print(s,"range=B6:C23","shape=18x2","numeric=",len(nums),"min=",min(nums),"max=",max(nums),"negative=",sum(v<0 for v in nums))\n else:\n  print(s,"dimensions=",ws.calculate_dimension())\n  if s=="BASE DE DATOS":\n   print("labels=",[(c.coordinate,c.value) for row in ws.iter_rows() for c in row if isinstance(c.value,str) and ("ABSOLUT" in c.value.upper() or c.value.upper().startswith(("A1 E","A2 E")))])\nprint("global_numeric=",len(allv),"min=",min(allv),"max=",max(allv),"negative=",sum(v<0 for v in allv))\nw.close()'
```

## Diseño y límites del dato histórico

Las diez hojas por nivel contienen 36 celdas numéricas en B6:C23 (18 por columna), organizadas en tres bloques de seis días para dos columnas rotuladas Analista 1 y Analista 2. El metadato lista pares de pruebas/calibraciones (incluidos 171 y 173) y fechas/analistas; registra diez niveles de 45 a 455 ppb. El libro también dice que excluye errores del día 0. No aporta evidencia suficiente para asignar inequívocamente cada uno de los tres bloques de seis días a una campaña comparable, ni confirma correspondencia de días entre analistas. Las fechas y etiquetas no resuelven por sí solas el cruce del diseño.

## Método y resultados exploratorios

Se ejecutó sin modificaciones:

```text
./curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M06_RR_CALAIRE.py
```

Terminó con rc=0 usando `./curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M06_RR_CALAIRE.py`. Es una descomposición exploratoria condicional: analista, bloque e interacción, con días anidados; no empareja los días entre analistas. La ejecución encontró interacciones por encima del F crítico nominal 3,315830 en los niveles 135, 360, 405 y 455. Con diez contrastes por nivel, Bonferroni usa α/10 y F crítico 6,354689; superan ese umbral los niveles 135 y 405. El F máximo de analista es 1,238163. Salida reproducible completa de ambos scripts ejecutados en esta reanudación: `reanudacion_AB_M00_decisiones_luna.md` (resumen de M06) y `reanudacion_AB_M00_ejecucion_luna.log` (M00). Todos estos resultados son exploratorios y condicionales al modelo: describen el arreglo tabulado, no constituyen validación histórica, análisis de errores firmados ni evidencia confirmada de componentes físicos. La validación permanece bloqueada por datos de signo y diseño faltantes.

## Datos de casos y faltantes para validar historia

`casos_taller/caso_C_historial_level2.md` describe seis días de calibración de CALAIRE en febrero de 2023. El CSV `casos_taller/datos_caso_C1.csv` contiene seis filas, una por día, con indicadores diarios extraídos de `Resumen!B6:I11` del libro indicado en la descripción; no son lecturas repetidas homogéneas con estructura intradía ni un R&R de dos operadores. `datos_caso_C2.csv` contiene diez comparaciones cuya fuente indicada es NISTIR 6963; son datos externos y didácticos, no historia CALAIRE.

Solicitar el archivo fuente original, una fila por lectura, con al menos:

1. referencia SRP e indicación Level 2, unidades y cálculo firmado reproducible `e = y − x`;
2. nivel nominal/observado, pareja SRP–Level 2, número de lectura, ciclo y orden de medida;
3. operador inequívoco por observación (aclarar A1/A2) y equipo/SN;
4. fecha y hora por observación, campaña/calibración y mapeo documental de los tres bloques y sus días;
5. identificación de series/calibraciones 171 y 173 y explicación de discrepancias «171/173» y «tres bloques»/«cinco pares»;
6. réplicas intradía por operador×día×nivel, lecturas originales y estado/configuración de instrumentos;
7. fórmulas/transformaciones que producen «VALORES ABSOLUTOS», exclusiones (incluido día 0), faltantes y confirmación de lecturas individuales previas a promedios.

Sin esos datos no se atribuye al libro distribución de errores firmados, no se separa repetibilidad intradía de variación entre días ni se concluye reproducibilidad histórica validada.

## Decisiones S-xx y revisión

- **S-03:** aplicado al guardar aquí el diagnóstico reproducible de inventario y ejecutarlo en modo solo lectura. No se añadió un script permanente separado: el alcance autorizado se limita al reporte B, práctica M00, script propio M00 y reportes A/B/M00. Se preserva el carácter exploratorio; no se usan magnitudes absolutas como errores firmados.
- **S-01:** registrado en `A_qapp_luna.md`; grafía visible `<±` distinta de extracción `<+`, sin interpretación semántica autorizada.
- **S-02:** registrado en `M00_practicas_luna.md`; M00-B corregida con faltante genuino y clave P99 no inferible.
- La revisión obligatoria Haiku falló con `API Error: 400 unknown provider for model claude-haiku-5-5`, evidencia en `AB_revision_haiku.log` y `M00_practicas_revision.log`. No hubo revisión Haiku ni hallazgos H-xx. El pipeline queda detenido antes de M01; no se declara aprobación.