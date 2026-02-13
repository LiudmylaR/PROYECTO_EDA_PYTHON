:chart_with_downwards_trend: Proyecto EDA con Python

:ledger: Descripción del Proyecto\
Este proyecto consiste en un análisis exploratorio de los datos de campañas de marketing de una entidad bancaria, integrando información demográfica, financiera y macroeconómica de los clientes, para identificar patrones y factores que influyen en la suscripción de depósitos a plazo.

:pushpin: Objetivos del Proyecto\
    Objetivo general:\
Realizar un análisis exploratorio de los datos de campañas de marketing de una entidad bancaria, integrando información comercial y demográfica de los clientes, para comprender la estructura de los datos, evaluar su calidad e identificar patrones asociados a la suscripción de depósitos a plazo.

    Objetivos específicos:
* Analizar la calidad de los datos, detectando valores nulos, inconsistencias y posibles outliers.
* Describir estadísticamente las principales variables numéricas y categóricas.
* Explorar la distribución y variabilidad de las variables más relevantes.
* Analizar la relación entre las características de los clientes y la variable objetivo (y).
* Visualizar patrones y tendencias relevantes mediante gráficos adecuados.
* Integrar los distintos conjuntos de datos a través del identificador común para enriquecer el análisis.

    Preguntas claves
1. ¿Qué características demográficas y financieras de los clientes están más asociadas a la suscripción del depósito a plazo?
2. ¿Cómo influyen la duración y el número de contactos de la campaña en la probabilidad de éxito?
3. ¿Existen diferencias en la efectividad de la campaña según el canal de contacto y el momento temporal (mes/año)?
4. ¿El historial de contactos y campañas previas mejora o reduce la tasa de suscripción del producto?
5. ¿Cómo influyen las condiciones macroeconómicas en la efectividad de la campaña y en la probabilidad de suscripción del depósito?

:books: Estructura del Proyecto\
:file_folder: PROYECTO_EDA_PYTHON\
├── data/\
│   ├── raw/\
│   │   ├── bank-additional.csv\
│   │   └── customer-details.xlsx\
│   │
│   └── processed/\
│       ├── bank_limpio.csv\
│       ├── consum_limpio.csv\
│       └── unido_eda.csv\
│
├── Notebooks/\
│    ├── 01_analisis_preliminar_bank.ipynb\
│    ├── 02_analisis_preliminar_consum.ipynb\
│    ├── 03_limpieza_transformacion.ipynb\
│    └── 04_eda.ipynb\
│
├── src/\
│    ├── sp_limpieza.py\
│    └── sp_eda.py\
│
├── .gitignore\
│
└── README.md

:nut_and_bolt: Herramientas Utilizadas
- Visual Studio Code
- Python
- Librerias:
    * Pandas
    * Numpy
    * Seaborn
    * Matplotlib

:page_with_curl: Plan de ejecución del Proyecto
- Definir el objetivo: identificar factores que influyen en la suscripción del depósito.
- Cargar e integrar datos: unir archivos por ID y corregir tipos de variables.
- Limpiar datos: tratar nulos, duplicados y columnas irrelevantes.
- EDA descriptivo: estadísticas básicas, distribuciones y correlaciones.
- Análisis del cliente: perfil demográfico y financiero asociado a la suscripción.
- Efectividad de la campaña: duración, número de contactos, canal y tiempo.
- Historial y contexto económico: impacto de campañas previas y variables macro.
- Conclusiones y recomendaciones: factores clave y estrategia óptima de marketing.

:white_check_mark: Informe explicativo del análisis\



:black_nib: Autoría\
Liudmyla Rudenkova\
Noviembre 2025\
[@LiudmylaR](https://github.com/LiudmylaR)