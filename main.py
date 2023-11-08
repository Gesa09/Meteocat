import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

estaciones_detalles = pd.read_csv("CSV/2022_MeteoCat_Detall_Estacions.csv")
estaciones = pd.read_csv("CSV/2020_MeteoCat_Estacions.csv")
metadatas = pd.read_csv("CSV/MeteoCat_Metadades.csv")

estaciones_detalles['DATA_LECTURA'] = pd.to_datetime(estaciones_detalles['DATA_LECTURA'])

february_data = estaciones_detalles[
    (estaciones_detalles['DATA_LECTURA'].dt.month == 2) &
    (estaciones_detalles['ACRÒNIM'] == "TM")]

temperaturas_por_estaciones = february_data.groupby(['CODI_ESTACIO', february_data['DATA_LECTURA'].dt.day])['VALOR'].mean().unstack(level=0)

def select_option():
    print("1 --> Exercici 3\n" +
          "2 --> Exercici 4\n" +
          "3 --> Exercici 5\n" +
          "4 --> Exit")
    opcio_seleccionada = input("Escull una opció: ")
    return opcio_seleccionada


def exercici_3():
    # Gráfico con diferentes colores
    plt.figure(figsize=(10, 6))
    for station in temperaturas_por_estaciones.columns:
        plt.plot(temperaturas_por_estaciones.index, temperaturas_por_estaciones[station], label=f'Estación {station}',marker='o')
    plt.xlabel('Días de febrero')
    plt.ylabel('Temperatura media')
    plt.title('Comparativa Temperatura Media Diaria - Febrero 2022')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('Graficos/grafico_temperatura_media_febrero.png')

    #febrero_2022 = estaciones_detalles[(estaciones_detalles['DATA_LECTURA'] >= '2022-02-01') & (estaciones_detalles['DATA_LECTURA'] <= '2022-02-28')]
    print(temperaturas_por_estaciones)

def __init__():
    while True:
        menu = select_option()
        match menu:
            case '1':
                exercici_3()
                print("Realitzat correctament. Mira a la carpeta 'Graficos'\n")
            case '2':
                exercici_4()
                print("Realitzat correctament. Mira a la carpeta 'Graficos'\n")
            case '3':
                exercici_5()
                print("Realitzat correctament. Mira a la carpeta 'Graficos'\n")
            case '4':
                exit()




__init__()
