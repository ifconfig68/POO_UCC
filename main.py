class Usuario : 
    def __init__(self , edad , nombre , cedula):
        self.edad = edad
        self.nombre = nombre
        self.cedula = cedula
        self.tipo = "clientes"
        print("objeto creado")
    def __str__(self):
        return f"Hola {self.nombre} su edad es {self.edad}.  Hasta luego!"

usuario = Usuario(18 , "anderson" , 112233)
print(usuario)
print (usuario.tipo)