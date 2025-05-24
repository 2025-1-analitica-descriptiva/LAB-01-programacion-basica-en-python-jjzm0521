"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    from itertools import groupby
    datos=[]
    with open(r"files\input\data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            campos=linea.strip().split("\t")
            datos.append(campos)


    claves=[]
    for linea in datos:
        conjunto=linea[-1].split(",")
        for clave in conjunto:
            clave=clave.split(":")
            claves.append((clave[0],int(clave[1])))
    claves=sorted(claves, key=lambda x:x[0])
    
    Dic_max_min=[]
    for key, group in groupby(claves, key=lambda x:x[0]):
        minimo=10
        maximo=0
        for casos in  group:
            if (minimo>casos[1]):
                minimo=casos[1]
            if (maximo<casos[1]):
                maximo=casos[1]
        Dic_max_min.append((key, minimo, maximo))

    return Dic_max_min
    