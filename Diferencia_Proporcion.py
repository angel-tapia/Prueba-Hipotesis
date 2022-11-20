from Tablas import *
from Constantes import *
import math
import os
"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una diferencia de proporciones.
        Dentro de la funcion va a leer datos y va a llamar a la funcion prueba.
    </summary>
    <param name="x1">Numero de exitos en la muestra 1.</param>
    <param name="x2">Numero de exitos en la muestra 2.</param>
    <param name="n1">Numero de ensayos en la muestra 1.</param>
    <param name="n2">Numero de ensayos en la muestra 2.</param>
    <param name="alpha">Nivel de significacion.</param>
    <param name="Z">Valor del estadistico de prueba.</param>
"""
def menu_diferencia_proporcion():
    print("Elige la prueba de hipotesis a utilizar:")
    print("1.")
    print("H0. " + Stheta + "1 - " + Stheta + "2" + " = 0")
    print("H1. " + Stheta + "1 - " + Stheta + "2" + " < 0")
    print("2.")
    print("H0. " + Stheta + "1 - " + Stheta + "2" + " = 0")
    print("H1. " + Stheta + "1 - " + Stheta + "2" + " > 0")
    print("3.")
    print("H0. " + Stheta + "1 - " + Stheta + "2" + " = 0")
    print("H1. " + Stheta + "1 - " + Stheta + "2" + " != 0")
    opcion = input("Opcion: ")
    os.system("cls")

    if opcion not in ["1", "2", "3"]:
        print("Opcion incorrecta, vuelve a intentarlo.")
        print("Presiona una tecla para continuar...")
        os.system("pause")
        os.system("cls")
        menu_diferencia_proporcion()
        return

    print("Prueba de hipotesis de una diferencia de proporciones")
    print("H0. " + Stheta + "1 - " + Stheta + "2" + " = 0")
    print("H1. " + Stheta + "1 - " + Stheta + "2" + " " + ["<", ">", "!="][int(opcion) - 1] + " 0")
    print("")
    print("Introduce los datos:")
    x1 = float(input("x1: "))
    x2 = float(input("x2: "))
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    alpha = float(input(Salpha + ": "))
    alpha = 0.5 - alpha
    P = (x1 + x2) / (n1 + n2)
    Z = (x1 / n1 - x2 / n2) / math.sqrt(P * (1 - P) * (1 / n1 + 1 / n2))
    prueba(Z, alpha, opcion)
    os.system("cls")

"""
    <summary>
        Funcion que rechaza o no rechaza H0.
    </summary>
    <param name="Z">Valor de la prueba.</param>
    <param name="alpha">Valor de alpha.</param>
    <param name="opcion">Opcion de la prueba.</param>
"""
def prueba(Z, alpha, opcion):
    if opcion == "1":
        if Z < -buscarZ(alpha):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    elif opcion == "2":
        if Z > buscarZ(alpha):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    elif opcion == "3":
        if Z < -buscarZ(alpha/2) or Z > buscarZ(alpha/2):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    print("Presiona una tecla para continuar...")
    os.system("pause")
    os.system("cls")
    return

menu_diferencia_proporcion()