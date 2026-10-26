"""Reproduce los ejemplos numéricos didácticos del capítulo M04."""
from math import ceil, sqrt

import numpy as np
from scipy import stats
from statsmodels.stats.power import TTestIndPower, TTestPower

# Vectores fijos y sintéticos. No son resultados de CALAIRE.
error_level = np.array([-0.8, 0.1, 0.4, -0.2, 0.7, 0.0, -0.5, 0.6])
paired_a = np.array([0.2, -0.1, 0.4, 0.0, 0.3, -0.2, 0.1, 0.5])
paired_b = np.array([0.0, -0.3, 0.2, 0.1, 0.1, -0.4, 0.0, 0.2])
welch_a = np.array([9.8, 10.2, 10.1, 9.9, 10.4, 9.7])
welch_b = np.array([10.7, 11.2, 10.8, 11.4, 10.9, 11.1, 10.6])
outlier = np.array([0.02, 0.04, 0.01, 0.03, 0.00, 0.05, 0.02, 0.28])


def show(name, **values):
    print(f"[{name}]")
    for key, value in values.items():
        print(f"{key}={value}")


# B: inferencia de una media (unidad independiente asumida: jornada/ciclo).
n = len(error_level)
mean = error_level.mean()
s = error_level.std(ddof=1)
se = s / sqrt(n)
df = n - 1
tcrit = stats.t.ppf(0.975, df)
tstat = mean / se
pvalue = 2 * stats.t.sf(abs(tstat), df)
show("B_media", datos=error_level.tolist(), n=n, media=mean, s=s, se=se,
     gl=df, tcrit_95=tcrit, IC95=(mean - tcrit * se, mean + tcrit * se),
     t=tstat, p=pvalue)

# I: t pareada aplicada a diferencias emparejadas; Welch para grupos distintos.
diff = paired_a - paired_b
n_pair = len(diff)
mean_diff = diff.mean()
s_diff = diff.std(ddof=1)
se_diff = s_diff / sqrt(n_pair)
df_pair = n_pair - 1
t_pair = mean_diff / se_diff
p_pair = 2 * stats.t.sf(abs(t_pair), df_pair)
t_pair_crit = stats.t.ppf(0.975, df_pair)
show("I_pareada", a=paired_a.tolist(), b=paired_b.tolist(), diferencias=diff.tolist(),
     media=mean_diff, s=s_diff, se=se_diff, gl=df_pair, t=t_pair, p=p_pair,
     IC95=(mean_diff-t_pair_crit*se_diff, mean_diff+t_pair_crit*se_diff))

n1, n2 = len(welch_a), len(welch_b)
m1, m2 = welch_a.mean(), welch_b.mean()
v1, v2 = welch_a.var(ddof=1), welch_b.var(ddof=1)
se_w = sqrt(v1/n1 + v2/n2)
df_w = (v1/n1 + v2/n2)**2 / ((v1/n1)**2/(n1-1) + (v2/n2)**2/(n2-1))
t_w = (m1-m2)/se_w
p_w = 2*stats.t.sf(abs(t_w), df_w)
t_wcrit = stats.t.ppf(0.975, df_w)
show("I_welch", A=welch_a.tolist(), B=welch_b.tolist(), media_A=m1,
     media_B=m2, s2_A=v1, s2_B=v2, diferencia=m1-m2, se=se_w, gl=df_w,
     t=t_w, p=p_w, IC95=(m1-m2-t_wcrit*se_w, m1-m2+t_wcrit*se_w))

# I: intervalo de confianza y prueba bilateral para una varianza normal.
var_sample = s**2
chi_lo = stats.chi2.ppf(0.025, df)
chi_hi = stats.chi2.ppf(0.975, df)
var_ci = (df*var_sample/chi_hi, df*var_sample/chi_lo)
variance_null = 0.25
chi_stat = df*var_sample/variance_null
p_var = 2*min(stats.chi2.cdf(chi_stat, df), stats.chi2.sf(chi_stat, df))
show("I_chi2_varianza", varianza_muestral=var_sample, gl=df,
     IC95_varianza=var_ci, varianza_H0=variance_null, chi2=chi_stat,
     p=p_var, cuantiles=(chi_lo, chi_hi))

# I: prueba F de razón de varianzas para dos muestras normales independientes.
ratio = v1/v2
f_lo, f_hi = stats.f.ppf(0.025, n1-1, n2-1), stats.f.ppf(0.975, n1-1, n2-1)
p_f = 2*min(stats.f.cdf(ratio, n1-1, n2-1), stats.f.sf(ratio, n1-1, n2-1))
show("I_F", razon=ratio, gl=(n1-1, n2-1), IC95_razon=(ratio/f_hi, ratio/f_lo),
     H0_razon=1, F=ratio, p=p_f, cuantiles=(f_lo, f_hi))

