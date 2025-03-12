#Missing getters and setters
from iproducto import iProducto
from funciones import costos, las_calorías, rentabilidad

class Malteada(iProducto):
    #Methods
    def __init__(self, nombre:str,precio_publico:float,ingredientes:list, volumen:int)->None:
        super().__init__()
        self.__nombre = nombre
        self.__precio_publico = precio_publico
        self.__ingredientes = ingredientes
        self.__volumen = volumen

    def calcular_costo(self)->float:
        return costos (*self.__ingredientes) + 500

    def calcular_calorias(self)->float:
        kcalorias_list = [ingrediente.calorias for ingrediente in self.__ingredientes]
        return las_calorías(kcalorias_list) + 200

    def calcular_rentabilidad(self)->float:
        return rentabilidad(self.__precio_publico,*self.ingredientes)

    #Getters / setters    
    #Getter and setter nombre is str
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected str')
        
    #Getter and setter precio_publico is float
    @property
    def precio_publico(self) -> float:
        return self.__precio_publico
    
    @precio_publico.setter
    def precio_publico(self, value:float) -> None:
        if isinstance(value, float):
            self.__precio_publico = value
        else:
            raise ValueError('Expected float')
    
    #Getter and setter ingredientes is list
    @property
    def ingredientes(self) -> list:
        return self.__ingredientes
    
    @ingredientes.setter
    def ingredientes(self, value:list) -> None:
        if isinstance(value, list):
            self.__ingredientes = value
        else:
            raise ValueError('Expected list')
        
    #Getter and setter volumen is int
    @property
    def volumen(self) -> int:
        return self.__volumen
    
    @volumen.setter
    def volumen(self, value:int) -> None:
        if isinstance(value, int):
            self.__volumen = value
        else:
            raise ValueError('Expected int')