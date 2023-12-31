bounds = [(78, 102), (33, 45), (27, 45), (27, 45), (27, 45)]
x_opt = [78, 33, 29.9952560256815985, 45, 36.7758129057882073]
y_opt = -30665.53867178332
dim = 5
fmax = -22302
fmin = -32217
vmax = 14.8482709
vn = 6

def f(X):
    y = 5.3578547 * X[2] * X[2] + 0.8356891 * X[0] * X[4] + 37.293239 * X[0] - 40792.141

    g1 = 85.334407 + 0.0056858 * X[1] * X[4] + 0.0006262 * X[0] * X[3] - 0.0022053 * X[2] * X[4] - 92
    g2 = -85.334407 - 0.0056858 * X[1] * X[4] - 0.0006262 * X[0] * X[3] + 0.0022053 * X[2] * X[4]
    g3 = 80.51249 + 0.0071317 * X[1] * X[4] + 0.0029955 * X[0] * X[1] + 0.0021813 * X[2] * X[2] - 110
    g4 = -80.51249 - 0.0071317 * X[1] * X[4] - 0.0029955 * X[0] * X[1] - 0.0021813 * X[2] * X[2] + 90
    g5 = 9.300961 + 0.0047026 * X[2] * X[4] + 0.0012547 * X[0] * X[2] + 0.0019085 * X[2] * X[3] - 25
    g6 = -9.300961 - 0.0047026 * X[2] * X[4] - 0.0012547 * X[0] * X[2] - 0.0019085 * X[2] * X[3] + 20

    return y, g1, g2, g3, g4, g5, g6
