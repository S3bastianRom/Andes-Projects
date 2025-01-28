from math import pi

#Punto 1 | Área del círculo
def area_circulo (ratio:float)->float:
    area = round (pi * (ratio**2),2)
    return area