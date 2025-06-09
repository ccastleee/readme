nombre = input("Ingrese un nombre: ").title()

while len(nombre) < 3 or len(nombre) > 15:
    print("Ingrese otro nombre: ")
    nombre = input("Ingrese un nombre: ").title()

print("Ingreso exitoso.")