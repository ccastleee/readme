sumador = 0
contador = 0

print("Ingrese cuanto gasto en cada dia de sus vacaciones.")

for i in range(12):
    gasto = float(input(f"Dia {i+1}: "))
    sumador += gasto
    if gasto >= 57500:
        contador += 1

print(f"Cantidad total gastada: ${sumador}\nConsumio mas de $57.500 {contador} dias.")