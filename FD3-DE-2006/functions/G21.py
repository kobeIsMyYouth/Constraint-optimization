import numpy as np
bounds = [(0, 1000), (0, 40), (0, 40), (100, 300), (6.3, 6.7), (5.9, 6.4), (4.5, 6.25)]
x_opt = [193.724510070034967, 5.56944131553368433e-27, 17.3191887294084914, 100.047897801386839,
         6.68445185362377892, 5.99168428444264833, 6.21451648886070451]
y_opt = 193.724510070035
dim = 7
fmax = 1000
fmin = 0
vmax = 17716.226972698205
vn = 6

def f(X):
    y = X[0]
    g1 = -X[0] + 35 * X[1] ** 0.6 + 35 * X[2] ** 0.6
    h1 = abs(-300 * X[2] + 7500 * X[4] - 7500 * X[5] - 25 * X[3] * X[4] + 25 * X[3] * X[5] + X[2] * X[3]) - 0.0001

    h2 = abs(100 * X[1] + 155.365 * X[3] + 2500 * X[6] - X[1] * X[3] - 25 * X[3] * X[6] - 15536.5) - 0.0001

    h3 = abs(-X[4] + np.log(-X[3] + 900)) - 0.0001

    h4 = abs(-X[5] + np.log(X[3] + 300)) - 0.0001

    h5 = abs(-X[6] + np.log(-2 * X[3] + 700)) - 0.0001


    return y, g1, h1, h2, h3, h4, h5