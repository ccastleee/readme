sumador = 0

print("Ingrese la cantidad de litros cada dia de la semana: ")

for i in range(7):
    litros = float(input(f"Dia {i+1}: "))
    sumador += litros
print(f"La cantidad de litros consumidos en la semana son {sumador} litros.")

