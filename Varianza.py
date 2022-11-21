from Tablas import *
from Constantes import *
import math
import os

"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una varianza.
    </summary>
"""
def menu_varianza():
    print("Elige la prueba de hipotesis a utilizar:")
    print("1.")
    print("H0 " + Ssigma + " = " + Ssigma + "_0")
    print("H1 " + Ssigma + " < " + Ssigma + "_0")
    print("2.")
    print("H0 " + Ssigma + " = " + Ssigma + "_0")
    print("H1 " + Ssigma + " > " + Ssigma + "_0")
    print("3.")
    print("H0 " + Ssigma + " = " + Ssigma + "_0")
    print("H1 " + Ssigma + " != " + Ssigma + "_0")
    opcion = int(input("Opcion: "))
    os.system("cls")
    if opcion not in [1, 2, 3]:
        print("Opcion incorrecta, vuelve a intentarlo.")
        print("Presione cualquier tecla para continuar...")
        os.system("pause")
        os.system("cls")
        menu_varianza()
        return
    
    print("Prueba de hipotesis concernite a varianzas")
    print("H0 " + Ssigma + " = " + Ssigma + "_0")
    print("H1 " + Ssigma + " " + ["<", ">", "!="][opcion - 1] + " " + Ssigma + "_0")
    print("")
    print("Introduce los datos:")
    n = int(input("n: "))
    varmu = float(input("S: "))
    sigma = float(input(Ssigma + ": "))
    alpha = float(input(Salpha + ": "))
    chi = (n - 1)(math.sqrt(varmu)) / (math.sqrt(sigma))
    print(Schi+"^2 = " + str(chi))
    prueba(chi, ["<", ">", "!="][opcion - 1], alpha, n-1)
    return

"""
    <summary>
        Funcion que rechaza o no rechaza H0.
    </summary>
    <param name="z">Valor del estadistico prueba.</param>
    <param name="operation">Operacion a realizar.</param>
    <param name="alpha">Valor de alpha.</param>
"""
def prueba(chi, operation, alpha, n):
    if operation == "<":
        if chi < buscarJiCuadrada(1-alpha, n):
            print("Rechazamos H0")
        else:
            print("No rechazamos H0")
    elif operation == ">":
        if chi > buscarJiCuadrada(alpha, n):
            print("Rechazamos H0")
        else:
            print("No rechazamos H0")
    elif operation == "!=":
        if chi < buscarJiCuadrada((1-alpha) / 2, n) or chi > buscarZ(alpha / 2, n):
            print("Rechazamos H0")
        else:
            print("No rechazamos H0")
    return
    
menu_varianza()
