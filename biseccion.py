import math
from tabulate import tabulate

def f(x):
  return x - math.tan(x)

def biseccion(a, b, e):
  c = a
  results = [[a,b,c]]
  while((b-a) >= e):
    c = (a+b)/2
    results.append([a,b,c, f(a), f(b), f(c)])
    if (f(c) <= e):
      break
    if (f(c)*f(a) < 0):
      b = c
    else:
      a = c
  print('Resultado: ', f(c))
  print(tabulate(results, headers=['a', 'b', '(a+b)/2', 'f(a)', 'f(b)', 'f(c)']))
a = 4
b = 4.5
e = 10**-3

biseccion(a, b, e)