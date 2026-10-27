d2, df = 3.2, 4
print(f'distance={d2:g}; df={df}; reduced_chi2={d2/df:g}')
from scipy.stats import chi2
q95 = chi2.ppf(.95, df)
print(f'chi2_0.95;{df}={q95:.6g}; consistent={d2 <= q95}')
