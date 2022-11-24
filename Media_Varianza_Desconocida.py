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
        Función menú que realiza la prueba de hipótesis de una media con varianza desconocida.
        Dentro de la función va a leer datos y va a llamar a la función prueba.
    </summary>
    <param name=sumatoria>Sumatoria de todos los datos ingresados <param>
    <param name=s>Desviación estándar muestral.<param>
"""
def menu_varianza_desconocida():
    #Creación de la ventana.
    ventana = Tk()
    ventana.title("Prueba de hipótesis para una media con varianza conocida")
    centrar(ventana, 500, 350)
    #Creación de labels, botones y textboxs.
    lbltitulo = Label(ventana, text="Introduce los datos y selecciona la region critica a evaluar:")
    lbltitulo.pack()
    lbln = Label(ventana, text="n =")
    lbln.pack()
    txtn = Entry(ventana)
    txtn.pack()
    lblxbarra = Label(ventana,text= Sxbar+" = ")
    lblxbarra.pack()
    txtxbarra = Entry(ventana)
    txtxbarra.pack()
    lblmiu = Label(ventana,text=Smu+" = ")
    lblmiu.pack()
    txtmiu = Entry(ventana)
    txtmiu.pack()
    lbls = Label(ventana,text="S = ")
    lbls.pack()
    txts = Entry(ventana)
    txts.pack()
    lblalpha = Label(ventana,text=Salpha+" = ")
    lblalpha.pack()
    txtalpha = Entry(ventana)
    txtalpha.pack()
    #Función para calcular el estadístico t.
    def calcularT():
        n = txtn.get()
        xbarra = txtxbarra.get()
        xmu = txtmiu.get()
        s = txts.get()
        return (float(xbarra) - float(xmu)) / (float(s) / math.sqrt(int(n)))
    #Función para obtener el valor de alpha.
    def obtenerAlpha():
        alpha = txtalpha.get()
        return 0.5-float(alpha)
    #Botones para las pruebas de hipótesis.
    btnRC_Menor_Que = Button(ventana,text="<",command=lambda: prueba(calcularT(), "<", obtenerAlpha()))
    btnRC_Menor_Que.pack()
    btnRC_Mayor_Que = Button(ventana,text=">" ,command=lambda: prueba(calcularT(), ">", obtenerAlpha()))
    btnRC_Mayor_Que.pack()
    btnRC_Diferente = Button(ventana,text="!=",command=lambda: prueba(calcularT(), "!=", obtenerAlpha()/2))
    btnRC_Diferente.pack()
    ventana.mainloop()
    return

"""
    <summary>
        Función que rechaza o no rechaza H0.
    </summary>
    <param name="t">Valor del estadístico de tablas.</param>
    <param name="operation">Operación a realizar.</param>
    <param name="alpha">Valor de la significancia.</param>
"""
def prueba(t, operation, alpha):
    if operation == "<":
        if t <= -buscarZ(alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")    
    elif operation == ">":
        if t >= buscarZ(alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    elif operation == "!=":
        if t <= -buscarZ(alpha) or t >= buscarZ(alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    return