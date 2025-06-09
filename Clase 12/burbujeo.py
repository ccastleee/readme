def ordenamiento_burbujeo(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                auxiliar = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = auxiliar
    return lista

numeros = [2, 52, 21, 99, 3]
numeros = ordenamiento_burbujeo(numeros)
print(numeros)