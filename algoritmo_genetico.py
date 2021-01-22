import random as rand

def optimizar(dominio, tam_pobl, porc_elite, prob_mut, reps):
    """Algoritmo genetico para optimizacion estocoastica.

    Entradas:
    dominio (DominioAG)
        Un objeto que modela el dominio del problema que se quiere aproximar.
    
    tam_pobl (int)
        Tamaño de la poblacion.
    
    porc_elite (float)
        Porcentaje de la poblacion que se tomara como elite.
    
    prob_mut (float)
        Probabilidad de mutacion, debe estar en el rango [0, 1]
    
    reps (int)
        Numero de iteraciones a ejecutar.

    Salidas:
        (estructura de datos) Estructura de datos segun el dominio, que representa una
        aproximacion a la mejor solucion al problema.
    """

    poblacion = dominio.generar_n(tam_pobl)
    
    while reps > 0:

        genomas = []
        for sol in poblacion:                       # Se puede usar listas de comprension
            aptitud = dominio.fcosto(sol)
            genoma = (sol, aptitud)
            genomas.append(genoma)

        genomas.sort(key=lambda x: x[1])

        for i in range(len(genomas)):
            poblacion[i] = genomas[i][0]

        num_padres = int(len(poblacion) * porc_elite)
        num_hijos = int(len(poblacion) - num_padres)
        sig_gen = poblacion[0:num_padres]
        descendencia = []

        while num_hijos > 0:
            
            x = rand.randrange(0, len(sig_gen))
            y = rand.randrange(0, len(sig_gen))

            while x == y:

                x = rand.randrange(0, len(sig_gen))
                y = rand.randrange(0, len(sig_gen))

            padre_a = sig_gen[x]
            padre_b = sig_gen[y]

            hijo = dominio.cruzar(padre_a, padre_b)
            p = rand.uniform(0, 1)

            if p <= prob_mut:
                hijo = dominio.mutar(hijo)
            descendencia.append(hijo)
            num_hijos = num_hijos - 1

        
        sig_gen += descendencia
        poblacion = sig_gen
        reps = reps - 1

    return poblacion[0]
