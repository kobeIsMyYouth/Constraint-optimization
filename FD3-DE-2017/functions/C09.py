import numpy as np

# e = 0.00001
# e = 0.00001
bound = 10
fmax_10 = 10
fmax_30 = 10
fmax_50 = 10
fmax_100 = 10
vmax_10 = 5
vmax_30 = 15
vmax_50 = 25
vmax_100 = 50

def f(X, D):
    z, w, y = [], [], []
    h = 0.0
    o = np.loadtxt("./materis/shift_data_9.txt")
    for k in range(D):
        z.append(X[k] - o[k])

    for w_l in range(0, D, 2):
        w.append(z[w_l])
    for y_l in range(1, D, 2):
        y.append(z[y_l])

    for j in range(0, int(D / 2 - 1)):
        h += (y[j] ** 2 - y[j + 1]) ** 2
    fx = np.max(z)
    g = np.prod(np.array(w))
    h = h - 0.0001
    return fx, g, h

if __name__ == "__main__":
    a = np.array([1,2,3,4,5])
    print(np.prod(a))