#Punto 1 | ¿Esto es Sano?
def esto_es_sano(kcalorias:int, vegetariano:bool)->bool:
    if kcalorias < 100 or vegetariano == True:
        return True
    else:
        return False
    

#Punto 2 | Las Calorías
def las_calorías(kcalorias_x_ingrediente:list)->float:
    total_kcal = round (sum(kcalorias_x_ingrediente) * 0.95, 2)
    return total_kcal

#Punto 3 | Costos
def costos (ingr1: dict, ingr2: dict, ingr3: dict) -> float:
    #Opcion 1
    total_cost = 0
    nombre_precio = [ingr1, ingr2, ingr3]
    for i in nombre_precio:
        total_cost += i.get("precio")
    
    #Opcion 2
    total_cost = sum (i[nombre_precio] for i in nombre_precio)

    return total_cost

