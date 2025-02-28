from Guarderia.boa_constrictor import Boa_Constrictor
from Guarderia.huron import Huron

class Guarderia():
    def __init__(self):
        self.geraldine = Boa_Constrictor("Geraldine", 5, 2, "Brasil", 100)
        self.antonia = Boa_Constrictor("Antonia", 4, 1, "Uganda", 500)
        self.oscar = Huron("Oscar", 2, 1, "Argentina", 50)
        self.jorge = Huron("jorge", 6, 3, "Colombia", 80)

    def alimentador_boa(self, boa, ratones):
        try:
            if boa is None:
                return "Esta Boa no existe"

            boa.agregar_raton(ratones)
            return("Exito")
        except ValueError:
            return "La boa esta llena"