import numpy as np
# e = 0.00000001
bound = 100
fmax_10 = 1000
fmax_30 = 3000
fmax_50 = 5000
fmax_100 = 10000
vmax_10 = 360000
vmax_30 = 720000
vmax_50 = 1800000
vmax_100 = 3600000

def f(X, D):
    z = []
    fx, h = 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_11.txt")
    for k in range(D):
        z.append(X[k] - o[k])
    for j in range(0, D - 1):
        h += (z[j] - z[j + 1]) ** 2
    for i1 in range(len(z)):
        fx += z[i1]
    g = np.prod(np.array(z))
    h = h - 0.0001
    return fx, g, h

if __name__ == "__main__":
    n = np.array([1,2,3,4,5,6])
    print(np.sum(n+2))