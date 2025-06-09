def mayor_menor_edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Usted es mayor de edad.")
    else:
        print("Usted es menor de edad.")

for i in range(4):
    mayor_menor_edad()