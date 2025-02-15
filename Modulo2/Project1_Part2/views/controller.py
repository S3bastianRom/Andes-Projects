from models.guarderia import Guarderia

class Controller(Guarderia):
    def __init__(self):
        self.guarderia = Guarderia()

    def retornar_perros(self):
        return self.guarderia.retornar_perros()