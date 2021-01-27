from dominio_ag import DominioAG
from dominio_tsp import DominioTSP
import csv as py_csv
import random as rand

class DominioAGTSP(DominioAG, DominioTSP):
    """
    Representa el objeto de dominio que conoce los detalles de implementación y modelamiento
    del problema del vendedor viajero para ser resuelto con algoritmos genéticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar(n)
        Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

    cruzar(sol_a, sol_b)
        Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

    mutar(sol)
        Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.
    """



    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero para ser resuelto
        con algoritmos genéticos.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que sera el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioAGTSP correctamente inicializada.
        """

        DominioTSP.__init__(self, ciudades_rutacsv, ciudad_inicio)



    def generar_n(self, n):
        """Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

        Entradas:
        n (int)
            Número de soluciones aleatorias a generar.

        Salidas:
        (list) Lista que contiene n listas, cada una representando
        una posible solucion al problema modelado por el objeto de dominio.
        """
        soluciones = []
      
        for i in range(n):

            sol = DominioTSP.generar(self)
            soluciones.append(sol)

        return soluciones



    def cruzar(self, sol_a, sol_b):
        """Produce una nueva posible solucion cruzando las dos soluciones dadas por parametro.

        Entradas:
        sol_a (estructura de datos)
            Estructura de datos que modela la solucion antecesora A que sera cruzada con la B

        sol_b (estructura de datos)
            Estructura de datos que modela la solucion antecesora B que sera cruzada con la A

        Salidas:
        (estructura de datos) Una nueva solucion producto del cruzamiento entre las soluciones A y B
        """

        if len(sol_a) != len(sol_b):

            raise ValueError("Las soluciones deben ser del mismo tamano. sol_a", sol_a, 'sol_b', sol_b)

        sol_size = len(sol_a)

        punto_cruce = rand.randint(1, sol_size -1)

        solve = sol_a[:punto_cruce]
        
        for ciudad in sol_b:
            if ciudad not in solve:
                solve.append(ciudad)
                if len(solve) == len(sol_a):
                    break
    
        return solve



    def mutar(self, sol):
        """Produce una nueva solucion aplicando un ligero cambio a la solucion dada por
        parametro.

        Entradas:
        sol (estructura de datos)
            La solucion a mutar.
        
        Salidas:
        (estructura de datos) Una nueva solucion que refleja un ligero cambio con respecto 
        a la solucion dada por parametro
        """

        mutacion = DominioTSP.vecino(self, sol)

        return mutacion
