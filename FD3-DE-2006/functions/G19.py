import numpy as np
bounds = [(0, 10), (0, 10), (0, 10), (0, 10), (0, 10), (0, 10), (0, 10), (0, 10), (0, 10),
          (0, 10), (0, 10), (0, 10),(0, 10), (0, 10), (0, 10)]
x_opt = [1.66991341326291344e-17, 3.95378229282456509e-16, 3.94599045143233784, 1.06036597479721211e-16,
         3.2831773458454161,9.99999999999999822, 1.12829414671605333e-17, 1.2026194599794709e-17,
         2.50706276000769697e-15,2.24624122987970677e-15,0.370764847417013987, 0.278456024942955571,
         0.523838487672241171, 0.388620152510322781, 0.298156764974678579]
y_opt = 32.6555929502463
dim = 15
fmax = 66512.5
fmin = -59.99999992891392
vmax = 4931.99999937451
vn = 5

def f(X):
    b = np.array([-40, -2, -0.25, -4, -4, -1, -40, -60, 5, 1])
    e = np.array([-15, -27, -36, -18, -12])
    c = np.array([[30, -20, -10, 32, -10],
                  [-20, 39, -6, -31, 32],
                  [-10, -6, 10, -6, -10],
                  [32, -31, -6, 39, -20],
                  [-10, 32, -10, -20, 30]
                  ])

    d = np.array([4, 8, 10, 6, 2])
    a = np.array([[-16, 2, 0, 1, 0],
                  [0, -2, 0, 0.4, 2],
                  [-3.5, 0, 2, 0, 0],
                  [0, -2, 0, -4, -1],
                  [0, -9, -2, 1, -2.8],
                  [2, 0, -4, 0, 0],
                  [-1, -1, -1, -1, -1],
                  [-1, -2, -3, -2, -1],
                  [1, 2, 3, 4, 5],
                  [1, 1, 1, 1, 1]
                  ])

    y = 0.0
    for i in range(5):
        for j in range(5):
            y = y + c[i, j] * X[10 + i] * X[10 + j]
    for j in range(5):
        y = y + 2 * d[j] * X[10 + j] ** 3
    for i in range(10):
        y = y - b[i] * X[i]

    g1 = 0.0
    g2 = 0.0
    g3 = 0.0
    g4 = 0.0
    g5 = 0.0
    for i in range(5):
        g1 = g1 - 2 * c[i, 0] * X[10 + i]
    g1 = g1 - 3 * d[0] * X[10 + 0] ** 2 - e[0]
    for i in range(10):
        g1 = g1 + a[i, 0] * X[i]

    for i in range(5):
        g2 = g2 - 2 * c[i, 1] * X[10 + i]
    g2 = g2 - 3 * d[1] * X[10 + 1] ** 2 - e[1]
    for i in range(10):
        g2 = g2 + a[i, 1] * X[i]

    for i in range(5):
        g3 = g3 - 2 * c[i, 2] * X[10 + i]
    g3 = g3 - 3 * d[2] * X[10 + 2] ** 2 - e[2]
    for i in range(10):
        g3 = g3 + a[i, 2] * X[i]

    for i in range(5):
        g4 = g4 - 2 * c[i, 3] * X[10 + i]
    g4 = g4 - 3 * d[3] * X[10 + 3] ** 2 - e[3]
    for i in range(10):
        g4 = g4 + a[i, 3] * X[i]

    for i in range(5):
        g5 = g5 - 2 * c[i, 4] * X[10 + i]
    g5 = g5 - 3 * d[4] * X[10 + 4] ** 2 - e[4]
    for i in range(10):
        g5 = g5 + a[i, 4] * X[i]

    return y, g1, g2, g3, g4, g5