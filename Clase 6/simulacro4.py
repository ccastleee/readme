edad = int(input("Ingrese su edad: "))

while edad >= 0:
    if edad >= 0 and edad <= 5:
        print("Primera infancia.")
    elif edad >= 6 and edad <= 12:
        print("Infante.")
    elif edad >= 13 and edad <= 17:
        print("Adolescente.")
    elif edad >= 18 and edad <= 26:
        print("Joven.")
    elif edad >= 27 and edad <= 59:
        print("Adulto.")
    else:
        print("Adulto mayor.")
    edad = int(input("Ingrese su edad: "))

