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
        Función menú que realiza la prueba de hipótesis de una proporción.
        Dentro de la función va a leer datos y va a llamar a la función prueba.
    </summary>
    <param name="x">Número de éxitos en la muestra.</param>
    <param name="n">Número de ensayos en la muestra.</param>
    <param name="alpha">Nivel de significancia.</param>
    <param name="Z">Valor del estadístico de prueba.</param>
"""
def menu_proporcion():
    ventana = Tk()
    ventana.title("Prueba de hipótesis para una proporción")
    centrar(ventana, 500, 350)
    lbltitulo = Label(ventana, text="Introduce los datos y selecciona la región crítica a evaluar:")
    lbltitulo.pack()
    lbln = Label(ventana, text="n =")
    lbln.pack()
    txtn = Entry(ventana)
    txtn.pack()
    lblx = Label(ventana,text= "x = ")
    lblx.pack()
    txtx = Entry(ventana)
    txtx.pack()
    lbltheta = Label(ventana,text=Stheta+"_0 = ")
    lbltheta.pack()
    txttheta = Entry(ventana)
    txttheta.pack()
    lblalpha = Label(ventana,text=Salpha+" = ")
    lblalpha.pack()
    txtalpha = Entry(ventana)
    txtalpha.pack()
    #Función para calcular el estadístico z.
    def calcularZ():
        x = float(txtx.get())
        n = float(txtn.get())
        theta = float(txttheta.get())
        return (x - n*theta) / math.sqrt(n*theta*(1-theta))
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