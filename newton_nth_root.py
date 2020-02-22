import math
from tabulate import tabulate

def newtons_method(f, df, x0, e, n, viewTables):
    delta = abs(f(x0))
    results = []
    i = 0
    while (delta > e) and (df(x0) != 0) and (i < n):
        x1 = x0 - f(x0)/df(x0)
        delta = abs(f(x0))
        if (viewTables):
            results.append([x0, f(x0), df(x0)])
        x0 = x1
        i = i + 1
    if (viewTables):
        results.append([x0, f(x0), df(x0)])
        print(tabulate(results, headers=['Xi', 'f(Xi)', 'df(Xi)']))
    return ((i == n) or not(x0 < limitePuntoObtenido))

def f(x):
    return x - math.tan(x)

def df(x):
    return 1 - (1 / (math.cos(x)**2))

def encontrarRaices(f, df, error, n, cantR):
    i = 1
    results = []
    while (i <= cantR):
        a = (i * math.pi)
        b = a + 1.57
        c = (a + b) / 2
        while (newtons_method(f, df, c, error, n, False)):
            if ((f(a) * f(c)) > 0):
                b = c
            else:
                a = c
            c = (a + b) / 2
        i = i + 1
        results.append(c)
    for puntoInicial in results:
        newtons_method(f, df, puntoInicial, error, n, True)
    return results
N = 7 

limitePuntoObtenido = 20000 

error = 10**-7 
cantRaices = 10
roots = encontrarRaices(f, df, error, N, cantRaices)
print(roots)
