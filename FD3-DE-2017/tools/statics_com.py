import numpy as np
from fitness import fit_com
from functions import C01
from functions import C02
from functions import C03
from functions import C04
from functions import C05
from functions import C06
from functions import C07
from functions import C08
from functions import C09
from functions import C10
from functions import C11
from functions import C12
from functions import C13
from functions import C14
from functions import C15
from functions import C16
from functions import C17
from functions import C18
from functions import C19
from functions import C20
from functions import C21
from functions import C22
from functions import C23
from functions import C24
from functions import C25
from functions import C26
from functions import C27
from functions import C28
def st1(solutions,fitnesses,f, d):
    """
    给定25次最优解和最优(目标函数值，约束违反量)，返回其统计值
    :param solutions: 25次最优解
    :param fitnesses: 25次最优（目标函数值，约束违反量）
    :param f: 目标函数
    :return:
    """
    l = len(fitnesses)
    fit = np.array(fitnesses)
    for i in range(l):
        best = i
        for j in range(i+1, l):
            if fit_com.fit(fitnesses[j][0], fitnesses[j][1], fitnesses[best][0], fitnesses[best][1], 0):
                best = j
        fit[i] = fitnesses[best]

    mean = np.mean(fit[::, 0])
    std = np.std(fit[::, 0])

    best_function = fit[0][0]
    best_vio_num = fit[0][1]  ##

    worst_function = fit[l-1][0]
    worst_vio_num = fit[l-1][1]  ##

    median_function = fit[int((l-1)/2)][0]
    median_vio_num = fit[int((l-1)/2)][1]

    medianInd = 0
    for i in range(l):
        if fitnesses[i][0] == median_function and fitnesses[i][1] == median_vio_num:
            medianInd = i
    median_res = f(solutions[medianInd], d)
    median_vio_vio_mean = 0.0
    flag = 0
    c1 = 0
    c2 = 0
    c3 = 0
    for i in range(1, len(median_res)):  ###
        if median_res[i] > 0:
            flag = flag + 1
            median_vio_vio_mean = median_vio_vio_mean + median_res[i]
        if median_res[i] > 1.0:
            c1 = c1 + 1
        if median_res[i] > 0.01:
            c2 = c2 + 1
        if median_res[i] > 0.0001:
            c3 = c3 + 1
    if flag != 0:
        median_vio_vio_mean = median_vio_vio_mean / flag

    return best_function, best_vio_num, worst_function, worst_vio_num, median_function, median_vio_num, median_vio_vio_mean, c1, c2, c3, mean, std


def st2(fes):
    """
    给定一个偏差数组，返回其最大值，最小值，中值，平均值和方差
    :param fes: 偏差数组
    :return:
    """
    best = np.min(fes)
    median = np.median(fes)
    worst = np.max(fes)
    mean = np.mean(fes)
    std = np.std(fes)

    return best, median, worst, mean, std

if __name__ == "__main__":
    a = (1,2,3,4,5)
    print(a[1::])
    # fitnesses = np.array([(1,1),(0.1,0),(0.2,0,3),(0.4,0.5)])
    #
    # print(np.argwhere(fitnesses == (1,1)))
    path = "../results/d=10/epsilon/C03"
    solutions = np.loadtxt(path + "/FES_5/solutions.txt")
    fitness = np.loadtxt(path + "/FES_5/fitnesses.txt")
    print(st1(solutions,fitness,C03.f,10))




