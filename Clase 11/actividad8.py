import random

def cargar_lista(lista):
    for i in range(14):
        n = random.randint(1,50)
        while n % 9 == 0:
            n = random.randint(1,50)
        lista.append(n)
    return lista

lista_1 = []
lista_1 = cargar_lista(lista_1)
print(lista_1)