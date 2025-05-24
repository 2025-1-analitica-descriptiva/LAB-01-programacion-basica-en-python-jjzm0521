"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    from itertools import groupby
    datos=[]
    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            campos=linea.strip().split("\t")
            datos.append(campos)

    letra_num=[]
    for linea in datos:
        letra_num.append((linea[0],int(linea[1])))

    letra_num=sorted(letra_num, key=lambda x:x[0])

    letra_sum=[]
    for key, group in groupby(letra_num, key=lambda x:x[0]):
            total=sum(item[1] for item in group)
            letra_sum.append((key, total))
    return letra_sum