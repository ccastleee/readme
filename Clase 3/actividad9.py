print("Bienvenido a la montaña rusa!")

edad = int(input("Ingrese la edad: "))
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

if edad > 16 and peso < 120.5 and altura > 1.55 and altura < 2.15:
    print("Puede pasar!")
else:
    print("No puede pasar!")