import streamlit as st
import pandas as pd
import os

# Configuración inicial de la aplicación
st.title("Visualización de Datos Agrícolas")
st.write("Esta aplicación permite cargar y explorar los datos del archivo CSV con métricas agrícolas.")

# Cargar el archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV", type="csv")

if uploaded_file:
    # Cargar datos del archivo CSV
    df = pd.read_csv(uploaded_file)

    # Mostrar vista previa de los datos
    st.subheader("Vista previa de los datos")
    st.dataframe(df.head())

    # Selección de análisis interactivo
    st.sidebar.header("Opciones de análisis")

    # Filtro de Año
    años = df['Año'].unique()
    selected_año = st.sidebar.selectbox("Selecciona un Año", sorted(años))

    # Filtrar datos por el año seleccionado
    df_filtered = df[df['Año'] == selected_año]

    # Mostrar datos filtrados
    st.subheader(f"Datos para el Año {selected_año}")
    st.dataframe(df_filtered)

    # Gráfica interactiva: Superficie Sembrada vs. Superficie Cosechada
    st.subheader("Superficie Sembrada vs. Superficie Cosechada")
    if not df_filtered.empty:
        chart_data = df_filtered[['Estado', 'Superficie_Sembrada', 'Superficie_Cosechada']]
        chart_data = chart_data.set_index('Estado')

        st.bar_chart(chart_data)

    # Métricas generales
    st.subheader("Métricas Generales")
    st.write(f"Producción total en el año {selected_año}: {df_filtered['Producción_Volumen'].sum()} toneladas")
    st.write(f"Valor total de la producción en el año {selected_año}: {df_filtered['Valor_Producción'].sum()} pesos")

    # Análisis adicional: Top 5 Estados por Valor de Producción
    st.subheader("Top 5 Estados por Valor de Producción")
    top_estados = df_filtered.groupby('Estado')["Valor_Producción"].sum().sort_values(ascending=False).head(5)
    st.bar_chart(top_estados)

else:
    st.info("Por favor, sube un archivo CSV para comenzar.")
