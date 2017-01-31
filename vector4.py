# -*-coding: utf-8 -*-
print "promedio de un  vector"
vector =[]
contador = int(raw_input("cantidad:"))
numero2 = 0
lista = []

for i in range (contador):
	numero = int(raw_input("numero:"))
	numero2 = numero2 + numero
	lista.append(numero)

print"este es el vector", lista 
print "esta es la suma del vector", numero2

numero3 = float(numero2) / float(contador) 
print "este es el promedio de los numeros del vector %f" % numero3