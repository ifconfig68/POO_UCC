class Usuario : 

    contador =  0
    color ="azul"
    def __init__(self , edad , nombre , cedula):
        self.edad = edad
        self.nombre = nombre
        self.cedula = cedula
        self.tipo = "clientes"
        self.logueado = False
        Usuario.contador +=1
        print("objeto creado")
    
    def login(self , user , passw):
        if user == "admin" and passw == "12345" :
            print (f"Bienbenido{self.nombre}")
            self.logueado = True
        else : 


    def logout(self):
        pass
            


    def __str__(self):
        return f"""
        Hola user su edad es {self.edad}.  Hasta luego!"

    
    
           """
 
usuario = Usuario(18 , "user1" , 112233)
usuario = Usuario(18 , "user2" , 112233)
usuario = Usuario(18 , "user3" , 112233)
   
print(f"cantidad de obejetos creados {Usuario.contador} ")
print(usuario)
print (usuario.tipo)