print("Grupo 7")

dia = input("Es dia de semana?: ")

if dia == "si":
    print("Trabajo.")
else:
    domingo = input("Es domingo?: ")
    llueve = input("LLueve?: ")
    if domingo == "si" or llueve == "si":
        print("Voy al cine.")
    else:
        print("Salgo a bailar.")