from constants import *

import pandas as pd


class Repository:
    def __init__(self):
        self._db = pd.read_csv(PATH).dropna()

    def get_all_sales(self):
        return self._db

    def get_unique_count(self, key, ascending=False):
        return (self._db
                .drop_duplicates([key])
                .sort_values(by=key, ascending=ascending)[key]
                .count())

    def get_group_sum(self, x_axis, y_axis):
        return (self._db
                .groupby(x_axis)
                .sum()
                .reset_index()
                .sort_values(by=y_axis, ascending=False))

    def get_filtered_sum(self):
        return (self._db)


if __name__ == '__main__':
    repo = Repository()
    sales = repo.get_all_sales()

    print(sales[PUBLISHER])
