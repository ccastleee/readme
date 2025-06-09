cont_pos = 0
cont_neg = 0
cont_cero = 0

print("Ingrese 10 numero")

for i in range(10):
    n = int(input("Ingrese un numero: "))
    if cont_pos > 0:
        cont_pos += 1
    elif cont_neg < 0:
        cont_neg += 1
    else:
        cont_cero += 1

print(f"Cantidad de numeros positivos: {cont_pos}, cantidad de numeros negativos: {cont_neg}, cantidad de ceros: {cont_cero}")