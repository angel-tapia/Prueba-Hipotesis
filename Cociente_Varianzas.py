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
    <params name="y">Posición en el eje de lasNúmero y respecto al centro de la pantalla.</params>
"""
def centrar(root, ancho, alto):
    x = root.winfo_screenwidth() // 2 - ancho // 2
    y = root.winfo_screenheight() // 2 - alto // 2
    posicion = str(ancho) + "x" + str(alto) + "+" + str(x) + "+" + str(y)
    root.geometry(posicion)
    root.resizable(0,0)

"""
    <summary>
        Función menú que realiza la prueba de hipótesis de un cociente de varianzas.
        Dentro de la función va a leer datos y va a llamar a la función prueba.
    </summary>
    <param name="n1">Número de elementos de la muestra 1.</param>
    <param name="n2">Número de elementos de la muestra 2.</param>
    <param name="s1">Desviación estándar de la muestra 1.</param>
    <param name="s2">Desviación estándar de la muestra 2.</param>
    <param name="alpha">Nivel de significación.</param>
    <param name="fisher>Valor del estadístico de prueba.</param>
"""
def menu_cociente_varianzas():
    ventana = Tk()
    ventana.title("Prueba de hipótesis para un Cociente de Varianzas")
    centrar(ventana, 500, 350)
    lbltitulo = Label(ventana, text="Introduce los datos y selecciona la region critica a evaluar")
    lbltitulo.pack()
    lbln1 = Label(ventana, text="n1 =")
    lbln1.pack()
    txtn1 = Entry(ventana)
    txtn1.pack()
    lbln2 = Label(ventana,text= "n2 = ")
    lbln2.pack()
    txtn2 = Entry(ventana)
    txtn2.pack()
    lbls1 = Label(ventana,text="S1 = ")
    lbls1.pack()
    txts1 = Entry(ventana)
    txts1.pack()
    lbls2 = Label(ventana,text="S2 = ")
    lbls2.pack()
    txts2 = Entry(ventana)
    txts2.pack()
    lblalpha = Label(ventana,text=Salpha+" = ")
    lblalpha.pack()
    txtalpha = Entry(ventana)
    txtalpha.pack()
    #Función para calcular el estadístico f.
    def calcularFisher():
        s1 = txts1.get()
        s2 = txts2.get()
        return float(s1)**2 / float(s2)**2        
    def obtenern1():
        n1 = txtn1.get()
        return int(n1)
    def obtenern2():
        n2 = txtn2.get()
        return int(n2)
    #Función para obtener el valor de alpha.        
    def obteneralpha():
        alpha = txtalpha.get()
        return float(alpha)
    #Botones para las pruebas de hipótesis.
    btnRC_Menor_Que = Button(ventana,text="<",command=lambda: prueba(obtenern2(), obtenern1(), calcularFisher(), obteneralpha(), "<"))
    btnRC_Menor_Que.pack()
    btnRC_Mayor_Que = Button(ventana,text=">" ,command=lambda: prueba(obtenern1(), obtenern2(), calcularFisher(), obteneralpha(), ">"))
    btnRC_Mayor_Que.pack()
    btnRC_Diferente = Button(ventana,text="!=",command=lambda: prueba(obtenern1(), obtenern2(), calcularFisher(), obteneralpha(), "!="))
    btnRC_Diferente.pack()
    ventana.mainloop()

    
    #prueba(n1, n2, fisher, alpha, opcion)

"""
    <summary>
        Función que rechaza o no rechaza H0
    </summary>
    <param name="n1">Número de elementos de la muestra 1.</param>
    <param name="n2">Número de elementos de la muestra 2.</param>
    <param name="fisher">Valor del estadístico de tablas.</param>
    <param name="alpha">Valor de la significancia.</param>
    <param name="opcion">Opción de la prueba de hipótesis.</param>
"""
def prueba(n1, n2, fisher, alpha, opcion):
    if opcion == "<":
        if fisher >= buscarF(n1 - 1, n2 - 1, alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")            
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")            
    elif opcion == ">":
        if fisher >= buscarF(n1 - 1, n2 - 1, alpha):
            messagebox.showinfo("Resultado","Rechazamos H0.")            
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")            
    elif opcion == "!=":
        if fisher >= buscarF(n1 - 1, n2 - 1, alpha/2) or fisher <= 1/buscarF(n1 - 1, n2 - 1, alpha/2):
            messagebox.showinfo("Resultado","Rechazamos H0.")
        else:
            messagebox.showinfo("Resultado","No rechazamos H0.")
    return         