import math
import numpy as np
# e = 1
bound = 100
fmax_10 = 3850000.0
fmax_30 = 94550000.0
fmax_50 = 429250000.0
fmax_100 = 3383500000.0
vmax_10 = 200000
vmax_30 = 600000
vmax_50 = 1000000
vmax_100 = 2000000
def f(X, D):
    z = []
    fx = 0.0
    g = 0.0
    o = np.loadtxt("./materis/shift_data_2.txt")[0:D]
    if D == 10:
        M = np.loadtxt("./materis/M_2_D10.txt")
    elif D == 30:
        M = np.loadtxt("./materis/M_2_D30.txt")
    elif D == 50:
        M = np.loadtxt("./materis/M_2_D50.txt")
    elif D == 100:
        M = np.loadtxt("./materis/M_2_D100.txt")
    else:
        print("D is not standard")
    for j in range(D):  # 维度
        z.append(X[j] - o[j])
    y = np.dot(M, z)
    for i in range(D):
        g += y[i] ** 2 - 5000 * math.cos(0.1 * math.pi * y[i]) - 4000
        temp = 0.0
        for k in range(i + 1):
            temp += z[k]
        fx += temp**2
    return fx, g
