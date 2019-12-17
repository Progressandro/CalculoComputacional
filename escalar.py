from math import fsum
import numpy.matlib
import numpy as np
x = [2.718281828, -3.141592645, 1.414213562, 0.5772156649, 0.3010299957]
y = [1486.2497, 878366.9879, -22.37492, 4773714.647, 0.000185049]
# Creating products set
sets = zip(x,y)
sets32 = zip(np.float32(x), np.float32(y))
product = lambda x, y: x * y
product32 = lambda x, y: np.float32(x * y)
products = list(map(lambda x: product(*x), sets))
products32 = list(map(lambda x: product32(*x), sets32))

print('--Ascending order--')
products.sort()
products32.sort()
print('Simple: ' + str(np.float32(sum(products32))))
print('Double: ' + str(fsum(products)))

print('--Descending order--')
products.reverse()
products32.reverse()
print('Simple: ' + str(np.float32(sum(products))))
print('Double: ' + str(fsum(products)))

products.reverse()
products32.reverse()

print('--Highest to Lowest--')
positives = []
negatives = []
positives32 = []
negatives32 = []

for number in products:
  if number >= 0:
    positives.append(number)
  else:
    negatives.append(number)

for number in products32:
  if number >= 0:
    positives32.append(number)
  else:
    negatives32.append(number)

positives.sort()
positives32.sort()
negatives.sort()
negatives32.sort()
print('Simple: ' + str(np.float32(sum(positives32) + sum(negatives32))))
print('Double: ' + str(fsum(positives) + fsum(negatives)))

print('--Lowest to Highest--')

positives.reverse()
positives32.reverse()
negatives.reverse()
negatives32.reverse()
print('Simple: ' + str(np.float32(sum(positives32) + sum(negatives32))))
print('Double: ' + str(fsum(positives) + fsum(negatives)))