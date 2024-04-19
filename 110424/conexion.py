import sqlite3
from sqlite3 import Error
from pathlib import Path
ruta = Path(__file__).parent.resolve()

class Conexion :
    tablas = ["usuario" , "programa"]
    def __init__(self) :
    
        self.con = False
        self.cursor = False

    def conectar(self) :
        try :
            self.con = sqlite3.connect(f"{ruta}/db.db") #conexión a la BD
            print("Conexión a la DB ok!")
            self.cursor = self.con.cursor() #crear cursor
            #cursor.execute (f"select * from usuario where user='{usuario}' and passwd='{password}' ") #ejecutar la sentencia SQL
             # resultado = cursor.fetchone() #obtener los resultados

        except Error as e:
            print(e)
        


    def desconectar(self):
        if self.con :
            self.con.close ()
            self.con = False
            self.cursor = False

    def consultar_todos(self , tabla):
        # select * from usuario
        # select * from usuario where nombre like '%andrea%'
        # select * from usuario where nombre like 'andrea%'
        # select * from usuario where nombre like '%andrea'
        # select * from usuario where nombre like 'andrea'

        
        try : 
            #query = f"SELECT * from {tabla}"  facil de hacer sqlinjection    query = f"SELECT * from {"' drop datbase"}"
            #self.cursor.execute({"SELECT * from ?" , (tabla,)})
            #resultado = self.cursor.fetchall()
            #return resultado
            if tabla in Conexion.tablas :
                query = f"SELECT * from {tabla}"
                self.cursor.execute(query)
                resultado = self.cursor.fetchall()
                return resultado
        
        except Exception as e :
            print (f"Error :{e}")
            return False
        
    
        

        #resultado = self.cursor.fetchone()




    def consultar_unico(self):
        pass

         


