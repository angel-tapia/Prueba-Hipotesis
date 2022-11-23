from Tablas import *
from Constantes import *
import math
from tkinter import Tk, Label , Button , Entry, messagebox
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
    ventanta = Tk()
    ventanta.title("Prueba de Hipotesis para un Cociente de Varianzas")
    ventanta.geometry("500x300")
    lbltitulo = Label(ventanta, text="Introduce los datos y selecciona la region critica a evaluar")
    lbltitulo.pack()
    lbln1 = Label(ventanta, text="n1 =")
    lbln1.pack()
    txtn1 = Entry(ventanta)
    txtn1.pack()
    lbln2 = Label(ventanta,text= "n2 = ")
    lbln2.pack()
    txtn2 = Entry(ventanta)
    txtn2.pack()
    lbls1 = Label(ventanta,text="S1 = ")
    lbls1.pack()
    txts1 = Entry(ventanta)
    txts1.pack()
    lbls2 = Label(ventanta,text="S2 = ")
    lbls2.pack()
    txts2 = Entry(ventanta)
    txts2.pack()
    lblalpha = Label(ventanta,text=Salpha+" = ")
    lblalpha.pack()
    txtalpha = Entry(ventanta)
    txtalpha.pack()

    def calcularFisher():
        s1 = txts1.get()
        s2 = txts2.get()
        return float(s1)**2 / float(s2)**2
    def obtenern1():
        n1 = txtn1.get()
        return int(n1)
    def obtenern2():
        n2 = txtn2.get()
        return int(n2)
    def obteneralpha():
        alpha = txtalpha.get()
        return float(alpha)
    btnRC_Menor_Que = Button(ventanta,text="<",command=lambda: prueba(obtenern1(),obtenern2(), calcularFisher(),obteneralpha(),"<"))
    btnRC_Menor_Que.pack()
    btnRC_Mayor_Que = Button(ventanta,text=">" ,command=lambda: prueba(obtenern1(),obtenern2(), calcularFisher(),obteneralpha(),">"))
    btnRC_Mayor_Que.pack()
    btnRC_Diferente = Button(ventanta,text="!=",command=lambda: prueba(obtenern1(),obtenern2(), calcularFisher(),obteneralpha(),"!="))
    btnRC_Diferente.pack()
    ventanta.mainloop()

    
    #prueba(n1, n2, fisher, alpha, opcion)

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
            messagebox.showinfo("Resultado","Rechazamos H0.")
            
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
            
    elif opcion == 2:
        if fisher >= buscarF(n2 - 1, n1 - 1, alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")
            
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
            
    else:
        if fisher >= buscarF(n1 - 1, n2 - 1, alpha/2) or fisher <= 1/buscarF(n2 - 1, n1 - 1, alpha/2):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    return         

    
