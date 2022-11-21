from Tablas import *
from Constantes import *
import math
import os
"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una diferencia de medias.
    </summary>
"""
from Tablas import *
from Constantes import *
import math
import os
"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una diferencia de medias.
    </summary>
"""
def menu_diferencia_medias():
    print("Elige la prueba de hipotesis a utilizar:")
    print("1.")
    print("H0. " + '\u03BC' + "1 - " + '\u03BC' + "2" + " = 0")
    print("H1. " + '\u03BC' + "1 - " + '\u03BC' + "2" + " < 0")
    print("2.")
    print("H0. " + '\u03BC' + "1 - " + '\u03BC' + "2" + " = 0")
    print("H1. " + '\u03BC' + "1 - " + '\u03BC' + "2" + " > 0")
    print("3.")
    print("H0. " + '\u03BC' + "1 - " + '\u03BC' + "2" + " = 0")
    print("H1. " + '\u03BC' + "1 - " + '\u03BC' + "2" + " != 0")
    opcion = input("Opcion: ")
    os.system("cls")

    if opcion not in ["1", "2", "3"]:
        print("Opcion incorrecta, vuelve a intentarlo.")
        print("Presiona una tecla para continuar...")
        os.system("pause")
        os.system("cls")
        menu_diferencia_medias()
        return
    
    print("Prueba de hipotesis de una diferencia de medias")
    print("H0. " + '\u03BC' + "1 - " + '\u03BC' + "2" + " = 0")
    print("H1. " + '\u03BC' + "1 - " + '\u03BC' + "2" + " " + ["<", ">", "!="][int(opcion) - 1] + " 0")
    print("")
    print("Introduce los datos:")
    x_bar1 = float(input("x1: "))
    x_bar2 = float(input("x2: "))
    delta = float(input('\u0394' + ": "))
    zigma1 = float(input('\u03C3' + "1: "))
    zigma2 = float(input('\u03C3' + "2: "))
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    alpha = float(input(Salpha + ": "))
    alpha = 0.5 - alpha
    z = (x_bar1 - x_bar2 - delta) / (math.sqrt((zigma1/n1) + (zigma2/n2)))
    prueba(z, alpha, opcion)
    os.system("cls")

def prueba(z, alpha, opcion):
    if opcion == "1":
        if z < -buscarZ(alpha):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    elif opcion == "2":
        if z > buscarZ(alpha):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    elif opcion == "3":
        if z < -buscarZ(alpha/2) or z > buscarZ(alpha/2):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    print("Presiona una tecla para continuar...")
    os.system("pause")
    os.system("cls")
    return

menu_diferencia_medias()
