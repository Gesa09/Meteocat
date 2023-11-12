import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    plt.figure(figsize=(10, 6))
    for station in temperaturas_por_estaciones.columns:
        plt.plot(temperaturas_por_estaciones.index, temperaturas_por_estaciones[station], label=f'Estación {station}',marker='o')
    plt.xlabel('Dies de Febrer')
    plt.ylabel('Temperatura mitjana')
    plt.title('Comparativa Temperatura Mitjana Diaria - Febrer 2022')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('Graficos/grafico_temperatura_media_febrero.png')

def exercici_4():
    february_2022_mean = temperaturas_por_estaciones.mean().mean()
    february_2023_prediction = february_2022_mean

    print(
        f"Predicció de temperatura mitjana estándar per Febrer de 2023: {int(round(february_2023_prediction))} graus")

    daily_median_temperatures = temperaturas_por_estaciones.median(axis=1).round().astype(int)

    plt.figure(figsize=(8, 4))
    plt.hist(daily_median_temperatures, bins=20, color='skyblue')
    plt.xlabel('Temperatura')
    plt.ylabel('Quantitat de dies')
    plt.title('Temperatures - Febrer 2023')
    plt.xticks(np.unique(daily_median_temperatures))
    plt.ylim(0, max(plt.hist(daily_median_temperatures, bins=20, color='skyblue')[0]) + 2)
    plt.savefig('Graficos/predicion_temperaturas.png')

    days_in_february_2023 = 28
    february_2023_random_temperatures = np.round(
        np.random.normal(february_2023_prediction, 2, days_in_february_2023)).astype(int)

    print("Valors de temperatura aleatoria per Febrer de 2023:")
    for i, temperature in enumerate(february_2023_random_temperatures, start=1):
        print(f"{i} de febrer: {temperature} graus")

def exercici_5():
    february_rain_data_2022 = estaciones_detalles[
        (estaciones_detalles['DATA_LECTURA'].dt.month == 2) &
        (estaciones_detalles['ACRÒNIM'] == 'PPT')
        ]

    february_rain_per_station = \
    february_rain_data_2022.groupby(['CODI_ESTACIO', february_rain_data_2022['DATA_LECTURA'].dt.day])[
        'VALOR'].mean().unstack(level=0)

    daily_median_rain = february_rain_per_station.median(axis=1)

    rainy_days_bool = daily_median_rain > 0

    days_of_february = range(1, len(daily_median_rain) + 1)

    plt.figure(figsize=(15, 6))
    plt.bar(days_of_february, rainy_days_bool, color=['blue' if rain else 'red' for rain in rainy_days_bool])
    plt.xlabel('Dies')
    plt.ylabel('Pluja (True/False)')
    plt.title('Predicció de pluja per Febrer 2023')
    plt.yticks([0, 1], ['No plou', 'Plou'])
    plt.xticks(days_of_february)
    plt.savefig('Graficos/prediccion_lluvia.png')

    rainy_days_count = np.sum(rainy_days_bool)
    non_rainy_days_count = len(rainy_days_bool) - rainy_days_count

    labels = ['Plou', 'No plou']
    sizes = [rainy_days_count, non_rainy_days_count]
    colors = ['#5da593', '#f70000']
    explode = (0.1, 0)
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title('Proporció de pluja per Febrer 2023')
    plt.savefig('Graficos/prediccion_lluvia2.png')


def __init__():
    while True:
        menu = select_option()
        match menu:
            case '1':
                exercici_3()
                print("Realitzat correctament. Fes un Rerun de la aplicació i mira a la carpeta 'Graficos'\n")
            case '2':
                exercici_4()
                print("Realitzat correctament. Fes un Rerun de la aplicació i mira a la carpeta 'Graficos'\n")
            case '3':
                exercici_5()
                print("Realitzat correctament. Fes un Rerun de la aplicació i mira a la carpeta 'Graficos'\n")
            case '4':
                exit()




__init__()
