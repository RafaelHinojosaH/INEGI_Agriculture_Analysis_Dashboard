import pandas as pd
import re

# Ruta al archivo combinado
file_path = "data/combined_data.csv"

# Leer el archivo combinado
df = pd.read_csv(file_path, encoding="utf-8")

# Renombrar columnas a nombres más legibles para facilitar el análisis y la interpretación
df.rename(columns={
    "Anio": "Anio",  # Año de la información, formato numérico de 4 dígitos (e.g., 2023)
    "Idestado": "ID_Estado",  # Código numérico que identifica al estado de producción (1-32)
    "Nomestado": "Estado",  # Nombre oficial de la entidad federativa o estado
    "Idddr": "ID_DDR",  # Código numérico del Distrito de Desarrollo Rural (1-193)
    "Nomddr": "DDR",  # Nombre del Distrito de Desarrollo Rural
    "Idcader": "ID_CADER",  # Código numérico del Centro de Apoyo al Desarrollo Rural (1-19)
    "Nomcader": "CADER",  # Nombre del Centro de Apoyo al Desarrollo Rural
    "Idmunicipio": "ID_Municipio",  # Código numérico del municipio o delegación de producción (1-570)
    "Nommunicipio": "Municipio",  # Nombre del municipio o delegación de producción
    "Idciclo": "ID_Ciclo",  # Código numérico que identifica al ciclo agrícola (1-3)
    "Nomcicloproductivo": "Ciclo_Producto",  # Nombre descriptivo del ciclo agrícola
    "Idmodalidad": "ID_Modalidad",  # Código numérico que identifica al tipo de modalidad hídrica (1-2)
    "Nommodalidad": "Modalidad",  # Nombre descriptivo de la modalidad hídrica
    "Idunidadmedida": "ID_Unidad_Medida",  # Código numérico que identifica la unidad de medida (1-6)
    "Nomunidad": "Unidad_Medida",  # Nombre descriptivo de la unidad de medida (e.g., Tonelada)
    "Idcultivo": "ID_Cultivo",  # Código numérico que identifica el cultivo agrícola (1-410)
    "Nomcultivo Sin Um": "Cultivo",  # Nombre del cultivo agrícola, sin unidad de medida adicional
    "Sembrada": "Superficie_Sembrada",  # Superficie sembrada del cultivo en hectáreas
    "Cosechada": "Superficie_Cosechada",  # Superficie cosechada del cultivo en hectáreas
    "Siniestrada": "Superficie_Siniestrada",  # Superficie afectada o perdida del cultivo en hectáreas
    "Volumenproduccion": "Produccion_Volumen",  # Volumen de producción en la unidad de medida correspondiente
    "Rendimiento": "Rendimiento",  # Rendimiento en términos de producción por hectárea
    "Precio": "Precio_Promedio",  # Precio medio rural por unidad de producción
    "Valorproduccion": "Valor_Produccion",  # Valor total de la producción en términos monetarios
    "Nomcultivo": "Cultivo_Extra",  # Nombre adicional del cultivo (puede incluir detalles adicionales)
    "Preciomediorural": "Precio_Rural_Extra"  # Precio medio rural adicional (si aplica)
}, inplace=True)


# Combinar datos de 'Cultivo_Extra' con 'Cultivo'
df['Cultivo'] = df['Cultivo'].combine_first(df['Cultivo_Extra'])

# Combinar datos de 'Precio_Promedio' con 'Precio_Rural_Extra'
df['Precio_Promedio'] = df['Precio_Promedio'].combine_first(df['Precio_Rural_Extra'])

# Eliminar columnas redundantes después de la concatenación
df.drop(columns=["Cultivo_Extra", "Precio_Rural_Extra"], inplace=True)

# Filtrar el DataFrame para incluir solo registros donde el año sea >= 2006
df_filtered = df[df['Ano'] >= 2006]

# Guardar el DataFrame transformado
output_path = "data/transformed_combined_data.csv"
           
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"Datos transformados guardados en: {output_path}")

special_characters_pattern = re.compile(r"[^\w\s]", re.UNICODE)
for column in df.columns:
    if df[column].dtype == 'object':
        has_special = df[column].apply(lambda x: bool(special_characters_pattern.search(str(x))) if pd.notnull(x) else False)
        if has_special.any():
                print(f"La columna '{column}' contiene caracteres especiales.")