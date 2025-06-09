diametro = float(input("Ingrese el diametro del circulo: "))


while diametro < 0 or diametro == 0:
    print("Error, ingrese el diametro correcto.")
    diametro = float(input("Ingrese el diametro del circulo: "))

radio = diametro/2
area_circulo = 3.14*(radio*radio)

print(f"El area del circulo de diametro {diametro} es: {area_circulo}")