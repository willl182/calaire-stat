import numpy as np
rng = np.random.default_rng(20261025)
for m in (10_000, 40_000):
    # Example distribution with standard deviation 2; MC standard error is s/sqrt(M).
    draws = rng.normal(0., 2., size=m)
    print(f'M={m}; sample_sd={draws.std(ddof=1):.6g}; MC_SE_mean={draws.std(ddof=1)/np.sqrt(m):.6g}; theoretical={2/np.sqrt(m):.6g}')

# GUM-S1 7.2.2 and 7.9.2 applied to the M13-A1 example.
p = .95
print(f'M_min=10^4/(1-p)={1e4/(1-p):.0f}')
u_rounded, ndig = 1.0, 2  # u = 1,0 nmol/mol = 10 x 10^-1: l = -1
delta = .5*10**(-1)
d_low, d_high = 0.011715, 0.000601
print(f'u={u_rounded}; delta={delta:g}; d_low={d_low}; d_high={d_high}; favourable={max(d_low, d_high) <= delta}')
