from dominio_ag import DominioAG
from dominio_tsp import DominioTSP

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
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioAGTSP correctamente inicializada.
        """

        ciudades = []
        indices_ciudades = []
        indice_ciudad_inicio = float('inf')

        with open(ciudades_rutacsv, 'r') as file:
            reader = py_csv.reader(file)
            for row in reader:
                ciudades.append(row)

        for i in range (1, len(ciudades[0])):
            if ciudades[0][j] == ciudad_inicio:
                indice_ciudad_inicio = j- 1
            indices_ciudades.append(j - 1)

        self.ciudades_rutacsv = ciudades_rutacsv
        self.ciudad_inicio = ciudad_inicio
        self.indice_ciudad_inicio = indice_ciudad_inicio
        self.indices_ciudades = indices_ciudades
        self.matriz_ciudades = ciudades

    def generar_n(self, n):
        """Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

        Entradas:
        n (int)
            Número de soluciones aleatorias a generar.

        Salidas:
        (list) Lista que contiene n listas, cada una representando
        una posible solución al problema modelado por el objeto de dominio.
        """
        soluciones = []

        sol = self.indices_ciudades
        sol.remove(self.indice_ciudad_inicio)

        for i in range(n):

            rand.shuffle(sol)
            soluciones.append(sol)

        return soluciones

    def cruzar(self, sol_a, sol_b):
        """Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

        Entradas:
        sol_a (estructura de datos)
            Estructura de datos que modela la solución antecesora A que será cruzada con la B

        sol_b (estructura de datos)
            Estructura de datos que modela la solución antecesora B que será cruzada con la A

        Salidas:
        (estructura de datos) Una nueva solución producto del cruzamiento entre las soluciones A y B
        """

        if len(sol_a) != len(sol_b):

            raise ValueError("Las soluciones deben ser del mismo tamano")

        sol_size = len(sol_a)

        punto_cruce = rand.randint(1, sol_size -1)

        gen_a = sol_a[0:punto_cruce]
        gen_b = sol_b[punto_cruce:]

        onjunto = list(set(sol_a)) + list(set(sol_b))

        for element in gen_a:
            if element in gen_b:
                gen_a.remove(element)

        for element in conjunto:
            if element not in gen_a and element not in gen_b:
                gen_a.append(element)

        descendencia = gen_a + gen_b
    
        return descendencia


    def mutar(self, sol):
        """Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.

        Entradas:
        sol (estructura de datos)
            La solución a mutar.
        
        Salidas:
        (estructura de datos) Una nueva solución que refleja un ligero cambio con respecto 
        a la solución dada por parámetro
        """

        punto_a = rand.randint(0,len(sol)-1)
        punto_b = rand.randint(0,len(sol)-1)
        temp = sol[punto_a]
        
        sol[punto_a] = sol[punto_b]
        sol[punto_b] = temp
        
        return sol
