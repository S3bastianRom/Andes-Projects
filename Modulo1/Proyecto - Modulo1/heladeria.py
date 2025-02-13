from funciones import mejor_producto
from base import Base

class Heladeria ():
    def __init__(self, productos: list, ingredientes:list)->None:
        self.__productos = productos
        self.__ingredientes = ingredientes
        self.__contador_ventas_dia = 0
        self.__tota_ventas = 0


    #Getters and setters 
    #Getter and setter ingredientes and method to add ingredientes and to check if an ingredient is existent or not
    @property
    def ingredientes(self) -> list:
        return self.__ingredientes
    
    @ingredientes.setter
    def ingredientes(self, nuevos_ingredientes: list):
        self.__ingredientes.extend (nuevos_ingredientes)

    #Getter and setter ventas_dia is int
    @property
    def ventas_dia(self) -> int:
        return self.__contador_ventas_dia
    
    #Obtener el mejor producto de la lista de productos
    def mejor_producto(self) -> str:
        return mejor_producto(*self.__productos)
    
    #Metodo venta
    def vender(self, nombre_producto:str)->bool:
        existente = [p for p in self.__productos if p.nombre == nombre_producto]

        if not existente:
            return False
        
        producto = existente[0]

        for ingrediente in producto.ingredientes:
            ingredientes_disponibles = [i for i in self.__ingredientes if i.nombre == ingrediente.nombre]
            
            if not ingredientes_disponibles:
                return False
            
            ingrediente_obj = ingredientes_disponibles[0]
            
            cantidad_necesaria = 0.2 if isinstance(ingrediente_obj, Base) else 1
            
            if ingrediente_obj.inventario < cantidad_necesaria:
                return False
            
            ingrediente_obj.inventario -= cantidad_necesaria
        
        self.__tota_ventas += producto.precio_publico 
        self.__contador_ventas_dia += 1
        return True