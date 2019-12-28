import sys
import os
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap
from Yahoo import api as yahoo
from GUI.design import Dialog
from GUI.plotGenerator import PlotGenerator
from Calculations.nDayAverage import MovingAverage
from Calculations.growth import Growth
from Variables.variables import *


def is_valid_date(date):
    return date is not "" and len(date) == 10


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Dialog()
        self.ui.setupUi(self)

        self.stock = None
        self.stock_index = None

        self.moving_average = MovingAverage()
        self.growth = Growth()
        self.plot_generator = PlotGenerator(self.moving_average, self.growth)

        self.ui.uuesti.clicked.connect(lambda: self.display_data(True))
        self.ui.display.clicked.connect(lambda: self.display_data(False))

    def display_data(self, recalculate):
        try:
            if self.ui.comboBox.currentData() is not None:
                temp_begin = self.ui.daysbegin.date().toString('yyyy-MM-dd')
                if is_valid_date(temp_begin):
                    temp_end = self.ui.daysend.date().toString('yyyy-MM-dd')
                    if is_valid_date(temp_end):
                        if os.path.exists(DEFAULT_PICTURE_NAME):
                            os.remove(DEFAULT_PICTURE_NAME)
                        if recalculate:
                            if self.stock_index is not self.ui.comboBox.currentIndex():
                                self.ui.comboBox.setCurrentIndex(self.stock_index)
                        else:
                            self.stock = self.ui.comboBox.currentData()
                            self.stock_index = self.ui.comboBox.currentIndex()
                            closing_prices, axis_labels = yahoo.load_yahoo_quote(self.stock, temp_begin, temp_end)
                        days = self.is_valid_number(self.ui.daysaverage.text(), closing_prices)
                        self.plot_generator.create_image(self.stock, days, closing_prices, axis_labels, recalculate)
                        self.ui.pilt.setScaledContents(True)
                        self.ui.pilt.setPixmap(QPixmap(DEFAULT_PICTURE_NAME))
        except Exception as exception:
            QMessageBox.warning(None, "Veateade", str(exception))

    def is_valid_number(self, days_from_ui, closing_prices):
        days_from_ui = int(days_from_ui)
        if days_from_ui < 2:
            raise Exception("Jooksva keskmise arvutamise päevi peab olema vähemalt 2!")
        if (len(closing_prices) - 2) < days_from_ui:
            raise Exception("Vaja pikemat ajaperioodi arvutamiseks!")
        return days_from_ui


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
