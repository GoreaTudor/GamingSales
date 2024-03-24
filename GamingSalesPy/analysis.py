from repository import Repository
from printer import *
from constants import *


def run_setup():
    raw_data = repo.get_all_sales()
    data = raw_data.dropna()

    print("\nHow data looks in table:")
    print(raw_data.head())

    print("\nSome statistical description:")
    print(raw_data.describe())

    print("\nColumns info:")
    print(raw_data.info())

    print("\nNull values:")
    print(raw_data.isnull().sum())

    print("\nShape (before cleanup):", raw_data.shape)
    print("Shape (after cleanup):", data.shape)

    return data


def run_counts(year_sales, genre_sales, platform_sales, publisher_sales):
    if year_sales:
        print('Count of', YEAR, ':', repo.get_unique_count(YEAR))

    if genre_sales:
        print('Count of', GENRE, ':', repo.get_unique_count(GENRE))

    if platform_sales:
        print('Count of', PLATFORM, ':', repo.get_unique_count(PLATFORM))

    if publisher_sales:
        print('Count of', PUBLISHER, ':', repo.get_unique_count(PUBLISHER))


def run_correlations(function, year_sales, genre_sales, platform_sales, publisher_sales):
    # Correlation between Year and Global Sales
    if year_sales:
        p_year_sales = repo.get_group_sum(YEAR, GLOBAL_SALES)
        function(p_year_sales, YEAR, GLOBAL_SALES)

    # Correlation between Genre and Global Sales
    if genre_sales:
        p_genre_sales = repo.get_group_sum(GENRE, GLOBAL_SALES)
        function(p_genre_sales, GENRE, GLOBAL_SALES)

    # Correlation between Platform and Global Sales
    if platform_sales:
        p_platform_sales = repo.get_group_sum(PLATFORM, GLOBAL_SALES)
        function(p_platform_sales, PLATFORM, GLOBAL_SALES)

    # Correlation between Publisher and Global Sales
    if publisher_sales:
        p_publisher_sales = repo.get_group_sum(PUBLISHER, GLOBAL_SALES).head(30)
        function(p_publisher_sales, PUBLISHER, GLOBAL_SALES)


def runner(setup, counts, correlations):
    if setup:
        run_setup()

    if counts:
        run_counts(year_sales=True,
                   genre_sales=True,
                   platform_sales=True,
                   publisher_sales=True)

    if correlations:
        run_correlations(function=print_barchart,
                         year_sales=True,
                         genre_sales=True,
                         platform_sales=True,
                         publisher_sales=True)


if __name__ == '__main__':
    repo = Repository()
    runner(
        setup=False,
        counts=False,
        correlations=True,
    )
