from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from conexion import * 


class Login (Conexion):
    def __init__(self)  :
        self.ventana = uic.loadUi ("110424/gui/login.ui")
        self.ventana.notificaciones.setText(" ")
        self.ventana.btn_login.clicked.connect(self.login)

       
    def login (self) :
        self.conectar()
        #verificar usuario y contraseña 
        self.desconectar()
        self.ventana_main = uic.loadUi ("110424/gui/main_windows.ui")
        self.ventana.hide()
        self.ventana_main.showMaximized()
        
        



if __name__ =="__main__" :
    print("*"*30)
    print ("Ejecute main.py")
    print("*"*30)

    

    

