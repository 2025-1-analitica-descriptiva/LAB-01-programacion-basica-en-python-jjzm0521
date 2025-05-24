"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_por_letra={}
    with open("files\input\data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            campos=linea.strip().split("\t")
            Letra=campos[0]
            columna_5=campos[4].split(",")
            suma=0
            for conjunto in columna_5:
                conjunto=conjunto.split(":")
                suma+=int(conjunto[1])
            
            if Letra in suma_por_letra:
                suma_por_letra[Letra]+=suma
            else:
                suma_por_letra[Letra]=suma
    suma_por_letra=dict(sorted(suma_por_letra.items()))
    return suma_por_letra


