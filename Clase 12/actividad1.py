import random

def cargar_lista(lista):
    for i in range(9):
        n = random.randint(0,1)
        lista.append(n)
    return lista

def porcentaje(lista):
    cont = 0
    for i in range(len(lista)):
        if lista[i] == 1:
            cont += 1
    return cont

def sumar(lista):
    sum = 0
    for i in range(len(lista)):
        sum += lista[i]
    return sum

lista_1 = []
lista_1 = cargar_lista(lista_1)
print(lista_1)
print(f"El porcentaje de numeros 1 en la lista es de {porcentaje(lista_1)}%")
print(f"La suma de todos los numeros de la lista es {sumar(lista_1)}.")
print(lista_1[1],lista_1[4],lista_1[6])