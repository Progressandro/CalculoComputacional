import math
from tabulate import tabulate

N = 15 
exp = -3 
MAX_POINT = 20000 
e = 10**-3

def newton(f, df, x0, e, n):
    delta = abs(f(x0))
    resultados = []
    i = 0
    while (delta > e) and (df(x0) != 0) and (i < n) and (abs(x0) < MAX_POINT):
        x1 = x0 - f(x0)/df(x0)
        delta = abs(f(x0))

        resultados.append([x0, f(x0), df(x0)])
        x0 = x1
        i = i + 1
    resultados.append([x0, f(x0), df(x0)])
    print(tabulate(resultados, headers=['Xi', 'f(Xi)', 'df(Xi)'], tablefmt="github", numalign="left", stralign="left"))
    return ((i == n) or not(abs(x0) < MAX_POINT))

def f(x):
    return 1 - math.exp(-1 * (math.pow(x, 2) - (12.15 * x) + 36.875)) - math.exp(-1 * (math.pow(x, 2) - (7.4 * x) + 13.2))

def df(x):
    return -((-2 * x) + 12.15) * (math.exp((-1 * (x**2)) + (12.15 * x) - 36.875)) - (((-2 * x) + 7.4) * math.exp((-1 * (x**2)) + (7.4 * x) - 13.2))

def getLowestPoint(f, df, x0, e, n):
    position = 0 
    inc = 10 ** ((-1) * position)
    lastStartingPoint = x0 
    while (position <= power): 
        if (not(newton(f, df, x0, e, n))): 
            lastStartingPoint = x0 
            x0 = x0 + inc 
        else: 
            position = position + 1 
            if (position <= power): 
                x0 = lastStartingPoint  
            inc = 10 ** ((-1) * position) 
    return x0 

newton(f, df, 3.5, e, N)
newton(f, df, 3.6, e, N)
newton(f, df, 3.7, e, N)
newton(f, df, 3.8, e, N)
newton(f, df, 3.9, e, N)
