class Concentrado:
    def __init__(self, nombre:str, precio:float, numero_kcal: int, registro_invima: int):
        self.__nombre = nombre
        self.__precio = precio
        self.__numero_kcal = numero_kcal
        self.__registro_invima = registro_invima

    def dar_informacion(self)->str:
        return f"{self.__nombre} (${self.__precio})"
    
    def calcular_rentabilidad(self)->float:
        rentabilidad = round((self.__precio / self.__numero_kcal), 2)
        return rentabilidad

    #Get and set Concentrado__nombre
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected str')

    #Get and set Concentrado__precio
    @property
    def precio(self) -> float:
        return self.__precio
    
    @precio.setter
    def precio(self, value:float) -> None:
        if isinstance(value, float):
            self.__precio = value
        else:
            raise ValueError('Expected float')
        

    #Get and set Concentrado__numero_kcal
    @property
    def numero_kcal(self) -> int:
        return self.__numero_kcal
    
    @numero_kcal.setter
    def numero_kcal(self, value:int) -> None:
        if isinstance(value, int):
            self.__numero_kcal = value
        else:
            raise ValueError('Expected int')