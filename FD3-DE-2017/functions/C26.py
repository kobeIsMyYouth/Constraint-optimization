import numpy as np
import math

# e = 0.01
bound = 100
fmax_10 = 25
fmax_30 = 75
fmax_50 = 125
fmax_100 = 250

vmax_10 = 100000
vmax_30 = 300000
vmax_50 = 500000
vmax_100 = 1000000

def f(X, D):
    y = []
    fx, g, part1_f, part2_f, part1_g, part2_g = 0.0, 0.0, 0.0, [], 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_26.txt")[0:D]
    for k in range(D):
        y.append(X[k] - o[k])
    if D == 10:
        M = np.loadtxt("./materis/M_26_D10.txt")
    elif D == 30:
        M = np.loadtxt("./materis/M_26_D30.txt")
    elif D == 50:
        M = np.loadtxt("./materis/M_26_D50.txt")
    elif D == 100:
        M = np.loadtxt("./materis/M_26_D100.txt")
    else:
        print("D is not standard")
    z = np.dot(M, y)

    for i in range(0, D):
        part1_f += z[i] ** 2
        for j in range(D):
            if j != i:
                part2_g += z[j] ** 2
        part1_g += np.sign(abs(z[i]) - part2_g - 1)
    for i1 in range(1, D + 1):
        part2_f.append(math.cos(z[i1 - 1] / math.sqrt(i1)))
    g = 1 - part1_g
    h = part1_f - 4 * D
    fx = part1_f / 4000 + 1 - np.prod(np.array(part2_f))
    h = abs(h) - 0.0001
    return fx, g, h