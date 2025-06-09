minimo = 9999

maximo = -9999

for i in range(10):
    n = int(input("Ingrese un numero: "))
    if n < minimo:
        minimo = n
    if n > maximo:
        maximo = n

print(f"El numero mas bajo es {minimo} y el numero mas alto es {maximo}.")