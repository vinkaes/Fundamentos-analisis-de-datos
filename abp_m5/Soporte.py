#METODO IQR
def calcular_IQR(df, columna):
    #Calcular cuartil 1 y 3
    Q1 = df[columna].quantile(0.25)   # Primer cuartil 25%
    Q3 = df[columna].quantile(0.75)   # Tercer cuartil 75%

    #Rango intercuartiles (IQR)
    IQR = Q3 - Q1

    #Límites superior e inferior
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    #DataFrame con las filas que están fuera de los límites
    df_outliers = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
    
    #print(f"Registros con Outliers detectados en {columna} con IQR : {df_outliers.shape[0]}\n Límite inferior: {limite_inferior}   Límite superior: {limite_superior} \n")

    return   df_outliers#, limite_inferior, limite_superior


#METODO Z-score
def calcular_Zscore(df, columna):
    from scipy.stats import zscore
    df_zscore=df.copy()
    df_zscore["z_score"] = zscore(df[columna])
    df_outliers = df_zscore[(df_zscore["z_score"] > 3) | (df_zscore["z_score"] < -3)]
    df_SIN_outliers = df_zscore[(df_zscore["z_score"] < 3) & (df_zscore["z_score"] > -3)]
    print(f"Registros con Outliers detectados en {columna} con Z-score: {df_outliers.shape[0]}")
    return df_outliers #,df_SIN_outliers
