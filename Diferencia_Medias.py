from Tablas import *
from Constantes import *
import math
import os
from tkinter import Tk, Label , Button , Entry, messagebox
"""
    <summary>
        Funcion menu que realiza la prueba de hipotesis de una diferencia de medias.
    </summary>
    <param name="x_bar1">Media de la población 1.</param>
    <param name="x_bar2">Media de la población 2.</param>
    <param name="sigma1">Desviación estándar de la población 1.</param>
    <param name="sigma2">Desviación estándar de la población 2.</param>
    <param name="n1">Numero de ensayos en la población 1.</param>
    <param name="n2">Numero de ensayos en la población 2.</param>
    <param name="delta">Diferencia proporcional que existe entre las medias.</param>
    <param name="alpha">Nivel de significacia.</param>
    <param name="z">Valor del estadistico de prueba.</param>
"""
def menu_diferencia_medias():
    ventanta = Tk()
    ventanta.title("Prueba de Hipotesis para una Diferencia de Medias")
    ventanta.geometry("500x600")
    lbltitulo = Label(ventanta, text="Introduce los datos y selecciona la region critica a evaluar")
    lbltitulo.pack()
    lblxbarra1 = Label(ventanta, text=Sxbar+"_1 = ")
    lblxbarra1.pack()
    txtxbarra1 = Entry(ventanta)
    txtxbarra1.pack()
    lblxbarra2 = Label(ventanta,text=Sxbar + "_2 = ")
    lblxbarra2.pack()
    txtxbarra2 = Entry(ventanta)
    txtxbarra2.pack()
    lbldelta = Label(ventanta,text=Sdelta+" = ")
    lbldelta.pack()
    txtdelta = Entry(ventanta)
    txtdelta.pack()
    lblSigma1 = Label(ventanta,text=Ssigma+"_1 = ")
    lblSigma1.pack()
    txtSigma1 = Entry(ventanta)
    txtSigma1.pack()
    lblSigma2 = Label(ventanta,text=Ssigma+"_2 = ")
    lblSigma2.pack()
    txtSigma2 = Entry(ventanta)
    txtSigma2.pack()
    lbln1 = Label(ventanta, text="n1 =")
    lbln1.pack()
    txtn1 = Entry(ventanta)
    txtn1.pack()
    lbln2 = Label(ventanta,text= "n2 = ")
    lbln2.pack()
    txtn2 = Entry(ventanta)
    txtn2.pack()
    lblalpha = Label(ventanta,text=Salpha+" = ")
    lblalpha.pack()
    txtalpha = Entry(ventanta)
    txtalpha.pack()

    def calcularZ():
        x_bar1 = txtxbarra1.get()
        x_bar2 = txtxbarra2.get()
        delta = txtdelta.get()
        sigma1 = txtSigma1.get()
        sigma2 = txtSigma2.get()
        n1 = txtn1.get()
        n2 = txtn2.get()
        return (float(x_bar1) - float(x_bar2) - float(delta)) / (math.sqrt((float(sigma1)**2 / int(n1)) + (float(sigma2)**2 / int(n2))))
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
    <param name="z">Valor de la prueba.</param>
    <param name="alpha">Valor de alpha.</param>
    <param name="opcion">Opcion de la prueba.</param>
"""
def prueba(z, alpha, opcion):
    if opcion == "1":
        if z < -buscarZ(alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    elif opcion == "2":
        if z > buscarZ(alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    elif opcion == "3":
        if z < -buscarZ(alpha) or z > buscarZ(alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    
    return


