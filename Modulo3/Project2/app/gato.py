from app.animal import Animal

class Gato(Animal):
    def __init__(self, nombre:str, peso:float, edad:int):
        super().__init__(nombre, peso, edad)

    
    def hacer_sonido(self)->str:
        return "¡Miau!"