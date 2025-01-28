from math import pi

#Punto 1 | Área del círculo
def area_circulo (radio:float)->float:
    area = round (pi * (radio**2),2)
    return area