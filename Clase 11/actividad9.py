import random

def cargar_lista(lista):
    for i in range(4*2):
        n = random.randint(1,10)
        lista.append(n)
    return lista

def porcentaje_lista(lista):
    cont_porc = 0
    for i in range(len(lista)):
        if lista[i] < 4:
            cont_porc += 1
    porcentaje = (cont_porc*100)/len(lista)
    porcentaje = round(porcentaje, 1)
    print(f"El porcentaje de numeros menores a 4 es del {porcentaje}%")

def numero_mas_alto_lista(lista):
    maximo = -9999
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    print(f"El numero mas alto es el {maximo}.")

lista_1 = []
lista_1 = cargar_lista(lista_1)
print(f"La lista generada es: {lista_1}")
porcentaje_lista(lista_1)
numero_mas_alto_lista(lista_1)