import pandas as pd
import numpy as np

def imputar_mediana(df, col):
    """
    Rellena los valores nulos de una columna numérica con su mediana.

    Argumentos:
        df (pandas.DataFrame): DataFrame que contiene los datos.
        col (str): Nombre de la columna en la que se imputarán los valores nulos.

    Retorna:
        pandas.DataFrame: DataFrame con los valores nulos de la columna reemplazados por la mediana.
    """
    median_val = df[col].median()
    df[col] = df[col].fillna(median_val)
    return df


def imputar_moda(df, col):
    """
    Rellena los valores nulos de una columna categórica con su moda.

    Argumentos:
    df (pandas.DataFrame): DataFrame que contiene los datos.
    col (str): Nombre de la columna en la que se imputarán los valores nulos.

    Retorna:
        pandas.DataFrame: DataFrame con los valores nulos de la columna reemplazados por la moda.
    """
    mode_val = df[col].mode()[0]
    df[col] = df[col].fillna(mode_val)
    return df


def lower(df, col):
    """
    Convierte a minúsculas los valores de una columna de texto.

    Argumentos:
    df (pandas.DataFrame): DataFrame que contiene los datos.
    col (str): Nombre de la columna a transformar.

    Retorna:
        pandas.DataFrame: DataFrame con la columna en minúsculas.
    """
    df[col] = df[col].str.lower()
    return df


def unknown(df, col, valor='unknown'):
    """
    Rellena los valores nulos de una columna categórica con un valor dado.

    Argumentos:
    df (pandas.DataFrame): DataFrame que contiene los datos.
    col (str): Nombre de la columna a imputar.
    valor (str), opcional (default='unknown'): Valor que se usará para reemplazar los nulos.

    Retorna: 
        pandas.DataFrame: DataFrame con los valores nulos reemplazados.
    """
    df[col] = df[col].fillna(valor)
    return df


def binario_yes_no(df, col):
    """
    Convierte una columna binaria en formato float (1.0 / 0.0)
    a valores categóricos 'yes' y 'no'.

    Argumentos:
    df (pandas.DataFrame): DataFrame que contiene los datos.
    col (str): Nombre de la columna a transformar.

    Retorna:
        pandas.DataFrame: DataFrame con la columna transformada.
    """
    df[col] = df[col].apply(lambda x: 'yes' if x == 1.0 else 'no')
    return df


def coma_float(df, col):
    """
    Convierte una columna de texto con comas decimales (ej. '93,444')
    a tipo numérico float reemplazando la coma por punto.

    Argumentos:
    df (pandas.DataFrame): DataFrame que contiene los datos.
    col (str): Nombre de la columna a convertir.

    Retorna:
        pandas.DataFrame: DataFrame con la columna transformada a float.
    """
    df[col] = df[col].str.replace(',', '.', regex=False).astype(float)
    return df