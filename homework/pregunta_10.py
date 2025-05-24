"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    from itertools import groupby
    datos=[]
    with open(r"files\input\data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            campos=linea.strip().split("\t")
            datos.append(campos)
    
    solucion=[]
    for lista in datos:
        letra=lista[0]
        columna_4=lista[3].split(",")
        columna_5=lista[4].split(",")
        solucion.append((letra,len(columna_4),len(columna_5)))

    return solucion

