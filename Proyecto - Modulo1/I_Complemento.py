from ingrediente import Ingrediente

class I_Complemento (Ingrediente):
    def __init__(self, precio:float, calorias:int, inventario:int, sano:bool)->None:
        super().__init__(precio, calorias, inventario, sano)
    
    def restablecer(self)->None:
        self._inventario = 0