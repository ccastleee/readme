print("Ingrese un numero que este entre 18 y 55.")

n = int(input("Ingrese un numero: "))

while n < 18 or n > 55:
    print("Error, ingrese un numero entre 18 y 55.")
    n = int(input("Ingrese un numero: "))

print(f"El numero {n} esta entre 18 y 55.")