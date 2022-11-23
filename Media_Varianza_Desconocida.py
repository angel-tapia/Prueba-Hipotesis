from Tablas import *
from Constantes import *
import math
import os
from tkinter import Tk, Label , Button , Entry, messagebox
"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una media con varianza desconocida.
    </summary>
    <param name= sumatoria> guarda la sumatoria de todos los datos ingresados <param>
    <param name = s>desviacion estandar de los datos ingresada por el usuario <param>
"""
def menu_varianza_desconocida():
    #creación de todos los componentes de la GUI
    ventanta = Tk()
    ventanta.title("Prueba de Hipotesis para una media con varianza conocida")
    ventanta.geometry("500x300")
    lbltitulo = Label(ventanta, text="Introduce los datos y selecciona la region critica a evaluar")
    lbltitulo.pack()
    lbln = Label(ventanta, text="n =")
    lbln.pack()
    txtn = Entry(ventanta)
    txtn.pack()
    lblxbarra = Label(ventanta,text= Sxbar+" = ")
    lblxbarra.pack()
    txtxbarra = Entry(ventanta)
    txtxbarra.pack()
    lblmiu = Label(ventanta,text=Smu+" = ")
    lblmiu.pack()
    txtmiu = Entry(ventanta)
    txtmiu.pack()
    lbls = Label(ventanta,text="S = ")
    lbls.pack()
    txts = Entry(ventanta)
    txts.pack()
    lblalpha = Label(ventanta,text=Salpha+" = ")
    lblalpha.pack()
    txtalpha = Entry(ventanta)
    txtalpha.pack()
    #Función para calcular Z
    def calcularZ():
        n = txtn.get()
        xbarra = txtxbarra.get()
        xmu = txtmiu.get()
        s = txts.get()
        return (float(xbarra) - float(xmu)) / (float(s) / math.sqrt(int(n)))
    #Función para obtener el valor de alpha cuando lo necesite, esto fue lo primero que se me ocurrió lo lamento Tapia
    def obtenerAlpha():
        alpha = txtalpha.get()
        return float(alpha)
    
    btnRC_Menor_Que = Button(ventanta,text="<",command=lambda: prueba(calcularZ(),"<", 0.5 - obtenerAlpha()))
    btnRC_Menor_Que.pack()
    btnRC_Mayor_Que = Button(ventanta,text=">" ,command=lambda: prueba(calcularZ(),">", 0.5 - obtenerAlpha()))
    btnRC_Mayor_Que.pack()
    btnRC_Diferente = Button(ventanta,text="!=",command=lambda: prueba(calcularZ(),"!=", 0.5 - obtenerAlpha()/2))
    btnRC_Diferente.pack()
    ventanta.mainloop()
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
            messagebox.showinfo("Resultado","Rechazamos H0.")
            
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
            
    elif operation == ">":
        if z > buscarZ(alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")
            
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
            print("No rechazamos H0.")
    elif operation == "!=":
        if z < -buscarZ(alpha) or z > buscarZ(alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")
            
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
            
    return
    

    