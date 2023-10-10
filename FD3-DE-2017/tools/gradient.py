import numpy as np
def numberical_grandient(f, x):
    """
    求函数f在x处的梯度
    :param f:
    :param x:
    :return:
    """

    h = 1.0e-8                     #定义一个微小量，不能太小，太小计算机没法正确表示
    grad = np.zeros_like(x)      #生成和x形状相同的数组
    for idx in range(x.size):    #计算所有偏导

        tmp_val = x[idx]

        x[idx] = tmp_val + h           #要计算的那个自变量加h，其余不变

        fxh1 = f(x)                     #计算f(x+h)

        x[idx] = tmp_val        #计算f(x-h)

        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (h)    #计算偏导
        if grad[idx] != grad[idx]:
            grad[idx] = 0.0
        x[idx] = tmp_val
    return grad

if __name__ == "__main__":
    f = lambda x: x**2

    print(numberical_grandient(f,np.array([6.])))