def cargar_lista(lista):
    for i in range(6):
        n = int(input("Ingrese un numero: "))
        while n < 50 or n > 250:
            print("Error.")
            n = int(input("Ingrese un numero: "))
        lista.append(n)
    return lista

def maximo_minimo(lista):
    maximo = -9999
    minimo = 9999
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
        if lista[i] < minimo:
            minimo = lista[i] 
    print(f"El maximo es: {maximo}")
    print(f"El minimo es: {minimo}")

lista_1 = []
lista_1 = cargar_lista(lista_1)
maximo_minimo(lista_1)