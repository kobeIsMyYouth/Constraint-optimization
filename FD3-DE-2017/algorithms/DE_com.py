import numpy as np
from random import choice
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
from tools import gradient

class DE():
    def __init__(self, pN0, pN1, dim, tmax, G, Ne, epsilon, tc, F, cr, cp):

        self.G = G   ###优化函数的信息（目标函数，边界值，最优解，最优值等）

        self.cp = cp
        self.cr = cr
        self.F = F
        self.pN0 = pN0
        self.pN1 = pN1
        self.pN = pN0
        self.Ne = Ne
        self.dim = dim
        self.tmax = tmax
        self.tc = tc
        self.epsilon = epsilon
        self.epsilon0 = epsilon
        self.devi = np.zeros((5*self.tmax))
        self.FES = 0
        self.fe = 0
        self.su = 0

        self.X = np.zeros((self.pN, self.dim))
        self.Xfv = np.zeros((self.pN, 2))
        self.Xbest = np.zeros((self.dim))
        self.Xbestfv = np.zeros((2))

        self.Pe = np.zeros((self.Ne, self.dim))
        self.Pefv = np.zeros((self.Ne, 2))

        if dim == 10:
            self.fmax = self.G.fmax_10
            self.vmax = self.G.vmax_10
            self.lowFES = 2e4
            self.medFES = 1e5
            self.higFES = 2e5
        elif dim == 30:
            self.fmax = self.G.fmax_30
            self.vmax = self.G.vmax_30
            self.lowFES = 6e4
            self.medFES = 3e5
            self.higFES = 6e5
        elif dim == 50:
            self.fmax = self.G.fmax_50
            self.vmax = self.G.vmax_50
            self.lowFES = 1e5
            self.medFES = 5e5
            self.higFES = 1e6
        elif dim == 100:
            self.fmax = self.G.fmax_100
            self.vmax = self.G.vmax_100
            self.lowFES = 2e5
            self.medFES = 1e6
            self.higFES = 2e6
        else:
            print("D is not standard!")

        self.gbest_1 = np.zeros((self.dim))  # 第5000次迭代时的最优解
        self.g_fit_1 = np.zeros((2))
        self.gbest_2 = np.zeros((self.dim))  # 第50000次迭代时的最优解
        self.g_fit_2 = np.zeros((2))
        self.gbest_3 = np.zeros((self.dim))  # 第500000次迭代时的最优解
        self.g_fit_3 = np.zeros((2))

        if dim == 10:
            self.fmax = self.G.fmax_10
            self.vmax = self.G.vmax_10
            self.lowFES = 2e4
            self.medFES = 1e5
            self.higFES = 2e5
        elif dim == 30:
            self.fmax = self.G.fmax_30
            self.vmax = self.G.vmax_30
            self.lowFES = 6e4
            self.medFES = 3e5
            self.higFES = 6e5
        elif dim == 50:
            self.fmax = self.G.fmax_50
            self.vmax = self.G.vmax_50
            self.lowFES = 1e5
            self.medFES = 5e5
            self.higFES = 1e6
        elif dim == 100:
            self.fmax = self.G.fmax_100
            self.vmax = self.G.vmax_100
            self.lowFES = 2e5
            self.medFES = 1e6
            self.higFES = 2e6
        else:
            print("D is not standard!")



    def init_Population(self):
        """
        随机初始化
        :return:
        """
        for i in range(self.pN):
            for j in range(self.dim):
                self.X[i][j] = -self.G.bound + 2 * self.G.bound * np.random.random()

        """
        计算初始的目标函数值和约束违反总量
        """
        for i in range(self.pN):
            res = np.array(self.G.f(self.X[i], self.dim))
            self.Xfv[i][0] = res[0]
            v = res[1::]
            phi = np.sum(v[v>0])
            self.Xfv[i][1] = phi

        self.Xbest = self.X[0].copy()
        self.Xbestfv[0] = self.Xfv[0][0]
        self.Xbestfv[1] = self.Xfv[0][1]
        for i in range(self.pN):
            if fit_com.fit(self.Xfv[i][0], self.Xfv[i][1], self.Xbestfv[0], self.Xbestfv[1], self.epsilon):
                self.Xbest = self.X[i].copy()
                self.Xbestfv[0] = self.Xfv[i][0]
                self.Xbestfv[1] = self.Xfv[i][1]

        """
        初始化epsilon
        """
        if self.epsilon0 != 0:
            phix = []
            for i in range(self.pN):
                res = np.array(self.G.f(self.X[i], self.dim)[1::])
                phix.append(np.sum(res[res > 0]))
            phix = sorted(phix)
            self.epsilon0 = phix[int(0.2*self.pN)]  ### Top 0.2

        """
        初始化精英集
        """
        if self.epsilon0 != 0 and self.Ne != 0:
            indexes = np.argsort(self.Xfv[::, 1])
            for i in range(self.Ne):
                self.Pe[i] = self.X[indexes[i]]
                self.Pefv[i][0] = self.Xfv[indexes[i]][0]
                self.Pefv[i][1] = self.Xfv[indexes[i]][1]

    def iterator(self):

        ld = [j for j in range(self.dim)]
        FES = 0

        while FES < self.tmax:

            P = self.Pe.copy()
            Pfv = self.Pefv.copy()

            if FES < self.tc:
                self.epsilon = self.epsilon0 * (1 - FES / self.tc) ** self.cp
            else:
                self.epsilon = 0.0

            # ee = self.e * (1 - (FES / (self.tmax + 0.0001))) ** self.cp
            prepN = self.pN

            self.pN = int(np.round(self.pN0 - (FES / self.tmax) * (self.pN0 - self.pN1)))

            ls1 = set([i for i in range(self.pN + self.Ne)])
            ls2 = set([i for i in range(self.pN)])

            if self.pN < prepN:
                delta = prepN - self.pN

                sortIndexes = self.Xfv[::, 0].argsort()
                deleteIndexes = sortIndexes[0:delta].copy()

                self.X = np.delete(self.X, deleteIndexes, axis=0)
                self.Xfv = np.delete(self.Xfv, deleteIndexes, axis=0)

            Xbestfv = self.Xbestfv.copy()

            Q = self.X.copy()
            QXfv = self.Xfv.copy()

            for i in range(self.pN):
                """
                mutation
                """
                if self.epsilon != 0 and self.Xbestfv[1] != 0:
                    l = list(ls1 - {i})
                    individual1 = choice(l)
                    l = list(set(l) - {individual1})
                    individual2 = choice(l)
                    l = list(set(l) - {individual2})
                    individual3 = choice(l)

                    # print((i,individual1,individual2,individual3))

                    if individual1 >= self.pN:
                        individual1 = individual1 - self.pN
                        Xp1 = P[individual1]
                        Xp1_fit = Pfv[individual1]

                    else:
                        Xp1 = Q[individual1]
                        Xp1_fit = QXfv[individual1]

                    if individual2 >= self.pN:
                        individual2 = individual2 - self.pN
                        Xp2 = P[individual2]
                        Xp2_fit = Pfv[individual2]
                    else:
                        Xp2 = Q[individual2]
                        Xp2_fit = QXfv[individual2]

                    if individual3 >= self.pN:
                        individual3 = individual3 - self.pN
                        Xp3 = P[individual3]
                        Xp3_fit = Pfv[individual3]
                    else:
                        Xp3 = Q[individual3]
                        Xp3_fit = QXfv[individual3]
                else:
                    l = list(ls2 - {i})

                    individual1 = choice(l)
                    l = list(set(l) - {individual1})
                    individual2 = choice(l)
                    l = list(set(l) - {individual2})
                    individual3 = choice(l)

                    # print((i, individual1, individual2, individual3))
                    Xp1 = Q[individual1]
                    Xp1_fit = QXfv[individual1]
                    Xp2 = Q[individual2]
                    Xp2_fit = QXfv[individual2]
                    Xp3 = Q[individual3]
                    Xp3_fit = QXfv[individual3]

                bestXp = np.argmax(np.array([Xp1_fit, Xp2_fit, Xp3_fit]))
                if bestXp == 0:
                    X_tmp = Xp1 + self.F * (Xp2 - Xp3)
                elif bestXp == 1:
                    X_tmp = Xp2 + self.F * (Xp1 - Xp3)
                else:
                    X_tmp = Xp3 + self.F * (Xp1 - Xp2)

                crossover_point = choice(ld)
                X_new = Q[i].copy()

                """
                指数交叉
                """
                L = 0
                while L < self.dim and np.random.random() <= self.cr:
                    L = L + 1
                points = [(crossover_point + m) % self.dim for m in range(L)]

                for j in range(self.dim):
                    if j in points:
                        X_new[j] = X_tmp[j]

                for j in range(self.dim):
                    """
                    控制在搜索范围内
                    """
                    if X_new[j] < -self.G.bound or X_new[j] > self.G.bound:
                        X_new[j] = - self.G.bound + 2 * self.G.bound * np.random.random()

                res = np.array(self.G.f(X_new, self.dim))
                # self.Xfv[i][0] = res[0]
                # v = res[1::]
                # phi = np.sum(v[v > 0])
                # self.Xfv[i][1] = phi
                # X_new_fitness, res = fit_vio2.fit(self.G.f, X_new, self.fmax, self.vmax, ee)

                v = np.array(res[1::])
                X_new_v = np.sum(v[v > 0])

                if self.epsilon != 0 and self.Ne != 0:
                    index = np.argsort(Pfv[::, 1])
                    if X_new_v <= Pfv[index[-1]][1]:
                        self.Pe[index[-1]] = X_new
                        self.Pefv[index[-1]][0] = res[0]
                        self.Pefv[index[-1]][1] = X_new_v

                # fit_vio2.fit(self.G.f, self.X[i], self.fmax, self.vmax, self.e)

                if fit_com.fit(res[0], X_new_v, QXfv[i][0], QXfv[i][1], self.epsilon):
                    self.X[i] = X_new
                    self.Xfv[i][0] = res[0]
                    self.Xfv[i][1] = X_new_v
                    if fit_com.fit(res[0], X_new_v, Xbestfv[0], Xbestfv[1], self.epsilon):
                        self.Xbest = X_new
                        self.Xbestfv[0] = res[0]
                        self.Xbestfv[1] = X_new_v
                        # v = np.array(res[1::])
                        # self.Xbestfv[2] = np.sum(v[v > 0])

                FES = FES + 1
                # print((t, self.pN, FES))
                de = self.Xbestfv[1] - 0
                self.devi[FES] = de

                if self.Xbestfv[1] == 0.0:
                    self.fe = 1
                    self.FES = FES
                #     if self.FES == self.tmax * self.pN and de <= 0.0001:
                #         self.FES = t * self.pN + i
                #         self.su = 1
                else:
                    # self.FES = self.tmax * self.pN
                    self.fe = 0
                #     self.su = 0

                print((self.Xbestfv[0], self.Xbestfv[1], FES))
                # print((self.Xbestfv[1], self.Xbestfv[2], t * self.pN + i, self.fe, self.su))

                if FES == self.lowFES - 1:
                    self.gbest_1 = self.Xbest.copy()
                    self.g_fit_1[0] = self.Xbestfv[0].copy()

                if FES == self.medFES - 1:
                    self.gbest_2 = self.Xbest.copy()
                    self.g_fit_2[0] = self.Xbestfv[0].copy()

                if FES == self.higFES - 1:
                    self.gbest_3 = self.Xbest.copy()
                    self.g_fit_3[0] = self.Xbestfv[0].copy()

        return self.gbest_1, self.g_fit_1, self.gbest_2, self.g_fit_2, self.gbest_3, self.g_fit_3, self.FES, self.devi, self.fe, self.su


if __name__ == "__main__":
    # def __init__(self, pN0, pN1, dim, tmax, G, Ne, epsilon, tc, F, cr, cp):
    d = DE(40, 4, 30, 600000, C03, 3, 1, 15000, 0.7, 0.9, 5)
    d.init_Population()
    res = d.iterator()
    print(res[0])


