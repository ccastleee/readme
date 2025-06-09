import random

def cargar_lista(lista):
    for i in range(4):
        n = random.randint(2,10)
        lista.append(n)
    return lista

def promedio(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    promedio = sum/len(x)
    print(promedio)

def nota_alta(y):
    mayor = -9999
    for i in range(len(y)):
        if y[i] > mayor:
            mayor = y[i]
    print(mayor)

notas_1 = []
notas_2 = []
notas_3 = []
notas_1 = cargar_lista(notas_1)
notas_2 = cargar_lista(notas_2)
notas_3 = cargar_lista(notas_3)
print(notas_1)
print(notas_2)
print(notas_3)
promedio(notas_1)
promedio(notas_2)
promedio(notas_3)
nota_alta(notas_1)
nota_alta(notas_2)
nota_alta(notas_3)