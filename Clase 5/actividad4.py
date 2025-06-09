cantidad_notas = int(input("Ingrese la cantidad de notas que tuvo en Matematica Discreta: "))

sum_notas = 0

for i in range(cantidad_notas):
    notas = float(input("Ingrese la nota: "))
    sum_notas += notas

promedio_materia = sum_notas / cantidad_notas

print(f"El promedio de las notas es: {promedio_materia}")