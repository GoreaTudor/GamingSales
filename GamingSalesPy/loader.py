import pandas as pd


def load_data():
    sales = pd.read_csv('.\\data\\vgsales.csv')
    print(sales)


def get_headers():
    pass


if __name__ == '__main__':
    print("TEST")
    load_data()

# TODO (when presenting):
#  0. SAY UR NAME
#  1. upload to sql db
#  2. connect to db, use env file for secrets
