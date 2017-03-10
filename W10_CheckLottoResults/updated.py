import pandas as pd
import numpy as np

def getLotto():
    url = "http://www.national-lottery.co.uk/results/lotto/draw-history/csv"
    data = pd.read_csv(url)
    columns = data.iloc[:, 7:8]
    makeCalculations(columns)


def makeCalculations(array):
    r = np.array([1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7])

    print("mean", np.mean(array))
    print("std", np.std(array))


def main():
    getLotto()

main()
