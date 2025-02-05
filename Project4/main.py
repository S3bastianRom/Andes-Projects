from boa_constrictor import Boa_Constrictor
from huron import Huron

def menu_exit():
    print ("Saliending")
    exit()

bola = Boa_Constrictor("Geraldine", 5, 2, "Brasil", 100)
roco = Huron("Oscar", 2, 1, "Argentina", 50)

menu = {
    "1": ("Revisar Boa", bola.hacer_sonido),  
    "2": ("Revisar Huron", roco.hacer_sonido),  
    "3": (f"Calcular flete {bola.obtener_nombre()}", bola.calcular_flete ),
    "4": (f"Calcular flete {roco.obtener_nombre()}", roco.calcular_flete ),
    "5": ("Quit", menu_exit)
}

for a in sorted(menu.keys()):
    print (f"{a}: {menu[a][0]}")

ans = input(f"Make A Choice: ").strip()
action = menu.get(ans)[1]

if action:
    print (action())