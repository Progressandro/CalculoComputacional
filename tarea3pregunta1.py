import math
from tabulate import tabulate
import numpy as np

def f(x):
    return (1 /  (1 + (((5.0 * x) / (d + 3.0))**2)))

d = float(9)
a = float(-(d + 3))
b = float(d + 3)
n = 10
cantidadDeNodos = n + 1
espacioEntreNodo = float((b - a)) / float(n)
acumulador = 0
matriz = [0.0] * cantidadDeNodos # Matriz n*n con todas las posiciones igual a 0.0
vector = [0.0] * cantidadDeNodos
punto_a_evaluar = 0

# print "El grado del polinomio es: ", n

for i in range(cantidadDeNodos):
    matriz[i] = [0.0] * cantidadDeNodos

for i in range(cantidadDeNodos):
    vector[i] = a + acumulador
    acumulador = acumulador + espacioEntreNodo

for i in range(cantidadDeNodos):
    matriz[i][0] = f(vector[i])

for j in range(1,cantidadDeNodos):
    for i in range(cantidadDeNodos - j):
        matriz[i][j] = ( (matriz[i+1][j-1]-matriz[i][j-1]) / (vector[i + j] - vector[i]))

print (vector)
print ("------------------------------")
print (tabulate(matriz))
print ("------------------------------")

aprx = 0
mul = 1.0
expresion = '' #------------------------------------------------------------------>Solo para mostrar el polinomio
for i in range(cantidadDeNodos):
    if (i): #--------------------------------------------------------------------->Solo para mostrar el polinomio
        expresion = expresion + ' + '#-------------------------------------------->Solo para mostrar el polinomio
    expresion = expresion + '('#-------------------------------------------------->Solo para mostrar el polinomio
    mul = matriz[0][i]
    expresion = expresion + str(mul)#--------------------------------------------->Solo para mostrar el polinomio
    for j in range(1,i+1):
        mul = mul * (punto_a_evaluar - vector[j-1])
        expresion = expresion + '*(x - (' + str(vector[j-1]) + '))'#-------------->Solo para mostrar el polinomio
    expresion = expresion + ')'#-------------------------------------------------->Solo para mostrar el polinomio
    aprx = aprx + mul

print ("------------------------------")
print ("Polinomio:")
print (expresion)#---------------------------------------------------------------->Solo para mostrar el polinomio
print ("------------------------------")
print ("El valor aproximado de f(",punto_a_evaluar,") es: ", aprx)
