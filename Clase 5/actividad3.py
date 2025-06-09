integrantes = int(input("Ingrese la cantidad de integrantes del grupo: "))
cont_caba = 0
cont_conur = 0

for i in range(5):
    lugar = input("Donde reside?: ")
    if lugar == "caba":
        cont_caba += 1
    elif lugar == "conurbano":
        cont_conur += 1

porcentaje_caba = (cont_caba * 100) / integrantes
porcentaje_conurbano = (cont_conur * 100) / integrantes
print(f"Porcentaje del grupo que viven en CABA: {porcentaje_caba}%")
print(f"Porcentaje del grupo que vive en el Conurbano: {porcentaje_conurbano}%")