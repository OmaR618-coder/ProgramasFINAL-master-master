from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
import os
from Tercer_parcial.Programa_3.CASO.caso_prueba3 import Programa3

class Interfaz3(QDialog): #HEREDAS DE UN DIALOG
    def __init__(self):
        super().__init__()
         
        loadUi("GUI/interfazPrograma3.ui", self)

        self.pushButtonCalcular.clicked.connect(self.calcular3)

    def calcular3(self):
        try:
            pvalor = float(self.pvalor.text())
            dof = float(self.dof.text())

            modelo = Programa3(pvalor, dof)
            modelo.calcularX()
            self.resultadoX.setText(str(modelo.x))

        except:
            QMessageBox.warning(self, "Error", "Entrada inválida")
