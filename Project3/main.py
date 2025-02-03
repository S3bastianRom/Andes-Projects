from perro import Perro
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
menu_de_acceso = "Que opcion quieres ver \n1. Listado de perros y comida favorita: \n2. Rentabilidades: \n_________\n"

menu_value = input(menu_de_acceso)

if menu_value == "1":
    print ("_________")
    for perro in list_perros:
        print (f"{perro.nombre} su comida favorita es {perro.fav_concentrado.nombre} ")
elif menu_value == "2":
    print ("_________")
    for concen in concent_list:
        print (f"{concen.nombre} tiene una rentabilidad de {concen.calcular_rentabilidad()}%")