import random

n = random.randint(1,100)
intentos = 1
while n % 5 != 0:
    print("Error.")
    intentos += 1
    n = random.randint(1,100)

if intentos == 1:
    print(f"El numero es {n} y solo hubo 1 intento!")
else:
    print(f"El numero es {n} y la cantidad de intentos fue de {intentos} veces!")