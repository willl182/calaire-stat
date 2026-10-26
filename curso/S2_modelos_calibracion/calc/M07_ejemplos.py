"""Reproduce los ejemplos numéricos simulados de M07."""
import numpy as np
from scipy import stats
from scipy.optimize import least_squares


def ols(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    X = np.column_stack((np.ones(len(x)), x))
    beta = np.linalg.solve(X.T @ X, X.T @ y)
    residuals = y - X @ beta
    sse = residuals @ residuals
    s2 = sse / (len(x) - 2)
    cov_beta = s2 * np.linalg.inv(X.T @ X)
    return beta, residuals, s2, cov_beta


def main():
    # Ejemplo OLS simulado: seis niveles de referencia, error con signo.
    x = np.array([0, 100, 200, 300, 400, 500], dtype=float)
    y = np.array([0.2, 100.7, 200.1, 301.0, 400.4, 501.2], dtype=float)
    beta, resid, s2, covb = ols(x, y)
    a, b = beta
    s_res = np.sqrt(s2)
    r = np.corrcoef(x, y)[0, 1]
    t_slope = (b - 1.0) / np.sqrt(covb[1, 1])
    p_slope = 2 * stats.t.sf(abs(t_slope), len(x)-2)
    r2 = 1 - np.sum(resid**2) / np.sum((y-y.mean())**2)
    print("OLS simulado: x=", x.tolist(), "y=", y.tolist())
    t_r = r*np.sqrt((len(x)-2)/(1-r**2))
    p_r = 2*stats.t.sf(abs(t_r),len(x)-2)
    print(f"Pearson r={r:.8f}; prueba rho=0: t={t_r:.8f}, g.l.={len(x)-2}, p={p_r:.8g}; R2={r2:.8f}; a={a:.8f}; b={b:.10f}")
    print("residuos=", np.round(resid, 8).tolist())
    print(f"s_res={s_res:.8f}; SE(a)={np.sqrt(covb[0,0]):.8f}; SE(b)={np.sqrt(covb[1,1]):.10f}; cov(a,b)={covb[0,1]:.10f}")
    print(f"prueba de pendiente b=1: t={t_slope:.8f}; g.l.={len(x)-2}; p={p_slope:.8f}")
    print("R2 no es criterio autónomo de aceptación; cifras arriba son solo ajuste a datos simulados.")

    # Uso inverso: respuesta nueva simulada y corrección aditiva.
    y_new = 250.50
    xhat = (y_new-a)/b
    correction = xhat-y_new
    print(f"uso inverso para y={y_new:.2f}: xhat={xhat:.8f}; xhat-y={correction:.8f} nmol/mol")
    u_y_new=0.20
    u2_xhat=(u_y_new**2+s_res**2+covb[0,0]+xhat**2*covb[1,1]+2*xhat*covb[0,1])/b**2
    u_xhat=np.sqrt(u2_xhat)
    print(f"incertidumbre inversa linealizada (u(y)={u_y_new:.2f}, covarianza de parámetros): u(xhat)={u_xhat:.8f} nmol/mol; k_t95={stats.t.ppf(.975,len(x)-2):.8f}; U={stats.t.ppf(.975,len(x)-2)*u_xhat:.8f}")
    # Intervalo de confianza de la media de respuesta y predicción de nueva lectura.
    x0 = 250.0
    X0 = np.array([1.0, x0])
    mean_hat = X0 @ beta
    leverage = X0 @ np.linalg.inv(np.column_stack((np.ones(len(x)),x)).T @ np.column_stack((np.ones(len(x)),x))) @ X0
    tcrit = stats.t.ppf(.975, len(x)-2)
    ci_mean = tcrit * np.sqrt(s2*leverage)
    pi_new = tcrit * np.sqrt(s2*(1+leverage))
    print(f"en x={x0:.1f}: yhat={mean_hat:.8f}; IC95 media ±{ci_mean:.8f}; IP95 nueva lectura ±{pi_new:.8f}")
    print(f"recta forzada al origen: pendiente={x@y/(x@x):.10f}; intercepto fijado=0")

    # OLS frente a WLS: precisión de la respuesta crece con concentración.
    xw = np.array([0,100,200,300,400,500], dtype=float)
    yw = np.array([0.4,100.5,200.8,300.2,401.4,500.5], dtype=float)
    uw = np.array([0.25,0.30,0.40,0.60,0.90,1.20])
    Xw = np.column_stack((np.ones(len(xw)),xw))
    bw_ols = np.linalg.lstsq(Xw,yw,rcond=None)[0]
    W = np.diag(1/uw**2)
    bw_wls = np.linalg.solve(Xw.T@W@Xw,Xw.T@W@yw)
    print("WLS simulado: incertidumbres estándar y=",uw.tolist())
    print(f"OLS a={bw_ols[0]:.8f}, b={bw_ols[1]:.10f}; WLS a={bw_wls[0]:.8f}, b={bw_wls[1]:.10f}")
    print("pesos relativos 1/u(y)^2=",np.round(1/uw**2,6).tolist())

    # Validación WLS ilustrativa con 12 niveles y errores estándar conocidos.
    xv=np.linspace(0,550,12)
    deviations=np.array([0.10,-0.20,0.15,-0.10,0.25,-0.15,0.20,-0.25,0.10,-0.10,0.15,-0.05])
    yv=0.3+1.001*xv+deviations
    uv=np.linspace(0.30,0.85,12)
    Xv=np.column_stack((np.ones(len(xv)),xv))
    Wv=np.diag(1/uv**2)
    betav=np.linalg.solve(Xv.T@Wv@Xv,Xv.T@Wv@yv)
    weighted_res=(yv-Xv@betav)/uv
    chi2_wls=float(weighted_res@weighted_res)
    df_wls=len(xv)-2
    chi2_crit=stats.chi2.ppf(.95,df_wls)
    print(f"validación WLS simulada, 12 puntos: chi2_obs={chi2_wls:.8f}; g.l.={df_wls}; chi2_0.95={chi2_crit:.8f}; max|residuo ponderado|={np.max(np.abs(weighted_res)):.8f}")

    # Falta de ajuste: réplicas independientes de y al mismo x.
    xr = np.repeat([0.,100.,200.,300.], 3)
    yr = np.array([0.1,0.2,0.3, 100.2,100.1,100.3,
                   200.0,200.1,200.2, 301.0,301.1,301.2])
    br, rr, sr2, _ = ols(xr,yr)
    grand = yr.mean()
    means = np.array([yr[xr==v].mean() for v in np.unique(xr)])
    ss_lof = sum(np.sum(xr==v)*(m-(br[0]+br[1]*v))**2 for v,m in zip(np.unique(xr),means))
    ss_pe = sum(np.sum((yr[xr==v]-yr[xr==v].mean())**2) for v in np.unique(xr))
    m, N = len(np.unique(xr)), len(yr)
    F_lof = (ss_lof/(m-2))/(ss_pe/(N-m))
    p_lof = stats.f.sf(F_lof,m-2,N-m)
    print(f"falta de ajuste simulada: a={br[0]:.8f}, b={br[1]:.10f}; SS_LOF={ss_lof:.8f}; SS_PE={ss_pe:.8f}; F({m-2},{N-m})={F_lof:.8f}; p={p_lof:.8f}")
    print("residuos relativos por nivel (%)=",np.round(100*(means-(br[0]+br[1]*np.unique(xr)))/np.maximum(np.abs(means),1e-12),6).tolist())

    # GGMR demostrativo, con incertidumbre correlacionada entre x, Vxy=0.
    # Vx contiene una contribución común simulada además del término independiente.
    xobs=np.array([0.,100.,200.,300.,400.,500.])
    yobs=np.array([0.3,100.4,200.7,300.5,401.0,500.9])
    ux=np.array([0.25]*6); uy=np.array([0.40]*6)
    Vx=np.diag(ux**2)+(0.12**2)*np.ones((6,6))
    Vy=np.diag(uy**2)
    Lx=np.linalg.cholesky(Vx); Ly=np.linalg.cholesky(Vy)
    def objective(theta):
        aa,bb=theta[:2]; xt=theta[2:]
        rx=np.linalg.solve(Lx,xobs-xt)
        ry=np.linalg.solve(Ly,yobs-(aa+bb*xt))
        return np.r_[rx,ry]
    init=np.r_[0.,1.,xobs]
    fit=least_squares(objective,init)
    ag,bg=fit.x[:2]; xadj=fit.x[2:]
    chi2=float(fit.fun@fit.fun)
    dof=len(xobs)-2
    pchi=stats.chi2.sf(chi2,dof)
    print("GGMR simulado (Vxy=0):")
    print(f"a={ag:.8f}; b={bg:.10f}; x ajustadas={np.round(xadj,8).tolist()}")
    print(f"chi2 ponderado={chi2:.8f}; g.l. declarados para el ejemplo={dof}; cola superior p={pchi:.8f}")
    print("Vx diagonal más componente común 0.12^2; Vy diagonal 0.40^2; Vxy=0")
    y_exact=0.3+1.001*xobs
    def objective_exact(theta):
        aa,bb=theta[:2]; xt=theta[2:]
        return np.r_[np.linalg.solve(Lx,xobs-xt),
                     np.linalg.solve(Ly,y_exact-(aa+bb*xt))]
    exact=least_squares(objective_exact,np.r_[0.,1.,xobs])
    chi2_low=float(exact.fun@exact.fun)
    print(f"GGMR simulado con datos casi perfectamente lineales: chi2 ponderado={chi2_low:.12g}; mismo modelo y covarianzas")
    y_high=yobs.copy(); y_high[3]+=5.0
    def objective_high(theta):
        aa,bb=theta[:2]; xt=theta[2:]
        return np.r_[np.linalg.solve(Lx,xobs-xt),
                     np.linalg.solve(Ly,y_high-(aa+bb*xt))]
    high=least_squares(objective_high,np.r_[0.,1.,xobs])
    chi2_high=float(high.fun@high.fun)
    print(f"GGMR simulado con discrepancia introducida en un punto: chi2 ponderado={chi2_high:.8f}; mismo modelo y covarianzas")


if __name__ == '__main__':
    main()
