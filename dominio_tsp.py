from dominio import Dominio
import csv as py_csv
import random as rand

ciudades = []
indices_ciudades = []
ciudad_inicio = 'Heredia'
indice_ciudad_inicio = float('inf')

with open('datos/ciudades_cr_pruebas.csv', 'r') as file:
    reader = py_csv.reader(file)
    for row in reader:
        ciudades.append(row)


for j in range (1, len(ciudades[0])):
    if ciudades[0][j] == ciudad_inicio:
        indice_ciudad_inicio = j - 1
    indices_ciudades.append(j - 1)


print('La matriz de ciudades es: ')
for i in range (len(ciudades)):
    for j in range (len(ciudades[0])):
        print(ciudades[i][j], end=' ')
    print()

print('El indice de la ciudad de inicio es:', indice_ciudad_inicio)

print('Los indices de todas las ciudades son', indices_ciudades)

sol = [2, 1, 3]
costo = 0.0

for i in range(len(sol) - 1):
    print(float(ciudades[sol[i]][sol[i+1]]))
    costo += float(ciudades[sol[i]][sol[i+1]])
        
costo += float(ciudades[indice_ciudad_inicio][sol[0]]) + float(ciudades[sol[len(sol) - 1]][indice_ciudad_inicio])   




class DominioTSP(Dominio):
    """
    Esta clase modela el dominio del problema del Vendedor Viajero para su resolución
    con algoritmos probabilísticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar()
        Construye aleatoriamente una lista que representa una posible solución al problema.

    fcosto(sol)
        Calcula el costo asociado con una solución dada.

    vecino(sol)
        Calcula una solución vecina a partir de una solución dada.

    validar(sol)
        Valida que la solución dada cumple con los requisitos del problema.

    texto(sol)
        Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.
    """

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioTSP correctamente inicializada.
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

    def revisar_duplicados(lista):
        if (len(lista) == len(set(lista))):
            return False
        return True
    
    def validar(self, sol):
        """Valida que la solución dada cumple con los requisitos del problema.

        Si n es el número de ciudades en el grafo, la solución debe:
        - Tener tamaño (n-1)
        - Contener sólo números enteros menores que n (las ciudades se numeran de 0 a (n-1))
        - No contener elementos repetidos
        - No contener la ciudad de inicio/fin del circuito

        Entradas:
        sol (list)
            La solución a validar.

        Salidas:
        (bool) True si la solución es válida, False en cualquier otro caso
        """
        if (revisar_duplicados(sol) == True):
            return False

        if len(sol) != len(self.indices_ciudades) - 1:
            return False

        if all(isinstance(x , int) and x < len(self.indices_ciudades) for x in sol) == False:
            return False

        if self.indice_ciudad_inicio in sol:
            return False

        return True

    def texto(self, sol):
        """Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

        La hilera cumple con el siguiente formato:
        Nombre ciudad inicio -> Nombre ciudad 1 -> ... -> Nombre ciudad n -> Nombre ciudad inicio

        Entradas:
        sol (list)
            Solución a representar como texto legible

        Salidas:
        (str) Hilera en el formato mencionado anteriormente.
        """

        string_sol = ''

        for i in range(len(sol)):
            string_sol += str(self.matriz_ciudades[0][sol[i] + 1]) + ' -> '

        return string_sol


    def generar(self):
        """Construye aleatoriamente una lista que representa una posible solución al problema.

        Entradas:
        ninguna

        Salidas:
        (list) Una lista que representa una solución válida para esta instancia del vendedor viajero
        """

        sol = self.indices_ciudades
        sol.remove(self.indice_ciudad_inicio)
        rand.shuffle(sol)

        return sol

    def fcosto(self, sol):
        """Calcula el costo asociado con una solución dada.

        Entradas:
        sol (list)
            Solución cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solución
        """
        costo = 0.0

        for i in range(len(sol)):
            costo += self.matriz_ciudades[sol[i]][sol[i+1]]
        
        costo += self.matriz_ciudades[self.indice_ciudad_inicio][sol[0]] + self.matriz_ciudades[sol[len(sol)- 1]][self.indice_ciudad_inicio] 

        return costo


    def vecino(self, sol):
        """Calcula una solución vecina a partir de una solución dada.

        Una solución vecina comparte la mayor parte de su estructura con 
        la solución que la origina, aunque no son exactamente iguales. El 
        método transforma aleatoriamente algún aspecto de la solución
        original.

        Entradas:
        sol (list)
            Solución a partir de la cual se originará una nueva solución vecina

        Salidas:
        (list) Solución vecina
        """
        n = len(sol)
        
        while i == j:

            i = rand.randint(0, n-1)
            j = rand.randint(0, n-1)
        
        temp = sol[i]
        sol[i] = sol[j]
        sol[j] = temp

        return sol