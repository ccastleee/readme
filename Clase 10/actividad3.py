def cargar_lista_usuario(lista):
    for i in range(cantidad):
        n = int(input("Ingrese un numero: "))
        n = validar_positivo(n)
        lista.append(n)
    return lista


def validar_positivo(x):
    while x < 0:
        print("Error, ingrese numeros positivos!")
        x = int(input("Ingrese un numero: "))
    return x



cantidad = int(input("Ingrese la cantidad de numeros que quiere cargar en la lista: "))
lista_1 = []
lista_1 = cargar_lista_usuario(lista_1)
print(lista_1)