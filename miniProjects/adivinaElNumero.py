import random


def adivina_el_numero(x):

    print("================================================")
    print("Bienvenido(a) al Juego!")
    print("================================================")
    print("Tu meta es adivinar el número generado por la computadora.")

    numero_aleatorio = random.randint(1, x)

    prediccion = 0 # Así nunca va a coincidir con el número_aleatorio

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un número entre 1 y {x}: ")) #f-string

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. El número es mayor...")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. El número es menor...")

    print(f"Coorrrectouu! Advinaste el número {numero_aleatorio}!")


adivina_el_numero(10) #falta parchear el caso en que se ingresa un string en vez de un int