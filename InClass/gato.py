from animal import Animal

class Gato():
    def __init__(self, nombre:str, peso:float, edad:int, color:str)->None:
        super().__init__(nombre, peso, edad)
        self.__color = color
    
    def hacer_sonido (self)->str:
        return "Miau, Miau!"
    
    def obtener_color(self):
        return self.__color