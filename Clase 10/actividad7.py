def cargar_lista(lista):
    for i in range(8):
        n = int(input("Ingrese un numero: "))
        lista.append(n)
    return lista

def mostrar_negativos(lista):
    for i in range(len(lista)):
        if lista[i] < 0:
            print(lista[i])

lista_1 = []
lista_1 = cargar_lista(lista_1)
mostrar_negativos(lista_1)