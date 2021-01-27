#Librerias necesarias
import math
import random


def optimizar(dominio, temperatura = 10e32, tasa_enfriamiento = 0.95):
    """Algoritmo de optimizacion estocastica simulated annealing.

    Entradas:
    dominio (Dominio)
        Un objeto que modela el dominio del problema que se quiere aproximar.

    temperatura (float/int)
        Temperatura inicial del algoritmo, se recomienda un numero alto

    tasa_enfriamiento (float)
        Porcentaje de enfriamiento de la temperatura durante cada iteracion, el valor
        por defecto es 0.95, lo que indica una tasa de enfriamiento del 5%.

    Salidas:
        (estructura de datos) Estructura de datos segun el dominio, que representa una
        aproximacion a la mejor solucion al problema.
    """

    solucion = dominio.generar() #genera una solucion al azar
    costo = dominio.fcosto(solucion) #se calcula el costo de dicha solucion
    
    while temperatura > 0.01:
        
        solucionP = dominio.vecino(solucion) #genera una solucion vecina al azar
        costoP = dominio.fcosto(solucionP) #se calcula el costo de la solucion vecina

        p = (math.exp(-(abs(costoP-costo))) ) / temperatura #math.exp eleva E a la potencia indicada
                                                            #abs = valor absoluto
        pAzar = random.uniform(0,1)                         #random.uniform retorna un valor intermedio entre 0 y 1 de distribucion uniforme
        
        if costoP<costo or pAzar<=p:
            solucion = solucionP
            costo = costoP
        
        temperatura= temperatura * tasa_enfriamiento
    
    return solucion