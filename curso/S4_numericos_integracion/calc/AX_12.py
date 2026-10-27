"""ARL bajo N(0,1), inicio cero y límites constantes; refinamiento de malla."""
import numpy as np
from scipy.stats import norm
from math import sqrt


def ewma_arl(n, lam=.2, limit=1.):
    edges = np.linspace(-limit, limit, n + 1)
    states = (edges[:-1] + edges[1:]) / 2
    mu = (1 - lam) * states[:, None]
    p = np.diff(norm.cdf((edges[None, :] - mu) / lam), axis=1)
    arl = np.linalg.solve(np.eye(n) - p, np.ones(n))
    # Exact start at zero, including when zero is not a cell center.
    initial = np.diff(norm.cdf(edges / lam))
    return 1 + initial @ arl


def cusum_arl(n, k=.5, limit=5.):
    # n positive cells, plus a separate state for the probability atom at zero.
    edges = np.linspace(0., limit, n + 1)
    states = np.r_[0., (edges[:-1] + edges[1:]) / 2]
    mu = states[:, None] - k
    p = np.empty((n + 1, n + 1))
    p[:, 0] = norm.cdf(k - states)  # P(S_next=0 | S=state), not first cell.
    p[:, 1:] = np.diff(norm.cdf(edges[None, :] - mu), axis=1)
    assert np.all(p >= 0) and np.all(p.sum(axis=1) <= 1)
    arl = np.linalg.solve(np.eye(n + 1) - p, np.ones(n + 1))
    assert np.max(np.abs(arl - 1 - p @ arl)) < 1e-8
    return arl[0]


if __name__ == '__main__':
    lam, sigma = .20, 1.
    factor = lam / (2 - lam)
    print(f'factor_varianza={factor:.9g}; sd_ewma={sigma*sqrt(factor):.9g}; ARL_geom_p001={1/.01:g}')
    results = []
    for n in (240, 480, 960, 1201):
        e, c = ewma_arl(n), cusum_arl(n)
        results.append((e, c))
        print(f'celdas={n}; EWMA_ARL0={e:.6f}; CUSUM_ARL0_atomo_cero={c:.6f}')
    change = np.abs(np.array(results[-1]) - results[-2])
    print(f'cambio_960_a_1201={change}; tolerancia_refinamiento=0.1')
    assert np.all(change < .1), 'Refinamiento insuficiente para el redondeo docente'
    assert tuple(round(v) for v in results[-1]) == (560, 931)
