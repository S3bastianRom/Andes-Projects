from circulo import area_circulo

#Punto 2 | Área del cuadrado
def area_cuadrado(lado:float)->float:
    area = round (lado ** 2, 2)
    return area

#Punto 3 | El área sombreada
def area_sombreada (lado:float):
    radio = (lado / 2)
    circulo  = area_circulo (radio)
    cuadrado = area_cuadrado(lado)

    shaded_area = round (cuadrado - circulo,2,)
    return (shaded_area)