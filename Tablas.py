import pandas as pd
from IPython.display import display

# Leemos el excel con los datos
tablaZ = pd.read_excel(r"Prueba-Hipotesis\TablaZ.xlsx")
tablaJiCuadrada = pd.read_excel(r"Prueba-Hipotesis\TablaJiCuadrada.xlsx")
#tablaT = pd.read_excel(r"Prueba-Hipotesis\TablaT.xlsx")
tablaFisher01 = pd.read_excel(r"Prueba-Hipotesis\TablaF0.01.xlsx")
#tablaFisher05 = pd.read_excel(r"Prueba-Hipotesis\TablaF0.005.xlsx")

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
def buscarJiCuadrada(alpha, n):
    return tablaJiCuadrada[alpha][n-1]

"""
    <summary>
        Funcion que calcula el valor de la tabla Fisher 0.01.
    </summary>
    <param name="v1">Grados de libertad.</param>
    <param name="v2">Grados de libertad.</param>
    <return>Valor de la tabla Fisher 0.01.</return>
"""
def buscarFisher01(v1, v2):
    return tablaFisher01[v1][v2]

"""
    <summary>
        Funcion que calcula el valor de la tabla Fisher 0.05.
    </summary>
    <param name="v1">Grados de libertad.</param>
    <param name="v2">Grados de libertad.</param>
    <return>Valor de la tabla Fisher 0.05.</return>
"""
def buscarFisher05(v1, v2):
    return #tablaFisher05[v1][v2]

"""
    <summary>
        Funcion que calcula el valor de la tabla Fisher.
    </summary>
    <param name="v1">Grados de libertad.</param>
    <param name="v2">Grados de libertad.</param>
    <param name="alpha">Valor de la significancia.</param>
    <return>Valor de la tabla Fisher.</return>
"""
def buscarF(v1, v2, alpha):
    if alpha == 0.01:
        return buscarFisher01(v1, v2)
    else:
        return buscarFisher05(v1, v2)

display(tablaFisher01)