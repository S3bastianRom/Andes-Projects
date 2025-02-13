from modulo import area_sombreada
from modulo import area_cuadrado

lado = float(input("Cuanto mide el lado del cuadrado: "))
while lado < 1:
    print ("Ingresa un valor valido")
    lado = float(input("Cuanto mide el lado del cuadrado: "))

print (f"El area sombreada tiene un area de {area_sombreada(lado)} cms")
print (f"El area del cuadrado es {area_cuadrado(lado)} cms")