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

        self.ui.uuesti.clicked.connect(lambda: self.display_data(True))
        self.ui.display.clicked.connect(lambda: self.display_data(False))

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

    def display_data(self, again):
        try:
            if self.ui.comboBox.currentData() is not None:
                tempBegin = self.ui.daysbegin.text()
                if self.is_valid_date(tempBegin):
                    tempEnd = self.ui.daysend.text()
                    if self.is_valid_date(tempEnd):
                        self.ui.begin = tempBegin
                        self.ui.end = tempEnd
                        if os.path.exists(self.ui.temp_picture_name):
                            os.remove(self.ui.temp_picture_name)
                        if again:
                            if self.ui.stock_index is not self.ui.comboBox.currentIndex():
                                self.ui.comboBox.setCurrentIndex(self.ui.stock_index)
                        else:
                            self.ui.stock = self.ui.comboBox.currentData()
                            self.ui.stock_index = self.ui.comboBox.currentIndex()
                            self.ui.data = yahoo.load_yahoo_quote(self.ui.stock, self.ui.begin, self.ui.end, info ='quote', format_output ='list')
                        days = self.set_default_average_days(self.ui.daysaverage.text())
                        Generator.generate_file(self.ui.data, self.ui.comboBox.currentText(), days, self.ui.temp_picture_name)
                        self.ui.pilt.setScaledContents(True)
                        self.ui.pilt.setPixmap(QPixmap(self.ui.temp_picture_name))
        except Exception as exception:
            QMessageBox.warning(None, "Veateade", str(exception))

    def set_default_average_days(self, days_from_ui):
        default_days = 20
        try:
            days_from_ui = int(days_from_ui)
            if (days_from_ui < 2) or (len(self.ui.data) < days_from_ui):
                self.ui.daysaverage.setText(str(default_days))
                return default_days
            return days_from_ui
        except Exception as exception:
            QMessageBox.warning(None, "Veateade", str(exception))
            self.ui.daysaverage.setText(str(default_days))
            return default_days

    def is_valid_date(self, date):
        return date is not "" and len(date) == 8


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
