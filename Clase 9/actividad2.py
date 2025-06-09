"""Crear una lista de 7 sabores de helado, posteriormente solicitar al cliente que
elija dos sabores para crear su cono de dos bochas.
Si el cliente elije un gusto que no existe, o un numero incorrecto a la selección
de sabores, volver a pedirle el gusto hasta que elija uno existente.
Imprimir el resultado final de la siguiente forma: Cono de halado de {gusto_1} y
{gusto_2}"""

saboresHelados = ["Frutilla", "Crema del cielo", "Dulce de leche", "Vainilla", "Tramontana", "Banana split", "Marroc"]

print("---Sabores de Helado---\n")
print(f"1-{saboresHelados[0]}\n"
      f"2-{saboresHelados[1]}\n"
      f"3-{saboresHelados[2]}\n"
      f"4-{saboresHelados[3]}\n"
      f"5-{saboresHelados[4]}\n"
      f"6-{saboresHelados[5]}\n"
      f"7-{saboresHelados[6]}\n")

gusto_1 = int(input(("Elija un sabor: ")))

while gusto_1 < 1 or gusto_1 > 7:
    print("Elija un sabor correcto.\n")
    gusto_1 = int(input(("Elija un sabor: ")))

gusto_2 = int(input(("Elija otro sabor: ")))

while gusto_1 < 1 or gusto_1 > 7:
    print("Elija un sabor correcto.")
    gusto_2 = int(input(("Elija otro sabor: ")))

print(f"Cono de helado de {saboresHelados[gusto_1-1]} y {saboresHelados[gusto_2-1]}")