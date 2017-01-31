# -*- coding: utf-8 -*-
print "sumatoria de una matriz diagonal"
lista = []
numeros = int(raw_input("Cuantos numeros:"))
matriz = []

for i in range(numeros):
	matriz.append([])
	for j in range(numeros):
		numero = int(raw_input("numero de la columna:"))
		matriz[i].append(numero)

for i in range(0, numeros):
	for x in range(0, numeros):
		if i == x:
			lista.append(matriz[i][x])

print "La diagonal es ", lista



	
	


