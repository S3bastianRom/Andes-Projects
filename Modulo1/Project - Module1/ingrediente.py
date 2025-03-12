from abc import ABC, abstractmethod
from funciones import esto_es_sano

class Ingrediente(ABC):
    def __init__(self, precio:float, calorias:int, nombre: str, inventario:int, es_vegetariano:bool)->None:
        self._precio = precio
        self._calorias = calorias
        self._nombre = nombre
        self._inventario = inventario
        self._es_vegetariano = es_vegetariano

    @abstractmethod
    def abastecer(self)->None:
        pass

    #Esto es sano funcion
    def es_sano(self) -> bool:
        return esto_es_sano(self._calorias, self._es_vegetariano)

    #Getter and seter parametro precio
    @property
    def precio(self) -> float:
        return self._precio
    
    @precio.setter
    def precio(self, value:float) -> None:
        if isinstance(value, float):
            self._precio = value
        else:
            raise ValueError('Expected float')
    
    
    #Getter and seter parametro calorias
    @property
    def calorias(self) -> int:
        return self._calorias
    
    @calorias.setter
    def calorias(self, value:int) -> None:
        if isinstance(value, int):
            self._calorias = value
        else:
            raise ValueError('Expected int')
        
    
    #Getter and setter nombre is str
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        if isinstance(value, str):
            self._nombre = value
        else:
            raise ValueError('Expected str')


    #Getter and seter parametro inventario
    @property
    def inventario(self) -> int:
        return round(self._inventario,2)

    @inventario.setter
    def inventario(self, nuevo_inventario: int)->None:
        self._inventario = nuevo_inventario
        
    
    #Getter and seter parametro es_vegetariano
    @property
    def es_vegetariano(self) -> bool:
        return self._es_vegetariano
    
    @es_vegetariano.setter
    def es_vegetariano(self, value:bool) -> None:
        if isinstance(value, bool):
            self._es_vegetariano = value
        else:
            raise ValueError('Expected bool')