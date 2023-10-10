import numpy as np
from functions import G09
def fit(f, X, fmax, fmin, v, e):
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

    res = f(X)
    fitness = -res[0]
    ll = len(res)
    count = np.sum(np.array(res)[1:len(res)] > 0)

    if count > 0:
        for i in range(1, len(res)):
            if res[i] > 0:
                cathy = (fmax - fmin) * (ll-1) / count + (fmax - fmin) * res[i] / (e * (v[i-1]))
                fitness = fitness - cathy
    return fitness, res

if __name__ == "__main__":
    # bounds = G09.bounds
    # X = [bounds[i][1] for i in range(len(bounds))]
    # fitness = fit(G09.f, X, G09.fmax, G09.fmin, G09.vmax, 0.1)
    # print(fitness)
    a = np.array([1,2,3,4,5,6])
    b = np.array([2,3,1,1,1,1])
    print(np.sum(a>b))

