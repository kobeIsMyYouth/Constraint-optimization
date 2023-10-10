import numpy as np
def st1(solutions,fitnesses,f, d):
    """
    给定25次最优解和最优适应度值，返回其统计值
    :param solutions: 25次最优解
    :param fitnesses: 25次最优适应度值
    :param f: 目标函数
    :return:
    """
    ress = []
    for i in range(len(fitnesses)):
        res = f(solutions[i],d)[0]
        ress.append(res)
    mean = np.mean(ress)
    std = np.std(ress)

    best_index = np.argmax(fitnesses)
    best_solution = solutions[best_index]
    best_res = f(best_solution, d)  ##
    best_function = best_res[0]
    best_vio_num = np.sum(np.array(best_res[1::]) > 0)  ##

    worst_index = np.argmin(fitnesses)
    worst_solution = solutions[worst_index]
    worst_res = f(worst_solution, d)  ##
    worst_function = worst_res[0]
    worst_vio_num = np.sum(np.array(worst_res[1::]) > 0)  ##

    median = np.median(fitnesses)
    #     print(median)
    median_index = np.argwhere(fitnesses == median)[0][0]
    #     print(median_index)
    median_solution = solutions[median_index]
    median_res = f(median_solution, d)  ##
    median_function = median_res[0]
    median_vio_num = np.sum(np.array(median_res[1::]) > 0)  ##

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

