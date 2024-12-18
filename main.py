# FORMATO
#{"name": "BMA", "buy": 105.22, "sell": 105.59, "timestamp": 1734367423775,"source": "A"}
#{"name": "BMA", "buy": 105.22, "sell": 105.59, "timestamp": 1734367423776,"source": "B"}
# 

import json
import logging

ancho_empresa = 10 ## Para imprimir en formato tabla
ancho_compra = 8
ancho_venta = 8
ancho_source = 5


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

ultimas_cotizaciones = {}
cotizaciones = []


def validar_cotizacion(cotizacion):


    campos = {"name", "buy", "sell", "timestamp", "source"}

    if not all(key in cotizacion for key in campos):
        logging.error(f"Datos incompletos recibidos: {cotizacion}")
        return False

    if not all(cotizacion.values()):
        logging.error(f"Datos vacios recibidos: {cotizacion}")
        return False


    if not isinstance(cotizacion["buy"], (int, float)) or not isinstance(cotizacion["sell"], (int, float)):
        logging.error(f"Valores de 'buy' o 'sell' invalidos: {cotizacion}")
        return False

    if cotizacion["source"] not in {"A", "B"}:
        logging.error(f"Valor de 'source' invalido: {cotizacion}")
        return False


    return True


def imprimir_ultimas_cotizaciones():
    logging.info("Ultimas cotizaciones:")

    for empresa, cotizacion in ultimas_cotizaciones.items():
        logging.info(f"{empresa:<{ancho_empresa}}\tCompra: {cotizacion['buy']:<{ancho_compra}}  Venta: {cotizacion['sell']:<{ancho_venta}}  Source: {cotizacion['source']:<{ancho_source}}")



def procesar_archivo(nombre_archivo):

    try:
        with open(nombre_archivo, 'r') as archivo:
            try:
                cotizaciones_archivo = json.load(archivo)  
                for cotizacion in cotizaciones_archivo:
                    if validar_cotizacion(cotizacion):
                       
                        if cotizacion["name"] not in ultimas_cotizaciones:
                            ultimas_cotizaciones[cotizacion["name"]] = cotizacion
                        else:
                            if ultimas_cotizaciones[cotizacion["name"]]["timestamp"] < cotizacion["timestamp"]:
                                ultimas_cotizaciones[cotizacion["name"]] = cotizacion
                    
                        logging.info(f"Cotizacion de empresa {cotizacion["name"]} procesada")
                        cotizaciones.append(cotizacion)

                logging.info(f"Cotizaciones del archivo {nombre_archivo} procesadas.")
                imprimir_ultimas_cotizaciones()

            except json.JSONDecodeError:
                logging.error(f"El archivo {nombre_archivo} no contiene un JSON valido.")

    except FileNotFoundError:
        logging.error(f"El archivo {nombre_archivo} no fue encontrado.")



            

if __name__ == "__main__":

    while True:
        try:
            archivo = input("Ingrese el nombre del archivo a procesar (o 'q' para terminar): ").strip()
            if archivo.lower() == 'q':
                logging.info("Ejecucion terminada por el usuario.")
                break
            procesar_archivo(archivo)
        except KeyboardInterrupt:
            logging.info("Ejecucion interrumpida por el usuario.")
            break