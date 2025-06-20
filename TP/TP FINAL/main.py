import const, functions

print(f"                          ----------GRUPO 7----------\nIntegrantes: {const.grupo[0]}, {const.grupo[1]}, {const.grupo[2]}, {const.grupo[3]}, {const.grupo[4]}\n-----------------------------------------------------------------------------------------")
for i in range(3):
    datos_pasajero = []
    print(f"\nReserva numero: {i+1}\n")
    nombre, apellido, dni = functions.pasajero()
    datos_pasajero.append(nombre)
    datos_pasajero.append(apellido)
    datos_pasajero.append(dni)
    ferrocarril, fecha_salida = functions.seleccion_dia()
    datos_pasajero.append(ferrocarril)
    datos_pasajero.append(fecha_salida)
    destino, lugar_llegada = functions.seleccion_destino()
    datos_pasajero.append(destino)
    datos_pasajero.append(lugar_llegada)
    asiento, tipo_asiento = functions.seleccion_asiento()
    datos_pasajero.append(tipo_asiento)
    total = functions.total_pasaje(destino, asiento)
    total = round(total, 2)
    datos_pasajero.append(total)
    const.ganancias.append(total)
    print(f"\n----------DATOS----------\n\nNUMERO DE FERROCARRIL: {datos_pasajero[3]}\n\nFECHA Y HORA DE SALIDA: {datos_pasajero[4]}\n\nLUGAR DE SALIDA: {const.lugar_salida[0]}\n\nLUGAR DE LLEGADA: {datos_pasajero[6]}\n\nNOMBRE: {datos_pasajero[0]}\n\nAPELLIDO: {datos_pasajero[1]}\n\nDNI: {datos_pasajero[2]}\n\nNUMERO DE RESERVA: {i+1}\n\nTIPO DE ASIENTO: {datos_pasajero[7]}\n\nTOTAL A PAGAR: {total}$\n")
mayor, indice_mayor = functions.mayor_ganancia_indice(const.ganancias)
print(f"Lista de ganancias\n{const.ganancias}\n")
functions.ordernar_reserva_matriz(const.ganancias)
print(f"\nLa reserva {indice_mayor+1} es la mas alta con {mayor}$.\n")
print(f"Total recaudado: {functions.total_recaudado(const.ganancias)}$.")
