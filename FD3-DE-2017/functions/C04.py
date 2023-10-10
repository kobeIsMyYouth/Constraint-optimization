import math
import numpy as np
# e = 1
bound = 10
fmax_10 = 1300
fmax_30 = 3900
fmax_50 = 6500
fmax_100 = 13000
vmax_10 = 400
vmax_30 = 1200
vmax_50 = 2000
vmax_100 = 4000

def f(X, D):
    z = []
    fx, g1, g2 = 0.0, 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_4.txt")
    for j in range(D):
        z.append(X[j] - o[j])
    for i in range(D):
        g1 -= z[i] * math.sin(2 * z[i])
        g2 += z[i] * math.sin(z[i])
        fx += z[i] ** 2 - 10 * math.cos(2 * math.pi * z[i]) + 10
    return fx, g1, g2
