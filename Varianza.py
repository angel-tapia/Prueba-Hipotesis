from Tablas import *
from Constantes import *
from tkinter import Tk, Label , Button , Entry, messagebox

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
        Función menú que realiza la prueba de hipótesis concerniente a varianzas.
    </summary>
    <param name="n">Número de datos.</param>
    <param name="s">Desviación estándar muestral.</param>
    <param name="sigma">Desviación estándar poblacional.</param>
    <param name="alpha">Nivel del significación.</param>
    <param name="chi">Valor del estadístico de prueba.</param>
"""
def menu_varianza():
    ventana = Tk()
    ventana.title("Prueba de hipótesis para varianzas.")
    centrar(ventana, 500, 350)
    lbltitulo = Label(ventana, text="Introduce los datos y selecciona la región crítica a evaluar:")
    lbltitulo.pack()
    lbln = Label(ventana, text="n =")
    lbln.pack()
    txtn = Entry(ventana)
    txtn.pack()
    lbls = Label(ventana,text= "S = ")
    lbls.pack()
    txts = Entry(ventana)
    txts.pack()
    lblsigma = Label(ventana,text=Ssigma+" = ")
    lblsigma.pack()
    txtsigma = Entry(ventana)
    txtsigma.pack()
    lblalpha = Label(ventana,text=Salpha+" = ")
    lblalpha.pack()
    txtalpha = Entry(ventana)
    txtalpha.pack()
    #Función para calcular el estadístico ji cuadrada.
    def calcularChi():
        n = float(txtn.get())
        s = float(txts.get())
        sigma = float(txtsigma.get())
        return (n - 1)*(s**2) / (sigma**2)
    #Función para obtener el valor de alpha.    
    def obtenerAlpha():
        alpha = txtalpha.get()
        return float(alpha)
    #Función para obtener el valor de los n número de datos.
    def obtenerN():
        n = txtn.get()
        return int(n)-1
    #Botones para las pruebas de hipótesis.
    btnRC_Menor_Que = Button(ventana, text="<", command=lambda: prueba(calcularChi(), "<", obtenerAlpha(), obtenerN()))
    btnRC_Menor_Que.pack()
    btnRC_Mayor_Que = Button(ventana, text=">" , command=lambda: prueba(calcularChi(), ">", obtenerAlpha(), obtenerN()))
    btnRC_Mayor_Que.pack()
    btnRC_Diferente = Button(ventana, text="!=", command=lambda: prueba(calcularChi(), "!=", obtenerAlpha(), obtenerN()))
    btnRC_Diferente.pack()
    ventana.mainloop()
    return

"""
    <summary>
        Función prueba que rechaza o no rechaza H0.
    </summary>
    <param name="chi">Valor del estadístico de tablas.</param>
    <param name="operation">Operación a realizar.</param>
    <param name="alpha">Valor de la significancia.</param>
    <param name="n">Grados de libertad.</param>
"""
def prueba(chi, operation, alpha, n):
    if operation == "<":
        if chi <= buscarJiCuadrada(1-alpha, n):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    elif operation == ">":
        if chi >= buscarJiCuadrada(alpha, n):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    elif operation == "!=":
        if chi <= buscarJiCuadrada((1-alpha) / 2, n) or chi >= buscarJiCuadrada(alpha / 2, n):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    return