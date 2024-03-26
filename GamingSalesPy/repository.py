from constants import *

import pandas as pd


class Repository:
    def __init__(self):
        self._db = pd.read_csv(PATH).dropna()

    # SELECT *
    # FROM vgsales
    def get_all_sales(self):
        return self._db

    # SELECT DISTINCT COUNT(:key)
    # FROM vgsales
    # ORDER BY :key DESC
    def select_distinct(self, key, ascending=False):
        return (self._db
                .drop_duplicates([key])
                .sort_values(by=key, ascending=ascending)
                [key]
                .count())

    # SELECT COUNT(:y_axis) as Nr_of_Games
    # FROM vgsales
    # (WHERE Year BETWEEN :min AND :max)  -  OPTIONAL
    # GROUP BY :x_axis
    # ORDER BY Nr_of_Games
    def group_by_count(self, x_axis, y_axis, should_filter=False):
        init = self._db

        if should_filter:
            result = init.loc[(init[YEAR] >= RANGE_MIN) &
                              (init[YEAR] <= RANGE_MAX)]
        else:
            result = init

        return (result
                .groupby(x_axis)
                [y_axis]
                .size()
                .reset_index(name=NR_OF_GAMES)
                .sort_values(by=NR_OF_GAMES, ascending=False))

    # SELECT SUM(*)
    # FROM vgsales
    # (WHERE Year BETWEEN :min AND :max)  -  OPTIONAL
    # GROUP BY :x_axis
    # ORDER BY :y_axis DESC
    def group_by_sum(self, x_axis, y_axis, should_filter=False):
        init = self._db

        if should_filter:
            result = init.loc[(init[YEAR] >= RANGE_MIN) &
                              (init[YEAR] <= RANGE_MAX)]
        else:
            result = init

        return (result
                .groupby(x_axis)
                .sum()
                .reset_index()
                .sort_values(by=y_axis, ascending=False))

    # SELECT MAX(COUNT(:y_axis))
    # FROM vgsales
    # GROUP BY :x_axis
    def group_by_count_max(self, x_axis, y_axis):
        return (self._db
                .groupby(x_axis)
                [y_axis]
                .agg(lambda x: x.value_counts().idxmax()))

    # SELECT SUM(Global_Sales)
    # FROM vgsales
    # GROUP BY Year
    def time_series(self):
        return (self._db
                .groupby(YEAR)
                [GLOBAL_SALES]
                .sum())


# TODO:
#  find difference between: count(), value_counts() and size()
