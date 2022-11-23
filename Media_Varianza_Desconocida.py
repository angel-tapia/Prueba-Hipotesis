from Tablas import *
from Constantes import *
import math
import os

"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una media con varianza desconocida.
    </summary>
    <param name="sumatoria">Guarda la sumatoria de todos los datos ingresados.<param>
    <param name="s">Desviacion estandar de los datos ingresada por el usuario.<param>
    <param name="xbarra">Media de los datos ingresados.<param>
    <param name="xmu">Media de la poblacion.<param>
    <param name="n">Cantidad de datos ingresados.<param>
    <param name="t">Valor de la prueba.<param>
    <param name="alpha">Nivel de significancia.<param>
    <param name="operation">Operacion a realizar.<param>
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
    
    print("Prueb de hipotesis para la media, con varianza desconocida")
    print("H0 " + Smu + " = " + Smu + "0")
    print("H1 " + Smu + " " + ["<", ">", "!="][opcion - 1] + " " + Smu + "0")
    print("")
    print("Introduce los datos:")
    n = int(input("n: "))
    print("Ahora introduce los n datos")
    for i in n:
        sumatoria = sumatoria + float(input)
    xbarra = sumatoria/n
    xmu = float(input(Smu + ": "))
    s = float(input("s : "))
    alpha = float(input(Salpha + ": "))
    t = (xbarra - xmu) / (s / math.sqrt(n))
    print("z = " + str(z))
    prueba(z, ["<", ">", "!="][opcion - 1], alpha, n-1)
    return
"""
    <summary>
        Funcion que rechaza o no rechaza H0.
    </summary>
    <param name="t">Valor del estadistico prueba.</param>
    <param name="operation">Operacion a realizar.</param>
    <param name="alpha">Valor de alpha.</param>
"""
def prueba(t, operation, alpha, n):
    if operation == "<":
        if t < -buscarT(alpha, n):
            print("Rechazamos H0")
        else:
            print("No rechazamos H0")
    elif operation == ">":
        if t > buscarT(alpha, n):
            print("Rechazamos H0")
        else:
            print("No rechazamos H0")
    elif operation == "!=":
        if t < -buscarT(alpha / 2, n) or t > buscarT(alpha / 2, n):
            print("Rechazamos H0")
        else:
            print("No rechazamos H0")
    return
    