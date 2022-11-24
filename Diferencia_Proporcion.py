from Tablas import *
from Constantes import *
from tkinter import Tk, Label , Button , Entry, messagebox
import math

"""
    <summary>
        Función que centra la ventana generada.
    </summary>
    <params name="root">Ventana fuente a centrar.</params>
    <params name="ancho">Anchura deseada para la ventana.</params>
    <params name="alto">Altura deseada para la ventana.</params>
    <params name="x">Posición en el eje de las x respecto al centro de la pantalla.</params>
    <params name="y">Posición en el eje de las y respecto al centro de la pantalla.</params>
"""
def centrar(root, ancho, alto):
    x = root.winfo_screenwidth() // 2 - ancho // 2
    y = root.winfo_screenheight() // 2 - alto // 2
    posicion = str(ancho) + "x" + str(alto) + "+" + str(x) + "+" + str(y)
    root.geometry(posicion)
    root.resizable(0,0)

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
"""
def menu_diferencia_proporcion():
    ventana = Tk()
    ventana.title("Prueba de hipótesis para una Diferencia de proporciones")
    centrar(ventana, 500, 350)
    lbltitulo = Label(ventana, text="Introduce los datos y selecciona la región crítica a evaluar:")
    lbltitulo.pack()
    lblx1 = Label(ventana, text="x1 = ")
    lblx1.pack()
    txtx1 = Entry(ventana)
    txtx1.pack()
    lblx2 = Label(ventana,text= "x2 = ")
    lblx2.pack()
    txtx2 = Entry(ventana)
    txtx2.pack()
    lbln1 = Label(ventana, text="n1 = ")
    lbln1.pack()
    txtn1 = Entry(ventana)
    txtn1.pack()
    lbln2 = Label(ventana,text= "n2 = ")
    lbln2.pack()
    txtn2 = Entry(ventana)
    txtn2.pack()
    lblalpha = Label(ventana,text=Salpha+" = ")
    lblalpha.pack()
    txtalpha = Entry(ventana)
    txtalpha.pack()
    #Función para calcular el estadístico z.
    def calcularZ():
        x1 = txtx1.get()
        x2 = txtx2.get()
        n1 = txtn1.get()
        n2 = txtn2.get()
        P = (float(x1)+float(x2)/int(n1)+int(n2))
        return (float(x1)/int(n1)-float(x2)/float(n2)) / math.sqrt(P * (1-P) * (1/int(n1)+1/int(n2)))
    #Función para obtener el valor de alpha.
    def obtenerAlpha():
        alpha = txtalpha.get()
        return 0.5-float(alpha)
    #Botones para las pruebas de hipótesis.
    btnRC_Menor_Que = Button(ventana, text="<", command=lambda: prueba(calcularZ(), "<", obtenerAlpha()))
    btnRC_Menor_Que.pack()
    btnRC_Mayor_Que = Button(ventana, text=">" , command=lambda: prueba(calcularZ(), ">", obtenerAlpha()))
    btnRC_Mayor_Que.pack()
    btnRC_Diferente = Button(ventana, text="!=", command=lambda: prueba(calcularZ(), "!=", obtenerAlpha()/2))
    btnRC_Diferente.pack()
    ventana.mainloop()
    return

"""
    <summary>
        Función que rechaza o no rechaza H0.
    </summary>
    <param name="z">Valor del estadístico de tablas.</param>
    <param name="alpha">Valor de la significancia.</param>
    <param name="operation">Opción de la prueba.</param>
"""
def prueba(z, operation, alpha):
    if operation == "<":
        if z <= -buscarZ(alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")            
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")            
    elif operation == ">":
        if z >= buscarZ(alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")            
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    elif operation == "!=":
        if z <= -buscarZ(alpha) or z >= buscarZ(alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")            
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")            
    return