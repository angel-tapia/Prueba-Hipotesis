from Constantes import *
from Media_Varianza_Conocida import *
from Media_Varianza_Desconocida import *
from Proporcion import *
from Varianza import *
from Diferencia_Medias import *
from Diferencia_Proporcion import *
from Cociente_Varianzas import *
import os

#Create a function menu
def menu():
    print("""
    Prueba de Hipotesis
    1. Prueba de Hipotesis para una media con varianza conocida
    2. Prueba de Hipotesis para una media con varianza desconocida
    3. Prueba de Hipotesis para una proporción
    4. Prueba de Hipotesis para varianza
    5. Prueba de Hipotesis para diferencia de medias
    6. Prueba de Hipotesis para diferencia de proporciones
    7. Prueba de Hipotesis para cociente de varianzas
    """)
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
    elif opcion == 5:
        print("Prueba de Hipotesis para diferencia de medias")
    elif opcion == 6:
        print("Prueba de Hipotesis para diferencia de proporciones")
    elif opcion == 7:
        print("Prueba de Hipotesis para cociente de varianzas")
    else:
        print("Opcion no valida")
        menu()
    os.system("pause")
    menu()


menu()