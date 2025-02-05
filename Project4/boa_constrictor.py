from animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratones_comidos = 0
    
    def hacer_sonido(self)->str:
        return "¡Tsss!"
    
    def agregar_raton(self, ratones_ingeridos:int)->None:
        self.__ratones_comidos += ratones_ingeridos

    def total_ratones(self) -> int:
        return self.__ratones_comidos