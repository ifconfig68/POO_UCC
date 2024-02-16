class Usuario : 

    contador =  0
    color ="azul"
    def __init__(self , edad , nombre , cedula):
        self.edad = edad
        self.nombre = nombre
        self.cedula = cedula
        self.tipo = "clientes"
        Usuario.contador +=1
        print("objeto creado")
    def __str__(self):
        return f"""
        Hola {self.nombre} su edad es {self.edad}.  Hasta luego!"

    
    
           """
 
usuario = Usuario(18 , "user1" , 112233)
usuario = Usuario(18 , "user2" , 112233)
usuario = Usuario(18 , "user3" , 112233)
   
print(f"cantidad de obejetos creados {Usuario.contador} ")
print(usuario)
print (usuario.tipo)