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
    reg = str(round(a, 2))+" * x + " + str(round(b, 2))

    plt.figure(figsize=(9, 6))
    plt.plot(x, y, 'ro')
    plt.plot(x, regline)
    plt.grid(True)

    section = np.linspace(start=min(x), stop=max(x), num=100)
    plt.plot(section, section * a + b)
    print('The Pearson correlation coefficient = ' + str(round(r, 2)))
    print('The regression line =' + str(reg))


    plt.xlabel (str(xla).upper())
    plt.ylabel (str(yla).upper())

    plt.tight_layout(0,2)
    plt.show()
    plt.savefig(plot())

plot()