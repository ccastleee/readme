print("Ingrese la temperatura que hizo en julio 2024")

suma = 0
for i in range(30):
    temp = float(input("Ingrese: "))
    while temp < -6 or temp > 6:
        print("ERROR!")
        temp = float(input("Ingrese: "))
    suma += temp

promedio = suma/30

print(promedio)