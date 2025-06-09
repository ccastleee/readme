"""FOR"""

for i in range(1, 6, 1):
    print("Buenas tardes!")


"""Ingresar las variables rango"""

n1 = int(input("ingrese el valor de inicio: "))

n2 = int(input("Ingrese hasta: "))
n3 = int(input("Ingrese el incremento: "))

for i in range(n1, n2, n3):
    print(i)

"""Contador"""

contador = 0

for i in range(5):
    contador += 1
    print(contador)
print(contador)

"""Sumador"""

sumador = 0

for i in range(5):
    sumador += 4
print(sumador)


num = float(input("Ingrese el nro que quiere ir sumando: "))

sumando = 0

for i in range(5):
    sumando += num
print(sumando)