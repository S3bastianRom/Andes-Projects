from ingrediente import Ingrediente

class Base (Ingrediente):
    def __init__(self, precio:float, calorias:int, nombre: str, inventario:int, es_vegetariano:bool, sabor:str)->None:
        super().__init__(precio, calorias, nombre, inventario, es_vegetariano)
        self._sabor =  sabor

    def abastecer(self)->None:
        self._inventario += 5

    @property
    def sabor(self) -> str:
        return self._sabor
    
    @sabor.setter
    def sabor(self, value:str) -> None:
        if isinstance(value, str):
            self._sabor = value
        else:
            raise ValueError('Corrige el sabor')