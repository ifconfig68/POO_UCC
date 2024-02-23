# modificadores de acceso 
class Juego :
    #doc string 
    """

        
    """
    def __init__(self) :
          self.__vidas = 0
          self.play()
          self.nivel = 0
          self.jugador = "Mario"
    
   
    
    def play (self) :
        if self.__vidas == 0 :
            self.__vidas = 3 
            print ("reiniciado contador vidas")

           
      
      
       
    def veryfy(self) : 
        if self.__vidas <=0 :
            print("game over...")
        else:
            print(f"Player : {self.jugador} esta vivo!!")
        print( f"Player {self.jugador} - Life's: {self.__vidas} - Nivel: {self.nivel}"    )

            

    def lose (self) :
        if self.__vidas > 0 :
            self.__vidas -= 1
        self.veryfy() #llamar un metodo desde otro 

        

    def reset (self , cant_vidas) :
            
            if cant_vidas > 0 and cant_vidas <= 3 :
                self.__vidas = cant_vidas
            else :
                 print ("error pera cant vidas")

    @staticmethod
    def bienvenida(nombre):
        print (f"bienvenido <<{nombre}>>a nuestra version 1.0")



    def __str__(self) :
      return f"Player {self.jugador} - Life's: {self.__vidas} - Nivel: {self.nivel}"
    
# programa pricipal
    
if __name__ == "__main__" :
    
    j1= Juego ()
    Juego.bienvenida(j1.jugador)
    while True : 
        op =  int(input("""

                        1. play
                        2. lose
                        3. Reset 
                        4. Exit  
                       

                """
                ))
        
        if  op == 1 : 
            j1.play()
        elif op == 2 :
            j1.lose()
        elif op ==3 :
            j1.reset
        elif op == 4 : 
            print("Adios")
       

        
    
        

