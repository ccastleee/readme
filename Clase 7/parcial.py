comentario = """Alumno: Matias Castillo
DNI: 43.323.817"""

print(comentario)

menu_1 = 14449.99
menu_2 = 12000.00
menu_3 = 10999.99

cliente = int(input("Bienvenido, elija su menu (1, 2 o 3): "))
cantidad = int(input("¿Cuanta cantidad desea?: "))
abono = input("¿Con que desea abonar? (EFECTIVO o MONEDA VIRTUAL): ").lower()

suma = 0
cont_1 = 0
cont_2 = 0
cont_3 = 0
efectivo = 0
moneda_virtual = 0

while cliente != 99:
    if cliente == 0 or cliente < 0 or cliente < 1 or cliente > 3:
        print("Error, ingrese un menu correcto!")
    elif abono != "efectivo" or abono != "moneda virtual":
        print("Abono incorrecto.")
    elif cliente == 1:
        cont_1 += 1
        suma += (menu_1*cantidad)
    elif cliente == 2:
        cont_2 += 1
        suma += (menu_2*cantidad)
    elif cliente == 3:
        cont_3 += 1
        suma += (menu_3*cantidad)
    elif abono == "EFECTIVO":
        efectivo += 1
    elif abono == "MONEDA VIRTUAL":
        moneda_virtual += 1
    cliente = int(input("Bienvenido, elija su menu (1, 2 o 3): "))
    cantidad = int(input("¿Cuanta cantidad desea?: "))
    abono = input("¿Con que desea abonar? (EFECTIVO o MONEDA VIRTUAL): ").lower()

pago_mas_usado = ""

if efectivo > moneda_virtual:
    pago_mas_usado = "Efectivo"
elif moneda_virtual > efectivo:
    pago_mas_usado = "Moneda virtual"
else:
    pago_mas_usado = "Hubo la misma cantidad de abono en cada uno"
        
promedio = suma/(cont_1 + cont_2 + cont_3)

print(f"Total recaudado: {suma}$")
print(f"El promedio total de ventas es: {promedio}")
print(f"Cantida total de menus\nMenu 1: {cont_1}\nMenu 2: {cont_2}\nMenu 3: {cont_3}")
print(f"El medio de pago mas usado fue: {pago_mas_usado}")