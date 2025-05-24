"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    from itertools import groupby
    datos=[]
    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:

        for linea in archivo:
            campos=linea.strip().split("\t")
            datos.append(campos)


    letras_numero=[]
    for linea in datos:
        letras=linea[3]
        letras=letras.strip().split(",")
        for letra in letras:
            letras_numero.append((letra,int(linea[1])))

    letras_numero = sorted(letras_numero, key=lambda x: x[0])

    
    dic_cantidad={}
    for key, group in groupby(letras_numero, key=lambda x:x[0]):
            total=sum(item[1] for item in group)
            dic_cantidad[key]=total
    return dic_cantidad