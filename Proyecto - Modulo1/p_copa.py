from productos import Producto

class Copa(Producto):
    def __init__(self, nombre:str, pvsp : float, tipo_de_vaso=str)->None:
        super().__init__(nombre, pvsp)
        self.__tipo_de_vaso = tipo_de_vaso