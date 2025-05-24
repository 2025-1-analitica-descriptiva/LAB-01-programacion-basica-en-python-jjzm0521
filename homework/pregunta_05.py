"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    from itertools import groupby

    datos=[]
    with open(r"files\input\data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            campos=linea.strip().split("\t")
            datos.append(campos)
    
    letras_y_numeros=[]
    for linea in datos:
        letras_y_numeros.append((linea[0],int(linea[1])))

    letras_y_numeros=sorted(letras_y_numeros, key=lambda x: x[0])

    Letra_Mym=[]
    for key,group in groupby(letras_y_numeros, key=lambda x:x[0]):
        maximo=0
        minimo=10
        for casos in  group:
            if (minimo>casos[1]):
                minimo=casos[1]
            elif (maximo<casos[1]):
                maximo=casos[1]
        Letra_Mym.append((key, maximo, minimo))

    return Letra_Mym


