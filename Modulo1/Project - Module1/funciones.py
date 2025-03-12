#Punto 1 | ¿Esto es Sano?
def esto_es_sano(kcalorias:int, vegetariano:bool)->bool:
    if kcalorias < 100 or vegetariano == True:
        return True
    else:
        return False
    

#Punto 2 | Las Calorías
def las_calorías(kcalorias_x_ingrediente:list)->float:
    total_kcal = round (sum(kcalorias_x_ingrediente), 2)
    return total_kcal

#Punto 3 | Costos
def costos (ingr1: dict, ingr2: dict, ingr3: dict) -> float:
    nombre_precio = [ingr1, ingr2, ingr3]
    total_costo = sum (i.precio for i in nombre_precio)
    return total_costo

def punto2_costos (ingr1: dict, ingr2: dict, ingr3: dict) -> float:
    nombre_precio = [ingr1, ingr2, ingr3]
    total_costo = sum (i.get("precio",0) for i in nombre_precio)
    return total_costo

#Punto 4 | Rentabilidad
def rentabilidad(pvsp:float, ingr1: dict, ingr2: dict, ingr3: dict)->float:
    total_cost = costos (ingr1, ingr2, ingr3)
    calculo_rentable = (pvsp - total_cost)

    return calculo_rentable

#Punto 5 | El mejor producto
def producto_mas_rentable(prod1:dict, prod2:dict, prod3:dict, prod4:dict)->str:
    productos = [prod1, prod2, prod3, prod4]
    top_name = None
    top_value = 0
    for i in productos:
        if i.get("rentabilidad",0) > top_value:
            top_value = i.get("rentabilidad",0)
            top_name = i.get("nombre",0)

    return top_name



def mejor_producto(*productos)->str:
    if not productos:
        return "No hay productos disponibles"

    producto_mas_rentable = productos[0]  # Tomamos el primer producto como referencia

    for producto in productos[1:]:  # Iteramos desde el segundo producto
        if producto.calcular_rentabilidad() > producto_mas_rentable.calcular_rentabilidad():
            producto_mas_rentable = producto  # Actualizamos el más rentable

    return producto_mas_rentable.nombre
