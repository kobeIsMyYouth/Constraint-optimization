import numpy as np
import math

# e = 1
bound = 50
fmax_10 = 110
fmax_30 = 330
fmax_50 = 550
fmax_100 = 1100

vmax_10 = 1100
vmax_30 = 3300
vmax_50 = 5500
vmax_100 = 11000

def f(X, D):
    y, fx, part1_g, part2_g = [], 0.0, 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_28.txt")[0:D]
    for k in range(D):
        y.append(X[k] - o[k])
    if D == 10:
        M = np.loadtxt("./materis/M_28_D10.txt")
    elif D == 30:
        M = np.loadtxt("./materis/M_28_D30.txt")
    elif D == 50:
        M = np.loadtxt("./materis/M_28_D50.txt")
    elif D == 100:
        M = np.loadtxt("./materis/M_28_D100.txt")
    else:
        print("D is not standard")
    z = np.dot(M, y)

    for i in range(0, D):
        part2_g += pow(math.sin(2 * z[i]), 2)
        fx += pow(abs(z[i]), 0.5) + 2 * math.sin(pow(z[i], 3))
    for i1 in range(0, D - 1):
        part1_g += -10 * math.exp(-0.2 * math.sqrt(z[i1] ** 2 + z[i1 + 1] ** 2))
    g1 = part1_g + (D - 1) * 10 / math.exp(-5)
    g2 = part2_g - 0.5 * D
    return fx, g1, g2