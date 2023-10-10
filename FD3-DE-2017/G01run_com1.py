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

from algorithms import DE_com
from fitness import fit_com
import numpy as np
from tools import statics_com


ps = ["C01"]

d = 100

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
    if p == "C01":
        G, cp, e = C01, 5, 1
    elif p == "C02":
        G, cp, e = C02, 5, 1
    elif p == "C03":
        G, cp, e = C03, 5, 1
    elif p == "C04":
        G, cp, e = C04, 5, 1
    elif p == "C05":
        G, cp, e = C05, 5, 1
    elif p == "C06":
        G, cp, e = C06, 5, 1
    elif p == "C07":
        G, cp, e = C07, 5, 1
    elif p == "C08":
        G, cp, e = C08, 5, 1
    elif p == "C09":
        G, cp, e = C09, 5, 1
    elif p == "C10":
        G, cp, e = C10, 5, 1
    elif p == "C11":
        G, cp, e = C11, 5, 1
    elif p == "C12":
        G, cp, e = C12, 5, 1
    elif p == "C13":
        G, cp, e = C13, 5, 1
    elif p == "C14":
        G, cp, e = C14, 5, 1
    elif p == "C15":
        G, cp, e = C15, 5, 1
    elif p == "C16":
        G, cp, e = C16, 5, 1
    elif p == "C17":
        G, cp, e = C17, 5, 1
    elif p == "C18":
        G, cp, e = C18, 5, 1
    elif p == "C19":
        G, cp, e = C19, 5, 1
    elif p == "C20":
        G, cp, e = C20, 5, 1
    elif p == "C21":
        G, cp, e = C21, 5, 1
    elif p == "C22":
        G, cp, e = C22, 5, 1
    elif p == "C23":
        G, cp, e = C23, 5, 1
    elif p == "C24":
        G, cp, e = C24, 5, 1
    elif p == "C25":
        G, cp, e = C25, 5, 1
    elif p == "C26":
        G, cp, e = C26, 5, 1
    elif p == "C27":
        G, cp, e = C27, 5, 1
    else:
        G, cp, e = C28, 5, 1

    for n in range(25):
        # def __init__(self, pN0, pN1, dim, tmax, G, Ne, epsilon, tc, F, cr, cp):
        # d = DE(40, 4, 30, 600000, C03, 3, 1, 15000, 0.7, 0.9, 5)
        P = DE_com.DE(40, 4, d, 2000000, G, 3, 1, 1600000, 0.7, 0.9, 5)
        P.init_Population()
        gbest_1, g_fit_1, gbest_2, g_fit_2, gbest_3, g_fit_3, FES, devi, fe, su = P.iterator()

        np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_3/gbest_" + str(n) + "_1.txt", gbest_1)
        np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_3/g_fit_" + str(n) + "_1.txt", g_fit_1)
        np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_4/gbest_" + str(n) + "_2.txt", gbest_2)
        np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_4/g_fit_" + str(n) + "_2.txt", g_fit_2)
        np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_5/gbest_" + str(n) + "_3.txt", gbest_3)
        np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_5/g_fit_" + str(n) + "_3.txt", g_fit_3)

        np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_" + str(n) + ".txt", [FES])
        # np.savetxt("./results/epsilon/" + p + "/devi_" + str(n) + ".txt", devi)

        fes.append(FES)

        fs = fs + fe
        sus = sus + su

        solutions1.append(gbest_1)
        fitnesses1.append(g_fit_1)

        solutions2.append(gbest_2)
        fitnesses2.append(g_fit_2)

        solutions3.append(gbest_3)
        fitnesses3.append(g_fit_3)

    np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_3/solutions.txt", solutions1)
    np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_3/fitnesses.txt", fitnesses1)

    np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_4/solutions.txt", solutions2)
    np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_4/fitnesses.txt", fitnesses2)

    np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_5/solutions.txt", solutions3)
    np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/FES_5/fitnesses.txt", fitnesses3)

    np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/fes.txt", fes)

    result0 = statics_com.st2(fes)

    result1 = statics_com.st1(solutions1, fitnesses1, G.f, d)
    result2 = statics_com.st1(solutions2, fitnesses2, G.f, d)
    result3 = statics_com.st1(solutions3, fitnesses3, G.f, d)

    fs = fs / 25
    sus = sus / 25

    result4 = np.array([fs, sus])

    np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/res0.txt", result0)
    np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/res1.txt", result1)
    np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/res2.txt", result2)
    np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/res3.txt", result3)
    np.savetxt("./results/d="+str(d)+"/epsilon1/" + p + "/res4.txt", result4)




