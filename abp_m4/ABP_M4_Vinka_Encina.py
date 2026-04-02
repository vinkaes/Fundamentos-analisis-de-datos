#Importar librerias
import numpy as np
import pandas as pd 


"""_____________________________________________________

                Lección 1 - La librería numpy
   _____________________________________________________"""

# * Crear base de datos de clientes y transacciones

# Nombres de clientes
nombres = ["Emma", "Mateo", "Isabella", "Facundo", "Sofía", "Benjamín", "Emilia", "Gaspar",
           "Julieta", "Lucas", "Aurora", "Thiago", "Mía", "Liam", "Trinidad", "Santiago",
           "Josefa","Vicente", "Isidora","Noah","Ariel", "Alex", "Andrea"]

# Nombres de clientes
apellidos = ["González", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto", "Contreras", "Silva",
             "Martínez", "Sepúlveda", "Morales", "Rodríguez", "López", "Araya", "Fuentes",
             "Hernández", "Torres", "Espinoza", "Flores", "Castillo","Santibáñez","Arias",
             "Palacios"]

#Regiones de clientes
regiones = ["Antofagasta", "Atacama", "Coquimbo", "Valparaíso", "Región Metropolitana","RM",
            "Maule", "Biobío", "La Araucanía", "Los Lagos"]
pesos_regiones = [0.05, 0.05, 0.05, 0.15, 0.2, 0.2, 0.05, 0.15, 0.05, 0.05]

# Géneros del cliente
generos = ["M", "F", "Masculino","Femenino"]

#IDs clientes
ids_cliente = np.arange(1, 51)

# Canal de venta
canales_venta = ["Página Web","Web", "App"]

#Fecha de venta
fecha_inicio = np.datetime64('2025-01-01')
fecha_fin = np.datetime64('2025-12-31')
dias_totales = (fecha_fin - fecha_inicio).astype(int)
dias_aleatorios = np.random.randint(0, dias_totales, size=100)
fechas_aleatorias = fecha_inicio + dias_aleatorios.astype('timedelta64[D]')
#print(fechas_aleatorias)

# Generar función para base de datos de clientes y transacciones:
def datos_ventas(inicio,fin):
    transacciones = []
    for i in range(inicio, fin + 1):
      id_transaccion = i
      fecha_venta = np.random.choice(fechas_aleatorias)
      id_cliente = f"CLTE_{np.random.choice(ids_cliente)}"
      nombre = np.random.choice(nombres)
      apellido = np.random.choice(apellidos)
      email = f"cliente_{i}@gmail.com"
      genero = np.random.choice(generos)
      region = np.random.choice(regiones, p=np.array(pesos_regiones)/sum(pesos_regiones))
      edad = np.random.randint(18, 70)
      canal_ventas =np.random.choice(canales_venta)
      cantidad = np.random.randint(1, 5)
      precio = np.random.randint(10_000, 1_000_000)
      id_producto = np.random.randint(1, 7)
      
      transacciones.append([
          id_transaccion,fecha_venta,id_cliente, nombre, apellido, email,genero,edad, region,
          canal_ventas, id_producto,cantidad,precio])

    return transacciones


# *Creación de base de datos de clientes y transacciones para Lección 2:

  #Elaboración de base
caso_base= datos_ventas(1,50)

  #Guardar dataset en formato .npy
np.save("caso_base.npy", np.array(caso_base, dtype=object))


# *Creación de base de datos de clientes y transacciones para Lección 3 con duplicados,
#  campos nulos y outliers:

  #Elaboración de base
caso_especiales= datos_ventas(51,150)

  #Conversión a dataframe para manipulación de casos especiales
df_ventas = pd.DataFrame(caso_especiales, columns=[
    "id_transacción", "fecha_venta", "id_cliente", "nombre_cliente", "apellido_cliente",
    "correo_cliente", "genero_cliente", "edad_cliente", "region","canal_venta","id_producto",
    "cantidad", "precio_unitario"])

  # Agregar datos nulos
df_ventas.loc[np.random.choice(df_ventas.index, 10), "edad_cliente"] = np.nan
df_ventas.loc[np.random.choice(df_ventas.index, 20), "correo_cliente"] = np.nan

  # Agregar datos duplicados
