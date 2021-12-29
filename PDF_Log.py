from PDF_UI import *
import fitz
import os
import openpyxl
from PyQt5.QtWidgets import QFileDialog
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def generaReportes(self):
        print('none now')
    def generarExcel(self):
        print('none now')
    def creaListaDePagina(self,pagActiva):
        #Recibimos la pagina activa del documento y creamos un txt con la info para despues leerla
        salida = open("prueba.txt","wb")
        salida.write(pagActiva.get_text().encode("utf8"))
        salida.close()
        #Leemos el TXt creado y lo asignamos a otra variable
        txtHojaActive = open("prueba.txt","r",encoding="utf8")
        contHojaActiva= txtHojaActive.readlines()
        txtHojaActive.close()
        #Borrando espacios vacios
        noneElement=[]
        for i in range(0,len(contHojaActiva)):
            if contHojaActiva[i] == " \n":
                noneElement.append(i)
        a = len(noneElement)
        for i in range(0,a):
            contHojaActiva.remove(" \n")
        cont2=[]#variable auxiliar para guardar temporalmente la info sin espacios
        for i in range(0,len(contHojaActiva)):
            aux=contHojaActiva[i].split(sep=' \n')
            cont2.append(aux[0])
        contHojaActiva = cont2
        print(cont2)  
       
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnSalir.clicked.connect(self.close)
        self.btnAbrir.clicked.connect(self.LeePDF)
        self.btnGenerar.clicked.connect(self.generaReportes)
    def LeePDF(self):       
        pdf = QFileDialog.getOpenFileName(self, 'Open a file', '','All Files (*.*)')
        docum = fitz.open(pdf[0])
        numberOfpages=docum.pageCount
        pagina=[]
        for i in range(0,numberOfpages):
            self.creaListaDePagina(docum.load_page(i))
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()