from PyQt5 import QtCore, QtWidgets

class Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)

        self.stock = None
        self.stock_index = None
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

        self.daysend = QtWidgets.QLineEdit(Dialog)
        self.daysend.setGeometry(QtCore.QRect(140, 440, 121, 31))
        self.daysend.setObjectName("daysend")

        self.daysbegin = QtWidgets.QLineEdit(Dialog)
        self.daysbegin.setGeometry(QtCore.QRect(10, 440, 121, 31))
        self.daysbegin.setObjectName("daysbegin")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(440, 440, 161, 31))
        self.comboBox.setObjectName("comboBox")

        self.display = QtWidgets.QPushButton(Dialog)
        self.display.setGeometry(QtCore.QRect(620, 440, 71, 31))
        self.display.setObjectName("display")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "n Days Average"))
        self.uuesti.setText(_translate("Dialog", "Taasarvuta"))
        self.display.setText(_translate("Dialog", "KUVA"))