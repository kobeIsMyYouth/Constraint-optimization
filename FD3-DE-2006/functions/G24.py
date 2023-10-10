bounds = [(0, 3), (0, 4)]
x_opt = [2.32952019747762, 3.17849307411774]
y_opt = -5.50801327159536

dim = 2
fmax = 0
fmin = -7
vmax = 4
vn = 2

def f(X):
    y = -X[0] - X[1]
    g1 = -2 * X[0] ** 4 + 8 * X[0] ** 3 - 8 * X[0] ** 2 + X[1] - 2
    g2 = -4 * X[0] ** 4 + 32 * X[0] ** 3 - 88 * X[0] ** 2 + 96 * X[0] + X[1] - 36

    return y, g1, g2