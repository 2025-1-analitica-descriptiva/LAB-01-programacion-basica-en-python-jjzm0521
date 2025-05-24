"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    from itertools import groupby
    datos=[]
    with open("files\input\data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            campos=linea.strip().split("\t")
            datos.append(campos)


    claves=[]
    for linea in datos:
        conjunto=linea[-1].split(",")
        for clave in conjunto:
            clave=clave.split(":")
            claves.append((clave[0],1))
    claves=sorted(claves, key=lambda x:x[0])

    cantidad_claves={}
    for key, group in groupby(claves, key=lambda x:x[0]):
        total=sum(item[1] for item in group)
        cantidad_claves[key]=total

    return cantidad_claves