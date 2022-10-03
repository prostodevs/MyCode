#!/usr/bin/env python3
""" Alta3 | J Stowe
    Pie Chart Test """

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')


def main():

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Cheese', 'Pepperoni', 'Mushrooms', 'Sausage', 'Green Peppers', 'Olives'
    sizes = [35, 25, 5, 10, 16, 9]
    # "explode" the 1st and 2nd slice (i.e. 'Cheese' and 'Pepperoni')
    explode = (0.2, 0.1, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')

    plt.title('Pizza Ratios') # simple title

    plt.savefig("/home/student/MyCode/graphing/pie_chart.png")


if __name__ == "__main__":
    main()
