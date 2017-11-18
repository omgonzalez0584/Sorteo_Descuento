import random

def aplicar_descuento(total_compras):
    digitos = (1,2,3,4,5)
    bola = random.choice(digitos)
    if bola == 1:
        print("Aleatoriamente obtuvo la bola Blanca")
        print("Lo siento....! no tiene descuento en su compra")
    elif bola == 2:
        desc = float(total_compras) * 0.10
        nuevo_total = float(total_compras) - desc
        print("Aleatoriamente usted obtuvo la Bola Roja ")
        print("Felicidades!!, se ha ganado un 10% de descuento!")
        print("Su nuevo total a pagar es", nuevo_total)
    elif bola == 3:
        desc = float(total_compras) * 0.20
        nuevo_total = float(total_compras) - desc
        print("Aleatoriamente usted obtuvo la bola Azul ")
        print("Felicidades!!, se ha ganado un 20% de descuento!")
        print("Su nuevo total a pagar es", nuevo_total)
    elif bola == 4:
        desc = float(total_compras) * 0.25
        nuevo_total = float(total_compras) - desc
        print("Aleatoriamente usted obtuvo la bola Verde ")
        print("Felicidades!!, se ha ganado un 25% de descuento!")
        print("Su nuevo total a pagar es", nuevo_total)
    else:
        desc = float(total_compras) * 0.50
        nuevo_total = float(total_compras) - desc
        print("Aleatoriamente usted obtuvo la bola Amarilla ")
        print("Felicidades!!, se ha ganado un 50% de descuento!")
        print("Su nuevo total a pagar es", nuevo_total)


def main():
    while True:
        total_compras = input("introduzca el total de las compras(Presione * si desea salir): ")
        if total_compras == '*':
            print("Adios")
            break
        elif int(total_compras) > 100:
            print("\t\tSu compra es Mayor a 100 aplica para nuestros sorteo")
            print("\t\t\t\tBola Blanca ---> No tiene Descuento")
            print("\t\t\t\tBola Roja ---> 10% de Descuento")
            print("\t\t\t\tBola Azul ---> 20% de Descuento")
            print("\t\t\t\tBola Verde ---> 25% de Descuento")
            print("\t\t\t\tBola Amarilla ---> 50% de Descuento")
            aplicar_descuento(total_compras)
        else:
            print("Lo sentimos sus compras son menores a 100.....No aplica para nuestro sorteo")

main()




