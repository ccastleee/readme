def mostrar_divisibles(lista):
    for i in range(len(lista)):
        if lista[i] % 9 == 0:
            print(lista[i])

numeros = [90, -33, 27, -12, 36, 7, -9]
mostrar_divisibles(numeros)