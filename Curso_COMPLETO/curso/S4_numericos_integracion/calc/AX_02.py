# Ejemplo AX.2: entrada común y dos contribuciones independientes.
common, independent = 0.30, 0.20
v = common**2 + independent**2
cov = common**2
vd = v + v - 2*cov
print(f'varianza_individual={v:.9g}; covarianza={cov:.9g}; varianza_diferencia={vd:.9g}; u_diferencia={vd**0.5:.9g}; u_independencia={(2*v)**0.5:.9g}')
