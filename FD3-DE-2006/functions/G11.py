bounds = [(-1, 1), (-1, 1)]
x_opt = [-0.707036070037170616, 0.500000004333606807]
y_opt = 0.7499

dim = 2
fmax = 5
fmin = 0
vmax = 1
vn = 1

def f(X):
    y = X[0] ** 2 + (X[1] - 1) ** 2

    h = abs(X[1] - X[0] ** 2) - 0.0001

    return y, h