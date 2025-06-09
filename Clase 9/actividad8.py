"""Calcular el IVA de un producto cuyo valor sea ingresado por teclado por el
usuario. El cálculo será realizado con una función que recibirá el valor del
producto como argumento al momento de llamar la función y deberá utilizar la
palabra reservada return a fin de devolver el resultado.
El IVA será del 21%.
Mostrar el resultado por consola."""

def calculo_iva(a):
    iva_producto = a * 0.21
    return iva_producto

producto = float(input("Ingrese el precio del producto: "))

print(f"El iva es de: ${round(calculo_iva(producto),2)}")