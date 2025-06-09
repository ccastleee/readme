print("GRUPO 7 - PASAJE TREN A MDQ")

dia_1 = "Miercoles"

dia_2 = "Jueves"

dia_3 = "Viernes"

hora_salida= "9:00 AM"

dolores = 5500

mdq = 8500

lugar_salida = "Plaza Constitución"

lugar_llegada = ""

lugar_llegada_dolores = "Dolores"

lugar_llegada_mdq = "Estación Mar del Plata"

asiento_semi_cama = 2500

ferrocarril = ""

ferrocarril_1 = "F234"

ferrocarril_2 = "F543"

ferrocarril_3 = "F045"

fecha_salida = ""

fecha_salida_1 = "07/05/2025"

fecha_salida_2 = "08/05/2025"

fecha_salida_3 = "09/05/2025"

tipo_asiento = ""

tipo_semi_cama = "Semi-cama"

tipo_simple = "Simple"


for i in range(3):

    total = 0

    print(f"\nReserva numero: {i+1}\n")

    nombre = input("\nIngrese su nombre: ").title()

    apellido = input("\nIngrese su apellido: ").title()

    dni = int(input("\nIngrese su DNI (sin puntos): "))

    print(f"\nIngrese que dia desea elegir:\n\n1.{dia_1} {hora_salida}\n\n2.{dia_2} {hora_salida}\n\n3.{dia_3} {hora_salida}\n")

    dia = int(input("Elija una opcion (1, 2 o 3): "))

    while dia < 1 or dia > 3:
        print("Error, ingrese un dia correcto.")
        dia = int(input("Ingrese que dia desea elegir (1, 2 o 3): "))
    if dia == 1:
        ferrocarril = ferrocarril_1
        fecha_salida = fecha_salida_1
    elif dia == 2:
        ferrocarril = ferrocarril_2
        fecha_salida = fecha_salida_2
    else:
        ferrocarril = ferrocarril_3
        fecha_salida = fecha_salida_3

    print("\nElija donde desea ir:\n\n1.Dolores\n\n2.Mar del Plata\n")

    destino = int(input("Elija una opcion (1 o 2): "))

    while destino < 1 or destino > 2:
        print("Error, ingrese un destino correcto.")
        destino = int(input("Elija una opcion (1 o 2): "))
    if destino == 1:
        total += dolores
        lugar_llegada = lugar_llegada_dolores
    else:
        total += mdq
        lugar_llegada = lugar_llegada_mdq

    print("\nEliga el tipo de asiento:\n\n1.Asiento simple (sin precio adicional)\n\n2.Asiento semi-cama (+$2500)\n")

    asiento = int(input("Elija una opcion (1 o 2): "))

    while asiento < 1 or asiento > 2:
        print("Error, elija el asiento correctamente.")
        asiento = int(input("Elija su opcion (1 o 2): "))
    if asiento == 1:
        tipo_asiento = tipo_simple
    else:
        total += asiento_semi_cama
        tipo_asiento = tipo_semi_cama
    
    print(f"\nDATOS\n\nNUMERO DE FERROCARRIL: {ferrocarril}\n\nFECHA DE SALIDA: {fecha_salida}\n\nHORA DE SALIDA: {hora_salida}\n\nLUGAR DE SALIDA: {lugar_salida}\n\nLUGAR DE LLEGADA: {lugar_llegada}\n\nNOMBRE: {nombre}\n\nAPELLIDO: {apellido}\n\nDNI: {dni}\n\nNUMERO DE RESERVA: {i+1}\n\nTIPO DE ASIENTO: {tipo_asiento}\n\nTOTAL A PAGAR: {total}\n")