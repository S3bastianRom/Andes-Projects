from base import Base
from complemento import Complemento
from copa import Copa
from malteada import Malteada
from heladeria import Heladeria

def main():
    # Ingredientes
    helado_fresa = Base(precio=1200, calorias=200, nombre="Helado de Fresa", inventario=10, es_vegetariano=True, sabor="Fresa")
    chispas_chocolate = Complemento(precio=500, calorias=150, nombre="Chispas de Chocolate", inventario=20, es_vegetariano=False)
    mani_japones = Complemento(precio=900, calorias=100, nombre="Mani Japonés", inventario=15, es_vegetariano=True)

    copa_fresa = Copa(nombre="Copa de Fresa", precio_publico=5000, ingredientes=[helado_fresa, chispas_chocolate, mani_japones], tipo_vaso="Mediano")
    malteada_chocolate = Malteada(nombre="Malteada de Chocolate", precio_publico=6000, ingredientes=[helado_fresa, chispas_chocolate, mani_japones], volumen=12)

    # Instancia de heladeria
    heladeria = Heladeria(productos=[copa_fresa, malteada_chocolate], ingredientes=[helado_fresa, chispas_chocolate, mani_japones])

    # Tests de agregacion
    print("\n--- Prueba: Agregar ingredientes ---")
    heladeria.ingredientes = [helado_fresa, chispas_chocolate, mani_japones]
    print("Ingredientes en la heladería:", [i.nombre for i in heladeria.ingredientes])


    # Base
    helado_vainilla = Base(precio=1100, calorias=180, nombre="Helado de Vainilla", inventario=8, es_vegetariano=True, sabor="Vainilla")
    helado_chocolate = Base(precio=1300, calorias=220, nombre="Helado de Chocolate", inventario=12, es_vegetariano=True, sabor="Chocolate")
    helado_menta = Base(precio=1400, calorias=190, nombre="Helado de Menta", inventario=5, es_vegetariano=True, sabor="Menta")
    helado_coco = Base(precio=1500, calorias=210, nombre="Helado de Coco", inventario=7, es_vegetariano=True, sabor="Coco")

    # Tests de agregacion
    print("\n--- Prueba: Agregar ingredientes ---")
    heladeria.ingredientes = [helado_vainilla, helado_chocolate, helado_menta, helado_coco]
    print("Ingredientes en la heladería:", [i.nombre for i in heladeria.ingredientes])

    # Complemento
    granola = Complemento(precio=600, calorias=120, nombre="Granola", inventario=10, es_vegetariano=True)
    oreo = Complemento(precio=700, calorias=160, nombre="Galletas Oreo", inventario=15, es_vegetariano=False)
    frutos_rojos = Complemento(precio=800, calorias=90, nombre="Frutos Rojos", inventario=12, es_vegetariano=True)
    caramelo = Complemento(precio=400, calorias=130, nombre="Salsa de Caramelo", inventario=20, es_vegetariano=True)


    # Tests de agregacion
    print("\n--- Prueba: Agregar ingredientes ---")
    heladeria.ingredientes = [granola, oreo, frutos_rojos, caramelo]
    print("Ingredientes en la heladería:", [i.nombre for i in heladeria.ingredientes])



    # Tests de agregacion
    print("\n--- Prueba: Agregar productos ---")
    heladeria.productos = [copa_fresa, malteada_chocolate]
    print("Productos en la heladería:", [p.nombre for p in heladeria.productos])

    # Tests de venta
    print("\n--- Prueba: Vender producto ---")
    print("Intentando vender 'Copa de Fresa'...")
    resultado = heladeria.vender("Copa de Fresa")
    print("Resultado de la venta:", resultado)
    print("Inventario después de la venta:")
    for ingrediente in heladeria.ingredientes:
        print(f"{ingrediente.nombre}: {ingrediente.inventario}")

    print("\n--- Prueba: Producto más rentable ---")
    mas_rentable = heladeria.mejor_producto()
    print("El producto más rentable es:", mas_rentable)

    print("\n--- Prueba: Ventas del día ---")
    print("Ventas del día:", heladeria.ventas_dia)

    print("\n--- Prueba: Vender producto sin ingredientes suficientes ---")
    print("Intentando vender 'Malteada de Chocolate'...")
    resultado = heladeria.vender("Malteada de Chocolate")
    print("Resultado de la venta:", resultado)
    print("Inventario después de la venta:")
    for ingrediente in heladeria.ingredientes:
        print(f"{ingrediente.nombre}: {ingrediente.inventario}")

if __name__ == "__main__":
    main()