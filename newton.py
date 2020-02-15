import math
from tabulate import tabulate
def metodo_newton(f, df, x0, e):
  delta = f(x0)
  resultados = []
  while delta > e:
    x0 = x0 - f(x0)/df(x0)
    delta = f(x0)
    resultados.append([x0, f(x0), df(x0)])
  print(tabulate(resultados, headers=['x0', 'f(x0)', 'df(x0)']))

def f(t):
  return 1 - math.exp(-1 * (math.pow(t, 2) - 12.15 * t + 36.875)) - math.exp(-1 * (math.pow(t, 2) - 7.4 * t + 13.2))

def df(t):
  return -(243/20-2*t)*math.exp((math.pow(t,2)+(243*t)/20-295/8)-(37/5-2*t))*math.exp((math.pow(-t,2)+(37*t)/5-66/5))

metodo_newton(f, df, 3.6, 10**-7)