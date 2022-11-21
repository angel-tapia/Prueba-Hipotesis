from Tablas import *
from Constantes import *
import math
import os

"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una varianza conocida.
        Dentro de la funcion va a leer datos y va a llamar a la funcion prueba.
    </summary>
    <param name="n">Numero de datos</param>
    <param name="xbarra">Media muestral</param>
    <param name="xmu">Media poblacional</param>
    <param name="sigma">Desviacion tipica poblacional</param>
    <param name="alpha">Nivel de significacion</param>
    <param name="z">Valor del estadistico prueba</param>
"""
def menu_varianza_conocida():
    print("Elige la prueba de hipotesis a utilizar:")
    print("1.")
    print("H0 " + Smu + " = " + Smu + "0")
    print("H1 " + Smu + " < " + Smu + "0")
    print("2.")
    print("H0 " + Smu + " = " + Smu + "0")
    print("H1 " + Smu + " > " + Smu + "0")
    print("3.")
    print("H0 " + Smu + " = " + Smu + "0")
    print("H1 " + Smu + " != " + Smu + "0")
    opcion = int(input("Opcion: "))
    os.system("cls")

    if opcion not in [1, 2, 3]:
        print("Opcion incorrecta, vuelve a intentarlo.")
        print("Presione cualquier tecla para continuar...")
        os.system("pause")
        os.system("cls")
        menu_varianza_conocida()
        return
    
    print("Prueba de hipotesis de una varianza conocida")
    print("H0 " + Smu + " = " + Smu + "0")
    print("H1 " + Smu + " " + ["<", ">", "!="][opcion - 1] + " " + Smu + "0")
    print("")
    print("Introduce los datos:")
    n = int(input("n: "))
    xbarra = float(input(Sxbar + ": "))
    xmu = float(input(Smu + ": "))
    sigma = float(input(Ssigma + ": "))
    alpha = float(input(Salpha + ": "))
    if opcion=="3":
        alpha = 0.5 - alpha/2
    else:
        alpha = 0.5 - alpha
    z = (xbarra - xmu) / (sigma / math.sqrt(n))
    print("z = " + str(z))
    prueba(z, ["<", ">", "!="][opcion - 1], alpha)
    return

"""
    <summary>
        Funcion que rechaza o no rechaza H0.
    </summary>
    <param name="z">Valor del estadistico prueba.</param>
    <param name="operation">Operacion a realizar.</param>
    <param name="alpha">Valor de alpha.</param>
"""
def prueba(z, operation, alpha):
    if operation == "<":
        if z < -buscarZ(alpha):
            print("Rechazamos H0.")
        else:
            print("No rechazamos H0.")
    elif operation == ">":
        if z > buscarZ(alpha):
            print("Rechazamos H0.")
        else:
            print("No rechazamos H0.")
    elif operation == "!=":
        if z < -buscarZ(alpha) or z > buscarZ(alpha):
            print("Rechazamos H0.")
        else:
            print("No rechazamos H0.")
    return
    
menu_varianza_conocida()