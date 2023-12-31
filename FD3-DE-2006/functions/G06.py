bounds = [(13, 100), (0, 100)]
x_opt = [14.09500000000000064, 0.8429607892154795668]
y_opt = -6961.81387558015
dim = 2
fmax = 1241000
fmin = -7973
vmax = 17814.19
vn = 2

def f(X):
    y = (X[0] - 10) ** 3 + (X[1] - 20) ** 3

    g1 = -(X[0] - 5) ** 2 - (X[1] - 5) ** 2 + 100
    g2 = (X[0] - 6) ** 2 + (X[1] - 5) ** 2 - 82.81

    return y, g1, g2
