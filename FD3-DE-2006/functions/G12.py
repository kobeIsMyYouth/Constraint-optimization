bounds = [(0,10),(0,10),(0,10)]
x_opt = [5,5,5]
y_opt = -1

dim = 3
fmax = -0.25
fmin = -1
vmax = 243
vn = 1

def f(X):
    y = -(100-(X[0]-5)**2-(X[1]-5)**2-(X[2]-5)**2)/100
    p = round(X[0], 0)
    q = round(X[1], 0)
    r = round(X[2], 0)
    g = (X[0]-p)**2+(X[1]-q)**2+(X[2]-r)**2-0.0625

    return y, g
if __name__ == "__main__":
    print(round(2.50,0))