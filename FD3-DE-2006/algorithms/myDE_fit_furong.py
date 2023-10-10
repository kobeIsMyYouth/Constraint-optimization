import numpy as np
from random import choice
from fitness import fit_vio2
from functions import aa
from functions import dd
from functions import tt_cc

class DE():
    def __init__(self, pN, dim, tmax, G,  F, cr, cp, e):
        """
        没有精英集的差分进化算法
        :param pN:
        :param dim:
        :param tmax:
        :param G:
        :param Ne:
        :param epsilon:
        :param tc:
        :param F:
        :param cr:
        :param cp:
        :param pg:
        :param Rg:
        :param e:
        """
        self.G = G   ###优化函数的信息（目标函数，边界值，最优解，最优值等）

        self.e = e
        self.cp = cp
        self.cr = cr
        self.F = F
        self.pN = pN
        self.dim = dim
        self.tmax = tmax
        self.devi = np.zeros((self.pN * self.tmax))
        self.FES = self.tmax*self.pN
        self.fe = 0
        self.su = 0

        self.X = np.zeros((self.pN, self.dim))
        self.Xfv = np.zeros((self.pN, 1))      ###适应度值

        self.Xbest = np.zeros((self.dim))     ###最优解
        self.Xbestfv = np.full(3, -1.0e78)    ###最优解的（适应度值，目标函数值，约束违反总量）

        self.gbest_1 = np.zeros((self.dim))  # 第5000次迭代时的最优解
        self.g_fit_1 = np.full(1, -1.0e78)  # 第5000次迭代时的最优适应度值

        self.gbest_2 = np.zeros((self.dim))  # 第50000次迭代时的最优解
        self.g_fit_2 = np.full(1, -1.0e78)  # 第50000次迭代时的最优适应度值

        self.gbest_3 = np.zeros((self.dim))  # 第500000次迭代时的最优解
        self.g_fit_3 = np.full(1, -1.0e78)  # 第500000次迭代时的最优适应度值

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
        计算初始的适应度值
        """
        for i in range(self.pN):

            fitness, res = fit_vio2.fit1(self.G.f, self.X[i], self.G.fmax, self.G.fmin, self.G.vmax, self.e)
            self.Xfv[i] = fitness
            if self.Xfv[i] > self.Xbestfv[0]:
                self.Xbest = self.X[i].copy()
                self.Xbestfv[0] = self.Xfv[i]
                self.Xbestfv[1] = res[0]
                v = np.array(res[1::])
                self.Xbestfv[2] = np.sum(v[v>0])

    def iterator(self):

        ls2 = set([i for i in range(self.pN)])
        ld = [j for j in range(self.dim)]

        for t in range(self.tmax):

            ee = self.e * (1 - (t / (self.tmax + 0.0001))) ** self.cp
            # ee = 1 - (t/(self.tmax + 0.0001))**5
            # phi = self.G.vn - (self.G.vn-1)*(t / self.tmax)**5
            # ee = 0.5
            Xbestfv = self.Xbestfv.copy()

            Q = self.X.copy()
            QXfv = self.Xfv.copy()

            for i in range(self.pN):
                """
                mutation
                """
                l = list(ls2 - {i})

                individual1 = choice(l)
                l = list(set(l) - {individual1})
                individual2 = choice(l)
                l = list(set(l) - {individual2})
                individual3 = choice(l)

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
                        # print("------------------------------------------------------------")

                X_new_fitness, res = fit_vio2.fit1(self.G.f, X_new, self.G.fmax, self.G.fmin, self.G.vmax, ee)

                if X_new_fitness > QXfv[i]:
                    self.X[i] = X_new
                    self.Xfv[i] = X_new_fitness
                    if X_new_fitness > Xbestfv[0]:
                        self.Xbest = X_new
                        self.Xbestfv[0] = X_new_fitness
                        self.Xbestfv[1] = res[0]
                        v = np.array(res[1::])
                        self.Xbestfv[2] = np.sum(v[v>0])

                de = self.Xbestfv[1] - self.G.y_opt
                self.devi[t * self.pN + i] = de

                if self.Xbestfv[2] == 0.0:
                    self.fe = 1
                    if self.FES == self.tmax * self.pN and de <= 0.0001:
                        self.FES = t * self.pN + i
                        self.su = 1
                else:
                    self.FES = self.tmax * self.pN
                    self.fe = 0
                    self.su = 0

                print((self.Xbestfv[0], self.Xbestfv[1], self.Xbestfv[2], t * self.pN + i, self.Xbest))
                # print((self.Xbestfv[1], self.Xbestfv[2], t * self.pN + i, self.fe, self.su))

                if t*self.pN+i == 5e3-1:
                    self.gbest_1 = self.Xbest.copy()
                    self.g_fit_1[0] = self.Xbestfv[0].copy()

                if t*self.pN+i == 5e4-1:
                    self.gbest_2 = self.Xbest.copy()
                    self.g_fit_2[0] = self.Xbestfv[0].copy()

                if t*self.pN+i == 5e5-1:
                    self.gbest_3 = self.Xbest.copy()
                    self.g_fit_3[0] = self.Xbestfv[0].copy()
            # if self.su == 1:
            #     break


        return self.gbest_1, self.g_fit_1, self.gbest_2, self.g_fit_2, self.gbest_3, self.g_fit_3, self.FES, self.devi, self.fe, self.su

if __name__ == "__main__":
    # def __init__(self, pN, dim, tmax, G,  F, cr, cp, e):
    d = DE(40, tt_cc.dim, 12500, tt_cc, 0.7, 0.9, 5, 0.1)
    d.init_Population()
    res = d.iterator()



