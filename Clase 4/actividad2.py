edad = int(input("Ingrese su edad: "))

if edad < 0 or edad >= 110:
    print("Error.")
elif edad >= 18 and edad <= 55:
    print("$20.000 - No aplica descuento.")
else:
    print("$13.500 - Aplica descuento")