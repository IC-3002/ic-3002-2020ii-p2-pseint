from algoritmo_genetico import optimizar as optimizar_ag
from simulated_annealing import optimizar as optimizar_sa
import time
from dominio_tsp import DominioTSP
from dominio_ag_tsp import DominioAGTSP
import numpy as np
import matplotlib.pyplot as plt


def calcular_tiempos_sa(repeticiones, ciudad_inicio, temperatura, enfriamiento):

    dominio_sa = DominioTSP('datos/ciudades_cr.csv', ciudad_inicio)
    tiempos = []
    soluciones = []
    mejor_indice = 0

    for i in range(repeticiones):
        
        start = time.time()
        sol = optimizar_sa(dominio_sa, temperatura, enfriamiento)
        soluciones.append(sol)
        end = time.time()
        duracion = end - start
        tiempos.append(duracion)
        mejor_tiempo = min(tiempos)

        if duracion < mejor_tiempo:
            mejor_indice = i

    indices = [str(x) for x in range(1, repeticiones+ 1)]

    plt.bar(indices, tiempos, color ='blue', width = 0.6)

    plt.xlabel("Numero de pruebas") 
    plt.ylabel("Tiempo de ejecucion")

    mejor_tiempo = min(tiempos)

    resultado = []

    resultado.append(mejor_tiempo)
    resultado.append(soluciones[mejor_indice])

    return resultado


def comparar_resultados_tiempo(resultados, temperatura):

    indices = [str(x) for x in range(1, 5+ 1)]
    colores = ['orange', 'red', 'blue', 'cyan', 'green']
    plt.bar(['0.50', '0.60', '0.70', '0.80', '0.90'], resultados, color =colores, width = 0.5)
    plt.xlabel("Resultados a temperatura " + temperatura) 
    plt.ylabel("Tiempo de ejecucion")

def comparar_resultados_costo(resultados):
    costos = []
    dominio_sa = DominioTSP('datos/ciudades_cr.csv', 'Alajuela')
    for i in range(len(resultados)):
        costos.append(dominio_sa.fcosto(resultados[i]))
    indices = [str(x) for x in range(1, 5+ 1)]
    colores = ['orange', 'red', 'blue', 'cyan', 'green']
    plt.bar(['0.50', '0.60', '0.70', '0.80', '0.90'], costos, color =colores, width = 0.5)
    plt.xlabel("Resultados a temperatura ") 
    plt.ylabel("Costo")







