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
    o = np.loadtxt("./materis/shift_data_16.txt")
    for k in range(D):
        y.append(X[k] - o[k])
    for i in range(0, D):
        part_g += y[i] ** 2
        fx += abs(y[i])
    g = part_g - 100 * D
    h = pow(math.cos(fx) + math.sin(fx), 2) - math.exp(math.cos(fx) + math.sin(fx)) - 1 + math.exp(1)
    h = abs(h) - 0.0001
    return fx, g, h