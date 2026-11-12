"""Reproduce ejemplos simulados de M07 y el contraste publicado ISO 28037."""
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


def ggmr(x, y, vx, vy):
    """Ajuste docente con Vxy=0; covarianzas absolutas, sin reescalar por Q."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    for matrix in (vx, vy):
        if matrix.shape != (len(x), len(x)) or not np.allclose(matrix, matrix.T):
            raise ValueError("Covarianza de dimensión incorrecta o no simétrica")
    lx, ly = np.linalg.cholesky(vx), np.linalg.cholesky(vy)
    def residual(theta):
        a, b = theta[:2]
        xt = theta[2:]
        return np.r_[np.linalg.solve(lx, x-xt),
                     np.linalg.solve(ly, y-a-b*xt)]
    fit = least_squares(residual, np.r_[0., 1., x])
    if not fit.success:
        raise RuntimeError(fit.message)
    covariance = np.linalg.inv(fit.jac.T @ fit.jac)[:2, :2]
    return fit, covariance


def main():
    # Ejemplo OLS simulado: seis niveles de referencia, error con signo.
    x = np.array([0, 100, 200, 300, 400, 500], dtype=float)
    y = np.array([0.2, 100.7, 200.1, 301.0, 400.4, 501.2], dtype=float)
    beta, resid, s2, covb = ols(x, y)
    a, b = beta
    s_res = np.sqrt(s2)
    r2 = 1 - np.sum(resid**2) / np.sum((y-y.mean())**2)
    print("OLS simulado: x=", x.tolist(), "y=", y.tolist())
    # M7 no incluye pruebas de correlación ni de pendiente (fuera del alcance de prop_e M7).
    print(f"R2={r2:.8f}; a={a:.8f}; b={b:.10f}")
    print("residuos=", np.round(resid, 8).tolist())
    print(f"s_res={s_res:.8f}; SE(a)={np.sqrt(covb[0,0]):.8f}; SE(b)={np.sqrt(covb[1,1]):.10f}; cov(a,b)={covb[0,1]:.10f}")
    print("R2 no es criterio autónomo de aceptación; cifras arriba son solo ajuste a datos simulados.")

    # Uso inverso: respuesta nueva simulada y corrección aditiva.
    y_new = 250.50
    xhat = (y_new-a)/b
    correction = xhat-y_new
    print(f"uso inverso para y={y_new:.2f}: xhat={xhat:.8f}; xhat-y={correction:.8f} nmol/mol")
    # u(y nueva) ya representa toda la dispersión de esa indicación.
    # ISO/TS 28037 11.1.3: no añadir de nuevo s_res como fuente independiente.
    u_y_new=0.20
    parameter_variance=covb[0,0]+xhat**2*covb[1,1]+2*xhat*covb[0,1]
    u2_xhat=(u_y_new**2+parameter_variance)/b**2
    u_xhat=np.sqrt(u2_xhat)
    # El bloque completo de parámetros comparte la estimación residual (4 g.l.).
    nu_eff=(u_y_new**2+parameter_variance)**2/(parameter_variance**2/(len(x)-2))
    k_inverse=stats.t.ppf(.975,nu_eff)
    print(f"incertidumbre inversa linealizada (u(y) total={u_y_new:.2f}): u(xhat)={u_xhat:.8f} nmol/mol; nu_eff={nu_eff:.8f}; k95={k_inverse:.8f}; U={k_inverse*u_xhat:.8f}")
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
    print("medias por nivel=", means.tolist())
    print("residuos absolutos de medias por nivel=", (means-(br[0]+br[1]*np.unique(xr))).tolist())
    print("residuos relativos por nivel (%)=",np.round(100*(means-(br[0]+br[1]*np.unique(xr)))/np.maximum(np.abs(means),1e-12),6).tolist())

    # GGMR demostrativo, con incertidumbre correlacionada entre x, Vxy=0.
    # Vx contiene una contribución común simulada además del término independiente.
    xobs=np.array([0.,100.,200.,300.,400.,500.])
    yobs=np.array([0.3,100.4,200.7,300.5,401.0,500.9])
    ux=np.array([0.25]*6); uy=np.array([0.40]*6)
    Vx=np.diag(ux**2)+(0.12**2)*np.ones((6,6))
    Vy=np.diag(uy**2)
    fit, covg = ggmr(xobs, yobs, Vx, Vy)
    ag,bg=fit.x[:2]; xadj=fit.x[2:]
    chi2=float(fit.fun@fit.fun)
    dof=len(xobs)-2
    pchi=stats.chi2.sf(chi2,dof)
    print("GGMR simulado (Vxy=0):")
    print(f"a={ag:.8f}; b={bg:.10f}; x ajustadas={np.round(xadj,8).tolist()}")
    print(f"chi2 ponderado={chi2:.8f}; g.l. declarados para el ejemplo={dof}; cola superior p={pchi:.8f}")
    print("Vx diagonal más componente común 0.12^2; Vy diagonal 0.40^2; Vxy=0")
    print("GGMR discrepancias blanqueadas zx=", np.round(fit.fun[:len(xobs)], 8).tolist())
    print("GGMR discrepancias blanqueadas zy=", np.round(fit.fun[len(xobs):], 8).tolist())
    assert np.isclose(np.sum(fit.fun**2), chi2)
    print("Son componentes del objetivo Q, no pruebas independientes por punto tras ajustar.")
    y_exact=0.3+1.001*xobs
    exact, _ = ggmr(xobs, y_exact, Vx, Vy)
    chi2_low=float(exact.fun@exact.fun)
    print(f"GGMR simulado con datos casi perfectamente lineales: chi2 ponderado={chi2_low:.12g}; mismo modelo y covarianzas")
    y_high=yobs.copy(); y_high[3]+=5.0
    high, _ = ggmr(xobs, y_high, Vx, Vy)
    chi2_high=float(high.fun@high.fun)
    print(f"GGMR simulado con discrepancia introducida en un punto: chi2 ponderado={chi2_high:.8f}; mismo modelo y covarianzas")
    # Misma orientación y mismos datos para los tres métodos.
    Xg = np.column_stack((np.ones(len(xobs)), xobs))
    bo = np.linalg.lstsq(Xg, yobs, rcond=None)[0]
    bw = np.linalg.lstsq(Xg / uy[:, None], yobs / uy, rcond=None)[0]
    _, cov_no_common = ggmr(xobs, yobs, np.diag(ux**2), Vy)
    print(f"Mismo conjunto: OLS={bo}; WLS={bw}; GGMR={fit.x[:2]}")
    print(f"Componente común: u(a) con={np.sqrt(covg[0,0]):.8f}, sin={np.sqrt(cov_no_common[0,0]):.8f}; u(b)={np.sqrt(covg[1,1]):.10f}")
    print(f"GGMR colas: inferior={stats.chi2.cdf(chi2,dof):.8f}; superior con discrepancia={stats.chi2.sf(chi2_high,dof):.8g}")

    # Publicado: ISO/TS 28037:2010, 10.3, tablas 25-26, pp. 35-36.
    xp = np.array([50.4, 99., 149.9, 200.4, 248.5, 299.7, 349.1])
    yp = np.array([52.3, 97.8, 149.7, 200.1, 250.4, 300.9, 349.2])
    vxp = np.array([[.50,0,.25,0,.25,0,.25], [0,1.25,1,0,0,1,1],
                    [.25,1,1.50,0,.25,1,1.25], [0,0,0,1.25,1,1,1],
                    [.25,0,.25,1,1.50,1,1.25], [0,1,1,1,1,2.25,2],
                    [.25,1,1.25,1,1.25,2,2.50]])
    vyp = 4*np.eye(7) + np.ones((7,7))
    fp, cp = ggmr(xp, yp, vxp, vyp)
    qp = float(fp.fun @ fp.fun)
    print(f"ISO publicado: a={fp.x[0]:.8f}; b={fp.x[1]:.8f}; Q={qp:.8f}; u(a)={np.sqrt(cp[0,0]):.8f}; u(b)={np.sqrt(cp[1,1]):.8f}; cov={cp[0,1]:.8f}")
    assert np.allclose(fp.x[:2], [.3424, 1.0012], atol=5e-5, rtol=0)
    assert abs(qp-1.772) < .0005
    assert np.allclose(np.sqrt(np.diag(cp)), [2.0569, .0090], atol=5e-5, rtol=0)
    assert abs(cp[0,1] - (-.0129)) < 5e-5
    assert np.allclose(fp.x[2:], [50.5727,98.5682,149.6080,200.4286,248.7393,299.4759,348.8921], atol=5e-5, rtol=0)
    print("Contraste ISO: parámetros, abscisas y Q concuerdan con el redondeo publicado; no valida todos los casos Vxy=0.")


if __name__ == '__main__':
    main()
