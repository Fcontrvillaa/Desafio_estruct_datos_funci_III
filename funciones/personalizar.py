
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
    #esta lista almacena  los ingredientes seleccionados
    ingre_seleccionados = []

    while True:

        

        print("""---Que desea hacer?--
        'a' para añadir un ingrediente
        'q' para quitar un ingrediente
        's' para salir           
              
              """)
        
        
        deseo = input(" :  ").lower()

        if deseo == "s":
            print("Selccion de ingreientes finalizada")
            return(ingre_seleccionados)
        elif deseo == "a":
            print("\n--- Opciones de Ingredientes ---")
                
            for k, v in lista_ingredientes.items():
                print(f"{k}.-{v}")   #muestra opciones
            
            opcion = input(" :  ").lower()

            if opcion in lista_ingredientes:
                seleccion = lista_ingredientes[opcion]
                ingre_seleccionados.append(seleccion)
                print("\nIngredientes seleccionados actualmente: " + ", ".join(ingre_seleccionados))

            else:
                print("\nSeleccionados hasta ahora: Ninguno")

        elif deseo == "q":
            
            print("\n--- Opciones de Ingredientes ---")
            for k, v in lista_ingredientes.items():
                print(f"{k}.-{v}")   #muestra opciones 

            print("\nIngredientes seleccionados actualmente: " + ", ".join(ingre_seleccionados))
            opcion_numero = input("ingrese el numero del ingrediente a quitar :")

            if opcion_numero in lista_ingredientes:    #existe en lista_ingredientes
                
                nombre_ingrediente_a_quitar = lista_ingredientes[opcion_numero]
                
                if nombre_ingrediente_a_quitar in ingre_seleccionados:
                    ingre_seleccionados.remove(nombre_ingrediente_a_quitar) #  elimina el nombre del ingrediente
                    print("\nIngredientes seleccionados actualmente: " + ", ".join(ingre_seleccionados))
                
                else:
                    print(f"'{nombre_ingrediente_a_quitar}' no está en tus ingredientes seleccionados.")
            else:
                print("\nOpción inválida. Por favor, ingrese un número del 1 al 9.")

            if not ingre_seleccionados:
                print("Ingredientes seleccionados actualmente: Ninguno")
                
               




        
    
        

        
    
    
        
    
    
    
    #opcion_ingredientes = input()
    #ingrediente = []
    #print({ingrediente})
    
    

    """"
        print("las opciones son :")
        
        for k, v in frutas.items():
            print(f"{k}.-{v}")   #muestra opciones

        opcion = int(input(": "))

        if opcion in frutas:
            fruta = fruta[opcion]
            vaso["frutas"].append(fruta)
        
---------------------------------------------------------

        quitar_frutas

            frutas = vaso["frutas"]
            print("borra opciones:")

            for i in frutas:
                print(f"1 .-{i}")

            opcion = int(input(": "))

            if opcion in frutas:
                fruta = frutas[opcion]
                vaso[frutas] = remove(fruta)


            """