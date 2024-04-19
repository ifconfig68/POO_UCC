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

        usuario = self.ventana.user.text()
        clave = self.ventana.passwd.text()
        #registros  = self.consultar_todos("programa")
        registros = self.consultar_todos("usuario" , user=usuario ,  passwd=clave)
        if len(registros)>0 :
            print ("bienvenido!!")
            self.ventana_main = uic.loadUi ("110424/gui/main_windows.ui")
            self.ventana_main.showMaximized()
            
            self.ventana.hide()
        else:
            print("credenciales error")
            self.ventana.notificaciones.setText("ERROR")
        if registros !=False :
            for  u in registros :
                print(u)
            else:
                print(f"cantidad de registros {len(registros)}")
            
        else:
            print ("error consulta")

        #verificar usuario y contraseña 
        self.desconectar()
    
        
        



if __name__ =="__main__" :
    print("*"*30)
    print ("Ejecute main.py")
    print("*"*30)

    

    

