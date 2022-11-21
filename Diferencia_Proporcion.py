from Tablas import *
from Constantes import *
import math
import os
"""
    <summary>
        Función menú que realiza la prueba de hipótesis de una diferencia de proporciones.
        Dentro de la función va a leer datos y va a llamar a la función prueba.
    </summary>
    <param name="x1">Número de exitos en la muestra 1.</param>
    <param name="x2">Número de exitos en la muestra 2.</param>
    <param name="n1">Número de ensayos en la muestra 1.</param>
    <param name="n2">Número de ensayos en la muestra 2.</param>
    <param name="alpha">Nivel de significación.</param>
    <param name="Z">Valor del estadístico de prueba.</param>
"""
def menu_diferencia_proporcion():
    print("Elige la prueba de hipótesis a utilizar:")
    print("1.")
    print("H0. " + Stheta + "1 - " + Stheta + "2" + " = 0")
    print("H1. " + Stheta + "1 - " + Stheta + "2" + " < 0")
    print("2.")
    print("H0. " + Stheta + "1 - " + Stheta + "2" + " = 0")
    print("H1. " + Stheta + "1 - " + Stheta + "2" + " > 0")
    print("3.")
    print("H0. " + Stheta + "1 - " + Stheta + "2" + " = 0")
    print("H1. " + Stheta + "1 - " + Stheta + "2" + " != 0")
    opcion = input("Opción: ")
    os.system("cls")

    if opcion not in ["1", "2", "3"]:
        print("Opción incorrecta, vuelve a intentarlo.")
        print("Presiona una tecla para continuar...")
        os.system("pause")
        os.system("cls")
        menu_diferencia_proporcion()
        return

    print("Prueba de hipótesis de una diferencia de proporciones")
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
        Función que rechaza o no rechaza H0.
    </summary>
    <param name="Z">Valor del estadístico de prueba.</param>
    <param name="alpha">Valor de alpha.</param>
    <param name="opcion">Opción de la prueba.</param>
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
    os.system("pause")
    os.system("cls")
    return

menu_diferencia_proporcion()