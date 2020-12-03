import unittest

from simulated_annealing import optimizar
from dominio_tsp import DominioTSP


class PruebaSimulatedAnnealing(unittest.TestCase):

    def test_optimizar(self):
        dominio = DominioTSP('datos/ciudades_cr_pruebas.csv', 'Alajuela')
        sol = optimizar(dominio)
        self.assertTrue(dominio.validar(sol))
