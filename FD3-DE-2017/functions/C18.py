import numpy as np
import math
# e = 0.00001
bound = 100
fmax_10 = 100200
fmax_30 = 300600
fmax_50 = 501000
fmax_100 = 1002000

vmax_10 = 12100000
vmax_30 = 36300000
vmax_50 = 60500000
vmax_100 = 121000000

def f(X, D):
    z, y = [], []
    fx, part1_h, part2_h, part1_g, part2_g = 0.0, 0.0, [], 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_18.txt")
    for k in range(D):
        y.append(X[k] - o[k])
        if abs(y[k]) < 0.5:
            z.append(y[k])
        else:
            z.append(0.5 * round(2 * y[k])) #四舍五入
    for i in range(0, D):
        part1_g += abs(y[i])
        part2_g += y[i] ** 2
        part2_h.append(pow(math.sin((y[i] - 1) * math.pi), 2))
        fx += z[i] ** 2 - 10 * math.cos(2 * math.pi * z[i]) + 10
    for j in range(0, D - 1):
        part1_h += 100 * pow((y[j] ** 2 - y[j + 1]), 2)
    g1 = 1 - part1_g
    g2 = part2_g - 100 * D
    h = part1_h + np.prod(np.array(part2_h))
    h = abs(h) - 0.0001
    return fx, g1, g2, h

if __name__ == "__main__":
    print(round(0.1))
