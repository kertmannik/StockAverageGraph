import matplotlib.pyplot as plt
from Variables.variables import *


class PlotGenerator():
    def __init__(self, moving_average):
        self.moving_average = moving_average

    def create_image(self, stock_name, days, raw_data):
        closing_prices = self.moving_average.get_closing_prices(raw_data)
        average_prices = self.moving_average.get_average_prices(closing_prices, days)

        plt.title(stock_name)
        plt.plot(average_prices)
        plt.plot(closing_prices)
        plt.legend([str(days) + ' päeva jooksev keskmine', 'reaalne'], loc='upper left')
        plt.savefig(DEFAULT_PICTURE_NAME)
        plt.clf()
