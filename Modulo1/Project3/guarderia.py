from concentrado import Concentrado

class Guarderia:
    def __init__(self)->None:
        self.__concentrados = []

    def nuevo_concentrado(self, concentrado : Concentrado)->None:
        self.__concentrados.append (concentrado)

    def listar_concentrados(self)->list:
        print("Lista de concentrados disponibles:")
        for conc in self.__concentrados:
            print(conc.nombre)