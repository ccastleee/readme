mensaje = """INGRESE LOS SIGUIENTES DATOS PARA PODER CONTINUAR: 

NOMBRE: Juan Manuel 

APELLIDO: Valerio ferrante 

DOMICILIO: LIMA 757 CABA 

ESTADO CIVIL: casado""" 

print(mensaje) 

nombre = input("Ingrese su nombre: ") 

nombre = nombre.title()

apellido = input("Ingrese su apellido: ") 

apellido = apellido.capitalize()

domicilio = input("Ingrese su domicilio: ")

domicilio = domicilio.upper()

estado_civil = input("Ingrese su estado civil: ") 

estado_civil = estado_civil.lower()

if nombre == "Juan Manuel" and apellido == "Valerio ferrante" and domicilio == "LIMA 757 CABA" and estado_civil == "casado": 

    print("CORRECTO") 

else: 

    print("ERROR") 