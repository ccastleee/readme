def cargar_lista(lista):
    for i in range(4*2):
        n = int(input("Ingrese un numero: "))
        lista.append(n)
    return lista

def sumar_numeros(lista):
    sumador = 0
    for i in range(len(lista)):
        sumador += lista[i]
    return sumador

lista_1 = []
lista_1 = cargar_lista(lista_1)
print(f"La suma de los numeros de la lista es {sumar_numeros(lista_1)}.")