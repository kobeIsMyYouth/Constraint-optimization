import numpy as np
import math

# e = 0.01
# e = 0.01
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
    o = np.loadtxt("./materis/shift_data_22.txt")[0:D]
    if D == 10:
        M = np.loadtxt("./materis/M_22_D10.txt")
    elif D == 30:
        M = np.loadtxt("./materis/M_22_D30.txt")
    elif D == 50:
        M = np.loadtxt("./materis/M_22_D50.txt")
    elif D == 100:
        M = np.loadtxt("./materis/M_22_D100.txt")
    else:
        print("D is not standard")

    for k in range(D):
        y.append(X[k] - o[k])
    z = np.dot(M, y)

    for i in range(0, D):
        g1 += z[i] ** 2 - 10 * math.cos(2 * math.pi * z[i]) + 10
    for j in range(0, D):
        g2 += z[j]

    g1 = g1 - 100
    g2 = g2 - 2 * D
    g3 = 5 - (g2 + 2 * D)

    for i1 in range(D - 1):
        fx += 100 * (z[i1] ** 2 - z[i1 + 1]) ** 2 + (z[i1] - 1) ** 2
    return fx, g1, g2, g3