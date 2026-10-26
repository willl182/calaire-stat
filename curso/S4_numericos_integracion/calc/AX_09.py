from math import sqrt
common, independent = .30, .20
v = common**2 + independent**2
cov = common**2
print(f'var_individual={v:g}; cov={cov:g}; var_difference={2*v-2*cov:g}; u_difference={sqrt(2*v-2*cov):.9g}')
