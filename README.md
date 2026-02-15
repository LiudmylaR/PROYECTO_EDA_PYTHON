:chart_with_downwards_trend: Proyecto EDA con Python

:ledger: Descripción del Proyecto\
Este proyecto consiste en un análisis exploratorio de los datos de campañas de marketing de una entidad bancaria portuguesa, integrando información demográfica, financiera y macroeconómica de los clientes, para identificar patrones y factores que influyen en la suscripción de depósitos a plazo.

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

Preguntas claves:
1. ¿Qué características demográficas y financieras de los clientes están más asociadas a la suscripción del depósito a plazo?
2. ¿Cómo influyen la duración y el número de contactos de la campaña en la probabilidad de éxito?
3. ¿Existen diferencias en la efectividad de la campaña según el canal de contacto y el momento temporal (mes/año)?
4. ¿El historial de contactos y campañas previas mejora o reduce la tasa de suscripción del producto?
5. ¿Cómo influyen las condiciones macroeconómicas en la efectividad de la campaña y en la probabilidad de suscripción del depósito?

:books: Estructura del Proyecto\
:file_folder: PROYECTO_EDA_PYTHON\
├── data/\
│   ├── raw/\
│   │       ├── bank-additional.csv\
│   │       └── customer-details.xlsx\
│   └── processed/\
│   │       ├── bank_limpio.csv\
│   │       ├── consum_limpio.csv\
│   │       └── unido_eda.csv\
├── Notebooks/\
│   ├── 01_analisis_preliminar_bank.ipynb\
│   ├── 02_analisis_preliminar_consum.ipynb\
│   ├── 03_limpieza_transformacion.ipynb\
│   └── 04_eda.ipynb\
├── src/\
│   ├── sp_limpieza.py\
│   └── sp_eda.py\
├── .gitignore\
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

:white_check_mark: Informe explicativo del análisis
1. Descripción general del conjunto de datos\
El conjunto de datos, previamente limpiado y preparado para el análisis, contiene:
42 752 registros, cada uno correspondiente a una interacción individual con un cliente durante una campaña de marketing bancario.
28 variables de tipo numérico, categórico y temporal.
Ausencia de valores nulos y duplicados, lo que garantiza consistencia y fiabilidad en el análisis.
Las variables incluyen información demográfica, financiera, de interacción comercial, comportamiento digital, contexto macroeconómico y resultado de conversión, permitiendo un análisis integral de los factores asociados a la suscripción del producto.
2. Análisis de variables numéricas\
**2.1** Variables demográficas y del cliente\
La edad se concentra alrededor de los 40 años, con variabilidad moderada y algunos valores extremos.
El ingreso presenta alta dispersión, evidenciando heterogeneidad socioeconómica.
La mayoría de clientes tiene uno o ningún hijo, mostrando baja variabilidad familiar.
El perfil de clientes es relativamente adulto y diverso en términos económicos, aunque la estructura familiar es bastante homogénea.\
**2.2** Variables de interacción con campañas\
La duración de la llamada muestra fuerte asimetría positiva, con llamadas muy largas asociadas a posibles conversiones.
El número de contactos en la campaña se concentra en valores bajos, aunque existen casos de contacto excesivo que sugieren saturación.
Existen muy pocos contactos previos, y el valor 999 en 'pdays' indica que la mayoría nunca fue contactada antes.
La calidad del contacto parece más relevante que la cantidad, y gran parte de los clientes no tenía historial previo de interacción.\
**2.3** Variables macroeconómicas\
La variación del empleo presenta valores positivos y negativos, reflejando ciclos económicos.
El índice de precios muestra baja dispersión, indicando estabilidad inflacionaria.
La confianza del consumidor es negativa y variable, señalando percepción económica moderada o baja.
El Euríbor varía ampliamente, reflejando cambios importantes en tasas de interés.
El número de empleados es relativamente estable.
El contexto económico fluctúa, especialmente en tasas de interés y empleo, lo que puede influir en decisiones de ahorro.\
**2.4** Variables temporales y digitales\
Las interacciones abarcan 2015-2019, mientras que la antigüedad de clientes se sitúa en 2012-2014.
Las visitas web mensuales presentan distribución casi simétrica, indicando uso digital frecuente.\
**2.5** Variable de conversión\
Solo ≈11 % de los clientes suscriben el producto.
La distribución está fuertemente sesgada hacia la respuesta negativa.
3. Análisis de variables categóricas\
Predominan perfiles administrativos, casados y con educación universitaria.
Más de la mitad posee hipoteca, pero pocos tienen otros préstamos.
El canal principal de contacto es teléfono móvil.
La mayoría no tuvo campañas previas y no suscribe el producto.
El dataset refleja una población bancaria estable, con baja conversión histórica.
4. Correlaciones con la suscripción\
**4.1** Factores positivos\
Duración de la llamada → principal predictor del éxito.
Contactos previos → aumentan la probabilidad de conversión.
**4.2** Factores negativos\
Variables económicas (empleo, Euríbor, variación del empleo) → reducen la probabilidad de suscripción cuando son altas.
Tiempo desde último contacto → menor probabilidad si nunca se contactó.
**4.3** Factores sin influencia\
Ingresos, hijos, visitas web → sin relación lineal con la conversión.
Edad y número de contactos → efecto muy débil.
5. Resultados por bloques de negocio\
**5.1** Perfil demográfico y financiero\
Mayor conversión en estudiantes, jubilados y solteros.
La hipoteca aumenta ligeramente la suscripción.
Ingresos y edad no son determinantes.
**5.2** Duración e intensidad de la campaña\
Conversaciones más largas → mayor éxito.
Más contactos → menor efectividad (rendimientos decrecientes).
La calidad del contacto supera a la cantidad.
**5.3** Canal y momento temporal\
El canal móvil es más efectivo que el fijo.
Pico de éxito en 2016 y variaciones leves posteriores.
Estacionalidad clara, con máximo en octubre.
**5.4** Historial de campañas previas\
Éxito previo → mayor probabilidad de nueva suscripción.
Demasiados contactos previos no mejoran resultados.
La experiencia previa influye positivamente.
**5.5** Contexto macroeconómico\
La suscripción aumenta cuando el entorno económico es incierto o débil.
Los clientes buscan seguridad y ahorro en periodos desfavorables.
6. Conclusiones generales
- La duración de la llamada es el factor más determinante del éxito.
- La experiencia previa positiva con el cliente incrementa la conversión.
- Exceso de contactos reduce la efectividad, evidenciando saturación comercial.
- El canal móvil y ciertos momentos del año mejoran resultados.
- Las condiciones macroeconómicas adversas favorecen la contratación de productos de ahorro.
- Las variables demográficas clásicas tienen impacto limitado.
7. Recomendaciones de negocio
- Priorizar llamadas de mayor calidad y duración.
- Focalizar campañas en clientes con historial positivo.
- Reducir contactos repetitivos sin respuesta.
- Utilizar principalmente el canal móvil.
- Intensificar campañas en periodos estacionales favorables y en contextos económicos inciertos.

:black_nib: Autoría\
Liudmyla Rudenkova\
Febrero 2026\
[@LiudmylaR](https://github.com/LiudmylaR)