""" *****************************************************************************
    *****************Análisis Exploratorio de Datos - ComercioYA*****************
    *****************************************************************************"""


#Importar librerías
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import Soporte as aux


#Carga el dataset y retorna un DataFrame
def cargar_datos(path):
    return pd.read_csv(path)

#IDA
def limpiar_datos(df):

    #Rellenar datos nulos edad cliente
    df_outliers=aux.calcular_IQR(df, "edad_cliente")
    if len(df_outliers) == 0:
        df["edad_cliente"] = df["edad_cliente"].fillna(round(df["edad_cliente"].mean()))
    else:
        df["edad_cliente"] = df["edad_cliente"].fillna(round(df["edad_cliente"].median()))

    #Rellenar datos nulos correo cliente
    df["correo_cliente"]= df["correo_cliente"].fillna("Sin correo electrónico")
    
    #Remplazar valores: "RM" por "Región Metropolitana"
    df["region"] = df["region"].str.replace(r"RM" , "Región Metropolitana",regex=True)

    #Remplazar valores: "Masculino" por "M"
    df["genero_cliente"] = df["genero_cliente"].str.replace(r"Masculino" , "M",regex=True)

    #Remplazar valores: "Femenino" por "F"
    df["genero_cliente"] = df["genero_cliente"].str.replace(r"Femenino" , "F",regex=True)

    #Remplazar valores: "Web" por "Página Web"
    df["canales_venta"] = df["canales_venta"].replace({"Web" : "Página Web"})

    return df

#Crear dummies
def crear_dummies(df):
    # Creación columna cuantitativa de genero_cliente donde F es 1 y M es 0
    df["genero_cliente_F"] = np.where(df["genero_cliente"]== "F", 1 , 0)

    # Creación columna cuantitativa de canales_venta donde Página Web es 1 y App es 0
    df["canal_web"]= np.where(df["canales_venta"]== "Página Web", 1 , 0)

    # Creación columna cuantitativa de categoria_producto donde Tecnología es 1 y ElectroHogar es 0
    df["categoria_Tecno"]= np.where(df["categoria_producto"]== "Tecnología", 1 , 0)   

    return df

#EDA:

# Matriz correlación
def matriz_correlacion(df):
    df_num = df.select_dtypes(include=["float64", "int32", "int64"]).drop(columns=["id_transaccion","id_producto"])
    corr = df_num.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Matriz de correlación")
    plt.show()
    return corr

# Regresión lineal simple
def modelo_reg_simple(df, columna_x, columna_y):
    x=sm.add_constant(df[columna_x])
    y = df[columna_y]
    modelo_simple = sm.OLS(y,x).fit()
    return modelo_simple, x, y

# Regresión lineal múltiple de 3 variables independientes
def modelo_reg_multiple(df, columna_x1,columna_x2,columna_x3, columna_y):
    x=sm.add_constant(df[[columna_x1,columna_x2,columna_x3]])
    y = df[columna_y]
    modelo_multiple = sm.OLS(y,x).fit()
    return modelo_multiple, x, y


#Calcular métritas R², MSE, MAE
def  metricas(modelo, x, y):
    predicciones = modelo.predict(x)
    print("Métricas de modelo:")
    print("MAE: ", mean_absolute_error(y, predicciones))
    print("MSE: ", mean_squared_error(y, predicciones))
    print("R2: ", r2_score(y, predicciones))
    return

#Graficar regresión
def grafico_regresion(df,columna_x, columna_y):
    sns.regplot(x=columna_x, y=columna_y , data=df )
    plt.title(f"Relación entre {columna_x} y {columna_y}", fontsize=15)
    #plt.savefig("GráficoRelaciónModelo.png", dpi=300, bbox_inches='tight')
    return plt.show()

#Histograma
def grafico_histograma(df,columna):
    plt.figure( figsize=(10, 5))
    plt.hist( df[columna], bins=8, edgecolor="black" )
    plt.title(f"Distribución de {columna}", fontsize=25)
    plt.xlabel(f"{columna}", fontsize=20)
    plt.ylabel("Frecuencia", fontsize=20)
    plt.tick_params(axis="both", labelsize=15)
    #plt.savefig("GráficoHistograma.png", dpi=300, bbox_inches='tight')
    return plt.show()

# Boxplot
def grafico_boxplot(df,columna):
    plt.figure( figsize=(10, 5) )
    plt.boxplot( df[columna])
    plt.ticklabel_format(style="plain", axis="y")
    plt.title(f"Boxplot de {columna}", fontsize=25)
    plt.ylabel(f"{columna}", fontsize=20)
    plt.tick_params(axis="both", labelsize=15)
    #plt.savefig("GráficoBoxplot.png", dpi=300, bbox_inches='tight')
    return plt.show()



"""*****************Ejecución de flujo*****************"""


df= cargar_datos("abp_m5/Dataset_ComercioYA.csv")
df_limpio=limpiar_datos(df)
df_nuevo= crear_dummies(df_limpio)
Mcorr=matriz_correlacion(df_nuevo)

g_hist=grafico_histograma(df_nuevo,"edad_cliente")
g_caja=grafico_boxplot(df_nuevo,"edad_cliente")

#Modelo simple
modelo_S, x1, y1 =modelo_reg_simple(df_nuevo,"visitas_previas","satisfaccion")
print(modelo_S.summary())
metrica_er=metricas(modelo_S, x1, y1)
g1= grafico_regresion(df_nuevo,"visitas_previas","satisfaccion")


#Modelo multiple
modelo_M, x2, y2=modelo_reg_multiple(df_nuevo,"visitas_previas","edad_cliente", "devolucion","satisfaccion")
print(modelo_M.summary())

