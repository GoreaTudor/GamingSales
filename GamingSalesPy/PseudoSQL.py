from constants import *
from repository import Repository


if __name__ == '__main__':
    repo = Repository()
    sales = repo.get_all_sales()

    print("\nSelect")
    proj = sales[[NAME, YEAR, PLATFORM]]
    print(proj)

    print("\nSelect Distinct")
    print(sales.drop_duplicates([PUBLISHER])[PUBLISHER])

    print("\nLimit")
    print(proj.head(10))  # First elements
    print(proj.tail(10))  # Last elements

    print("\nFilter")
    print(proj.loc[proj[YEAR] <= 2010])
    print(proj.loc[
              ~(proj[PLATFORM] == 'PC') &
              (proj[YEAR] >= 2010) |
              (proj[YEAR] == 2007)]
          .head(20))

    print("\nGroup By")
    print(proj.groupby([PLATFORM]).size())
    print(">>> PC", proj.groupby([PLATFORM]).size()['PC'])

    ####################
    # TESTING QUERIES: #
    ####################

    print("\n\nBethesda's Unique Game Launches")
    # SELECT DISTINCT Name, Publisher
    # FROM vgsales
    # WHERE Publisher = 'Bethesda Softworks'
    uq = sales.drop_duplicates([NAME])
    uq_filtered = uq.loc[uq[PUBLISHER] == BETHESDA]
    print(uq_filtered[[NAME, PUBLISHER]])
