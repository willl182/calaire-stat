# Verificación transversal de la ficha común — 2026-10-26

Supervisor: claude-sol (gpt-6.1-sol). Alcance: contenido, no adopción operativa.

## S-TR-01 — Evidencia enlazada a directorio inexistente

Ubicación: `S3_01_ficha_criterios.md`, párrafo posterior a tabla SRP/EPA. Severidad: menor (trazabilidad documental). Problema: `calc/fuentes_M09_M10/` no existe. Corrección aplicada: remitir a `calc/auditoria_M09_M10/`, que conserva extractos de las fuentes citadas. Se conserva la ficha como corrección candidata de la ejecución interrumpida: reúne los campos exigidos por prop_e §5 M10 y distingue tolerancias, límites de control e indicadores, sin aprobar criterios del laboratorio.

## Fuentes contrastadas directamente

Extracción con `pdftotext -layout` de los originales locales, 26-10-2026:

- SRP-SOP §9.1.1: pendiente 1±0,04, intercepto 0±4 ppb, mínimo seis niveles positivos y dos ceros, al menos siete lecturas por concentración, un ciclo diario durante seis días. §9.1.3 distingue reverificación y reparaciones mayores.
- SRP-QAPP §6.2.1: tres ciclos mínimos, doce concentraciones incluyendo ceros, promedios de diez lecturas. Tabla 7-1 y texto imprimen signos ambiguos para el intercepto. Se conserva advertencia, sin inventar desigualdad.
- `ficha_TAD_actual.txt`, líneas 1323–1358: verificación de tres ciclos, cero y seis niveles positivos, criterios por punto y por regresión; reverificación de un ciclo, límites absolutos y cambios frente a medias previas. Las ecuaciones 8–9 corresponden a la dispersión de tres pendientes/interceptos, no a una desviación genérica con divisor n−1.
- `ficha_CFR_actual.txt`, líneas 248–251: metas O3, 90 % para precisión y 95 % para sesgo absoluto, ambas 7 %. Líneas 1036–1087: estimadores y asignación de signo por percentiles. El PDF contiene fórmulas como imágenes: se examinó además `verificacion_fuentes_agente/CFR_p19.png`, que muestra ecuaciones 2–5. La desviación firmada y la de magnitudes tienen divisor n−1; el límite de sesgo usa t(0,95;n−1) y AS/raíz(n).
- `ficha_EN_actual.txt`, definición 3.12: detección 3,3·sz/B; tabla de características y §8.4.5: repetibilidad al cero, no error estándar de la media. No convertir 3s0 en definición universal.

Los extractos `ficha_*_actual.txt` son auxiliares de verificación, no nuevas fuentes ni datos del laboratorio. Las simulaciones de la ficha se contrastan con los scripts M11/M12 en sus informes respectivos. No se certifica vigencia/adopción local, ni se resuelve la tipografía ambigua del QAPP.

## Coherencia de remisiones

Se comprobaron encabezados de `../S4_numericos_integracion/AX_libreto.md`: existen AX.1, AX.2, AX.8, AX.9, AX.10, AX.11 y AX.12. Los destinos temáticos requeridos por S3 coinciden con la guía. No se modifica ni se aprueba aquí el contenido de S4.

## Control del alcance de edición

Se comparó `git status --porcelain` global con `estado_inicial_20261026.txt`. El control de igualdad de estados externos **falló**: aparecieron cambios concurrentes en S1, S2 y S4. No se ejecutó ninguna edición de esos archivos desde esta revisión ni se revirtieron cambios ajenos. Este control no permite certificar inmovilidad de todo el árbol externo; el alcance de las ediciones propias permanece en S3. Se conserva el estado inicial como evidencia, sin atribuir automáticamente cambios concurrentes a esta ejecución.

No existe en S3 una carpeta `auditoria_interrupcion_sol/` con C01–C27. El LEEME disponible atribuye esos identificadores a S1. La evidencia recuperable propia de S3 consta de 36 bloques en `auditoria_interrupcion_sol_2/cambios_sol.diff`, además de instantáneas en `versiones/`; no se inventan decisiones Cxx sin evidencia.
