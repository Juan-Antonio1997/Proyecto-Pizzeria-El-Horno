#Autor: Juan Antonio Gómez Martín
import pandas as pd, logging as log, json, os
from datetime import datetime

RUTA_CSV = "datos/productos.csv"
SEPARADOR = ","
RUTA_DATOS = "datos/pedidos.json"

log.basicConfig(
    level=log.INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        log.FileHandler("logs/ejecucion.log")
    ]
)

def leer_menu():
    productos = pd.read_csv(RUTA_CSV, sep=SEPARADOR)
    return productos

def error_leer_menu():
    log.error(f"El fichero \"{RUTA_CSV}\" no existe o no fue encontrado")
    print(f"Error: El fichero \"{RUTA_CSV}\" no existe o no fue encontrado")

def imprimir_menu(menu):
    print("  Menú Pizzería El Horno   ")
    print("---------------------------")
    print(menu)

def line_skip():
    print("")

def crear_pedido():
    return pd.DataFrame()

def agregar_al_pedido(menu, pedido, id):
    nombre = menu["nombre"].loc[menu["id"] == id]
    precio = menu["precio"].loc[menu["id"] == id]
    datos_producto = {
        "nombre": nombre,
        "precio": precio
    }
    producto = pd.DataFrame(datos_producto)
    return pd.concat([pedido, producto], ignore_index=True)

def calcular_subtotal(pedido):
    if pedido.size != 0:
        return pedido["precio"].sum()
    else:
        return 0

def calcular_iva(subtotal):
    return round(subtotal * 0.1, 2)

def calcular_total_final(subtotal, iva):
    return subtotal + iva

def guardar_pedido(pedido):
    subtotal = calcular_subtotal(pedido)
    iva = calcular_iva(subtotal)
    total_final = calcular_total_final(subtotal, iva)
    pedido_dict = pedido.to_dict(orient="records")
    fechaAct = datetime.now()
    ticket = {
        "fecha": fechaAct.strftime("%d/%m/%Y"),
        "hora": fechaAct.strftime("%H:%M:%S"),
        "pedido": pedido_dict,
        "subtotal": subtotal,
        "iva": iva,
        "total_final": total_final
    }
    if os.path.exists(RUTA_DATOS):
        with open(RUTA_DATOS, "r", encoding="utf-8") as f:
            lista_tickets = json.load(f)
    else:
        lista_tickets = []
    lista_tickets.append(ticket)
    with open(RUTA_DATOS, 'w', encoding="utf-8") as f:
        json.dump(lista_tickets, f, indent=4)
    log.info(f"Venta realizada con éxito. Total: {total_final}€")
    return json.dumps(ticket, indent=4)