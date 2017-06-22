import matplotlib.pyplot as plt
import numpy as np


def get_data():
    data = np.random.normal(size=1000)

    return data


def make_plot(data):
    plt.hist(data)
    plt.xlabel('Value')
    plt.ylabel('Counts')


if __name__ == '__main__':
    data = get_data()
    make_plot(data)

    # Execute this to see the plots
    plt.show()
