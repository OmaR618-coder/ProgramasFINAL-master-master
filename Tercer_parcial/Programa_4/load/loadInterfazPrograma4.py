from PyQt5 import QtWidgets,uic
from PyQt5.uic import loadUi
from Tercer_parcial.Programa_4.CASO.caso_prueba4 import Programa4

class Interfaz4(QtWidgets.QDialog): #HEREDAS DE UN MAIN WINDOW
    def __init__(self):
        super().__init__()
        loadUi("gui/interfazPrograma4.ui",self) #NOMBRE ARCHIVO
        self.showMaximized()
       
       
        self.pushButtonTEST1.clicked.connect(self.case1) #Nombre QPushButton y .CLICKED
       
        self.pushButtonTEST2.clicked.connect(self.case2) #Nombre QPushButton y .CLICKED

    def test1(self):
        c1 = Programa4(self)
        #c1.

    def test2(self):
        c2 = Programa4(self)
        #c2.
       
    def salir(self):
        self.close()