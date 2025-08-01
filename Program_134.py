# SciPy Optimizers in Python

from scipy.optimize import root
from scipy.optimize import minimize
from math import cos


def eqn(x):
    return x + cos(x)


myroot = root(eqn, 0)
print(myroot.x)
print(myroot)


def eqn(x):
    return x**2 + x + 2


mymin = minimize(eqn, 0, method="BFGS")
print(mymin)