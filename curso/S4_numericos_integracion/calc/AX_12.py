import numpy as np
from scipy.stats import norm
from math import sqrt
lam, sigma = .20, 1.
factor = lam/(2-lam)
print(f'factor_varianza={factor:.9g}; sd_ewma={sigma*sqrt(factor):.9g}; ARL_geom_p001={1/.01:g}')

# Finite-state Markov approximation of a two-sided EWMA run length.
h = 3*sigma*sqrt(factor)
n = 240
edges = np.linspace(-h, h, n+1)
centers = (edges[:-1]+edges[1:])/2
P = np.empty((n,n))
for i,z in enumerate(centers):
    mu, sd = (1-lam)*z, lam*sigma
    P[i,:] = norm.cdf((edges[1:]-mu)/sd)-norm.cdf((edges[:-1]-mu)/sd)
arl = np.linalg.solve(np.eye(n)-P, np.ones(n))
start = np.argmin(np.abs(centers))
print(f'EWMA_grid_states={n}; threshold={h:.9g}; approximate_ARL0={arl[start]:.6g}')

# Finite-state Markov approximation of one-sided CUSUM under N(0,1).
k, threshold, n = .5, 5., 240
edges = np.linspace(0., threshold, n+1)
centers = (edges[:-1]+edges[1:])/2
P = np.empty((n,n))
for i,state in enumerate(centers):
    mu = state-k
    # The zero atom from max(0, state + X - k) is assigned to the first cell.
    P[i,0] = norm.cdf((edges[1]-mu))
    if n > 1:
        P[i,1:] = norm.cdf(edges[2:]-mu)-norm.cdf(edges[1:-1]-mu)
arl = np.linalg.solve(np.eye(n)-P, np.ones(n))
start = 0
print(f'CUSUM_grid_states={n}; k={k:g}; threshold={threshold:g}; approximate_ARL0={arl[start]:.6g}')
