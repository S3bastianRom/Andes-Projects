from concentrado import Concentrado

class Perro:
    def __init__(self, nombre:str, edad:int, raza:str, peso:float, fav_concentrado: Concentrado) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__raza = raza
        self.__peso = peso
        self.__fav_concentrado = fav_concentrado
    
    @staticmethod
    def ladrar () -> str:
        return  "Guau, guau!"
    
    def modificar_peso(self, nuevo_peso:float)-> None:
        self.__peso = nuevo_peso

  
    def dar_informacion(self)->str:
        return self.__nombre + "(" + self.__raza + "): " + str (self.__peso) + "|" + str (self.__edad)
    
    #Get and set Perro__fav_concentrado
    @property
    def fav_concentrado(self) -> str:
        return self.__fav_concentrado

    @fav_concentrado.setter
    def dar_concentrado(self, value:str) -> None:
        if isinstance(value, str):
            self.__fav_concentrado = value
        else:
            raise ValueError('Expected str')
    
    #Get and set Perro__nombre
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected str')