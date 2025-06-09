def carga_lista(lista):
    for i in range(8):
        n = int(input("Ingrese un numero: "))
        while n <= 0:
            print("Error.")
            n = int(input("Ingrese un numero: "))
    lista.append(n)
    return lista

def recorrer_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    promedio = suma/len(lista)
    print(f"El promedio es: {promedio}")

lista_1 = []
lista_1 = carga_lista(lista_1)
recorrer_lista(lista_1)