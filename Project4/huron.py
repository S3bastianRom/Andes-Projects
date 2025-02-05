from animal_exotico import Animal_Exotico

class Huron(Animal_Exotico):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)

    def hacer_sonido(self)->str:
        return "¡Eek Eek!"