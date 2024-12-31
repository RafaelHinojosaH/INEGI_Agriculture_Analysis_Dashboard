import plotly.express as px

def plot_bar_chart(df, x_col, y_col):
    """Crea un gráfico de barras interactivo con Plotly."""
    return px.bar(df, x=x_col, y=y_col)

def plot_line_chart(df, x_col, y_col):
    """Crea un gráfico de líneas interactivo con Plotly."""
    return px.line(df, x=x_col, y=y_col)
