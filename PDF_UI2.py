# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Pc\Documents\Repos\LeerPDFmulti\PDF_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 306)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblAbrir = QtWidgets.QLabel(self.centralwidget)
        self.lblAbrir.setGeometry(QtCore.QRect(20, 120, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblAbrir.setFont(font)
        self.lblAbrir.setObjectName("lblAbrir")
        self.btnAbrir = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbrir.setGeometry(QtCore.QRect(280, 117, 101, 31))
        self.btnAbrir.setStyleSheet("background-color: rgb(106, 137, 186);")
        self.btnAbrir.setObjectName("btnAbrir")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 241, 41))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(19, 121, 255);")
        self.label.setObjectName("label")
        self.btnGenerar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerar.setGeometry(QtCore.QRect(120, 230, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnGenerar.setFont(font)
        self.btnGenerar.setStyleSheet("background-color: rgb(94, 142, 255);")
        self.btnGenerar.setObjectName("btnGenerar")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(440, 250, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnSalir.setFont(font)
        self.btnSalir.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btnSalir.setObjectName("btnSalir")
        self.lblserie = QtWidgets.QLabel(self.centralwidget)
        self.lblserie.setGeometry(QtCore.QRect(10, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblserie.setFont(font)
        self.lblserie.setObjectName("lblserie")
        self.txtSerie = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSerie.setGeometry(QtCore.QRect(270, 180, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtSerie.setFont(font)
        self.txtSerie.setAutoFillBackground(True)
        self.txtSerie.setObjectName("txtSerie")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblAbrir.setText(_translate("MainWindow", "Selecciona el archivo PDF"))
        self.btnAbrir.setText(_translate("MainWindow", "Abrir"))
        self.label.setText(_translate("MainWindow", "Generar Reportes "))
        self.btnGenerar.setText(_translate("MainWindow", "Generar Reportes"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.lblserie.setText(_translate("MainWindow", "Ingresa el numero de la serie"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
