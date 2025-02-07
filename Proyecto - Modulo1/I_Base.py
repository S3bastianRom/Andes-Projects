from ingrediente import Ingrediente

class I_Base (Ingrediente):
    def __init__(self, precio:float, calorias:int, inventario:int, sano:bool, sabor:str)->None:
        super().__init__(precio, calorias, inventario, sano)
        self.__sabor =  sabor

    @property
    def sabor(self) -> str:
        return self.__sabor
    
    @sabor.setter
    def sabor(self, value:str) -> None:
        if isinstance(value, str):
            self.__sabor = value
        else:
            raise ValueError('Corrige el sabor')