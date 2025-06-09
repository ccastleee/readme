contador = 0

for i in range(10):
    notas = float(input("Ingrese las notas: "))
    if notas >= 6:
        contador += 1

print(contador)