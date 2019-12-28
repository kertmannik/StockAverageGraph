class MovingAverage:
    def moving_average(self, days):
        return sum(days) / len(days)

    def last_n_days(self, days, index, N):
        return days[index-(N-1):index]

    def get_average_prices(self, real, days):
        average = []
        for index, item in enumerate(real):
            if index > days - 2:
                average.append(self.moving_average(self.last_n_days(real, index, days)))
            else:
                average.append(real[index])
        return average
