import math
from tabulate import tabulate

#------------------------> Metodo de Newton <---------------------------------#
def newtons_method(f, df, x0, e, n, viewTables):
    delta = abs(f(x0))
    tablaDeResultados = []
    i = 0
    while (delta > e) and (df(x0) != 0) and (i < n):
        x1 = x0 - f(x0)/df(x0)
        delta = abs(f(x0))
        if (viewTables):
            tablaDeResultados.append([x0, f(x0), df(x0)])
        x0 = x1
        # print df(x0)
        i = i + 1
    if (viewTables):
        tablaDeResultados.append([x0, f(x0), df(x0)])
        print(tabulate(tablaDeResultados, headers=['Xi', 'f(Xi)', 'df(Xi)']))
    return ((i == n) or not(x0 < MAX_POINT)) #----------------------------------------> Retorna True si el metodo diverge

#------------> Funcion Que Evalua a F(x) En El Punto Inicial Dado <------------#
def f(x):
    return x - math.tan(x)

#------------> Funcion Que Evalua a F'(x) En El Punto Inicial Dado <-----------#
def df(x):
    return 1 - (1 / (math.cos(x)**2))

def FindRoots(f, df, error, n, roots):
    i = 1
    results = []
    while (i <= roots):
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
MAX_POINT = 10000
error = 10**-7
rootNumber = 10
print(FindRoots(f, df, error, N, rootNumber))
