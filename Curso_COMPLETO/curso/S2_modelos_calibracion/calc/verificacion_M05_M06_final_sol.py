"""Comprobaciones independientes finales; no modifica fuentes ni evidencia histórica.
Ejecutar desde cualquier directorio con curso/.venv/bin/python -I.
"""
from pathlib import Path
from itertools import product
import hashlib
import importlib.util
import json
import subprocess

import numpy as np
import openpyxl
import pandas as pd
from scipy.stats import beta, f, f_oneway
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.power import TTestPower

ROOT = Path(__file__).resolve().parents[3]
CALC = Path(__file__).resolve().parent


def load(name):
    spec = importlib.util.spec_from_file_location(name, CALC / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    m6 = load("M06_ejemplos")
    rr = load("M06_RR_CALAIRE")
    checks = 0

    def close(actual, expected, label, atol=1e-10):
        nonlocal checks
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=1e-9)
        checks += 1
        print("PASS", label)

    # Contrastes por diferencias directas, no por sumas de signos del script.
    table = []
    for F, Cx, T in product((-1, 1), repeat=3):
        y = .20 + .40*F + .10*Cx - .05*T + .15*F*Cx + .02*F*T - .01*Cx*T + .04*F*Cx*T
        table.append((F, Cx, T, y))
    table = np.array(table)
    contrasts = []
    for cols in [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]:
        signs = table[:, cols].prod(axis=1)
        contrasts.append(table[signs == 1, 3].mean() - table[signs == -1, 3].mean())
    close(contrasts, [.8, .2, -.1, .3, .04, -.02, .08], "M05 siete efectos factoriales")
    powers = [TTestPower().power(.2 / np.sqrt(.2**2 + .1**2/n), d, .05)
              for d, n in [(6, 8), (6, 16), (12, 8)]]
    close(powers, [.495146582, .500928099, .873251093], "M05 potencia statsmodels", atol=5e-10)
    close([2, 9, 12, 168], [3-1, 3*(4-1), 3*4*(2-1), 3*4*2*(8-1)], "M05 estratos suman 191")
    assert sum([2, 9, 12, 168]) == 192-1
    close(np.sqrt(.3**2/6 + .24**2/48), .12727922061357855, "M06 B precisión media")
    close(np.sqrt(.3**2 + .24**2/8)/np.sqrt(6), np.sqrt(.3**2/6 + .24**2/48), "M06 B medias sin doble conteo")

    groups = [[-.2, 0, .1, .1], [.3, .5, .6, .6], [-.1, .1, .2, .2]]
    one = m6.one_way(groups)
    close(one['f'], f_oneway(*groups).statistic, "M06 un factor scipy independiente")
    frame = pd.DataFrame({'error': np.array(groups).ravel(), 'day': np.repeat(range(3), 4)})
    fit = anova_lm(ols('error ~ C(day)', frame).fit())
    close(fit['sum_sq'].to_numpy(), [one['ss_between'], one['ss_within']], "M06 un factor SS statsmodels")
    close((one['tau2'], one['sigma2']), (.065, .02), "M06 componentes un factor")

    crossed = np.array([[[0, .2], [.1, .3], [.4, .6]], [[.3, .5], [0, .2], [.7, .9]]])
    frame = pd.DataFrame([{'response': crossed[i,j,k], 'analyst': str(i), 'campaign': str(j)}
                          for i,j,k in product(range(2), range(3), range(2))])
    fit = anova_lm(ols('response ~ C(analyst)*C(campaign)', frame).fit())
    direct = m6.two_way_with_replication(crossed)
    close(fit['sum_sq'].to_numpy(), [direct[k] for k in ['ss_a','ss_b','ss_ab','ss_e']], "M06 cruzado SS statsmodels")
    shifted = m6.two_way_with_replication(crossed-.4)
    close([direct[k] for k in ['ss_a','ss_b','ss_ab','ss_e']],
          [shifted[k] for k in ['ss_a','ss_b','ss_ab','ss_e']], "M06 invariancia por traslación firmada")
    close([(shifted['ms_a']-shifted['ms_ab'])/6,
           (shifted['ms_b']-shifted['ms_ab'])/4,
           (shifted['ms_ab']-shifted['ms_e'])/2, shifted['ms_e']],
          [.005, .05666666666666667, .01666666666666667, .02], "M06 cuatro componentes jerárquicas")
    # REML equilibrado: comparar toda una rejilla positiva con el mínimo de frontera.
    negative = np.array([[0,.2,-.1,.1],[.05,.25,-.05,.15],[-.03,.17,-.13,.07]])
    sst = ((negative-negative.mean())**2).sum()
    ssw = ((negative-negative.mean(axis=1,keepdims=True))**2).sum()
    ssb = sst-ssw
    lam = np.r_[0., np.logspace(-8, 8, 2001)]
    profile = 11*np.log((ssw+ssb/(1+4*lam))/11) + 2*np.log1p(4*lam)
    assert np.argmin(profile) == 0
    checks += 1
    print('PASS M06 REML frontera frente a rejilla positiva amplia')
    close(sst/11, .014824242424242425, 'M06 sigma2 REML')
    critical_f = f.isf(.05/4, 4, 12)
    close(critical_f/(critical_f+3), beta.ppf(1-.05/4, 2, 6), 'M06 Cochran beta frente a F')
    close(critical_f/(critical_f+3), .6287244614609693, 'M06 Cochran tabla 0.629', atol=1e-9)

    wb = openpyxl.load_workbook(rr.BOOK, data_only=True, read_only=True)
    arrays = [np.array(list(wb[f'{level}ppb'].iter_rows(min_row=6,max_row=23,min_col=2,max_col=3,values_only=True)),dtype=float).reshape(3,6,2).transpose(2,0,1) for level in rr.LEVELS]
    all_values = np.concatenate([x.ravel() for x in arrays])
    assert all_values.size == 360 and np.isfinite(all_values).all() and (all_values >= 0).all()
    checks += 1
    print('PASS R&R 360 entradas finitas no negativas; signo NO confirmado')
    vals = [rr.nested_anova(x) for x in arrays]
    for level, x, result in zip(rr.LEVELS, arrays, vals):
        frame = pd.DataFrame([{'response': x[i,j,k], 'analyst': str(i), 'block': str(j)}
                              for i,j,k in product(range(2), range(3), range(6))])
        fit = anova_lm(ols('response ~ C(analyst)*C(block)', frame).fit())
        ms = fit['mean_sq'].to_numpy()
        close([result['F_analyst'],result['F_block'],result['F_interaction']],
              [ms[0]/ms[2],ms[1]/ms[2],ms[2]/ms[3]], f'R&R nivel {level} OLS independiente')
    significant = [level for level,result in zip(rr.LEVELS, vals) if result['F_interaction']>f.isf(.05/10,2,30)]
    assert significant == [135,405]
    checks += 1
    base = wb['BASE DE DATOS']
    assert base['E17'].value == base['E18'].value
    print('PASS R&R umbral Bonferroni y fechas iguales 171/173; contradicción documental permanece')
    print('BASE DE DATOS C5:', base['C5'].value)
    print('BASE DE DATOS C19:', base['C19'].value)
    wb.close()
    for chapter in ['M05', 'M06']:
        text = (CALC.parent/(chapter+'_libreto.md')).read_text()
        assert text.count('[PRÁCTICA — fase de ejercicios]') == 3
        checks += 1
        print('PASS',chapter,'tres marcadores sin desarrollo')
    manifest = json.loads((CALC/'fuentes_M05_M06_final_sol/manifest.json').read_text())
    for source in sorted((CALC/'fuentes_sol').glob('M05_M06_*.txt')):
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        match = [row for row in manifest if row['sha256'] == digest]
        assert len(match) == 1
        print('EXTRACTO HISTÓRICO VIGENTE',source.name,'=',match[0]['text'],Path(match[0]['source']).name)
    print('TOTAL', checks, 'comprobaciones numéricas/estructurales; 19 extractos históricos cotejados.')


if __name__ == '__main__':
    main()
