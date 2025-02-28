from Guarderia.ianimal import iAnimal
from abc import ABC, abstractmethod

class Animal (iAnimal):
    def __init__(self, nombre:str, peso:float, edad:int)->None:
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = 0

    def comer (self, kilos:int)->None:
        self._kilos_comidos += kilos

    def obtener_kilos_comidos(self)->int:
        return self._kilos_comidos
    
    def obtener_nombre(self) -> str:
        return self._nombre
        
    def peso(self) -> float:
        return self._peso
    
    def edad(self) -> int:
        return self._edad
    
    @abstractmethod
    def hacer_sonido(self)->None:
        pass