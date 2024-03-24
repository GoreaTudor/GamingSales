import matplotlib.pyplot as plt


def print_correlation_barchart(data, x_axis, y_axis):
    plt.figure(figsize=(12, 6))
    plt.bar(data[x_axis], data[y_axis], color='skyblue')
    plt.title('Correlation between ' + x_axis + ' and ' + y_axis)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

