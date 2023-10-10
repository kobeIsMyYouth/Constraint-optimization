import math

bounds = [(0.0000001, 10), (0, 10)]
x_opt = [1.22797135260752599, 4.24537336612274885]
y_opt = -0.0958250414180359

dim = 2
fmax = 0
fmin = -1416
vmax = 148
vn = 2


def f(X):
    y = -((math.sin(2 * math.pi * X[0])) ** 3) * math.sin(2 * math.pi * X[1]) / ((X[0] ** 3) * (X[0] + X[1]))

    g1 = X[0] ** 2 - X[1] + 1
    g2 = 1 - X[0] + (X[1] - 4) ** 2

    return y, g1, g2
