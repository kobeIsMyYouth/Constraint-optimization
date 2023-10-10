import numpy as np
import math
# e = 1
bound = 100
fmax_10 = 5
fmax_30 = 15
fmax_50 = 25
fmax_100 = 50

vmax_10 = 4.5
vmax_30 = 4.5
vmax_50 = 4.5
vmax_100 = 4.5

def f(X, D):
    y = []
    fx, part1_g, part2_g, part1_f = 0.0, 0.0, 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_20.txt")
    for k in range(D):
        y.append(X[k] - o[k])
    for i1 in range(0, D):
        part1_g += y[i1]
    for i in range(D - 1):
        fx += g(y[i], y[i+1])
    g1 = pow(math.cos(part1_g), 2) - 0.25 * math.cos(part1_g) - 0.125
    g2 = math.exp(math.cos(part1_g)) - math.exp(0.25)
    fx = fx + g(y[D-1], y[0])
    return fx, g1, g2

def g(y1, y2):
    return 0.5 + (pow(math.sin(math.sqrt(y1 ** 2 + y2 ** 2)), 2) - 0.5) / pow(
            (1 + 0.001 * math.sqrt(y1 ** 2 + y2 ** 2)), 2)