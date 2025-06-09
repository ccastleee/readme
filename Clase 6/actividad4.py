suma = 0
contador = 0

luz = float(input("Ingrese el gasto: "))

while luz >= 0:
    suma += luz
    contador += 1
    luz = float(input("Ingrese el gasto: "))
if suma == 0:
    print("Usted no ingreso nada.")
else:
    promedio = suma/contador
    print(promedio) 
