# -*- coding: utf-8 -*-
print "moda"
lista = []
moda, x, moda2 = 0, 0, 0
condicion = False

numeros = int(raw_input("Cuantos numeros:"))

for i in range(0, numeros):
	i += 1
	numero = int(raw_input("Digita el numero %d:" % i))
	lista.append(numero)

for i in range(0, numeros):
	x = i + 1
	for x in range(x, numeros):
		if lista[i] == lista[x]:
			if condicion:
				moda2 = lista[i]
				condicion = False
			else:
		 		moda = lista[i]
		 		condicion = True
if condicion:
	print "La moda es:", moda
else:
	print "La moda es:", moda
	print "la sedunda moda es:", moda2