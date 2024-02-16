class Usuario :

    
        
    def __init__(self , user ) :
        self.user  = user 
        self.calificacion = 0
        print ("obejeto creado")
        

    def enviarCalificacion (self ,nuevaCalifacion)  :
        if nuevaCalifacion <= 10 :
            self.calificacion = nuevaCalifacion
            print(f"Bienvenido  {usuario.user} su calificacion {usuario.calificacion} ha sido enviada exitosamente")
        else :
            print("error")

        

    
usuario  = Usuario("anderson")

usuario.enviarCalificacion(2)

print(usuario.calificacion)







    
    

    
