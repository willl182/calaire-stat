#!/usr/bin/env bash
# Regenera los extractos de la ronda final de citas S2 (F-01…F-08) desde docs/.
# Uso: bash curso/citas/extractos/s2_ronda_final.sh   (desde la raíz del repositorio)
set -euo pipefail
D="docs"
X="curso/citas/extractos"
ext() { # archivo_pdf pagina_pdf salida
  pdftotext -f "$2" -l "$2" -layout "$D/$1" - > "$X/$3" 2>/dev/null
}
ext "o3_tad_508_20230906_final.pdf" 36 ronda_tad_p36.txt            # F-01: §4.4.1, «three (3) stable testing cycles»
ext "Statistical Concepts – A First Course.pdf" 210 ronda_hv_p210.txt  # F-01: §6.1.3 Power
ext "Statistical Concepts – A First Course.pdf" 234 ronda_hv_p234.txt  # F-01: §6.5 Power Using G*Power
ext "Statistical Concepts – A First Course.pdf" 364 ronda_hv_p364.txt  # F-03: encabezado §9.3
ext "Statistical Concepts – A First Course.pdf" 377 ronda_hv_p377.txt  # F-03: «There is really not much…»
ext "Statistical Concepts – A First Course.pdf" 399 ronda_hv_p399.txt  # F-02: §10.1.1.5.2 y «magnitude of the correlation»
ext "Statistical Concepts – A First Course.pdf" 332 ronda_hv_p332.txt  # F-08: §8.2.1, método de Bonferroni
ext "Chemometrics Statistics and Computer Application.pdf" 222 ronda_otto_p222.txt  # F-04: tabla 6.1 (p. impresa 217)
ext "Chemometrics Statistics and Computer Application.pdf" 227 ronda_otto_p227.txt  # F-04: ec. (6.20) (p. impresa 222)
ext "Air quality_ Determination of ozone in ambient air_ ISO 13964.pdf" 14 ronda_iso13964_p14.txt  # F-05: §6.2.2 (p. impresa 6)
