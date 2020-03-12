import math
from tabulate import tabulate

def newtons_method(f, df, x0, e, n):
    delta = abs(f(x0))
    tablaDeResultados = []
    i = 0
    while (delta > e) and (df(x0) != 0) and (i < n) and (abs(x0) < limitePuntoObtenido):
        x1 = x0 - f(x0)/df(x0)
        delta = abs(f(x0))

        tablaDeResultados.append([x0, f(x0), df(x0)])
        x0 = x1
        i = i + 1
    tablaDeResultados.append([x0, f(x0), df(x0)])
    print(tabulate(tablaDeResultados, headers=['Xi', 'f(Xi)', 'df(Xi)'], numalign="left"))
    return ((i == n) or not(abs(x0) < limitePuntoObtenido)) #----------------------------------------> Retorna True si el metodo diverge

def f(x):
    return math.atan(coeficiente * x) - 1

def df(x):
    return coeficiente / (1 + (coeficiente**2)*(x**2))

def getLowestPoint(f, df, x0, e, n):
    posicionAModificar = 0 
    incremento = 10 ** ((-1) * posicionAModificar)
    puntoInicialAnterior = x0 
    while (posicionAModificar <= cantidadDePosicionesAModificar):
        if (not(newtons_method(f, df, x0, e, n))): 
            puntoInicialAnterior = x0 
            x0 = x0 + incremento
        else: 
            posicionAModificar = posicionAModificar + 1
            if (posicionAModificar <= cantidadDePosicionesAModificar):
                x0 = puntoInicialAnterior
            incremento = 10 ** ((-1) * posicionAModificar)
    return x0 

terminalDeCedula = 5 
coeficiente = (terminalDeCedula + 1) / 2
N = 15 
exp = -3
startingPoint = 0.7
cantidadDePosicionesAModificar = -1 * exp

limitePuntoObtenido = 20000

error = 10**-3


print ('Punto mas bajo: ', getLowestPoint(f, df, startingPoint, error, N))
