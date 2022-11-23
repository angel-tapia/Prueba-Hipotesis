from Constantes import *
from Media_Varianza_Conocida import *
from Media_Varianza_Desconocida import *
from Proporcion import *
from Varianza import *
from Diferencia_Medias import *
from Diferencia_Proporcion import *
from Cociente_Varianzas import *
import os
from tkinter import Tk, Label , Button , Entry
"""
    <summary>
        Funcion que muestra el menu de las pruebas de hipotesis.
    </summary>
"""
def menu():
    ventana = Tk()
    ventana.title("Prueba De Hipotesis")
    ventana.geometry("500x300")
    
    #Media_Varianza_Conocida
    btnMedia_Varianza_Conocida = Button(ventana,text="Prueba de Hipotesis para una media con varianza conocida", command=menu_varianza_conocida)
    btnMedia_Varianza_Conocida.pack()
    #Media_Varianza_Desconocida
    btnMedia_Varianza_Desconocida = Button(ventana,text="Prueba de Hipotesis para una media con varianza desconocida",command=menu_varianza_desconocida)
    btnMedia_Varianza_Desconocida.pack()
    #Proporcion
    btnProporcion = Button(ventana,text="Prueba de Hipotesis para una proporción",command=menu_proporcion)
    btnProporcion.pack()
    #Varianza
    btnVarianza = Button(ventana,text="Prueba de Hipotesis para varianza",command=menu_varianza)
    btnVarianza.pack()
    #Diferencia de Medias
    btnDiferencia_de_Medias = Button(ventana,text="Prueba de Hipotesis para diferencia de medias",command=menu_diferencia_medias)
    btnDiferencia_de_Medias.pack()
    #Diferencia de Proporciones
    btnDiferencia_de_proporciones = Button(ventana,text="Prueba de Hipotesis para diferencia de proporciones",command=menu_diferencia_proporcion)
    btnDiferencia_de_proporciones.pack()
    #Cociente de Varianzas
    btnCociente_de_Varianzas = Button(ventana,text="Prueba de Hipotesis para cociente de varianzas",command=menu_cociente_varianzas)
    btnCociente_de_Varianzas.pack()
    ventana.mainloop()
    """""
    <summary>
    opcion = int(input("Seleccione una opcion: "))
    os.system("cls")
    #Create a switch for the options
    if opcion == 1:
        print("Prueba de Hipotesis para una media con varianza conocida")
        menu_varianza_conocida()
    elif opcion == 2:
        print("Prueba de Hipotesis para una media con varianza desconocida")
        menu_varianza_desconocida()
    elif opcion == 3:
        print("Prueba de Hipotesis para una proporción")
        menu_proporcion()
    elif opcion == 4:
        print("Prueba de Hipotesis para varianza")
        menu_varianza()
    elif opcion == 5:
        print("Prueba de Hipotesis para diferencia de medias")
        menu_diferencia_medias()
    elif opcion == 6:
        print("Prueba de Hipotesis para diferencia de proporciones")
        menu_diferencia_proporcion()
    elif opcion == 7:
        print("Prueba de Hipotesis para cociente de varianzas")
        menu_cociente_varianzas()
    else:
        print("Opcion no valida")
        menu()
    os.system("pause")
    menu()
</summary>
"""
menu()