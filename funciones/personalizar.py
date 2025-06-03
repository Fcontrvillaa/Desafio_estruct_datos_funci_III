
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
        print("Has elejido Salsa de Tomate")
        return("Salsa de Tomate")
    elif opcion_salsa == "2":
        print("Has elejido Salsa Alfredo")
        return("Salsa Alfredo")
    elif opcion_salsa == "3":
        print("Has elejido Salsa Barbecue")
        return("Salsa Barbecue")
    elif opcion_salsa == "4":
        print("Has elejido Salsa Pesto")
        return("Salsa Pesto")
    
    else:
        print("Elige una opcion valida de masa")



def ingredientes():
    """añade o quita ingredientes de una lista """
    
    lista_ingredientes = {
        "1": "Tomate",
        "2": "Champiñones",
        "3": "Aceituna",
        "4": "Cebolla",
        "5": "Pollo",
        "6": "Jamón",
        "7": "Carne",
        "8": "Tocino",
        "9": "Queso"
    }
    ingre_seleccionados = []

    while True:

        print("\n--- Opciones de Ingredientes ---")
        for numero, nombre in lista_ingredientes.items():
            print(f"  {numero}.{nombre}")
        if ingre_seleccionados:
            print("\nIngredientes seleccionados actualmente:", ", ".join(ingre_seleccionados))
        else:
            print("\nSeleccionados hasta ahora: Ninguno")
    #opcion_ingredientes = input()
    #ingrediente = []
    #print({ingrediente})
    
    else:
        print("Elige una opcion valida de Ingredientes")

    #