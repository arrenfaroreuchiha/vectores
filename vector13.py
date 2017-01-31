# -*- coding: utf-8 -*-
print "sumatoria de una matriz diagonal secundaria"
diagonal = []
numeros = int(raw_input("Cuantos numeros:"))
matriz = []
v = 0
suma = 0
contador = 0

for i in range(numeros):
	matriz.append([])
	for j in range(numeros):
		numero = int(raw_input("numero de la columna:"))
		matriz[i].append(numero)
print "\n"
for i in range(0, numeros):
	print matriz[i]
	for j in range(0, numeros):
		if i + j == numeros - 1:
			suma = suma + matriz[i][j]
			diagonal.append(matriz[i][j])
			contador = contador + 1
print "\n"
print "esta es la diagonal", diagonal
x = float(suma) / float(contador)
print "este es el promedio", x




			
		
			
			
	
	
	 
	
	
	

	


