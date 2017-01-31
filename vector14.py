# -*- coding: utf-8 -*-
jesus = 12
print "determinante de una matriz"
lista = []
matriz = []
contador = 0
numero = int(raw_input("cantidad:"))
diagonal = []
r = 0
j = 0
v = 0
if numero == 2:
	for i in range(0, numero):
		matriz.append([])
		for x in range(0, numero):
			numeros = int(raw_input("numeros:"))
			matriz[i].append(numeros)
	print matriz

	for i in range(0, numero):
		print "aca lalin", matriz[i]
		for x in range(0, numero):
			if i == x:
				lista.append(matriz[i][x])

	print "\n"
	print "aca lalo", lista
	for i in range(1, numero):
		r = lista[i] * lista[j]
		
	print "esta es la multipricacion de la primera diagonal", r

	for i in range(0, numero):
		#print matriz[i]
		for j in range(0, numero):
			if i + j == numero - 1:
				diagonal.append(matriz[i][j])
	print "\n"
	print diagonal

	p = 0
	for i in range(1, numero):
		v = diagonal[i] * diagonal[p]
	print "esta es la multipricacion de la segunda diagonal", v

	print "______"
	e = 0

	e = r - v
	print "esta es la determinante de la matriz", e

else:
	for i in range(0, numero):
		matriz.append([])
		for x in range(0, numero):
			numeros = int(raw_input("numeros:"))
			matriz[i].append(numeros)
	#print matriz

	for i in range(0, numero):
		#print matriz[i]
		for x in range(0, numero):
			if i + x == numero - 3:
				lista.append(matriz[i][x])
		break
	print "______"
	print "este es el numero por el que se va a multripricar",lista
	por = 0
	lista1 = []
	for i in range(1, numero):
		#print matriz[i]
		for x in range(1, numero):
			lista1.append(matriz[i][x])
	print lista1

	jonsi = 1
	for j, item in enumerate(lista):
		v = lista[j]
		print "aquiiii", v 

	for i, item in enumerate(lista1):
		contador = lista1[i] 
		jonsi = jonsi * contador
	print jonsi

	h = jonsi * v
	print h



	print "______"


	lista2 = []
	for i in range(0, numero):
		for x in range(0, numero):
			if i + x == numero - 2:
				lista2.append(matriz[i][x])
		break
	print "este es el numero que se va multiplicar", lista2

	lista3 = []
	for i in range(1, numero):
		for x in range(numero):
			if x != 1:
				lista3.append(matriz[i][x])

	print lista3

	eduardo = 1
	for j, item in enumerate(lista2):
		p = lista2[j]
	for j, item in enumerate(lista3):
		contador1 = lista3[j]
		eduardo = eduardo * contador1
	print eduardo
	t = eduardo * p
	print t 
	print "______"

	lista5 = []
	for i in range(0, numero):
		for x in range(0, numero):
			if i + x == numero - 1:
				lista5.append(matriz[i][x])
		break
	print "este es el numero por el que va a multiplicar", lista5

	lista6 = []
	for i in range(1, numero):
		for x in range(0, 2):
			lista6.append(matriz[i][x])
	print lista6

	andres = 1
	for j, item in enumerate(lista5):
		s = item
	for j, item in enumerate(lista6):
		contador2 = lista6[j]
		andres = andres * contador2
	print andres 
	f = s * andres 
	print f

	farore = h - t
	print "esta es la resta de las dos determinantes:", farore

	aren = farore + f
	print "esta es la suma de las determinantes:", aren
