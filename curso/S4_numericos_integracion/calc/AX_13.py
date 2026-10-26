import numpy as np
rng = np.random.default_rng(20261025)
for m in (10_000, 40_000):
    # Example distribution with standard deviation 2; MC standard error is s/sqrt(M).
    draws = rng.normal(0., 2., size=m)
    print(f'M={m}; sample_sd={draws.std(ddof=1):.6g}; MC_SE_mean={draws.std(ddof=1)/np.sqrt(m):.6g}; theoretical={2/np.sqrt(m):.6g}')
