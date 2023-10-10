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
vmax_100 = 121000000000000

def f(X, D):
    z, y = [], []
    fx, part1_h, part2_h, part1_g, part2_g = 0.0, 0.0, [], 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_27.txt")[0:D]
    for k in range(D):
        y.append(X[k] - o[k])
    if D == 10:
        M = np.loadtxt("./materis/M_27_D10.txt")
    elif D == 30:
        M = np.loadtxt("./materis/M_27_D30.txt")
    elif D == 50:
        M = np.loadtxt("./materis/M_27_D50.txt")
    elif D == 100:
        M = np.loadtxt("./materis/M_27_D100.txt")
    else:
        print("D is not standard")
    z = np.dot(M, y)

    for i in range(0, D):
        part1_g += abs(z[i])
        part2_g += z[i] ** 2
        part2_h.append(pow(math.sin((z[i] - 1) * math.pi), 2))

    for j in range(0, D - 1):
        part1_h += 100 * pow((z[j] ** 2 - z[j + 1]), 2)

    g1 = 1 - part1_g
    g2 = part2_g - 100 * D
    h = part1_h + np.prod(np.array(part2_h))
    h = abs(h) - 0.0001
    for k in range(D):
        if abs(z[k]) < 0.5:
            z[k] = z[k]
        else:
            z[k] = 0.5 * round(2 * z[k]) #四舍五入
        fx += z[k] ** 2 - 10 * math.cos(2 * math.pi * z[k]) + 10
    return fx, g1, g2, h

if __name__ == "__main__":
    print(round(0.1))
