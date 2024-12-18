# FORMATO
#{"name": "BMA", "buy": 105.22, "sell": 105.59, "timestamp": 1734367423775,"source": "A"}
#{"name": "BMA", "buy": 105.22, "sell": 105.59, "timestamp": 1734367423776,"source": "B"}
# 





import json
import logging

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


def procesar_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as f:
        for linea in f:
            try:
                cotizacion = json.loads(linea)

                if validar_cotizacion(cotizacion):
                    if cotizacion["name"] not in ultimas_cotizaciones:
                        ultimas_cotizaciones[cotizacion["name"]] = cotizacion
                    else:
                        if ultimas_cotizaciones[cotizacion["name"]]["timestamp"] < cotizacion["timestamp"]:
                            ultimas_cotizaciones[cotizacion["name"]] = cotizacion
                    
                    cotizaciones.append(cotizacion)
            except json.JSONDecodeError:
                logging.error(f"Error al procesar la línea: {linea}")
            
    logging.info("Cotizaciones procesadas correctamente.")
    logging.info("Cotizaciones: %s", ultimas_cotizaciones)
                    

if __name__ == "__main__":

    while True:
        try:
            input = input("Ingrese el nombre del archivo a procesar (o 'q' para terminar): ").strip()
            if input.lower() == 'q':
                logging.info("Ejecución terminada por el usuario.")
                break
            procesar_archivo(input)
        except KeyboardInterrupt:
            logging.info("Ejecución interrumpida por el usuario.")
            break