df_ventas = pd.concat([df_ventas, df_ventas.sample(15)])

  #Generación de copia
df_ventas2=df_ventas.copy()

  # Agregar datos outliers
df_ventas2.loc[np.random.choice(df_ventas2.index, 5), "precio_unitario"] = np.random.randint(2_000_000, 3_000_000)

  #Generar archivo
#df_ventas2.to_csv("ventas_ecommerce_ce.csv", index=False)
df_ventas2.to_excel("ventas_ecommerce_ce.xlsx", index=False, sheet_name="Ventas")

# * Archivo para lección 3 formato excel
df_productos = pd.DataFrame([
      [1, "Smartphone", "Tecnología"],
      [2, "Audífonos", "Tecnología"],
      [3, "Notebook", "Tecnología"],
      [4, "Tablet", "Tecnología"],
      [5, "Smart TV", "Tecnología"],
      [6, "Parlante", "Tecnología"]
  ], columns=["id_producto", "nombre_producto", "categoria_producto"])

df_productos.to_excel("productos.xlsx", index=False, sheet_name="Productos")

"""_____________________________________________________

                Lección 2 - La librería pandas
   _____________________________________________________"""

print("\033[93m*\033[0m"*137)
print("\n\033[93m                                                 Lección 2 - La librería pandas \033[0m\n")
print("\033[93m*\033[0m"*137)

  #Lectura de archivo .npy
datos_caso_base = np.load("caso_base.npy", allow_pickle=True)

  #Transformación a dataframe
df_caso_base = pd.DataFrame(datos_caso_base, columns=[
    "id_transacción", "fecha_venta", "id_cliente", "nombre_cliente", "apellido_cliente",
    "correo_cliente", "genero_cliente", "edad_cliente", "region","canal_venta","id_producto",
    "cantidad", "precio_unitario"])

  #Visualizar primeras filas
print(df_caso_base.head())

  #Visualizar últimas filas
print(df_caso_base.tail())

  #Información de los datos del dataframe
print("\n \033[1mInformación sobre df_caso_base:\033[0m ")
print( df_caso_base.info() )

  #Modificación de tipo de dato para estadísticas descriptivas
df_caso_base["fecha_venta"] = pd.to_datetime(df_caso_base["fecha_venta"]).dt.floor("D")
df_caso_base["edad_cliente"] = df_caso_base["edad_cliente"].astype(int)
df_caso_base["cantidad"] = df_caso_base["cantidad"].astype(int)
df_caso_base["precio_unitario"] = df_caso_base["precio_unitario"].astype(int)
df_caso_base["id_producto"] = df_caso_base["id_producto"].astype(int)

  #Obtener estadísticas descriptivas
print("\n \033[1mEstadísticas descriptivas de df_caso_base:\033[0m ")
print(df_caso_base.describe())

  #Aplicar filtros condicionales: Ver cuántos registros se tienen por id_producto 
  #  superior al promedio de cantidad
print("\n\033[1mRegistros id_producto igual a 1 con cantidad superior al promedio\033[0m \n",
      df_caso_base[(df_caso_base["id_producto"]==1) & (df_caso_base["cantidad"]> df_caso_base["cantidad"].mean())],"\n")
print("\033[1mRegistros id_producto igual a 2 con cantidad superior al promedio\033[0m \n",
      df_caso_base[(df_caso_base["id_producto"]==2) & (df_caso_base["cantidad"]> df_caso_base["cantidad"].mean())],"\n")
print("\033[1mRegistros id_producto igual a 3 con cantidad superior al promedio\033[0m \n",
      df_caso_base[(df_caso_base["id_producto"]==3) & (df_caso_base["cantidad"]> df_caso_base["cantidad"].mean())],"\n")
print("\033[1mRegistros id_producto igual a 4 con cantidad superior al promedio\033[0m \n",
      df_caso_base[(df_caso_base["id_producto"]==4) & (df_caso_base["cantidad"]> df_caso_base["cantidad"].mean())],"\n")
