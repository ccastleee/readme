print("Ingrese numeros entre el 2 y el 8")

n = int(input("Ingrese un numero: "))

suma = 0
cont = 0

while n != 99:
    while n < 2 or n > 8:
        print("ERROR!")
        n = int(input("Ingrese un numero: "))
    suma += n
    cont += 1
    n = int(input("Ingrese un numero: "))


print(f"La suma de los numeros ingresados entre el 2 y el 8 es: {suma} y la cantidad de numeros ingresado entre ese rango es: {cont}")