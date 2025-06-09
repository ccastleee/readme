cont_play = 0
cont_xbox = 0
cont_pc = 0
cont_nintendo = 0

for i in range(50):
    usuarios = input("Ingrese en que plataforma juega (PLAYSTATION, XBOX, PC O NINTENDO): ").upper()
    if usuarios == "PLAYSTATION":
        cont_play += 1
    elif usuarios == "XBOX":
        cont_xbox += 1
    elif usuarios == "PC":
        cont_pc += 1
    elif usuarios == "NINTENDO":
        cont_nintendo += 1

porcentaje_xbox = (cont_xbox*100)/50
porcentaje_pc = (cont_pc*100)/50

print(f"PLAYSTATION: {cont_play} XBOX: {cont_xbox} PC: {cont_pc} NINTENDO: {cont_nintendo}")
print(f"El promedio de jugadores de xbox es: {porcentaje_xbox} y de pc: {porcentaje_pc}")