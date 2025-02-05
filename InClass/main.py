from perro import Perro
from boa_constrictor import Boa_Constrictor
from huron import Huron
from concentrado import Concentrado
from guarderia import Guarderia

from concentrado import Concentrado

concentrado_1 = Concentrado("DogMax", 35.50, 8050, "INV-12345")
concentrado_2 = Concentrado("NutriCan", 28.99, 3080, "INV-67890")
concentrado_3 = Concentrado("Perrito Feliz", 40.75, 50, "INV-54321")
concentrado_4 = Concentrado("CanVital", 32.30, 42, "INV-98765")
concentrado_5 = Concentrado("SuperDog", 29.99, 3, "INV-24680")

concent_list = [concentrado_1, concentrado_2, concentrado_3, concentrado_4, concentrado_5]
guarda_perros = Guarderia()

perro1 = Perro("Max", 30, "German Sheperd", 27.3, concentrado_1)
perro2 = Perro("Zeuz",40, "Bulldog", 28.2, concentrado_2)
perro3 = Perro("Tatan",50, "Bull terrier", 23.9, concentrado_3)
perro4 = Perro("Orion",20, "Pitbull", 5.1, concentrado_4)
perro5 = Perro("Maximo",25, "French Poddle", 35.3, concentrado_5)

list_perros = [perro1, perro2, perro3, perro4, perro5]

for p in list_perros:
    print (f"{p.obtener_nombre()} esta ladrando, escuchalo {p.hacer_sonido()}")


bola = Boa_Constrictor(nombre="Bola", peso=8.5, edad=4, pais_origen="Brasil", impuestos=12.5)

print(bola.hacer_sonido())  # Esperado: "¡Tsss!"

# Agregar ratones a la Boa
bola.agregar_raton(5)  # Agregamos 5 ratones
bola.agregar_raton(3)  # Agregamos 3 ratones


print(f"Total ratones ingeridos: {bola.total_ratones()}")  # Esperado: 8
print(f"El flete de la Boa es: {bola.calcular_flete()}")  # Esperado: 106.25 (12.5 * 8.5)


roco = Huron(nombre="Roco", peso=2.3, edad=3, pais_origen="Chile", impuestos=7.2)

print(roco.hacer_sonido())  # Esperado: "¡Eek Eek!"
print(f"El flete del Huron es: {roco.calcular_flete()}")  # Esperado: 16.56 (7.2 * 2.3)
