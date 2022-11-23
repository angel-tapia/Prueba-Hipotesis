from Tablas import *
from Constantes import *
import math
import os

"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una proporcion.
    </summary>
    <param name="x">Numero de exitos en la muestra.</param>
    <param name="n">Numero de ensayos en la muestra.</param>
    <param name="alpha">Nivel de significancia.</param>
    <param name="z">Valor del estadistico de prueba.</param>
"""
def menu_proporcion():
    print("Elige la prueba de hipotesis a utilizar:")
    print("1.")
    print("H0. " + Stheta + " = " + Stheta + "0")
    print("H1. " + Stheta + " > " + Stheta + "0")
    print("2.")
    print("H0. " + Stheta + " = " + Stheta + "0")
    print("H1. " + Stheta + " < " + Stheta + "0")
    print("3.")
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
    if opcion=="3":
        alpha = 0.5 - alpha/2
    else:
        alpha = 0.5 - alpha
    z = (x - n*theta) / math.sqrt(n*theta*(1-theta))
    print("z = " + str(z))
    prueba(z, alpha, opcion)
    os.system("cls")

"""
    <summary>
        Funcion que rechaza o no rechaza H0.
    </summary>
    <param name="z">Valor de la prueba.</param>
    <param name="alpha">Valor de alpha.</param>
    <param name="opcion">Opcion de la prueba.</param>
"""
def prueba(z, alpha, opcion):
    if opcion == "1":
        if z > buscarZ(alpha):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    elif opcion == "2":
        if z < -buscarZ(alpha):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    elif opcion == "3":
        if z < -buscarZ(alpha) or z > buscarZ(alpha):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    print("Presiona una tecla para continuar...")
    os.system("pause")
    os.system("cls")
    return