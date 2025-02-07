from abc import ABC, abstractmethod

class Ingrediente(ABC):
    def __init__(self, precio:float, calorias:int, inventario:int, sano:bool)->None:
        self._precio = precio
        self._calorias = calorias
        self._inventario = inventario
        self._sano = sano

    def reabastecer(self, nueva_cantidad):
        if nueva_cantidad > 0:
            self._inventario += nueva_cantidad