import numpy as np
import math

# cp = 0, e = 1
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
    o = np.loadtxt("./materis/shift_data_19.txt")
    for k in range(D):
        y.append(X[k] - o[k])
    for i in range(0, D):
        part2_g += pow(math.sin(2 * y[i]), 2)
        fx += pow(abs(y[i]), 0.5) + 2 * math.sin(pow(y[i], 3))
    for i1 in range(0, D - 1):
        part1_g += -10 * math.exp(-0.2 * math.sqrt(y[i1] ** 2 + y[i1 + 1] ** 2))
    g1 = part1_g + (D - 1) * 10 / math.exp(-5)
    g2 = part2_g - 0.5 * D
    return fx, g1, g2