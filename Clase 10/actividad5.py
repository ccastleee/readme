def cargar_lista(lista):
    for i in range(6):
        n = float(input("Ingrese un numero: "))
        n = validar(n)
        lista.append(n)
    return lista


def validar(x):
    while x < 1.55 or x > 2.15:
        print("Error, solo numeros entre 1.55 y 2.15!")
        x = float(input("Ingrese un numero: "))
    return x

lista_1 = []
lista_1 = cargar_lista(lista_1)
print(lista_1)