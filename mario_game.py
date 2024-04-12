class juego  :
    def __init__(self , jugador) -> None:
        self.jugador  = jugador




class jugador (juego) :
    def __init__(self, jugador) -> None:
        super().__init__(jugador)


class acciones () : 
    def __init__(self , movimiento) -> None:
        self.movimiento = movimiento
    
    def moverse () : 
        print ("me he movido ")

    



if __name__ == "__main__" :
    jugador = juego ("mario")
    jugador.acciones("2")
    

    

        



