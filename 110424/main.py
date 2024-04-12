from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

from login import Login

class Software :
    def __init__(self) -> None:
        self.app =QApplication([])
        self.ventana_login = Login()
        self.ventana_login.ventana.show()
        self.app.exec()


        
    



if __name__ =="__main__" :
    ini = Software()
    

    

    