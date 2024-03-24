from repository import Repository
from printer import *
from constants import *


def setup(shouldPrint):
    raw_data = repo.get_all_sales()
    data = raw_data.dropna()

    if shouldPrint:
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


def run_counts():
    print("DA")


def run_correlations(year_sales, genre_sales, platform_sales, publisher_sales):
    # Correlation between Year and Global Sales
    if year_sales:
        p_year_sales = repo.get_group_sum(YEAR, GLOBAL_SALES)
        print_correlation_barchart(p_year_sales, YEAR, GLOBAL_SALES)

    # Correlation between Genre and Global Sales
    if genre_sales:
        p_genre_sales = repo.get_group_sum(GENRE, GLOBAL_SALES)
        print_correlation_barchart(p_genre_sales, GENRE, GLOBAL_SALES)

    # Correlation between Platform and Global Sales
    if platform_sales:
        p_platform_sales = repo.get_group_sum(PLATFORM, GLOBAL_SALES)
        print_correlation_barchart(p_platform_sales, PLATFORM, GLOBAL_SALES)

    # Correlation between Publisher and Global Sales
    if publisher_sales:
        p_publisher_sales = repo.get_group_sum(PUBLISHER, GLOBAL_SALES).head(20)
        print_correlation_barchart(p_publisher_sales, PUBLISHER, GLOBAL_SALES)


if __name__ == '__main__':
    repo = Repository()
    setup(shouldPrint=False)

    run_correlations(year_sales=True,
                     genre_sales=True,
                     platform_sales=True,
                     publisher_sales=True)

