import time # Import the time module, para medir el tiempo de ejecución de una función
import logging # Import the logging module, para registrar mensajes de depuración



logging.basicConfig(level=logging.INFO, format="%(asctime)s-%(levelname)s-%(message)s") # Configuración del nivel de depuración

#configuramos el registro de mensajes logging para que muestre mensajes de nivel info y superior
#definimos el formato de los mensajes de registro, incluyendo la marca de tiempo asctime
#el nivel del mensaje levelname y el mensaje message




def timeit(func):# Definimos el decorador timeit
    
    def wrapper(*args, **kwargs):# Definimos la función wrapper que recibe los argumentos de la función decorada
        start_time=time.time()# Guardamos el tiempo de inicio de la ejecución de la función
        result=func(*args, **kwargs)#  Ejecutamos la función decorada
        end_time=time.time() # Guardamos el tiempo de fin de la ejecución de la función
        elapsed_time=end_time-start_time # Calculamos el tiempo de ejecución
        logging.info(f"{func.__name__}ejecutada en: {elapsed_time:.4f} seconds")# Registramos el tiempo de ejecución
        return result # Retornamos el resultado de la función decorada
    return wrapper # Retornamos la función wrapper -devolvemos el decorador

def logit(func):

    def wrapper(*args, **kwargs): # Definimos la función wrapper que recibe los argumentos de la función decorada
        logging.info(f"Empezando a ejecutar la función- corriendo {func.__name__}")#    Registramos el inicio de la ejecución de la función     
        result=func(*args, **kwargs)# Ejecutamos la función decorada
        logging.info(f"Completando-Terminando de ejecutar la función {func.__name__}")# Registramos el fin de la ejecución de la función
        return result # Retornamos el resultado de la función decorada
    return wrapper # Retornamos la función wrapper -devolvemos el decorador

    


    