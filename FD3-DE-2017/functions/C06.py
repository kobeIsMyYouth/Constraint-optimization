import math
import numpy as np
# e = 1
bound = 20
fmax_10 = 1300
fmax_30 = 3900
fmax_50 = 6500
fmax_100 = 13000
vmax_10 = 2400
vmax_30 = 7200
vmax_50 = 12000
vmax_100 = 24000

def f(X, D):
    z = []
    fx = 0
    h1, h2, h3, h4, h5, h6 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_6.txt")
    for j in range(D):
        z.append(X[j] - o[j])
    for i in range(D):
        h1 -= z[i] * math.sin(z[i])
        h2 += z[i] * math.sin(math.pi * z[i])
        h3 -= z[i] * math.cos(z[i])
        h4 += z[i] * math.cos(math.pi * z[i])
        h5 += z[i] * math.sin(2 * np.sqrt(np.abs(z[i])))
        h6 -= z[i] * math.sin(2 * np.sqrt(np.abs(z[i])))
        fx += z[i] ** 2 - 10 * math.cos(2 * math.pi * z[i]) + 10
    h1 = np.abs(h1) - 0.0001
    h2 = np.abs(h2) - 0.0001
    h3 = np.abs(h3) - 0.0001
    h4 = np.abs(h4) - 0.0001
    h5 = np.abs(h5) - 0.0001
    h6 = np.abs(h6) - 0.0001
    return fx, h1, h2, h3, h4, h5, h6
if __name__ == "__main__":
    X = [-0.74218096, 5.88715354, 6.49704012, 9.1265041,  9.308883,
         7.07408455, -9.4904145, -4.28443379, -4.29366117, -8.67718072]
    print(f(X, 10))