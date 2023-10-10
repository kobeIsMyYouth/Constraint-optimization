import numpy as np
from random import choice
from fitness import fit_com_ranking
from functions import G01
from functions import G02
from functions import G03
from functions import G04
from functions import G05
from functions import G06
from functions import G07
from functions import G08
from functions import G09
from functions import G10
from functions import G11
from functions import G12
from functions import G13
from functions import G14
from functions import G15
from functions import G16
from functions import G17
from functions import G18
from functions import G19
from functions import G20
from functions import G21
from functions import G22
from functions import G23
from functions import G24
from tools import gradient

class DE():
    def __init__(self, pN, dim, tmax, G, Ne, epsilon, tc, F, cr, cp):

        self.G = G   ###优化函数的信息（目标函数，边界值，最优解，最优值等）

        self.cp = cp
        self.cr = cr
        self.F = F
        self.pN = pN
        self.Ne = Ne
        self.dim = dim
        self.tmax = tmax
        self.tc = tc
        self.epsilon = epsilon
        self.epsilon0 = epsilon
        self.devi = np.zeros((self.pN * self.tmax))
        self.FES = self.tmax*self.pN
        self.fe = 0
        self.su = 0

        self.X = np.zeros((self.pN, self.dim))
        self.Xfv = np.zeros((self.pN, 2))
        self.Xbest = np.zeros((self.dim))
        self.Xbestfv = np.zeros((2))

        self.Pe = np.zeros((self.Ne, self.dim))
        self.Pefv = np.zeros((self.Ne, 2))

        self.gbest_1 = np.zeros((self.dim))  # 第5000次迭代时的最优解
        self.g_fit1 = np.zeros((2))
        self.gbest_2 = np.zeros((self.dim))  # 第50000次迭代时的最优解
        self.g_fit2 = np.zeros((2))
        self.gbest_3 = np.zeros((self.dim))  # 第500000次迭代时的最优解
        self.g_fit3 = np.zeros((2))


    def init_Population(self):
        """
        随机初始化
        :return:
        """
        for i in range(self.pN):
            for j in range(self.dim):
                self.X[i][j] = self.G.bounds[j][0] + (self.G.bounds[j][1] - self.G.bounds[j][0])\
                               * np.random.random()

        """
        计算初始的目标函数值和约束违反总量
        """
        for i in range(self.pN):
            res = np.array(self.G.f(self.X[i]))
            self.Xfv[i][0] = res[0]
            v = res[1::]
            phi = np.sum(v[v>0])
            self.Xfv[i][1] = phi

        self.Xbest = self.X[0].copy()
        self.Xbestfv[0] = self.Xfv[0][0]
        self.Xbestfv[1] = self.Xfv[0][1]
        for i in range(self.pN):
            if fit_com_ranking.fit(self.Xfv[i][0], self.Xfv[i][1], self.Xbestfv[0], self.Xbestfv[1], 0, self.tmax):
                self.Xbest = self.X[i].copy()
                self.Xbestfv[0] = self.Xfv[i][0]
                self.Xbestfv[1] = self.Xfv[i][1]

        """
        初始化epsilon
        """
        if self.epsilon0 != 0:
            phix = []
            for i in range(self.pN):
                res = np.array(self.G.f(self.X[i])[1::])
                phix.append(np.sum(res[res > 0]))
            phix = sorted(phix)
            self.epsilon0 = phix[int(0.2*self.pN)]  ### Top 0.2

        """
        初始化精英集
        """
        if self.epsilon0 != 0:
            indexes = np.argsort(self.Xfv[::, 1])
            for i in range(self.Ne):
                self.Pe[i] = self.X[indexes[i]]
                self.Pefv[i][0] = self.Xfv[indexes[i]][0]
                self.Pefv[i][1] = self.Xfv[indexes[i]][1]

    def iterator(self):

        ls1 = set([i for i in range(self.pN+self.Ne)])
        ls2 = set([i for i in range(self.pN)])
        ld = [j for j in range(self.dim)]
        m = len(self.G.f(self.X[0])) - 1
        Cfunctions = []
        deltaCfunctions = []

        for i in range(m):
            f = lambda X: self.G.f(X)[i+1]
            Cfunctions.append(f)
            g = lambda X: self.G.f(X)[i+1] if self.G.f(X)[i+1]>0 else 0
            deltaCfunctions.append(g)

        for t in range(self.tmax):
            Xbest = self.Xbest.copy()
            Xbestfv = self.Xbestfv.copy()

            Q = self.X.copy()
            QXfv = self.Xfv.copy()

            P = self.Pe.copy()
            Pfv = self.Pefv.copy()

            if t < self.tc:
                self.epsilon = self.epsilon0 * (1 - t / self.tc)**self.cp
            else:
                self.epsilon = 0.0


            for i in range(self.pN):
                """
                mutation
                """
                # Xp1 = Xp2 = Xp3 = np.zeros((self.dim))
                if self.epsilon != 0:
                    l = list(ls1-{i})
                    individual1 = choice(l)
                    l = list(set(l)-{individual1})
                    individual2 = choice(l)
                    l = list(set(l) - {individual2})
                    individual3 = choice(l)

                    # print((i,individual1,individual2,individual3))

                    if individual1 >= self.pN:
                        individual1 = individual1 - self.pN
                        Xp1 = P[individual1]
                        # print("**********")
                    else:
                        Xp1 = Q[individual1]

                    if individual2 >= self.pN:
                        individual2 = individual2 - self.pN
                        Xp2 = P[individual2]
                    else:
                        Xp2 = Q[individual2]

                    if individual3 >= self.pN:
                        individual3 = individual3 - self.pN
                        Xp3 = P[individual3]
                    else:
                        Xp3 = Q[individual3]
                else:
                    l = list(ls2 - {i})

                    individual1 = choice(l)
                    l = list(set(l) - {individual1})
                    individual2 = choice(l)
                    l = list(set(l) - {individual2})
                    individual3 = choice(l)

                    # print((i, individual1, individual2, individual3))
                    Xp1 = Q[individual1]
                    Xp2 = Q[individual2]
                    Xp3 = Q[individual3]

                X_tmp = Xp1 + self.F*(Xp2-Xp3)

                crossover_point = choice(ld)
                X_new = Q[i].copy()

                """
                指数交叉
                """
                L = 0
                while L < self.dim and np.random.random() <= self.cr:
                    L = L + 1
                points = [(crossover_point + i) % self.dim for i in range(L)]

                for j in range(self.dim):
                    if j in points:
                        X_new[j] = X_tmp[j]

                for j in range(self.dim):
                    """
                    控制在搜索范围内
                    """
                    if X_new[j] < self.G.bounds[j][0] or X_new[j] > self.G.bounds[j][1]:
                        X_new[j] = self.G.bounds[j][0]+(self.G.bounds[j][1] - self.G.bounds[j][0])*np.random.random()

                res = np.array(self.G.f(X_new))
                X_new_f = res[0]
                v = res[1::]
                X_new_v = np.sum(v[v > 0])

                if self.epsilon != 0:
                    index = np.argsort(Pfv[::, 1])
                    if X_new_v <= Pfv[index[-1]][1]:
                        self.Pe[index[-1]] = X_new
                        self.Pefv[index[-1]][0] = X_new_f
                        self.Pefv[index[-1]][1] = X_new_v


                if fit_com_ranking.fit(X_new_f, X_new_v, QXfv[i][0], QXfv[i][1], t, self.tmax):
                    self.X[i] = X_new
                    self.Xfv[i][0] = X_new_f
                    self.Xfv[i][1] = X_new_v
                    if fit_com_ranking.fit(X_new_f, X_new_v, Xbestfv[0], Xbestfv[1], t, self.tmax):
                        self.Xbest = X_new
                        self.Xbestfv[0] = X_new_f
                        self.Xbestfv[1] = X_new_v

                de = self.Xbestfv[0] - self.G.y_opt
                self.devi[t * self.pN + i] = de

                if self.Xbestfv[1] == 0.0:
                    self.fe = 1
                    if self.FES == self.tmax * self.pN and de <= 0.0001:
                        self.FES = t * self.pN + i
                        self.su = 1
                else:
                    self.FES = self.tmax * self.pN
                    self.fe = 0
                    self.su = 0

                if t*self.pN+i == 5e3:
                    self.gbest_1 = self.Xbest.copy()
                    self.g_fit1 = self.Xbestfv.copy()

                if t*self.pN+i == 5e4:
                    self.gbest_2 = self.Xbest.copy()
                    self.g_fit2 = self.Xbestfv.copy()

                if t*self.pN+i == 5e5:
                    self.gbest_3 = self.Xbest.copy()
                    self.g_fit3 = self.Xbestfv.copy()

                print((self.Xbestfv[0], self.Xbestfv[1], t * self.pN + i, self.fe, self.su))
            if self.su == 1:
                break

        return self.gbest_1, self.g_fit1, self.gbest_2, self.g_fit2, self.gbest_3, self.g_fit3, self.FES, self.devi, self.fe, self.su

if __name__ == "__main__":
    # def __init__(self, pN, dim, tmax, G, Ne, epsilon, tc, F, cr, cp):
    d = DE(40, G03.dim, 12500, G03, 3, 0, 2500, 0.7, 0.9, 5)
    d.init_Population()
    res = d.iterator()


