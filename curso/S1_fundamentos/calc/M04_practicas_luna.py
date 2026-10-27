"""Cálculos reproducibles para las prácticas aplicadas de M04.

Todos los vectores son sintéticos, fijos y no representan datos de CALAIRE.
"""
from math import sqrt, ceil
import numpy as np
from scipy import stats
from statsmodels.stats.power import TTestPower, TTestIndPower

# B: una jornada independiente por valor en un único nivel.
b = np.array([-0.4, 0.2, 0.1, 0.5, -0.1, 0.3, 0.0, 0.6])
n = len(b); mean = b.mean(); s = b.std(ddof=1); se = s/sqrt(n); df=n-1
crit=stats.t.ppf(.975,df); t=mean/se
print('B', 'datos=',b.tolist(),'n=',n,'media=',mean,'s=',s,'se=',se,'gl=',df,
      'IC95=',(mean-crit*se,mean+crit*se),'t=',t,'p=',2*stats.t.sf(abs(t),df))
margin=.30
ci95=(mean-crit*se,mean+crit*se)
descarta_magnitud=ci95[0]>-margin and ci95[1]<margin
print('B_margen', 'magnitud_relevante=',margin,'IC95=',ci95,
      'descarta_magnitud=',descarta_magnitud)
assert not descarta_magnitud

# I: cada par corresponde a una jornada; Welch usa grupos independientes.
a=np.array([.1,.4,-.2,.5,.3,-.1,.6,.2]); bb=np.array([-.1,.2,-.1,.1,0,-.3,.2,0])
d=a-bb; nd=len(d); md=d.mean(); sd=d.std(ddof=1); sed=sd/sqrt(nd); td=md/sed
cd=stats.t.ppf(.975,nd-1)
paired_ref=stats.ttest_rel(a,bb)
print('I_pareada', 'diferencias=',d.tolist(),'media=',md,'s=',sd,'se=',sed,
      'gl=',nd-1,'IC95=',(md-cd*sed,md+cd*sed),'t=',td,'p=',2*stats.t.sf(abs(td),nd-1),
      'SciPy_t=',paired_ref.statistic,'SciPy_p=',paired_ref.pvalue)
assert np.isclose(td,paired_ref.statistic) and np.isclose(2*stats.t.sf(abs(td),nd-1),paired_ref.pvalue)
g1=np.array([9.6,10.0,10.3,9.8,10.5,9.9]); g2=np.array([10.4,11.0,10.7,11.5,10.8,11.3,10.6])
n1,n2=len(g1),len(g2); m1,m2=g1.mean(),g2.mean(); v1,v2=g1.var(ddof=1),g2.var(ddof=1)
sew=sqrt(v1/n1+v2/n2); dfw=(v1/n1+v2/n2)**2/((v1/n1)**2/(n1-1)+(v2/n2)**2/(n2-1)); tw=(m1-m2)/sew; cw=stats.t.ppf(.975,dfw)
welch_ref=stats.ttest_ind(g1,g2,equal_var=False)
print('I_Welch','medias=',m1,m2,'s2=',v1,v2,'dif=',m1-m2,'se=',sew,'gl=',dfw,
      'IC95=',(m1-m2-cw*sew,m1-m2+cw*sew),'t=',tw,'p=',2*stats.t.sf(abs(tw),dfw),
      'SciPy_t=',welch_ref.statistic,'SciPy_p=',welch_ref.pvalue)
