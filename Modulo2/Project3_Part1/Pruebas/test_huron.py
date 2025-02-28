import unittest
from Guarderia.huron import Huron

class TestBoa_Constrictor(unittest.TestCase):
    def test_hacer_sonido(self):
        huron = Huron("Oscar", 2, 1, "Argentina", 50)
        self.assertEqual(huron.hacer_sonido(), "¡Eek Eek!")

    def test_calculo_flete(self):
        huron = Huron("Oscar", 2, 1, "Argentina", 50)
        self.assertEqual (huron.calcular_flete(), 100)