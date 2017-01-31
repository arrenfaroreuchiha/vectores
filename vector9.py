# -*- coding: utf-8 -*-
print "el menor y mayor en un vector"
lista = []
numero2 = 0
numeros = 0
mayor = 0
menor = 0
numeros = int(raw_input("cantidad:"))
menor2 = 0

for i in range(0, numeros):
	i += 1
 	numero2 = int(raw_input("digita el numero %d:" % i))
 	lista.append(numero2)

for i in range(0, numeros):
	x = i + 1
	for x in range(x, numeros):
		if lista[i] > lista[x]:
			mayor = lista[i]
			menor = lista[x]
		else:
			menor = lista[i]
			mayor = lista[x]
	break
			
print "el vector es:", lista
print "el mayor de los numeros es:", mayor
print "el menor de los numeros es:", menor
 	

	
	
 	
 
 	


 		






 	