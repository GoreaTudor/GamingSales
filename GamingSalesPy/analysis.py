import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    raw_data = pd.read_csv('.\\data\\vgsales.csv')

    print("\nHow data looks in table:")
    print(raw_data.head())

    print("\nSome statistical description:")
    print(raw_data.describe())

    print("\nColumns info:")
    print(raw_data.info())

    print("Shape (before cleanup):", raw_data.shape)
    data = raw_data.dropna()
    print("Shape (after cleanup):", data.shape)

