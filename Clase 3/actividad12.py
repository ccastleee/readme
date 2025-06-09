num = int(input("Ingrese un numero: "))

if num % 5 == 0 and num % 9 == 0:
    print(f"{num} es divisible por 5 y 9.")
else:
    print(f"{num} no es divisle por 5 y 9.")