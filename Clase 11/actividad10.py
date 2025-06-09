def promedio_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    promedio = suma/len(lista)
    promedio = round(promedio, 1)
    print(f"El promedio de la lista es de {promedio}.")

def porcentaje_lista(lista):
    cont_par = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            cont_par += 1
    porcentaje = (cont_par*100)/len(lista)
    porcentaje = round(porcentaje, 1)
    print(f"El porcentaje de numeros pares de la lista es del {porcentaje}%")

def numero_mas_alto(lista):
    maximo = -9999
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    print(f"El numeros mas alto de la lista es el {maximo}.")

num_1 = [12, 15, 18, 3, 9]
num_2 = [5, 10, 8]
num_3 = [99, 13, 1, 17, 12, 23, 70, 6]

print("----------------------------------------")
print("----------------------------------------")
print("\nLISTA 1\n")
promedio_lista(num_1)
porcentaje_lista(num_1)
numero_mas_alto(num_1)
print("----------------------------------------")
print("----------------------------------------")
print("\nLISTA 2\n")
promedio_lista(num_2)
porcentaje_lista(num_2)
numero_mas_alto(num_2)
print("----------------------------------------")
print("----------------------------------------")
print("\nLISTA 3\n")
promedio_lista(num_3)
porcentaje_lista(num_3)
numero_mas_alto(num_3)
print("----------------------------------------")
print("----------------------------------------")