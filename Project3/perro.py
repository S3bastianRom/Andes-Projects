class Perro:
    def __init__(self, nombre:str, edad:int, raza:str, peso:float) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__raza = raza
        self.__peso = peso
    
    @staticmethod
    def ladrar () -> str:
        return  "Guau, guau!"
    
    def modificar_peso(self, nuevo_peso:float)-> None:
        self.__peso = nuevo_peso

  
    def dar_informacion(self):
        return self.__nombre + "(" + self.__raza + "): " + str (self.__peso) + "|" + str (self.__edad)
    
    @property
    def dar_nombre(self) -> str:
        """ Devuelve el valor del atributo privado 'dar_nombre' """
        return self.dar_nombre
    
    @dar_nombre.setter
    def dar_nombre(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'dar_nombre'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.dar_nombre = value
        else:
            raise ValueError('Expected str')