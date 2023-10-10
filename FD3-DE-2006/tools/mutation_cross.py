from random import choice
import numpy as np
def mutation_cross_1(ls2, ld, i, Q, Xb, F_a, F_b, cr):
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

    X_tmp = Xp3 + F_a * (Xb - Xp2) + F_b * (Q[i] - Xp1)

    crossover_point = choice(ld)
    X_new = Q[i]

    """
    二项式交叉
    """
    for j in range(len(ld)):
        if np.random.random() < cr or j == crossover_point:
            X_new[j] = X_tmp[j]
    return X_new