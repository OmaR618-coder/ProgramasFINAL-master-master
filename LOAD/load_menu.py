from PyQt5 import QtWidgets,uic
from Segundo_parcial.Integracion_Num.ventana import Ventana #Importamos por que esta en otro archivo
from Segundo_parcial.Regresion_Lineal.load.load_interfaz_regresion_lineal import Interfaz
from Tercer_parcial.Programa_3.load.loadInterfazPrograma3 import Interfaz3
from Tercer_parcial.Programa_4.load.loadInterfazPrograma4 import Interfaz4 #FROM TERCER PARCIAL PROGRAMA 4

class Menu(QtWidgets.QMainWindow): #HEREDAS DE UN MAIN WINDOW
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/MENÚ PROGRAMAS.ui",self) #NOMBRE ARCHIVO
        self.showMaximized()
        
        
        self.actionRegLin.triggered.connect(self.clickRegresionLineal) #Nombre action y .triggered
        self.actionSalir.triggered.connect(self.salir)

        self.actionIntegNum.triggered.connect(self.clickIntegracionNumerica) #Nombre action y .triggered
        self.actionSalir.triggered.connect(self.salir)

        self.actionPrograma_3.triggered.connect(self.clickPrograma3) #Nombre action y .triggered
        self.actionSalir.triggered.connect(self.salir)

        self.actionPrograma_4.triggered.connect(self.clickPrograma4) #Nombre action y .triggered
        self.actionSalir.triggered.connect(self.salir)

    def clickRegresionLineal(self):
        RegLin = Interfaz()
        RegLin.exec()
    
    def clickIntegracionNumerica(self):
        IntegNum = Ventana()
        IntegNum.exec()

    def clickPrograma3(self):
        prog3 = Interfaz3()
        prog3.exec()

    def clickPrograma4(self):
        prog4 = Interfaz4()
        prog4.exec()

    def salir(self):
        self.close()
