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
    # res = f(X)
    # fitness = -res[0]
    # ll = len(res)
    # count = np.sum(np.array(res)[1:ll] > 0)
    # # v = np.sum(np.array(res)[1:ll])
    # ff = fmax - fmin
    # if count > 0:
    #     for i in range(1, ll):
    #         if res[i] > 0:
    #             cathy = ff * (ll-1) / count + ff * res[i] / (e * vmax)
    #             fitness = fitness - cathy
    # return fitness, res
    res = f(X)
    # fitness = -res[0]
    v = np.array(res[1::])
    count = np.sum(v[v>0])
    ff = fmax - fmin
    if count == 0:
        # fitness = -res[0]
        count = -vmax
        fitness = -(res[0] + (fmax * count) / (e * vmax))
    else:
        fitness = -res[0] - ff - (ff * count) / (e * vmax)

    return fitness, res, count

def fit1(f, X, fmax, fmin, vmax, e):

    y, g1, g2, g3, g4, g5 = f(X)
    fitness = -y
    count1 = np.sum(g1 > 0)
    count2 = np.sum(g2 > 0)
    count3 = np.sum(g3 > 0)
    count4 = np.sum(g4 > 0)
    count5 = np.sum(g5 > 0)
    count = count1 + count2 + count3 + count4 + count5
    ll = 85
    ff = fmax - fmin
    if count>0:
        if count1 > 0:
            for i in range(5):
                for j in range(4):
                    if g1[i][j] > 0:
                        cathy = ff * ll / count + ff * g1[i][j] / (e * vmax)
                        fitness = fitness - cathy
        if count2 > 0:
            for i in range(5):
                    if g2[i] > 0:
                        cathy = ff * ll / count + ff * g2[i] / (e * vmax)
                        fitness = fitness - cathy
        if count3 > 0:
            for i in range(5):
                for j in range(4):
                    if g3[i][j] > 0:
                        cathy = ff * ll / count + ff * g3[i][j] / (e * vmax)
                        fitness = fitness - cathy
        if count4 > 0:
            for i in range(5):
                for j in range(4):
                    if g4[i][j] > 0:
                        cathy = ff * ll / count + ff * g4[i][j] / (e * vmax)
                        fitness = fitness - cathy
        if count5 > 0:
            for i in range(5):
                for j in range(4):
                    if g5[i][j] > 0:
                        cathy = ff * ll / count + ff * g5[i][j] / (e * vmax)
                        fitness = fitness - cathy
    v = np.sum(g1[g1>0]) + np.sum(g2[g2>0]) + np.sum(g3[g3>0]) + np.sum(g4[g4>0]) + np.sum(g5[g5>0])

    return fitness, y, v

if __name__ == "__main__":
    # bounds = G09.bounds
    # X = [bounds[i][1] for i in range(len(bounds))]
    # fitness = fit(G09.f, X, G09.fmax, G09.fmin, G09.vmax, 0.1)
    # print(fitness)
    a = np.array([1,2,3,4,5,6])
    b = np.array([2,3,1,1,1,1])
    print(np.sum(a>b))

