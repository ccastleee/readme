num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
operacion = input("Ingrese el tipo de operacion: ")

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

if operacion == "suma":
    print(f"La suma es {suma}")
    if suma % 2 == 0:
        print(f"{suma} es par!")
    else:
        print(f"{suma} es impar!")
elif operacion == "resta":
    print(f"La resta es {resta}")
    if resta % 2 == 0:
        print(f"{resta} es par!")
    else:
        print(f"{resta} es impar!")
elif operacion == "multiplicacion":
    print(f"La multiplicacion es {multiplicacion}")
    if multiplicacion % 2 == 0:
        print(f"{multiplicacion} es par!")
    else:
        print(f"{multiplicacion} es impar!")
elif operacion == "division":
    print(f"La division es {division}")
    if division % 2 == 0:
        print(f"{division} es par!")
    else:
        print(f"{division} es impar!")