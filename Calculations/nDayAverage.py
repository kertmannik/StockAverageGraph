import matplotlib.pyplot as plt


def moving_average(days):
    return sum(days) / len(days)


def last_n_days(days, index, N):
    return days[index-(N-1):index]


def generate_file(lines, stock_name, days, picture_name):
    dates = []
    real = []
    lines.pop(0)

    for line in lines:
        items = line.split(",")
        if len(items) == 7 and items[4] != "null":
            real.append(float(items[4]))
            dates.append(items[0])

    average = []
    for index, item in enumerate(real):
        if index > days - 2:
            average.append(moving_average(last_n_days(real, index, days)))
        else:
            average.append(real[index])

    plt.title(stock_name)
    plt.plot(average)
    plt.plot(real)
    plt.legend([str(days) + ' päeva jooksev keskmine', 'reaalne'], loc='upper left')
    plt.savefig(picture_name)
    plt.clf()
