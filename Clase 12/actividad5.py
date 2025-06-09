import random

def cargar_auto(lista):
    for i in range(2+3):
        patente = input("Ingrese la patente: ")
        lista.append(patente)
    return lista

def valores_aleatorios(lista):
    for i in range(5):
        n = random.randint(0, 420000)
        lista.append(n)
    return lista

def ordenamiento(lista, lista_1):
    for i in range(len(lista)):
        min_indice = i 
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_indice]:
                min_indice = j
        auxiliar = lista[i]
        lista[i] = lista[min_indice]
        lista[min_indice] = auxiliar
        auxiliar_1 = lista_1[i]
        lista_1[i] = lista_1[min_indice]
        lista_1[min_indice] = auxiliar_1
    return lista, lista_1

def armar_matriz(lista, lista_1):
    matriz = []
    for i in range(len(lista)):
        fila = [lista[i], lista_1[i]]
        matriz.append(fila)
    for i in range(len(matriz)):
        print(matriz[i][0], matriz[i][1])

vehiculo = []
km = []

vehiculo = cargar_auto(vehiculo)
km = valores_aleatorios(km)
print(vehiculo)
print(km)
vehiculo, km = ordenamiento(vehiculo, km)
print(f"Patentes ordenadas alfabeticamente: \n{vehiculo}\nKM ordenados de menor a mayor: \n{km}")
armar_matriz(vehiculo, km)