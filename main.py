import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def read_csv():
    estaciones_path = "CSV/2020_MeteoCat_Estacions.csv"
    estaciones_detalles_path = "CSV/2022_MeteoCat_Detall_Estacions.csv"
    metadatas_path = "CSV/MeteoCat_Metadades.csv"

    estaciones = pd.read_csv(estaciones_path)
    estaciones_detalles = pd.read_csv(estaciones_detalles_path)
    metadatas = pd.read_csv(metadatas_path)

    estaciones_array = np.array(estaciones)
    estaciones_detalles_array = np.array(estaciones_detalles)
    metadatas_array = np.array(metadatas)

    #estaciones_detalles_array['DATA_LECTURA'] = pd.to_datetime(estaciones_detalles_array['DATA_LECTURA'])
    #return estaciones_detalles_array

#GRÁFICO
    february_data = estaciones_detalles[
        (estaciones_detalles['DATA_LECTURA'].dt.month == 2)
        (estaciones_detalles['ACRÒNIM'] == "TM")
    ]

    temperaturas_por_estaciones = february_data.groupby(['CODI_ESTACIO', february_data['DATA_LECTURA'].dt.day])

    #febrero_2022 = estaciones_detalles[(estaciones_detalles['DATA_LECTURA'] >= '2022-02-01') & (estaciones_detalles['DATA_LECTURA'] <= '2022-02-28')]
    print(temperaturas_por_estaciones)

def __init__():
    print(read_csv())



__init__()
