# -*- coding: utf-8 -*-
import math
lista = []
moda, x, suma, r2 = 0, 0, 0, 0

print "desviacion estandar"
numeros = int(raw_input("Cuantos numeros: "))

for i in range(0, numeros):
	i += 1
	numero = int(raw_input("Digita el numero %d: " % i))
	lista.append(numero)
	suma = suma + numero

promedio = suma / numeros
# print " %f " % promedio

for i in range(0, numeros):
	x = i + 1
	print lista
	print "Numero %d es, %s" % (x, lista[i])

for i in range(0, numeros):
	r1 = (lista[i] - promedio) ** 2
	r2 = r2 + r1

desviacion = math.sqrt(r2/5)

print "La desviacion es, ", desviacion




	

 



 
