import requests # importar el modulo  requests que sirve para hacer peticiones a una página web- solicitudes http
from bs4 import BeautifulSoup # importar el modulo BeautifulSoup que sirve para extraer la información de una página web, para analizar los documentos html 
import pandas as pd # importar el modulo pandas que sirve para manipular datos en python -manejar datos en los dataframes

def fetch_page(url): # definir una función que recibe como parametro una url -obtenemos el contenido de la página
    
    response = requests.get(url) # hacer una petición a la url para obtener el contenido de la página get a la url
    if response.status_code == 200: # si la respuesta es 200 significa que la peticion fue exitosa
        return response.content # retornar el contenido de la página    -devolvemos si contenido de la pagina si la solicitud fue exitosa
    else:
        raise Exception(f'Error al solicitar la página {url}') # si la respuesta no es 200 lanzar una excepción con un mensaje de error si solicitud falla
    
    #analizamos los detalles del producto
def parse_product(product): # definir una función que recibe como parametro un producto -extraer la información de un producto
    
    title=product.select_one('a.title').text.strip() # encontramos y obtenemos extraer el titulo del producto
    description=product.find("p",class_='description').text.strip() # encontramos y obtenemos extraer la descripción del producto
    price=product.find("h4",class_='price').text.strip() # encontramos y obtenemos extraer el precio del producto
    return { # retornar un diccionario con la información del producto
        "title":title, # retornar el titulo del producto
        "description":description, # retornar la descripción del producto
        "price":price # retornar el precio del producto
    }

def scrape(url): # definir una función que recibe como parametro una url -extraer la información de los productos de la página web  
    page_content=fetch_page(url) # obtener el contenido de la página web
    soup=BeautifulSoup(page_content,"html.parser") # analizar el contenido de la página web con BeautifulSoup
    #print(soup)
    products=soup.find_all("div",class_:="thumbnail") # encontrar y obtener todos los productos de la página web, encontramos todos los elementos div con la clase thumbnail que representa productos 
   # print(products)
    products_data=[] # inicializar una lista vacía para almacenar la información de los productos
    for product in products: # iterar sobre todos los productos de la página web
        product_info=parse_product(product) # extraer la información de un producto
        products_data.append(product_info) # agregar la información del producto a la lista de productos
    
    #print(products_data)
    return pd.DataFrame(products_data) # retornar un dataframe con la información de los productos  

base_url="https://webscraper.io/test-sites/e-commerce/allinone" # definir la url base de la página web que queremos scrapear
#print(fetch_page(base_url)) # imprimir el contenido de la página web  
#print(scrape(base_url))   # imprimir la información de los productos de la página web
df=scrape(base_url) # extraer la información de los productos de la página web  


#imprimir la información de los productos en un dataframe resultante     con pandas
print(df) # imprimir el dataframe con la información de los productos



df.to_csv("data/raw/products.csv", index=False) # guardar la información de los productos en un archivo csv sin incluir el indice


      

        
        