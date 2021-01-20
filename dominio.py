from abc import ABC
from abc import abstractmethod


class Dominio(ABC):
    """
    Representa el objeto de dominio que conoce los detalles de implementacion y modelamiento
    de algun problema especifico para ser resuelto con algoritmos probabilisticos.

    Metodos:
    generar()
        Construye aleatoriamente una estructura de datos que representa una posible 
        solucion al problema.

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

    @abstractmethod
    def generar(self):
        """Construye una estructura de datos que representa una posible solucion al problema.

        Entradas:
        ninguna

        Salidas:
        Una estructura de datos que representa una posible solucion valida al problema
        """

        pass

    @abstractmethod
    def fcosto(self, sol):
        """Calcula el costo asociado con una solucion dada.

        Entradas:
        sol (estructura de datos)
            Solucion cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solucion
        """

        pass

    @abstractmethod
    def vecino(sol):
        """Revisa si la solucion dada contiene elementos duplicados o no.

        Entradas:
        sol (estructura de datos)
            Solucion a partir de la cual se verificara si tiene elementos duplicados.

        Salidas:
        (bool) valor booleano que determina si la solucion contiene elementos duplicados.
        """

        pass

    @abstractmethod
    def validar(self, sol):
        """Valida que la solucion dada cumpla con todos los requerimientos del problema.

        Entradas:
        sol (estructura de datos)
            La solucion a validar

        Salidas:
        (bool) True si la solucion es valida, False en cualquier otro caso.
        """

        pass

    @abstractmethod
    def texto(self, sol):
        """Construye una representacion en hilera legible por humanos de la solucion
        con el fin de reportar resultados al usuario final.

        Entradas:
        sol (estructura de datos)
            La solucion a transformar en texto legible

        Salidas:
        (str) El texto legible que representa a la solucion.
        """

        pass
