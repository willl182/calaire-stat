import numpy as np
# Covarianza OLS para diseño x=(0,1) y varianza de error conocida sigma2=1.
X = np.array([[1., 0.], [1., 1.]])
print(np.linalg.inv(X.T @ X))
