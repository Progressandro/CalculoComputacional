import math
from tabulate import tabulate

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
    return math.atan(term * x) - 1

def df(x):
    return term / (1 + (term**2)*(x**2))

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

ci = 5 
term = (ci + 1) / 2 
N = 15 
exp = -3 
startingPoint = 0.7 
power = -1 * exp 

MAX_POINT = 20000 
e = 10**-3

# print ('Lowest point: ', getLowestPoint(f, df, startingPoint, e, N))
newton(f, df, math.pi / 2, e, N)
newton(f, df, math.pi * 5, e, N)
newton(f, df, math.pi * 10, e, N)
