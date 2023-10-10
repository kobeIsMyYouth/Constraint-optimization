from functions import C08
from algorithms import myDE_fit
import numpy as np
from tools import statics


ps = ["C08"]
d = 10
cp = 4
e = 0.0005

for p in ps:
    fs = []
    vs = []
    FESs = []

    for n in range(25):
        # DE(40, 4, 30, 600000, C07, 0.7, 0.9, 5, 1, 0, 0, 0)
        # def __init__(self, pN0, pN1, dim, tmax, G, F, cr, cp, e, Ne, epsilon0, tc):

        P = myDE_fit.DE(40, 4, d, 200000, C08, 0.7, 0.9, cp, e, 3, 1, 0)
        P.init_Population()
        f, v, FES = P.iterator()

        fs.append(f)
        vs.append(v)
        FESs.append(FES)



    np.savetxt("./results/parameter_analysis/cp=" + str(cp) + ",e=" + str(e) + "/fs.txt", fs)
    np.savetxt("./results/parameter_analysis/cp=" + str(cp) + ",e=" + str(e) + "/vs.txt", vs)
    np.savetxt("./results/parameter_analysis/cp=" + str(cp) + ",e=" + str(e) + "/FESs.txt", FESs)




