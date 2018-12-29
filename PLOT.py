import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress as lr

def plot():
    file = np.loadtxt(input('Enter your file : '))

    xla = input ('Enter name of xlabel')
    yla = input('Enter name of ylabel')

    x = file[:, 0]
    y = file[:, 1]

    a, b, r, _, da = lr(x, y)
    regline = a*x + b

    plt.figure(figsize=(5, 3))
    plt.plot(x, y, 'ro')
    plt.plot(x, regline)
    plt.grid(True)

    section = np.linspace(start=min(x), stop=max(x), num=100)
    plt.plot(section, section * a + b, label="regression line, a = {0}, b = {1}".format(a, b))
    print('The Pearson correlation coefficient = ' + str(round(r, 2)))

    plt.xlabel (str(xla).upper())
    plt.ylabel (str(yla).upper())

    plt.legend()
    plt.tight_layout(0,2)
    plt.show()

plot()