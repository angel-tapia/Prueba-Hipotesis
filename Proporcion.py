from Tablas import *
from Constantes import *
import math
import os

"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una proporcion.
    <param name="x">Numero de exitos en la muestra.</param>
    <param name="n">Numero de ensayos en la muestra.</param>
    <param name="alpha">Nivel de significancia.</param>
    <param name="Z">Valor del estadistico de prueba.</param>
"""
def menu_proporcion():
    print("Elige la prueba de hipotesis a utilizar:")
    print("1)")
    print("H0. " + Stheta + " = " + Stheta + "0")
    print("H1. " + Stheta + " > " + Stheta + "0")
    print("2)")
    print("H0. " + Stheta + " = " + Stheta + "0")
    print("H1. " + Stheta + " < " + Stheta + "0")
    print("3)")
    print("H0. " + Stheta + " = " + Stheta + "0")
    print("H1. " + Stheta + " != " + Stheta + "0")
    opcion = input("Opcion: ")
    os.system("cls")

    if opcion not in ["1", "2", "3"]:
        print("Opcion incorrecta, vuelve a intentarlo.")
        print("Presiona una tecla para continuar...")
        os.system("pause")
        os.system("cls")
        menu_proporcion()
        return

    print("Prueba de hipotesis de proporciones")
    print("H0. " + Stheta + " = " + Stheta + "0")
    print("H1. " + Stheta + [">", "<", "!="][int(opcion) - 1] + Stheta + "0")
    print("")
    print("Introduce los datos:")
    theta = float(input(Stheta+"0: "))
    x = float(input("x: "))
    n = int(input("n: "))
    alpha = float(input(Salpha + ": "))
    Z = (x - n*theta) / math.sqrt(n*theta*(1-theta))
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
        if Z > buscarZ(0.5-alpha):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    elif opcion == "2":
        if Z < -buscarZ(0.5-alpha):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    elif opcion == "3":
        if Z < -buscarZ(0.5-alpha/2) or Z > buscarZ(0.5-alpha/2):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    print("Presiona una tecla para continuar...")
    os.system("pause")
    os.system("cls")
    return

menu_proporcion()