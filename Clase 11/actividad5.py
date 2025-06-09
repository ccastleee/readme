def cargar_lista(lista):
    for i in range(6*2):
        n = int(input("Ingrese un numero: "))
        lista.append(n)
    return lista

def porcentaje_pos_neg(lista):
    cont_pos = 0
    cont_neg = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            cont_pos += 1
        else:
            cont_neg += 1
    porcentaje_pos = (cont_pos*100)/len(lista)
    porcentaje_neg = (cont_neg*100)/len(lista)
    porcentaje_pos = round(porcentaje_pos, 2)
    porcentaje_neg = round(porcentaje_neg, 2)
    print(f"El porcentaje de numeros positivos es el {porcentaje_pos}%\n"
          f"El porcentaje de numeros negativos es el {porcentaje_neg}%")

lista_1 = []
lista_1 = cargar_lista(lista_1)
porcentaje_pos_neg(lista_1)