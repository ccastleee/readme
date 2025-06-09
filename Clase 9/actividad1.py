"""- Crear una lista llamada razasDePerros vacía e imprimirla.
- Luego volver a inicializarla, pero con los siguientes elementos:
o Bulldog
o Pitbull
o Chihuahua
o Golden
o Dalmata
- Imprimir la lista actualizada
- Modificar el elemento “Chihuahua” por “Ovejero Aleman”
- Imprimir la lista actualizada
- Imprimir la lista desde “Pitbull” hasta “Golden” inclusive."""

razasDePerros = [] 

print(razasDePerros)

razasDePerros.append("Bulldog")
razasDePerros.append("Pitbull")
razasDePerros.append("Chihuahua")
razasDePerros.append("Golden")
razasDePerros.append("Dalmata")

print(razasDePerros)

razasDePerros[2] = "Ovejero Aleman"

print(razasDePerros)

print(razasDePerros[1:4])