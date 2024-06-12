import pandas as pd # importamos la libreía pandas para trabajar con dataframes de datos para manejar y analizar datos
import os # importamos la librería os para trabajar con el sistema operativo
from ..decorators.decorators import timeit, logit # Importamos los decoradores personalizados timeit y logit
#esos modulos son internos no hace falta descargar

@logit # aplicamos el decorador logit a la función load_data
@timeit # medimos el tiempo de ejecucion de la funcion
def load_data(data_path):# definimos la función load_data que recibe como parámetro la ruta del archivo
    
    
    if data_path.endswith('.csv'): # si la ruta del archivo termina con .csv es decir products.csv
        df=pd.read_csv(data_path)# leemos el archivo csv y lo guardamos en la variable df
    elif data_path.endswith('.xlsx'):# si la ruta del archivo termina con .xlsx es decir products.xlsx
        df=pd.read_excel(data_path) # leemos el archivo excel y lo guardamos en la variable df
    else:
        raise ValueError('Unsuppordte file format, only .csv and .xlsx files are supported')# si no es un archivo .csv o .xlsx lanzamos un error
    print('Data loaded correctly')# imprimimos un mensaje de que los datos se cargaron correctamente
    return df # retornamos el dataframe df dataframe con los datos cargados
#print(load_data("data/raw/products.csv"))# llamamos a la función load_data con la ruta del archivo products.csv
@logit #   aplicamos el decorador logit a la función 
@timeit # medimos el tiempo de ejecucion de la funcion
def clean_data(df):# definimos la función clean_data que recibe como parámetro el dataframe df un dataframe es una estructura de datos que se usa para almacenar datos en forma de tabla
    #limpiamos los datos
    df["price"]=df["price"].replace(r"[\$,]","", regex=True).astype(float)# eliminamos el signo de dolar y las comas y convertimos el precio a float - r viene de row 
    #Antes era $2,222.99 y ahora es 2222.99 
    print("Data cleaned correctly")# imprimimos un mensaje de que los datos se limpiaron correctamente
    return df # retornamos el dataframe df con los datos limpiados es decir sin signo de dolar y sin comas
@logit # aplicamos el decorador logit a la función 
@timeit # medimos el tiempo de ejecucion de la funcion
def analyze_data(df):# definimos la función analyze_data que recibe como parámetro el dataframe df
    print("Basic Data Analysis:")# imprimimos un mensaje de que los datos se analizaron correctamente
    print(df.describe())# imprimimos un resumen estadístico de los datos del dataframe df
    print("\nProducts with highest prices:")# imprimimos un mensaje en un encabezado de los productos con los precios más altos
    highestPrices= df.nlargest(6,"price")# llamamos a la función highest_prices con el dataframe df como parámetro 
    print(highestPrices)# imprimimos los 6 productos con los precios más altos
    return highestPrices# retornamos los 6 productos con los precios más altos
@logit # aplicamos el decorador logit a la función 
@timeit # medimos el tiempo de ejecucion de la funcion 
def save_clean_data(df, outputh_path):# definimos la función save_clean_data que recibe como parámetro el dataframe df y la ruta de salida output_path
    
    if outputh_path.endswith('.csv'): # si la ruta de salida termina con .csv es decir products.csv
        df.to_csv(outputh_path, index=False)# guardamos el dataframe df es decir los datos en un archivo csv
    elif outputh_path.endswith('.xlsx'):# si la ruta de salida termina con .xlsx es decir products.xlsx
        df.to_excel(outputh_path, index=False)
    else:    
        raise ValueError('Unsuppordte file format, only .csv and .xlsx files are supported')# si no es un archivo .csv o .xlsx lanzamos un error
    print(f"Data saved correctly in {outputh_path}")# imprimimos un mensaje de que los datos se guardaron correctamente en la ruta de salida

if __name__=="__main__":# si el archivo se ejecuta como un script, permitimos que el script solo se ejecute en este archivo
    data_path="data/raw/products.csv"# definimos la ruta del archivo de entrada, definimos la ruta del archivo sin procesar        
    output_path="data/processed/cleaned_products.csv"# definimos la ruta del archivo de salida
    
    df=load_data(data_path)# llamamos a la función load_data con la ruta del archivo de entrada, cargamos datos de un archivo específico    
    df=clean_data(df)# llamamos a la función clean_data con el dataframe df, limpiamos los datos cargados
    df=analyze_data(df)# llamamos a la función analyze_data con el dataframe df, análisis básico de la data
    os.makedirs("data/processed", exist_ok=True)# creamos el directorio o carpeta processed de salida si no existe
    save_clean_data(df, output_path)# llamamos a la función save_clean_data con el dataframe df y la ruta de salida, guardamos los datos limpiados en un archivo específico 
    
    