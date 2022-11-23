from Tablas import *
from Constantes import *
import math
import os
from tkinter import Tk, Label , Button , Entry, messagebox
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
    ventanta = Tk()
    ventanta.title("Prueba de Hipotesis para una Varianza")
    ventanta.geometry("500x300")
    lbltitulo = Label(ventanta, text="Introduce los datos y selecciona la region critica a evaluar")
    lbltitulo.pack()
    lbln = Label(ventanta, text="n =")
    lbln.pack()
    txtn = Entry(ventanta)
    txtn.pack()
    lbls = Label(ventanta,text= "S = ")
    lbls.pack()
    txts = Entry(ventanta)
    txts.pack()
    lblsigma = Label(ventanta,text=Ssigma+" = ")
    lblsigma.pack()
    txtsigma = Entry(ventanta)
    txtsigma.pack()
    lblalpha = Label(ventanta,text=Salpha+" = ")
    lblalpha.pack()
    txtalpha = Entry(ventanta)
    txtalpha.pack()

    def calcularChi():
        n = txtn.get()
        s = txts.get()
        sigma = txtsigma.get()
        return (int(n) - 1)(math.pow(float(s), 2)) / (math.pow(float(sigma), 2))
    
    def obtenerAlpha():
        alpha = txtalpha.get()
        return float(alpha)
    def obtenerN():
        n = txtn.get()
        return int(n)-1
    btnRC_Menor_Que = Button(ventanta,text="<",command=lambda: prueba(calcularChi(),"<",  obtenerAlpha(),obtenerN()))
    btnRC_Menor_Que.pack()
    btnRC_Mayor_Que = Button(ventanta,text=">" ,command=lambda: prueba(calcularChi(),">",  obtenerAlpha(),obtenerN()))
    btnRC_Mayor_Que.pack()
    btnRC_Diferente = Button(ventanta,text="!=",command=lambda: prueba(calcularChi(),"!=",  obtenerAlpha(),obtenerN()))
    btnRC_Diferente.pack()
    ventanta.mainloop()
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
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    elif operation == ">":
        if chi > buscarJiCuadrada(alpha, n):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    elif operation == "!=":
        if chi < buscarJiCuadrada((1-alpha) / 2, n) or chi > buscarZ(alpha / 2, n):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    os.system("pause")
    os.system("cls")
    return
    

