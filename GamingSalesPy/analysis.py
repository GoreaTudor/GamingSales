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
        print('Count of', YEAR, ':', repo.select_distinct(YEAR))

    if genre_sales:
        print('Count of', GENRE, ':', repo.select_distinct(GENRE))

    if platform_sales:
        print('Count of', PLATFORM, ':', repo.select_distinct(PLATFORM))

    if publisher_sales:
        print('Count of', PUBLISHER, ':', repo.select_distinct(PUBLISHER))


def run_numeric_correlations(function, year_sales, genre_sales, platform_sales, publisher_sales):
    # Correlation between Year and Global Sales
    if year_sales:
        p_year_sales = repo.group_by_sum(YEAR, GLOBAL_SALES)
        function(p_year_sales, YEAR, GLOBAL_SALES)

    # Correlation between Genre and Global Sales
    if genre_sales:
        p_genre_sales = repo.group_by_sum(GENRE, GLOBAL_SALES)
        function(p_genre_sales, GENRE, GLOBAL_SALES)

    # Correlation between Platform and Global Sales
    if platform_sales:
        p_platform_sales = repo.group_by_sum(PLATFORM, GLOBAL_SALES)
        function(p_platform_sales, PLATFORM, GLOBAL_SALES)

    # Correlation between Publisher and Global Sales
    if publisher_sales:
        p_publisher_sales = repo.group_by_sum(PUBLISHER, GLOBAL_SALES).head(30)
        function(p_publisher_sales, PUBLISHER, GLOBAL_SALES)


def run_label_correlations(platform_genre, genre_publisher, platform_publisher):
    # What is the main Genre for each Platform
    if platform_genre:
        p_platform_genre = repo.group_by_count(PLATFORM, GENRE)
        print("\nWhat is the main Genre for each Platform:")
        print(p_platform_genre)

    # What is the main Publisher for each Genre
    if genre_publisher:
        p_genre_publisher = repo.group_by_count(GENRE, PUBLISHER)
        print("\nWhat is the main Publisher for each Genre:")
        print(p_genre_publisher)

    # What is the main Publisher for each Platform
    if platform_publisher:
        p_platform_publisher = repo.group_by_count(PLATFORM, PUBLISHER)
        print("\nWhat is the main Publisher for each Platform:")
        print(p_platform_publisher)


def run_specific_queries(games_by_platforms):
    publisher = 'Bethesda Softworks'

    # Get Nr of Games for each platform, where publisher is Bethesda
    if games_by_platforms:
        p_init = repo.get_all_sales()
        p_filtered = p_init.loc[p_init[PUBLISHER] == publisher]
        p_bethesda = (p_filtered.groupby(PLATFORM)
                      .count()
                      .sort_values(by=PUBLISHER, ascending=False))
        print(p_bethesda[PUBLISHER])


def runner(setup, counts, numeric_correlations, label_correlations, specific_queries):
    if setup:
        run_setup()

    if counts:
        run_counts(year_sales=True,
                   genre_sales=True,
                   platform_sales=True,
                   publisher_sales=True,
                   )

    if numeric_correlations:
        run_numeric_correlations(function=print_barchart,
                                 year_sales=True,
                                 genre_sales=True,
                                 platform_sales=True,
                                 publisher_sales=True,
                                 )

    if label_correlations:
        run_label_correlations(platform_genre=True,
                               genre_publisher=True,
                               platform_publisher=True,
                               )

    if specific_queries:
        run_specific_queries(games_by_platforms=True,
                             )


if __name__ == '__main__':
    repo = Repository()
    runner(
        setup=False,
        counts=False,
        numeric_correlations=False,
        label_correlations=True,
        specific_queries=False,
    )
