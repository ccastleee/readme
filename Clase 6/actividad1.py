animales = input("Ingrese nombres de animales: ").upper()

cont_animales = 1

while animales != "TIGRE":
    animales = input("Ingrese nombres de animales: ").upper()
    cont_animales += 1

print(f"Cantidad de animales ingresados: {cont_animales}")