# modificadores de acceso 
class Juego :
    def __init__(self) :
          self.__vidas = 3
          self.nivel = 0
          self.jugador = "Mario"
    
   
    
    def play (self) :
        print("Go!")
        self.nivel+=1

    def veryfy(self) : 
      if self.__vidas <=0 :
            print("game over...")
      else:
            print(f"Player : {self.jugador} esta vivo!!") 
            

    def lose (self) :
        if self.__vidas > 0 :
            self.__vidas -= 1
        self.veryfy() #llamar un metodo desde otro 


    def reset (self , cant_vidas) :
            if cant_vidas > 0 and cant_vidas <= 3 :
                self.__vidas = cant_vidas
            else :
                 print ("error pera cant vidas")


    def __str__(self) :
      return f"Player {self.jugador} - Life's: {self.__vidas} - Nivel: {self.nivel}"
    
# programa pricipal
    
if __name__ == "__main__" :
    j1= Juego ()
    j1.play()
    j1.veryfy()
   
    j1.lose()
    j1.lose()
    j1.lose()
    j1.lose()
    

    j1.reset (3)
    j1.veryfy()

    print ("*" * 40)

    
   
    

