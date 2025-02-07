from productos import Producto

class Malteada(Producto):
    def __init__(self, nombre:str, pvsp : float, oz_volumen : float)->None:
        super().__init__(nombre, pvsp)
        self.__oz_volumen = oz_volumen