# I: cálculo de potencia bilateral y n para efectos definidos (Cohen d).
alpha = 0.05
power_solver = TTestPower()
ind_solver = TTestIndPower()
for label, effect, nobs in [("media", 0.5, 16), ("pareadas", 0.5, 16)]:
    power = power_solver.power(effect_size=effect, nobs=nobs, alpha=alpha,
                               alternative="two-sided")
    needed = power_solver.solve_power(effect_size=effect, power=0.80,
                                      alpha=alpha, alternative="two-sided")
    show(f"I_potencia_{label}", d=effect, n=nobs, alpha=alpha, potencia=power,
         n_para_80=needed, n_entero=ceil(needed))
effect_groups = 0.8
power_groups = ind_solver.power(effect_size=effect_groups, nobs1=12,
                                alpha=alpha, ratio=1.0,
                                alternative="two-sided")
n_groups = ind_solver.solve_power(effect_size=effect_groups, power=0.80,
                                  alpha=alpha, ratio=1.0,
                                  alternative="two-sided")
show("I_potencia_dos_grupos", d=effect_groups, n_por_grupo=12,
     alpha=alpha, potencia=power_groups, n_por_grupo_para_80=n_groups, n_entero_por_grupo=ceil(n_groups))

# I: incertidumbre estándar estimada de s bajo normalidad (aproximación).
u_s = s / sqrt(2*df)
show("I_incertidumbre_s", s=s, gl=df, u_s_aprox=u_s,
     formula="s/sqrt(2*gl)")

# I: diagnósticos de extremos; la decisión depende de supuestos y del diseño.
no = len(outlier)
mean_o = outlier.mean()
s_o = outlier.std(ddof=1)
g = max(abs(outlier-mean_o))/s_o
gcrit = 2.22  # tabla de Grubbs para n=8 y nivel 0,99.
sorted_outlier = np.sort(outlier)
q_dixon = (sorted_outlier[-1]-sorted_outlier[-2])/(sorted_outlier[-1]-sorted_outlier[0])
qcrit = 0.59  # tabla de Dixon para n=8 y nivel 0,99.
show("I_atipicos", datos=outlier.tolist(), n=no, media=mean_o, s=s_o,
     G=g, Gcrit= gcrit, Q_Dixon=q_dixon, Qcrit_Dixon=qcrit)

# A: Bonferroni para tres contrastes bilaterales y comparación con valores p.
family_p = np.array([0.012, 0.031, 0.20])
m = len(family_p)
alpha_family = 0.05
bonf_alpha = alpha_family/m
bonf_adjusted = np.minimum(family_p*m, 1)
show("A_multiplicidad", p=family_p.tolist(), m=m, alpha_familiar=alpha_family,
     alpha_por_prueba=bonf_alpha, p_ajustados=bonf_adjusted.tolist(),
     rechazos=(bonf_adjusted <= alpha_family).tolist())

# A: equivalencia TOST en un ejemplo de una media; margen fijado antes de ver datos.
margin = 0.5
mean_eq = 0.08
s_eq = 0.4
n_eq = 20
df_eq = n_eq-1
se_eq = s_eq/sqrt(n_eq)
t_lower = (mean_eq + margin)/se_eq
p_lower = stats.t.sf(t_lower, df_eq)
t_upper = (mean_eq - margin)/se_eq
p_upper = stats.t.cdf(t_upper, df_eq)
tost_ci_90 = stats.t.ppf(0.95, df_eq)
ci_eq=(mean_eq-tost_ci_90*se_eq,mean_eq+tost_ci_90*se_eq)
show("A_equivalencia", media=mean_eq, s=s_eq, n=n_eq, margen=(-margin,margin),
     se=se_eq, t_inferior=t_lower, p_inferior=p_lower,
     t_superior=t_upper, p_superior=p_upper, IC90=ci_eq,
     equivalente=(p_lower<0.05 and p_upper<0.05))

# A: consistencia de tres desviaciones frente al vector esperado bajo H0.
residual=np.array([0.12,-0.05,0.08])
standard_uncertainty=np.array([0.10,0.10,0.10])
q_consistency=float(np.sum((residual/standard_uncertainty)**2))
df_consistency=len(residual)
crit_consistency=stats.chi2.ppf(0.95,df_consistency)
p_consistency=stats.chi2.sf(q_consistency,df_consistency)
show("A_consistencia", residuos=residual.tolist(), u=standard_uncertainty.tolist(),
     chi2=q_consistency, gl=df_consistency, critico_95=crit_consistency,
     p=p_consistency, compatible=(q_consistency<=crit_consistency))
