import sys
import os
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap
from Calculations import nDayAverage as Generator
from Yahoo import request as yahoo
from GUI.design import Dialog


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Dialog()
        self.ui.setupUi(self)
        self.fill_combobox()

        self.ui.uuesti.clicked.connect(lambda: self.file_open(True))
        self.ui.display.clicked.connect(lambda: self.file_open(False))

    def fill_combobox(self):
        with open('stocks.txt', 'r') as file:
            file = file.read().replace('\n', 'uusrida')
            stocks = file.split("uusrida")

        if stocks is not None and len(stocks) > 0:
                self.ui.comboBox.blockSignals(True)
                self.ui.comboBox.addItem("")
                for stock in stocks:
                    data = stock.split(",")
                    self.ui.comboBox.addItem(data[0],data[1])

    def file_open(self, again):
        try:
            if self.ui.comboBox.currentData() is not None:
                tempBegin = self.ui.daysbegin.text()
                if tempBegin is not "" and len(tempBegin) == 8:
                    tempEnd = self.ui.daysend.text()
                    if tempEnd is not "" and len(tempEnd) == 8:
                        self.ui.begin = tempBegin
                        self.ui.end = tempEnd
                        if os.path.exists(self.ui.temp_picture_name):
                            os.remove(self.ui.temp_picture_name)
                        if not again:
                            self.ui.stock = self.ui.comboBox.currentData()
                            self.ui.data = yahoo.load_yahoo_quote(self.ui.stock, self.ui.begin, self.ui.end, info ='quote', format_output ='list')
                        # TODO: taasarvutamine aga valitud on uus vp
                        try:
                            days = int(self.ui.daysaverage.text())
                            if days < 2:
                                days = 20
                                self.ui.daysaverage.setText(str(days))
                            if len(self.ui.data) < days:
                                days = 20
                                self.ui.daysaverage.setText(str(days))
                        except Exception as exception:
                            print(exception)
                            days = 20
                            self.ui.daysaverage.setText(str(days))
                        Generator.generate_file(self.ui.data, self.ui.comboBox.currentText(), days, self.ui.temp_picture_name)
                        self.ui.pilt.setScaledContents(True)
                        self.ui.pilt.setPixmap(QPixmap(self.ui.temp_picture_name))
        except Exception as exception:
            QMessageBox.warning(None, "Veateade", str(exception))


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
