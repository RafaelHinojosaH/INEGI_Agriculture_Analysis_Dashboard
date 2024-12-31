import os
import pandas as pd

# Ruta al directorio que contiene los archivos CSV
data_directory = "data/"

# Obtener lista de archivos CSV
csv_files = [os.path.join(data_directory, f) for f in os.listdir(data_directory) if f.endswith('.csv')]

# Leer y concatenar todos los archivos CSV
dataframes = [pd.read_csv(file, encoding='latin1') for file in csv_files]
combined_df = pd.concat(dataframes, ignore_index=True)

# Mostrar información del DataFrame combinado
print(combined_df.info())

# Guardar el archivo combinado
combined_df.to_csv("data/combined_data.csv", index=False)
print("Archivo combinado guardado en: data/combined_data.csv")

