import math
import numpy as np
# e = 1
# e = 0.1
bound = 50
fmax_10 = 1000
fmax_30 = 3000
fmax_50 = 50000
fmax_100 = 100000
vmax_10 = 6000
vmax_30 = 18000
vmax_50 = 30000
vmax_100 = 60000

def f(X, D):
    z = []
    fx = 0
    h1, h2 = 0, 0
    o = np.loadtxt("./materis/shift_data_7.txt")
    for j in range(D):
        z.append(X[j] - o[j])
    for i in range(D):
        h1 += z[i] - 100 * math.cos(0.5 * z[i]) + 100
        h2 -= z[i] - 100 * math.cos(0.5 * z[i]) + 100
        fx += z[i] * math.sin(z[i])
    h1 = np.abs(h1) - 0.0001
    h2 = np.abs(h2) - 0.0001
    return fx, h1, h2