from abc import ABC, abstractmethod

class iProducto(ABC):
    @abstractmethod
    def calcular_calorias(self)->None:
        pass

    @abstractmethod
    def calcular_costo(self)->None:
        pass

    @abstractmethod
    def calcular_rentabilidad(self)->None:
        pass