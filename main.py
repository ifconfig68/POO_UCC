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
            print (f"Bienvenido {self.nombre}")
            self.logueado = True
        else : 
            print ("Usuario o contraseña incorrectas")


    def logout(self):
        self.logueado = False
        print ("sesion cerrada")
            


    def __str__(self):   #metodo magico. si un se quiere imprimir un objeto sin algun valor especifico esto se ejecuta solo .
        return f"""
        Hola user su edad es {self.edad}.  Hasta luego!"  

           """
 
usuario1 = Usuario(18 , "admin" , 112233)
print (usuario1.edad)
usuario2 = Usuario(18 , "user2" , 112233)
usuario3 = Usuario(18 , "user3" , 112233)
   
print(f"cantidad de obejetos creados {Usuario.contador} ")
print(usuario1.nombre)
print (usuario2.nombre)
print (usuario3.nombre)

print ("--"*30)

usuario1.login(usuario1.nombre , "12345")
usuario2.login("admin" , "12345")
usuario1.logout()
print("--"*30) 
print(f"Estado de {usuario2.nombre} es {usuario2.logueado}")
print(f"Estado de {usuario1.nombre} es {usuario1.logueado}")

#tarea 
#hacer unsa clase de servicio al cliente en un clinica  de la ciudad de medellin
