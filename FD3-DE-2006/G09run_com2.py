from functions import G09
from algorithms import DE_com
from fitness import fit_com
import numpy as np
from tools import statics_com

solutions1 = []
fitnesses1 = []
solutions2 = []
fitnesses2 = []
solutions3 = []
fitnesses3 = []
fes = []
fs = 0  ## 可行率
sus = 0  ## 成功率


p = "G09"
for n in range(25):
    P = DE_com.DE(40, G09.dim, 12500, G09, 0, 1, 2500, 0.7, 0.9, 5)
    P.init_Population()
    gbest_1, g_fit_1, gbest_2, g_fit_2, gbest_3, g_fit_3, FES, devi, fe, su = P.iterator()

    np.savetxt("./results/epsilon2/" + p + "/FES_3/gbest_" + str(n) + "_1.txt", gbest_1)
    np.savetxt("./results/epsilon2/" + p + "/FES_3/g_fit_" + str(n) + "_1.txt", g_fit_1)
    np.savetxt("./results/epsilon2/" + p + "/FES_4/gbest_" + str(n) + "_2.txt", gbest_2)
    np.savetxt("./results/epsilon2/" + p + "/FES_4/g_fit_" + str(n) + "_2.txt", g_fit_2)
    np.savetxt("./results/epsilon2/" + p + "/FES_5/gbest_" + str(n) + "_3.txt", gbest_3)
    np.savetxt("./results/epsilon2/" + p + "/FES_5/g_fit_" + str(n) + "_3.txt", g_fit_3)

    np.savetxt("./results/epsilon2/" + p + "/FES_" + str(n) + ".txt", [FES])
    np.savetxt("./results/epsilon2/" + p + "/devi_" + str(n) + ".txt", devi)

    fes.append(FES)

    fs = fs + fe
    sus = sus + su

    solutions1.append(gbest_1)
    fitnesses1.append(g_fit_1)

    solutions2.append(gbest_2)
    fitnesses2.append(g_fit_2)

    solutions3.append(gbest_3)
    fitnesses3.append(g_fit_3)

np.savetxt("./results/epsilon2/" + p + "/FES_3/solutions.txt", solutions1)
np.savetxt("./results/epsilon2/" + p + "/FES_3/fitnesses.txt", fitnesses1)

np.savetxt("./results/epsilon2/" + p + "/FES_4/solutions.txt", solutions2)
np.savetxt("./results/epsilon2/" + p + "/FES_4/fitnesses.txt", fitnesses2)

np.savetxt("./results/epsilon2/" + p + "/FES_5/solutions.txt", solutions3)
np.savetxt("./results/epsilon2/" + p + "/FES_5/fitnesses.txt", fitnesses3)

np.savetxt("./results/epsilon2/" + p + "/fes.txt", fes)

result0 = statics_com.st2(fes)

result1 = statics_com.st1(solutions1, fitnesses1, G09.f)
result2 = statics_com.st1(solutions2, fitnesses2, G09.f)
result3 = statics_com.st1(solutions3, fitnesses3, G09.f)

fs = fs / 25
sus = sus / 25

result4 = np.array([fs, sus])

np.savetxt("./results/epsilon2/" + p + "/res0.txt", result0)
np.savetxt("./results/epsilon2/" + p + "/res1.txt", result1)
np.savetxt("./results/epsilon2/" + p + "/res2.txt", result2)
np.savetxt("./results/epsilon2/" + p + "/res3.txt", result3)
np.savetxt("./results/epsilon2/" + p + "/res4.txt", result4)