print("\033[1mRegistros id_producto igual a 5 con cantidad superior al promedio\033[0m \n",
      df_caso_base[(df_caso_base["id_producto"]==5) & (df_caso_base["cantidad"]> df_caso_base["cantidad"].mean())],"\n")
print("\033[1mRegistros id_producto igual a 6 con cantidad superior al promedio\033[0m \n",
      df_caso_base[(df_caso_base["id_producto"]==6) & (df_caso_base["cantidad"]> df_caso_base["cantidad"].mean())],"\n")

  #Aplicar filtros condicionales: Ver cuántos registros se tienen por precio_unitario 
  #  igual a máximo, mínimo y superior promedio
print("\033[1mRegistros con precio_unitario como máximo\033[0m \n",
      df_caso_base[(df_caso_base["precio_unitario"]== df_caso_base["precio_unitario"].max())],"\n")
print("\033[1mRegistros con precio_unitario como mínimo\033[0m \n",
      df_caso_base[(df_caso_base["precio_unitario"]== df_caso_base["precio_unitario"].min())],"\n")
print("\033[1mRegistros con precio_unitario superior al promedio\033[0m \n",
      df_caso_base[(df_caso_base["precio_unitario"]> df_caso_base["precio_unitario"].mean())],"\n")

  #Guardar el DataFrame preliminar en un archivo CSV
df_caso_base.to_csv("ventas_ecommerce_caso_base.csv", index=False)



"""_______________________________________________________________________

                Lección 3 - Obtención de datos desde archivos             
   _______________________________________________________________________"""

print("\033[93m*\033[0m"*137)
print("\n\033[93m                                                 Lección 3 - Obtención de datos desde archivos \033[0m\n")
print("\033[93m*\033[0m"*137)

  #Leer base de Lección 2
ventas_base = pd.read_csv("ventas_ecommerce_caso_base.csv")
print(f"\033[1mMuestra de datos dataframe ventas_base\033[0m\n {ventas_base.head()}")

  #Leer base de formato Excel para concatenar
casos_especiales= pd.read_excel("ventas_ecommerce_ce.xlsx",engine="openpyxl")
print(f"\n\033[1mDatos dataframe casos_especiales\033[0m\n {casos_especiales}")
  
  #Leer base de formato Excel para merge
productos= pd.read_excel("productos.xlsx",engine="openpyxl")
print(f"\n\033[1mDatos dataframe productos\033[0m\n {productos}")

  #Realizar concatenación
base_concatenado = pd.concat([ventas_base,casos_especiales])
print(f"\n\033[1mDatos dataframe base_concatenado\033[0m\n {base_concatenado}")

  #Realizar join
base_left_join = pd.merge(base_concatenado,productos, on= "id_producto", how="left")
print(f"\n\033[1mDatos dataframe base_left_join\033[0m\n {base_left_join}")

  #Modificar tipo de valor de fecha_venta
base_left_join["fecha_venta"] = pd.to_datetime(base_left_join["fecha_venta"]).dt.floor("D")
base_left_join["precio_unitario"] = base_left_join["precio_unitario"].astype(int)

  #Guardar dataframe consolidado
base_left_join.to_csv("ventas_ecommerce_consolidado.csv", index=False)

"""_______________________________________________________________________

                Lección 4 - Manejo de valores perdidos y outliers             
   _______________________________________________________________________"""

print("\033[93m*\033[0m"*137)
print("\n\033[93m                                                 Lección 4 - Manejo de valores perdidos y outliers \033[0m\n")
print("\033[93m*\033[0m"*137)

# Generación de copia de DataFrame
df_base=base_left_join.copy()

  #Identificar nulos
print("\n\033[1m Identificación de valores nulos:\033[0m\n", df_base.isnull().sum())

  #Imputación con una nueva categoría en correo_cliente
df_base["correo_cliente"]=df_base["correo_cliente"].fillna("Sin correo electrónico")

  #Comprobación de imputación en correo_cliente
print("\n\033[1m Identificación de valores nulos tras imputación correo_cliente:\033[0m\n",df_base.isnull().sum())


  #Identificación de outliers para edad_cliente:
    #Calcular cuartil 1 y 3
