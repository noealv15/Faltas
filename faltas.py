import pandas as pd
import requests 
import json
from datetime import datetime

# Leer el archivo Excel
faltas_ad = pd.read_excel('faltas_29_12_dic.xlsx')

faltas_ad.info()
faltas_ad.head()

def convertir_nombres_columnas(faltas_ad):
    """
    Convierte los nombres de las columnas de un DataFrame a minúsculas, elimina espacios al inicio y al final, 
    y reemplaza los espacios por guiones bajos.

    Args:
        faltas_ad: El DataFrame de Pandas.

    Returns:
        Un nuevo DataFrame con los nombres de las columnas modificados.
    """
    faltas_ad.columns = (
        faltas_ad.columns
        .str.strip()  # Elimina espacios al inicio y al final
        .str.lower()  # Convierte a minúsculas
        .str.replace(' ', '_')  # Reemplaza espacios internos por guiones bajos
    )
    return faltas_ad

faltas_ad = convertir_nombres_columnas(faltas_ad)
print(faltas_ad)