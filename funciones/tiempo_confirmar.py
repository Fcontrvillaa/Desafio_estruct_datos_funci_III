
def tiempo_confirmacion(pizza):
    n_ingredientes = len(pizza["ingredientes"])
    estimar_tiempo = 20 + (n_ingredientes*2)  #tiempo por cada ingrediente 2min
    print(f"El tiempo estimado para que la pizza este lista :{estimar_tiempo} minutos.")

    confirmar = input("Desea confirmar su orden (si/no)?").lower()

    if confirmar == "si":
        print("Pedido Confirmado. Gracias por preferir pizzas JAT!")
        
    else:
        print("Orden Cancelada")