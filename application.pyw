import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from Calculations import nDayAverage as generator
from Yahoo import request as yahoo


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        self.stock = None
        self.begin = None
        self.end = None
        self.data = None
        self.temp_picture_name = "temp.png"
                
        self.pilt = QtWidgets.QLabel(Dialog)
        self.pilt.setGeometry(QtCore.QRect(14, 5, 671, 431))
        self.pilt.setText("")
        self.pilt.setObjectName("pilt")
        
        self.daysaverage = QtWidgets.QLineEdit(Dialog)
        self.daysaverage.setGeometry(QtCore.QRect(370, 440, 51, 31))
        self.daysaverage.setObjectName("daysaverage")
        self.daysaverage.setText("20")
        
        self.uuesti = QtWidgets.QPushButton(Dialog)
        self.uuesti.setGeometry(QtCore.QRect(270, 440, 93, 31))
        self.uuesti.setObjectName("uuesti")
        self.uuesti.clicked.connect(lambda: self.file_open(True))

        self.daysend = QtWidgets.QLineEdit(Dialog)
        self.daysend.setGeometry(QtCore.QRect(140, 440, 121, 31))
        self.daysend.setObjectName("daysend")
        
        self.daysbegin = QtWidgets.QLineEdit(Dialog)
        self.daysbegin.setGeometry(QtCore.QRect(10, 440, 121, 31))
        self.daysbegin.setObjectName("daysbegin")
        
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(440, 440, 161, 31))
        self.comboBox.setObjectName("comboBox")
        self.fill_combobox()

        self.display = QtWidgets.QPushButton(Dialog)
        self.display.setGeometry(QtCore.QRect(620, 440, 71, 31))
        self.display.setObjectName("display")
        self.display.clicked.connect(lambda: self.file_open(False))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "n Days Average"))
        self.uuesti.setText(_translate("Dialog", "Taasarvuta"))
        self.display.setText(_translate("Dialog", "KUVA"))

    def fill_combobox(self):
        with open('stocks.txt', 'r') as file:
            file = file.read().replace('\n', 'uusrida')
            stocks = file.split("uusrida")

        if stocks is not None and len(stocks) > 0:
                self.comboBox.blockSignals(True)
                self.comboBox.addItem("")
                for stock in stocks:
                    data = stock.split(",")
                    self.comboBox.addItem(data[0],data[1])
    
    def file_open(self, again):
        try:
            if self.comboBox.currentData() is not None:
                tempBegin = self.daysbegin.text()
                if tempBegin is not "" and len(tempBegin) == 8:
                    tempEnd = self.daysend.text()
                    if tempEnd is not "" and len(tempEnd) == 8:
                        self.begin = tempBegin
                        self.end = tempEnd
                        if os.path.exists(self.temp_picture_name):
                            os.remove(self.temp_picture_name)
                        if not again:
                            self.stock = self.comboBox.currentData()
                            self.data = yahoo.load_yahoo_quote(self.stock, self.begin, self.end, info ='quote', format_output ='list')
                        try:
                            days = int(self.daysaverage.text())
                            if days < 2:
                                days = 20
                                self.daysaverage.setText(str(days))
                            if len(self.data) < days:
                                days = 20
                                self.daysaverage.setText(str(days))
                        except Exception as exception:
                            days = 20
                            self.daysaverage.setText(str(days))
                        generator.generate_file(self.data, self.comboBox.currentText(), days, self.temp_picture_name)
                        self.pilt.setScaledContents(True)
                        self.pilt.setPixmap(QPixmap(self.temp_picture_name))
        except Exception as exception:
            QMessageBox.warning(None, "Veateade", str(exception))

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())            
      
