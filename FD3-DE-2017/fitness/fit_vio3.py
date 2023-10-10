import numpy as np
from functions import G09

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