Q1 = df_base["edad_cliente"].quantile(0.25)   # Primer cuartil 25%
Q3 = df_base["edad_cliente"].quantile(0.75)   # Tercer cuartil 75%

    #Rango intercuartiles (IQR)
IQR = Q3 - Q1

    #Límites superior e inferior
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

    #DataFrame con las filas que están fuera de los límites
df_outliers = df_base[(df_base["edad_cliente"] < limite_inferior) | (df_base["edad_cliente"] > limite_superior)]

  #Imputación con media o mediana según existencia de outliers en edad_cliente
if len(df_outliers) == 0:
    df_base["edad_cliente"] = df_base["edad_cliente"].fillna(round(df_base["edad_cliente"].mean()))

else:
    df_base["edad_cliente"] = df_base["edad_cliente"].fillna(round(df_base["edad_cliente"].median()))

  #Comprobación de imputación en edad_cliente
print("\n\033[1m Identificación de valores nulos tras imputación edad_cliente:\033[0m\n",df_base.isnull().sum())


"""--------------------------------------------------------------------"""

  #Obtener estadísticas descriptivas tras las imputaciones
pd.set_option('display.max_columns', None)
with pd.option_context("display.float_format", "{:.2f}".format):
    print(f"\n\033[1m Estadísticas descriptivas tras imputaciones:\033[0m\n {df_base.describe()}")

 #Identificación de outliers para precio_unitario:

 #METODO IQR

    #Calcular cuartil 1 y 3
Q1 = df_base["precio_unitario"].quantile(0.25)   # Primer cuartil 25%
Q3 = df_base["precio_unitario"].quantile(0.75)   # Tercer cuartil 75%

    #Rango intercuartiles (IQR)
IQR = Q3 - Q1

    #Límites superior e inferior
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

    #DataFrame con las filas que están fuera de los límites
df_outliers_IQR= df_base[(df_base["precio_unitario"] < limite_inferior) | (df_base["precio_unitario"] > limite_superior)]
print(f"\n\033[1m Outliers IQR encontrados:\033[0m \n {df_outliers_IQR}")


  #METODO Z-score
from scipy.stats import zscore
df_base["z_score"] = zscore(df_base["precio_unitario"])
df_outliers_zscore = df_base[(df_base["z_score"] > 3) | (df_base["z_score"] < -3)]
print(f"\n\033[1m Outliers Z-score encontrados:\033[0m \n {df_outliers_zscore}")

#Eliminación de outliers
df_base_sin_outliers = df_base[(df_base["precio_unitario"] > limite_inferior) & (df_base["precio_unitario"] < limite_superior)]

print(f"\n\033[1mTotal registros con outliers:\033[0m {df_base.shape}")
print(f"\033[1mTotal registros sin outliers:\033[0m {df_base_sin_outliers.shape}")

  #Guardar dataframe limpio
df_base_sin_outliers.to_csv("ventas_ecommerce_limpio.csv", index=False)

"""_______________________________________________________________________

                          Lección 5 - DATA WRANGLING             
   _______________________________________________________________________"""


print("\033[93m*\033[0m"*137)
print("\n\033[93m                                                 Lección 5 - DATA WRANGLING   \033[0m\n")
print("\033[93m*\033[0m"*137)

# Generar copia tras imputación de nulos y eliminación de outliers
df_base_limpio = df_base_sin_outliers.copy()

#Identificar duplicados
duplicados = df_base_limpio.duplicated()
print(f"\n\033[1mNúmero de duplicados identificados:\033[0m {duplicados.sum()}")

#Eliminar duplicados
df_base_sin_dup = df_base_limpio.drop_duplicates()
print(f"\033[1mTotal registros sin duplicados:\033[0m {df_base_sin_dup.shape}")

#Verificar tipos de datos
print("\n \033[1mVista de tipos de datos:\033[0m\n")
print(df_base_sin_dup.info())

#Transformar tipos de datos
df_base_sin_dup["edad_cliente"] = df_base_sin_dup["edad_cliente"].astype(int)

#Confirmación tipos de datos
print("\n \033[1mVista después de transformación de tipos de datos:\033[0m\n")
print(df_base_sin_dup.info())


