from Tablas import *
from Constantes import *
import math
import os
from tkinter import Tk, Label , Button , Entry, messagebox
"""
    <summary>
        Función menú que realiza la prueba de hipótesis de una diferencia de proporciones.
        Dentro de la función va a leer datos y va a llamar a la función prueba.
    </summary>
    <param name="x1">Número de exitos en la muestra 1.</param>
    <param name="x2">Número de exitos en la muestra 2.</param>
    <param name="n1">Número de ensayos en la muestra 1.</param>
    <param name="n2">Número de ensayos en la muestra 2.</param>
    <param name="alpha">Nivel de significación.</param>
    <param name="Z">Valor del estadístico de prueba.</param>
"""
def menu_diferencia_proporcion():
    ventanta = Tk()
    ventanta.title("Prueba de Hipotesis para una Diferencia de proporciones")
    ventanta.geometry("500x600")
    lbltitulo = Label(ventanta, text="Introduce los datos y selecciona la region critica a evaluar")
    lbltitulo.pack()
    lblx1 = Label(ventanta, text="x1 =")
    lblx1.pack()
    txtx1 = Entry(ventanta)
    txtx1.pack()
    lblx2 = Label(ventanta,text= "x2 = ")
    lblx2.pack()
    txtx2 = Entry(ventanta)
    txtx2.pack()
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
        x1 = txtx1.get()
        x2 = txtx2.get()
        n1 = txtn1.get()
        n2 = txtn2.get()
        P = (float(x1)+float(x2)/int(n1)+int(n2))
        return (float(x1)/int(n1)-float(x2)/float(n2)) / math.sqrt(P * (1-P) * (1/int(n1)+1/int(n2)))
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
        Función que rechaza o no rechaza H0.
    </summary>
    <param name="Z">Valor del estadístico de prueba.</param>
    <param name="alpha">Valor de alpha.</param>
    <param name="opcion">Opción de la prueba.</param>
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

