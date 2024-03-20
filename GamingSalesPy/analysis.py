from repository import Repository

if __name__ == '__main__':
    repo = Repository()
    raw_data = repo.get_all_sales()

    print("\nHow data looks in table:")
    print(raw_data.head())

    print("\nSome statistical description:")
    print(raw_data.describe())

    print("\nColumns info:")
    print(raw_data.info())

    print("\nShape (before cleanup):", raw_data.shape)
    data = raw_data.dropna()
    print("Shape (after cleanup):", data.shape)
