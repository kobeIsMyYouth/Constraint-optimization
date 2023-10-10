import numpy as np
import math

# e = 0.0001
bound = 100
fmax_10 = 22.71
fmax_30 = 22.71
fmax_50 = 22.71
fmax_100 = 22.71
vmax_10 = 200000
vmax_30 = 600000
vmax_50 = 1000000
vmax_100 = 2000000

def f(X, D):
    y = []
    fx, g, h, part_g, part1_f, = 0.0, 0.0, 0.0, 0.0, 0.0  # part_g + y[0]**2 = part_h
    o = np.loadtxt("./materis/shift_data_23.txt")[0:D]
    for k in range(D):
        y.append(X[k] - o[k])
    if D == 10:
        M = np.loadtxt("./materis/M_23_D10.txt")
    elif D == 30:
        M = np.loadtxt("./materis/M_23_D30.txt")
    elif D == 50:
        M = np.loadtxt("./materis/M_23_D50.txt")
    elif D == 100:
        M = np.loadtxt("./materis/M_23_D100.txt")
    else:
        print("D is not standard")
    z = np.dot(M, y)

    for i in range(1, D):
        part_g += z[i] ** 2
    g = part_g + 1 - abs(z[0])
    h = z[0] ** 2 + part_g - 4
    part2_f = z[0] ** 2 + part_g
    for j in range(0, D):
        part1_f += math.cos(2 * math.pi * z[j])
    fx = -20 * math.exp(-0.2 * math.sqrt(part2_f / D)) + 20 - math.exp(part1_f / D) + math.e
    h = abs(h) - 0.0001
    return fx, g, h