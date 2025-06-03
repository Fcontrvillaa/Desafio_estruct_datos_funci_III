from funciones.menus import menu_principal
from funciones.menus import menu_personalizar
from funciones.tiempo_confirmar import tiempo_confirmacion


def main():

    pizza = {
    "Masa": "Masa Tradicional",
    "Salsa" : "Salsa de Tomate",
    "ingredientes": ["1","2","3"]   
    }


while True:
    menu_principal()
    opcion_principal = input("Seleccione una opcion :")  #falta tray para nuemros validos....

    if opcion_principal == "1":
        menu_personalizar
            
    elif opcion_principal == "2":
        print(f"La pizza actual es : {pizza}")

    elif opcion_principal == "3":
        tiempo_confirmacion()

    else:
        print("terminado")
        break

    
    
    
