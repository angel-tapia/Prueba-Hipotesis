import pandas as pd
from IPython.display import display

# Leemos el excel con los datos
tablaZ = pd.read_excel(r"Prueba-Hipotesis\TablaZ.xlsx")
tablaT = pd.read_excel(r"Prueba-Hipotesis\TablaT.xlsx")
tablaJiCuadrada = pd.read_excel(r"Prueba-Hipotesis\TablaJiCuadrada.xlsx")
#tablaFisher = pd.read_excel(r"Prueba-Hipotesis\TablaFisher.xlsx")

"""
    <summary>
        Funcion que busca el valor de la tabla Z
    </summary>
    <param name="x">Valor a buscar</param>
    <returns>Valor de la tabla Z respecto a fila y columna</returns>
"""
def buscarZ(x):
    closer = 1e9
    ans = 0
    for col in tablaZ:
        if col == 'z':
            continue
        for j in range(len(tablaZ[col])):
            val = tablaZ[col][j]
            closer = min(closer, abs(x - val))
            if closer == abs(x - val):
                ans = col + tablaZ['z'][j]
    return ans

"""
    <summary>
        Funcion que calcula el valor de la tabla Z.
    </summary>
    <param name="alpha">Valor de la significancia.</param>
    <param name="n">Grados de libertad.</param>
    <return>Valor de la tabla JiCuadrada.</return>
"""

def buscarT(alpha, n):
    return tablaT[alpha][n-1]

def buscarJiCuadrada(alpha, n):
    return tablaJiCuadrada[alpha][n-1]
    