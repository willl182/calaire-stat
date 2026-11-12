"""Soluciones reproducibles de las prácticas B e I de M06.
Datos simulados fijados aquí; no son resultados de CALAIRE.
Ejecutar desde la raíz de Curso_CORTO: ../Curso_COMPLETO/curso/.venv/bin/python -I calc/M06_practicas_luna.py
"""
from math import sqrt
from pathlib import Path

import numpy as np
import openpyxl
from scipy.stats import beta, chi2, f

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "docs" / "F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm"

# B: componentes ya estimadas; diseño equilibrado declarado.
sr, se, d, n, k = 0.24, 0.30, 6, 8, 2.0
u2 = se**2/d + sr**2/(d*n)
u = sqrt(u2)
u_solo = sr/sqrt(d*n)

# I: Level 2 propio; diferencias con signo en 94 nmol/mol nominal (columnas F, L, R, X, AD y AJ de BD_DIAS).
wb = openpyxl.load_workbook(BOOK, data_only=True, read_only=True)
ws = wb["BD_DIAS"]
cols = [6, 12, 18, 24, 30, 36]
groups = np.array([[-ws.cell(row, col).value for row in range(31, 39)] for col in cols], dtype=float)
wb.close()
if groups.shape != (6, 8) or not np.isfinite(groups).all():
    raise ValueError("Se esperaban 6 días x 8 errores finitos en BD_DIAS")
means = groups.mean(axis=1)
grand = groups.mean()
ssb = groups.shape[1] * ((means-grand)**2).sum()
ssw = ((groups-means[:, None])**2).sum()
msb, msw = ssb/5, ssw/42
Fday = msb/msw
crit_day = f.ppf(.95, 5, 42)
tau2 = (msb-msw)/8
sr_i, se_i = sqrt(msw), sqrt(tau2)
variance_ci = (ssw / chi2.ppf(.975, 42), ssw / chi2.ppf(.025, 42))
tau2_se = sqrt(2 * (msb**2/5 + msw**2/42) / 8**2)
se_day_se_delta = tau2_se / (2*se_i)
# Cuatro varianzas de grupo simuladas para Cochran.
vars_ = np.array([.010, .012, .011, .027])
C = vars_.max()/vars_.sum()
Ccrit = beta.ppf(1-.05/4, 4/2, 3*4/2)

print('B simulated inputs: s_r=0.24, s_entre=0.30, d=6, n=8, k=2')
print(f'B u2={u2:.9f}; u={u:.9f}; U={k*u:.9f}; u_without_between={u_solo:.9f}')
print('I own Level 2 signed errors, 94 nmol/mol nominal, from BD_DIAS rows 31:38:', groups.tolist())
print(f'I means={means.tolist()}, grand={grand:.9f}; SS_between={ssb:.9f}; SS_within={ssw:.9f}; SS_total={ssb+ssw:.9f}')
print(f'I df=(5,42); MS=({msb:.9f},{msw:.9f}); F={Fday:.9f}; Fcrit05={crit_day:.9f}; tau2={tau2:.9f}; s_entre={se_i:.9f}; s_r={sr_i:.9f}')
print(f'I sigma2 95% CI={variance_ci}; SE(tau2) approx={tau2_se:.9f}; SE(s_entre) delta approx={se_day_se_delta:.9f}')
print(f'I Cochran simulated variances={vars_.tolist()}; C={C:.6f}; Ccrit05={Ccrit:.6f} (no automatic deletion)')
