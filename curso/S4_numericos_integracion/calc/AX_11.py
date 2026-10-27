from scipy.stats import chi2, t
from math import sqrt
n, mean, s, alpha = 10, .20, .30, .05
df = n-1
lo = s*sqrt(df/chi2.ppf(1-alpha/2, df))
hi = s*sqrt(df/chi2.ppf(alpha/2, df))
half = t.ppf(1-alpha/2, df)*s/sqrt(n)
print(f'df={df}; chi2_lo={chi2.ppf(alpha/2,df):.9g}; chi2_hi={chi2.ppf(1-alpha/2,df):.9g}; sigma_CI=({lo:.9g},{hi:.9g}); tcrit={t.ppf(1-alpha/2,df):.9g}; mean_CI=({mean-half:.9g},{mean+half:.9g})')

# One-sided limits used by M12-I (EPA one-point checks): d = -2, +1, -1, +2 %.
d = [-2., 1., -1., 2.]
nd = len(d); dfd = nd-1
md = sum(d)/nd
sd = sqrt(sum((v-md)**2 for v in d)/dfd)
q10 = chi2.ppf(.10, dfd)
L90 = sd*sqrt(dfd/q10)
ad = [abs(v) for v in d]
AB = sum(ad)/nd
AS = sqrt(sum((v-AB)**2 for v in ad)/dfd)
t95 = t.ppf(.95, dfd)
L95 = AB + t95*AS/sqrt(nd)
print(f'one_sided: s_d={sd:.6g}; chi2_0.10;3={q10:.6g}; L90={L90:.6g}; AB={AB:g}; AS={AS:.6g}; t_0.95;3={t95:.6g}; L95_AB={L95:.6g}')
