n = int(input("Ingrese numeros: "))

cont_1 = 0
cont_2 = 0

while n % 9 != 0:
    if n % 2 == 0:
        cont_1 += 1
    else:
        cont_2 += 1
    n = int(input("Ingrese numeros: "))

print(f"La cantidad de numeros pares ingresados es: {cont_1}\nLa cantidad de numeros impares ingresados es: {cont_2}")