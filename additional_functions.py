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

def calcular_tiempos_ag(ciudad_inicio, tam_pobl, porc_elite, porc_mut, reps):

    dominio_ag = DominioAGTSP('datos/ciudades_cr.csv', ciudad_inicio)
    tiempos = []
    soluciones = []
    mejor_indice = 0

    for i in range(10):
            
        start = time.time()
        sol = optimizar_ag(dominio_ag,tam_pobl, porc_elite, porc_mut, reps)
        soluciones.append(sol)
        end = time.time()
        duracion = end - start
        tiempos.append(duracion)
        mejor_tiempo = min(tiempos)

        if duracion < mejor_tiempo:
            mejor_indice = i
                
    indices = [str(x) for x in range(1, 11)]

    plt.bar(indices, tiempos, color ='blue', width = 0.6)

    plt.xlabel("Numero de pruebas") 
    plt.ylabel("Tiempo de ejecucion")

    mejor_tiempo = min(tiempos)

    resultado = []

    resultado.append(mejor_tiempo)
    resultado.append(soluciones[mejor_indice])

    return resultado


def comparar_resultados_tiempo(resultados, temperatura):

    colores = ['orange', 'red', 'blue', 'cyan', 'green']
    plt.bar(['0.50', '0.60', '0.70', '0.80', '0.90'], resultados, color =colores, width = 0.5)
    plt.xlabel("Resultados a temperatura " + temperatura) 
    plt.ylabel("Tiempo de ejecucion")


def comparar_resultados_tiempo_ag(resultados, reps):

    colores = ['orange', 'red', 'blue', 'cyan']
    plt.bar(['50', '300', '1000'], resultados, color = colores, width = 0.7)
    plt.xlabel("Resultados con " + reps + ' repeticiones') 
    plt.ylabel("Tiempo de ejecucion")



def comparar_resultados_costo(resultados, temperatura):
    costos = []
    dominio_sa = DominioTSP('datos/ciudades_cr.csv', 'Alajuela')
    for i in range(len(resultados)):
        costos.append(dominio_sa.fcosto(resultados[i]))

    colores = ['orange', 'red', 'blue', 'cyan', 'green']
    plt.bar(['0.50', '0.60', '0.70', '0.80', '0.90'], costos, color =colores, width = 0.5)
    plt.xlabel("Resultados a temperatura " + temperatura) 
    plt.ylabel("Costo")


def comparar_resultados_costo_ag(resultados, reps):
    costos = []
    dominio_ag = DominioAGTSP('datos/ciudades_cr.csv', 'Alajuela')
    for i in range(len(resultados)):
        costos.append(dominio_ag.fcosto(resultados[i]))
    colores = ['orange', 'red', 'blue', 'cyan', 'green']
    plt.bar(['50', '300', '700'], costos, color = colores, width = 0.7)
    plt.xlabel("Resultados con " + reps + ' repeticiones') 
    plt.ylabel("Costo")



def comparar_tiempo_algoritmos(tiempo_sa, tiempo_ag):
    resultados = [tiempo_sa, tiempo_ag]
    colores = ['red', 'blue']
    plt.bar(['Simulated Anealing', 'Genetic Algorithm'], resultados, color = colores, width = 0.5)
    plt.xlabel('Resultados con buenos parametros en ambos algoritmos') 
    plt.ylabel("Tiempo de ejecucion")


def comparar_costo_algoritmos(sol_sa_a, sol_ag_a, ciudad_inicio):
    costos = []
    dominio = DominioTSP('datos/ciudades_cr.csv', ciudad_inicio)
    costos.append(dominio.fcosto(sol_sa_a))
    costos.append(dominio.fcosto(sol_ag_a))
    colores = ['red', 'blue']
    plt.bar(['Simulated Anealing', 'Genetic Algorithm'], costos, color = colores, width = 0.5)
    plt.xlabel('Resultados con buenos parametros en ambos algoritmos') 
    plt.ylabel("Costo")




