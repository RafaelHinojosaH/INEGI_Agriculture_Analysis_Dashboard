import os
import pandas as pd
import requests

# Lista de URLs de los archivos CSV
urls = [
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agr_mun_2023.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agr_mun_2022.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agr_mun_2021.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2020.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2019.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2018.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2017.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2016.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2015.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2014.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2013.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2012.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2011.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2010.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2009.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2008.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2007.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2006.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2005.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2004.csv",
    "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_2003.csv"
]

# Ruta del directorio donde se guardarán los archivos CSV
data_directory = "data/"

# Crear el directorio si no existe
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

# Descargar los archivos si no están presentes 
# Actualizar para tener un nombre más dijerible 
for url in urls:
    filename = os.path.join(data_directory, os.path.basename(url))
    if not os.path.exists(filename):
        print(f"Descargando {filename}...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"{filename} descargado correctamente.")
        else:
            print(f"Error al descargar {filename}. Código de estado: {response.status_code}")
    else:
        print(f"{filename} ya existe. Omite la descarga.")

# Obtener lista de archivos CSV en el directorio
csv_files = [os.path.join(data_directory, f) for f in os.listdir(data_directory) if f.endswith('.csv')]

# Leer y concatenar todos los archivos CSV
dataframes = []
for file in csv_files:
    try:
        df = pd.read_csv(file, encoding='latin1')
        dataframes.append(df)
    except Exception as e:
        print(f"Error al leer {file}: {e}")

if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Guardar el archivo combinado
    combined_file = os.path.join(data_directory, "combined_data.csv")
    combined_df.to_csv(combined_file, index=False)
    print(f"Archivo combinado guardado en: {combined_file}")
else:
    print("No se encontraron archivos CSV válidos para combinar.")