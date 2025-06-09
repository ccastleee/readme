comentario = """Alumno: Matias Castillo
DNI: 43.323.817"""

print(comentario)

menu_1 = 14449.99
menu_2 = 12000.00
menu_3 = 10999.99

suma = 0
cont_1 = 0
cont_2 = 0
cont_3 = 0
efectivo = 0
moneda_virtual = 0
pago_mas_usado = ""

cliente = int(input("Bienvenido, elija su menu (1, 2 o 3): "))

while cliente != 99:
    while cliente == 0 or cliente < 0 or cliente < 1 or cliente > 3:
        print("Error, ingrese un menu correcto!")
        cliente = int(input("Bienvenido, elija su menu (1, 2 o 3): "))
    cantidad = int(input("¿Cuanta cantidad desea?: "))
    if cliente == 1:
        cont_1 += 1
        suma += (menu_1*cantidad)
    elif cliente == 2:
        cont_2 += 1
        suma += (menu_2*cantidad)
    else:
        cont_3 += 1
        suma += (menu_3*cantidad)
    abono = input("¿Con que desea abonar? (EFECTIVO o MONEDA VIRTUAL): ").upper()
    while abono != "EFECTIVO" and abono != "MONEDA VIRTUAL":
        print("Error, ingrese un abono correcto!")
        abono = input("¿Con que desea abonar? (EFECTIVO o MONEDA VIRTUAL): ").upper()
    if abono == "EFECTIVO":
        efectivo += 1
    else:
        moneda_virtual += 1
    cliente = int(input("Bienvenido, elija su menu (1, 2 o 3): "))

if efectivo > moneda_virtual:
    pago_mas_usado = "Efectivo"
elif moneda_virtual > efectivo:
    pago_mas_usado = "Moneda virtual"
else:
    pago_mas_usado = "hubo la misma cantidad de abonos en cada uno."
        
promedio = suma/(cont_1 + cont_2 + cont_3)
promedio = round(promedio,2)
suma = round(suma,2)

print(f"Total recaudado: {suma}$")
print(f"El promedio total de ventas es: {promedio}$")
print(f"Cantida total de menus\nMenu 1: {cont_1}\nMenu 2: {cont_2}\nMenu 3: {cont_3}")
print(f"El medio de pago mas usado fue: {pago_mas_usado}")