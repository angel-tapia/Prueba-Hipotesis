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
        Función menú que realiza la prueba de hipótesis de una varianza conocida.
        Dentro de la función va a leer datos y va a llamar a la función prueba.
    </summary>
    <param name="n">Número de datos de la muestra.</param>
    <param name="xbarra">Media muestral.</param>
    <param name="xmu">Media poblacional.</param>
    <param name="sigma">Desviacion estándar poblacional.</param>
    <param name="alpha">Nivel de significación.</param>
"""
def menu_varianza_conocida():
    #Creación de la ventana.
    ventana = Tk()
    ventana.title("Prueba de hipótesis para una media con varianza conocida")
    centrar(ventana, 500, 350)
    #Creación de labels, botones y textboxs.
    lbltitulo = Label(ventana, text="Introduce los datos y selecciona la región crítica a evaluar:")
    lbltitulo.pack()
    lbln = Label(ventana, text="n =")
    lbln.pack()
    txtn = Entry(ventana)
    txtn.pack()
    lblxbarra = Label(ventana,text=Sxbar+" = ")
    lblxbarra.pack()
    txtxbarra = Entry(ventana)
    txtxbarra.pack()
    lblmiu = Label(ventana,text=Smu+" = ")
    lblmiu.pack()
    txtmiu = Entry(ventana)
    txtmiu.pack()
    lblsigma = Label(ventana,text=Ssigma+" = ")
    lblsigma.pack()
    txtsigma = Entry(ventana)
    txtsigma.pack()
    lblalpha = Label(ventana,text=Salpha+" = ")
    lblalpha.pack()
    txtalpha = Entry(ventana)
    txtalpha.pack()
    #Función para calcular el estadístico z.
    def calcularZ():
        n = txtn.get()
        xbarra = txtxbarra.get()
        xmu = txtmiu.get()
        sigma = txtsigma.get()
        return (float(xbarra) - float(xmu)) / (float(sigma) / math.sqrt(int(n)))
    #Función para obtener el valor de alpha.
    def obtenerAlpha():
        alpha = txtalpha.get()
        return float(alpha)
    #Botones para las pruebas de hipótesis.
    btnRC_Menor_Que = Button(ventana, text="<", command=lambda: prueba(calcularZ(), "<", 0.5-obtenerAlpha()))
    btnRC_Menor_Que.pack()
    btnRC_Mayor_Que = Button(ventana, text=">" , command=lambda: prueba(calcularZ(), ">", 0.5-obtenerAlpha()))
    btnRC_Mayor_Que.pack()
    btnRC_Diferente = Button(ventana, text="!=", command=lambda: prueba(calcularZ(), "!=", 0.5-obtenerAlpha()/2))
    btnRC_Diferente.pack()
    ventana.mainloop()
    return

"""
    <summary>
        Función que rechaza o no rechaza H0.
    </summary>
    <param name="z">Valor del estadístico de tablas.</param>
    <param name="operation">Operación a realizar.</param>
    <param name="alpha">Valor de la significancia.</param>
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