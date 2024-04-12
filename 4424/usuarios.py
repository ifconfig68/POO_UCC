from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

from pathlib import Path
ruta = Path(__file__).parent.resolve()


if __name__ != "__main__" :
    print ("modulo importado")
    app2 = QApplication([])
    ventana2 = uic.loadUi ("4424/usuarios.ui")
    ventana2.show()
    app2.exec()
else :
    print("ejecuete main.py para iniciar")

