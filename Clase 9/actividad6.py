"""Crear una lista vacía de nombre numeros.
Solicitar al usuario que ingrese tres números decimales en tres variables de
nombres: 'a', 'b' y 'c'.
Añadir estos tres valores a la lista ya creada.
Posteriormente guardar en una variable 'e' la siguiente ecuación:
e = (a*55 / b) + c-2
Agregar el valor de 'e' a la lista numeros.
Imprimir la lista."""

numeros = []

a = float(input("Ingrese un numero decimal: "))

numeros.append(a)

b = float(input("Ingrese otro numero decimal: "))

numeros.append(b)

c = float(input("Ingrese otro numero decimal: "))

numeros.append(c)

e = (a*55 / b) + c-2

numeros.append(e)

print(numeros)