assert np.isclose(tw,welch_ref.statistic) and np.isclose(2*stats.t.sf(abs(tw),dfw),welch_ref.pvalue)
chi=df*s*s/.25; chi_ci=(df*s*s/stats.chi2.ppf(.975,df),df*s*s/stats.chi2.ppf(.025,df)); pchi=2*min(stats.chi2.cdf(chi,df),stats.chi2.sf(chi,df))
print('I_chi2','s2=',s*s,'IC95=',chi_ci,'H0_s2=.25','chi2=',chi,'p=',pchi)
ratio=v1/v2; df1=n1-1; df2=n2-1; fc=stats.f.ppf([.025,.975],df1,df2); pf=2*min(stats.f.cdf(ratio,df1,df2),stats.f.sf(ratio,df1,df2))
print('I_F','ratio=',ratio,'IC95=',(ratio/fc[1],ratio/fc[0]),'F=',ratio,'gl=',df1,df2,'p=',pf)
for label,effect,solver,kwargs in [('media',.5,TTestPower(),{}),('parejas',.5,TTestPower(),{}),('dos_grupos',.5,TTestIndPower(),{'ratio':1.0})]:
    if label=='dos_grupos':
        needed=solver.solve_power(effect_size=effect,nobs1=None,alpha=.05,power=.80,alternative='two-sided',**kwargs)
        actual=solver.power(effect_size=effect,nobs1=12,alpha=.05,alternative='two-sided',**kwargs)
        dfp=22
        ncp=effect*sqrt(12/2)
        direct=stats.nct.cdf(stats.t.ppf(.025,dfp),dfp,ncp)+stats.nct.sf(stats.t.ppf(.975,dfp),dfp,ncp)
        assert np.isclose(actual,direct,atol=1e-10)
        ncp_target=effect*sqrt(needed/2)
        df_target=2*needed-2
        power_target=stats.nct.cdf(stats.t.ppf(.025,df_target),df_target,ncp_target)+stats.nct.sf(stats.t.ppf(.975,df_target),df_target,ncp_target)
        print('I_potencia',label,'n_objetivo_por_grupo=',needed,'entero=',ceil(needed),'potencia_12=',actual,'nct=',direct,'potencia_objetivo=',power_target)
    else:
        needed=solver.solve_power(effect_size=effect,nobs=None,alpha=.05,power=.80,alternative='two-sided')
        actual=solver.power(effect_size=effect,nobs=16,alpha=.05,alternative='two-sided')
        dfp=15
        ncp=effect*sqrt(16)
        direct=stats.nct.cdf(stats.t.ppf(.025,dfp),dfp,ncp)+stats.nct.sf(stats.t.ppf(.975,dfp),dfp,ncp)
        assert np.isclose(actual,direct,atol=1e-10)
        print('I_potencia',label,'n_objetivo=',needed,'entero=',ceil(needed),'potencia_16=',actual,'nct=',direct)
print('I_u_s','s=',s,'gl=',df,'u_s=',s/sqrt(2*df))
# Grubbs unilateral para un extremo alto; Q de Dixon didáctico suministrado.
o=np.array([.01,.05,.02,.04,.03,.00,.06,.18]); so=o.std(ddof=1); go=(o.max()-o.mean())/so
q=np.sort(o); qo=(q[-1]-q[-2])/(q[-1]-q[0]); tg=stats.t.ppf(1-.01/len(o),len(o)-2); gc=(len(o)-1)/sqrt(len(o))*sqrt(tg*tg/(len(o)-2+tg*tg)); qcrit=.59
print('I_extremos','media=',o.mean(),'s=',so,'G=',go,'Gcrit_unilateral=',gc,'Q=',qo,'Qcrit_suministrado_didactico=',qcrit)

# A: tres pruebas en una familia prefijada; TOST con el margen docente ±0,30.
p=np.array([.012,.031,.20]); print('A_Bonferroni','alpha_por_prueba=',.05/3,'p_ajustados=',np.minimum(3*p,1).tolist())
me, se_= .08,.4/sqrt(20); dfe=19; mar=.30; tlo=(me+mar)/se_; thi=(me-mar)/se_
print('A_TOST','SE=',se_,'IC90=',(me-stats.t.ppf(.95,dfe)*se_,me+stats.t.ppf(.95,dfe)*se_),
      't_inferior=',tlo,'p_inferior=',stats.t.sf(tlo,dfe),'t_superior=',thi,'p_superior=',stats.t.cdf(thi,dfe))
res=np.array([.16,-.08,.04]); u=np.full(3,.10); qstat=np.sum((res/u)**2)
V=np.diag(u**2); qmatrix=float(res @ np.linalg.solve(V,res))
print('A_chi2','Q=',qstat,'Q_matricial=',qmatrix,'gl=3','critico=',stats.chi2.ppf(.95,3),'p=',stats.chi2.sf(qstat,3))

# Comprobaciones de colas, coberturas y umbrales de tamaños muestrales.
assert np.isclose(ci95[0],mean-crit*se) and np.isclose(qstat,qmatrix)
assert np.isclose(md,d.mean()) and np.isclose(m1-m2,g1.mean()-g2.mean())
assert np.isclose(go,2.3156757298039623) and np.isclose(qo,2/3)
assert stats.t.sf(tlo,dfe)<.05 and stats.t.cdf(thi,dfe)<.05
print('comprobaciones_practicas_M04=OK')
