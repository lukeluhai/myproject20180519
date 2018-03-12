from scipy import constants as C
import numpy as np
import scipy.special as S

print(C.c)
m = np.linspace(0.1, 0.9, 4)
u = np.linspace(-10, 10, 200)
results = S.ellipj(u[:,None],m[None,:])
print(y.shape for y in results)
print(results)


# 非线性方程组求解
from math import sin, cos
from scipy import optimize


def f(x):
    x0, x1, x2=x.tolist()
    return[5*x1+3, 4*x0*x0-2*sin(x1*x2), x1*x2-1.5]
# f 计算方程组的误差，[ 1 ,1 ,1 ]是未知数的初始值


result = optimize.fsolve(f, [1,1,1])
print(result)
print(f(result))
