# -*-coding: utf-8 -*-
print "sumatoria de un vector"
contador = int(raw_input("cantidad:"))
lista = []
numero2 = 0
for i in range (contador):
	numero = int(raw_input("numero:"))
	lista.append(numero)
	numero2 = numero2 + numero
	

print "este es el vector", lista
print "esta es la suma de un vector", numero2

