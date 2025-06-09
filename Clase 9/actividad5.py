"""Teniendo las siguientes listas:
lista1 = [2, 45.2, 3]
lista2 = [7.2, 33, 15.1]
crear una nueva lista multiplicando los valores de cada posición
correspondientes a cada lista."""

lista1 = [2, 45.2, 3]
lista2 = [7.2, 33, 15.1]
lista3 = []

lista3.append(lista1[0]*lista2[0])
lista3.append(lista1[1]*lista2[1])
lista3.append(lista1[2]*lista2[2])

print(lista3)