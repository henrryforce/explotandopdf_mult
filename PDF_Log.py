from PDF_UI import *
import fitz
import os
import openpyxl
from PyQt5.QtWidgets import QFileDialog
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def separaMultiplos(self,a):
        return a.split(sep=' x ')
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
        cont2=[]
        for i in range(0,len(contHojaActiva)):
            aux=contHojaActiva[i].split(sep=' =')
            cont2.append(aux[0])
        contHojaActiva = cont2
        #Se optienen las multiplicaciones y resultados de la lista limpia de basura
        mult =[]
        resM = []
        for i in range(2,180,3):
            mult.append(contHojaActiva[i])
        for i in range(3,181,3):
            resM.append(contHojaActiva[i])
        #Se preparan 2 listas para las multiplicaciones y resultados
        multip = []
        auxlistaTab =[]
        multipR=[]
        auxlistaTabR =[]
        for i in range(0,61):
            if(i<10):
                auxlistaTab.append(mult[i])
                auxlistaTabR.append(resM[i])
            elif(i==10):
                multip.append(auxlistaTab)
                auxlistaTab =[]
                multipR.append(auxlistaTabR)
                auxlistaTabR =[]
            if(i<20 and i>=10):
                auxlistaTab.append(mult[i])
                auxlistaTabR.append(resM[i])
            elif(i==20):
                multip.append(auxlistaTab)
                auxlistaTab =[]
                multipR.append(auxlistaTabR)
                auxlistaTabR =[]
            if(i<30 and i>=20):
                auxlistaTab.append(mult[i])
                auxlistaTabR.append(resM[i])
            elif(i==30):
                multip.append(auxlistaTab)
                auxlistaTab =[]
                multipR.append(auxlistaTabR)
                auxlistaTabR =[]
            if(i<40 and i >=30):
                auxlistaTab.append(mult[i])
                auxlistaTabR.append(resM[i])
            elif(i==40):
                multip.append(auxlistaTab)
                auxlistaTab =[]
                multipR.append(auxlistaTabR)
                auxlistaTabR =[]
            if(i<50 and i >=40):
                auxlistaTab.append(mult[i])
                auxlistaTabR.append(resM[i])
            elif(i==50):
                multip.append(auxlistaTab)
                auxlistaTab =[]
                multipR.append(auxlistaTabR)
                auxlistaTabR =[]
            if(i<60 and i >=50):
                auxlistaTab.append(mult[i])
                auxlistaTabR.append(resM[i])
            elif(i==60):
                multip.append(auxlistaTab)
                auxlistaTab =[]
                multipR.append(auxlistaTabR)
                auxlistaTabR =[]
        hojaT =[] #Variable que contendra la lista de listas de las tablas
        tabla = []
        for j in range(0,6):
            for i in range(0,10):
                m = self.separaMultiplos(multip[j][i])
                tabla.append(m)
                tabla[i].append(multipR[j][i])
            hojaT.append(tabla)
            tabla = []
        hojaT.append(contHojaActiva[0])
        return hojaT
       
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
            pagina = self.creaListaDePagina(docum.load_page(i))
            for j in pagina:
                print(j)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()