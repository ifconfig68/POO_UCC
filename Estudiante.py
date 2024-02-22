class Estudiante :
    nombre : str
    nota1 : float
    nota2 : float

    def __init__(self , nombre  , nota1 , nota2) :
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        print("objeto creado")
    
    def obtener_nota_promedio(self) :
        promedio = (self.nota1 + self.nota2) / 2
        return f"el  promedio de   {self.nombre} es {promedio}"

obj_estudiante = Estudiante("anderson" , 5 , 5 )
resultado = obj_estudiante.obtener_nota_promedio()
print (resultado)




