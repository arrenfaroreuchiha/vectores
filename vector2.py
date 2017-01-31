# -*- coding: utf-8 -*-

# lista = []
# for i in range(0,5):
# 	numero = raw_input("numero: ")
# 	lista.append(numero)

# print lista

lista = []
for i in range(0,5):
	numero = raw_input("numero: ")
	lista.insert(i, numero)

print lista
maximo = max(lista)
print maximo


