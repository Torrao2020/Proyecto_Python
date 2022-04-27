# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Operaciones.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 423)
        self.lblnumeroUno = QtWidgets.QLabel(Form)
        self.lblnumeroUno.setGeometry(QtCore.QRect(10, 40, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblnumeroUno.setFont(font)
        self.lblnumeroUno.setObjectName("lblnumeroUno")
        self.txtNumeroUno = QtWidgets.QTextEdit(Form)
        self.txtNumeroUno.setGeometry(QtCore.QRect(10, 80, 291, 31))
        self.txtNumeroUno.setObjectName("txtNumeroUno")
        self.lblnumeroDos = QtWidgets.QLabel(Form)
        self.lblnumeroDos.setGeometry(QtCore.QRect(10, 120, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblnumeroDos.setFont(font)
        self.lblnumeroDos.setObjectName("lblnumeroDos")
        self.txtNumeroDos = QtWidgets.QTextEdit(Form)
        self.txtNumeroDos.setGeometry(QtCore.QRect(10, 160, 291, 31))
        self.txtNumeroDos.setObjectName("txtNumeroDos")
        self.lblSuma = QtWidgets.QLabel(Form)
        self.lblSuma.setGeometry(QtCore.QRect(10, 260, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblSuma.setFont(font)
        self.lblSuma.setObjectName("lblSuma")
        self.btnSumar = QtWidgets.QPushButton(Form)
        self.btnSumar.setGeometry(QtCore.QRect(10, 220, 75, 23))
        self.btnSumar.setObjectName("btnSumar")
        self.btnRestar = QtWidgets.QPushButton(Form)
        self.btnRestar.setGeometry(QtCore.QRect(120, 220, 75, 23))
        self.btnRestar.setObjectName("btnRestar")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 220, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.close)
        self.btnRestar.clicked.connect(self.lblSuma.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Operaciones gráficas"))
        self.lblnumeroUno.setText(_translate("Form", "Digite un entero:"))
        self.lblnumeroDos.setText(_translate("Form", "Digite un entero:"))
        self.lblSuma.setText(_translate("Form", "La suma es :"))
        self.btnSumar.setText(_translate("Form", "Sumar"))
        self.btnRestar.setText(_translate("Form", "Limpiar"))
        self.pushButton_3.setText(_translate("Form", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

