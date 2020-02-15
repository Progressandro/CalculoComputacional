from math import pow, fsum, exp, factorial
import numpy.matlib
import numpy as np


print('-----------------Metodo e^-5-----------------')
# Double precision

sameResult = False
previousResult = -40000
previousTerms = []
n = 0
expX = -5
finalIterator = -3
while not sameResult:
  terms = previousTerms
  res = pow(-5, n) / factorial(n)
  terms.append(res)
  currentResult = fsum(terms)
  sameResult = previousResult == currentResult
  previousResult = currentResult
  previousTerms = terms
  finalIterator = n
  n = n + 1
print('++++++Double precision++++++')
print('Final Result: ' + str(previousResult))
print('Final Iteration: ' + str(finalIterator))
print('++++++++++++++++++++++++++++')

# Simple precision

sameResult = False
previousResult = -40000
previousTerms = []
n = 0
expX = -5
finalIterator = -3
while not sameResult:
  terms = previousTerms
  res = np.float32(pow(-5, n) / factorial(n))
  terms.append(res)
  currentResult = np.float32(fsum(terms))
  sameResult = previousResult == currentResult
  previousResult = currentResult
  previousTerms = terms
  finalIterator = n
  n = n + 1
print('++++++Simple precision++++++')
print('Final Result: ' + str(previousResult))
print('Final Iteration: ' + str(finalIterator))
print('++++++++++++++++++++++++++++')
print('---------------------------------------------')

print('-----------------Metodo 1/e^5-----------------')
# Double precision

sameResult = False
previousResult = -40000
previousTerms = []
n = 0
expX = -5
finalIterator = -3
while not sameResult:
  terms = previousTerms
  res = pow(5, n) * factorial(n)
  terms.append(res)
  currentResult = fsum(terms)
  sameResult = previousResult == currentResult
  previousResult = currentResult
  previousTerms = terms
  finalIterator = n
  n = n + 1
print('++++++Double precision++++++')
print('Final Result: ' + str(1 / previousResult))
print('Final Iteration: ' + str(finalIterator))
print('++++++++++++++++++++++++++++')

# Simple precision

sameResult = False
previousResult = -40000
previousTerms = []
n = 0
finalIterator = -3
while not sameResult:
  terms = previousTerms
  res = np.float32(pow(5, n) * factorial(n))
  terms.append(res)
  currentResult = np.float32(fsum(terms))
  sameResult = previousResult == currentResult
  previousResult = currentResult
  previousTerms = terms
  finalIterator = n
  n = n + 1
print('++++++Simple precision++++++')
print('Final Result: ' + str(1 / previousResult))
print('Final Iteration: ' + str(finalIterator))
print('++++++++++++++++++++++++++++')
print('----------------------------------------------')