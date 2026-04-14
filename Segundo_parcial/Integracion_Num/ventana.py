from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
import os
from Segundo_parcial.Integracion_Num.integracion import Integracion

class Ventana(QDialog):
    def __init__(self):
        super().__init__()
         
        loadUi("GUI/dialogo.ui", self)

        self.boton_calcular.clicked.connect(self.calcular)

    def calcular(self):
        try:
            x = float(self.input_x.text())
            dof = float(self.input_dof.text())

            modelo = Integracion(x, dof)
            resultado = modelo.iterar()

            self.output.setText(str(resultado))

        except:
            QMessageBox.warning(self, "Error", "Entrada inválida")
