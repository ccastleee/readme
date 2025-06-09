p = input("Desea ingresar un numero?: ").upper()

cont_1 = 0
cont_2 = 0
while p == "SI":
    cont_1 += 1
    n = float(input("Ingrese un numero: "))
    if n > 15:
        cont_2 += 1
    p = input("Desea ingresar un numero?: ").upper()

porcentaje = (cont_2 * 100)/cont_1
print(f"El porcentaje de numeros mayores a 15 ingresados es: {porcentaje}")