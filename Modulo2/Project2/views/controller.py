# controller/controller.py
from models.guarderia import Guarderia

class Controller:
    def __init__(self):
        self.guarderia = Guarderia()

    def retornar_perros(self):
        # Llama al método retornar_perros del modelo Guarderia
        return self.guarderia.retornar_perros()

# Si necesitas ver la salida, puedes probar la clase Controlador directamente
if __name__ == "__main__":
    controller = Controller()
    print(controller.retornar_perros())