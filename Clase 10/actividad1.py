def cargar_lista(lista):
    for i in range(5):
        n = int(input("Ingrese un numero: "))
        lista.append(n)
    return lista

lista_1 = []
lista_1 = cargar_lista(lista_1)
print(lista_1)