#Remplazar valores: "RM" por "Región Metropolitana"
df_base_sin_dup["region"] = df_base_sin_dup["region"].str.replace(r"RM" , "Región Metropolitana",regex=True)

#Remplazar valores: "Masculino" por "M"
df_base_sin_dup["genero_cliente"] = df_base_sin_dup["genero_cliente"].str.replace(r"Masculino" , "M",regex=True)

#Remplazar valores: "Femenino" por "F"
df_base_sin_dup["genero_cliente"] = df_base_sin_dup["genero_cliente"].str.replace(r"Femenino" , "F",regex=True)

#Remplazar valores: "Web" por "Página Web"
df_base_sin_dup["canal_venta"] = df_base_sin_dup["canal_venta"].replace({"Web" : "Página Web"})

#Creación de columna iva del precio_unitario con apply y lambda
df_base_sin_dup["iva_precio"] = df_base_sin_dup["precio_unitario"].apply(lambda x: round((x * 0.19)/1.19))

#Creación de columna ingreso_venta
df_base_sin_dup["ingreso_venta"] = df_base_sin_dup["precio_unitario"] * df_base_sin_dup["cantidad"]

#Creación de columna zona con map
mapeo={"Antofagasta":"Norte","Atacama":"Norte","Coquimbo":"Norte",
      "Valparaíso":"Central","Región Metropolitana":"Central","Maule":"Central",
      "Biobío":"Sur","La Araucanía":"Sur", "Los Lagos":"Sur"}

df_base_sin_dup["zona"] = df_base_sin_dup["region"].map(mapeo)

#Discretización de edad_cliente
bins=[17,30,40,60,70]
etiquetas=["Joven","Adulto Joven","Adulto","Adulto mayor"]
df_base_sin_dup["grupo_etario"] = pd.cut(df_base_sin_dup["edad_cliente"],bins=bins,labels=etiquetas)

#Vista de dataframe 
print(f"\n \033[1mVista de dataframe tras data wrangling:\033[0m\n {df_base_sin_dup.head()}")

  #Guardar dataframe optimizado
df_base_sin_dup.to_csv("ventas_ecommerce_optimizado.csv", index=False)


"""_______________________________________________________________________

                Lección 6 - Agrupamiento y pivoteo de datos             
   _______________________________________________________________________"""

print("\033[93m*\033[0m"*137)
print("\n\033[93m                                                 Lección 6 - Agrupamiento y pivoteo de datos   \033[0m\n")
print("\033[93m*\033[0m"*137)

#Generación de copia
df_optimizado= df_base_sin_dup.copy()

#Group by para ver los ingresos de venta por producto
df_group_prod = df_optimizado.groupby("nombre_producto")["ingreso_venta"].sum()
print(f"\n \033[1mAgrupación de ingresos de venta por producto:\033[0m\n {df_group_prod}")

#Group by para ver los ingresos de venta por región
df_group_reg = df_optimizado.groupby("region")["ingreso_venta"].sum()
print(f"\n \033[1mAgrupación de ingresos de venta por región:\033[0m\n {df_group_reg}")

#Pivoteo de región y zona por ingresos de venta
df_sin_dups_pivot = df_optimizado.drop_duplicates(subset=["region", "zona"])
df_pivoteado = df_sin_dups_pivot.pivot(index="region", columns="zona", values="ingreso_venta")
print(f"\n\033[1mTabla pivoteada \033[0m\n{df_pivoteado}")

#Despivoteo de región y zona por ingresos de venta 
df_despivoteado = df_pivoteado.reset_index().melt(id_vars="region",var_name="zona",value_name="ingreso_venta")
print(f"\n\033[1mTabla despivoteada \033[0m\n{df_despivoteado}")

#Generar archivo final
df_optimizado.to_csv("ventas_ecommerce_final.csv", index=False)
df_optimizado.to_excel("ventas_ecommerce_final.xlsx", index=False, sheet_name="Ventas")
print("\n\033[1mSe han creado los archivos Excel y CSV del df_optimizado\033[0m")
print(f"\033[1mCon el tamaño de (filas,columnas): \033[0m {df_optimizado.shape}")

