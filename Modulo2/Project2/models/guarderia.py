from models.perros import Perro

class Guarderia:
    def __init__(self) -> None:
        self.__perros = []

        self.agregar_perros(Perro(nombre="Rufo", raza="Labrador", peso=22, edad=7))
        self.agregar_perros(Perro(nombre="Bingo", raza="Pug", peso=6, edad=2))
        self.agregar_perros(Perro(nombre="Lassie", raza="Collie", peso=27, edad=5))


    def agregar_perros(self, perro: Perro):
        self.__perros.append (perro)

    def retornar_perros(self):
        return tuple(self.__perros)

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


    #Getter and setter ubicacion is str
    @property
    def ubicacion(self) -> str:
        return self.__ubicacion
    
    @ubicacion.setter
    def ubicacion(self, value:str) -> None:
        if isinstance(value, str):
            self.__ubicacion = value
        else:
            raise ValueError('Expected str')