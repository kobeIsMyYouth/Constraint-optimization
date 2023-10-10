import numpy as np
from functions import G09
def fit(f, X, fmax, fmin, vmax, e):
    """
    适应度函数
    :param f: 目标函数
    :param X: 决策变量
    :param fmax: 目标函数的最大值
    :param fmin: 目标函数的最小值
    :param vmax: 最大约束违反量
    :param e: 约束违反量阈值
    :return: 适应度值
    """

    f, h, g = f(X)
    fitness = -f
    phi = 0

    for i in range(1, len(h)):
        if h[i] > 0:
            phi = phi + h[i]
    for j in range(1, len(g)):
        if g[j] > 0:
            phi = phi + g[j]

    if phi == 0:
        theta = -vmax
        fitness = fitness - ((fmax - fmin) / (e * vmax)) * theta
    else:
        theta = phi
        fitness = fitness - (fmax - fmin) - ((fmax - fmin) / (e * vmax)) * theta

    return fitness, f, phi

if __name__ == "__main__":
    # bounds = G09.bounds
    # X = [bounds[i][1] for i in range(len(bounds))]
    # fitness = fit(G09.f, X, G09.fmax, G09.fmin, G09.vmax, 0.1)
    # print(fitness)
    a = np.array([1,2,3,4,5,6])
    b = np.array([2,3,1,1,1,1])
    print(np.sum(a>b))

