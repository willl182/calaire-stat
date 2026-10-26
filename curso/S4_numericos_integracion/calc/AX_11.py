from scipy.stats import chi2, t
from math import sqrt
n, mean, s, alpha = 10, .20, .30, .05
df = n-1
lo = s*sqrt(df/chi2.ppf(1-alpha/2, df))
hi = s*sqrt(df/chi2.ppf(alpha/2, df))
half = t.ppf(1-alpha/2, df)*s/sqrt(n)
print(f'df={df}; chi2_lo={chi2.ppf(alpha/2,df):.9g}; chi2_hi={chi2.ppf(1-alpha/2,df):.9g}; sigma_CI=({lo:.9g},{hi:.9g}); tcrit={t.ppf(1-alpha/2,df):.9g}; mean_CI=({mean-half:.9g},{mean+half:.9g})')
