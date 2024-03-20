from constants import *

import pandas as pd


class Repository:
    def __init__(self):
        self._db = pd.read_csv(PATH)

    def get_all_sales(self):
        return self._db


if __name__ == '__main__':
    repo = Repository()
    sales = repo.get_all_sales()

    print(sales[PUBLISHER])
