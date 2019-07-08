import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def moving_average(days):
    return sum(days)/ len(days)

def last_N_days(days, index, N):
    return days[index-(N-1):index]

def generate_file(lines, stock_name, days, picture_name):
    line_count = 0
    dates = []
    real = []
    lines.pop(0)
    for line in lines:
        items = line.split(",")
        if line_count > 0 and len(items) == 7 and items[4] != "null":
            real.append(float(items[4]))
            dates.append(items[0])
        line_count += 1

    average = []
    for index, item in enumerate(real):
        if index > days-2:
            average.append(moving_average(last_N_days(real, index, days)))
        else:
            average.append(real[index])
    filename = stock_name
    plt.title(filename)
    plt.plot(average)
    plt.plot(real)
    plt.legend([str(days) + ' päeva keskmine', 'reaalne'], loc='upper left')
    plt.savefig(picture_name)
    plt.clf()
