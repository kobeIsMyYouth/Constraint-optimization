import numpy as np
import math

# e = 0.001
bound = 100
fmax_10 = 100
fmax_30 = 100
fmax_50 = 100
fmax_100 = 100

vmax_10 = 100000
vmax_30 = 300000
vmax_50 = 500000
vmax_100 = 1000000

def f(X, D):
    y = []
    fx, g, sum_y = 0.0, 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_24.txt")[0:D]
    for k in range(D):
        y.append(X[k] - o[k])
    if D == 10:
        M = np.loadtxt("./materis/M_24_D10.txt")
    elif D == 30:
        M = np.loadtxt("./materis/M_24_D30.txt")
    elif D == 50:
        M = np.loadtxt("./materis/M_24_D50.txt")
    elif D == 100:
        M = np.loadtxt("./materis/M_24_D100.txt")
    else:
        print("D is not standard")
    z = np.dot(M, y)

    for i in range(0, D):
        sum_y += z[i] ** 2
    g = sum_y - 100 * D
    fx = max(list(map(abs, z)))
    h = math.cos(fx) + math.sin(fx)
    h = abs(h) - 0.0001
    return fx, g, h