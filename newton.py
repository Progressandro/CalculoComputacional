import math
from tabulate import tabulate
def metodo_newton(f, df, x0, e):
  delta = f(x0)
  resultados = []
  while delta > e:
    x0 = x0 - f(x0)/df(x0)
    delta = f(x0)
    resultados.append([x0, f(x0), df(x0)])
    print 'Raiz encontrada: ', x0
    print 'f(x) en la raiz: ', f(x0)
  print(tabulate(resultados, headers=['x0', 'f(x0)', 'df(x0)']))

def f(x):
  return -(math.sin(x)/5) + x - (4/5)

def df(x):
  return 1 - (math.cos(x)/5)

metodo_newton(f, df, math.pi/2, 10**-6)
