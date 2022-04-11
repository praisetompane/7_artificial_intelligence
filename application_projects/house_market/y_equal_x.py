'''
    current_plt = current plot being used
    m = slope
'''


def straight_line(current_plt, m):
    x_values = [x for x in range(10)]
    y_values = [y*m for y in x_values]

    current_plt.plot(x_values, y_values)
