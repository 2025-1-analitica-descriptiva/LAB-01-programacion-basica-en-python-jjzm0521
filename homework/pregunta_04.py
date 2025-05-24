"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    from itertools import groupby
    datos=[]
    with open("files\input\data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            campos=linea.strip().split("\t")
            datos.append(campos)
    meses=[]
    for linea in datos:
        fechas=linea[2]
        fecha_g=fechas.split("-")
        print(linea[2])
        meses.append((fecha_g[1], 1))
    
    meses=sorted(meses, key=lambda x:x[0])

    meses_suma=[]
    for key, gruop in groupby(meses, key=lambda x:x[0]):
        total=sum(item[1] for item in gruop)
        meses_suma.append((key, total))

    return meses_suma












