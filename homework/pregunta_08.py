"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    from itertools import groupby
    datos=[]
    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:

        for linea in archivo:
            campos=linea.strip().split("\t")
            datos.append(campos)

    columnas=[]
    for linea in datos:
        columnas.append((int(linea[1]), linea[0]))
    
    columnas=sorted(columnas, key=lambda x:x[1])
    columnas=sorted(columnas, key=lambda x:x[0])

    letras_por_numero=[]
    for key, group in groupby(columnas, key=lambda x:x[0]):
        lista_letra=[]
        for item in group:
            if item[1] not in lista_letra:
                lista_letra.append(item[1])
        

        letras_por_numero.append((key,lista_letra))
    
    return letras_por_numero
