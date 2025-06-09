import random

def cargar_lista(lista):
    for i in range(5+5):
        n = random.randint(100,150)
        n = validar_pares(n)
        lista.append(n)
    return lista


def validar_pares(numero):
    while numero % 2 != 0:
        numero = random.randint(100,150)
    return numero

def promedio(lista):
    sum = 0
    for i in range(len(lista)):
        sum += lista[i]
    prom = sum/len(lista)
    return prom

def valor_bajo(lista):
    minimo = 9999
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo

lista_1 = []
lista_1 = cargar_lista(lista_1)
print(lista_1)
print(f"El promedio de los elementos de la lista es {promedio(lista_1)}.")
print(f"El menor elemento de la lista es el {valor_bajo(lista_1)}.")
