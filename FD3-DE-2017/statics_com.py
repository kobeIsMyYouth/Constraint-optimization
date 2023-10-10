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
def st1(fitnesses):
    """
    给定25次最优解和最优(目标函数值，约束违反量)，返回其统计值
    :param solutions: 25次最优解
    :param fitnesses: 25次最优（目标函数值，约束违反量）
    :param f: 目标函数
    :return:
    """
    best_fun = 0.0
    best_vio = 0.0
    median_fun = 0.0
    median_vio = 0.0
    worst_fun = 0.0
    worst_vio = 0.0
    mean_fun = 0.0
    mean_vio = 0.0
    std_fun = 0.0
    std_vio = 0.0

    if np.min(fitnesses[::,1]) == 0: #25次求解中存在可行解
        functs = fitnesses[fitnesses[::,1]==0]
        best_fun = np.min(functs[::,0])
        worst_fun = np.max(functs[::, 0])
        median_fun = np.median(functs[::, 0])
        mean_fun = np.mean(functs[::, 0])
        std_fun = np.std(functs[::, 0])

    else: #25次求解中不存在可行解

        ff = fitnesses[fitnesses[::,0].argsort()]
        best_fun = ff[0][0]
        best_vio = ff[0][1]
        median_fun = ff[13][0]
        median_vio = ff[13][1]
        worst_fun = ff[-1][0]
        worst_vio = ff[-1][1]
        mean_fun = np.mean(fitnesses[::,0])
        mean_vio = np.mean(fitnesses[::,1])
        std_fun = np.std(fitnesses[::,0])
        std_vio = np.std(fitnesses[::,1])

    return best_fun, best_vio, worst_fun, worst_vio, median_fun, median_vio, mean_fun, mean_vio, std_fun, std_vio


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

    d = 100

    # functions = [C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15,
    #          C16, C17, C18, C19, C20, C21, C22, C23, C24, C25, C26, C27, C28]
    # funcs = ["C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "C13", "C14", "C15", "C16",
    #          "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27", "C28"]

    functions = [C01]
    funcs = ["C01"]

    for j in range(len(funcs)):
        print(j)
        path = "./results/d=" + str(d) + "/epsilon1/" + funcs[j]

        solutions = np.loadtxt(path + "/FES_5/solutions.txt")
        fitness = np.zeros((len(solutions), 2))

        for i in range(len(solutions)):
            res = functions[j].f(solutions[i], d)
            fitness[i][0] = res[0]
            v = np.array(res[1::])
            fitness[i][1] = np.sum(v[v > 0])

        res3 = st1(fitness)
        np.savetxt(path + "/res3.txt", res3)
        np.savetxt(path + "/FES_5/fitnesses.txt", fitness)



