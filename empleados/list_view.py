from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from empleado import * 


class List_view(Empleado) :
    
    def __init__(self)  :
        self.ventana = uic.loadUi ("empleados/gui/list_view.ui")
        self.ventana.btn_consultar.clicked.connect(self.consultar_registros)
        self.empleado = Empleado()
        

    def consultar_registros(self) :
         datos =  self.empleado.select_all()
         


       
       
        


if __name__ =="__main__" :
    print("*"*30)
    print ("Ejecute main.py")
    print("*"*30)