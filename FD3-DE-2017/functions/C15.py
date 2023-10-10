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
    o = np.loadtxt("./materis/shift_data_15.txt")
    for k in range(D):
        y.append(X[k] - o[k])
    for i in range(0, D):
        sum_y += y[i] ** 2
    g = sum_y - 100 * D
    fx = max(list(map(abs, y)))
    h = math.cos(fx) + math.sin(fx)
    h = abs(h) - 0.0001
    return fx, g, h