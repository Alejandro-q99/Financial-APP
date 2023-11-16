import numpy as np
import pandas as pd






def normalize_percentage(value):
    """
    Convierte un valor de porcentaje en formato string a un decimal.
    Ejemplo: '99.0%' se convierte en 0.99.
    Maneja los valores no numéricos o faltantes adecuadamente.
    """
    try:
        if isinstance(value, str):
            return float(value.strip('%')) / 100
    except ValueError:
        # Retorna None o un valor predeterminado en caso de valores no convertibles
        return None
    return value




def remove_arrows(value):
    """
    Elimina los símbolos de flecha (↑ y ↓) de un string.
    """
    if isinstance(value, str):
        return value.replace('↑', '').replace('↓', '')
    return value




def clean_and_convert_data(df):
    """
    Limpia y convierte los datos del DataFrame.
    La idea es normalizar el dataset para que sea más calculable"
    
    """
    cleaned_df = df.copy()

    # Columnas que necesitan normalización de porcentajes
    percentage_columns = ['diferencia', 'paridad', 'qp', 'ttir', 'uptir']

    # Limpiar y convertir porcentajes
    for col in percentage_columns:
        cleaned_df[col] = cleaned_df[col].apply(remove_arrows).apply(normalize_percentage)

    # Convertir volumen y vt a numérico
    cleaned_df['volumen'] = pd.to_numeric(cleaned_df['volumen'], errors='coerce')
    cleaned_df['vt'] = pd.to_numeric(cleaned_df['vt'], errors='coerce')

    return cleaned_df





def percentage_nan(df):
    """
    Calcula el porcentaje de valores NaN en cada columna de un DataFrame.

    :param df: DataFrame de pandas.
    :return: Un DataFrame con el porcentaje de NaN en cada columna.
    """
    # Calcula el total de NaN en cada columna
    total_nan = df.isna().sum()

    # Calcula el porcentaje
    percentage = (total_nan / len(df)) * 100

    return percentage