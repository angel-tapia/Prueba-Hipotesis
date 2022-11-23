from Tablas import *
from Constantes import *
import math
import os
from tkinter import Tk, Label , Button , Entry, messagebox
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
    #creación de todos los componentes de la GUI
    ventantaMedia_Varianza_Conocida = Tk()
    ventantaMedia_Varianza_Conocida.title("Prueba de Hipotesis para una media con varianza conocida")
    ventantaMedia_Varianza_Conocida.geometry("500x300")
    lbltitulo = Label(ventantaMedia_Varianza_Conocida, text="Introduce los datos y selecciona la region critica a evaluar")
    lbltitulo.pack()
    lbln = Label(ventantaMedia_Varianza_Conocida, text="n =")
    lbln.pack()
    txtn = Entry(ventantaMedia_Varianza_Conocida)
    txtn.pack()
    lblxbarra = Label(ventantaMedia_Varianza_Conocida,text= Sxbar+" = ")
    lblxbarra.pack()
    txtxbarra = Entry(ventantaMedia_Varianza_Conocida)
    txtxbarra.pack()
    lblmiu = Label(ventantaMedia_Varianza_Conocida,text=Smu+" = ")
    lblmiu.pack()
    txtmiu = Entry(ventantaMedia_Varianza_Conocida)
    txtmiu.pack()
    lblsigma = Label(ventantaMedia_Varianza_Conocida,text=Ssigma+" = ")
    lblsigma.pack()
    txtsigma = Entry(ventantaMedia_Varianza_Conocida)
    txtsigma.pack()
    lblalpha = Label(ventantaMedia_Varianza_Conocida,text=Salpha+" = ")
    lblalpha.pack()
    txtalpha = Entry(ventantaMedia_Varianza_Conocida)
    txtalpha.pack()
    #Función para calcular Z
    def calcularZ():
        n = txtn.get()
        xbarra = txtxbarra.get()
        xmu = txtmiu.get()
        sigma = txtsigma.get()
        return (float(xbarra) - float(xmu)) / (float(sigma) / math.sqrt(int(n)))
    #Función para obtener el valor de alpha cuando lo necesite, esto fue lo primero que se me ocurrió lo lamento Tapia
    def obtenerAlpha():
        alpha = txtalpha.get()
        return float(alpha)
    
    btnRC_Menor_Que = Button(ventantaMedia_Varianza_Conocida,text="<",command=lambda: prueba(calcularZ(),"<", 0.5 - obtenerAlpha()))
    btnRC_Menor_Que.pack()
    btnRC_Mayor_Que = Button(ventantaMedia_Varianza_Conocida,text=">" ,command=lambda: prueba(calcularZ(),">", 0.5 - obtenerAlpha()))
    btnRC_Mayor_Que.pack()
    btnRC_Diferente = Button(ventantaMedia_Varianza_Conocida,text="!=",command=lambda: prueba(calcularZ(),"!=", 0.5 - obtenerAlpha()/2))
    btnRC_Diferente.pack()
    ventantaMedia_Varianza_Conocida.mainloop()
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
    
