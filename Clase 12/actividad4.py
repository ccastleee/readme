import random

def cargar_lista(lista):
    for i in range(11):
        n = random.randint(1, 20)
        lista.append(n)
    return lista

def ordenamiento_seleccion(lista):
    for i in range(len(lista)):
        min_indice = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_indice]:
                min_indice = j
        auxiliar = lista[i]
        lista[i] = lista[min_indice]
        lista[min_indice] = auxiliar
    return lista

numeros = []
numeros = cargar_lista(numeros)
print(numeros)
numeros = ordenamiento_seleccion(numeros)
print(numeros)