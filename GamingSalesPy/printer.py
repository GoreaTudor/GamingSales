import matplotlib.pyplot as plt


color = 'skyblue'


def print_barchart(data, x_axis, y_axis):
    plt.figure(figsize=(10, 6))
    plt.bar(data[x_axis], data[y_axis], color=color)
    plt.title('Correlation between ' + x_axis + ' and ' + y_axis)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()


def print_plot(data, x_axis, y_axis):
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_axis], data[y_axis], color=color)
    plt.title('Correlation between ' + x_axis + ' and ' + y_axis)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.xticks(rotation=45, ha='right')
    plt.show()
