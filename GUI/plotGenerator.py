import matplotlib.pyplot as plt
from Variables.variables import *


class PlotGenerator():
    def __init__(self, moving_average):
        self.moving_average = moving_average
        self.closing_prices = None

    def create_image(self, stock_name, days, raw_data, recalculate):
        if not recalculate:
            self.closing_prices = self.moving_average.get_closing_prices(raw_data)
        average_prices = self.moving_average.get_average_prices(self.closing_prices, days)

        plt.title(stock_name)
        plt.plot(average_prices)
        plt.plot(self.closing_prices)
        plt.legend([str(days) + ' päeva jooksev keskmine', 'reaalne'], loc='upper left')
        plt.savefig(DEFAULT_PICTURE_NAME)
        plt.clf()
