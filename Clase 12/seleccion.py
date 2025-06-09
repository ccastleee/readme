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

numeros = [10, 24, 2, 54, 99]
numeros = ordenamiento_seleccion(numeros)
print(numeros)