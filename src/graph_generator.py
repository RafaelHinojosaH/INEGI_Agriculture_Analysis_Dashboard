import pandas as pd
import matplotlib.pyplot as plt
import os

# Create 'graphs' folder if it doesn't exist
output_dir = "graphs"
os.makedirs(output_dir, exist_ok=True)

# Simulating data loading for demonstration (replace with actual file path if available)
# df = pd.read_csv("your_file.csv") # Uncomment and modify for actual file
df = pd.DataFrame({
    'Año': [2020, 2021, 2022],
    'Estado': ['Jalisco', 'Michoacán', 'Puebla'],
    'Superficie_Sembrada': [1000, 1200, 1100],
    'Superficie_Cosechada': [950, 1150, 1050],
    'Producción_Volumen': [800, 900, 850],
    'Rendimiento': [0.85, 0.9, 0.8],
    'Precio_Promedio': [20, 22, 21],
    'Valor_Producción': [16000, 19800, 17850]
})

# Generate and save graphs

# 1. Superficie Sembrada vs. Año
plt.figure(figsize=(10, 6))
plt.bar(df['Año'], df['Superficie_Sembrada'], color='skyblue')
plt.xlabel('Año')
plt.ylabel('Superficie Sembrada')
plt.title('Superficie Sembrada por Año')
plt.savefig(os.path.join(output_dir, 'superficie_sembrada_vs_año.png'))
plt.close()

# 2. Superficie Cosechada vs. Año
plt.figure(figsize=(10, 6))
plt.plot(df['Año'], df['Superficie_Cosechada'], marker='o', linestyle='-', color='green')
plt.xlabel('Año')
plt.ylabel('Superficie Cosechada')
plt.title('Superficie Cosechada por Año')
plt.savefig(os.path.join(output_dir, 'superficie_cosechada_vs_año.png'))
plt.close()

# 3. Producción Volumen vs. Año
plt.figure(figsize=(10, 6))
plt.bar(df['Año'], df['Producción_Volumen'], color='orange')
plt.xlabel('Año')
plt.ylabel('Producción Volumen')
plt.title('Producción Volumen por Año')
plt.savefig(os.path.join(output_dir, 'produccion_volumen_vs_año.png'))
plt.close()

# 4. Rendimiento vs. Año
plt.figure(figsize=(10, 6))
plt.plot(df['Año'], df['Rendimiento'], marker='s', linestyle='--', color='purple')
plt.xlabel('Año')
plt.ylabel('Rendimiento')
plt.title('Rendimiento por Año')
plt.savefig(os.path.join(output_dir, 'rendimiento_vs_año.png'))
plt.close()

# 5. Valor Producción vs. Precio Promedio
plt.figure(figsize=(10, 6))
plt.scatter(df['Precio_Promedio'], df['Valor_Producción'], color='red')
plt.xlabel('Precio Promedio')
plt.ylabel('Valor Producción')
plt.title('Valor Producción vs. Precio Promedio')
plt.savefig(os.path.join(output_dir, 'valor_vs_precio_promedio.png'))
plt.close()

# Display confirmation of saved files
"Graphs saved successfully in 'graphs' folder."