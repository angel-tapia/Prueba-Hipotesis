from Tablas import *
from Constantes import *
import math
import os
from tkinter import Tk, Label , Button , Entry, messagebox
"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una proporcion.
    </summary>
    <param name="x">Numero de exitos en la muestra.</param>
    <param name="n">Numero de ensayos en la muestra.</param>
    <param name="alpha">Nivel de significancia.</param>
    <param name="Z">Valor del estadistico de prueba.</param>
"""
def menu_proporcion():
    ventanta = Tk()
    ventanta.title("Prueba de Hipotesis para una proporcion")
    ventanta.geometry("500x300")
    lbln = Label(ventanta, text="n =")
    lbln.pack()
    txtn = Entry(ventanta)
    txtn.pack()
    lblx = Label(ventanta,text= "x = ")
    lblx.pack()
    txtx = Entry(ventanta)
    txtx.pack()
    lblalpha = Label(ventanta,text=Salpha+" = ")
    lblalpha.pack()
    txtalpha = Entry(ventanta)
    txtalpha.pack()
    def calcularZ():
        x = txtx.get()
        n = txtn.get()
        theta = int(x)/int(n)
        return (int(x) - int(n)*theta) / math.sqrt(int(n)*theta*(1-theta))
   
    def obtenerAlpha():
        alpha = txtalpha.get()
        return float(alpha)
   
    btnRC_Menor_Que = Button(ventanta,text="<",command=lambda: prueba(calcularZ(), 0.5 - obtenerAlpha(),"1"))
    btnRC_Menor_Que.pack()
    btnRC_Mayor_Que = Button(ventanta,text=">" ,command=lambda: prueba(calcularZ(), 0.5 - obtenerAlpha(),"2"))
    btnRC_Mayor_Que.pack()
    btnRC_Diferente = Button(ventanta,text="!=",command=lambda: prueba(calcularZ(), 0.5 - obtenerAlpha()/2,"3"))
    btnRC_Diferente.pack()
    ventanta.mainloop()
    return

"""
    <summary>
        Funcion que rechaza o no rechaza H0.
    </summary>
    <param name="Z">Valor de la prueba.</param>
    <param name="alpha">Valor de alpha.</param>
    <param name="opcion">Opcion de la prueba.</param>
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

