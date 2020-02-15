from math import fsum, pow
import numpy.matlib
import numpy as np

k = 1
terms = []
previousResult = -3000
sameResult = False
while not sameResult:
  for i in range(1, k):
    terms.append(1 / pow(k, 4))
  current = fsum(terms)
  print('Previous: ' + str(previousResult))
  print('current: ' + str(current))
  print('Terms: ' + str(len(terms)))
  sameResult = previousResult == current
  previousResult = current
  k = k + 1
print('Iterations: ' + str(len(terms)))