pass_1 = "ALGORITMIA2025"

user = input("Ingrese su usuario: ")

password = input("Ingrese su contrasena: ")

password = password.upper()

while password != pass_1:
    print("Error, contrasena no valida.")
    password = input("Ingrese su contrasena: ")

print(f"Bienvenido {user}!")