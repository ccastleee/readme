"""Crear un algoritmo que solicite al usuario ingresar cuantos muebles quiere
comprar, posteriormente el tipo que quiere de cada uno (económico, común y
premium) y dependiendo que haya elegido ir mostrándolo por consola el tipo de
madera que lleva cada mueble escogido:
Muebles:
- Económico = pino.
- Común = abeto.
- Premium = roble.
Utilizar una lista para el tipo de madera."""

tipo_madera = ["Pino", "Abeto", "Roble"]

mensaje = """Tipos de Mueble
1-Económico
2-Común
3-Premium"""

cantidad = int(input("Ingrese la cantidad de muebles: "))

for i in range(cantidad):
    print(mensaje)
    tipo = int(input("Ingrese el tipo de mueble que desea: "))
    while tipo < 1 or tipo > 3:
        print("Error, elija una opcion correcta!")
        tipo = int(input("Ingrese el tipo de mueble que desea: "))
    if tipo == 1:
        print(f"Su mueble es de {tipo_madera[0]}.")
    elif tipo == 2:
        print(f"Su mueble es de {tipo_madera[1]}.")
    else:
        print(f"Su mueble es de {tipo_madera[2]}.")