# -*- coding: utf-8 -*-
print "lectura de una matriz por colomna y fila"
lista = []
matriz = []
for i in range(3):
	matriz.append([])
	for j in range(3):
		numero = raw_input("numero de la columna: ")
		matriz[i].append(numero)
	

print "esta es la matriz por fila", matriz
print "__________"

for i in range(0, 3):
	print matriz[i]

for i in range(0, 3):
	# print  matriz[i]
	for j in range(0, 3):
		print matriz[i][j]
