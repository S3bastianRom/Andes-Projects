import unittest
from Guarderia.boa_constrictor import Boa_Constrictor

class TestBoa_Constrictor(unittest.TestCase):
    def test_hacer_sonido(self):
        boa = Boa_Constrictor("Geraldine", 5, 2, "Brasil", 100)
        self.assertEqual(boa.hacer_sonido(), "¡Tsss!")

    def test_agregar_raton(self)->None:
        boa = Boa_Constrictor("Geraldine", 5, 2, "Brasil", 100)
        try:
            boa.agregar_raton(9)
            self.assertEqual (boa.total_ratones(), 9)
        except ValueError as e:
            self.assertEqual (str(e), "Demasiados Ratones!")

    def test_calculo_flete(self):
        boa = Boa_Constrictor("Geraldine", 5, 2, "Brasil", 100)
        self.assertEqual (boa.calcular_flete(), 500)