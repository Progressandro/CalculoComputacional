import math
from tabulate import tabulate
import numpy as np

def f(x):
    return (1 /  (1 + (((5.0 * x) / (d + 3.0))**2)))

def g(k):
    return (d + 3.0) * (math.cos((((2.0 * k) + 1.0) / 22.0) * math.pi))

d = float(5)
a = float(-(d + 3))
b = float(d + 3)
n = 10
nodes = n + 1
gap = float((b - a)) / float(n)
matrix = [0.0] * nodes 
vectorX = [0.0] * nodes
vectorY = [0.0] * nodes
evaluate = 0

for i in range(nodes):
    matrix[i] = [0.0] * nodes

for i in range(nodes):
    vectorX[i] = g(i)

for i in range(nodes):
    matrix[i][0] = f(vectorX[i])
    vectorY[i] = matrix[i][0]

for j in range(1,nodes):
    for i in range(nodes - j):
        matrix[i][j] = ( (matrix[i+1][j-1]-matrix[i][j-1]) / (vectorX[i + j] - vectorX[i]))

print (tabulate([vectorX, vectorY]))
print (tabulate([matrix[0]]))

approximation = 0
mul = 1.0
expression = '' 
for i in range(nodes):
    if (i): 
        expression = expression + ' + '
    mul = matrix[0][i]
    expression = expression + str(mul)
    for j in range(1,i+1):
        mul = mul * (evaluate - vectorX[j-1])
        expression = expression + '*(x-(' + str(vectorX[j-1]) + '))'
    approximation = approximation + mul

print ("Polinomial:")
print (expression)
print ("------------------------------")
print ("f(",evaluate,") approximation: ", approximation)
