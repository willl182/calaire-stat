from scipy.stats import norm
L, u = 10., 1.
for theta in (12., 8., 10.):
    p = norm.cdf((L-theta)/u)
    print(f'theta={theta:g}; P_Y_le_L={p:.9g}; P_Y_gt_L={1-p:.9g}')
