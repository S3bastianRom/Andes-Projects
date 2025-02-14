class Perro:
    def __init__(self, nombre:str, edad:int, raza:str, peso:float) -> None:
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected str')
        
    @property
    def edad(self) -> int:
        return self.__edad
    
    @edad.setter
    def edad(self, value:int) -> None:
        if isinstance(value, int):
            self.__edad = value
        else:
            raise ValueError('Expected int')

    @property
    def raza(self) -> str:
        return self.__raza
    
    @raza.setter
    def raza(self, value:str) -> None:
        if isinstance(value, str):
            self.__raza = value
        else:
            raise ValueError('Expected str')
        
    @property
    def peso(self) -> float:
        return self.__peso
    
    @peso.setter
    def peso(self, value:float) -> None:
        if isinstance(value, float):
            self.__peso = value
        else:
            raise ValueError('Expected float')