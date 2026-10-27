# Revisión Haiku 5.5 de la corrección O-02 (AX.12)

## Plan

Contrastar el párrafo final de AX.12 (`AX_libreto.md`, línea 315) y el texto registrado en `AX_bitacora_luna.md` (sección «Corrección O-02») con M11-A (`M11_libreto.md`, Escenas A1–A2, líneas 151–193).

Criterios:

1. Exactitud de lo atribuido a M11-A: EWMA con L=2,7; CUSUM bilateral; probabilidad de alarma en horizonte fijo; demora condicionada a detectar; no ARL.
2. Redacción oral: frases cortas, sin ambigüedad de referentes.
3. Referencia conservada: la cita a Montgomery se mantiene sin cambios.

No se edita el libreto. Solo se escribe este informe.

## Hallazgos

| ID | Ubicación | Problema | Corrección propuesta |
|---|---|---|---|
| H-01 | `AX_libreto.md:315` | Dice que el ejemplo de AX.12 «usa otros parámetros» para CUSUM, pero el CUSUM unilateral usa k=0,5 y h=5, los mismos de M11-A. Lo que cambia es el lado (unilateral frente a bilateral) y el L de EWMA (3 frente a 2,7). | Precisar: «…y CUSUM unilateral con los mismos k=0,5 y h=5 de M11-A, pero solo con la suma superior». |
| H-02 | `AX_libreto.md:315` | La cita usa la clave «Montgomery» sin año. M11-A usa «Montgomery 2013» (`M11_libreto.md:241`). Ambas apuntan a la misma obra, pero la clave no coincide entre capítulos. El pendiente bibliográfico (edición y numeral) sigue abierto. | Mantener la referencia tal como está, pues el usuario pidió conservarla. Dejar anotado en pendientes que la clave debe unificarse cuando se verifique la edición. Severidad baja. |
| H-03 | `AX_libreto.md:315` | Frase larga con dos incisos de guion largo para lectura oral («…usa otros parámetros —EWMA con L=3 y límites estacionarios, y CUSUM unilateral— para ilustrar…»). | Partir en dos frases: «El ejemplo de este anexo usa otros parámetros: EWMA con L=3 y límites estacionarios, y CUSUM unilateral. Sirve para ilustrar el cálculo complementario de ARL; no describe el análisis de M11-A.» Severidad baja. |

Verificado sin hallazgo:

- EWMA L=2,7 y CUSUM bilateral atribuidos a M11-A: coinciden con `M11_libreto.md:153–189` (`L=2.7`, `k=0,5`, `h=5`, ambas sumas).
- «Probabilidad de alarma en horizonte fijo»: correcto (19,909 % EWMA; 9,177 % CUSUM, horizonte 50).
- «Demoras condicionadas a detectar; esas demoras no son ARL»: correcto (`M11_libreto.md:191`).
- Límites de arranque EWMA: la fórmula de la pizarra AX.12 coincide con la de M11-A (`M11_libreto.md:163`).
- Texto de la bitácora («Texto nuevo») idéntico al párrafo de `AX_libreto.md:315`.
- Cifras: ARL≈560 y ≈931 de AX.12 se mencionan en M11-A (`M11_libreto.md:191`) con el mismo sentido («no se trasladan»); no se modificaron.

## Veredicto

**Aprobado con correcciones menores.** La atribución a M11-A es exacta en EWMA L=2,7, CUSUM bilateral, probabilidad en horizonte, demora condicional y «no ARL». Hay que corregir H-01 (los k y h del CUSUM sí coinciden con M11-A; solo cambia el lado) antes de dar por cerrada O-02. H-02 y H-03 son de baja severidad: el primero es pendiente bibliográfico, el segundo es estilo oral.
