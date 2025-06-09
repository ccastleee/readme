"""Crear una lista vacía e ir ingresando en esa lista el nombre de cada uno de los
integrantes del grupo mediante el método append() Ir mostrando tambien cada
uno de los nombres ingresados por consola mientras se vayan ingresando.
Finalmente mostrar el nombre del grupo y la totalidad de los integrantes.
Ejemplo:
Maria
Belén
Roberto
Norma
Grupo N° 3:
[Maria, Belén, Roberto, Norma]
Pista: Crear un bucle for dependiendo la cantidad de integrantes del grupo."""

grupo = []

for i in range(5):
    integrante = input(f"Ingrese el integrante N°{i+1}: ").capitalize()
    print(integrante)
    grupo.append(integrante)

print("Grupo N°7")
print(grupo)