def cargar_lista(lista):
    for i in range(cantidad):
        n = int(input("Ingrese un numero: "))
        lista.append(n)
    return lista

def pares(lista):
    cont_pares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            cont_pares += 1
    return cont_pares

def impares(x):
    x = cantidad - pares(x)
    return x
    
lista_1 = []
cantidad = int(input("Ingrese la cantidad de numeros que desea cargar en la lista: "))
while cantidad < 3:
    print("Error, debe ser mayor a 3.")
    cantidad = int(input("Ingrese un numero: "))
lista_1 = cargar_lista(lista_1)
print(f"La cantidad de numeros pares de la lista es {pares(lista_1)} y la cantidad de impares {impares(lista_1)}.")
