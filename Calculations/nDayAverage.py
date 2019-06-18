import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def moving_average(days):
    return sum(days)/ len(days)

def last_N_days(days, index, N):
    return days[index-(N-1):index]

def generate_file(lines, stock_name, days, picture_name):
    N = days
    line_count = 0
    dates = []
    real = []
    lines.pop(0)
    for line in lines:
        items = line.split(",")
        if line_count > 0 and len(items)== 7 and items[4] != "null":
            real.append(float(items[4]))
            dates.append(items[0])
        line_count += 1
            
    average = np.convolve(real, np.ones((N,))/N, mode='valid')

    my_average = []
    for index, item in enumerate(real):
        if index > N-2:
            my_average.append(moving_average(last_N_days(real, index, N)))
        else:
            my_average.append(real[index])
    #filename = file.split("/")[-1:][0]
    filename = stock_name
    plt.title(filename)
    plt.plot(my_average)
    plt.plot(real)
    plt.legend([str(N) + ' päeva keskmine', 'reaalne'],loc='upper left')
    ##plt.show()
    plt.savefig(picture_name)
    plt.clf()
