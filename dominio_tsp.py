from dominio import Dominio
import csv as py_csv
import random as rand

class DominioTSP(Dominio):
    """
    Esta clase modela el dominio del problema del Vendedor Viajero para su resolucion
    con algoritmos probabilisticos.

    Las soluciones se modelan como listas de enteros, donde cada numero representa
    una ciudad especifica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Metodos:
    generar()
        Construye aleatoriamente una lista que representa una posible solucion al problema.

    fcosto(sol)
        Calcula el costo asociado con una solucion dada.

    vecino(sol)
        Calcula una solucion vecina a partir de una solucion dada.

    validar(sol)
        Valida que la solucion dada cumple con los requisitos del problema.

    texto(sol)
        Construye una representacion en hilera legible por humanos de la solucion
        con el fin de reportar resultados al usuario final.
    """

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        especifica del problema del vendedor viajero.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que sera el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioTSP correctamente inicializada.
        """

        ciudades = []
        indices_ciudades = []
        indice_ciudad_inicio = None

        with open(ciudades_rutacsv, 'r') as file:
            reader = py_csv.reader(file)
            for row in reader:
                ciudades.append(row)

        for j in range (1, len(ciudades[0])):
            if ciudades[0][j] == ciudad_inicio:
                indice_ciudad_inicio = j - 1
            indices_ciudades.append(j - 1)

        self.ciudad_inicio = ciudad_inicio
        self.indice_ciudad_inicio = indice_ciudad_inicio
        self.indices_ciudades = indices_ciudades
        self.matriz_ciudades = ciudades
    
    def validar(self, sol):
        """Valida que la solucion dada cumple con los requisitos del problema.

        Si n es el numero de ciudades en el grafo, la solucion debe:
        - Tener tamanno (n-1)
        - Contener solo numeros enteros menores que n (las ciudades se numeran de 0 a (n-1))
        - No contener elementos repetidos
        - No contener la ciudad de inicio/fin del circuito

        Entradas:
        sol (list)
            La solucion a validar.

        Salidas:
        (bool) True si la solucion es valida, False en cualquier otro caso
        """

        if (len(sol) != len(set(sol))):
            return False

        if len(sol) != len(self.indices_ciudades) - 1:
            return False

        if all(isinstance(x , int) and x < len(self.indices_ciudades) for x in sol) == False:
            return False

        if self.indice_ciudad_inicio in sol:
            return False

        return True

    def texto(self, sol):
        """Construye una representacion en hilera legible por humanos de la solucion
        con el fin de reportar resultados al usuario final.

        La hilera cumple con el siguiente formato:
        Nombre ciudad inicio -> Nombre ciudad 1 -> ... -> Nombre ciudad n -> Nombre ciudad inicio

        Entradas:
        sol (list)
            Solucion a representar como texto legible

        Salidas:
        (str) Hilera en el formato mencionado anteriormente.
        """

        string_sol = []
        separator = ' -> '
        string_sol.append(str(self.matriz_ciudades[0][self.indice_ciudad_inicio + 1]))

        for i in range(len(sol)):
            string_sol.append(str(self.matriz_ciudades[0][sol[i] + 1]))

        string_sol.append(str(self.matriz_ciudades[0][self.indice_ciudad_inicio + 1]))

        return separator.join(string_sol)



    def generar(self):
        """Construye aleatoriamente una lista que representa una posible solucion al problema.

        Entradas:
        ninguna

        Salidas:
        (list) Una lista que representa una solucion valida para esta instancia del vendedor viajero
        """
        sol = list(range(0,len(self.indices_ciudades)))

        if self.indice_ciudad_inicio != None:
            sol.remove(self.indice_ciudad_inicio)

        rand.shuffle(sol)

        return sol


    def fcosto(self, sol):
        """Calcula el costo asociado con una solucion dada.

        Entradas:
        sol (list)
            Solucion cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solucion
        """
        costo = 0.0

        for i in range(len(sol) - 1):

            costo += float(self.matriz_ciudades[sol[i] + 1][sol[i+1] + 1])
        
        costo += float(self.matriz_ciudades[self.indice_ciudad_inicio + 1][sol[0] + 1]) + float(self.matriz_ciudades[sol[len(sol)- 1] + 1][self.indice_ciudad_inicio + 1])

        return costo


    def vecino(self, sol):

        """Calcula una solucion vecina a partir de una solucion dada.

        Una solucion vecina comparte la mayor parte de su estructura con 
        la solucion que la origina, aunque no son exactamente iguales. El 
        metodo transforma aleatoriamente algun aspecto de la solucion
        original.

        Entradas:
        sol (list)
            Solucion a partir de la cual se originara una nueva solucion vecina

        Salidas:
        (list) Solucion vecina
        """
        
        vecino = sol[:]

        n = len(sol)
        
        x = rand.randint(0, n-1)
        y = rand.randint(0, n-1)

        while x == y:

            x = rand.randint(0, n-1)
            y = rand.randint(0, n-1)
        
        temp = vecino[x]
        vecino[x] = vecino[y]
        vecino[y] = temp

        return vecino