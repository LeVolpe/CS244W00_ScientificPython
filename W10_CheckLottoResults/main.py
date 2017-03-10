import pandas as pd

def getLotto():
    url = "http://www.national-lottery.co.uk/results/lotto/draw-history/csv"
    print(pd.read_csv(url, sep="\t", na_values="."))


def main():
    getLotto()

main()


