from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

from list_view import List_view

class Software :
    def __init__(self) -> None:
        self.app =QApplication([])
        self.ventana_login = List_view()
        self.ventana_login.ventana.show()
        self.app.exec()

  
    




if __name__ =="__main__" :
    ini = Software()

    print("todo bien")
    
    