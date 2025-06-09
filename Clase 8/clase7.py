"""nombre largo"""

max = -9999

for i in range(5):
    nombre = input("Ingrese un nombre: ").title()
    cant = len(nombre)
    if cant > max:
        max = cant
        largo = nombre

print(f"El nombre mas largo es: {largo} contando con {max}")

"""funciones"""

def mi_primera_funcion():
    print("Mi primera funcion")

for i in range(4):
    mi_primera_funcion()

def saludar():
    nombre = input("Ingrese su nombre: ").title()
    print(f"Buenos dias, {nombre}!")

saludar()

def nombre_apellido(a, b):
    print(f"Soy {a} {b}!")

nombre_apellido("Matias","Castillo")
