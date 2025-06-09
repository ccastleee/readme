def cargar_lista(lista):
    for i in range(4):
        n = input("Ingrese un nombre: ").capitalize()
        n = validar_nombre(n)
        lista.append(n)
    return lista

def validar_nombre(x):
    while len(x) < 3 or len(x) > 12:
        print("Error, el nombre tiene que tener entre 3 y 12 letras!")
        x = input("Ingrese un nombre: ").capitalize()
    return x

lista_1 = []
lista_1 = cargar_lista(lista_1)
print(lista_1)