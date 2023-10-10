import numpy as np

# e = 0.0001
bound = 100
fmax_10 = 100
fmax_30 = 100
fmax_50 = 100
fmax_100 = 100
vmax_10 = 1100000
vmax_30 = 24800000.0
vmax_50 = 110500000.0
vmax_100 = 858500000.0

def f(X, D):
    z, w, y = [], [], []
    h1, h2 = 0.0, 0.0
    o = np.loadtxt("./materis/shift_data_8.txt")
    for k in range(D):
        z.append(X[k] - o[k])
    for w_l in range(0, D, 2): #偶数
        w.append((z[w_l]))
    for y_l in range(1, D, 2): #奇数
        y.append(z[y_l])
    for i1 in range(len(y)):
        temp = 0.0
        for j1 in range(i1 + 1):
            temp += y[j1]
        h1 += temp**2
    for i in range(0, int(D / 2)):
        temp = 0.0
        for j in range(i + 1):
            temp += w[j]
        h2 += temp**2
    fx = max(z)
    h1 = abs(h1) - 0.0001
    h2 = abs(h2) - 0.0001
    return fx, h1, h2

if __name__ == "__main__":
    D = 50
    sumu = 0.0
    for i in range(D):
        sumu += (i+1)*(i+1)
    print(sumu*100*100*2)