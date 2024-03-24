from constants import *

import pandas as pd


class Repository:
    def __init__(self):
        self._db = pd.read_csv(PATH).dropna()

    def get_all_sales(self):
        return self._db

    def select_distinct(self, key, ascending=False):
        return (self._db
                .drop_duplicates([key])
                .sort_values(by=key, ascending=ascending)[key]
                .count())

    def group_by_sum(self, x_axis, y_axis):
        return (self._db
                .groupby(x_axis)
                .sum()
                .reset_index()
                .sort_values(by=y_axis, ascending=False))

    def group_by_count(self, x_axis, y_axis):
        return (self._db
                .groupby(x_axis)
                [y_axis]
                .agg(lambda x: x.value_counts().idxmax()))


if __name__ == '__main__':
    repo = Repository()
    sales = repo.get_all_sales()

    print(sales[PUBLISHER])
