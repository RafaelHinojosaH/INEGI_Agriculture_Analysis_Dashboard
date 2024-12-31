import os

def ensure_directory(directory):
    """Crea el directorio si no existe."""
    os.makedirs(directory, exist_ok=True)

