bounds = [(-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10)]
x_opt = [2.17199634142692, 2.3636830416034, 8.77392573913157, 5.09598443745173, 0.990654756560493, 1.43057392853463,
         1.32164415364306, 9.82872576524495, 8.2800915887356, 8.3759266477347]
y_opt = 24.30620906818
dim = 10
fmax = 7032
fmin = -24
vmax = 4329
vn = 8
def f(X):
    y = X[0] * X[0] + X[1] * X[1] + X[0] * X[1] - 14 * X[0] - 16 * X[1] + (X[2] - 10) ** 2 + 4 * (X[3] - 5) ** 2 + (
            X[4] - 3) ** 2 + 2 * (X[5] - 1) ** 2 + 5 * X[6] * X[6] + 7 * (X[7] - 11) ** 2 + 2 * (X[8] - 10) ** 2 + (
                X[9] - 7) ** 2 + 45

    g1 = -105 + 4 * X[0] + 5 * X[1] - 3 * X[6] + 9 * X[7]
    g2 = 10 * X[0] - 8 * X[1] - 17 * X[6] + 2 * X[7]
    g3 = -8 * X[0] + 2 * X[1] + 5 * X[8] - 2 * X[9] - 12
    g4 = 3 * (X[0] - 2) ** 2 + 4 * (X[1] - 3) ** 2 + 2 * X[2] * X[2] - 7 * X[3] - 120
    g5 = 5 * X[0] * X[0] + 8 * X[1] + (X[2] - 6) ** 2 - 2 * X[3] - 40
    g6 = X[0] * X[0] + 2 * (X[1] - 2) ** 2 - 2 * X[0] * X[1] + 14 * X[4] - 6 * X[5]
    g7 = 0.5 * (X[0] - 8) ** 2 + 2 * (X[1] - 4) ** 2 + 3 * X[4] * X[4] - X[5] - 30
    g8 = -3 * X[0] + 6 * X[1] + 12 * (X[8] - 8) ** 2 + - 7 * X[9]

    return y, g1, g2, g3, g4, g5, g6, g7, g8