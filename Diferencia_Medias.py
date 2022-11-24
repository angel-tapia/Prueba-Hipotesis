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
        Función menú que realiza la prueba de hipótesis de una diferencia de medias.
    </summary>
    <param name="x_bar1">Media de la población 1.</param>
    <param name="x_bar2">Media de la población 2.</param>
    <param name="sigma1">Desviación estándar de la población 1.</param>
    <param name="sigma2">Desviación estándar de la población 2.</param>
    <param name="n1">Número de ensayos en la población 1.</param>
    <param name="n2">Número de ensayos en la población 2.</param>
    <param name="delta">Diferencia proporcional que existe entre las medias.</param>
    <param name="alpha">Nivel de significacia.</param>
    <param name="z">Valor del estadístico de prueba.</param>
"""
def menu_diferencia_medias():
    ventana = Tk()
    ventana.title("Prueba de hipótesis para una diferencia de medias")
    centrar(ventana, 500, 450)
    lbltitulo = Label(ventana, text="Introduce los datos y selecciona la región crítica a evaluar:")
    lbltitulo.pack()
    lblxbarra1 = Label(ventana, text=Sxbar+"_1 = ")
    lblxbarra1.pack()
    txtxbarra1 = Entry(ventana)
    txtxbarra1.pack()
    lblxbarra2 = Label(ventana,text=Sxbar + "_2 = ")
    lblxbarra2.pack()
    txtxbarra2 = Entry(ventana)
    txtxbarra2.pack()
    lbldelta = Label(ventana,text=Sdelta+" = ")
    lbldelta.pack()
    txtdelta = Entry(ventana)
    txtdelta.pack()
    lblSigma1 = Label(ventana,text=Ssigma+"_1 = ")
    lblSigma1.pack()
    txtSigma1 = Entry(ventana)
    txtSigma1.pack()
    lblSigma2 = Label(ventana,text=Ssigma+"_2 = ")
    lblSigma2.pack()
    txtSigma2 = Entry(ventana)
    txtSigma2.pack()
    lbln1 = Label(ventana, text="n1 =")
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
        x_bar1 = txtxbarra1.get()
        x_bar2 = txtxbarra2.get()
        delta = txtdelta.get()
        sigma1 = txtSigma1.get()
        sigma2 = txtSigma2.get()
        n1 = txtn1.get()
        n2 = txtn2.get()
        return (float(x_bar1) - float(x_bar2) - float(delta)) / (math.sqrt((float(sigma1)**2 / int(n1)) + (float(sigma2)**2 / int(n2))))
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