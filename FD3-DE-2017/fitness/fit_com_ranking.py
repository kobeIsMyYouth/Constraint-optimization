import numpy as np
from functions import G09
def fit(f1, phi1, f2, phi2, t, tmax):
    """
    epsilon约束处理技术
    :param f: 目标函数
    :param X1: 第一个待对比的解
    :param X2: 第二个待对比的解
    :param epsilon: 参数
    :return: 按照epsilon约束处理规则，如果X1优于X2，返回Ture，否则False
    """
    flag = False

    pfmax = 0.1
    pfmin = 0

    pf = pfmax - (pfmax - pfmin)*(t / tmax)**5

    if (phi1 <= 0 and phi2 <= 0) or np.random.random() < pf:
        if f1 < f2:
            flag = True
    else:
        if phi1 < phi2:
            flag = True

    return flag

def fit_tri(f1, phi1, f2, phi2, f3, phi3, epsilon):
    """
    返回三个中中等的（目标函数值，约束违反总量）
    :param f1: 第一个目标函数
    :param phi1: 第一个约束违反量
    :param f2: 第二个目标函数
    :param phi2: 第二个约束违反量
    :param f3: 第三个目标函数
    :param phi3: 第三个约束违反量
    :param epsilon: 参数
    :return:
    """
    flag = False

    if phi1 <= epsilon and phi2 <= epsilon and f1 < f2:
        flag = True
    if phi1 == phi2 and f1 < f2:
        flag = True
    if phi1 < phi2 and (phi1 > epsilon or phi2 > epsilon):
        flag = True

    return flag

def f(X):
    return np.sum(X), X[0], X[1], X[2]

if __name__ == "__main__":
    g = lambda X: f(X)
    X1 = [-1,-3,2]
    X2 = [-1,-2,2]
    epsilon = 1.5
    print(fit(g,X1,X2,epsilon))
