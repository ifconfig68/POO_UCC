import sqlite3
from sqlite3 import Error
from pathlib import Path
ruta = Path(__file__).parent.resolve()

class Conexion :
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
        finally:
            if self.con :
                self.con.close()


    def desconectar(self):
        if self.con :
            self.con.close ()


         


