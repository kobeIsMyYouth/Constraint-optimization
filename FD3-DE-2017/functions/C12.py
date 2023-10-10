import numpy as np
import math
# e = 1
bound = 100
fmax_10 = 100200
fmax_30 = 300600
fmax_50 = 501000
fmax_100 = 1002000
vmax_10 = 101000
vmax_30 = 303000
vmax_50 = 505000
vmax_100 = 1010000

def f(X, D):
    y = []
    fx, g1, g2 = 0.0, 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_12.txt")
    for k in range(D):
        y.append(X[k] - o[k])

    for i in range(0, D):
        g1 -= abs(y[i])
    for j in range(0, D):
        g2 += y[j] ** 2

    g1 = g1 + 4
    g2 = g2 - 4
    for i1 in range(D):
        fx += y[i1] ** 2 - 10 * math.cos(2 * math.pi * y[i1]) + 10
    return fx, g1, g2

if __name__ == "__main__":
    print(round(2.50,0))