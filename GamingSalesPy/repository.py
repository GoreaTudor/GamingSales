from constants import *

import pandas as pd


class Repository:
    def __init__(self):
        self._db = pd.read_csv(PATH)

    def get_all_sales(self):
        return self._db

    def get_unique_count(self, key):
        return (self._db
                .drop_duplicates([key])
                .size())

    def get_group_sum(self, group_name, result, ascending=False):
        return (self._db
                .groupby(group_name)
                .sum()
                .reset_index()
                .sort_values(by=result, ascending=ascending))


if __name__ == '__main__':
    repo = Repository()
    sales = repo.get_all_sales()

    print(sales[PUBLISHER])
