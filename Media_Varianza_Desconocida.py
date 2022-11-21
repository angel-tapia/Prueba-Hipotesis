from Tablas import *
from Constantes import *
import math
import os

"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una varianza desconocida.
    </summary>
"""
def menu_varianza_desconocida():
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
        menu_varianza_desconocida()
        return
    
    print("Prueb de hipotesis de una varianza conocida")
    print("H0 " + Smu + " = " + Smu + "0")
    print("H1 " + Smu + " " + ["<", ">", "!="][opcion - 1] + " " + Smu + "0")
    print("")
    print("Introduce los datos:")
    n = int(input("n: "))
    xbarra = float(input(Sxbar + ": "))
    xmu = float(input(Smu + ": "))
    sigma = float(input(Ssigma + ": "))
    alpha = float(input(Salpha + ": "))
    z = (xbarra - xmu) / (sigma / math.sqrt(n))
    print("z = " + str(z))
    prueba(z, ["<", ">", "!="][opcion - 1], alpha,n-1)
    return

def prueba(z, operation, alpha, n):
    if operation == "<":
        if z < -buscarT(alpha,n):
            print("Rechazamos H0")
        else:
            print("No rechazamos H0")
    elif operation == ">":
        if z > buscarT(alpha,n):
            print("Rechazamos H0")
        else:
            print("No rechazamos H0")
    elif operation == "!=":
        if z < -buscarT(alpha / 2,n) or z > buscarT(alpha / 2,n):
            print("Rechazamos H0")
        else:
            print("No rechazamos H0")
    return
    
menu_varianza_desconocida()
    