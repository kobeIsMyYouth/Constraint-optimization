import math
import numpy as np
# e = 1
bound = 100
fmax_10 = 3850000.0
fmax_30 = 94550000.0
fmax_50 = 429250000.0
fmax_100 = 3383500000.0
vmax_10 = 200000
vmax_30 = 600000
vmax_50 = 1000000
vmax_100 = 2000000

def f(X, D):
    z = []
    fx, g, h = 0.0, 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_3.txt")
    for j in range(D):
        z.append(X[j] - o[j])
    for i in range(D):
        g += z[i] ** 2 - 5000 * math.cos(0.1 * math.pi * z[i]) - 4000
        h -= z[i] * math.sin(0.1 * math.pi * z[i])
        temp = 0.0
        for k in range(i + 1):
            temp += z[k]
        fx += temp ** 2
    h = abs(h)-0.0001 ###
    return fx, g, h

if __name__ == "__main__":
    print(f([1,1,1,1,1,1,1,1,1,1],10))