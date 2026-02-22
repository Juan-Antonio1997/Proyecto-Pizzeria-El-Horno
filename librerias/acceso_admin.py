#Autor: Juan Antonio Gómez Martín
import logging as log, json, pandas as pd

RUTA_CONFIG = "datos/config.json"
RUTA_DATOS = "datos/pedidos.json"

log.basicConfig(
    level=log.INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        log.FileHandler("logs/ejecucion.log")
    ]
)

def leer_config():
    try:
        with open(RUTA_CONFIG, 'r', encoding="utf-8") as f:
            passwords = json.load(f)
        return passwords
    except FileNotFoundError:
        log.error(f"El fichero \"{RUTA_CONFIG}\" no existe o no fue encontrado")
        return []

def check_password(contra):
    passwords = leer_config()
    if contra in passwords:
        return True
    else:
        return False

def acceso_autorizado():
    log.info("Acceso autorizado al panel de administración")

def acceso_denegado():
    log.error("Se ha cerrado el programa tras 3 intentos fallidos de inicio de sesión")

def line_skip():
    print("")

def leer_datos():
    try:
        with open(RUTA_DATOS, "r", encoding="utf-8") as f:
            lista_tickets = json.load(f)
        return lista_tickets
    except FileNotFoundError:
        log.error(f"El fichero \"{RUTA_DATOS}\" no existe o no fue encontrado")
        return "FileNotFound"

def total_recaudado(lista_datos):
    datos = pd.DataFrame(lista_datos)
    return round(datos["total_final"].sum(), 2)

def media_gasto(lista_datos):
    datos = pd.DataFrame(lista_datos)
    return round(datos["total_final"].mean(), 2)