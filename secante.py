import math
from tabulate import tabulate


def f(x): 
  return x - 0.8 - (0.2*math.sin(x))

def metodo_secante(x0, x1, e, n, f):
  i = 1
  resultados = []
  while i <= n:
    m = (f(x0) - f(x1)) / (x1 - x0)
    x2 = x1 - (x1 - x0) * f(x1) / (f(x1) - f(x0))
    resultados.append([x0, x1, f(x0), f(x1),m, f(x1)/m, x2])
    if (abs(x2- x1) < e):
      print(tabulate(resultados, headers=['xk-1', 'xk', 'f(xk-1)', 'f(xk)', 'm', 'f(xk)/m', 'xk+1']))
      print('Resultado: ', x2)
      return x2

    i = i + 1
    x0 = x1
    x1 = x2

x0 = 0
x1 = math.pi/2
e = 10**-6
n = 20

metodo_secante(x0, x1, e, n, f)