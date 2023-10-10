from functions import C10
from functions import C11
from functions import C12
from functions import C13
from algorithms import myDE_fit
import numpy as np
from tools import statics


ps = ["C10", "C11", "C12", "C13"]
d = 50

for p in ps:
    solutions1 = []
    fitnesses1 = []
    solutions2 = []
    fitnesses2 = []
    solutions3 = []
    fitnesses3 = []
    fes = []
    fs = 0  ## 可行率
    sus = 0  ## 成功率
    if p == "C10":
        G = C10
        e = 0.00001
    elif p == "C11":
        G = C11
        e = 0.00000001
    elif p == "C12":
        G = C12
        e = 1
    else:
        G = C13
        e = 1
    for n in range(25):
        # DE(40, 4, 30, 600000, C07, 0.7, 0.9, 5, 1, 0, 0, 0)
        # def __init__(self, pN0, pN1, dim, tmax, G, F, cr, cp, e, Ne, epsilon0, tc):

        P = myDE_fit.DE(40, 4, 50, 1000000, G, 0.7, 0.9, 5, e, 3, 1, 0)
        P.init_Population()
        gbest_1, g_fit_1, gbest_2, g_fit_2, gbest_3, g_fit_3, FES, devi, fe, su = P.iterator()

        np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_3/gbest_" + str(n) + "_1.txt", gbest_1)
        np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_3/g_fit_" + str(n) + "_1.txt", g_fit_1)
        np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_4/gbest_" + str(n) + "_2.txt", gbest_2)
        np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_4/g_fit_" + str(n) + "_2.txt", g_fit_2)
        np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_5/gbest_" + str(n) + "_3.txt", gbest_3)
        np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_5/g_fit_" + str(n) + "_3.txt", g_fit_3)

        np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_" + str(n) + ".txt", [FES])
        # np.savetxt("./results/d=" + str(d) + "/" + p + "/devi_" + str(n) + ".txt", devi)

        fes.append(FES)

        fs = fs + fe
        sus = sus + su

        solutions1.append(gbest_1)
        fitnesses1.append(g_fit_1[0])

        solutions2.append(gbest_2)
        fitnesses2.append(g_fit_2[0])

        solutions3.append(gbest_3)
        fitnesses3.append(g_fit_3[0])

    np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_3/solutions.txt", solutions1)
    np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_3/fitnesses.txt", fitnesses1)

    np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_4/solutions.txt", solutions2)
    np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_4/fitnesses.txt", fitnesses2)

    np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_5/solutions.txt", solutions3)
    np.savetxt("./results/d=" + str(d) + "/" + p + "/FES_5/fitnesses.txt", fitnesses3)

    np.savetxt("./results/d=" + str(d) + "/" + p + "/fes.txt", fes)

    result0 = statics.st2(fes)


    result1 = statics.st1(solutions1, fitnesses1, G.f, d)
    result2 = statics.st1(solutions2, fitnesses2, G.f, d)
    result3 = statics.st1(solutions3, fitnesses3, G.f, d)

    fs = fs / 25
    sus = sus / 25

    result4 = np.array([fs, sus])

    np.savetxt("./results/d=" + str(d) + "/" + p + "/res0.txt", result0)
    np.savetxt("./results/d=" + str(d) + "/" + p + "/res1.txt", result1)
    np.savetxt("./results/d=" + str(d) + "/" + p + "/res2.txt", result2)
    np.savetxt("./results/d=" + str(d) + "/" + p + "/res3.txt", result3)

    np.savetxt("./results/d=" + str(d) + "/" + p + "/res4.txt", result4)




