import sys
import os
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap
from Yahoo import request as yahoo
from GUI.design import Dialog
from GUI.plotGenerator import PlotGenerator
from Calculations.nDayAverage import MovingAverage
from Variables.variables import *


def is_valid_date(date):
    return date is not "" and len(date) == 8


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Dialog()
        self.ui.setupUi(self)

        self.stock = None
        self.stock_index = None
        self.data = None

        self.moving_average = MovingAverage()
        self.plot_generator = PlotGenerator(MovingAverage())

        self.ui.uuesti.clicked.connect(lambda: self.display_data(True))
        self.ui.display.clicked.connect(lambda: self.display_data(False))

    def display_data(self, recalculate):
        try:
            if self.ui.comboBox.currentData() is not None:
                temp_begin = self.ui.daysbegin.text()
                if is_valid_date(temp_begin):
                    temp_end = self.ui.daysend.text()
                    if is_valid_date(temp_end):
                        if os.path.exists(DEFAULT_PICTURE_NAME):
                            os.remove(DEFAULT_PICTURE_NAME)
                        if recalculate:
                            if self.stock_index is not self.ui.comboBox.currentIndex():
                                self.ui.comboBox.setCurrentIndex(self.stock_index)
                        else:
                            self.stock = self.ui.comboBox.currentData()
                            self.stock_index = self.ui.comboBox.currentIndex()
                            self.data = yahoo.load_yahoo_quote(self.stock, temp_begin, temp_end, info ='quote', format_output ='list')
                        days = self.set_default_average_days(self.ui.daysaverage.text())
                        self.plot_generator.create_image(self.stock, days, self.data)
                        self.ui.pilt.setScaledContents(True)
                        self.ui.pilt.setPixmap(QPixmap(DEFAULT_PICTURE_NAME))
        except Exception as exception:
            QMessageBox.warning(None, "Veateade", str(exception))

    def set_default_average_days(self, days_from_ui):
        default_days = DEFAULT_DAYS
        try:
            days_from_ui = int(days_from_ui)
            if (days_from_ui < 2) or (len(self.data) < days_from_ui):
                self.ui.daysaverage.setText(str(default_days))
                return default_days
            return days_from_ui
        except Exception as exception:
            QMessageBox.warning(None, "Veateade", str(exception))
            self.ui.daysaverage.setText(str(default_days))
            return default_days


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
