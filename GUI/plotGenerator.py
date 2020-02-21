import matplotlib.pyplot as plt
from Variables.variables import *


class PlotGenerator():
    def __init__(self, moving_average, growth):
        self.moving_average = moving_average
        self.growth = growth
        self.closing_prices = None
        self.axis_labels = None

    def create_image(self, stock_name, days, closing_prices, axis_labels, recalculate):
        if not recalculate:
            self.closing_prices = closing_prices
            self.axis_labels = axis_labels
        average_prices = self.moving_average.get_average_prices(self.closing_prices, days)

        plt.title(self.compose_title(stock_name, closing_prices[0], closing_prices[-1]))
        plt.plot(average_prices)
        plt.plot(self.closing_prices)
        self.set_labels(plt)
        plt.legend([str(days) + ' päeva jooksev keskmine', 'reaalne'], loc='upper left')
        plt.savefig(DEFAULT_PICTURE_NAME)
        plt.clf()

    def set_labels(self, plt):
        step_amount = int(len(self.closing_prices) / (DEFAULT_LABEL_AMOUNT * 2))
        indexes = []
        for i in range(1, DEFAULT_LABEL_AMOUNT * 2, 2):
            indexes.append(step_amount * i)
        plt.xticks(indexes, self.extract_labels(indexes, self.axis_labels))

    def extract_labels(self, indexes, all_labels):
        labels = []
        for position in indexes:
            labels.append(all_labels[position])
        return labels

    def compose_title(self, name, start_price, end_price):
        first_day_price = self.closing_prices[0]
        last_day_price = self.closing_prices[len(self.closing_prices) - 1]
        growth = self.growth.get_growth(first_day_price, last_day_price)
        return str(name) + "\n" + str(growth) + "%" + " | " + str(start_price) + "/" + str(end_price)