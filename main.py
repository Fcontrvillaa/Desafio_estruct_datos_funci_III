from funciones.menus import menu_principal
from funciones.menus import menu_personalizar
from funciones.tiempo_confirmar import tiempo_confirmacion
from funciones.personalizar import masa
from funciones.personalizar import salsa


def main():

    pizza = {
    "Masa": "",
    "Salsa" : "",
    "ingredientes": []   
    }


    while True:
        menu_principal()
        opcion_principal = input("Seleccione una opcion :")  #falta tray para nuemros validos....

        if opcion_principal == "1":
            
            while True:            
                menu_personalizar()
                opcion_personalizar = input("Seleccione una opcion :").lower()

                if opcion_personalizar == "a":
                    pizza["Masa"] = masa()
            
                elif opcion_personalizar == "b":
                    pizza ["Salsa"] = salsa()

                elif opcion_personalizar == "c":
                    print(opcion_personalizar)

                elif opcion_personalizar == "d":
                    print("vuelve a menu principal")
                    break
                
                else:       # Si la opción no es 'a', 'b', 'c', 'd' 
                    print("Opción no válida. Por favor, ingrese una letra de las opciones mostradas.")


                                    
        elif opcion_principal == "2":
            print(f"La pizza actual es : {pizza}")

        elif opcion_principal == "3":
            tiempo_confirmacion(pizza)

        else:
            print("terminado")
            break


if __name__ == "__main__":
    main()  
    
    
