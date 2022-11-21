from Tablas import *
from Constantes import *
import math
import os

"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una diferencia de medias.
    </summary>
    <param name="x_bar1">Media de la población 1.</param>
    <param name="x_bar2">Media de la población 2.</param>
    <param name="sigma1">Desviación estándar de la población 1.</param>
    <param name="sigma2">Desviación estándar de la población 2.</param>
    <param name="n1">Numero de ensayos en la población 1.</param>
    <param name="n2">Numero de ensayos en la población 2.</param>
    <param name="delta">Diferencia proporcional que existe entre las medias.</param>
    <param name="alpha">Nivel de significacia.</param>
    <param name="z">Valor del estadistico de prueba.</param>
"""
def menu_diferencia_medias():
    print("Elige la prueba de hipotesis a utilizar:")
    print("1.")
    print("H0. " + Smu + "1 - " + Smu + "2" + " = 0")
    print("H1. " + Smu + "1 - " + Smu + "2" + " < 0")
    print("2.")
    print("H0. " + Smu + "1 - " + Smu + "2" + " = 0")
    print("H1. " + Smu + "1 - " + Smu + "2" + " > 0")
    print("3.")
    print("H0. " + Smu + "1 - " + Smu + "2" + " = 0")
    print("H1. " + Smu + "1 - " + Smu + "2" + " != 0")
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
    print("H0. " + Smu + "1 - " + Smu + "2" + " = 0")
    print("H1. " + Smu + "1 - " + Smu + "2" + " " + ["<", ">", "!="][int(opcion) - 1] + " 0")
    print("")
    print("Introduce los datos:")
    x_bar1 = float(input(Sxbar + "1: "))
    x_bar2 = float(input(Sxbar + "2: "))
    delta = float(input(Sdelta + ": "))
    sigma1 = float(input(Ssigma + "1: "))
    sigma2 = float(input(Ssigma + "2: "))
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    alpha = float(input(Salpha + ": "))
    if opcion=="3":
        alpha = 0.5 - alpha/2
    else:
        alpha = 0.5 - alpha
    z = (x_bar1 - x_bar2 - delta) / (math.sqrt((sigma1/n1) + (sigma2/n2)))
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
        if z < -buscarZ(alpha) or z > buscarZ(alpha):
            print("Se rechaza H0.")
        else:
            print("No se rechaza H0.")
    print("Presiona una tecla para continuar...")
    os.system("pause")
    os.system("cls")
    return

menu_diferencia_medias()
