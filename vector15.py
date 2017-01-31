# -*- coding: utf-8 -*-
print "la suma de numeros pares y guardad en un vector"

vector = []
contador1 = 0
cantidad = int(raw_input("cantidad de numeros:"))
matriz = []
lalo = 0

for i in range(cantidad):
	print ("------------------------------")
	numero = int(raw_input("diguite el numero:"))
	pares = numero % 2
	if pares == 0:
		print "es par:", numero
		contador1 = contador1 + numero
		vector.insert(i, numero)
	else:
		print "no es par", numero
print ("---------------------------------")
print "los siento pero para hacer una matriz de 2x2 o 3x3 tienes que llenarla|"
for i in range(3):
	matriz.append([])
	for z in range(3):
		diguital = int(raw_input("numero:"))
		matriz[i].append(diguital)

print ("----------------------------------------")
print "este es el vector", vector
print "la suma de numeros pares es:", contador1
print "esta es la matriz dados los numeros por fila:", matriz
print ("------------------------------------")

for i in range(0, 3):
	print matriz[i]
print ("-----------------------------------")
for i in range(0, 3):
	for y in range(0,3):
		print matriz[i][y]
print ("---------------------------------")
v= 0
for i, item in enumerate(matriz):
	v = matriz[i]
print v


