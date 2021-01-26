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

    for i in range(repeticiones):
        
        start = time.time()
        sol = optimizar_sa(dominio_sa, temperatura, enfriamiento)
        end = time.time()
        
        tiempos.append(end - start)

    plt.bar(range(repeticiones), tiempos, color ='blue', width = 0.6)

    plt.xlabel("Tiempo de ejecucion") 
    plt.ylabel("Tiempo")

    return tiempos