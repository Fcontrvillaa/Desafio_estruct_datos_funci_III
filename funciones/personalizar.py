
def masa():
    """Selecciona tipo de masa"""

    print("""Opciones de masas:
        1. Masa Tradicional
        2. Masa Delgada
        3. Masa con bordes de Queso
        """)
    opcion_masa = input()

    if opcion_masa == "1":
        print("Has elijido Masa Tradicional")
        return("Masa Tradicional")
    elif opcion_masa == "2":
        print("Has elijido Masa Delgada")
        return("Masa Delgada")
    elif opcion_masa == "3":
        print("Has elijido Masa con bordes de Queso")
        return("Masa con bordes de Queso")
        
    else:
        print("Elige una opcion valida de masa")



def salsa():
    """Selecciona tipo de salsas"""

    print("""Opciones de Salsas:
        1. Salsa de Tomate
        2. Salsa Alfredo
        3. Salsa Barbecue
        4. Salsa Pesto
        """)
    opcion_salsa = input()

    if opcion_salsa == "1":
        print("Has elijido Salsa de Tomate")
        return("Salsa de Tomate")
    elif opcion_salsa == "2":
        print("Has elijido Salsa Alfredo")
        return("Salsa Alfredo")
    elif opcion_salsa == "3":
        print("Has elijido Salsa Barbecue")
        return("Salsa Barbecue")
    elif opcion_salsa == "4":
        print("Has elijido Salsa Pesto")
        return("Salsa Pesto")
        
    else:
        print("Elige una opcion valida de masa")