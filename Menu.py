from Constantes import *
from Media_Varianza_Conocida import *
from Media_Varianza_Desconocida import *
from Proporcion import *
from Varianza import *
from Diferencia_Medias import *
from Diferencia_Proporcion import *
from Cociente_Varianzas import *
from tkinter import Tk, Button

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
        Función que muestra el menú de las pruebas de hipótesis.
    </summary>
"""
def menu():
    ventana = Tk()
    ventana.title("Pruebas de hipótesis")
    centrar(ventana, 500, 300)
    
    #Media_Varianza_Conocida
    btnMedia_Varianza_Conocida = Button(ventana,text="Prueba de hipótesis para una media con varianza conocida.", command=menu_varianza_conocida)
    btnMedia_Varianza_Conocida.pack()
    #Media_Varianza_Desconocida
    btnMedia_Varianza_Desconocida = Button(ventana,text="Prueba de hipótesis para una media con varianza desconocida.", command=menu_varianza_desconocida)
    btnMedia_Varianza_Desconocida.pack()
    #Proporción
    btnProporcion = Button(ventana,text="Prueba de hipótesis para una proporción.", command=menu_proporcion)
    btnProporcion.pack()
    #Varianza
    btnVarianza = Button(ventana,text="Prueba de hipótesis para varianzas.", command=menu_varianza)
    btnVarianza.pack()
    #Diferencia de Medias
    btnDiferencia_de_Medias = Button(ventana,text="Prueba de hipótesis para diferencia de medias", command=menu_diferencia_medias)
    btnDiferencia_de_Medias.pack()
    #Diferencia de Proporciones
    btnDiferencia_de_proporciones = Button(ventana,text="Prueba de hipótesis para diferencia de proporciones.", command=menu_diferencia_proporcion)
    btnDiferencia_de_proporciones.pack()
    #Cociente de Varianzas
    btnCociente_de_Varianzas = Button(ventana,text="Prueba de hipótesis para cociente de varianzas. ", command=menu_cociente_varianzas)
    btnCociente_de_Varianzas.pack()
    ventana.mainloop()
    """""    
    opcion = int(input("Seleccione una opción: "))
    os.system("cls")
    #Create a switch for the options
    if opcion == 1:
        print("Prueba de hipótesis para una media con varianza conocida.")
        menu_varianza_conocida()
    elif opcion == 2:
        print("Prueba de hipótesis para una media con varianza desconocida.")
        menu_varianza_desconocida()
    elif opcion == 3:
        print("Prueba de hipótesis para una proporción.")
        menu_proporcion()
    elif opcion == 4:
        print("Prueba de hipótesis para varianzas.")
        menu_varianza()
    elif opcion == 5:
        print("Prueba de hipótesis para diferencia de medias.")
        menu_diferencia_medias()
    elif opcion == 6:
        print("Prueba de hipótesis para diferencia de proporciones.")
        menu_diferencia_proporcion()
    elif opcion == 7:
        print("Prueba de hipótesis para cociente de varianzas.")
        menu_cociente_varianzas()
    else:
        print("Opción no valida.")
        menu()
    os.system("pause")
    menu()
"""
menu()