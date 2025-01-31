class Concentrado:
    def __init__(self, nombre:str, precio:float, numero_kcal: int, registro_invima: int):
        self.__nombre = nombre
        self.__precio = precio
        self.__numero_kcal = numero_kcal
        self.__registro_invima = registro_invima

    def dar_informacion(self)->str:
        return f"{self.__nombre} (${self.__precio})"
    
    def calcular_rentabilidad(self)->float:
        return round((self.__precio / self.__numero_kcal), 2)
    
