from Tablas import *
from Constantes import *
import math
import os

"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de un cociente de varianzas.
        Dentro de la funcion va a leer datos y va a llamar a la funcion prueba.
    </summary>
    <param name="n1">Numero de elementos de la muestra 1.</param>
    <param name="n2">Numero de elementos de la muestra 2.</param>
    <param name="s1">Desviacion tipica de la muestra 1.</param>
    <param name="s2">Desviacion tipica de la muestra 2.</param>
    <param name="alpha">Nivel de significacion.</param>
    <param name="fisher>Valor de la tabla de fisher.</param>
"""
def menu_cociente_varianzas():
    print("Elige la prueba de hipotesis a utilizar:")
    print("1.")
    print("H0 " + Ssigma + "1^2 = " + Ssigma + "2^2")
    print("H1 " + Ssigma + "1^2 != " + Ssigma + "2^2")
    print("2.")
    print("H0 " + Ssigma + "1^2 = " + Ssigma + "2^2")
    print("H1 " + Ssigma + "1^2 < " + Ssigma + "2^2")
    print("3.")
    print("H0 " + Ssigma + "1^2 = " + Ssigma + "2^2")
    print("H1 " + Ssigma + "1^2 > " + Ssigma + "2^2")
    opcion = int(input("Opcion: "))
    os.system("cls")

    if opcion not in [1, 2, 3]:
        print("Opcion incorrecta, vuelve a intentarlo.")
        print("Presione cualquier tecla para continuar...")
        os.system("pause")
        os.system("cls")
        menu_cociente_varianzas()
        return

    print("Prueba de hipotesis de un cociente de varianzas")
    print("H0 " + Ssigma + "1^2 = " + Ssigma + "2^2")
    print("H1 " + Ssigma + "1^2 " + ["!=", "<", ">"][opcion - 1] + " " + Ssigma + "2^2")
    print("")
    print("Introduce los datos:")
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    s1 = float(input(Ssigma + "1: "))
    s2 = float(input(Ssigma + "2: "))
    alpha = float(input(Salpha + ": "))
    alpha = 0.5 - alpha 
    fisher = s1**2 / s2**2
    os.system("cls")
    prueba(n1, n2, fisher, alpha, opcion)

"""
    <summary>
        Funcion que rechaza o no rechaza H0
    </summary>
    <param name="n1">Numero de elementos de la muestra 1</param>
    <param name="n2">Numero de elementos de la muestra 2</param>
    <param name="fisher">Valor del estadistico de prueba de fisher</param>
    <param name="alpha">Nivel de significancia</param>
    <param name="opcion">Opcion de la prueba de hipotesis</param>
"""
def prueba(n1, n2, fisher, alpha, opcion):
    if opcion == 1:
        if fisher >= buscarF(n1 - 1, n2 - 1, alpha):
            print("Se rechaza H0")
        else:
            print("No se rechaza H0")
    elif opcion == 2:
        if fisher >= buscarF(n2 - 1, n1 - 1, alpha):
            print("Se rechaza H0")
        else:
            print("No se rechaza H0")
    else:
        if fisher >= buscarF(n1 - 1, n2 - 1, alpha/2):
            print("Se rechaza H0")
        else:
            print("No se rechaza H0")

    print("Presione cualquier tecla para continuar...")
    os.system("pause")
    os.system("cls")
