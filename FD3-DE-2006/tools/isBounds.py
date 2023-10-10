

def isBounds(X_new, bounds):
    flag = True
    for i in range(len(X_new)):
        if X_new[i] < bounds[i][0] or X_new[i] > bounds[i][1]:
            flag = False
    return flag