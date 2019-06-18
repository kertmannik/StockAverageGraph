import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def moving_average(days):
    return sum(days)/ len(days)

def last_N_days(days, index, N):
    return days[index-(N-1):index]

def generate_file(file, days, picture_name):
    N = days
    my_average = []
    real = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        dates = []
        real = []
        for index, item in enumerate(csv_reader):
            if line_count > 0 and item[4] != "null":
                real.append(float(item[4]))
                dates.append(item[0])
            line_count += 1
            
    average = np.convolve(real, np.ones((N,))/N, mode='valid')

    my_average = []
    for index, item in enumerate(real):
        if index > N-2:
            my_average.append(moving_average(last_N_days(real, index, N)))
        else:
            my_average.append(real[index])
    filename = file.split("/")[-1:][0]
    plt.title(filename)
    plt.plot(my_average)
    plt.plot(real)
    plt.legend([str(N) + ' päeva keskmine', 'reaalne'],loc='upper left')
    ##plt.show()
    plt.savefig(picture_name)
    plt.clf()
