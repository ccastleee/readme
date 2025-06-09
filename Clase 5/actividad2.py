print("Ingrese 10 numeros")

sumador = 0

for i in range(10):
    n = int(input("Ingrese un numero: "))
    if n > 8 and n < 15:
        sumador += n

print(f"La suma de numeros mayores a 8 y menores a 15 es: {sumador}")