import math

import numpy as np

# e = 0.1
bound = 100
fmax_10 = 100200
fmax_30 = 300600
fmax_50 = 501000
fmax_100 = 1002000
vmax_10 = 101000
vmax_30 = 303000
vmax_50 = 505000
vmax_100 = 1010000

def f(X, D):
    y = []
    fx, part_g1, part_g2 = 0.0, 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_21.txt")[0:D]
    if D == 10:
        M = np.loadtxt("./materis/M_21_D10.txt")
    elif D == 30:
        M = np.loadtxt("./materis/M_21_D30.txt")
    elif D == 50:
        M = np.loadtxt("./materis/M_21_D50.txt")
    elif D == 100:
        M = np.loadtxt("./materis/M_21_D100.txt")
    else:
        print("D is not standard")

    for j in range(D):  # 维度
        y.append(X[j] - o[j])
    z = np.dot(M, y)
    for i in range(D):
        part_g1 += abs(z[i])
        part_g2 += z[i]**2
    for k in range(D):
        fx += z[k]**2 - 10 * math.cos(2*math.pi*z[k]) + 10
    g1 = 4 - part_g1
    g2 = part_g2 - 4
    return fx, g1, g2
