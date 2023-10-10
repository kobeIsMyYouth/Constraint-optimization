
bounds = [(0, 300), (0, 300), (0, 100), (0, 200), (0, 100), (0, 300), (0, 100), (0, 200), (0.01, 0.03)]
x_opt = [0.00510000000000259465, 99.9947000000000514, 9.01920162996045897e-18, 99.9999000000000535,
         0.000100000000027086086, 2.75700683389584542e-14, 99.9999999999999574, 200, 0.0100000100000100008]
y_opt = -400.055099999999584

dim = 9
fmax = 10600.0
fmin = -3900
vmax = 728.9996997181571
vn = 6

def f(X):
    y = -9 * X[4] - 15 * X[7] + 6 * X[0] + 16 * X[1] + 10 * (X[5] + X[6])

    g1 = X[8] * X[2] + 0.02 * X[5] - 0.025 * X[4]
    g2 = X[8] * X[3] + 0.02 * X[6] - 0.015 * X[7]

    h1 = abs(X[0] + X[1] - X[2] - X[3]) - 0.0001
    h2 = abs(0.03 * X[0] + 0.01 * X[1] - X[8] * (X[2] + X[3])) - 0.0001
    h3 = abs(X[2] + X[5] - X[4]) - 0.0001
    h4 = abs(X[3] + X[6] - X[7]) - 0.0001

    return y, g1, g2, h1, h2, h3, h4