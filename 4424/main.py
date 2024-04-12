from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import sqlite3
import usuarios

from pathlib import Path
ruta  = Path(__file__).parent.resolve()
print(ruta)


def conex_db():
   
    usuario = ventana.user_login.text()
    pw = ventana.pass_login.text()
    try :
        con = sqlite3.connect(f"{ruta}\\db.db") #conexión a la BD

       
        print ("conexion exitosa")
        cursor = con.cursor()
        cursor.execute (f"select * from usuario where user = '{usuario}' and pass = '{pw}'") #ejecutar la sentencia SQL
        resultado = cursor.fetchone() #obtener los resultados
        print(resultado)
        if resultado :
            print(f"Bienvenido {resultado[1]}!!")
            usuarios.ventana2.show()

        else:
            print("Error de credenciales")
        

        pw = ventana.pass_login.text()
        print(pw)
    except Exception as e :
        print(f"no se puede conectar {e}")    

        


if __name__ == "__main__" :


    app = QApplication([])
    ventana = uic.loadUi (f"{ruta}\\login.ui")
    ventana.pushButton_login.clicked.connect(conex_db)


#ventana.show()
app.exec()


