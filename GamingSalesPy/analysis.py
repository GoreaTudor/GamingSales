from repository import Repository
from printer import *
from constants import *
import pandas as pd


def run_setup():
    raw_data = pd.read_csv(PATH)
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


def run_counts(genre, platform, publisher, game):
    if genre:
        print('Count of', GENRE, ':', repo.select_distinct(GENRE))

    if platform:
        print('Count of', PLATFORM, ':', repo.select_distinct(PLATFORM))

    if publisher:
        print('Count of', PUBLISHER, ':', repo.select_distinct(PUBLISHER))

    if game:
        print('Count of', NAME, ':', repo.select_distinct(NAME))


def run_sales_correlations(function, should_filter, year, genre, platform, publisher):
    # Correlation between Year and Global Sales
    if year:
        p_year_sales = repo.group_by_sum(YEAR, GLOBAL_SALES, should_filter)
        function(p_year_sales, YEAR, GLOBAL_SALES)

    # Correlation between Genre and Global Sales
    if genre:
        p_genre_sales = repo.group_by_sum(GENRE, GLOBAL_SALES, should_filter)
        function(p_genre_sales, GENRE, GLOBAL_SALES)

    # Correlation between Platform and Global Sales
    if platform:
        p_platform_sales = repo.group_by_sum(PLATFORM, GLOBAL_SALES, should_filter)
        function(p_platform_sales, PLATFORM, GLOBAL_SALES)

    # Correlation between Publisher and Global Sales
    if publisher:
        p_publisher_sales = repo.group_by_sum(PUBLISHER, GLOBAL_SALES, should_filter).head(30)
        function(p_publisher_sales, PUBLISHER, GLOBAL_SALES)


def run_games_correlations(function, should_filter, year, genre, platform, publisher):
    # Correlation between Year and Global Sales
    if year:
        p_year_games = repo.group_by_count(YEAR, NAME, should_filter)
        function(p_year_games, YEAR, NR_OF_GAMES)

    # Correlation between Genre and Global Sales
    if genre:
        p_genre_games = repo.group_by_count(GENRE, NAME, should_filter)
        function(p_genre_games, GENRE, NR_OF_GAMES)

    # Correlation between Platform and Global Sales
    if platform:
        p_platform_games = repo.group_by_count(PLATFORM, NAME, should_filter)
        function(p_platform_games, PLATFORM, NR_OF_GAMES)

    # Correlation between Publisher and Global Sales
    if publisher:
        p_publisher_games = repo.group_by_count(PUBLISHER, NAME, should_filter).head(30)
        function(p_publisher_games, PUBLISHER, NR_OF_GAMES)


def run_label_correlations(platform_genre, genre_publisher, platform_publisher):
    # What is the main Genre for each Platform
    if platform_genre:
        p_platform_genre = repo.group_by_count_max(PLATFORM, GENRE)
        print("\nWhat is the main Genre for each Platform:")
        print(p_platform_genre)

    # What is the main Publisher for each Genre
    if genre_publisher:
        p_genre_publisher = repo.group_by_count_max(GENRE, PUBLISHER)
        print("\nWhat is the main Publisher for each Genre:")
        print(p_genre_publisher)

    # What is the main Publisher for each Platform
    if platform_publisher:
        p_platform_publisher = repo.group_by_count_max(PLATFORM, PUBLISHER)
        print("\nWhat is the main Publisher for each Platform:")
        print(p_platform_publisher)


def run_specific_queries(games_by_platforms, games_by_genre):
    # Get Nr of Games for each platform, where publisher is Bethesda
    if games_by_platforms:
        p_init = repo.get_all_sales()
        p_filtered = p_init.loc[p_init[PUBLISHER] == BETHESDA]
        p_bethesda = (p_filtered.groupby(PLATFORM)
                      .count()
                      .sort_values(by=PUBLISHER, ascending=False))
        print("\nNr of Games for each Platform, where Publisher is Bethesda")
        print(p_bethesda[PUBLISHER])

    # Get Nr of Games for each genre, where publisher is Bethesda
    if games_by_genre:
        p_init = repo.get_all_sales()
        p_filtered = p_init.loc[(p_init[PUBLISHER] == BETHESDA) &
                                (p_init[YEAR] >= 2010)]
        p_bethesda = (p_filtered.groupby(GENRE)
                      .count()
                      .sort_values(by=PUBLISHER, ascending=False))
        print("\nNr of Games for each Genre, where publisher is Bethesda and year >= 2010")
        print(p_bethesda[PUBLISHER])


def run_time_series():
    # Predict Global Sales based on Year.
    result = repo.time_series()

    plt.figure(figsize=(12, 6))
    result.plot(kind='line', color='skyblue')
    plt.title('Global Sales of Video Games Over Time')
    plt.xlabel('Year')
    plt.ylabel('Global Sales (millions)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def runner(setup, counts, sales_correlations, games_correlations, label_correlations, specific_queries, time_series):
    if setup:
        run_setup()

    if counts:
        run_counts(genre=True,
                   platform=True,
                   publisher=True,
                   game=True,
                   )

    if sales_correlations:
        run_sales_correlations(function=print_barchart,
                               should_filter=False,
                               year=True,
                               genre=True,
                               platform=True,
                               publisher=True,
                               )
        run_sales_correlations(function=print_barchart,
                               should_filter=True,
                               year=True,
                               genre=True,
                               platform=True,
                               publisher=True,
                               )

    if games_correlations:
        run_games_correlations(function=print_barchart,
                               should_filter=False,
                               year=True,
                               genre=True,
                               platform=True,
                               publisher=True,
                               )
        run_games_correlations(function=print_barchart,
                               should_filter=True,
                               year=True,
                               genre=True,
                               platform=True,
                               publisher=True,
                               )

    if label_correlations:
        run_label_correlations(platform_genre=True,
                               genre_publisher=True,
                               platform_publisher=True,
                               )

    if specific_queries:
        run_specific_queries(games_by_platforms=True,
                             games_by_genre=True,
                             )
    if time_series:
        run_time_series()


if __name__ == '__main__':
    repo = Repository()
    runner(
        setup=False,
        counts=False,
        sales_correlations=False,
        games_correlations=False,
        label_correlations=True,
        specific_queries=False,
        time_series=False,
    )
