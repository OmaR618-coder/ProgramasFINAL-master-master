from PyQt5 import QtWidgets,uic
from PyQt5.uic import loadUi
"""from CASOS.regresion_lineal import Caso_uno #Importamos por que esta en otro archivo"""
from Segundo_parcial.Regresion_Lineal.CASOS.regresion_lineal import Regresion_lineal

class Interfaz(QtWidgets.QDialog): #HEREDAS DE UN MAIN WINDOW
    def __init__(self):
        super().__init__()
        loadUi("gui/dialogo RegresionLineal.ui",self) #NOMBRE ARCHIVO
        self.showMaximized()
       
       
        self.caso1.clicked.connect(self.case1) #Nombre QPushButton y .CLICKED
       
        self.caso2.clicked.connect(self.case2) #Nombre QPushButton y .CLICKED
       
        self.caso3.clicked.connect(self.case3) #Nombre QPushButton y .CLICKED
       

        self.caso4.clicked.connect(self.case4) #Nombre QPushButton y .CLICKED
       

    def case1(self):
        c1 = Regresion_lineal(self)
        c1.caso1()
        c1.calcularRegresion()
   
    def case2(self):
        c2 = Regresion_lineal(self)
        c2.caso2()
        c2.calcularRegresion()

    def case3(self):
        c3 = Regresion_lineal(self)
        c3.caso3()
        c3.calcularRegresion()

    def case4(self):
        c4 = Regresion_lineal(self)
        c4.caso4()
        c4.calcularRegresion()
       
    def salir(self):
        self.close()