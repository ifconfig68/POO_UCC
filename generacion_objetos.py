# modificadores de acceso 
class Juego :
    genero = "arcade"
    #doc string 
    """

        
    """
    def __init__(self , nombre) :
          self.__vidas = 0
          self.play()
          self.nivel = 0
          self.jugador = nombre 
    
   
    
    def play (self) :
        if self.__vidas == 0 :
            self.__vidas = 3 
            #print ("reiniciado contador vidas")

           
      
      
       
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


    @classmethod
    def cambiar_genero (cls , nuevo):
        cls.genero = nuevo


    def __str__(self) :
      return f"Player {self.jugador} - Life's: {self.__vidas} - Nivel: {self.nivel}"
    
# programa pricipal
    
if __name__ == "__main__" :
    
    
    
    juegos = [] # vector o lista
    for j in range (10):
        n = input("nombre del jugador ")
        juegos.append(Juego(n))
    
    for i in juegos :
        print(i)
    
    juegos[0].veryfy()
    juegos[1].veryfy()
    juegos[2].veryfy()


    print ("--"*30)
    
