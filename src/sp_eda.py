import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analisis_rapido(df):
    """
    Realiza un análisis exploratorio básico de un DataFrame.
    Esta función muestra:
    - Las primeras 5 filas del DataFrame.
    - Información general de la estructura (tipos de datos y valores no nulos).
    - Número total de filas duplicadas.
    - Cantidad de valores nulos por columna.

    Args:
        df (pandas.DataFrame): DataFrame que se desea analizar.

    Retorna: 
        NONE. La función imprime resultados en pantalla.

    """
    print("LAS 5 PRIMERAS COLUMNAS DE DATAFRAME SON:")
    display(df.head())
    print("INFORMACIÓN BÁSICA DE DATAFRAME:")
    display(df.info())
    print(f"EL NÚMERO DE DUPLICADOS ES: {df.duplicated().sum()}")
    print(f"EL NÚMERO DE VALORES NULOS ES:")
    display(df.isna().sum())
    

def num_nulos(df):
    """
    Identifica y ordena las columnas con valores nulos en un DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame a analizar.

    Retorna:
        pandas.Series: Serie con el número de valores nulos por columna,
        filtrada solo a columnas con nulos y ordenada de mayor a menor.
    """
    nulos = df.isnull().sum()
    print("El número de valores nulos:")
    return nulos[nulos > 0].sort_values(ascending=False)


def porcent_nulos(df):
    """
    Genera una tabla con el porcentaje de valores nulos por columna.

    La función:
    - Calcula el porcentaje de valores nulos.
    - Filtra solo las columnas con nulos.
    - Ordena de mayor a menor porcentaje.
    - Redondea los resultados a 2 decimales.

    Args:
        df (pandas.DataFrame): DataFrame a analizar.

    Retorna:
        pandas.DataFrame: Tabla con el porcentaje de valores nulos por columna.
    """
    nulos_porc = df.isnull().mean() * 100
    nulos_tabla = pd.DataFrame(nulos_porc, columns=['nulos%'])

    return (
        nulos_tabla[nulos_tabla['nulos%'] > 0]
        .sort_values(by='nulos%', ascending=False)
        .round(2)
    )

def descriptivo_num(df):
    """
    Muestra un análisis descriptivo básico de las variables numéricas y tipo fechade un DataFrame.

    La función:
    - Identifica las columnas de tipo numérico y fecha.
    - Imprime sus nombres.
    - Presenta las estadísticas descriptivas principales
      (count, mean, std, min, percentiles y max) redondeadas a 2 decimales.

    Args:
        df (pandas.DataFrame): DataFrame que se desea analizar.

    Retorna: 
        NONE. La función muestra resultados en pantalla.
    """
    columnas_num = df.select_dtypes(include=['number','datetime']).columns
    print("Variables numéricas son:\n", columnas_num)

    print("\nLas estadísticas básicas:")
    display(df.describe().round(2).T)


def histplot_num(df):
    """
    Genera histogramas con curva KDE para las variables numéricas y de tipo fecha
    de un DataFrame, excluyendo dentro del bucle las columnas 'contact_month' y
    'contact_year'.

    Args:
        df (pandas.DataFrame): DataFrame que contiene los datos a analizar.

    Retorna: 
        NONE. Muestra en pantalla las gráficas de distribución de cada variable válida.
    """
    columnas_num = df.select_dtypes(include=['number', 'datetime']).columns
    for col in columnas_num:
        # Excluir columnas no deseadas dentro del bucle
        if col in ['contact_month', 'contact_year']:
            continue
        print(f"Distribución de la columna *{col}*")
        plt.figure(figsize=(10, 3))
        sns.histplot(df[col], kde=True)
        plt.xlabel(col)
        plt.ylabel('Frecuencia')
        plt.show()


def boxplots_num(df):
    """
    Genera diagramas de caja (boxplots) para detectar valores atípicos en las
    variables numéricas y de tipo fecha de un DataFrame.
    Se excluyen automáticamente las columnas 'contact_month' y 'contact_year'
    dentro del bucle de iteración.

    Args:
        df (pandas.DataFrame): DataFrame que contiene los datos a analizar.

    Retorna: 
        NONE. Muestra en pantalla los boxplots de cada variable válida.
    """

    columnas_num = df.select_dtypes(include=['number', 'datetime']).columns
    for col in columnas_num:

        # Excluir columnas no deseadas
        if col in ['contact_month', 'contact_year']:
            continue
        plt.figure(figsize=(10, 2))
        sns.boxplot(x=df[col])
        plt.title(f'Análisis de Outliers: {col}')
        plt.xlabel(col)
        plt.ylabel('Frecuencia')
        plt.show()



def descriptivo_cat(df):
    """
    Realiza un análisis descriptivo de las variables categóricas de un DataFrame.

    La función:
    - Identifica las columnas categóricas (tipo 'category', 'object' o 'string').
    - Muestra las estadísticas descriptivas básicas (count, unique, top, freq).
    - Indica el número de valores únicos por variable.
    - Presenta los 10 valores más frecuentes de cada columna, incluyendo valores nulos.

    Args:
        df (pandas.DataFrame): DataFrame que se desea analizar.

    Retorna: 
        NONE. La función muestra resultados en pantalla.
    """
    columnas_cat = df.select_dtypes(include=['category','object','string']).columns
    print("Variables categoricas son:\n", columnas_cat)

    print("\nLas estadísticas básicas:")
    display(df.describe(include=['category','object','string']).round(2).T)

    for col in columnas_cat:
        print(f"La columna *{col}* tiene {df[col].nunique()} valores unicos:")
        print("Los 10 valores con más frequencia son:")
        display(df[col].value_counts(dropna = False).head(10))

    
def countplot_cat(df, max_categories = 100):
    """
    Muestra gráficos de distribución para columnas categóricas de un DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame de entrada.
        max_categories (int), opcional (default = 100)
            Número máximo de categorías permitido para mostrar el gráfico.
            Si una columna tiene más, se omite la visualización.
    """
    columnas_cat = df.select_dtypes(include=['category','object','string']).columns
    for col in columnas_cat:
        if df[col].nunique() > max_categories:
            print(f"La columna *{col}* tiene demasiadas categorias para visualización")
            continue
        print(f"Distribución de la columna *{col}*")
        plt.figure(figsize = [12,3])
        sns.countplot(x = df[col], order = df[col].value_counts().index)
        plt.tight_layout()
        plt.show()


def correlaciones(df):
    """
    Calcula y muestra la matriz de correlación para variables numéricas.

    Args:
        df (pandas.DataFrame): DataFrame de entrada.
    """
    corr = df.select_dtypes(include="number").corr()
    # Creamos una máscara para el triángulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", center=0)
    plt.title("Matriz de correlación")
    plt.show()