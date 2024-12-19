# Challenge IEB
## Manejo de Cotizaciones

Para la resolucion del ejercicio se utilizan dos estructuras.


### Cotizaciones
Es una lista, su proposito es almacenar todas las cotizaciones recibidas a lo largo del tiempo. Simula un historial de cotizaciones.

### Ultimas Cotizaciones
Es un diccionario donde la clave es el *name* de la empresa, mientras que los valores son el resto de la informacion de una cotizacion (Precio de compra, venta, timestamp y fuente)

La idea es guardar en este diccionario siempre que el timestamp de la cotizacion recibida sea mas reciente que el que existia previamente en el mismo.


## Input de los datos

El input de las cotizaciones se hace a traves de archivos .json, dentro del archivo hay vectores que contienen la estructura de la cotizacion. La estructura de los mismos en el archivo se ve de esta forma:

```
 {
    "name": "SONY",
    "buy": 29.78,
    "sell": 30.49,
    "timestamp": 1733792855561,
    "source": "B"
  },
```


## Funcionamiento

Al ejecutar el script, se le pedira al usuario que ingrese el nombre del archivo donde estan las cotizaciones.

Tras ingresarlo, se procedera a procesar las mismas, aqui vemos el ejemplo con el set de datos del archivo *datos.json*

![](/imgs/datos1.png)

Notar de que, a pesar de que habia 10 cotizaciones, en las ultimas solo se muestran 8, puesto que algunas cotizaciones se repetian con distinto timestamp, por lo que solo se guarda la mas reciente.


Ahora ingresaremos de input el archivo *datos2.json* que contiene un total de 7 cotizaciones

![](/imgs/datos2.png)

Como se puede observar, se actualizan los precios de las existentes tras comparar los timestamps (Por ejemplo *YPF*), como asi tambien se agregan nuevas cotizaciones que no eran existentes en el primer set de datos (Por ejempo *FORD*)