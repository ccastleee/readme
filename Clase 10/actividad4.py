def cargar_lista(lista):
    for i in range(3+2):
        n = int(input("Ingrese un numero: "))
        n = validar_pares(n)
        lista.append(n)
    return lista

def validar_pares(x):
    while x % 2 != 0:
        print("Error, solo numeros pares!")
        x = int(input("Ingrese un numero: "))
    return x

lista_1 = []
lista_1 = cargar_lista(lista_1)
print(lista_1)