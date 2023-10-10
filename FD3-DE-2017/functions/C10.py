import numpy as np

# e = 0.00001
bound = 100
fmax_10 = 100
fmax_30 = 100
fmax_50 = 100
fmax_100 = 100
vmax_10 = 200000
vmax_30 = 600000
vmax_50 = 1000000
vmax_100 = 2000000

def f(X, D):
    z = []
    h1, h2 = 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_10.txt")
    for k in range(D):
        z.append(X[k] - o[k])
    for i in range(0, D):
        temp = 0.0
        for j in range(i + 1):
            temp += z[j]
        h1 += temp**2
    for i1 in range(0, D - 1):
        h2 += (z[i1] - z[i1 + 1]) ** 2
    fx = np.max(z)
    h1 = h1 - 0.0001
    h2 = h2 - 0.0001
    return fx, h1, h2