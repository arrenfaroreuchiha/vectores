# -*-coding: utf-8 -*-
print "el mayor"

lista = []
contador = int(raw_input("cantidad:"))
numero = 0

for i in range (contador):
	numero1 = int(raw_input("numeros:"))
	lista.insert(i, numero1)
	if numero1 > numero:
		numero  = numero1
		

print "este es el vector", lista
print "este es el mayor de los numeros", numero