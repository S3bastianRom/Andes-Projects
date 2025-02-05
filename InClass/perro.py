from concentrado import Concentrado
from animal import Animal 

class Perro(Animal):
    def __init__(self, nombre:str, peso:float, edad:int, raza:str, fav_concentrado: Concentrado) -> None:
        super().__init__(nombre, peso, edad)
        self.__raza = raza
        self.__fav_concentrado = fav_concentrado
    

    def hacer_sonido (self) -> str:
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
    
    """#Get and set Perro__nombre
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected str')"""