import numpy as np
import math
# e = 1
bound = 100
fmax_10 = 10301000
fmax_30 = 30903000
fmax_50 = 51505000
fmax_100 = 103010000
vmax_10 = 102200
vmax_30 = 306600
vmax_50 = 511000
vmax_100 = 1022000

def f(X, D):
    y = []
    fx, g1, g2 = 0.0, 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_13.txt")
    for k in range(D):
        y.append(X[k] - o[k])
    for i in range(0, D):
        g1 += y[i] ** 2 - 10 * math.cos(2 * math.pi * y[i]) + 10
    for j in range(0, D):
        g2 += y[j]

    g1 = g1 - 100
    g2 = g2 - 2 * D
    g3 = 5 - (g2 + 2 * D)

    for i1 in range(D - 1):
        fx += 100 * (y[i1] ** 2 - y[i1 + 1]) ** 2 + (y[i1] - 1) ** 2
    return fx, g1, g2, g3
