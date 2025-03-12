from ingrediente import Ingrediente

class Complemento (Ingrediente):
    def __init__(self, precio:float, calorias:int, nombre: str, inventario:int, es_vegetariano:bool)->None:
        super().__init__(precio, calorias, nombre,  inventario, es_vegetariano)
    
    def abastecer(self)->None:
        self._inventario += 10

    def renovar_inventario(self, cantidad: int = 0) -> None:
        self._inventario = cantidad