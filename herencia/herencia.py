class Usuario  :
    def __init__(self , nombre , correo , id)  :
        self.nombre = nombre
        self.correo  = correo
        self.id = id
        self.logueado = False

    def login (self) :
        self.logueado = True
        return self.logueado

    def logout(self) :  
        self.logueado =False     
        return self.logueado
        

        

class Estudiante(Usuario) :
    def estudiar(self) :
        print("ando estudiado...")
    

class Profesor (Usuario):
    def revisar(self) : 
        print("revisando actividades...")

    
if __name__ == "__main__" :
    print("<3" * 30)
    estudiate = Estudiante("anderson" , "aaa@operador.com" , 1)
    print(f"hola {estudiate.nombre}")