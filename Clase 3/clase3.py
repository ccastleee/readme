"""positivo o negativo"""

numero = int(input("Ingrese un numero: "))

if numero > 0:
    print(f"{numero} es positivo.")
elif numero < 0:
    print(f"{numero} es negativo.")
else:
    print("Es cero.")
    print("Fin.")

print(2%2)
print(9%2)
print(8%2)
print(16%2)
print(13%2)

"""divisible por 7"""

num = int(input("Ingrese un numero: "))

if num % 7 == 0:
    print(f"{num} es divisible por 7")
else:
    print(f"{num} no es divisible por 7")

"""estructura iterativa for"""

print("el piso esta sucio")
print("barro")
for i in range(15):
    print("trapeo")
print("el piso esta limpio")

"""tabla del 1"""

for i in range(1,11):
    print(i)

"""bucle for"""

print("Se pueden anotar 3 alumnos a la clase.")

for i in range(3):
    nombre = input("Ingrese su nombre: ")
    print(f"{nombre} se inscribio!")
print("FIN.")