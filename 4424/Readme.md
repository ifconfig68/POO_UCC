QT Designer
https://build-system.fman.io/qt-designer-download

Sqlite browser
https://sqlitebrowser.org/dl/

Libreria para conectar Python con Qt
https://pypi.org/project/PyQt6/

Vinvular ui en python
===================
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

app = QApplication([])
ventana = uic.loadUi ("archivo.ui")

ventana.show()
app.exec()

===================

******************************************
Gestión de eventos de la interfaz gráfica
---
ventana.control.evento.connect(funcion)
---
***************************************

Cuadros de diálogo
***************************************
from PyQt6.QtWidgets import QMessageBox

QMessageBox.information(contenedor,"Título", "Mensaje")
resp = QMessageBox.question(contenedor,"Título", "Pregunta")
# QMessageBox.StandardButton.Yes / QMessageBox.StandardButton.No

---------------------------------------------
Conectar con Base de datos SQlite
---------------------------------------------
import sqlite3
con = sqlite3.connect("bd") #conexión a la BD
cursor = con.cursor() #crear cursor
cursor.execute ("sql") #ejecutar la sentencia SQL
resultado = cursor.fetchone() #obtener los resultados

---------------------------------------------
Conectar con Base de datos MongoDB
---------------------------------------------
https://pypi.org/project/pymongo/

---------------
Operaciones sobre una colección

find()
insert_one() / insert_many()
update_one() / update_many()
delete_one() / delete_many()
---------------

