#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Omar Alberto Torres
#
# Created:     25/04/2022
# Copyright:   (c) Usuario 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
from Operaciones_UI import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt4 import QtCore

class Ventana(QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btnSumar.clicked.connect(self.sumar)

    def sumar(self):
        n1 = self.ui.txtNumeroUno.toPlainText()
        n2 = self.ui.txtNumeroDos.toPlainText()
        suma = int(n1) + int(n2)
        self.ui.lblSuma.setText("La suma es: "+ str(suma))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
