import dominio_ag_tsp as dominio
import random as rand

def optimizar(dominio, tam_pobl, porc_elite, prob_mut, reps):
    """Algoritmo genético para optimización estocástica.

    Entradas:
    dominio (DominioAG)
        Un objeto que modela el dominio del problema que se quiere aproximar.
    
    tam_pobl (int)
        Tamaño de la población.
    
    porc_elite (float)
        Porcentaje de la población que se tomará como elite.
    
    prob_mut (float)
        Probabilidad de mutación, debe estar en el rango [0, 1]
    
    reps (int)
        Número de iteraciones a ejecutar.

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """

    poblacion = dominio.generar_n(tam_pobl)
    genomas = []
    while reps > 0:

        for sol in poblacion:

            aptitud = dominio.fcosto(sol)
            genoma = (sol, aptitud)
            genomas.append(genoma)
        
        genomas.sort(key=lambda genoma: genoma[1]) #llave aptitud

        for i in range(0, len(genomas)):

            poblacion[i] = genomas[i][0]

        num_padres = int(len(poblacion) * porc_elite)
        num_hijos = int(len(poblacion) - num_padres)
        sig_gen = poblacion[0:num_padres]
        descendencia = []

        while num_hijos > 0:

            padre_a = sig_gen[rand.randint(0, len(sig_gen) - 1)]
            padre_b = sig_gen[rand.randint(0, len(sig_gen) - 1)]
            hijo = dominio.cruzar(padre_a, padre_b)
            p = rand.uniform(0, 1)

            if p <= prob_mut:
                hijo = dominio.mutar(hijo)

            descendencia.append(hijo)
            num_hijos -= 1


        poblacion = sig_gen.extend(descendencia)
        reps -= 1
    
    return poblacion[0]