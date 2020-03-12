import math
from tabulate import tabulate

def newtons_method(f, df, x0, e, n):
    delta = abs(f(x0))
    tablaDeResultados = []
    i = 0
    while (delta > e) and (df(x0) != 0) and (i < n):
        x1 = x0 - f(x0)/df(x0)
        delta = abs(f(x0))
        tablaDeResultados.append([x0, f(x0), df(x0)])
        x0 = x1
        i = i + 1
    tablaDeResultados.append([x0, f(x0), df(x0)])
    print(tabulate(tablaDeResultados, headers=['Xi', 'f(Xi)', 'df(Xi)'], numalign="left"))
    return ((i == n) or not(x0 < LIMIT_POINT))

def f(x):
    return ((x**2) / 4) - ((math.sin(x)) * x) - ((math.cos(2 * x)) / 2) + 0.5

def df(x):
    return (math.sin(2*x)) - (math.sin(x)) - (x * math.cos(x)) + (x / 2)

N = 25 
LIMIT_POINT = 10000

error = 10**-7

newtons_method(f, df, (math.pi / 2), error, N)
newtons_method(f, df, (math.pi * 5), error, N)
newtons_method(f, df, (math.pi * 10), error, N)
