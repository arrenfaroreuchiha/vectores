
lista = []
moda, x, moda2 = 0, 0, 0
condicion = False

numeros = int(raw_input("Cuantos numeros: "))

for i in range(0, numeros):
	i += 1
	numero = int(raw_input("Digita el numero %d: " % i))
	lista.append(numero)

 for j, item in enumerate(lista):
	print j, item

for i in range(0, numeros):
	# print "_________"
	x = i + 1
	for x in range(x, numeros):
		# print "posicion i %d  y el valor es %d" % (i,lista[i])
		# print "posicion x %d  y el valor es %d" % (x,lista[x])
		if lista[i] == lista[x]:
			if condicion:
				moda2 = lista[i]
				condicion = False
			else:
		 		moda = lista[i]
		 		condicion = True
if condicion:
	print "La moda es, ", moda
else:
	print "La moda es, ", moda, moda2