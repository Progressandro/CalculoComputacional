import math
from tabulate import tabulate
import numpy as np

def f(x):
  return np.float32(pow(2 * x, 3) - ((34/7) * pow(x,2))  + ((209/49) * x) - (173/343))

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

x0 = -1
x1 = 1
e = 10**-6
n = 20

metodo_secante(x0, x1, e, n, f)
