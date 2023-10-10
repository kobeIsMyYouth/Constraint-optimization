import math
import numpy as np
# e = 1
bound = 10
fmax_10 = 10301000
fmax_30 = 30903000
fmax_50 = 51505000
fmax_100 = 103010000
vmax_10 = 4000
vmax_30 = 12000
vmax_50 = 20000
vmax_100 = 40000

def f(X, D):
    z = []
    fx, g1, g2 = 0, 0, 0
    o = np.loadtxt("./materis/shift_data_5.txt")[0:D]
    if D == 10:
        M1 = np.loadtxt("./materis/M1_5_D10.txt")
        M2 = np.loadtxt("./materis/M2_5_D10.txt")
    elif D == 30:
        M1 = np.loadtxt("./materis/M1_5_D30.txt")
        M2 = np.loadtxt("./materis/M2_5_D30.txt")
    elif D == 50:
        M1 = np.loadtxt("./materis/M1_5_D50.txt")
        M2 = np.loadtxt("./materis/M2_5_D50.txt")
    elif D == 100:
        M1 = np.loadtxt("./materis/M1_5_D100.txt")
        M2 = np.loadtxt("./materis/M2_5_D100.txt")
    else:
        print("D is not standard")
    for j in range(D):  # 维度
        z.append(X[j] - o[j])
    y = np.dot(M1, z)
    w = np.dot(M2, z)
    for i in range(D):
        g1 += y[i] ** 2 - 50 * math.cos(2 * math.pi * y[i]) - 40
        g2 += w[i] ** 2 - 50 * math.cos(2 * math.pi * w[i]) - 40
    for k in range(D - 1):
        fx += 100 * pow((z[k] ** 2 - z[k + 1]), 2) + (z[k] - 1) ** 2
    return fx, g1, g2