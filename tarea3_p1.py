import math
from tabulate import tabulate
import numpy as np

def f(x):
    return (1 /  (1 + (((5.0 * x) / (d + 3.0))**2)))

d = float(5)
a = float(-(d + 3))
b = float(d + 3)
n = 10
nodes = n + 1
gap = float((b - a)) / float(n)
acc = 0
matrix = [0.0] * nodes 
vector = [0.0] * nodes
evaluate = 0

for i in range(nodes):
    matrix[i] = [0.0] * nodes

for i in range(nodes):
    vector[i] = a + acc
    acc = acc + gap

for i in range(nodes):
    matrix[i][0] = f(vector[i])

for j in range(1,nodes):
    for i in range(nodes - j):
        matrix[i][j] = ( (matrix[i+1][j-1]-matrix[i][j-1]) / (vector[i + j] - vector[i]))

print (vector)
print (tabulate(matrix))

approximation = 0
mul = 1.0
expression = ''
for i in range(nodes):
    if (i):
        expression = expression + ' + '
    expression = expression + '('
    mul = matrix[0][i]
    expression = expression + str(mul)
    for j in range(1,i+1):
        mul = mul * (evaluate - vector[j-1])
        expression = expression + '*(x - (' + str(vector[j-1]) + '))'
    expression = expression + ')'
    approximation = approximation + mul

print ("\n\n")
print ("Polynomial:")
print (expression)
print ("------------------------------")
print ("f(",evaluate,") approximation: ", approximation)
