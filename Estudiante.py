class Estudiante :
    nombre : str
    nota1 : float
    nota2 : float
    count = 0
    institucion = "udea"

    def __init__(self , nombre  , nota1 , nota2) :
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        Estudiante.count +=1
        #print("objeto creado")
        print(f"cantidad de estudiantes creados {Estudiante.count} ")
    
    def obtener_nota_promedio(self) :
        promedio = (self.nota1 + self.nota2) / 2
        print(f"hola {self.nombre } su promedio es  {promedio}  {Estudiante.institucion}")
    
    def cambio_institucion(self ) :
        Estudiante.institucion = "ucc"
        print (f"hola {self.nombre} estudias en la {Estudiante.institucion}")
    


obj_estudiante = Estudiante("anderson" , 5 , 2 )
obj_estudiante1 = Estudiante("Gabriel" , 5 , 3 )
obj_estudiante2 = Estudiante("camilo" , 5 , 1 )

obj_estudiante.obtener_nota_promedio()
obj_estudiante1.obtener_nota_promedio()
obj_estudiante2.obtener_nota_promedio()

obj_estudiante.cambio_institucion()

obj_estudiante1.cambio_institucion()
obj_estudiante2.cambio_institucion()











