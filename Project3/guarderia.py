from perro import Perro
from concentrado import Concentrado

perro_1 = Perro("Zeus", 8, "criollo", 18.5)
perro_2 = Perro("Leonardo", 2, "Pastor Belga", 25.6)

concentrado_max = Concentrado("Max", 187569.58, 15800, 654654654654)
print (perro_1.dar_informacion())

perro_1.dar_nombre = 55

print (perro_1.dar_informacion())