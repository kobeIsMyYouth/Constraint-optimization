import math
import numpy as np

# e = 0.001
bound = 100
fmax_10 = 1000
fmax_30 = 3000
fmax_50 = 5000
fmax_100 = 10000

vmax_10 = 100000
vmax_30 = 300000
vmax_50 = 500000
vmax_100 = 1000000

def f(X, D):
    y = []
    fx, g, part_g = 0.0, 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_25.txt")[0:D]
    for k in range(D):
        y.append(X[k] - o[k])
    if D == 10:
        M = np.loadtxt("./materis/M_25_D10.txt")
    elif D == 30:
        M = np.loadtxt("./materis/M_25_D30.txt")
    elif D == 50:
        M = np.loadtxt("./materis/M_25_D50.txt")
    elif D == 100:
        M = np.loadtxt("./materis/M_25_D100.txt")
    else:
        print("D is not standard")
    z = np.dot(M, y)
    for i in range(0, D):
        part_g += z[i] ** 2
        fx += abs(z[i])
    g = part_g - 100 * D
    h = pow(math.cos(fx) + math.sin(fx), 2) - math.exp(math.cos(fx) + math.sin(fx)) - 1 + math.exp(1)
    h = abs(h) - 0.0001
    return fx, g, h