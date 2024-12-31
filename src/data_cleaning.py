import pandas as pd

# Ruta al archivo combinado
file_path = "data/combined_data.csv"

# Leer el archivo combinado
df = pd.read_csv(file_path, encoding="latin1")

# Renombrar columnas a nombres más legibles
df.rename(columns={
    "Anio": "Ano",
    "Idestado": "ID_Estado",
    "Nomestado": "Estado",
    "Idddr": "ID_DDR",
    "Nomddr": "DDR",
    "Idcader": "ID_CADER",
    "Nomcader": "CADER",
    "Idmunicipio": "ID_Municipio",
    "Nommunicipio": "Municipio",
    "Idciclo": "ID_Ciclo",
    "Nomcicloproductivo": "Ciclo_Producto",
    "Idmodalidad": "ID_Modalidad",
    "Nommodalidad": "Modalidad",
    "Idunidadmedida": "ID_Unidad_Medida",
    "Nomunidad": "Unidad_Medida",
    "Idcultivo": "ID_Cultivo",
    "Nomcultivo Sin Um": "Cultivo",
    "Sembrada": "Superficie_Sembrada",
    "Cosechada": "Superficie_Cosechada",
    "Siniestrada": "Superficie_Siniestrada",
    "Volumenproduccion": "Produccion_Volumen",
    "Rendimiento": "Rendimiento",
    "Precio": "Precio_Promedio",
    "Valorproduccion": "Valor_Produccion",
    "Nomcultivo": "Cultivo_Extra",
    "Preciomediorural": "Precio_Rural_Extra"
}, inplace=True)

# Combinar datos de 'Cultivo_Extra' con 'Cultivo'
df['Cultivo'] = df['Cultivo'].combine_first(df['Cultivo_Extra'])

# Combinar datos de 'Precio_Promedio' con 'Precio_Rural_Extra'
df['Precio_Promedio'] = df['Precio_Promedio'].combine_first(df['Precio_Rural_Extra'])

# Eliminar columnas redundantes después de la concatenación
df.drop(columns=["Cultivo_Extra", "Precio_Rural_Extra"], inplace=True)

# Guardar el DataFrame transformado
output_path = "data/transformed_combined_data.csv"
df.to_csv(output_path, index=False, encoding="latin1")

print(f"Datos transformados guardados en: {output_path}")
