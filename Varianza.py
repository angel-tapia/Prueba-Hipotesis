from Tablas import *
from Constantes import *
import math
import os

"""
    <summary>
        Función menú que realiza la prueba de hipótesis concerniente a varianzas.
    </summary>
    <param name="n">Número de datos.</param>
    <param name="s">Desviación estándar muestral.</param>
    <param name="sigma">Desviación estándar poblacional.</param>
    <param name="alpha">Nivel del significación.</param>
    <param name="chi">Valor del estadístico de prueba.</param>
"""
def menu_varianza():
    print("Elige la prueba de hipótesis a utilizar:")
    print("1.")
    print("H0 " + Ssigma + " = " + Ssigma + "_0")
    print("H1 " + Ssigma + " < " + Ssigma + "_0")
    print("2.")
    print("H0 " + Ssigma + " = " + Ssigma + "_0")
    print("H1 " + Ssigma + " > " + Ssigma + "_0")
    print("3.")
    print("H0 " + Ssigma + " = " + Ssigma + "_0")
    print("H1 " + Ssigma + " != " + Ssigma + "_0")
    opcion = int(input("Opción: "))
    os.system("cls")
    if opcion not in [1, 2, 3]:
        print("Opción incorrecta, vuelve a intentarlo.")
        print("Presione cualquier tecla para continuar...")
        os.system("pause")
        os.system("cls")
        menu_varianza()
        return
    
    print("Prueba de hipótesis concerniente a varianzas:")
    print("H0 " + Ssigma + " = " + Ssigma + "_0")
    print("H1 " + Ssigma + " " + ["<", ">", "!="][opcion - 1] + " " + Ssigma + "_0")
    print("")
    print("Introduce los datos:")
    n = int(input("n: "))
    s = float(input("S: "))
    sigma = float(input(Ssigma + ": "))
    alpha = float(input(Salpha + ": "))
    chi = (n - 1)(math.pow(s, 2)) / (math.pow(sigma, 2))
    print(Schi+"2 = " + str(chi))
    prueba(chi, ["<", ">", "!="][opcion - 1], alpha, n-1)
    return

"""
    <summary>
        Función prueba que rechaza o no rechaza H0.
    </summary>
    <param name="chi">Valor del estadístico de prueba.</param>
    <param name="operation">Operación a realizar.</param>
    <param name="alpha">Valor de alpha.</param>
    <param name="n">Grados de libertad.</param>
"""
def prueba(chi, operation, alpha, n):
    if operation == "<":
        if chi < buscarJiCuadrada(1-alpha, n):
            print("Rechazamos H0.")
        else:
            print("No rechazamos H0.")
    elif operation == ">":
        if chi > buscarJiCuadrada(alpha, n):
            print("Rechazamos H0.")
        else:
            print("No rechazamos H0.")
    elif operation == "!=":
        if chi < buscarJiCuadrada((1-alpha) / 2, n) or chi > buscarZ(alpha / 2, n):
            print("Rechazamos H0.")
        else:
            print("No rechazamos H0.")
    os.system("pause")
    os.system("cls")
    return
    
menu_varianza()
