"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    from itertools import groupby

    datos=[]
    with open("files\input\data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            Campos=linea.strip().split("\t")
            datos.append(Campos)
    
    cantidad_letras=[(linea[0],1) for linea in datos]   

    cantidad_letras=sorted(cantidad_letras, key=lambda x:x[0])

    cantidad_sumada=[]
    for key, group in groupby(cantidad_letras, key=lambda x:x[0]):
        total=sum(item[1] for item in group)
        cantidad_sumada.append((key, total))

    return cantidad_sumada


