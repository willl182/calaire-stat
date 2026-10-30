"""Soluciones reproducibles de las prácticas B, I y A de M06.
Datos simulados fijados aquí; no son resultados de CALAIRE.
Ejecutar desde la raíz: curso/.venv/bin/python curso/S2_modelos_calibracion/calc/M06_practicas_luna.py
"""
from math import sqrt
from pathlib import Path

import numpy as np
import openpyxl
from scipy.stats import beta, chi2, f

ROOT = Path(__file__).resolve().parents[3]
BOOK = ROOT / "docs" / "F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm"

# B: componentes ya estimadas; diseño equilibrado declarado.
sr, se, d, n, k = 0.24, 0.30, 6, 8, 2.0
u2 = se**2/d + sr**2/(d*n)
u = sqrt(u2)
u_solo = sr/sqrt(d*n)

# I: Level 2 propio; diferencias con signo en 94 nmol/mol nominal (columna AL de BD_DIAS).
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

# A: 2 analistas x 3 campañas x 2 días anidados; cada celda contiene
# dos medias diarias firmadas (simuladas); la matriz de partida menos 0,4 se fija aquí.
x = np.array([[[0,.2],[.1,.3],[.4,.6]], [[.3,.5],[0,.2],[.7,.9]]]) - .4
na, nb, r = x.shape
mu = x.mean(); ma=x.mean(axis=(1,2)); mb=x.mean(axis=(0,2)); mc=x.mean(axis=2)
ssa=nb*r*((ma-mu)**2).sum(); ssb_a=na*r*((mb-mu)**2).sum()
ssab=r*((mc-ma[:,None]-mb[None,:]+mu)**2).sum()
sse=((x-mc[:,:,None])**2).sum()
dfa,dfb,dfab,dfe=1,2,2,6
msa,msb_a,msab,mse=ssa/dfa,ssb_a/dfb,ssab/dfab,sse/dfe
Fa,Fb,Fab=msa/msab,msb_a/msab,msab/mse
# Tres contrastes de interacción predeclarados: diferencias de analista
# entre cada par de campañas; Bonferroni controla la familia completa.
analyst_campaign = x.mean(axis=2)
diff_by_campaign = analyst_campaign[1] - analyst_campaign[0]
contrasts = np.array([diff_by_campaign[j] - diff_by_campaign[i]
                      for i, j in ((0, 1), (0, 2), (1, 2))])
F_interaction_contrasts = contrasts**2 / (2*mse)
Fcrit_bonf = f.ppf(1-.05/3, 1, 6)
# Componentes por momentos, factores aleatorios equilibrados.
var_a=(msa-msab)/(nb*r); var_b=(msb_a-msab)/(na*r)
var_ab=(msab-mse)/r; var_day=mse
# Componente negativa y estimación REML restringida en ejemplo equilibrado.
neg=np.array([[0,.2,-.1,.1],[.05,.25,-.05,.15],[-.03,.17,-.13,.07]])
means_n=neg.mean(axis=1); g=neg.mean(); sst=((neg-g)**2).sum()
sw=((neg-means_n[:,None])**2).sum(); sb=4*((means_n-g)**2).sum()
msw_n=sw/9; msb_n=sb/2; tau_raw=(msb_n-msw_n)/4
# En la frontera tau2=0, sigma2_REML=SST/(N-1); la optimización
# restringida se comprueba en M06_ejemplos.py.
sigma2_reml=sst/11

print('B simulated inputs: s_r=0.24, s_entre=0.30, d=6, n=8, k=2')
print(f'B u2={u2:.9f}; u={u:.9f}; U={k*u:.9f}; u_without_between={u_solo:.9f}')
print('I own Level 2 signed errors, 94 nmol/mol nominal, from BD_DIAS rows 31:38:', groups.tolist())
print(f'I means={means.tolist()}, grand={grand:.9f}; SS_between={ssb:.9f}; SS_within={ssw:.9f}; SS_total={ssb+ssw:.9f}')
print(f'I df=(5,42); MS=({msb:.9f},{msw:.9f}); F={Fday:.9f}; Fcrit05={crit_day:.9f}; tau2={tau2:.9f}; s_entre={se_i:.9f}; s_r={sr_i:.9f}')
print(f'I sigma2 95% CI={variance_ci}; SE(tau2) approx={tau2_se:.9f}; SE(s_entre) delta approx={se_day_se_delta:.9f}')
print(f'I Cochran simulated variances={vars_.tolist()}; C={C:.6f}; Ccrit05={Ccrit:.6f} (no automatic deletion)')
print('A simulated signed daily means, analyst x campaign x day:',x.tolist())
print(f'A SS=(A:{ssa:.6f}, campaign:{ssb_a:.6f}, interaction:{ssab:.6f}, day:{sse:.6f})')
print(f'A MS=({msa:.6f},{msb_a:.6f},{msab:.6f},{mse:.6f}); F=({Fa:.6f},{Fb:.6f},{Fab:.6f})')
print(f'A interaction contrasts campaign pairs=(12,13,23): estimates={contrasts.tolist()}; F={F_interaction_contrasts.tolist()}; Bonferroni Fcrit(1,6)={Fcrit_bonf:.6f}; no contrast exceeds')
print(f'A moment variances=(analyst:{var_a:.6f}, campaign:{var_b:.6f}, interaction:{var_ab:.6f}, day:{var_day:.6f})')
print(f'A negative-component example MS_between={msb_n:.6f}; MS_within={msw_n:.6f}; tau2_raw={tau_raw:.6f}; REML boundary tau2=0, sigma2={sigma2_reml:.6f}')
