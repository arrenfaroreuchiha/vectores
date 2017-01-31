# -*- coding: utf-8 -*-
print "sumatoria y promedio de una matriz"

lista = []
matriz = []
contador = 0
contador1 = 0
numero = int(raw_input("cantidad:"))

for i in range(numero):
	matriz.append([])
	for j in range(numero):
		numero1 = int(raw_input("numero de la columna:"))
		matriz[i].append(numero1)
		contador = numero1 + contador
		contador1 += 1

print "esta es la matriz:", matriz
print "esta es la suma de la matriz:", contador
print "numeros total", contador1

promedio = float(contador) / float(contador1)
print "el promedio es:", promedio

