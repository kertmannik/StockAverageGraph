from PyQt5 import QtCore, QtWidgets
from Variables.variables import *
from datetime import date


def set_begin_date():
    today = date.today()
    last_year = today.year - 1
    return str(last_year) + "0101"


def set_end_date():
    today = date.today()
    return today.strftime("%Y%m%d")


class Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)

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
        self.daysend.setText(set_end_date())

        self.daysbegin = QtWidgets.QLineEdit(Dialog)
        self.daysbegin.setGeometry(QtCore.QRect(10, 440, 121, 31))
        self.daysbegin.setObjectName("daysbegin")
        self.daysbegin.setText(set_begin_date())

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(440, 440, 161, 31))
        self.comboBox.setObjectName("comboBox")

        self.display = QtWidgets.QPushButton(Dialog)
        self.display.setGeometry(QtCore.QRect(620, 440, 71, 31))
        self.display.setObjectName("display")

        self.retranslate_ui(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.fill_combobox()

    def retranslate_ui(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "n Days Average"))
        self.uuesti.setText(_translate("Dialog", "Taasarvuta"))
        self.display.setText(_translate("Dialog", "KUVA"))

    def fill_combobox(self):
        with open(DEFAULT_STOCKS_FILENAME, 'r') as file:
            stocks = file.read().split('\n')

        if stocks is not None and len(stocks) > 0:
            self.comboBox.blockSignals(True)
            self.comboBox.addItem("")
            for stock in stocks:
                data = stock.split(",")
                if len(data) == 2:
                    self.comboBox.addItem(data[0], data[1])
            self.comboBox.blockSignals(False)
