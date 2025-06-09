print("ingrese valor entre 2 y 8")
n = int(input("ingrese: "))
cont = 0
suma = 0
while n!=99:
    while n<2 or n>8:
        print("error")
        n = int(input("ingrese: "))
    suma = suma+n
    cont = cont+1
    n = int(input("ingrese: "))
print(f"suma: {suma} e")