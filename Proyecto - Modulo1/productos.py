from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre:str, pvsp : float)->None:
        self._nombre = nombre
        self._pvsp = pvsp
        self._ingredientes = []
    
    @abstractmethod
    def kcalorias_conteo(self):
        pass

    @abstractmethod
    def calculo_costo(self):
        pass

    @abstractmethod
    def calculo_rentabilidad(self):
        pass