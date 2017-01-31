# -*- coding: utf-8 -*-
print "sumatoria de una matriz"

lista = []
matriz = []
contador = 0
contador1= 0
numero = int(raw_input("cantidad:"))

def john():
	for i in range(numero):
	matriz.append([])
	for j in range(numero):
		numero1 = int(raw_input("numero de la columna:"))
		matriz[i].append(numero1)
		contador = numero1 + contador

print "esta es la matriz:", matriz
print "esta es la suma de la matriz:", contador






