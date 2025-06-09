min = 9999

for i in range(8):
    nom = input("Ingrese un nombre: ").title()
    if len(nom) < min:
        min = len(nom)
        corto = nom

print(f"El nombre mas corto es: {corto}, contando con {min} letras.")