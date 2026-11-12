from math import sqrt
a, b, y = 1., 2., 11.
uy, ua, ub, covab = .20, .10, .02, -.001
xhat = (y-a)/b
numerator = uy**2 + ua**2 + xhat**2*ub**2 + 2*xhat*covab
print(f'xhat={xhat:g}; numerador={numerator:.9g}; varianza={numerator/b**2:.9g}; u={sqrt(numerator/b**2):.9g}')
