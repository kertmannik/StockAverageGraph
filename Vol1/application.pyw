import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
import nDayAverage as generator

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.filename = None
        self.temp_picture_name = "temp.png"
        
        self.nupp = QtWidgets.QPushButton(Dialog)
        self.nupp.setGeometry(QtCore.QRect(540, 440, 93, 31))
        self.nupp.setObjectName("nupp")
        self.nupp.clicked.connect(lambda: self.file_open(False))
        
        self.pilt = QtWidgets.QLabel(Dialog)
        self.pilt.setGeometry(QtCore.QRect(4, 5, 631, 431))
        self.pilt.setText("")
        self.pilt.setObjectName("pilt")
        
        self.daysaverage = QtWidgets.QTextEdit(Dialog)
        self.daysaverage.setGeometry(QtCore.QRect(480, 440, 51, 31))
        self.daysaverage.setObjectName("daysaverage")
        self.daysaverage.setText("20")
        
        self.uuesti = QtWidgets.QPushButton(Dialog)
        self.uuesti.setGeometry(QtCore.QRect(380, 440, 93, 31))
        self.uuesti.setObjectName("uuesti")
        self.uuesti.clicked.connect(lambda: self.file_open(True))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "n Days Average"))
        self.nupp.setText(_translate("Dialog", "Vali fail"))
        self.uuesti.setText(_translate("Dialog", "Taasarvuta"))
        
    def file_open(self, again):
        try:
            fname = None
            if os.path.exists(self.temp_picture_name):
                os.remove(self.temp_picture_name)
                
            if again:
                fname = self.filename[0]
            else:
                dialog = QFileDialog()
                fname = dialog.getOpenFileName(None, "Import csv", "", "CSV files (*.csv)")
                self.filename = fname
                fname = fname[0]
            filename = fname.split("/")[-1:][0]
            try:
                days = int(self.daysaverage.toPlainText())
            except Exception as exception:
                days = 20
                self.daysaverage.setText(str(days))
            if days < 2:
                days = 20
                self.daysaverage.setText(str(days))
            generator.generate_file(fname, days, self.temp_picture_name)
            self.pilt.setScaledContents(True)
            self.pilt.setPixmap(QPixmap(self.temp_picture_name))
        except Exception as exception:
            print(exception)

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())            
      
