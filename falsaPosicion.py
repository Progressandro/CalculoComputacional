import numpy as np
from tabulate import tabulate
MAX_ITER = 20
a = np.float(-1)
b = np.float(1)

def f(x):
  return np.float32(pow(2 * x, 3) - ((34/7) * pow(x,2))  + ((209/49) * x) - (173/343))


def falsePosition(a, b):
  if f(a) * f(b) >= 0:
    print('Error de entrada.')
    return -1

  resultados = []
  
  c = np.float32(a)

  for i in range(MAX_ITER):
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))

    if f(c) == 0:
      break
    elif f(c) * f(a) < 0:
      b = c
    else:
      a = c
    resultados.append([i, a, b, c, f(a), f(b), f(c)])
  
  print(tabulate(resultados, headers=['i', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)']))
  print('El valor de la raiz es: ', '%.4f' %c)
falsePosition(a, b)
