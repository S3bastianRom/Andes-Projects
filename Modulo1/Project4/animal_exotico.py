from animal import Animal

class Animal_Exotico (Animal):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos: float)->None:
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    def calcular_flete(self)-> float:
        impuesto = (self._impuestos * self._peso)
        return impuesto
    
    def hacer_sonido(self):
        pass